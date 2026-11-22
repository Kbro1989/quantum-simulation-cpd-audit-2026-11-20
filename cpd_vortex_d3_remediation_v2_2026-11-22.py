#!/usr/bin/env python3
"""
cpd_vortex_d3_remediation_v2_2026-11-22.py

D3 REMEDIATION REVISION 2 -- corrected measurement geometry.  Not validated.

Why this revision exists: in revision 1 the bilinear sampler CLAMPED out-of-domain
loop samples to the grid edge.  A loop hanging off the domain therefore re-sampled
boundary values, which can manufacture winding.  That contaminates the +-1 hit set
and can explain its growth, so no physical conclusion may be drawn from revision 1's
hit-set growth until boundary contamination is excluded.

Corrections, per the remediation spec:
  1. Bilinear sampling rejects any loop that is not wholly inside the valid
     interpolation domain.  Nothing is clamped.
  2. hit_set keeps only boundary-valid centres and records valid vs rejected loop
     counts separately, per frame / grid / z-slice.
  3. Hit-set growth is re-measured on valid loops only.
  4. The fixed 0.5-unit disc lattice is replaced by a continuous feasibility test
     (max-min slack over the true intersection of the discs).  Reference-core
     containment is reported as a DIAGNOSTIC, never used as an estimator input.
  5. Boundary bisection verifies the starting classification, establishes valid
     opposite-classification brackets, rejects invalid loops, and retains all four
     crossing coordinates.
  6. The original centroid is kept as a baseline CONTROL, excluded from the
     replacement-estimator PASS criterion.
  7. Acceptance is a separate executable (cpd_vortex_d3_acceptance_2026-11-22.py).
  8. Output is strict JSON: NaN -> null.
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
RADII = (2.0, 3.0)
Z_SLICES = (-2.0, 0.0, 2.0)
GRIDS = (48, 64, 96)
DTS = (0.005, 0.0025)


# ---------------------------------------------------------------- geometry
def loop_valid(xa, ya, cx, cy, r):
    """The whole loop must lie inside the valid interpolation domain."""
    return (cx - r) >= xa[0] and (cx + r) <= xa[-1] and \
           (cy - r) >= ya[0] and (cy + r) <= ya[-1]


def bilinear(f, xa, ya, px, py):
    # loop_valid() already guarantees the samples are inside the domain; the
    # minimum() only handles the final cell (px == xa[-1] would otherwise index
    # one past the end).  No out-of-domain sample is ever clamped.
    ix = (px - xa[0]) / (xa[1] - xa[0])
    iy = (py - ya[0]) / (ya[1] - ya[0])
    i0 = np.minimum(np.floor(ix).astype(int), len(xa) - 2)
    j0 = np.minimum(np.floor(iy).astype(int), len(ya) - 2)
    fx = ix - i0; fy = iy - j0
    return ((1-fx)*(1-fy)*f[i0, j0] + fx*(1-fy)*f[i0+1, j0]
            + (1-fx)*fy*f[i0, j0+1] + fx*fy*f[i0+1, j0+1])


def winding(sl, xa, ya, cx, cy, r, npts=360):
    """Winding number, or None if the loop is not wholly inside the domain."""
    if not loop_valid(xa, ya, cx, cy, r):
        return None
    phi = np.linspace(0, 2*np.pi, npts, endpoint=False)
    v = bilinear(sl, xa, ya, cx + r*np.cos(phi), cy + r*np.sin(phi))
    d = np.angle(v[1:]*np.conj(v[:-1]))
    d = np.append(d, np.angle(v[0]*np.conj(v[-1])))
    return float(np.sum(d) / (2*np.pi))


def hit_set(sl, xa, ya, radius, spacing=1.0):
    """Valid +-1 centres only; rejected loops counted separately."""
    step = max(1, int(round(spacing / (xa[1] - xa[0]))))
    hits, n_valid, n_rej = [], 0, 0
    for j in range(len(xa)):
        for k in range(len(ya)):
            if (j % step) or (k % step):
                continue
            if not loop_valid(xa, ya, xa[j], ya[k], radius):
                n_rej += 1
                continue
            n_valid += 1
            if abs(winding(sl, xa, ya, xa[j], ya[k], radius)) >= 0.9:
                hits.append((float(xa[j]), float(ya[k])))
    return hits, n_valid, n_rej


# ---------------------------------------------------------------- reference
def reference(rho, xa, ya, rmax=3.0, rel=0.05):
    rr = np.sqrt(xa[:, None] ** 2 + ya[None, :] ** 2)
    mask = rr <= rmax
    thr = rel * float(rho.max())
    mins = []
    for j in range(1, rho.shape[0] - 1):
        for k in range(1, rho.shape[1] - 1):
            if not mask[j, k]:
                continue
            v = rho[j, k]
            if v < thr and v <= rho[j-1:j+2, k-1:k+2].min():
                mins.append((float(xa[j]), float(ya[k]), float(v)))
    if not mins:
        return None
    core = min(mins, key=lambda m: m[2])
    ann = (rr >= 1.5) & (rr <= 2.5)
    annulus = float(rho[ann].mean()) if ann.any() else None
    prominence = ((annulus - core[2]) / annulus) if (annulus and annulus > 0) else None
    sep = min((math.dist((m[0], m[1]), (n[0], n[1])) for i, m in enumerate(mins)
               for n in mins[i+1:]), default=None)
    return {"core": core[:2], "density": core[2], "annulus": annulus,
            "prominence": prominence, "competing": len(mins), "min_sep": sep,
            "region": rmax}


# ---------------------------------------------------------------- estimators
def est_baseline(sl, xa, ya):
    """A (CONTROL): centroid of the valid +-1 disc."""
    hits, nv, nr = hit_set(sl, xa, ya, 2.0)
    if not hits:
        return {"core": None, "extent": None, "n": 0, "valid_loops": nv,
                "rejected_loops": nr, "coverage": "no_valid_hits"}
    a = np.array(hits)
    c = (float(a[:, 0].mean()), float(a[:, 1].mean()))
    return {"core": c, "extent": float(np.max(np.linalg.norm(a - c, axis=1))),
            "n": len(hits), "valid_loops": nv, "rejected_loops": nr, "coverage": "ok"}


def est_disc_intersection(sl, xa, ya):
    """B: continuous feasibility test on the true intersection of the +-1 discs.

    The vortex lies in every +-1 loop's disc, so it lies in the intersection.
    Feasibility and the feasible centroid are found by maximizing the minimum slack
    min_i (R_i - |p - c_i|) on an adaptive grid -- no fixed lattice, no clamping.
    """
    discs = []
    tot_v = tot_r = 0
    for R in RADII:
        h, nv, nr = hit_set(sl, xa, ya, R)
        discs += [(c[0], c[1], R) for c in h]
        tot_v += nv; tot_r += nr
    if not discs:
        return {"core": None, "extent": None, "n": 0, "area": 0,
                "valid_loops": tot_v, "rejected_loops": tot_r,
                "coverage": "no_valid_hits"}

    xs = np.array([d[0] for d in discs]); ys = np.array([d[1] for d in discs])
    Rmax = max(d[2] for d in discs)
    lo = np.array([xs.min() - Rmax, ys.min() - Rmax])
    hi = np.array([xs.max() + Rmax, ys.max() + Rmax])

    def slacks(p):
        return np.array([R - math.hypot(p[0]-cx, p[1]-cy) for cx, cy, R in discs])

    best, best_s = None, -1e18
    step = 0.25
    for _ in range(4):
        gx = np.arange(lo[0], hi[0] + 1e-9, step)
        gy = np.arange(lo[1], hi[1] + 1e-9, step)
        if len(gx) * len(gy) > 4_000_000:
            break
        X, Y = np.meshgrid(gx, gy, indexing="ij")
        S = np.full(X.shape, np.inf)
        for cx, cy, R in discs:
            S = np.minimum(S, R - np.hypot(X-cx, Y-cy))
        idx = np.unravel_index(np.argmax(S), S.shape)
        if S[idx] > best_s:
            best_s = float(S[idx]); best = (float(X[idx]), float(Y[idx]))
        span = step * 4
        lo = np.array([best[0] - span, best[1] - span])
        hi = np.array([best[0] + span, best[1] + span])
        step /= 4.0

    if best is None or best_s < 0:
        return {"core": None, "extent": None, "n": len(discs), "area": 0,
                "max_slack": best_s, "valid_loops": tot_v, "rejected_loops": tot_r,
                "coverage": "infeasible"}

    # feasible patch around the best point, for centroid/extent
    fine = np.arange(best[0] - 2*step*4, best[0] + 2*step*4 + 1e-9, step*4)
    finey = np.arange(best[1] - 2*step*4, best[1] + 2*step*4 + 1e-9, step*4)
    X, Y = np.meshgrid(fine, finey, indexing="ij")
    S = np.full(X.shape, np.inf)
    for cx, cy, R in discs:
        S = np.minimum(S, R - np.hypot(X-cx, Y-cy))
    m = S >= 0
    if not m.any():
        return {"core": None, "extent": None, "n": len(discs), "area": 0,
                "max_slack": best_s, "valid_loops": tot_v, "rejected_loops": tot_r,
                "coverage": "infeasible_patch"}
    px, py = X[m], Y[m]
    core = (float(px.mean()), float(py.mean()))
    return {"core": core, "extent": float(np.max(np.hypot(px-core[0], py-core[1]))),
            "n": len(discs), "area": int(m.sum()), "max_slack": best_s,
            "valid_loops": tot_v, "rejected_loops": tot_r, "coverage": "ok"}


def est_boundary_bisection(sl, xa, ya):
    """C: bisect the winding +1 -> 0 boundary along four axes.

    Repaired: the starting classification is verified, each direction must find a
    VALID loop of the opposite classification to bracket, invalid loops are
    rejected rather than clamped, and all four crossings are retained.
    """
    hits, nv, nr = hit_set(sl, xa, ya, 2.0)
    if not hits:
        return {"core": None, "extent": None, "n": 0, "valid_loops": nv,
                "rejected_loops": nr, "coverage": "no_valid_hits", "crossings": []}
    a = np.array(hits)
    start = (float(a[:, 0].mean()), float(a[:, 1].mean()))
    w0 = winding(sl, xa, ya, start[0], start[1], 2.0)
    if w0 is None or abs(w0) < 0.9:
        return {"core": None, "extent": None, "n": len(hits), "valid_loops": nv,
                "rejected_loops": nr, "coverage": "start_not_interior",
                "start_winding": w0, "crossings": []}

    crossings, diag = [], {}
    for name, dx, dy in (("xp", 1, 0), ("xn", -1, 0), ("yp", 0, 1), ("yn", 0, -1)):
        lo, hi, ok = 0.0, None, False
        t = 0.25
        while t <= 8.0:
            cx, cy = start[0] + dx*t, start[1] + dy*t
            if not loop_valid(xa, ya, cx, cy, 2.0):
                diag[name] = "domain_exit"
                break
            w = winding(sl, xa, ya, cx, cy, 2.0)
            if w is not None and abs(w) < 0.9:
                hi = t; ok = True
                break
            lo = t
            t += 0.25
        if not ok:
            diag[name] = "no_bracket"
            continue
        for _ in range(28):
            mid = 0.5*(lo + hi)
            cx, cy = start[0] + dx*mid, start[1] + dy*mid
            w = winding(sl, xa, ya, cx, cy, 2.0)
            if w is not None and abs(w) >= 0.9:
                lo = mid
            else:
                hi = mid
        crossings.append((start[0] + dx*0.5*(lo+hi), start[1] + dy*0.5*(lo+hi)))
        diag[name] = "ok"
    if len(crossings) < 4:
        return {"core": None, "extent": None, "n": len(hits), "valid_loops": nv,
                "rejected_loops": nr, "coverage": "partial_brackets",
                "start_winding": w0, "crossings": crossings, "directions": diag}
    c = np.array(crossings)
    core = (float(c[:, 0].mean()), float(c[:, 1].mean()))
    return {"core": core, "extent": float(np.max(np.linalg.norm(c - core, axis=1))),
            "n": len(hits), "valid_loops": nv, "rejected_loops": nr,
            "coverage": "ok", "start_winding": w0, "crossings": crossings,
            "directions": diag}


ESTIMATORS = {"baseline_centroid": est_baseline,
              "disc_intersection": est_disc_intersection,
              "boundary_bisection": est_boundary_bisection}
CONTROL = "baseline_centroid"


def sanitize(o):
    """Strict JSON: NaN/Inf -> None."""
    if isinstance(o, float):
        return None if (math.isnan(o) or math.isinf(o)) else o
    if isinstance(o, dict):
        return {k: sanitize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sanitize(v) for v in o]
    return o


def main():
    out = {"revision": 2, "status": "D3 remediation revision 2 -- NOT VALIDATED",
           "supersedes": "895bec2 (revision 1) -- preserved immutable",
           "geometry_fix": "out-of-domain loop samples rejected, never clamped",
           "control": CONTROL,
           "acceptance_criteria": {
               "bounded_error": 1.0, "refine_factor": 1.2, "agree": 0.5,
               "blind": 0.5, "unambiguous": "competing minima == 1",
               "note": "control excluded from the replacement PASS criterion"},
           "radii": list(RADII), "frames": list(FRAMES), "z_slices": list(Z_SLICES),
           "runs": []}
    for N in GRIDS:
        for dt in DTS:
            g = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
            X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
            rp = np.sqrt(X ** 2 + Y ** 2)
            psi = WaveFunction3D(g, rp * np.exp(-(rp ** 2 + Z ** 2) / (4*SIGMA**2))
                                 * np.exp(1j*np.arctan2(Y, X)))
            psi.normalize()
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
                        ref = reference(rho, g.x, g.y)
                        rec = {"slice_index": k, "reference": ref}
                        for name, fn in ESTIMATORS.items():
                            r = fn(sl, g.x, g.y)
                            if r.get("core") is not None and ref is not None:
                                r["err_vs_ref"] = round(math.dist(r["core"], ref["core"]), 4)
                            rec[name] = r
                        # diagnostic only: is the reference core inside B's intersection?
                        b = rec["disc_intersection"]
                        if b.get("core") is not None and ref is not None:
                            b["reference_inside_estimate"] = bool(
                                math.dist(b["core"], ref["core"]) <= (b.get("extent") or 0) + 1e-9)
                        if rec["disc_intersection"].get("core") is not None and \
                           rec["boundary_bisection"].get("core") is not None:
                            rec["B_vs_C"] = round(math.dist(
                                rec["disc_intersection"]["core"],
                                rec["boundary_bisection"]["core"]), 4)
                        fr["slices"][str(zv)] = rec
                        print(f" step {step:3d} z={zv:+.0f}: "
                              f"A={rec['baseline_centroid'].get('core')} "
                              f"B={rec['disc_intersection'].get('core')} "
                              f"C={rec['boundary_bisection'].get('core')} "
                              f"rejA={rec['baseline_centroid'].get('rejected_loops')} "
                              f"rejB={rec['disc_intersection'].get('rejected_loops')} "
                              f"errB={rec['disc_intersection'].get('err_vs_ref')} "
                              f"errC={rec['boundary_bisection'].get('err_vs_ref')}")
                    run["frames"].append(fr)
                if step < STEPS:
                    psi = solver.step(psi)
            out["runs"].append(run)

    print("\n===== BLIND DISPLACED PROFILES =====")
    blind = []
    for disp in [(1.5, -1.0), (-2.0, 1.5), (0.0, 2.5)]:
        g = Grid3D(48, BOX[0], BOX[1], 48, BOX[0], BOX[1], 48, BOX[0], BOX[1])
        X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
        dx_, dy_ = X-disp[0], Y-disp[1]
        rp = np.sqrt(dx_**2 + dy_**2)
        psi = WaveFunction3D(g, rp * np.exp(-(rp**2+Z**2)/(4*SIGMA**2))
                             * np.exp(1j*np.arctan2(dy_, dx_)))
        psi.normalize()
        k = int(np.abs(g.z).argmin()); sl = psi.psi[:, :, k]
        ref = reference(np.abs(sl)**2, g.x, g.y)
        row = {"true": list(disp), "reference": ref["core"] if ref else None}
        for name, fn in ESTIMATORS.items():
            r = fn(sl, g.x, g.y)
            row[name] = (None if r.get("core") is None else
                         {"core": [round(r["core"][0], 4), round(r["core"][1], 4)],
                          "error": round(math.dist(r["core"], disp), 4)})
        blind.append(row)
        print(f" true={disp} ref={row['reference']} A={row['baseline_centroid']} "
              f"B={row['disc_intersection']} C={row['boundary_bisection']}")
    out["blind_tests"] = blind

    p = IDX / "quantum_vortex_d3_remediation_v2.json"
    p.write_text(json.dumps(sanitize(out), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
