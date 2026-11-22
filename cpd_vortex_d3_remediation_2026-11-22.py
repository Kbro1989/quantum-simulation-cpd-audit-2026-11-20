#!/usr/bin/env python3
"""
cpd_vortex_d3_remediation_2026-11-22.py

D3 REMEDIATION CANDIDATE -- not yet validated.

Gate 1 (b7b3391) established that the winding-disc CENTROID fails spatial
convergence while the topology stays intact.  This script implements two
replacement estimators and evaluates all three blind against an independent
density reference, on the same four Gate 1 configurations plus a finer grid.

Estimators
  A baseline_centroid      -- the existing estimator, kept for comparison
  B disc_intersection      -- intersect the +-1 discs from two loop radii
  C boundary_bisection     -- bisect the winding +1 -> 0 boundary along 4 axes

Reference (independent of all three)
  Central LOCAL density minimum, with prominence vs its annulus, competing-minimum
  count and separation, and sensitivity to the search-region size.  Its search
  region is declared from the grid, never from a detector's candidate coordinates.

Acceptance criteria -- fixed BEFORE running:
  ACC_BOUND_ERR    <= 1.0 grid unit, all frames
  ACC_REFINE       err(N=64) <= 1.2 * err(N=48)      (not worse under refinement)
  ACC_AGREE        |B - C| <= 0.5 grid unit
  ACC_UNAMBIGUOUS  competing minima == 1, no estimator switching
  ACC_BLIND        displaced synthetic vortices recovered within 0.5 grid unit
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
HIT_RADII = (2.0, 3.0)
Z_SLICES = (-2.0, 0.0, 2.0)
GRIDS = (48, 64, 96)
DTS = (0.005, 0.0025)

ACC_BOUND_ERR = 1.0
ACC_REFINE_FACTOR = 1.2
ACC_AGREE = 0.5
ACC_BLIND = 0.5


# ---------------------------------------------------------------- utilities
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


def hit_set(sl, xa, ya, radius, spacing):
    step = max(1, int(round(spacing / (xa[1] - xa[0]))))
    pts = []
    for j in range(3, len(xa) - 3, step):
        for k in range(3, len(ya) - 3, step):
            if abs(winding(sl, xa, ya, xa[j], ya[k], radius, npts=180)) >= 0.9:
                pts.append((float(xa[j]), float(ya[k])))
    return pts


# ---------------------------------------------------------------- estimators
def est_baseline(sl, xa, ya):
    """A: centroid of the +-1 disc (the estimator that failed Gate 1)."""
    hits = hit_set(sl, xa, ya, 2.0, 2.0)
    if not hits:
        return None
    a = np.array(hits)
    return {"core": (float(a[:, 0].mean()), float(a[:, 1].mean())),
            "extent": float(np.max(np.linalg.norm(a - a.mean(0), axis=1))), "n": len(hits)}


def est_disc_intersection(sl, xa, ya):
    """B: intersect the +-1 discs from two radii; report centroid and extent.

    The vortex lies inside every loop that winds +-1, so it lies in the
    intersection of the discs D(c, R) over all hits.  No median-based disc
    filtering: an earlier version kept only discs near the median hit, and that
    heuristic was found to be the cause of the N=64 coverage collapse (the hit
    set grows to ~180 points late in the run and the median wanders, discarding
    the discs that actually cover the core).  Coverage is reported explicitly
    instead of being hidden behind a None.
    """
    discs = []
    for R in HIT_RADII:
        for c in hit_set(sl, xa, ya, R, 1.0):
            discs.append((c[0], c[1], R))
    if not discs:
        return {"core": None, "extent": None, "n": 0, "area": 0, "coverage": "no_hits"}
    xs = np.array([d[0] for d in discs]); ys = np.array([d[1] for d in discs])
    Rmax = max(d[2] for d in discs)
    step = 0.5
    gx = np.arange(xs.min() - Rmax, xs.max() + Rmax + 1e-9, step)
    gy = np.arange(ys.min() - Rmax, ys.max() + Rmax + 1e-9, step)
    X, Y = np.meshgrid(gx, gy, indexing="ij")
    inside = np.ones(X.shape, dtype=bool)
    for cx, cy, R in discs:
        inside &= ((X - cx) ** 2 + (Y - cy) ** 2) <= R * R
    area = int(inside.sum())
    if area == 0:
        return {"core": None, "extent": None, "n": len(discs), "area": 0,
                "coverage": "empty_intersection"}
    px, py = X[inside], Y[inside]
    core = (float(px.mean()), float(py.mean()))
    return {"core": core, "extent": float(np.max(np.hypot(px - core[0], py - core[1]))),
            "n": len(discs), "area": area, "coverage": "ok"}


def est_boundary_bisection(sl, xa, ya):
    """C: bisect the winding +1 -> 0 boundary along +-x and +-y from an interior hit."""
    hits = hit_set(sl, xa, ya, 2.0, 1.0)
    if not hits:
        return None
    a = np.array(hits)
    start = (float(a[:, 0].mean()), float(a[:, 1].mean()))
    crossings = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        lo, hi = 0.0, 6.0
        if abs(winding(sl, xa, ya, start[0] + dx * hi, start[1] + dy * hi, 2.0)) >= 0.9:
            continue
        for _ in range(28):
            mid = 0.5 * (lo + hi)
            if abs(winding(sl, xa, ya, start[0] + dx * mid, start[1] + dy * mid, 2.0)) >= 0.9:
                lo = mid
            else:
                hi = mid
        crossings.append((start[0] + dx * 0.5 * (lo + hi), start[1] + dy * 0.5 * (lo + hi)))
    if len(crossings) < 4:
        return None
    c = np.array(crossings)
    core = (float(c[:, 0].mean()), float(c[:, 1].mean()))
    return {"core": core, "extent": float(np.max(np.linalg.norm(c - core, axis=1))),
            "n": len(crossings)}


ESTIMATORS = {"baseline_centroid": est_baseline,
              "disc_intersection": est_disc_intersection,
              "boundary_bisection": est_boundary_bisection}


# ---------------------------------------------------------------- reference
def reference(rho, xa, ya, rmax=3.0, rel=0.05):
    """Central LOCAL density minimum + prominence + competing minima. Never uses a
    detector's candidate coordinates."""
    rr = np.sqrt(xa[:, None] ** 2 + ya[None, :] ** 2)
    mask = rr <= rmax
    thr = rel * float(rho.max())
    mins = []
    for j in range(1, rho.shape[0] - 1):
        for k in range(1, rho.shape[1] - 1):
            if not mask[j, k]:
                continue
            v = rho[j, k]
            if v < thr and v <= rho[j - 1:j + 2, k - 1:k + 2].min():
                mins.append((float(xa[j]), float(ya[k]), float(v)))
    if not mins:
        return None
    core = min(mins, key=lambda m: m[2])
    ann = (rr >= 1.5) & (rr <= 2.5)
    annulus = float(rho[ann].mean()) if ann.any() else float("nan")
    prominence = (annulus - core[2]) / annulus if annulus > 0 else float("nan")
    sep = min((math.dist((m[0], m[1]), (n[0], n[1])) for i, m in enumerate(mins)
               for n in mins[i + 1:]), default=float("nan"))
    gi = int(np.argmin(np.abs(xa - core[0])))
    gj = int(np.argmin(np.abs(ya - core[1])))
    return {"core": core[:2], "density": core[2], "annulus": annulus,
            "prominence": prominence, "competing": len(mins), "min_sep": sep,
            "grid_ij": [gi, gj]}


