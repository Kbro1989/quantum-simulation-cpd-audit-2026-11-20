#!/usr/bin/env python3
"""
Domain 21: GPU Numerical Precision & Zero-Floor Integrity

Extends the CPU zero-floor taxonomy (Domain 17) to GPU execution.
Tests:
- Complex64 vs Complex128 precision
- IEEE-754 normal vs subnormal handling
- Underflow to zero behavior
- NaN/Inf propagation on GPU
- GPU-specific flush-to-zero behavior
- Vortex core density precision
- Phase winding near numerical zeros
- Norm/energy conservation on GPU vs CPU
"""

import os
import sys
import json
import numpy as np
import time
from pathlib import Path

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain21_precision_zero_floor")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid2D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.observables.current import vortex_positions
from quantumlab.observables.expectation import total_energy_expectation, position_expectation, momentum_expectation
from quantumlab.solvers.backends import get_backend, cupy_available

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
    }

def test_precision_modes():
    """Test complex64 vs complex128 on GPU."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    results = {}
    grid = Grid1D(256, -8.0, 8.0)
    V = HarmonicOscillator(omega=1.0, m=1.0)
    
    for dtype_name, dtype in [("complex64", np.complex64), ("complex128", np.complex128)]:
        solver = SplitOperatorSolver(
            grid, V, 0.01, hbar=1.0, m=1.0, 
            backend='cupy', device_id=0
        )
        
        psi0 = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
        # Convert to target precision
        psi0.psi = psi0.psi.astype(dtype)
        
        # Evolve
        psi = solver.evolve(psi0, 100)
        
        # Check precision
        norm = np.sum(np.abs(psi.psi)**2) * grid.dx
        energy = total_energy_expectation(psi, V, hbar=1.0, m=1.0)
        
        results[dtype_name] = {
            "final_norm": float(norm),
            "final_energy": float(energy),
            "dtype": str(psi.psi.dtype),
        }
    
    return results


def test_subnormal_handling():
    """Test subnormal value handling on GPU vs CPU."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    # Create arrays with subnormal values
    subnormal_f64 = np.float64(5e-324)  # Smallest subnormal double
    subnormal_f32 = np.float32(1e-45)   # Smallest subnormal float
    
    # Test on CPU
    cpu_sub_f64 = subnormal_f64 * 2.0
    cpu_sub_f32 = subnormal_f32 * 2.0
    
    # Test on GPU
    gpu_sub_f64 = cupy.array(subnormal_f64) * 2.0
    gpu_sub_f32 = cupy.array(subnormal_f32) * 2.0
    
    cupy.cuda.Stream.null.synchronize()
    
    return {
        "cpu": {
            "subnormal_f64_x2": float(cpu_sub_f64),
            "subnormal_f32_x2": float(cpu_sub_f32),
            "f64_is_zero": cpu_sub_f64 == 0.0,
            "f32_is_zero": cpu_sub_f32 == 0.0,
        },
        "gpu": {
            "subnormal_f64_x2": float(gpu_sub_f64.get()),
            "subnormal_f32_x2": float(gpu_sub_f32.get()),
            "f64_is_zero": bool((gpu_sub_f64 == 0).get()),
            "f32_is_zero": bool((gpu_sub_f32 == 0).get()),
        },
        "match": {
            "f64": np.isclose(cpu_sub_f64, float(gpu_sub_f64.get())),
            "f32": np.isclose(cpu_sub_f32, float(gpu_sub_f32.get())),
        }
    }


def test_underflow_behavior():
    """Test underflow to zero behavior."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    # Create values that will underflow when squared
    tiny = np.float64(1e-200)
    tiny_arr = cupy.full((100,), tiny, dtype=cupy.float64)
    
    # Square on CPU
    cpu_sq = tiny * tiny
    # Square on GPU
    gpu_sq = (tiny_arr * tiny_arr).get()[0]
    
    return {
        "cpu_squared": float(cpu_sq),
        "gpu_squared": float(gpu_sq),
        "cpu_is_zero": cpu_sq == 0.0,
        "gpu_is_zero": gpu_sq == 0.0,
        "match": np.isclose(cpu_sq, gpu_sq),
    }


def test_nan_inf_propagation():
    """Test NaN and Inf propagation on GPU."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    # Create arrays with NaN/Inf
    arr_nan = cupy.array([1.0, np.nan, 3.0], dtype=cupy.float64)
    arr_inf = cupy.array([1.0, np.inf, 3.0], dtype=cupy.float64)
    arr_neginf = cupy.array([1.0, -np.inf, 3.0], dtype=cupy.float64)
    
    # Operations
    nan_result = (arr_nan * 2.0).get()
    inf_result = (arr_inf * 2.0).get()
    neginf_result = (arr_neginf * 2.0).get()
    inf_minus_inf = (arr_inf + arr_neginf).get()
    zero_times_inf = (cupy.array([0.0]) * cupy.array([np.inf])).get()
    
    cupy.cuda.Stream.null.synchronize()
    
    return {
        "nan_propagation": float(nan_result[1]) if not np.isnan(nan_result[1]) else "NaN",
        "inf_propagation": float(inf_result[1]) if np.isinf(inf_result[1]) else "Inf",
        "neginf_propagation": float(neginf_result[1]) if np.isinf(neginf_result[1]) else "-Inf",
        "inf_minus_inf": float(inf_minus_inf[1]) if not np.isnan(inf_minus_inf[1]) else "NaN",
        "zero_times_inf": float(zero_times_inf[0]) if not np.isnan(zero_times_inf[0]) else "NaN",
    }


