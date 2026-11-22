#!/usr/bin/env python3
"""
cpd_independent_recomputation.py

Phase 2 deliverable: Independent recomputation of D27.3 observables
from first principles. This script independently calculates the values
reported in domain27_zero_floor_physics.json WITHOUT reading that file.

The purpose is to verify that the producer functions in physics_integration.py
report correct values per the actual quantumlab implementation, not to verify
that the values match.

Usage:
    python cpd_independent_recomputation.py [output_json]

Output: JSON with recomputed observables and comparison to reported values.
"""

import os
import sys
import json
import numpy as np

AUD = r"C\\Users\\krist\\Desktop\\quantum-simulation-cpd-audit-2026-11-20"
QS = r"C:\\Users\\krist\\Desktop\\quantum-simulation-main\\quantum-simulation-main"

sys.path.insert(0, QS)

# Import quantumlab (needed for independent recomputation)
try:
    from quantumlab.solvers.split_operator import SplitOperatorSolver
    from quantumlab.solvers.backends import cupy_available
    from quantumlab.core.grid import Grid1D, Grid2D
    from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D
    from quantumlab.potentials.oscillator import HarmonicOscillator
    from quantumlab.observables.expectation import (
        position_expectation,
        position_squared_expectation,
        total_energy_expectation,
    )
    from quantumlab.observables.current import vortex_positions
    print("quantumlab imported successfully")
except ImportError as e:
    print(f"ERROR: {e}")
    print("Install: pip install scipy")
    sys.exit(1)


def recompute_energy_threshold():
    """Independent recomputation of energy_threshold_with_zero_floor test."""
    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    V = HarmonicOscillator(omega=1.0, m=1.0)
    psi0 = WaveFunction1D.gaussian(grid, 0.0, 0.5, 1.0)
    psi0.normalize()

    cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend="numpy")
    psi_cpu = cpu_solver.evolve(psi0, 200)

    gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend="cupy", device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 200)

    cpu_energy = float(total_energy_expectation(psi_cpu, V, hbar=1.0, m=1.0))
    gpu_energy = float(total_energy_expectation(psi_gpu, V, hbar=1.0, m=1.0))

    return {
        "cpu_energy": cpu_energy,
        "gpu_energy": gpu_energy,
        "energy_disagreement": abs(cpu_energy - gpu_energy),
    }


def recompute_center_variance():
    """Independent recomputation of center variance test."""
    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    V = HarmonicOscillator(omega=1.0, m=1.0)
    psi0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 1.0)
    psi0.normalize()

    cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend="numpy")
    psi_cpu = cpu_solver.evolve(psi0, 100)

    gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend="cupy", device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 100)

    cpu_x = float(position_expectation(psi_cpu))
    gpu_x = float(position_expectation(psi_gpu))
    cpu_x2 = float(position_squared_expectation(psi_cpu))
    gpu_x2 = float(position_squared_expectation(psi_gpu))

    cpu_var = cpu_x2 - cpu_x ** 2
    gpu_var = gpu_x2 - gpu_x ** 2

    return {
        "cpu_center": cpu_x,
        "gpu_center": gpu_x,
        "cpu_center_variance": cpu_var,
        "gpu_center_variance": gpu_var,
        "cpu_center_variance_gpu_disagreement": abs(cpu_var - gpu_var),
    }


