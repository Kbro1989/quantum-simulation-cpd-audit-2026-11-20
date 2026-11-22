#!/usr/bin/env python3
"""
cpd_vortex_regularized_2026-11-22.py

Closes two of the open physics gates from the audit:

  (a) REGULARIZED INITIAL STATE.  The state used until now,
        psi = A exp(-r^2/4 sigma^2) exp(i theta)
      has maximal amplitude on its axis, so it is a singular (non-regular) field
      and D1 core depletion fails by construction.  A regular singly-quantized
      vortex must satisfy psi ~ f(r) exp(i theta) with f(r) -> 0 as r -> 0:
        psi = A * r_perp * exp(-(r_perp^2 + z^2)/(4 sigma^2)) * exp(i theta)
      This is better posed: the amplitude vanishes linearly on the axis while the
      phase winding stays +1.

  (b) INDEPENDENT CIRCULATION.  Detector v3 computed Gamma from the same phase
      increments used for the winding number, so D4 restated D2.  Here Gamma is
      computed from the VELOCITY FIELD
        v = (hbar/m) Im(grad psi / psi)
      which is a different numerical route (gradient of the complex field, not a
      phase-difference sum), then integrated around the loop.

D1 (core depletion), D2 (winding), D3 (localisation) and D4 (independent
circulation) are reported per frame at two grid resolutions.
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

BOX, DT, STEPS = (-6.0, 6.0), 0.005, 40
HBAR, MASS, SIGMA = 1.0, 1.0, 1.0
FRAMES = (0, 10, 20, 30, 40)
RADII = (2.0, 3.0, 4.0)
GRIDS = (48, 64)


def build(N):
    g = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
    rperp = np.sqrt(X ** 2 + Y ** 2)
    psi = rperp * np.exp(-(rperp ** 2 + Z ** 2) / (4.0 * SIGMA ** 2)) * np.exp(
        1j * np.arctan2(Y, X))
    wf = WaveFunction3D(g, psi)
    wf.normalize()
    return g, wf


def bilinear(field, x_axis, y_axis, px, py):
    ix = np.clip((px - x_axis[0]) / (x_axis[1] - x_axis[0]), 0, len(x_axis) - 1.001)
    iy = np.clip((py - y_axis[0]) / (y_axis[1] - y_axis[0]), 0, len(y_axis) - 1.001)
    i0, j0 = ix.astype(int), iy.astype(int)
    fx, fy = ix - i0, iy - j0
    return ((1 - fx) * (1 - fy) * field[i0, j0] + fx * (1 - fy) * field[i0 + 1, j0]
            + (1 - fx) * fy * field[i0, j0 + 1] + fx * fy * field[i0 + 1, j0 + 1])


def winding(sl, xa, ya, cx, cy, r, npts=720):
    phi = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    px, py = cx + r * np.cos(phi), cy + r * np.sin(phi)
    v = bilinear(sl, xa, ya, px, py)
    d = np.angle(v[1:] * np.conj(v[:-1]))
    d = np.append(d, np.angle(v[0] * np.conj(v[-1])))
    return float(np.sum(d) / (2 * np.pi)), float(np.sum(d))


def circulation_velocity(psi3, g, cx, cy, r, npts=720):
    """Gamma = oint v.dl with v = (hbar/m) Im(grad psi / psi) -- independent of the
    phase-difference route."""
    k = int(np.abs(g.z).argmin())
    sl = psi3[:, :, k]
    eps = 1e-7
    inv = np.conj(sl) / (np.abs(sl) ** 2 + eps ** 2)
    dpx = (np.roll(sl, -1, 0) - np.roll(sl, 1, 0)) / (2 * g.dx)
    dpy = (np.roll(sl, -1, 1) - np.roll(sl, 1, 1)) / (2 * g.dy)
    vx = (HBAR / MASS) * (dpx * inv).imag
    vy = (HBAR / MASS) * (dpy * inv).imag

    phi = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    px, py = cx + r * np.cos(phi), cy + r * np.sin(phi)
    vx_s = bilinear(vx, g.x, g.y, px, py)
    vy_s = bilinear(vy, g.x, g.y, px, py)
    tx, ty = -np.sin(phi), np.cos(phi)
    ds = r * (2 * np.pi / npts)
    return float(np.sum((vx_s * tx + vy_s * ty) * ds))


def blind_core(sl, xa, ya, spacing=2.0):
    hits = []
    step = max(1, int(round(spacing / (xa[1] - xa[0]))))
    for j in range(4, len(xa) - 4, step):
        for k in range(4, len(ya) - 4, step):
            n, _ = winding(sl, xa, ya, xa[j], ya[k], spacing, npts=180)
            if abs(n) >= 0.9:
                hits.append((float(xa[j]), float(ya[k])))
    if not hits:
        return None
    a = np.array(hits)
    return float(a[:, 0].mean()), float(a[:, 1].mean())


def main():
    out = {"grid_convention": "dx = (hi-lo)/N; origin is a node iff N is even",
           "initial_state": "psi = A * r_perp * exp(-(r_perp^2+z^2)/(4 sigma^2)) * exp(i theta)",
           "hbar": HBAR, "mass": MASS, "sigma": SIGMA, "h_over_m": 2 * math.pi * HBAR / MASS,
           "radii": RADII, "grids": {}}
    for N in GRIDS:
        g, psi = build(N)
        i0 = N // 2
        solver = SplitOperatorSolver(g, HarmonicTrap(omegas=1.0, m=1.0), DT, HBAR, MASS,
                                     order=2, backend="numpy")
        print(f"\n===== N={N}  origin x[{i0}]={g.x[i0]:.6f} =====")
        rec = []
        for step in range(STEPS + 1):
            if step in FRAMES:
                k = int(np.abs(g.z).argmin())
                sl = psi.psi[:, :, k]
                rho = np.abs(sl) ** 2
                axis = float(rho[i0, i0])
                rr = np.sqrt(g.x[:, None] ** 2 + g.y[None, :] ** 2)
                ann = (rr >= 1.5) & (rr <= 2.5)
                annulus = float(rho[ann].mean())
                core = blind_core(sl, g.x, g.y)
                rows = []
                for r in RADII:
                    n, _ = winding(sl, g.x, g.y, 0.0, 0.0, r)
                    gam = circulation_velocity(psi.psi, g, 0.0, 0.0, r)
                    rows.append({"radius": r, "winding": round(n, 4),
                                 "gamma_velocity_field": round(gam, 6),
                                 "ratio_to_h_over_m": round(gam / (2 * math.pi * HBAR / MASS), 4)})
                rec.append({"step": step,
                            "axis_density": round(axis, 8),
                            "annulus_density": round(annulus, 8),
                            "depleted": bool(axis < 0.5 * annulus),
                            "blind_core": (None if core is None else [round(core[0], 4), round(core[1], 4)]),
                            "blind_error": (None if core is None else round(math.dist(core, (0.0, 0.0)), 4)),
                            "loops": rows})
                print(f" step {step:3d}: D1 axis={axis:.6f} ann={annulus:.6f} "
                      f"depleted={rec[-1]['depleted']}  D3 err={rec[-1]['blind_error']}")
                for l in rows:
                    print(f"        r={l['radius']}: winding={l['winding']:+.3f} "
                          f"Gamma={l['gamma_velocity_field']:+.5f} "
                          f"ratio={l['ratio_to_h_over_m']:+.4f}")
            if step < STEPS:
                psi = solver.step(psi)
        out["grids"][str(N)] = {"origin_index": i0, "origin_coordinate": float(g.x[i0]),
                                "dx": g.dx, "frames": rec}
    p = IDX / "quantum_vortex_regularized.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
