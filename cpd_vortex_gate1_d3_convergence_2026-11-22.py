#!/usr/bin/env python3
"""
cpd_vortex_gate1_d3_convergence_2026-11-22.py

GATE 1 — D3 temporal and spatial convergence, as a separate validation gate from
GPE stationarity.

The detector under test is the phase-winding centroid.  Its reference is built by
a DIFFERENT physical observable: the transverse density minimum.  For a regularised
vortex the core is a density hole, so the density minimum is an independent
localisation that does not use phase winding at all.  Comparing the two separates

  * physical vortex motion   -> both references move together
  * detector bias            -> only the winding centroid moves
  * numerical instability   -> the density field becomes multi-modal / noisy

The initial axis is NOT used as ground truth after evolution, per the gate spec.

Swept: N in {48, 64}, dt in {0.005, 0.0025}, steps to 200, loop radii {2,3,4},
three z-slices.  Recorded per frame: core-position error, localization error,
winding on loops around each reference, density at the core, and the number of
competing transverse minima.
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

BOX, STEPS = (-6.0, 6.0), 200
HBAR, MASS, SIGMA = 1.0, 1.0, 1.0
FRAMES = tuple(range(0, STEPS + 1, 20))
RADII = (2.0, 3.0, 4.0)
Z_SLICES = (-2.0, 0.0, 2.0)
GRIDS = (48, 64)
DTS = (0.005, 0.0025)


def build(N):
    g = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
    rperp = np.sqrt(X ** 2 + Y ** 2)
    psi = rperp * np.exp(-(rperp ** 2 + Z ** 2) / (4.0 * SIGMA ** 2)) * np.exp(
        1j * np.arctan2(Y, X))
    wf = WaveFunction3D(g, psi)
    wf.normalize()
    return g, wf


def bilinear(field, xa, ya, px, py):
    ix = np.clip((px - xa[0]) / (xa[1] - xa[0]), 0, len(xa) - 1.001)
    iy = np.clip((py - ya[0]) / (ya[1] - ya[0]), 0, len(ya) - 1.001)
    i0, j0 = ix.astype(int), iy.astype(int)
    fx, fy = ix - i0, iy - j0
    return ((1 - fx) * (1 - fy) * field[i0, j0] + fx * (1 - fy) * field[i0 + 1, j0]
            + (1 - fx) * fy * field[i0, j0 + 1] + fx * fy * field[i0 + 1, j0 + 1])


def winding(sl, xa, ya, cx, cy, r, npts=360):
    phi = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    v = bilinear(sl, xa, ya, cx + r * np.cos(phi), cy + r * np.sin(phi))
    d = np.angle(v[1:] * np.conj(v[:-1]))
    d = np.append(d, np.angle(v[0] * np.conj(v[-1])))
    return float(np.sum(d) / (2 * np.pi))


def winding_centroid(sl, xa, ya, spacing):
    """Detector under test: centroid of the +-1 winding disc."""
    step = max(1, int(round(spacing / (xa[1] - xa[0]))))
    hits = []
    for j in range(4, len(xa) - 4, step):
        for k in range(4, len(ya) - 4, step):
            if abs(winding(sl, xa, ya, xa[j], ya[k], spacing, npts=180)) >= 0.9:
                hits.append((float(xa[j]), float(ya[k])))
    if not hits:
        return None
    a = np.array(hits)
    return float(a[:, 0].mean()), float(a[:, 1].mean())


def _central_local_minima(rho, xa, ya, rmax=3.0, rel=0.05):
    """Local minima of the transverse density inside r <= rmax.

    The GLOBAL density minimum is NOT usable here: for a regularised vortex in a
    Gaussian envelope the tail at the box edge is lower than the core.  The core is
    a LOCAL minimum relative to its surroundings, so the search is restricted to a
    declared central region and reports every competing minimum in it.
    """
    rr = np.sqrt(xa[:, None] ** 2 + ya[None, :] ** 2)
    mask = rr <= rmax
    thr = rel * float(rho.max())
    out = []
    for j in range(1, rho.shape[0] - 1):
        for k in range(1, rho.shape[1] - 1):
            if not mask[j, k]:
                continue
            v = rho[j, k]
            if v < thr and v <= rho[j - 1:j + 2, k - 1:k + 2].min():
                out.append((float(xa[j]), float(ya[k]), float(v)))
    return out


def density_reference(rho, xa, ya, rmax=3.0):
    """Independent reference: deepest central local density minimum (no phase)."""
    mins = _central_local_minima(rho, xa, ya, rmax)
    if not mins:
        return None
    return min(mins, key=lambda m: m[2])


def competing_minima(rho, xa, ya, rmax=3.0):
    return len(_central_local_minima(rho, xa, ya, rmax))


def main():
    out = {"gate": "GATE 1 - D3 temporal and spatial convergence",
           "detector_under_test": "phase-winding centroid",
           "independent_reference": "transverse density minimum",
           "initial_state": "psi = A*r_perp*exp(-(r_perp^2+z^2)/4 sigma^2)*exp(i theta)",
           "steps": STEPS, "frames": list(FRAMES), "radii": list(RADII),
           "z_slices": list(Z_SLICES), "h_over_m": 2 * math.pi * HBAR / MASS,
           "runs": []}
    for N in GRIDS:
        for dt in DTS:
            g, psi = build(N)
            solver = SplitOperatorSolver(g, HarmonicTrap(omegas=1.0, m=1.0), dt, HBAR, MASS,
                                         order=2, backend="numpy")
            run = {"N": N, "dt": dt, "dx": g.dx, "frames": []}
            print(f"\n===== N={N} dt={dt} =====")
            for step in range(STEPS + 1):
                if step in FRAMES:
                    fr = {"step": step, "slices": {}}
                    for zv in Z_SLICES:
                        k = int(np.abs(g.z - zv).argmin())
                        sl = psi.psi[:, :, k]
                        rho = np.abs(sl) ** 2
                        det = winding_centroid(sl, g.x, g.y, 2.0)
                        ref = density_reference(rho, g.x, g.y)
                        nm = competing_minima(rho, g.x, g.y)
                        loops_det = [round(winding(sl, g.x, g.y, det[0], det[1], r), 3)
                                     if det else None for r in RADII]
                        loops_ref = ([round(winding(sl, g.x, g.y, ref[0], ref[1], r), 3)
                                      for r in RADII] if ref else None)
                        err = (None if (det is None or ref is None) else
                               round(math.dist(det, (ref[0], ref[1])), 4))
                        fr["slices"][str(zv)] = {
                            "slice_index": k,
                            "detector_core": (None if det is None else [round(det[0], 4), round(det[1], 4)]),
                            "reference_core": (None if ref is None else [round(ref[0], 4), round(ref[1], 4)]),
                            "detector_vs_reference_error": err,
                            "reference_core_density": (None if ref is None else round(ref[2], 9)),
                            "competing_minima": nm,
                            "winding_around_detector": loops_det,
                            "winding_around_reference": loops_ref,
                        }
                    run["frames"].append(fr)
                    s0 = fr["slices"]["0.0"]
                    print(f" step {step:3d}: det={s0['detector_core']} ref={s0['reference_core']} "
                          f"err={s0['detector_vs_reference_error']} "
                          f"minima={s0['competing_minima']} "
                          f"w_det={s0['winding_around_detector']} w_ref={s0['winding_around_reference']}")
                if step < STEPS:
                    psi = solver.step(psi)
            out["runs"].append(run)
    p = IDX / "quantum_vortex_gate1_d3.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