def test_vortex_core_precision():
    """Test vortex core density precision on GPU vs CPU."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    from quantumlab.solvers.split_operator import SplitOperatorSolver
    from quantumlab.observables.current import vortex_positions
    
    grid = Grid2D(128, -4.0, 4.0, 128, -4.0, 4.0)
    X, Y = grid.X, grid.Y
    
    # Create vortex state
    psi = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
    psi.psi = psi.psi * (X + 1j*Y)
    psi.normalize()
    
    # CPU reference
    cpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi, 10)
    
    # GPU solver
    gpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi, 10)
    
    # Compare vortex detection
    pos_cpu, q_cpu = vortex_positions(psi_cpu, min_density=0.0)
    pos_gpu, q_gpu = vortex_positions(psi_gpu, min_density=0.0)
    
    # Core density at vortex center
    X, Y = grid.X, grid.Y
    center_mask = (X**2 + Y**2) < 0.5**2
    cpu_core_density = float(np.max(np.abs(psi_cpu.psi[center_mask])**2))
    gpu_core_density = float(np.max(np.abs(psi_gpu.psi[center_mask])**2))
    
    return {
        "cpu": {
            "vortices_found": int(len(pos_cpu)),
            "charges": [int(c) for c in q_cpu],
            "core_density": cpu_core_density,
        },
        "gpu": {
            "vortices_found": int(len(pos_gpu)),
            "charges": [int(c) for c in q_gpu],
            "core_density": gpu_core_density,
        },
        "agreement": {
            "vortices_match": len(pos_cpu) == len(pos_gpu),
            "charges_match": [int(c) for c in q_cpu] == [int(c) for c in q_gpu],
            "core_density_rel_error": abs(cpu_core_density - gpu_core_density) / max(cpu_core_density, 1e-100),
        }
    }


def test_phase_winding_precision():
    """Test phase winding precision near numerical zeros."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    grid = Grid2D(128, -4.0, 4.0, 128, -4.0, 4.0)
    X, Y = grid.X, grid.Y
    
    # Test with vortex at different sub-grid positions
    results = {}
    for dx in [0.0, 0.25, 0.5]:
        psi = WaveFunction2D.gaussian(Grid2D(128, -4.0, 4.0, 128, -4.0, 4.0), 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
        psi.psi = psi.psi * ((X-dx) + 1j*Y)
        psi.normalize()
        
        # CPU
        cpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='numpy')
        psi_cpu = cpu_solver.evolve(psi, 1)
        pos_cpu, q_cpu = vortex_positions(psi_cpu, min_density=0.0)
        
        # GPU
        gpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
        psi_gpu = gpu_solver.evolve(psi, 1)
        pos_gpu, q_gpu = vortex_positions(psi_gpu, min_density=0.0)
        
        results[f"dx_{dx}"] = {
            "cpu": {"vortices": len(pos_cpu), "charges": list(q_cpu)},
            "gpu": {"vortices": len(pos_gpu), "charges": list(q_gpu)},
            "match": len(pos_cpu) == len(pos_gpu) and list(q_cpu) == list(q_gpu),
        }
    
    return results


def test_norm_energy_conservation():
    """Test norm and energy conservation on GPU vs CPU over long evolution."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    grid = Grid1D(256, -8.0, 8.0)
    V = HarmonicOscillator(omega=1.0, m=1.0)
    psi0 = WaveFunction1D.gaussian(grid, -3.0, 2.0, 1.0)
    
    # CPU
    cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi0, 500)
    cpu_norm = psi_cpu.norm()
    cpu_energy = total_energy_expectation(psi_cpu, V, hbar=1.0, m=1.0)
    
    # GPU
    gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 500)
    gpu_norm = psi_gpu.norm()
    gpu_energy = total_energy_expectation(psi_gpu, V, hbar=1.0, m=1.0)
    
    return {
        "cpu": {"norm": float(cpu_norm), "energy": float(cpu_energy)},
        "gpu": {"norm": float(gpu_norm), "energy": float(gpu_energy)},
        "agreement": {
            "norm_rel_error": abs(cpu_norm - gpu_norm) / cpu_norm,
            "energy_rel_error": abs(cpu_energy - gpu_energy) / max(abs(cpu_energy), 1e-100),
        }
    }


def main():
    print("=" * 70)
    print("DOMAIN 21: GPU Precision & Zero-Floor Integrity")
    print("=" * 70)
    
    dev_info = get_device_info()
    print(f"Device: {json.dumps(dev_info, indent=2)}")
    
    if not cupy_available():
        print("CuPy not available - skipping")
        return
    
    all_results = {
        "device": get_device_info(),
        "tests": {}
    }
    
    tests = [
        ("precision_modes", test_precision_modes),
        ("subnormal_handling", test_subnormal_handling),
        ("underflow_behavior", test_underflow_behavior),
        ("nan_inf_propagation", test_nan_inf_propagation),
        ("vortex_core_precision", test_vortex_core_precision),
        ("phase_winding_precision", test_phase_winding_precision),
        ("norm_energy_conservation", test_norm_energy_conservation),
    ]
    
    for name, test_fn in tests:
        print(f"\n>>> {name}")
        try:
            result = test_fn()
            # Convert numpy types to Python types for JSON serialization
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
            result = convert(result)
            all_results["tests"][name] = result
            print(f"  OK")
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            all_results["tests"][name] = {"error": str(e)}
    
    out_file = os.path.join(OUT, "domain21_precision_zero_floor.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nResults saved: {out_file}")
    print("Done.")


if __name__ == "__main__":
    import cupy
    main()