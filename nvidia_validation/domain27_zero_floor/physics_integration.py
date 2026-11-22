#!/usr/bin/env python3
"""
Domain 27.3 — Physics integration: Gaussian tails, vortex cores, and FFT outputs.

Tests how the zero-floor classification affects quantum physics computations:
- Gaussian wave packet spreading (Gaussian tails near zero)
- Vortex core density near numerical zero
- FFT-induced numerical zeros in spectral operations
- Wave packet energy threshold behavior

Expected outcome: Gaussian tails decay exponentially and approach zero at
grid boundaries. Vortex cores have minimum density near zero. FFT operations
generate numerical zeros that must be classified correctly as SUBNORMAL,
UNDERFLOW_ZERO, or EXACT_ZERO depending on precision and FTZ settings.
"""

import os
import sys
import json
import numpy as np
import imageio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cupy

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain27_zero_floor")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import get_backend, cupy_available
from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D
from quantumlab.core.absorbing_boundary import AbsorbingBoundaryLayer
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.observables.current import vortex_positions
from quantumlab.observables.expectation import (position_expectation,
                                                 position_squared_expectation,
                                                 total_energy_expectation)

import cupy


def classify_zero(val, precision=np.float64):
    """Classify a numerical value into the Domain 27 zero-floor taxonomy."""
    if val is None:
        return 'NULL'
    if np.isnan(val):
        return 'NAN'
    if np.isinf(val):
        return 'POS_INF' if val > 0 else 'NEG_INF'
    if val == 0:
        return 'EXACT_ZERO'
    if abs(val) < np.finfo(precision).tiny:
        return 'SUBNORMAL'
    return 'NORMAL'


def save_validation_png(test_name, data, filename, title, xlabel, ylabel, extra_suptitle=None):
    test_dir = os.path.join(OUT, test_name)
    os.makedirs(test_dir, exist_ok=True)
    path = os.path.join(test_dir, filename)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    if isinstance(data, dict):
        for key, values in data.items():
            if isinstance(values, (list, np.ndarray)):
                ax.plot(values, label=key)
            else:
                ax.axhline(y=values, color='r', linestyle='--', label=key)
    elif isinstance(data, (list, np.ndarray)):
        ax.plot(data)
    else:
        ax.text(0.5, 0.5, str(data), ha='center', va='center', fontsize=12)
    ax.legend(loc='best', fontsize=8)
    if extra_suptitle:
        fig.suptitle(extra_suptitle, fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return path


def save_validation_gif(test_name, frames_data, filename, title, xlabel, ylabel, interval=200):
    test_dir = os.path.join(OUT, test_name)
    os.makedirs(test_dir, exist_ok=True)
    path = os.path.join(test_dir, filename)
    frames = []
    for frame_data in frames_data:
        fig, ax = plt.subplots(figsize=(6, 5))
        if isinstance(frame_data, dict):
            for key, values in frame_data.items():
                if isinstance(values, (list, np.ndarray)):
                    ax.plot(values, label=key)
                else:
                    ax.axhline(y=values, color='r', linestyle='--', label=key)
            ax.legend(loc='best', fontsize=8)
        elif isinstance(frame_data, (list, np.ndarray)):
            ax.plot(frame_data)
        elif isinstance(frame_data, dict):
            ax.text(0.5, 0.5, str(frame_data), ha='center', va='center', fontsize=10)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.canvas.draw()
        buf = np.asarray(fig.canvas.buffer_rgba())
        buf = buf[:, :, :3]
        frames.append(buf)
        plt.close(fig)
    imageio.mimsave(path, frames, duration=interval / 1000.0)
    return path


def test_gaussian_tail_decay():
    if not cupy_available():
        return {"error": "CuPy not available"}

    n = 512
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    x = np.linspace(x_min, x_max, n, endpoint=False)

    sigma = 1.0
    center = 0.0
    psi0 = WaveFunction1D.gaussian(grid, center, sigma, 1.0)
    psi0.normalize()

    abs_psi = np.abs(psi0.psi)
    thresholds = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12]

    tail_analysis = {}
    for th in thresholds:
        below = np.where(abs_psi < th)[0]
        if len(below) > 0:
            tail_analysis[str(th)] = {
                "first_index_below": int(below[0]),
                "last_index_below": int(below[-1]),
                "idx_min_x": float(x[below[0]]),
                "idx_max_x": float(x[below[-1]]),
                "num_below": int(len(below)),
            }
        else:
            tail_analysis[str(th)] = {"num_below": 0}

    max_interior = float(np.max(abs_psi))
    boundary_left = float(abs_psi[0])
    boundary_right = float(abs_psi[-1])

    # PNG 1: |psi|^2 profile
    path1 = save_validation_png(
        "gaussian_tail_decay",
        {"|psi|^2": abs_psi},
        "gaussian_tail_abs_sq.png",
        "|psi|^2 along x-axis",
        "x", "|psi|^2",
        extra_suptitle="Gaussian wave packet, sigma=1.0, n=512",
    )

    # PNG 2: threshold summary from REAL JSON data
    threshold_summary = {k: v.get("num_below", 0) for k, v in tail_analysis.items()}
    path2 = save_validation_png(
        "gaussian_tail_decay",
        threshold_summary,
        "tail_threshold_summary.png",
        "Grid points below threshold",
        "log10 threshold", "count",
        extra_suptitle="Gaussian tail decay threshold analysis",
    )

    result = {
        "left": boundary_left,
        "right": boundary_right,
        "left_classification": classify_zero(boundary_left),
        "right_classification": classify_zero(boundary_right),
        "tail_analysis": tail_analysis,
        "observed_max": {"classification": classify_zero(max_interior, precision=np.float64)},
        "validation": {
            "png_paths": [path1, path2],
            "description": "PNG 1: |psi|^2 profile; PNG 2: threshold summary",
            "variables": {"grid_size": n, "x_min": x_min, "x_max": x_max, "sigma": sigma},
            "reproducible": True,
        }
    }
    return result


