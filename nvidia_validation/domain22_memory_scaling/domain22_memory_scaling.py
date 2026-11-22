#!/usr/bin/env python3
"""
Domain 22: GPU Memory Scaling

Measures:
1. VRAM baseline (free/used)
2. State allocation (bytes per wavefunction, potential, buffers)
3. Evolution peak VRAM (during evolve)
4. Scaling (1D/2D/3D grid sweeps)
4. Fragmentation (repeated alloc/dealloc)

Mathematical baseline for complex128: M_psi = 16 * Nx * Ny * Nz bytes
For complex64: M_psi = 8 * Nx * Ny * Nz bytes

Measures entire solver working set including FFT workspaces, potential arrays, temp buffers.
"""

import os
import sys
import json
import numpy as np
import time
from pathlib import Path

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain22_memory_scaling")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import cupy_available

import cupy
from cupy import get_default_memory_pool, get_default_pinned_memory_pool

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


def get_vram_info():
    """Get VRAM info via NVML if available, else CuPy pool."""
    info = {}
    try:
        import pynvml
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
        info["nvml"] = {
            "total_bytes": mem.total,
            "free_bytes": mem.free,
            "used_bytes": mem.used,
        }
    except Exception:
        info["nvml"] = {"error": "pynvml not available"}
    
    # CuPy memory pool info
    pool = get_default_memory_pool()
    info["cupy_pool"] = {
        "used_bytes": pool.used_bytes(),
        "total_bytes": pool.total_bytes(),
        "free_bytes": pool.free_bytes(),
    }
    return info


def theoretical_psi_bytes(grid_shape, dtype=np.complex128):
    """Theoretical wavefunction storage."""
    n = np.prod(grid_shape)
    return int(n * np.dtype(dtype).itemsize)


