#!/usr/bin/env python3
"""
Gate G0 + Domain 19: CUDA Execution Provenance and Residency Probe.

Verifies:
1. Backend selection truth (explicit 'cupy', 'auto', 'gpu:true' paths)
2. Actual CUDA device identity and array residency throughout evolution
3. Host↔Device transfer accounting (counts, bytes, locations)
3. Failure behavior for unavailable GPU backends

Uses CuPy-level instrumentation + runtime assertions.
"""

import os
import sys
import json
import numpy as np
from pathlib import Path

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain19_cuda_residency")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.potentials.barriers import Gaussian3DBarrier
from quantumlab.solvers.split_step_1d import SplitStep1DSolver
from quantumlab.solvers.split_step_2d import SplitStep2DSolver
from quantumlab.solvers.split_step_3d import SplitStep3DSolver
from quantumlab.solvers.split_step_3d_gpu import SplitStep3DGPU
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import get_backend, cupy_available

import cupy
import cupyx.scipy.fft as cp_fft

# =====================================================================
# Instrumentation: CuPy transfer tracker
# =====================================================================
class CudaResidencyTracker:
    """Tracks CuPy array device residency and host↔device transfers."""
    
    def __init__(self):
        self.h2d_count = 0
        self.h2d_bytes = 0
        self.d2h_count = 0
        self.d2h_bytes = 0
        self.sync_count = 0
        self.array_creations = []  # (name, shape, dtype, device_id)
        self.transfer_events = []  # (direction, bytes, location)
    
    def record_creation(self, name, array, device_id=None):
        if device_id is None:
            try:
                device_id = array.device.id
            except:
                device_id = -1
        self.array_creations.append({
            "name": name,
            "shape": array.shape,
            "dtype": str(array.dtype),
            "device_id": device_id,
            "is_cupy": isinstance(array, cupy.ndarray)
        })
    
    def record_h2d(self, bytes_transferred, location):
        self.h2d_count += 1
        self.h2d_bytes += bytes_transferred
        self.transfer_events.append({"direction": "h2d", "bytes": bytes_transferred, "location": location})
    
    def record_d2h(self, bytes_transferred, location):
        self.d2h_count += 1
        self.d2h_bytes += bytes_transferred
        self.transfer_events.append({"direction": "d2h", "bytes": bytes_transferred, "location": location})
    
    def record_sync(self, location):
        self.sync_count += 1
    
    def to_dict(self):
        return {
            "h2d_count": self.h2d_count,
            "h2d_bytes": self.h2d_bytes,
            "d2h_count": self.d2h_count,
            "d2h_bytes": self.d2h_bytes,
            "sync_count": self.sync_count,
            "array_creations": self.array_creations,
            "transfer_events": self.transfer_events,
        }


# Monkey-patch CuPy transfer functions for tracking
original_asarray = cupy.asarray
original_asnumpy = cupy.asnumpy
original_get = cupy.ndarray.get if hasattr(cupy.ndarray, 'get') else None

def track_asarray(obj, *args, **kwargs):
    result = original_asarray(obj, *args, **kwargs)
    if isinstance(obj, np.ndarray):
        tracker.record_h2d(obj.nbytes, "cupy.asarray")
    return result

def track_asnumpy(obj, *args, **kwargs):
    result = original_asnumpy(obj, *args, **kwargs)
    if isinstance(obj, cupy.ndarray):
        tracker.record_d2h(obj.nbytes, "cupy.asnumpy")
    return result

tracker = CudaResidencyTracker()

def install_tracking():
    cupy.asarray = track_asarray
    cupy.asnumpy = track_asnumpy

def uninstall_tracking():
    cupy.asarray = original_asarray
    cupy.asnumpy = original_asnumpy


# =====================================================================
# Device identity verification
# =====================================================================
def get_device_identity():
    """Return dict with GPU identity info."""
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
        "uuid": getattr(dev, 'uuid', None),
    }


def verify_array_on_device(array, expected_device_id, name):
    """Assert array is on expected CUDA device."""
    if not isinstance(array, cupy.ndarray):
        return False, f"{name}: NOT a cupy.ndarray (type={type(array).__name__})"
    if array.device.id != expected_device_id:
        return False, f"{name}: on device {array.device.id}, expected {expected_device_id}"
    return True, f"{name}: OK on device {array.device.id}"