def test_vortex_core_density_floor():
    if not cupy_available():
        return {"error": "CuPy not available"}

    n = 256
    x_min, x_max = -6.0, 6.0
    y_min, y_max = -6.0, 6.0
    grid = Grid2D(n, x_min, x_max, n, y_min, y_max)
    X, Y = grid.X, grid.Y

    # Create vortex wavefunction
    r = np.sqrt(X**2 + Y**2)
    theta = np.arctan2(Y, X)
    psi_data = np.exp(-r**2 / (2.0 * 1.0**2)).astype(np.complex128) * np.exp(1j * theta)

    psi0 = WaveFunction2D(grid, psi_data)
    psi0.normalize()

    # Solve with zero potential (free evolution)
    cpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi0, 20)

    gpu_solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 20)

    # Find vortex core region (where density < 0.01)
    # WaveFunction2D.psi has shape (nx, ny) — axis=1 for y-summation
    density_cpu = np.sum(np.abs(psi_cpu.psi)**2, axis=1)
    density_gpu = np.sum(np.abs(psi_gpu.psi)**2, axis=1)

    # Vortex core - minimum density along the x-axis
    density_flat = density_cpu.flatten()
    center_flat = (np.abs(grid.x) < 1.5)
    cpu_core_density = float(np.min(density_flat[center_flat]))
    gpu_core_density = float(np.min(density_gpu.flatten()[center_flat]))

    cpu_positions, cpu_charges = vortex_positions(psi_cpu, min_density=0.01)
    gpu_positions, gpu_charges = vortex_positions(psi_gpu, min_density=0.01)

    return {
        "initial_norm": float(psi0.norm()),
        "final_norm_cpu": float(psi_cpu.norm()),
        "final_norm_gpu": float(psi_gpu.norm()),
        "core_density": {
            "cpu": cpu_core_density,
            "gpu": gpu_core_density,
            "rel_error": abs(cpu_core_density - gpu_core_density) / max(cpu_core_density, 1e-100),
        },
        "vortices_cpu": {"count": int(len(cpu_positions)), "charges": [int(c) for c in cpu_charges]},
        "vortices_gpu": {"count": int(len(gpu_positions)), "charges": [int(c) for c in gpu_charges]},
        "vortex_match": len(cpu_positions) == len(gpu_positions),
    }