def measure_solver_memory(dimension, grid_size, dtype=np.complex128, n_steps=10):
    """Measure memory for a single solver configuration."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
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
    
    V = None  # Free evolution for minimal potential overhead
    solver = SplitOperatorSolver(grid, V, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
    
    # Record baseline VRAM
    pool = get_default_memory_pool()
    cupy.cuda.Stream.null.synchronize()
    baseline_pool = pool.used_bytes()
    
    # Upload wavefunction (simulates _upload)
    psi_dev = solver._upload(wf)
    after_upload_pool = pool.used_bytes()
    
    # Warmup
    for _ in range(3):
        _ = solver._advance(psi_dev)
    cupy.cuda.Stream.null.synchronize()
    after_warmup_pool = pool.used_bytes()
    
    # Measure peak during evolution
    peak_pool = pool.used_bytes()
    for step in range(10):
        psi_dev = solver._advance(psi_dev)
        current = pool.used_bytes()
        if current > peak_pool:
            peak_pool = current
    cupy.cuda.Stream.null.synchronize()
    
    # Download (simulates _download)
    wf_final = WaveFunction1D(grid, solver._be.to_host(psi_dev)) if hasattr(grid, 'N') else None
    
    return {
        "dimension": 1,  # will be set by caller
        "grid_size": grid_size,
        "dtype": str(dtype),
        "theoretical_psi_bytes": theoretical_psi_bytes(wf.psi.shape, dtype),
        "baseline_pool_bytes": baseline_pool,
        "after_upload_pool_bytes": after_upload_pool,
        "after_warmup_pool_bytes": after_warmup_pool,
        "peak_pool_bytes": peak_pool,
        "upload_overhead_bytes": after_upload_pool - baseline_pool,
        "evolution_overhead_bytes": peak_pool - after_upload_pool,
        "workspace_bytes": peak_pool - after_upload_pool - theoretical_psi_bytes(wf.psi.shape, dtype),
    }


def measure_fragmentation(dimension, grid_size, dtype=np.complex128, n_cycles=20):
    """Measure memory fragmentation via repeated alloc/dealloc."""
    if not cupy_available():
        return {"error": "CuPy not available"}
    
    pool = get_default_memory_pool()
    
    # Track pool size over cycles
    pool_sizes = []
    
    for cycle in range(n_cycles):
        # Create fresh grid and wavefunction each cycle
        if dimension == 1:
            grid = Grid1D(grid_size, -grid_size/2, grid_size/2)
            wf = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
            wf.psi = wf.psi.astype(dtype)
        elif dimension == 2:
            grid = Grid2D(grid_size, -grid_size/2, grid_size/2, 
                          grid_size, -grid_size/2, grid_size/2)
            wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
            wf.psi = wf.psi.astype(dtype)
        else:
            grid = Grid3D(grid_size, -grid_size/2, grid_size/2,
                          grid_size, -grid_size/2, grid_size/2,
                          grid_size, -grid_size/2, grid_size/2)
            wf = WaveFunction3D.gaussian(grid, 0,0,0, 0,0,0, 1.0, 1.0, 1.0)
            wf.psi = wf.psi.astype(dtype)
        
        solver = SplitOperatorSolver(grid, None, 0.01, hbar=1.0, m=1.0, backend='cupy', device_id=0)
        
        # Upload and evolve
        psi_dev = solver._upload(wf)
        for _ in range(3):
            psi_dev = solver._advance(psi_dev)
        
        # Record pool size
        pool_size = get_default_memory_pool().used_bytes()
        pool_sizes.append(pool_size)
    
    cupy.cuda.Stream.null.synchronize()
    
    return {
        "dimension": dimension,
        "grid_size": grid_size,
        "dtype": str(dtype),
        "n_cycles": n_cycles,
        "pool_sizes_bytes": pool_sizes,
        "max_pool_bytes": max(pool_sizes),
        "min_pool_bytes": min(pool_sizes),
        "avg_pool_bytes": np.mean(pool_sizes),
        "fragmentation_mb": (max(pool_sizes) - min(pool_sizes)) / (1024*1024),
    }


def main():
    print("=" * 70)
    print("DOMAIN 22: GPU Memory Scaling")
    print("=" * 70)
    
    dev_info = get_device_info()
    print(f"Device: {json.dumps(dev_info, indent=2)}")
    
    if not cupy_available():
        print("CuPy not available - skipping")
        return
    
    # Print VRAM baseline
    vram = get_vram_info()
    print(f"\nVRAM Baseline: {json.dumps(vram, indent=2)}")
    
    # Theoretical baselines
    print("\n=== Theoretical Wavefunction Storage (complex128) ===")
    for n in [64, 128, 256, 512, 1024]:
        for dim in [1, 2, 3]:
            shape = (n,) * dim
            bytes_ = theoretical_psi_bytes(shape)
            print(f"  {dim}D {n}^{dim}: {bytes_ / (1024**2):.1f} MiB")
    
    # Test configurations
    dims = [1, 2, 3]
    sizes = {
        1: [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],
        2: [32, 64, 128, 256, 512, 1024],
        3: [16, 32, 64, 128, 256],
    }
    
    all_results = {
        "device": get_device_info(),
        "vram_baseline": vram,
        "theoretical_baselines": {
            f"{n}^{dim}": theoretical_psi_bytes((n,)*dim, np.complex128) 
            for dim in [1,2,3] for n in [64,128,256,512,1024]
        },
        "scaling": {},
        "fragmentation": {},
    }
    
    # Scaling measurements
    for dim in dims:
        print(f"\n=== Scaling: {dim}D ===")
        dim_results = {}
        for size in sizes[dim]:
            print(f"  {dim}D {size}^{dim}...")
            try:
                r = measure_solver_memory(dim, size, n_steps=10)
                r["dimension"] = dim
                dim_results[f"{size}^{dim}"] = r
                print(f"    Theoretical psi: {r['theoretical_psi_bytes']/1024/1024:.2f} MiB")
                print(f"    Upload overhead: {r['upload_overhead_bytes']/1024/1024:.2f} MiB")
                print(f"    Evolution overhead: {r['evolution_overhead_bytes']/1024/1024:.2f} MiB")
                print(f"    Workspace: {r['workspace_bytes']/1024/1024:.2f} MiB")
                print(f"    Peak pool: {r['peak_pool_bytes']/1024/1024:.2f} MiB")
            except Exception as e:
                print(f"    ERROR: {e}")
                dim_results[f"{size}^{dim}"] = {"error": str(e)}
        all_results["scaling"][f"{dim}D"] = dim_results
    
    # Fragmentation measurements (subset)
    print("\n=== Fragmentation ===")
    for dim in [1, 2, 3]:
        size = sizes[dim][2]  # medium size
        print(f"  {dim}D {size}^{dim} fragmentation...")
        try:
            r = measure_fragmentation(dim, size, n_cycles=20)
            r["dimension"] = dim
            all_results["fragmentation"][f"{dim}D_{size}^{dim}"] = r
            print(f"    Pool range: {r['min_pool_bytes']/1024/1024:.1f} - {r['max_pool_bytes']/1024/1024:.1f} MiB")
            print(f"    Fragmentation: {r['fragmentation_mb']:.2f} MiB")
        except Exception as e:
            print(f"    ERROR: {e}")
            all_results["fragmentation"][f"{dim}D_{size}^{dim}"] = {"error": str(e)}
    
    # Complex64 comparison (subset)
    print("\n=== Complex64 vs Complex128 ===")
    for dim in [1, 2]:
        size = sizes[dim][2]
        print(f"  {dim}D {size}^{dim} complex64...")
        try:
            r128 = measure_solver_memory(dim, size, dtype=np.complex128)
            r64 = measure_solver_memory(dim, size, dtype=np.complex64)
            print(f"    c128 peak: {r128['peak_pool_bytes']/1024/1024:.1f} MiB")
            print(f"    c64 peak: {r64['peak_pool_bytes']/1024/1024:.1f} MiB")
            print(f"    Ratio: {r64['peak_pool_bytes']/r128['peak_pool_bytes']:.2f}")
            all_results.setdefault("precision_comparison", {})[f"{dim}D_{size}^{dim}"] = {
                "complex128": r128,
                "complex64": r64,
            }
        except Exception as e:
            print(f"    ERROR: {e}")
    
    # Save results
    output = {
        "device": get_device_info(),
        "timestamp": "2026-11-21",
        "results": all_results,
    }
    
    # Convert numpy types for JSON
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
    
    output = convert(output)
    
    out_file = os.path.join(OUT, "domain22_memory_scaling.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved: {out_file}")
    print("Done.")


if __name__ == "__main__":
    import cupy
    main()