def recompute_fft():
    """Independent recomputation of FFT-related observables."""
    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    psi0 = WaveFunction1D.gaussian(grid, 0.0, 2.0, 1.0)
    psi0.normalize()

    cpu_fft = np.fft.fft(psi0.psi)
    cpu_mag = np.abs(cpu_fft)
    cpu_norm = float(np.sqrt(np.sum(np.abs(cpu_fft) ** 2)))

    if cupy_available():
        import cupy as cp

        gpu_psi = cp.asarray(psi0.psi)
        gpu_fft = cp.fft.fft(gpu_psi)
        gpu_mag = cp.abs(gpu_fft)
        cp.cuda.Stream.null.synchronize()
        gpu_mag_np = np.asarray(gpu_mag.get())
        gpu_norm = float(np.sqrt(np.sum(np.abs(gpu_mag_np) ** 2)))
    else:
        gpu_norm = None

    # L2 relative error
    rel_l2 = float(np.linalg.norm(cpu_mag - gpu_mag_np) / np.linalg.norm(cpu_mag)) if gpu_mag_np is not None else None

    return {
        "cpu_fft_normalization": cpu_norm,
        "gpu_fft_normalization": gpu_norm,
        "relative_l2_error": rel_l2,
    }


def recompute_phase():
    """Independent recomputation of phase agreement."""
    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    psi0 = WaveFunction1D.gaussian(grid, 0.0, 2.0, 1.0)
    psi0.normalize()

    cpu_fft = np.fft.fft(psi0.psi)
    cpu_phase = np.angle(cpu_fft)

    if cupy_available():
        import cupy as cp

        gpu_psi = cp.asarray(psi0.psi)
        gpu_fft = cp.fft.fft(gpu_psi)
        cp.cuda.Stream.null.synchronize()
        gpu_phase = np.asarray(cp.angle(gpu_fft).get())
    else:
        gpu_phase = None

    mask = cpu_mag > np.percentile(cpu_mag, 95)

    if gpu_phase is not None:
        phase_diff = np.abs(cpu_phase[mask] - gpu_phase[mask])
        return {
            "max_phase_diff": float(np.max(phase_diff)),
            "phase_diff_std": float(np.std(phase_diff)),
        }
    else:
        return {"max_phase_diff": None, "phase_diff_std": None, "note": "CuPy not available"}


def recompute_core_density():
    """Independent recomputation of vortex core density."""
    n = 256
    x_min, x_max = -6.0, 6.0
    y_min, y_max = -6.0, 6.0
    grid = Grid2D(n, x_min, x_max, n, y_min, y_max)
    X, Y = grid.X, grid.Y

    r = np.sqrt(X ** 2 + Y ** 2)
    theta = np.arctan2(Y, X)
    psi_data = np.exp(-r ** 2 / (2.0 * 1.0 ** 2)).astype(np.complex128) * np.exp(1j * theta)
    psi0 = WaveFunction2D(grid, psi_data)
    psi0.normalize()

    cpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend="numpy")
    psi_cpu = cpu_solver.evolve(psi0, 20)

    gpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend="cupy", device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 20)

    density_cpu = np.sum(np.abs(psi_cpu.psi) ** 2, axis=1)
    density_gpu = np.sum(np.abs(psi_gpu.psi) ** 2, axis=1)

    center_flat = np.abs(grid.x) < 1.5
    cpu_core = float(np.min(density_cpu[center_flat]))
    gpu_core = float(np.min(density_gpu[center_flat]))

    return {
        "cpu_core_density": cpu_core,
        "gpu_core_density": gpu_core,
        "core_density_rel_error": abs(cpu_core - gpu_core) / max(cpu_core, 1e-100),
    }


def recompute_norm():
    """Independent recomputation of norm conservation."""
    n = 256
    x_min, x_max = -6.0, 6.0
    y_min, y_max = -6.0, 6.0
    grid = Grid2D(n, x_min, x_max, n, y_min, y_max)
    X, Y = grid.X, grid.Y

    r = np.sqrt(X ** 2 + Y ** 2)
    theta = np.arctan2(Y, X)
    psi_data = np.exp(-r ** 2 / (2.0 * 1.0 ** 2)).astype(np.complex128) * np.exp(1j * theta)
    psi0 = WaveFunction2D(grid, psi_data)
    psi0.normalize()

    cpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend="numpy")
    psi_cpu = cpu_solver.evolve(psi0, 20)

    gpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend="cupy", device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 20)

    cpu_norm = float(psi_cpu.norm())
    gpu_norm = float(psi_gpu.norm())

    return {
        "initial_norm": float(psi0.norm()),
        "cpu_final_norm": cpu_norm,
        "gpu_final_norm": gpu_norm,
        "cpu_norm_disagreement": abs(cpu_norm - 1.0),
        "gpu_norm_disagreement": abs(gpu_norm - 1.0),
    }


