#!/usr/bin/env python3
"""
cpd_legacy_td_verdict_2026-11-21.py

Independent probe of the UNCOMMITTED working-tree change to the legacy
SplitStep solvers (CPD-P1-1).  Compares the legacy solvers against the
production SplitOperatorSolver on an explicitly time-dependent potential
(DipoleDrive) -- the exact acceptance case named in cpd_remediation_plan.md B1.

Acceptance (plan B1):  max|psi_legacy - psi_td| after 20 steps < 1e-12
for a DipoleDrive with phase=0.

Also tests a candidate correction (half-step at t, half-step at t+dt) without
touching the repository, and probes the SplitStep3DGPU CPU-fallback path.

This probe reads no audit artifact and imports only quantumlab.
"""
import json
import sys

import numpy as np
from scipy.fft import fft, ifft

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction3D
from quantumlab.potentials.time_dependent import DipoleDrive
from quantumlab.solvers.split_step_1d import SplitStep1DSolver
from quantumlab.solvers.split_operator import SplitOperatorSolver

OUT = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20\cpd_legacy_td_verdict_2026-11-21.json"


def corrected_strang_1d(leg, psi0, steps, dt):
    """Candidate fix: V(t) first half, V(t+dt) second half (matches SplitOperatorSolver)."""
    psi = psi0.psi.copy()
    for _ in range(steps):
        leg._update_operators(leg.t)
        psi = psi * leg.U_V
        psi = ifft(fft(psi) * leg.U_T)
        leg._update_operators(leg.t + dt)
        psi = psi * leg.U_V
        leg.t += dt
    return psi


def run_1d_case(phase, steps=20, dt=0.01, n=256):
    grid = Grid1D(n, -8.0, 8.0)
    pot = DipoleDrive(base=None, F0=1.0, omega=2.0, axis="x", phase=phase)

    psi0 = WaveFunction1D.gaussian(grid, 0.0, 1.0, 1.0)  # x0, k0, sigma

    prod = SplitOperatorSolver(grid, pot, dt, 1.0, 1.0, order=2, backend="numpy")
    leg = SplitStep1DSolver(grid, pot, dt, 1.0, 1.0)
    leg_fix = SplitStep1DSolver(grid, pot, dt, 1.0, 1.0)

    p_prod = psi0.psi.copy()
    p_leg = psi0.psi.copy()
    per_step = []
    for _ in range(steps):
        p_prod = prod.step(WaveFunction1D(grid, p_prod)).psi
        p_leg = leg.step(WaveFunction1D(grid, p_leg)).psi
        per_step.append(float(np.max(np.abs(p_leg - p_prod))))

    p_fix = corrected_strang_1d(leg_fix, psi0, steps, dt)

    d_leg = float(np.max(np.abs(p_leg - p_prod)))
    d_fix = float(np.max(np.abs(p_fix - p_prod)))
    return {
        "phase": phase,
        "steps": steps,
        "dt": dt,
        "legacy_vs_production": d_leg,
        "legacy_first_step_diff": per_step[0],
        "legacy_acceptance_1e-12": bool(d_leg < 1e-12),
        "candidate_fix_vs_production": d_fix,
        "candidate_fix_acceptance_1e-12": bool(d_fix < 1e-12),
        "per_step": per_step,
    }


def run_3d_gpu_fallback_case(steps=20, dt=0.01, n=32):
    """SplitStep3DGPU falls back to CPU when CuPy is absent; its step() was
    never wired to _update_operators, so the frozen-U_V defect survives there."""
    grid = Grid3D(n, -6.0, 6.0, n, -6.0, 6.0, n, -6.0, 6.0)
    pot = DipoleDrive(base=None, F0=1.0, omega=2.0, axis="x", phase=0.0)

    # x0, y0, z0 are positions; k0_* momenta; sigma_* widths
    psi0 = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    prod = SplitOperatorSolver(grid, pot, dt, 1.0, 1.0, order=2, backend="numpy")
    from quantumlab.solvers.split_step_3d_gpu import SplitStep3DGPU
    gpu = SplitStep3DGPU(grid, pot, dt, 1.0, 1.0)

    p_prod = psi0.psi.copy()
    p_gpu = psi0.psi.copy()
    for _ in range(steps):
        p_prod = prod.step(WaveFunction3D(grid, p_prod)).psi
        p_gpu = gpu.step(WaveFunction3D(grid, p_gpu)).psi

    d = float(np.max(np.abs(p_gpu - p_prod)))
    return {
        "gpu_backend_active": bool(getattr(gpu, "_gpu", False)),
        "steps": steps,
        "max_abs_diff": d,
        "acceptance_1e-12": bool(d < 1e-12),
    }


def main():
    results = {"probe": "cpd_legacy_td_verdict", "repo": REPO, "cases": {}}
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
        elif "legacy_vs_production" in case:
            print(f"{name}: legacy={case['legacy_vs_production']:.6e} "
                  f"(first_step {case['legacy_first_step_diff']:.3e}) "
                  f"fix={case['candidate_fix_vs_production']:.6e} "
                  f"legacy_ok={case['legacy_acceptance_1e-12']} fix_ok={case['candidate_fix_acceptance_1e-12']}")
        else:
            print(f"{name}: max|dpsi|={case['max_abs_diff']:.6e} ok={case['acceptance_1e-12']}")
    print("written:", OUT)


if __name__ == "__main__":
    main()
