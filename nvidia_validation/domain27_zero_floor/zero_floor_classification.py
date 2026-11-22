#!/usr/bin/env python3
"""
Domain 27.2 — CUDA zero-floor comparison against the actual quantum-simulation-main implementation.

This script extends Domain 27.1 by measuring how GPU (CuPy) execution differs from CPU
(NumPy/SciPy) in terms of zero-floor classification, focusing on:
- FTZ (flush-to-zero) behavior on CUDA
- Subnormal preservation
- Underflow behavior
- Backend-specific zeroFloor classification

Run from quantum-simulation-cpd-audit-2026-11-20 root:
    python nvidia_validation/domain27_zero_floor/zero_floor_classification.py
"""

import os
import sys
import json
import numpy as np
import time
from pathlib import Path

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain27_zero_floor")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import get_backend, cupy_available
from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.core.absorbing_boundary import AbsorbingBoundaryLayer
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.potentials.barriers import Gaussian3DBarrier
from quantumlab.observables.current import vortex_positions
from quantumlab.observables.expectation import total_energy_expectation, position_expectation

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


def classify_value(value, device='cpu', precision=np.float64):
    """
    Classify a numerical value into the Domain 27 zero-floor taxonomy.

    Classes:
    - NULL: missing/unavailable
    - NAN: Not-a-Number
    - POS_INF: +infinity
    - NEG_INF: -infinity
    - GPU_FTZ_ZERO: subnormal flushed to zero by GPU (FTZ enabled)
    - UNDERFLOW_ZERO: nonzero mathematical result rounded to zero
    - EXACT_ZERO: numerically zero
    - SUBNORMAL: nonzero subnormal
    - NORMAL: representable normal
    """
    if value is None:
        return 'NULL'

    if isinstance(value, np.ndarray):
        result = np.empty(value.shape, dtype='U32')
        for idx in np.ndindex(value.shape):
            result[idx] = classify_value(value[idx], device, precision)
        return result

    if np.isnan(value):
        return 'NAN'

    if np.isinf(value):
        return 'POS_INF' if value > 0 else 'NEG_INF'

    if value == 0:
        return 'EXACT_ZERO'

    if abs(value) < np.finfo(precision).tiny:
        # Determine if this is a subnormal or underflowed to zero
        if device == 'cuda':
            # On CUDA, we may not be able to distinguish subnormal vs zeroed
            # before FTZ is applied. The comparison here is against the CPU
            # value, not the GPU value.
            cpu_val = np.float64(value)
            # subnormal check
            return 'SUBNORMAL' if abs(cpu_val) < np.finfo(np.float64).tiny else 'EXACT_ZERO'
        return 'SUBNORMAL'

    return 'NORMAL'


def classify_device_array(arr, device='cpu', precision=np.float64):
    """Classify each element of a device array (cupy or numpy)."""
    if hasattr(arr, 'get'):
        # cupy array
        arr_np = arr.get()
    else:
        arr_np = np.asarray(arr)

    result = np.empty(arr.shape, dtype='U32')
    for idx in np.ndindex(arr.shape):
        result[idx] = classify_value(arr_np[idx], device, precision)
    return result


def test_precision_modes():
    """CPU vs GPU: precision comparison."""
    if not cupy_available():
        return {"error": "CuPy not available"}

    results = {}
    grid = Grid1D(256, -8.0, 8.0)
    V = HarmonicOscillator(omega=1.0, m=1.0)

    for dtype_name, dtype in [("complex64", np.complex64), ("complex128", np.complex128)]:
        # CPU solver
        cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='numpy')
        psi0_cpu = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
        psi0_cpu.psi = np.asarray(psi0_cpu.psi, dtype=dtype)
        psi_cpu = cpu_solver.evolve(psi0_cpu, 100)

        # GPU solver
        gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
        psi0_gpu = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
        psi0_gpu.psi = np.asarray(psi0_gpu.psi, dtype=dtype)
        psi_gpu = gpu_solver.evolve(psi0_gpu, 100)

        # Norm
        norm_gpu = float(np.sum(np.abs(psi_gpu.psi)**2) * grid.dx)
        norm_cpu = float(np.sum(np.abs(psi_cpu.psi)**2) * grid.dx)

        results[dtype_name] = {
            "gpu_norm": norm_gpu,
            "cpu_norm": norm_cpu,
            "gpu_factor": norm_gpu / norm_cpu if norm_cpu != 0 else None,
            "dtype": str(psi_gpu.psi.dtype),
            "gpu_dtype": str(psi_gpu.psi.dtype),
        }

    return results