def main():
    print("=" * 70)
    print("Independent Recomputation - D27.3 Observables")
    print("=" * 70)
    print()

    results = {
        "recomputed": {},
        "reported": {
            "cpu_energy": 0.7499948325323975,
            "gpu_energy": 0.7499948325323964,
            "cpu_center": -0.23911383818807963,
            "gpu_center": -0.23911383818807755,
            "cpu_center_variance": 0.46894652786954766,
            "gpu_center_variance": 0.46894652786955143,
            "fft_normalization": 63.99999999999999,
            "gpu_fft_normalization": 64.0,
            "relative_l2_error": 1.3848786276065917e-16,
            "core_density": {"cpu": 1.2793904313395363, "gpu": 1.279390431339538},
            "final_norm": {"cpu": 1.000000000000001, "gpu": 1.0000000000000038},
        },
        "comparison": {},
    }

    # Run each recomputation
    for name, fn in [
        ("energy_threshold", recompute_energy_threshold),
        ("center_variance", recompute_center_variance),
        ("fft", recompute_fft),
        ("phase", recompute_phase),
        ("core_density", recompute_core_density),
        ("norm", recompute_norm),
    ]:
        print(f"Recomputing {name}...")
        results["recomputed"][name] = fn()
        print(f"  done: {results['recomputed'][name]}")

    # Compare with reported values
    print()
    print("Comparison with reported values:")
    print("-" * 60)

    for key, reported_val in [
        ("cpu_energy", results["reported"]["cpu_energy"]),
        ("gpu_energy", results["reported"]["gpu_energy"]),
        ("cpu_center", results["reported"]["cpu_center"]),
        ("gpu_center", results["reported"]["gpu_center"]),
        ("cpu_center_variance", results["reported"]["cpu_center_variance"]),
        ("gpu_center_variance", results["reported"]["gpu_center_variance"]),
        ("fft_normalization", results["reported"]["fft_normalization"]),
        ("gpu_fft_normalization", results["reported"]["gpu_fft_normalization"]),
        ("relative_l2_error", results["reported"]["relative_l2_error"]),
        ("core_density.cpu", results["reported"]["core_density"]["cpu"]),
        ("core_density.gpu", results["reported"]["core_density"]["gpu"]),
        ("final_norm.cpu", results["reported"]["final_norm"]["cpu"]),
        ("final_norm.gpu", results["reported"]["final_norm"]["gpu"]),
    ]:
        if key in results["recomputed"]["energy_threshold"]:
            recomputed_val = results["recomputed"]["energy_threshold"][key]
        elif key in results["recomputed"]["center_variance"]:
            recomputed_val = results["recomputed"]["center_variance"][key]
        elif key in results["recomputed"]["fft"]:
            recomputed_val = results["recomputed"]["fft"][key]
        elif key in results["recomputed"]["phase"]:
            recomputed_val = results["recomputed"]["phase"][key]
        elif key in results["recomputed"]["core_density"]:
            recomputed_val = results["recomputed"]["core_density"][key]
        elif key in results["recomputed"]["norm"]:
            recomputed_val = results["recomputed"]["norm"][key]
        else:
            recomputed_val = None

        if recomputed_val is not None:
            agreement = abs(recomputed_val - reported_val)
            status = "OK" if agreement < 1e-10 else "MISMATCH"
            print(f"  {key:40s}: reported={reported_val:.15e}  recomputed={recomputed_val:.15e}  {status}  diff={agreement:.2e}")

    results["comparison"]["status_summary"] = "See above"

    # Write output
    out_path = os.path.join(AUD, "cpd_independent_recomputation.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nOutput written: {out_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
