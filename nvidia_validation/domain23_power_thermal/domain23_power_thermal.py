#!/usr/bin/env python3
"""
Domain 23: GPU Power & Thermal Efficiency

Measures:
- Average and peak GPU power (W)
- Total energy consumed (J)
- Temperature (°C)
- SM and memory utilization
- Graphics and memory clocks
- Power and thermal throttling
- Steps per joule (primary efficiency metric)

Uses NVML for power/energy/temperature, DCGM if available.
"""

import os
import sys
import json
import numpy as np
import time
from pathlib import Path

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain23_power_thermal")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import cupy_available

import cupy

def get_device_info():
    if not cupy_available():
        return {"available": False}
    dev = cupy.cuda.Device()
    props = cupy.cuda.runtime.getDeviceProperties(dev.id)
    return {
        "available": True,
        "device_id": dev.id,
        "name": props["name"].decode() if isinstance(props["name"], bytes) else props["name"],
        "compute_capability": f"{props['major']}.{props['minor']}",
        "total_memory": props["totalGlobalMem"],
    }

def get_nvml_handle():
    try:
        import pynvml
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        return pynvml, handle
    except Exception as e:
        return None, str(e)


def measure_power_temperature(pynvml, handle):
    """Read instantaneous power, temperature, clocks, utilization.
    Handles 'Not Supported' errors for laptop GPU NVML calls gracefully."""
    result = {"power_w": None, "temp_c": None, "gpu_util_pct": None, 
              "mem_util_pct": None, "sm_clock_mhz": None, "mem_clock_mhz": None,
              "power_limit_w": None, "errors": []}
    
    # Power measurement
    try:
        result["power_w"] = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
    except Exception as e:
        result["errors"].append(f"power: {e}")
    
    # Temperature
    try:
        result["temp_c"] = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
    except Exception as e:
        result["errors"].append(f"temp: {e}")
    
    # Utilization
    try:
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        result["gpu_util_pct"] = util.gpu
        result["mem_util_pct"] = util.memory
    except Exception as e:
        result["errors"].append(f"util: {e}")
    
    # Clocks
    try:
        result["sm_clock_mhz"] = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_SM)
    except Exception as e:
        result["errors"].append(f"sm_clock: {e}")
    
    try:
        result["mem_clock_mhz"] = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_MEM)
    except Exception as e:
        result["errors"].append(f"mem_clock: {e}")
    
    # Power limit
    try:
        result["power_limit_w"] = pynvml.nvmlDeviceGetPowerManagementLimit(handle) / 1000.0
    except Exception as e:
        result["errors"].append(f"power_limit: {e}")
    
    if result["errors"]:
        result["error"] = "; ".join(result["errors"]) + " (some telemetry unavailable)"
    
    return result


def measure_energy(pynvml, handle):
    """Read total energy consumption (J)."""
    try:
        if handle is None:
            return None
        energy_j = pynvml.nvmlDeviceGetTotalEnergyConsumption(handle) / 1000.0
        return energy_j
    except Exception as e:
        return None