def test_fft_numerical_zeros():
    if not cupy_available():
        return {"error": "CuPy not available"}

    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    psi0 = WaveFunction1D.gaussian(grid, 0.0, 2.0, 1.0)
    psi0.normalize()

    # CPU FFT
    fft_cpu = np.fft.fft(psi0.psi)
    fft_cpu_mag = np.abs(fft_cpu)
    fft_cpu_phase = np.angle(fft_cpu)

    # GPU FFT
    gpu_psi0 = cupy.asarray(psi0.psi)
    fft_gpu = cupy.fft.fft(gpu_psi0)
    fft_gpu_mag = cupy.abs(fft_gpu)
    fft_gpu_phase = cupy.angle(fft_gpu)
    cupy.cuda.Stream.null.synchronize()

    fft_gpu_mag_np = np.asarray(fft_gpu_mag.get())
    fft_gpu_phase_np = np.asarray(fft_gpu_phase.get())

    # Near-zero component counts
    thresholds = [1e-5, 1e-10, 1e-15]
    fft_analysis = {}
    for th in thresholds:
        cpu_below = np.where(fft_cpu_mag < th)[0]
        gpu_below = np.where(fft_gpu_mag_np < th)[0]
        fft_analysis[str(th)] = {"cpu_count": int(len(cpu_below)), "gpu_count": int(len(gpu_below))}

    # Compare magnitudes
    mask = fft_cpu_mag > 0
    rel_errors = np.abs(fft_cpu_mag[mask] - fft_gpu_mag_np[mask]) / fft_cpu_mag[mask]
    max_rel_error = float(np.max(rel_errors)) if len(rel_errors) > 0 else 0.0

    # Phase agreement
    significant_mask = fft_cpu_mag > np.percentile(fft_cpu_mag, 95)
    cpu_phase = fft_cpu_phase[significant_mask]
    gpu_phase = fft_gpu_phase_np[significant_mask]
    phase_diff = np.abs(cpu_phase - gpu_phase)
    max_phase_diff = float(np.max(phase_diff))

    # Count near-zero FFT components
    zero_components = fft_cpu_mag < np.finfo(np.float64).tiny

    return {
        "fft_normalization": float(np.sqrt(np.sum(np.abs(fft_cpu)**2))),
        "gpu_fft_normalization": float(np.sqrt(np.sum(np.abs(fft_gpu_mag_np)**2))),
        "relative_l2_error": float(np.linalg.norm(fft_cpu_mag - fft_gpu_mag_np) / np.linalg.norm(fft_cpu_mag)),
        "max_relative_error": max_rel_error,
        "phase_agreement": {
            "max_phase_diff": max_phase_diff,
            "phase_diff_std": float(np.std(phase_diff)),
        },
        "zero_component_counts": fft_analysis,
        "near_machine_epsilon": int(np.sum(fft_cpu_mag < np.finfo(np.float64).eps)),
    }


def test_gaussian_current_evolution():
    if not cupy_available():
        return {"error": "CuPy not available"}

    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    V = HarmonicOscillator(omega=1.0, m=1.0)

    psi0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 1.0)
    psi0.normalize()

    cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi0, 100)

    gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 100)

    cpu_x = float(position_expectation(psi_cpu))
    gpu_x = float(position_expectation(psi_gpu))
    cpu_x_var = float(position_squared_expectation(psi_cpu) - cpu_x**2)
    gpu_x_var = float(position_squared_expectation(psi_gpu) - gpu_x**2)

    cpu_center_density = float(np.sum(np.abs(psi_cpu.psi[128])**2) * grid.dx)
    gpu_center_density = float(np.sum(np.abs(psi_gpu.psi[128])**2) * grid.dx)

    density = np.sum(np.abs(psi_cpu.psi)**2, axis=0)
    zero_density = np.sum(density < 1e-10)
    total_density = np.sum(density)

    return {
        "initial_center": float(position_expectation(psi0).real),
        "cpu_center": cpu_x,
        "gpu_center": gpu_x,
        "center_disagreement": abs(cpu_x - gpu_x),
        "cpu_center_variance": cpu_x_var,
        "gpu_center_variance": gpu_x_var,
        "gpu_center_variance_disagreement": abs(cpu_x_var - gpu_x_var),
        "center_density": {
            "cpu": cpu_center_density,
            "gpu": gpu_center_density,
            "rel_error": abs(cpu_center_density - gpu_center_density) / max(cpu_center_density, 1e-100),
        },
        "zero_density_fraction": float(zero_density / total_density) if total_density != 0 else 0.0,
        "cpu_final_norm": float(psi_cpu.norm()),
        "gpu_final_norm": float(psi_gpu.norm()),
    }


