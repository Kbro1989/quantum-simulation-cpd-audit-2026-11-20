#!/usr/bin/env python3
"""
cpd_vortex_detector_v3_2026-11-22.py

v2 established two facts that change the detector design:

  1. quantumlab's Grid3D(N, lo, hi, ...) uses spacing dx = (hi - lo) / N with N
     points.  Therefore x[N//2] == 0 EXACTLY iff N is EVEN.  With N=49 the
     "origin" index 24 sits at x = -0.122449, so the imposed vortex is sampled
     off-centre.  N=48 puts the origin exactly on node 24.
  2. A winding loop of radius R around a candidate centre returns +-1 for every
     centre within R of the vortex, so a hit-list is a DISC, not a point.  The
     core must be localised as the centroid of that disc.

This version:
  * N = 48 (origin exactly on node 24),
  * D1 measured TRANSVERSELY (axis density vs the surrounding annulus at the
    same z) - the previous version compared against the z-extremes, which is
    not a core-depletion test,
  * blind localisation by lattice winding with radius == lattice spacing,
    core = centroid of the +-1 disc,
  * analytical reference loops at four radii, reported separately,
  * circulation Gamma vs h/m.
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

N, BOX, DT, STEPS = 48, (-6.0, 6.0), 0.005, 40
HBAR, MASS, SIGMA = 1.0, 1.0, 1.0
FRAMES = (0, 10, 20, 30, 40)
RADII = (2.0, 3.0, 4.0, 5.0)
Z_SLICES = (-2.0, 0.0, 2.0)
ORIGIN_IDX = N // 2          # exact zero because N is even


def winding(psi_slice, x_axis, y_axis, cx, cy, radius, npts=360):
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


def blind_localise(psi_slice, x_axis, y_axis, spacing=2.0):
    """Lattice winding with loop radius == spacing; core = centroid of the +-1 disc."""
    hits = []
    j = 4
    while j < len(x_axis) - 4:
        k = 4
        while k < len(y_axis) - 4:
            n, _ = winding(psi_slice, x_axis, y_axis, x_axis[j], y_axis[k], spacing, npts=180)
            if abs(n) >= 0.9:
                hits.append((float(x_axis[j]), float(y_axis[k])))
            k += max(1, int(round(spacing / (y_axis[1] - y_axis[0]))))
        j += max(1, int(round(spacing / (x_axis[1] - x_axis[0]))))
    if not hits:
        return None, 0
    arr = np.array(hits)
    return (float(arr[:, 0].mean()), float(arr[:, 1].mean())), len(hits)


def main():
    grid = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    trap = HarmonicTrap(omegas=1.0, m=1.0)
    x = grid.x
    print(f"grid N={N}  dx={grid.dx:.9f}  x[0]={x[0]:.6f}  x[N//2]={x[ORIGIN_IDX]:.9f}  "
          f"x[N-1]={x[-1]:.6f}")
    print(f"origin exactly on a node: {abs(x[ORIGIN_IDX]) < 1e-12}\n")

    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    psi = WaveFunction3D(grid, np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (4.0 * SIGMA ** 2))
                         * np.exp(1j * np.arctan2(Y, X)))
    psi.normalize()
    solver = SplitOperatorSolver(grid, trap, DT, HBAR, MASS, order=2)

    # D1 - TRANSVERSE core depletion at z=0
    k0 = int(np.abs(grid.z).argmin())
    sl0 = np.abs(psi.psi[:, :, k0]) ** 2
    axis_rho = float(sl0[ORIGIN_IDX, ORIGIN_IDX])
    rr = np.sqrt(X[:, :, 0] ** 2 + Y[:, :, 0] ** 2)
    ann = (rr >= 1.5) & (rr <= 2.5)
    annulus_rho = float(sl0[:, :][ann].mean()) if ann.any() else float("nan")
    print(f"D1 transverse core depletion at z=0:")
    print(f"   rho on axis = {axis_rho:.6f}   rho in annulus 1.5<r<2.5 = {annulus_rho:.6f}")
    print(f"   -> {'DEPLETED' if axis_rho < 0.5 * annulus_rho else 'NOT DEPLETED (axis is a density maximum)'}\n")

    z_idx = {round(float(zv), 6): int(np.abs(grid.z - zv).argmin()) for zv in Z_SLICES}
    out_frames = []
    for step in range(STEPS + 1):
        if step in FRAMES:
            rec = {"step": step, "z_slices": {}}
            for zv, k in z_idx.items():
                sl = psi.psi[:, :, k]
                ref = []
                for r in RADII:
                    n, tot = winding(sl, grid.x, grid.y, 0.0, 0.0, r)
                    ref.append({"radius": r, "winding": round(n, 4),
                                "circulation_hbar_over_m": round(HBAR / MASS * tot, 6),
                                "ratio_to_h_over_m": round(
                                    (HBAR / MASS * tot) / (2 * math.pi * HBAR / MASS), 4)})
                core, nhits = blind_localise(sl, grid.x, grid.y)
                rec["z_slices"][str(zv)] = {
                    "slice_index": k,
                    "analytical_axis": [0.0, 0.0],
                    "analytical_reference_loops": ref,
                    "blind_core": (None if core is None else [round(core[0], 4), round(core[1], 4)]),
                    "blind_hit_count": nhits,
                    "blind_core_error": (None if core is None else round(
                        math.dist(core, (0.0, 0.0)), 4)),
                }
                print(f"step {step:3d} z={zv:+.0f}: analytical "
                      f"{[(l['radius'], l['winding']) for l in ref]}  "
                      f"blind_core={rec['z_slices'][str(zv)]['blind_core']} "
                      f"err={rec['z_slices'][str(zv)]['blind_core_error']}")
            out_frames.append(rec)
        if step < STEPS:
            psi = solver.step(psi)

    out = {
        "grid": {"N": N, "box": BOX, "dx": grid.dx,
                 "origin_index": ORIGIN_IDX, "origin_coordinate": float(x[ORIGIN_IDX]),
                 "origin_exact": bool(abs(x[ORIGIN_IDX]) < 1e-12),
                 "convention": "dx = (hi-lo)/N; x[N//2] == 0 iff N is even"},
        "dt": DT, "steps": STEPS, "sigma": SIGMA, "hbar": HBAR, "mass": MASS,
        "h_over_m": 2 * math.pi * HBAR / MASS,
        "D1_core_depletion": {
            "axis_density": axis_rho, "annulus_density": annulus_rho,
            "depleted": bool(axis_rho < 0.5 * annulus_rho),
            "note": "imposed state |psi| = A exp(-r^2/4 sigma^2) is maximal on the axis",
        },
        "radii_grid_units": list(RADII), "z_slices_grid_units": list(Z_SLICES),
        "frames": out_frames,
    }
    p = IDX / "quantum_vortex_detector_v3.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