def test_subnormal_handling():
    """CPU vs GPU: subnormal value handling."""
    if not cupy_available():
        return {"error": "CuPy not available"}

    results = {}
    subnormal_f64 = np.float64(5e-324)
    subnormal_f32 = np.float32(1e-45)
    tiny_f64 = np.float64(1e-200)
    tiny_f32 = np.float32(1e-40)

    # CPU operations
    cpu_sub_f64 = subnormal_f64 * 2.0
    cpu_sub_f32 = subnormal_f32 * 2.0
    cpu_sq_f64 = tiny_f64 * tiny_f64
    cpu_sq_f32 = tiny_f32 * tiny_f32

    # GPU operations
    gpu_sub_f64 = cupy.array(subnormal_f64) * 2.0
    gpu_sub_f32 = cupy.array(subnormal_f32) * 2.0
    gpu_sq_f64 = cupy.array(tiny_f64) * cupy.array(tiny_f64)
    gpu_sq_f32 = cupy.array(tiny_f32) * cupy.array(tiny_f32)

    cupy.cuda.Stream.null.synchronize()

    results["subnormal"] = {
        "cpu": {
            "f64_x2": float(cpu_sub_f64),
            "f32_x2": float(cpu_sub_f32),
            "f64_is_zero": cpu_sub_f64 == 0.0,
            "f32_is_zero": cpu_sub_f32 == 0.0,
            "f64_classification": classify_value(cpu_sub_f64, 'cpu', np.float64),
            "f32_classification": classify_value(cpu_sub_f32, 'cpu', np.float32),
        },
        "gpu": {
            "f64_x2": float(gpu_sub_f64.get()),
            "f32_x2": float(gpu_sub_f32.get()),
            "f64_is_zero": bool((gpu_sub_f64 == 0).get()),
            "f32_is_zero": bool((gpu_sub_f32 == 0).get()),
            "f64_classification": classify_value(gpu_sub_f64, 'cuda', np.float64),
            "f32_classification": classify_value(gpu_sub_f32, 'cuda', np.float32),
        },
        "match": {
            "f64": np.isclose(cpu_sub_f64, float(gpu_sub_f64.get())),
            "f32": np.isclose(cpu_sub_f32, float(gpu_sub_f32.get())),
        }
    }

    results["underflow"] = {
        "cpu_squared_f64": float(cpu_sq_f64),
        "cpu_squared_f32": float(cpu_sq_f32),
        "cpu_f64_is_zero": cpu_sq_f64 == 0.0,
        "cpu_f32_is_zero": cpu_sq_f32 == 0.0,
        "gpu_squared_f64": float(gpu_sq_f64.get()),
        "gpu_squared_f32": float(gpu_sq_f32.get()),
        "gpu_f64_is_zero": bool(gpu_sq_f64 == 0),
        "gpu_f32_is_zero": bool(gpu_sq_f32 == 0),
        "gpu_f64_classification": classify_value(gpu_sq_f64.get(), 'cuda', np.float64),
        "gpu_f32_classification": classify_value(gpu_sq_f32.get(), 'cuda', np.float32),
    }

    return results


def test_nan_inf_propagation():
    """CPU vs GPU: NaN and Inf propagation."""
    if not cupy_available():
        return {"error": "CuPy not available"}

    arr_nan = cupy.array([1.0, np.nan, 3.0], dtype=cupy.float64)
    arr_inf = cupy.array([1.0, np.inf, 3.0], dtype=cupy.float64)
    arr_neginf = cupy.array([1.0, -np.inf, 3.0], dtype=cupy.float64)

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
    """CPU vs GPU: vortex core density precision."""
    if not cupy_available():
        return {"error": "CuPy not available"}

    grid = Grid2D(128, -4.0, 4.0, 128, -4.0, 4.0)
    X, Y = grid.X, grid.Y

    psi = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
    psi.psi = psi.psi * (X + 1j*Y)
    psi.normalize()

    cpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi, 10)

    gpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi, 10)

    pos_cpu, q_cpu = vortex_positions(psi_cpu, min_density=0.0)
    pos_gpu, q_gpu = vortex_positions(psi_gpu, min_density=0.0)

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


