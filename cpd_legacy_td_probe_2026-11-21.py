#!/usr/bin/env python3
"""
cpd_legacy_td_probe_2026-11-21.py

Independent probe of the UNCOMMITTED working-tree change to the legacy
SplitStep solvers (CPD-P1-1).  Compares the legacy solvers against the
production SplitOperatorSolver on an explicitly time-dependent potential
(DipoleDrive) -- the exact acceptance case named in cpd_remediation_plan.md B1.

Acceptance (plan B1):  max|psi_legacy - psi_td| after 20 steps < 1e-12
for a DipoleDrive with phase=0.

This probe reads no audit artifact and imports only quantumlab.
"""
import json
import os
import sys

import numpy as np

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction3D
from quantumlab.potentials.time_dependent import DipoleDrive
from quantumlab.solvers.split_step_1d import SplitStep1DSolver
from quantumlab.solvers.split_operator import SplitOperatorSolver

OUT = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20\cpd_legacy_td_probe_2026-11-21.json"


def run_1d_case(phase, steps=20, dt=0.01, n=256):
    grid = Grid1D(n, -8.0, 8.0)
    pot = DipoleDrive(base=None, F0=1.0, omega=2.0, axis="x", phase=phase)

    psi0 = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)
    psi0.normalize()

    prod = SplitOperatorSolver(grid, pot, dt, 1.0, 1.0, order=2, backend="numpy")
    leg = SplitStep1DSolver(grid, pot, dt, 1.0, 1.0)

    p_prod = psi0.psi.copy()
    p_leg = psi0.psi.copy()
    per_step = []
    for k in range(steps):
        p_prod = prod.step(WaveFunction1D(grid, p_prod)).psi
        p_leg = leg.step(WaveFunction1D(grid, p_leg)).psi
        per_step.append(float(np.max(np.abs(p_leg - p_prod))))

    return {
        "phase": phase,
        "steps": steps,
        "dt": dt,
        "max_abs_diff": float(np.max(np.abs(p_leg - p_prod))),
        "final_step_diff": per_step[-1],
        "first_step_diff": per_step[0],
        "acceptance_1e-12": bool(np.max(np.abs(p_leg - p_prod)) < 1e-12),
        "per_step": per_step,
    }


def run_3d_gpu_fallback_case(steps=20, dt=0.01, n=32):
    """SplitStep3DGPU falls back to CPU when CuPy is absent; its step() was
    never wired to _update_operators, so the frozen-U_V defect survives there."""
    grid = Grid3D(n, -6.0, 6.0, n, -6.0, 6.0, n, -6.0, 6.0)
    pot = DipoleDrive(base=None, F0=1.0, omega=2.0, axis="x", phase=0.0)

    psi0 = WaveFunction3D.gaussian(grid, (0.0, 0.0, 0.0), 1.0, 1.0)
    psi0.normalize()

    prod = SplitOperatorSolver(grid, pot, dt, 1.0, 1.0, order=2, backend="numpy")
    from quantumlab.solvers.split_step_3d_gpu import SplitStep3DGPU
    gpu = SplitStep3DGPU(grid, pot, dt, 1.0, 1.0)

    p_prod = psi0.psi.copy()
    p_gpu = psi0.psi.copy()
    for _ in range(steps):
        p_prod = prod.step(WaveFunction3D(grid, p_prod)).psi
        p_gpu = gpu.step(WaveFunction3D(grid, p_gpu)).psi

    return {
        "gpu_backend_active": bool(getattr(gpu, "_gpu", False)),
        "steps": steps,
        "max_abs_diff": float(np.max(np.abs(p_gpu - p_prod))),
        "acceptance_1e-12": bool(np.max(np.abs(p_gpu - p_prod)) < 1e-12),
    }


def main():
    results = {"probe": "cpd_legacy_td_probe", "repo": REPO, "cases": {}}
    results["cases"]["1d_phase0"] = run_1d_case(0.0)
    results["cases"]["1d_phase_pi_2"] = run_1d_case(np.pi / 2.0)
    try:
        results["cases"]["3d_gpu_fallback"] = run_3d_gpu_fallback_case()
    except Exception as exc:  # pragma: no cover - report, do not crash
        results["cases"]["3d_gpu_fallback"] = {"error": f"{type(exc).__name__}: {exc}"}

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)

    for name, case in results["cases"].items():
        if "error" in case:
            print(f"{name}: ERROR {case['error']}")
        else:
            print(f"{name}: max|dpsi|={case['max_abs_diff']:.6e} "
                  f"first_step={case.get('first_step_diff', float('nan')):.6e} "
                  f"acceptance_1e-12={case['acceptance_1e-12']}")
    print("written:", OUT)


if __name__ == "__main__":
    main()