# =====================================================================
# Test harness
# =====================================================================
def make_config(solver_type, backend='numpy', gpu=False, device_id=0, **kwargs):
    """Build a simulation config dict."""
    cfg = {
        "dimension": kwargs.get("dimension", 1),
        "dt": kwargs.get("dt", 0.01),
        "hbar": kwargs.get("hbar", 1.0),
        "m": kwargs.get("m", 1.0),
        "solver": solver_type,
        "backend": backend,
        "gpu": gpu,
        "device_id": device_id,
        "order": kwargs.get("order", 2),
        "nonlinearity": kwargs.get("nonlinearity", 0.0),
        "rotation": kwargs.get("rotation", 0.0),
        "damping": kwargs.get("damping", 0.0),
        "num_steps": kwargs.get("num_steps", 5),
        "grid": kwargs.get("grid", {"N": 64, "L": 8.0}),
        "wavefunction": kwargs.get("wavefunction", {"x0": 0.0, "k0": 1.0, "sigma": 1.0}),
        "potential": kwargs.get("potential", {"type": "harmonic_oscillator", "omega": 1.0}),
    }
    return cfg


def build_solver_from_config(cfg):
    """Replicate runner.py's _build_solver logic."""
    from quantumlab.solvers.split_step_1d import SplitStep1DSolver
    from quantumlab.solvers.split_step_2d import SplitStep2DSolver
    from quantumlab.solvers.split_step_3d import SplitStep3DSolver
    from quantumlab.solvers.split_step_3d_gpu import SplitStep3DGPU
    from quantumlab.solvers.split_operator import SplitOperatorSolver
    from quantumlab.potentials.oscillator import HarmonicOscillator
    from quantumlab.potentials.traps import HarmonicTrap
    from quantumlab.potentials.barriers import Gaussian3DBarrier
    from quantumlab.potentials.base import Potential
    
    dim = cfg["dimension"]
    dt = float(cfg["dt"])
    hbar = float(cfg.get("hbar", 1.0))
    m = float(cfg.get("m", 1.0))
    gpu = bool(cfg.get("gpu", False))
    
    # Build grid
    grid_cfg = cfg["grid"]
    if dim == 1:
        grid = Grid1D(grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2)
    elif dim == 2:
        grid = Grid2D(grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2, 
                      grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2)
    elif dim == 3:
        grid = Grid3D(grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2,
                      grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2,
                      grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2)
    else:
        raise ValueError(f"Unsupported spatial dimension: {dim}")
    
    # Build potential
    pot_cfg = cfg.get("potential", {})
    ptype = pot_cfg.get("type", "harmonic_oscillator")
    if ptype == "harmonic_oscillator":
        potential = HarmonicOscillator(omega=pot_cfg.get("omega", 1.0), m=m)
    elif ptype == "harmonic_trap":
        potential = HarmonicTrap(omegas=pot_cfg.get("omega", 1.0), m=m)
    elif ptype == "gaussian_3d_barrier":
        potential = Gaussian3DBarrier(
            V0=pot_cfg.get("V0", 5.0),
            width=pot_cfg.get("width", 1.0),
            x0=pot_cfg.get("x0", 0.0),
            y0=pot_cfg.get("y0", 0.0),
            z0=pot_cfg.get("z0", 0.0),
        )
    else:
        class ZeroPotential(Potential):
            def evaluate(self, grid): return np.zeros(grid.shape)
        potential = ZeroPotential()
    
    if cfg.get("solver") == "split_operator":
        return SplitOperatorSolver(
            grid, potential, dt, hbar, m,
            order=int(cfg.get("order", 2)),
            nonlinearity=float(cfg.get("nonlinearity", 0.0)),
            rotation=float(cfg.get("rotation", 0.0)),
            damping=float(cfg.get("damping", 0.0)),
            backend=cfg.get("backend", "numpy"),
            device_id=cfg.get("device_id", 0),
        )
    if dim == 1:
        return SplitStep1DSolver(grid, potential, dt, hbar, m)
    elif dim == 2:
        return SplitStep2DSolver(grid, potential, dt, hbar, m)
    elif dim == 3:
        if gpu:
            return SplitStep3DGPU(grid, potential, dt, hbar, m)
        return SplitStep3DSolver(grid, potential, dt, hbar, m)
    raise ValueError(f"Unsupported spatial dimension: {dim}")