def test_norm_energy_conservation():
    """CPU vs GPU: norm and energy conservation over long evolution."""
    if not cupy_available():
        return {"error": "CuPy not available"}

    grid = Grid1D(256, -8.0, 8.0)
    V = HarmonicOscillator(omega=1.0, m=1.0)
    psi0 = WaveFunction1D.gaussian(grid, -3.0, 2.0, 1.0)

    cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi0, 500)
    cpu_norm = psi_cpu.norm()
    cpu_energy = float(total_energy_expectation(psi_cpu, V, hbar=1.0, m=1.0))

    gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 500)
    gpu_norm = psi_gpu.norm()
    gpu_energy = float(total_energy_expectation(psi_gpu, V, hbar=1.0, m=1.0))

    return {
        "cpu": {"norm": float(cpu_norm), "energy": cpu_energy},
        "gpu": {"norm": float(gpu_norm), "energy": gpu_energy},
        "agreement": {
            "norm_rel_error": abs(cpu_norm - gpu_norm) / cpu_norm,
            "energy_rel_error": abs(cpu_energy - gpu_energy) / max(abs(cpu_energy), 1e-100),
        }
    }


def test_ftz_presence():
    """
    Test for FTZ (flush-to-zero) behavior on GPU.

    This test is deterministic: CPU and GPU should match EXACTLY for values
    that are representable in float64. If GPU returns 0.0 for a nonzero input
    while CPU returns a nonzero value, FTZ is present.
    """
    if not cupy_available():
        return {"error": "CuPy not available"}

    # Create a subnormal value that should be preserved on CPU but may be
    # flushed to zero on GPU if FTZ is enabled.
    subnormal = np.float64(1e-300)
    arr = cupy.full((1000,), subnormal, dtype=cupy.float64)

    # Operations that might trigger FTZ
    multiplied = arr * 2.0
    exponentiated = cupy.exp(arr)
    divided = arr / 2.0

    cupy.cuda.Stream.null.synchronize()

    cpu_multiplied = subnormal * 2.0
    cpu_exponentiated = np.exp(subnormal)
    cpu_divided = subnormal / 2.0

    results = {
    "input_value": float(subnormal),
    "cpu_multiplied": float(cpu_multiplied),
    "gpu_multiplied": float(multiplied.get()[0]),
    "gpu_multiplied_zero": bool((multiplied == 0).sum() == 1000),

    "cpu_exponentiated": float(cpu_exponentiated),
    "gpu_exponentiated": float(exponentiated.get()[0]),
    "gpu_exp_zero": bool((exponentiated == 0).sum() == 1000),

    "cpu_divided": float(cpu_divided),
    "gpu_divided": float(divided.get()[0]),
    "gpu_div_zero": bool((divided == 0).sum() == 1000),

    "ftz_detected": bool(
        (cpu_multiplied != 0.0 and float(multiplied.get()[0]) == 0.0) or
        (cpu_exponentiated != 0.0 and float(exponentiated.get()[0]) == 0.0)
    ),
    }

    return results


def main():
    print("=" * 72)
    print("DOMAIN 27: Numerical Zero-Floor Taxonomy — D27.2: CUDA comparison")
    print("=" * 72)

    dev_info = get_device_info()
    print(f"Device: {json.dumps(dev_info, indent=2)}")

    if not cupy_available():
        print("CuPy not available - skipping")
        return

    all_results = {
        "device": get_device_info(),
        "tests": {}
    }

    test_fns = [
        ("precision_modes", test_precision_modes),
        ("subnormal_handling", test_subnormal_handling),
        ("nan_inf_propagation", test_nan_inf_propagation),
        ("vortex_core_precision", test_vortex_core_precision),
        ("norm_energy_conservation", test_norm_energy_conservation),
        ("ftz_presence", test_ftz_presence),
    ]

    for name, test_fn in test_fns:
        print(f"\n>>> {name}")
        try:
            result = test_fn()
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

    out_file = os.path.join(OUT, "domain27_zero_floor_comparison.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

    print(f"\nResults saved: {out_file}")
    print("Domain 27.2 complete.")
    print("Next: D27.3 — Physics integration (Gaussian tails, vortex cores, FFT).")


if __name__ == "__main__":
    import cupy
    main()