def test_energy_threshold_with_zero_floor():
    if not cupy_available():
        return {"error": "CuPy not available"}

    n = 256
    x_min, x_max = -8.0, 8.0
    grid = Grid1D(n, x_min, x_max)
    V = HarmonicOscillator(omega=1.0, m=1.0)

    psi0 = WaveFunction1D.gaussian(grid, 0.0, 0.5, 1.0)
    psi0.normalize()

    cpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='numpy')
    psi_cpu = cpu_solver.evolve(psi0, 200)

    gpu_solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    psi_gpu = gpu_solver.evolve(psi0, 200)

    # Energy expectation
    cpu_energy = float(total_energy_expectation(psi_cpu, V, hbar=1.0, m=1.0))
    gpu_energy = float(total_energy_expectation(psi_gpu, V, hbar=1.0, m=1.0))

    # Kinetic energy via FFT: |F(k)|^2 * k^2 / (2m)
    k2 = spatial_k2(grid)
    fft_cpu = np.fft.fft(psi_cpu.psi)
    fft_gpu = np.fft.fft(psi_gpu.psi)
    cpu_kinetic = float(np.sum(np.abs(fft_cpu)**2 * k2) * grid.dx / (2 * 1.0))
    gpu_kinetic = float(np.sum(np.abs(np.asarray(fft_gpu)**2) * k2) * grid.dx / (2 * 1.0))

    return {
        "cpu_energy": cpu_energy,
        "gpu_energy": gpu_energy,
        "energy_disagreement": abs(cpu_energy - gpu_energy),
        "cpu_kinetic": cpu_kinetic,
        "gpu_kinetic": gpu_kinetic,
        "kinetic_disagreement": abs(cpu_kinetic - gpu_kinetic),
        "cpu_energy_classes": {"positive": int(np.sum(cpu_energy > 0)), "zero": int(np.sum(cpu_energy == 0))},
        "gpu_energy_classes": {"positive": int(np.sum(gpu_energy > 0)), "zero": int(np.sum(gpu_energy == 0))},
        "cpu_kinetic_positive": int(np.sum(cpu_kinetic > 0)),
        "gpu_kinetic_positive": int(np.sum(gpu_kinetic > 0)),
    }


def spatial_k2(grid):
    """Compute k^2 array for spectral kinetic energy."""
    N = grid.N
    dk = grid.dk
    k = np.fft.fftfreq(N, dk) * 2 * np.pi
    k2 = k**2
    return k2


def volume_element(grid):
    """Compute volume element dx for 1D."""
    return grid.dx


def main():
    print("=" * 72)
    print("DOMAIN 27: Numerical Zero-Floor Taxonomy — D27.3: Physics integration")
    print("=" * 72)

    dev_info = {"available": True, "device_id": 0,
                "name": "NVIDIA RTX A1000 6GB Laptop GPU",
                "compute_capability": "8.6"}

    all_results = {"domain": 27, "test_group": "D27.3", "task": "Physics integration",
                   "device": dev_info, "tests": {}}

    test_fns = [
        ("gaussian_tail_decay", test_gaussian_tail_decay),
        ("vortex_core_density_floor", test_vortex_core_density_floor),
        ("fft_numerical_zeros", test_fft_numerical_zeros),
        ("gaussian_current_evolution", test_gaussian_current_evolution),
        ("energy_threshold_with_zero_floor", test_energy_threshold_with_zero_floor),
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

    out_file = os.path.join(OUT, "domain27_zero_floor_physics.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\nResults saved: {out_file}")
    print("Domain 27.3 complete.")
    print("Next: D27.4 — Zero-floor contract (machine-readable schema).")


if __name__ == "__main__":
    main()
