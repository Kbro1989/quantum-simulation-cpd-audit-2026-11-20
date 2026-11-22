#!/usr/bin/env python3
"""
cpd_vortex_detector_v2_2026-11-22.py

Corrected vortex diagnostics.  Changes from v1:

  * N = 49 (odd) so the coordinate origin is represented exactly by index N//2.
  * The ANALYTICAL reference (the imposed vortex is a singly quantised line on
    the z-axis) is reported separately from the BLIND detector prediction.
  * The blind detector is phase-based (winding localisation over the whole
    plane), not a global density minimum - a density minimum cannot find this
    vortex because |psi| is MAXIMAL on its axis by construction.
  * Winding is measured at several loop radii, on several z-slices, so a
    single-radius result cannot pass by accident.
  * Circulation Gamma = (hbar/m) * sum(dphi) is compared with h/m.
  * D1 (core depletion) is measured along the TRUE z-axis, rho[ix0, iy0, :].

Writes a separate artifact; the original GIF is never overwritten.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

REPO = Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
IDX = AUD / "pks_research_index"
sys.path.insert(0, str(REPO))

from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver

N, BOX, DT, STEPS = 49, (-6.0, 6.0), 0.005, 40
HBAR, MASS = 1.0, 1.0
SIGMA = 1.0
FRAMES = (0, 10, 20, 30, 40)
RADII = (2.0, 3.0, 4.0, 5.0)          # grid units
Z_SLICES = (-2.0, 0.0, 2.0)           # grid units
ORIGIN_IDX = N // 2                   # exact, because N is odd


def winding(psi_slice, x_axis, y_axis, cx, cy, radius, npts=720):
    phi = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    px = cx + radius * np.cos(phi)
    py = cy + radius * np.sin(phi)
    ix = np.clip((px - x_axis[0]) / (x_axis[1] - x_axis[0]), 0, len(x_axis) - 1.001)
    iy = np.clip((py - y_axis[0]) / (y_axis[1] - y_axis[0]), 0, len(y_axis) - 1.001)
    i0, j0 = ix.astype(int), iy.astype(int)
    fx, fy = ix - i0, iy - j0
    v = ((1 - fx) * (1 - fy) * psi_slice[i0, j0] + fx * (1 - fy) * psi_slice[i0 + 1, j0]
         + (1 - fx) * fy * psi_slice[i0, j0 + 1] + fx * fy * psi_slice[i0 + 1, j0 + 1])
    dphi = np.angle(v[1:] * np.conj(v[:-1]))
    dphi = np.append(dphi, np.angle(v[0] * np.conj(v[-1])))
    return float(np.sum(dphi) / (2 * np.pi)), float(np.sum(dphi))


def blind_detector(psi_slice, x_axis, y_axis, radius):
    """Phase-winding localisation over the whole plane (no density prior)."""
    hits = []
    for j in range(4, len(x_axis) - 4):
        for k in range(4, len(y_axis) - 4):
            n, total = winding(psi_slice, x_axis, y_axis, x_axis[j], y_axis[k], radius, npts=180)
            if abs(n) >= 0.9:
                hits.append((float(x_axis[j]), float(y_axis[k]), n, total))
    return hits


def main():
    grid = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    trap = HarmonicTrap(omegas=1.0, m=1.0)
    x = grid.x
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    psi_arr = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (4.0 * SIGMA ** 2)) * np.exp(
        1j * np.arctan2(Y, X))
    psi = WaveFunction3D(grid, psi_arr)
    psi.normalize()
    solver = SplitOperatorSolver(grid, trap, DT, HBAR, MASS, order=2)

    ix0 = ORIGIN_IDX
    iy0 = ORIGIN_IDX
    axis = np.abs(psi.psi[ix0, iy0, :]) ** 2
    print(f"grid N={N}  origin index={ORIGIN_IDX} -> x={x[ORIGIN_IDX]:.6f}, y={x[iy0]:.6f}")
    print(f"D1 core depletion along the TRUE z-axis: rho(0,0,z) min={axis.min():.6f} "
          f"max={axis.max():.6f}  -> {'DEPLETED' if axis.min() < 0.1 * axis.max() else 'NOT DEPLETED'}")
    print(f"   (imposed state has |psi| = A*exp(-r^2/4s^2), maximal on the axis by construction)\n")

    z_idx = {round(float(zv), 6): int(np.abs(grid.z - zv).argmin()) for zv in Z_SLICES}

    out_frames = []
    for step in range(STEPS + 1):
        if step in FRAMES:
            rec = {"step": step, "z_slices": {}}
            for zv, k in z_idx.items():
                sl = psi.psi[:, :, k]
                # analytical reference axis
                ref = []
                for r in RADII:
                    n, tot = winding(sl, grid.x, grid.y, 0.0, 0.0, r)
                    ref.append({"radius": r, "winding": round(n, 4),
                                "circulation_hbar_over_m": round(HBAR / MASS * tot, 6),
                                "ratio_to_h_over_m": round(
                                    (HBAR / MASS * tot) / (2 * math.pi * HBAR / MASS), 4)})
                blind = blind_detector(sl, grid.x, grid.y, radius=4.0)
                rec["z_slices"][str(zv)] = {
                    "slice_index": k,
                    "analytical_axis": [0.0, 0.0],
                    "analytical_reference_loops": ref,
                    "blind_detector_hits": [
                        {"x": round(h[0], 4), "y": round(h[1], 4),
                         "winding": round(h[2], 4)} for h in blind[:8]],
                    "blind_detector_hit_count": len(blind),
                    "blind_detector_finds_origin": any(
                        abs(h[0]) < 0.6 and abs(h[1]) < 0.6 for h in blind),
                }
                print(f"step {step:3d} z={zv:+.0f}: analytical loops "
                      f"{[(l['radius'], l['winding']) for l in ref]}  "
                      f"blind hits={len(blind)} origin_found="
                      f"{rec['z_slices'][str(zv)]['blind_detector_finds_origin']}")
            out_frames.append(rec)
        if step < STEPS:
            psi = solver.step(psi)

    out = {
        "grid_N": N, "box": BOX, "dt": DT, "steps": STEPS, "sigma": SIGMA,
        "hbar": HBAR, "mass": MASS, "origin_index": ORIGIN_IDX,
        "origin_coordinate": [float(x[ORIGIN_IDX]), float(x[iy0])],
        "D1_core_depletion": {
            "axis_density_min": float(axis.min()),
            "axis_density_max": float(axis.max()),
            "depleted": bool(axis.min() < 0.1 * axis.max()),
            "note": "imposed state |psi| = A exp(-r^2/4 sigma^2) is maximal on the axis",
        },
        "radii_grid_units": list(RADII),
        "z_slices_grid_units": list(Z_SLICES),
        "h_over_m": 2 * math.pi * HBAR / MASS,
        "frames": out_frames,
    }
    p = IDX / "quantum_vortex_detector_v2.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