def run_benchmark_with_telemetry(dimension, grid_size, steps, dtype=np.complex128, sample_interval=0.1):
    """Run evolution with periodic power/temperature sampling."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    pynvml, handle = get_nvml_handle()
    if pynvml is None:
        return {"error": f"NVML not available: {handle}"}
    
    # Build grid and solver
    if dimension == 1:
        grid = Grid1D(grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
    elif dimension == 2:
        grid = Grid2D(grid_size, -grid_size/2, grid_size/2, 
                      grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
    else:
        grid = Grid3D(grid_size, -grid_size/2, grid_size/2,
                      grid_size, -grid_size/2, grid_size/2,
                      grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction3D.gaussian(grid, 0,0,0, 0,0,0, 1.0, 1.0, 1.0)
    
    wf.psi = wf.psi.astype(dtype)
    V = None
    solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    
    # Initial telemetry
    initial_telemetry = measure_power_temperature(pynvml, handle)
    initial_energy = measure_energy(pynvml, handle)
    
    # Upload
    psi_dev = solver._upload(wf)
    
    # Warmup
    for _ in range(3):
        psi_dev = solver._advance(psi_dev)
    cupy.cuda.Stream.null.synchronize()
    
    # Sampling during evolution
    telemetry_samples = []
    energy_samples = []
    temps = []
    powers = []
    gpu_utils = []
    mem_utils = []
    
    start_time = time.time()
    psi = psi_dev
    
    for step in range(steps):
        step_start = time.time()
        psi = solver._advance(psi)
        cupy.cuda.Stream.null.synchronize()
        step_time = time.time() - step_start
        
        # Sample telemetry at interval
        if step % max(1, int(sample_interval / 0.01)) == 0:
            tel = measure_power_temperature(pynvml, handle)
            if tel.get("temp_c") is not None or tel.get("power_w") is not None:
                tel["step"] = step
                tel["step_time_s"] = step_time
                telemetry_samples.append(tel)
                if tel.get("temp_c") is not None:
                    temps.append(tel["temp_c"])
                if tel.get("power_w") is not None:
                    powers.append(tel["power_w"])
                if tel.get("gpu_util_pct") is not None:
                    gpu_utils.append(tel["gpu_util_pct"])
                if tel.get("mem_util_pct") is not None:
                    mem_utils.append(tel["mem_util_pct"])
            energy = measure_energy(pynvml, handle)
            if energy is not None:
                energy_samples.append({"step": step, "energy_j": energy})
    
    end_time = time.time()
    
    # Final telemetry
    final_telemetry = measure_power_temperature(pynvml, handle)
    final_energy = measure_energy(pynvml, handle)
    
    # Compute metrics
    total_time = end_time - start_time
    total_energy = final_energy - initial_energy if isinstance(final_energy, (int, float)) and isinstance(initial_energy, (int, float)) else None
    
    # Compute averages from samples
    avg_power = None
    avg_temp = None
    avg_gpu_util = None
    avg_mem_util = None
    if temps:
        avg_power = np.mean(powers) if powers else None
        avg_temp = np.mean(temps)
        avg_gpu_util = np.mean(gpu_utils) if gpu_utils else None
        avg_mem_util = np.mean(mem_utils) if mem_utils else None
    
    steps_per_joule = steps / total_energy if total_energy and total_energy > 0 else None
    energy_per_step = total_energy / steps if total_energy and total_energy > 0 else None
    
    return {
        "dimension": dimension,
        "grid_size": grid_size,
        "dtype": str(dtype),
        "n_steps": steps,
        "total_time_s": total_time,
        "total_energy_j": total_energy,
        "energy_per_step_j": energy_per_step,
        "steps_per_joule": steps_per_joule,
        "avg_power_w": avg_power,
        "avg_temp_c": avg_temp,
        "avg_gpu_util_pct": avg_gpu_util,
        "avg_mem_util_pct": avg_mem_util,
        "initial_telemetry": initial_telemetry,
        "final_telemetry": final_telemetry,
        "telemetry_samples": telemetry_samples,
        "energy_samples": energy_samples,
    }


def run_sustained_load_test(duration_s=30):
    """Run sustained load to test thermal throttling."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    pynvml, handle = get_nvml_handle()
    if pynvml is None:
        return {"error": f"NVML not available: {handle}"}
    
    # Large 3D workload for sustained load
    grid = Grid3D(128, -8.0, 8.0, 128, -8.0, 8.0, 128, -8.0, 8.0)
    wf = WaveFunction3D.gaussian(grid, 0,0,0, 0,0,0, 1.0, 1.0, 1.0)
    V = None
    solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    
    psi_dev = solver._upload(wf)
    for _ in range(3):
        psi_dev = solver._advance(psi_dev)
    cupy.cuda.Stream.null.synchronize()
    
    pynvml, handle = get_nvml_handle()
    telemetry_log = []
    start_time = time.time()
    
    while time.time() - start_time < duration_s:
        psi_dev = solver._advance(psi_dev)
        cupy.cuda.Stream.null.synchronize()
        
        tel = measure_power_temperature(pynvml, handle)
        tel["elapsed_s"] = time.time() - start_time
        telemetry_log.append(tel)
        time.sleep(0.1)  # Sample at 10 Hz
    
    # Analyze for throttling
    temps = []
    powers = []
    sm_clocks = []
    for t in telemetry_log:
        tc = t.get("temp_c")
        pw = t.get("power_w")
        sc = t.get("sm_clock_mhz")
        if tc is not None:
            temps.append(tc)
        if pw is not None:
            powers.append(pw)
        if sc is not None:
            sm_clocks.append(sc)
    
    throttling_detected = False
    if len(sm_clocks) > 10:
        clock_drop = (max(sm_clocks) - min(sm_clocks)) / max(sm_clocks) * 100
        throttling_detected = clock_drop > 5  # >5% clock drop suggests throttling
    
    return {
        "duration_s": duration_s,
        "telemetry_log": telemetry_log,
        "temp_range_c": {"min": min(temps), "max": max(temps), "avg": np.mean(temps)} if temps else None,
        "power_range_w": {"min": min(powers), "max": max(powers), "avg": np.mean(powers)} if powers else None,
        "sm_clock_range_mhz": {"min": min(sm_clocks), "max": max(sm_clocks), "avg": np.mean(sm_clocks)} if sm_clocks else None,
        "throttling_detected": throttling_detected,
        "clock_drop_pct": (max(sm_clocks) - min(sm_clocks)) / max(sm_clocks) * 100 if sm_clocks else None,
    }