def build_grid_and_wf(cfg):
    """Build grid and initial wavefunction from config."""
    dim = cfg["dimension"]
    grid_cfg = cfg["grid"]
    wf_cfg = cfg["wavefunction"]
    
    if dim == 1:
        grid = Grid1D(grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2)
        wf = WaveFunction1D.gaussian(grid, wf_cfg.get("x0", 0.0), wf_cfg.get("k0", 1.0), wf_cfg.get("sigma", 1.0))
    elif dim == 2:
        grid = Grid2D(grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2, grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2)
        wf = WaveFunction2D.gaussian(grid, 
            wf_cfg.get("x0", 0.0), wf_cfg.get("y0", 0.0),
            wf_cfg.get("k0_x", 0.0), wf_cfg.get("k0_y", 0.0),
            wf_cfg.get("sigma_x", 1.0), wf_cfg.get("sigma_y", 1.0))
    elif dim == 3:
        grid = Grid3D(grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2,
                       grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2,
                       grid_cfg["N"], -grid_cfg["L"]/2, grid_cfg["L"]/2)
        wf = WaveFunction3D.gaussian(grid,
            wf_cfg.get("x0", 0.0), wf_cfg.get("y0", 0.0), wf_cfg.get("z0", 0.0),
            wf_cfg.get("k0_x", 0.0), wf_cfg.get("k0_y", 0.0), wf_cfg.get("k0_z", 0.0),
            wf_cfg.get("sigma_x", 1.0), wf_cfg.get("sigma_y", 1.0), wf_cfg.get("sigma_z", 1.0))
    return grid, wf


