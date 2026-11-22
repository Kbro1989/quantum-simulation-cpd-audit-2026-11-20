#!/usr/bin/env python3
"""
Domain 20: FFT Performance & Memory Bandwidth Characterization

Measures:
- Forward FFT, inverse FFT throughput (ms/transform)
- Kinetic phase multiplication
- Potential phase multiplication  
- Complete Strang step
- Full evolution throughput
- 1D, 2D, 3D with increasing grid sizes
- Power-of-two vs mixed-prime dimensions
"""

import os
import sys
import json
import numpy as np
import time
from pathlib import Path

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain20_fft_performance")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import get_backend, cupy_available

import cupy
import cupyx.scipy.fft as cp_fft

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

def benchmark_fft(backend_name, grid, n_warmup=20, n_repeat=100):
    """Benchmark forward and inverse FFT."""
    xp = cupy if backend_name == 'cupy' else np
    fft_mod = cp_fft if backend_name == 'cupy' else np.fft
    
    # Create test array
    arr = xp.random.random(grid.shape) + 1j * xp.random.random(grid.shape)
    arr = xp.asarray(arr, dtype=xp.complex128)
    
    # Warmup
    for _ in range(n_warmup):
        fwd = fft_mod.fftn(arr)
        inv = fft_mod.ifftn(fwd)
        if backend_name == 'cupy':
            cupy.cuda.Stream.null.synchronize()
    
    # Benchmark forward FFT
    cupy.cuda.Stream.null.synchronize() if backend_name == 'cupy' else None
    start = time.perf_counter()
    for _ in range(n_repeat):
        fwd = fft_mod.fftn(arr)
        if backend_name == 'cupy':
            cupy.cuda.Stream.null.synchronize()
    fwd_time = (time.perf_counter() - start) / n_repeat * 1000  # ms
    
    # Benchmark inverse FFT
    fwd = fft_mod.fftn(arr)
    if backend_name == 'cupy':
        cupy.cuda.Stream.null.synchronize()
    start = time.perf_counter()
    for _ in range(n_repeat):
        inv = fft_mod.ifftn(fwd)
        if backend_name == 'cupy':
            cupy.cuda.Stream.null.synchronize()
    inv_time = (time.perf_counter() - start) / n_repeat * 1000  # ms
    
    return {
        "forward_fft_ms": fwd_time,
        "inverse_fft_ms": inv_time,
        "total_fft_ms": fwd_time + inv_time,
        "array_size": arr.size,
        "array_bytes": arr.nbytes,
    }