def main():
    print("=" * 70)
    print("DOMAIN 23: GPU Power & Thermal Efficiency")
    print("=" * 70)
    
    dev_info = get_device_info()
    print(f"Device: {json.dumps(dev_info, indent=2)}")
    
    if not cupy_available():
        print("CuPy not available - skipping")
        return
    
    pynvml, handle = get_nvml_handle()
    if pynvml is None:
        print(f"NVML not available: {handle}")
        print("Install pynvml: pip install pynvml")
        return
    
    print("NVML initialized successfully")
    
    all_results = {
        "device": get_device_info(),
        "nvml_available": True,
        "benchmarks": {},
        "sustained_load": {},
    }
    
    # Test configurations
    configs = [
        (1, 8192, 100),   # 1D long evolution
        (2, 512, 50),     # 2D medium
        (3, 128, 20),     # 3D medium
        (3, 256, 10),     # 3D large (high memory)
    ]
    
    for dim, size, steps in configs:
        print(f"\n>>> {dim}D {size}^{dim}, {steps} steps")
        try:
            result = run_benchmark_with_telemetry(dim, size, steps)
            all_results["benchmarks"][f"{dim}D_{size}^{dim}"] = result
            print(f"  Steps: {steps}, Time: {result.get('total_time_s', 'N/A'):.2f}s" if result.get('total_time_s') is not None else '  Steps: N/A')
            print(f"  Energy: {result.get('total_energy_j', 'N/A'):.3f} J" if result.get('total_energy_j') is not None else '  Energy: N/A')
            print(f"  Steps/J: {result.get('steps_per_joule', 'N/A'):.1f}" if result.get('steps_per_joule') is not None else '  Steps/J: N/A')
            print(f"  Avg Power: {result.get('avg_power_w', 'N/A'):.1f} W" if result.get('avg_power_w') is not None else '  Avg Power: N/A')
            print(f"  Avg Temp: {result.get('avg_temp_c', 'N/A'):.1f} °C" if result.get('avg_temp_c') is not None else '  Avg Temp: N/A')
            print(f"  GPU Util: {result.get('avg_gpu_util_pct', 'N/A'):.1f}%" if result.get('avg_gpu_util_pct') is not None else '  GPU Util: N/A')
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            all_results["benchmarks"][f"{dim}D_{size}^{dim}"] = {"error": str(e)}
    
    # Sustained load test
    print("\n>>> Sustained load test (30s)")
    try:
        result = run_sustained_load_test(30)
        all_results["sustained_load"] = result
        print(f"  Throttling: {result.get('throttling_detected', 'N/A')}")
        print(f"  Temp range: {result.get('temp_range_c', 'N/A')}")
        print(f"  Power range: {result.get('power_range_w', 'N/A')}")
        print(f"  Clock drop: {result.get('clock_drop_pct', 'N/A'):.1f}%" if result.get('clock_drop_pct') is not None else '  Clock drop: N/A')
    except Exception as e:
        print(f"  ERROR: {e}")
        all_results["sustained_load"] = {"error": str(e)}
    
    # Save results
    def convert(obj):
        if isinstance(obj, (np.bool_, np.integer, np.floating)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert(v) for v in obj]
        return obj
    
    output = {
        "device": get_device_info(),
        "timestamp": "2026-11-21",
        "results": convert(all_results),
    }
    
    out_file = os.path.join(OUT, "domain23_power_thermal.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved: {out_file}")
    print("Done.")


if __name__ == "__main__":
    import cupy
    main()