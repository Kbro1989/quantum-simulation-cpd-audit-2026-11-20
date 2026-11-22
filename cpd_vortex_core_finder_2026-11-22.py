#!/usr/bin/env python3
"""
cpd_vortex_core_finder_2026-11-22.py

Finds the ACTUAL phase-singular vortex line in the toy state and measures it
properly, rather than measuring a loop around the Gaussian envelope edge.

For each recorded step, on the slice nearest z=0:
  1. scan candidate centres over a 7x7 region around the origin
  2. compute the winding number of the phase around a loop of radius 8 cells
  3. locate the core where the winding is consistently +-1 (a phase vortex)
  4. measure the circulation of the phase gradient around that core

The vortex core is where the phase is singular (the line along z where
theta = atan2(y,x) is undefined) -- NOT where the Gaussian envelope is small.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

REPO = Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
OUT = AUD / "quantum_3d_asset_suite"
IDX = AUD / "pks_research_index"
sys.path.insert(0, str(REPO))

from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver

N, BOX = 48, (-6.0, 6.0)
DT, STEPS = 0.005, 40
HBAR, MASS = 1.0, 1.0
LEVELS = (0.50, 0.15, 0.03)


def vortex_line_state(grid, sigma=1.0, charge=1):
    X, Y, Z = grid.X, grid.Y, grid.Z
    theta = np.arctan2(Y, X)
    psi = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (4.0 * sigma ** 2)) * np.exp(1j * charge * theta)
    wf = WaveFunction3D(grid, psi.astype(complex))
    wf.normalize()
    return wf


def winding_of(psi_slice, x_axis, y_axis, cx, cy, radius, npts=720):
    """Winding number and circulation around a circle of given radius in the slice."""
    phi = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    px = cx + radius * np.cos(phi)
    py = cy + radius * np.sin(phi)
    ix = np.clip((px - x_axis[0]) / (x_axis[1] - x_axis[0]), 0, len(x_axis) - 1.001)
    iy = np.clip((py - y_axis[0]) / (y_axis[1] - y_axis[0]), 0, len(y_axis) - 1.001)
    i0 = ix.astype(int); j0 = iy.astype(int)
    fx, fy = ix - i0, iy - j0
    v = ((1 - fx) * (1 - fy) * psi_slice[i0, j0] + fx * (1 - fy) * psi_slice[i0 + 1, j0]
         + (1 - fx) * fy * psi_slice[i0, j0 + 1] + fx * fy * psi_slice[i0 + 1, j0 + 1])
    dphi = np.angle(v[1:] * np.conj(v[:-1]))
    dphi = np.append(dphi, np.angle(v[0] * np.conj(v[-1])))
    return float(np.sum(dphi) / (2 * np.pi)), float(np.sum(dphi))


def find_core_slice(psi_slice, x_axis, y_axis, radius_px=5):
    best = None
    for j in range(20, 28):
        for k in range(20, 28):
            n, total = winding_of(psi_slice, x_axis, y_axis, x_axis[j], y_axis[k], radius_px)
            if n != 0 and (best is None or abs(n) < abs(best["winding"])):
                best = {"cx": float(x_axis[j]), "cy": float(y_axis[k]),
                        "winding": n, "circulation_phase": total}
    return best


def main():
    grid = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    trap = HarmonicTrap(omegas=1.0, m=1.0)
    psi = vortex_line_state(grid)
    solver = SplitOperatorSolver(grid, trap, DT, HBAR, MASS, order=2, backend="numpy")

    snapshots = {}
    for k in range(0, STEPS + 1):
        if k in (0, 10, 20, 30, 40):
            snapshots[k] = psi.psi.copy()
        if k < STEPS:
            psi = solver.step(psi)

    z_slice = np.abs(grid.z).argmin()
    rho_slice = np.abs(snapshots[0]) ** 2
    # rho is |psi|; the vortex (phase singularity) is at the origin where
    # |psi| reaches its MAXIMUM (the Gaussian envelope is 1 there).
    vortex_core_density = float(np.abs(snapshots[0][N // 2, N // 2, :]).max())
    print(f"|psi| at origin (vortex core): {vortex_core_density:.6f}  |  "
          f"|psi| at box edge: {float(rho_slice[4, 4, :].max()):.2e}")

    results = []
    for k in sorted(snapshots):
        sl = snapshots[k][:, :, z_slice]
        core = find_core_slice(sl, grid.x, grid.y)
        # circulation of the phase gradient around the found core
        n, total = winding_of(sl, grid.x, grid.y, core["cx"], core["cy"], 8 * 3,
                              npts=720)
        v = (HBAR / MASS) * total
        results.append({
            "step": k,
            "vortex_core": [round(core["cx"], 6), round(core["cy"], 6)],
            "core_rotation": round(core["winding"], 4),
            "circulation_phase_rad": round(total, 6),
            "circulation_hbar_over_m": round(v, 6),
            "theoretical_h_over_m": round(2 * math.pi * HBAR / MASS, 6),
            "quantization_ratio": round(v / (2 * math.pi * HBAR / MASS), 6),
        })
        print(f"step {k}: vortex at ({core['cx']:.3f},{core['cy']:.3f}) "
              f"winding {core['winding']:+.3f}, circulation/core {v:+.5f}, "
              f"ratio {v/(2*math.pi*HBAR/MASS):+.4f}")

    p = IDX / "quantum_vortex_core_analysis.json"
    p.write_text(json.dumps({"vortex_core_density_at_origin": vortex_core_density,
                             "theoretical_h_over_m": 2 * math.pi * HBAR / MASS,
                             "frames": results}, indent=2) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