def benchmark_split_operator_step(backend_name, dimension, grid_size, n_warmup=10, n_repeat=50):
    """Benchmark complete Strang step via SplitOperatorSolver."""
    if not cupy_available() and backend_name == 'cupy':
        return None
    
    from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
    from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
    from quantumlab.potentials.oscillator import HarmonicOscillator
    from quantumlab.solvers.split_operator import SplitOperatorSolver
    
    if dimension == 1:
        grid = Grid1D(grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
    elif dimension == 2:
        grid = Grid2D(grid_size, -grid_size/2, grid_size/2, grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
    else:
        grid = Grid3D(grid_size, -grid_size/2, grid_size/2, 
                      grid_size, -grid_size/2, grid_size/2,
                      grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction3D.gaussian(grid, 0,0,0, 0,0,0, 1.0, 1.0, 1.0)
    
    V = HarmonicOscillator(omega=1.0, m=1.0)
    solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    
    # Warmup
    for _ in range(n_warmup):
        wf = solver.evolve(wf, 1)
    
    # Benchmark
    cupy.cuda.Stream.null.synchronize()
    start = time.perf_counter()
    for _ in range(n_repeat):
        wf = solver.evolve(wf, 1)
    cupy.cuda.Stream.null.synchronize()
    step_time = (time.perf_counter() - start) / n_repeat * 1000  # ms
    
    return {
        "step_time_ms": step_time,
        "grid_size": grid_size,
        "dimension": dimension,
        "array_size": wf.psi.size,
        "array_bytes": wf.psi.nbytes if hasattr(wf.psi, 'nbytes') else wf.psi.size * 16,
    }


def benchmark_kinetic_potential(backend_name, dimension, grid_size, n_repeat=100):
    """Benchmark kinetic and potential phase multiplication separately."""
    if not cupy_available() and backend_name == 'cupy':
        return None
    
    from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
    from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
    from quantumlab.potentials.oscillator import HarmonicOscillator
    from quantumlab.solvers.split_operator import SplitOperatorSolver
    
    if dimension == 1:
        grid = Grid1D(grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
    elif dimension == 2:
        grid = Grid2D(grid_size, -grid_size/2, grid_size/2, grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
    else:
        grid = Grid3D(grid_size, -grid_size/2, grid_size/2, 
                      grid_size, -grid_size/2, grid_size/2,
                      grid_size, -grid_size/2, grid_size/2)
        wf = WaveFunction3D.gaussian(grid, 0,0,0, 0,0,0, 1.0, 1.0, 1.0)
    
    V = HarmonicOscillator(omega=1.0, m=1.0)
    solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    
    # Upload once
    psi_dev = solver._upload(wf)
    
    # Benchmark kinetic step
    cupy.cuda.Stream.null.synchronize()
    start = time.perf_counter()
    for _ in range(n_repeat):
        psi_dev = solver._kinetic_step(psi_dev, 1.0)
    cupy.cuda.Stream.null.synchronize()
    kinetic_time = (time.perf_counter() - start) / n_repeat * 1000
    
    # Benchmark potential half-step
    cupy.cuda.Stream.null.synchronize()
    start = time.perf_counter()
    for _ in range(n_repeat):
        psi_dev = solver._potential_half_step(psi_dev, 0.0, 1.0)
    cupy.cuda.Stream.null.synchronize()
    potential_time = (time.perf_counter() - start) / n_repeat * 1000
    
    return {
        "kinetic_step_ms": kinetic_time,
        "potential_half_step_ms": potential_time,
        "total_strang_ms": kinetic_time + 2 * potential_time,
    }


def main():
    print("=" * 70)
    print("DOMAIN 20: FFT Performance & Memory Bandwidth")
    print("=" * 70)
    
    dev_info = get_device_info()
    print(f"Device: {json.dumps(dev_info, indent=2)}")
    
    if not dev_info["available"]:
        print("CuPy not available - skipping GPU benchmarks")
        return
    
    results = {
        "device": dev_info,
        "timestamp": "2026-11-21",
        "benchmarks": {}
    }
    
    # Test configurations
    dims = [1, 2, 3]
    sizes = {
        1: [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],
        2: [32, 64, 128, 256, 512, 1024],
        3: [16, 32, 64, 128, 256],
    }
    
    for dim in dims:
        print(f"\n=== Dimension {dim}D ===")
        dim_results = {}
        
        for size in sizes[dim]:
            print(f"  Grid {size}^{dim}...")
            try:
                # FFT benchmark
                grid = None
                if dim == 1:
                    grid = Grid1D(size, -size/2, size/2)
                elif dim == 2:
                    grid = Grid2D(size, -size/2, size/2, size, -size/2, size/2)
                else:
                    grid = Grid3D(size, -size/2, size/2, size, -size/2, size/2, size, -size/2, size/2)
                
                fft_results = benchmark_fft('cupy', grid)
                
                # Split-operator step benchmark (smaller reps for larger grids)
                n_rep = max(10, 50 // max(1, size // 256))
                step_results = benchmark_split_operator_step('cupy', dim, size, n_repeat=n_rep)
                
                # Kinetic/potential breakdown (for smaller grids)
                kp_results = None
                if size <= 256:
                    kp_results = benchmark_kinetic_potential('cupy', dim, size)
                
                dim_results[f"{size}^{dim}"] = {
                    "fft": fft_results,
                    "split_operator_step": step_results,
                    "kinetic_potential": kp_results,
                }
                print(f"    FFT: {fft_results['forward_fft_ms']:.3f} + {fft_results['inverse_fft_ms']:.3f} = {fft_results['total_fft_ms']:.3f} ms")
                if step_results:
                    print(f"    Step: {step_results['step_time_ms']:.3f} ms")
                if kp_results:
                    print(f"    Kinetic: {kp_results['kinetic_step_ms']:.3f} ms, Potential: {kp_results['potential_half_step_ms']:.3f} ms")
                    
            except Exception as e:
                print(f"    ERROR: {e}")
                dim_results[f"{size}^{dim}"] = {"error": str(e)}
        
        results["benchmarks"][f"{dim}D"] = dim_results
    
    # CPU comparison (for key sizes)
    print("\n=== CPU Comparison ===")
    cpu_results = {}
    for dim in [1, 2]:
        size = 256 if dim == 1 else 64
        print(f"  CPU {dim}D {size}^{dim}...")
        grid = Grid1D(size, -size/2, size/2) if dim == 1 else Grid2D(size, -size/2, size/2, size, -size/2, size/2)
        cpu_fft = benchmark_fft('numpy', grid)
        cpu_results[f"{size}^{dim}"] = cpu_fft
        print(f"    CPU FFT: {cpu_fft['total_fft_ms']:.3f} ms")
    
    results["cpu_comparison"] = cpu_results
    
    # Save results
    out_file = os.path.join(OUT, "domain20_fft_performance.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved: {out_file}")
    print("Done.")
    return results


if __name__ == "__main__":
    import cupy
    main()