# ---------------------------------------------------------------- state
def build(N, displacement=(0.0, 0.0)):
    g = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
    dx_, dy_ = X - displacement[0], Y - displacement[1]
    rperp = np.sqrt(dx_ ** 2 + dy_ ** 2)
    theta = np.arctan2(dy_, dx_)
    psi = rperp * np.exp(-(rperp ** 2 + Z ** 2) / (4.0 * SIGMA ** 2)) * np.exp(1j * theta)
    wf = WaveFunction3D(g, psi)
    wf.normalize()
    return g, wf


def evaluate(sl, rho, xa, ya):
    ref = reference(rho, xa, ya)
    out = {"reference": ref}
    for name, fn in ESTIMATORS.items():
        try:
            r = fn(sl, xa, ya)
        except Exception as e:
            r = {"error": str(e)}
        if r and r.get("core") is not None:
            r["err_vs_ref"] = (None if ref is None else
                               round(math.dist(r["core"], ref["core"]), 4))
        out[name] = r
    if out["disc_intersection"] and out["boundary_bisection"]:
        d, b = out["disc_intersection"], out["boundary_bisection"]
        if d.get("core") is not None and b.get("core") is not None:
            out["B_vs_C"] = round(math.dist(d["core"], b["core"]), 4)
    return out