def run_residency_test(name, cfg, expected_backend_name, expected_device_id=None, should_fail=False):
    """Run a single residency test and return results dict."""
    print(f"\n{'='*60}")
    print(f"TEST: {name}")
    print(f"Config: solver={cfg.get('solver')}, backend={cfg.get('backend')}, gpu={cfg.get('gpu')}, device_id={cfg.get('device_id')}")
    print(f"Expected backend: {expected_backend_name}")
    
    global tracker
    tracker = CudaResidencyTracker()
    install_tracking()
    
    result = {
        "name": name,
        "config": cfg,
        "expected_backend": expected_backend_name,
        "expected_device_id": expected_device_id,
        "should_fail": should_fail,
        "passed": False,
        "errors": [],
        "warnings": [],
        "device_identity": get_device_identity(),
        "backend_resolved": None,
        "backend_name": None,
        "device_id_used": None,
        "tracker": None,
        "residency_checks": [],
    }
    
    try:
        if not cupy_available() and expected_backend_name == 'cupy':
            result["errors"].append("CuPy not available but cupy backend expected")
            result["passed"] = False
            return result
        
        # Build grid and wavefunction
        grid, wf = build_grid_and_wf(cfg)
        
        # Track initial array
        tracker.record_creation("initial_wavefunction", wf.psi)
        
        # Build solver (this calls get_backend internally)
        solver = build_solver_from_config(cfg)
        
        # Capture backend info
        result["backend_resolved"] = str(solver._be) if hasattr(solver, '_be') else "unknown"
        result["backend_name"] = solver._be.name if hasattr(solver, '_be') else "unknown"
        result["device_id_used"] = cfg.get("device_id", 0)
        
        print(f"  Backend resolved: {result['backend_name']}")
        print(f"  Expected: {expected_backend_name}")
        
        # Verify backend matches expectation
        if result["backend_name"] != expected_backend_name:
            result["errors"].append(f"Backend mismatch: got {result['backend_name']}, expected {expected_backend_name}")
        
        # Verify device identity
        if expected_backend_name == 'cupy':
            if not cupy_available():
                result["errors"].append("Expected cupy backend but CuPy unavailable")
            else:
                actual_dev = cupy.cuda.Device().id
                result["device_id_used"] = actual_dev
                if expected_device_id is not None and actual_dev != expected_device_id:
                    result["warnings"].append(f"Device ID mismatch: got {actual_dev}, expected {expected_device_id}")
        
        # Run evolution with residency checks
        print(f"  Running {cfg.get('num_steps', 5)} evolution steps...")
        tracker.h2d_count = 0
        tracker.h2d_bytes = 0
        tracker.d2h_count = 0
        tracker.d2h_bytes = 0
        tracker.sync_count = 0
        tracker.transfer_events = []
        
        # Use evolve() for proper GPU residency (single upload, N steps, single download)
        # Patch _advance to verify internal arrays stay on device
        original_advance = solver._advance
        residency_checks = []
        
        def instrumented_advance(psi):
            # Verify input psi is on device
            if expected_backend_name == 'cupy':
                ok, msg = verify_array_on_device(psi, expected_device_id or cupy.cuda.Device().id, "_advance input")
                residency_checks.append({"phase": "_advance_input", "ok": ok, "msg": msg})
                if not ok:
                    result["errors"].append(msg)
            
            # Call original
            psi_out = original_advance(psi)
            
            # Verify output psi is on device
            if expected_backend_name == 'cupy':
                ok, msg = verify_array_on_device(psi_out, expected_device_id or cupy.cuda.Device().id, "_advance output")
                residency_checks.append({"phase": "_advance_output", "ok": ok, "msg": msg})
                if not ok:
                    result["errors"].append(msg)
            
            return psi_out
        
        solver._advance = instrumented_advance
        
        # Also instrument _upload and _download
        original_upload = solver._upload
        original_download = solver._download
        
        def instrumented_upload(wf):
            psi = original_upload(wf)
            if expected_backend_name == 'cupy':
                ok, msg = verify_array_on_device(psi, expected_device_id or cupy.cuda.Device().id, "_upload output")
                residency_checks.append({"phase": "_upload", "ok": ok, "msg": msg})
                if not ok:
                    result["errors"].append(msg)
            return psi
        
        def instrumented_download(psi):
            if expected_backend_name == 'cupy':
                ok, msg = verify_array_on_device(psi, expected_device_id or cupy.cuda.Device().id, "_download input (should be device)")
                residency_checks.append({"phase": "_download_input", "ok": ok, "msg": msg})
                if not ok:
                    result["errors"].append(msg)
            wf = original_download(psi)
            if expected_backend_name == 'cupy':
                ok, msg = verify_array_on_device(wf.psi, expected_device_id or cupy.cuda.Device().id, "_download output (should be host)")
                residency_checks.append({"phase": "_download_output", "ok": not ok, "msg": msg})  # Expect host array
                if ok:  # If it's still on device, that's wrong
                    result["errors"].append(msg)
            return wf
        
        solver._upload = instrumented_upload
        solver._download = instrumented_download
        
        # Use evolve for proper GPU residency
        tracker.h2d_count = 0
        wf_current = wf
        # Use evolve for proper GPU residency (single upload, N steps, single download)
        wf_current = solver.evolve(wf_current, cfg.get("num_steps", 5))
        
        # Final check: result should be host array
        if expected_backend_name == 'cupy':
            ok, msg = verify_array_on_device(wf_current.psi, expected_device_id or cupy.cuda.Device().id, "final result (should be host)")
            # For final result, we expect ok=False (host array), so not ok = True = PASS
            residency_checks.append({"phase": "final_result", "ok": not ok, "msg": msg})
            if ok:  # If it's still on device, that's wrong
                result["errors"].append("Final result should be host array but is on device: " + msg)
        
        result["residency_checks"].extend(residency_checks)
        
        # Check for unexpected transfers during evolution (after step 0)
        evolution_h2d = sum(1 for e in tracker.transfer_events if e["direction"] == "h2d" and "step" in e.get("location", ""))
        evolution_d2h = sum(1 for e in tracker.transfer_events if e["direction"] == "d2h" and "step" in e.get("location", ""))
        
        if evolution_h2d > 0:
            result["warnings"].append(f"Unexpected H2D transfers during evolution: {evolution_h2d}")
        if evolution_d2h > 0:
            result["errors"].append(f"Unexpected D2H transfers during evolution: {evolution_d2h}")
        
        result["passed"] = len(result["errors"]) == 0
        
    except Exception as e:
        result["errors"].append(f"Exception: {type(e).__name__}: {e}")
        result["passed"] = False
    finally:
        uninstall_tracking()
        result["tracker"] = tracker.to_dict()
    
    status = "PASS" if result["passed"] else "FAIL"
    print(f"  Result: {status}")
    if result["errors"]:
        for e in result["errors"]:
            print(f"  ERROR: {e}")
    if result["warnings"]:
        for w in result["warnings"]:
            print(f"  WARN: {w}")
    
    return result