def main():
    out = {"remediation": "D3 estimator candidates -- NOT YET VALIDATED",
           "baseline": "b7b3391 Gate 1 D3 failure (immutable)",
           "acceptance": {"ACC_BOUND_ERR": ACC_BOUND_ERR, "ACC_REFINE_FACTOR": ACC_REFINE_FACTOR,
                          "ACC_AGREE": ACC_AGREE, "ACC_BLIND": ACC_BLIND,
                          "ACC_UNAMBIGUOUS": "competing minima == 1"},
           "hit_radii": HIT_RADII, "frames": list(FRAMES), "runs": []}
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
                        ev = evaluate(sl, rho, g.x, g.y)
                        ev["slice_index"] = k
                        ev["reference_region_sensitivity"] = {
                            str(r): (lambda rr: None if rr is None else
                                     {"core": [round(rr["core"][0], 3), round(rr["core"][1], 3)],
                                      "competing": rr["competing"]})(reference(rho, g.x, g.y, rmax=r))
                            for r in (2.0, 3.0, 4.0)}
                        fr["slices"][str(zv)] = ev
                        b = ev["baseline_centroid"]; d = ev["disc_intersection"]; c = ev["boundary_bisection"]
                        print(f" step {step:3d} z={zv:+.0f}: "
                              f"A={b.get('core') if b else None} "
                              f"B={d.get('core') if d else None} "
                              f"C={c.get('core') if c else None} "
                              f"B-C={ev.get('B_vs_C')} ref={ev['reference']['core'] if ev['reference'] else None} "
                              f"errB={d.get('err_vs_ref') if d else None} errC={c.get('err_vs_ref') if c else None}")
                    run["frames"].append(fr)
                if step < STEPS:
                    psi = solver.step(psi)
            out["runs"].append(run)

    # ---- blind displaced-profile tests (no displacement fed to any estimator) ----
    print("\n===== BLIND DISPLACED-PROFILE TESTS =====")
    blind = []
    for disp in [(1.5, -1.0), (-2.0, 1.5), (0.0, 2.5)]:
        g, psi = build(48, displacement=disp)
        k = int(np.abs(g.z).argmin())
        sl = psi.psi[:, :, k]
        rho = np.abs(sl) ** 2
        ev = evaluate(sl, rho, g.x, g.y)
        row = {"true_displacement": list(disp), "reference": ev["reference"]["core"] if ev["reference"] else None}
        for name in ESTIMATORS:
            r = ev[name]
            if not r or r.get("core") is None:
                row[name] = None
            else:
                row[name] = {"core": [round(r["core"][0], 4), round(r["core"][1], 4)],
                             "error": round(math.dist(r["core"], disp), 4)}
        row["PASS"] = all(row[n] and row[n]["error"] <= ACC_BLIND for n in ESTIMATORS)
        blind.append(row)
        print(f" true={disp} ref={row['reference']} "
              f"A={row['baseline_centroid']} B={row['disc_intersection']} "
              f"C={row['boundary_bisection']} PASS={row['PASS']}")
    out["blind_tests"] = blind
    p = IDX / "quantum_vortex_d3_remediation.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