# =====================================================================
# Main test matrix
# =====================================================================
def main():
    print("=" * 70)
    print("GATE G0 + DOMAIN 19: CUDA Execution Provenance and Residency")
    print("=" * 70)
    
    # Print device identity
    dev_info = get_device_identity()
    print(f"Device: {json.dumps(dev_info, indent=2)}")
    print()
    
    all_results = []
    
    # Test 1: explicit backend='cupy' with SplitOperatorSolver
    print("\n>>> Test 1: SplitOperatorSolver with backend='cupy' (explicit)")
    cfg = make_config("split_operator", backend='cupy', device_id=0, dimension=1, num_steps=5)
    r = run_residency_test("SplitOperator_1D_cupy_explicit", cfg, expected_backend_name='cupy', expected_device_id=0)
    all_results.append(r)
    
    # Test 2: backend='auto' with SplitOperatorSolver (should resolve to cupy)
    print("\n>>> Test 2: SplitOperatorSolver with backend='auto' (should resolve to cupy)")
    cfg = make_config("split_operator", backend='auto', device_id=0, dimension=1, num_steps=5)
    r = run_residency_test("SplitOperator_1D_auto", cfg, expected_backend_name='cupy', expected_device_id=0)
    all_results.append(r)
    
    # Test 3: gpu=True with split_operator (THE KNOWN DEFECT - should show scipy-cpu)
    print("\n>>> Test 3: SplitOperatorSolver with gpu=True (KNOWN DEFECT)")
    cfg = make_config("split_operator", backend='numpy', gpu=True, dimension=1, num_steps=5)
    r = run_residency_test("SplitOperator_1D_gpu_true", cfg, expected_backend_name='scipy-cpu', expected_device_id=None)
    all_results.append(r)
    
    # Test 4: SplitOperatorSolver 2D with cupy
    print("\n>>> Test 4: SplitOperatorSolver 2D with backend='cupy'")
    cfg = make_config("split_operator", backend='cupy', device_id=0, dimension=2, num_steps=5)
    r = run_residency_test("SplitOperator_2D_cupy", cfg, expected_backend_name='cupy', expected_device_id=0)
    all_results.append(r)
    
    # Test 5: SplitOperatorSolver 3D with cupy
    print("\n>>> Test 5: SplitOperatorSolver 3D with backend='cupy'")
    cfg = make_config("split_operator", backend='cupy', device_id=0, dimension=3, num_steps=3)
    r = run_residency_test("SplitOperator_3D_cupy", cfg, expected_backend_name='cupy', expected_device_id=0)
    all_results.append(r)
    
    # Test 6: SplitStep3DGPU (explicit GPU solver)
    print("\n>>> Test 6: SplitStep3DGPU (explicit GPU solver)")
    cfg = make_config("split_step_3d_gpu", backend='cupy', device_id=0, dimension=3, num_steps=3)
    r = run_residency_test("SplitStep3DGPU", cfg, expected_backend_name='cupy', expected_device_id=0)
    all_results.append(r)
    
    # Test 7: explicitly unavailable GPU backend (device_id out of range)
    print("\n>>> Test 7: SplitOperatorSolver with invalid device_id (should fail)")
    if cupy_available():
        n_dev = cupy.cuda.runtime.getDeviceCount()
        cfg = make_config("split_operator", backend='cupy', device_id=n_dev, dimension=1, num_steps=1)
        r = run_residency_test("SplitOperator_invalid_device", cfg, expected_backend_name='cupy', expected_device_id=None, should_fail=True)
        # For this test, pass = it correctly raises an error
        r["passed"] = not r["passed"]  # invert: we expect it to fail
        all_results.append(r)
    
    # Test 8: backend='numpy' explicitly (CPU baseline)
    print("\n>>> Test 8: SplitOperatorSolver with backend='numpy' (CPU baseline)")
    cfg = make_config("split_operator", backend='numpy', dimension=1, num_steps=3)
    r = run_residency_test("SplitOperator_1D_numpy", cfg, expected_backend_name='scipy-cpu')
    all_results.append(r)
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    passed = sum(1 for r in all_results if r["passed"])
    total = len(all_results)
    print(f"Tests passed: {passed}/{total}")
    for r in all_results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['name']}")
        if r["errors"]:
            for e in r["errors"]:
                print(f"    ERROR: {e}")
    
    # Save results
    output = {
        "gate": "G0 + Domain 19",
        "date": "2026-11-21",
        "device_identity": dev_info,
        "repo": REPO,
        "audit_dir": AUD,
        "results": all_results,
        "summary": {"passed": passed, "total": total}
    }
    
    out_file = os.path.join(OUT, "g0_domain19_results.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {out_file}")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)