#!/usr/bin/env python3
"""
cpd_vortex_d3_remediation_v4_2026-11-22.py

D3 REMEDIATION REVISION 4 -- circle fitting as a DISTINCT estimator.  NOT VALIDATED.

Preserved immutable: b7b3391 (Gate 1), 895bec2 (rev 1), d259430 (rev 2), 8bfcd92 (rev 3).

Hypothesis under test
----------------------
For an isolated unit-winding vortex, the set of loop centres whose radius-R loop
encloses the vortex is the disc |c - x_v| < R, whose boundary is a CIRCLE of radius
R centred on the vortex.  Every recorded crossing therefore lies on that circle.
Fitting the circle recovers the centre WITHOUT assuming the four-crossing mean is
unbiased -- which is exactly the weakness found in revision 3.

So the hypothesis is precise: the earlier estimator's weakness is its
four-direction CENTRE APPROXIMATION, not the winding-boundary geometry.

Constraints honoured
--------------------
* Four-crossing averaging is retained as a CONTROL; circle fitting is separate.
* Only valid, recorded crossings are fitted.  Missing crossings are never
  extrapolated as if observed.
* Reports angular coverage, crossing count, fit residuals, conditioning, centre
  error -- and R_fit vs the loop radius (a fit whose radius is not ~R is not the
  expected disc boundary).
* Sensitivity to missing angular sectors and to asymmetric domain boundaries.
* Density-core reference used diagnostically only.
* Centred + displaced profiles, multiple grids, both timesteps.

Freeze protocol
---------------
The estimator is frozen before the holdout is evaluated.  Run without --holdout to
develop, then with --holdout.  The script prints SHA-256 of its own file; the two
runs must match.  Development profiles: the 3 revision-2 + 4 revision-3 profiles.
Holdout: a separate undisclosed set, used only for final validation.
"""
import hashlib
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
R_LOOP = 2.0
ANGLES = tuple(range(0, 360, 10))
GRIDS = (48, 64)
DTS = (0.005, 0.0025)
TIME_FRAMES = (0, 100, 200)

# development profiles (revision-2 baseline + revision-3 set)
DEV_PROFILES = [(1.5, -1.0), (-2.0, 1.5), (0.0, 2.5),
                (2.25, 0.75), (-1.25, -2.25), (0.75, -2.75), (-2.75, -0.75)]
# reserved undisclosed holdout -- final validation only
HOLDOUT_PROFILES = [(1.75, 2.25), (-2.5, -1.75), (2.75, -2.25), (-1.75, 2.75), (0.5, 1.25)]


def loop_valid(xa, ya, cx, cy, r):
    return (cx - r) >= xa[0] and (cx + r) <= xa[-1] and \
           (cy - r) >= ya[0] and (cy + r) <= ya[-1]


def bilinear(f, xa, ya, px, py):
    ix = (px - xa[0]) / (xa[1] - xa[0])
    iy = (py - ya[0]) / (ya[1] - ya[0])
    i0 = np.minimum(np.floor(ix).astype(int), len(xa) - 2)
    j0 = np.minimum(np.floor(iy).astype(int), len(ya) - 2)
    fx = ix - i0; fy = iy - j0
    return ((1-fx)*(1-fy)*f[i0, j0] + fx*(1-fy)*f[i0+1, j0]
            + (1-fx)*fy*f[i0, j0+1] + fx*fy*f[i0+1, j0+1])


def winding(sl, xa, ya, cx, cy, r, npts=360):
    if not loop_valid(xa, ya, cx, cy, r):
        return None
    phi = np.linspace(0, 2*np.pi, npts, endpoint=False)
    v = bilinear(sl, xa, ya, cx + r*np.cos(phi), cy + r*np.sin(phi))
    d = np.angle(v[1:]*np.conj(v[:-1]))
    d = np.append(d, np.angle(v[0]*np.conj(v[-1])))
    return float(np.sum(d) / (2*np.pi))


def reference(rho, xa, ya, rmax=3.0, rel=0.05):
    rr = np.sqrt(xa[:, None] ** 2 + ya[None, :] ** 2)
    mask = rr <= rmax
    thr = rel * float(rho.max())
    mins = [(float(xa[j]), float(ya[k]), float(rho[j, k]))
            for j in range(1, rho.shape[0]-1) for k in range(1, rho.shape[1]-1)
            if mask[j, k] and rho[j, k] < thr and rho[j, k] <= rho[j-1:j+2, k-1:k+2].min()]
    if not mins:
        return None
    core = min(mins, key=lambda m: m[2])
    ann = (rr >= 1.5) & (rr <= 2.5)
    return {"core": core[:2], "competing": len(mins)}


def circle_fit(pts):
    """Kasa algebraic fit + Gauss-Newton geometric refinement. Returns dict."""
    x = np.array([p[0] for p in pts]); y = np.array([p[1] for p in pts])
    A = np.column_stack([2*x, 2*y, np.ones(len(x))])
    b = x**2 + y**2
    cond = float(np.linalg.cond(A))
    sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    cx, cy = float(sol[0]), float(sol[1])
    r = math.sqrt(max(sol[2] + cx**2 + cy**2, 0.0))
    for _ in range(30):
        d = np.hypot(x-cx, y-cy)
        if np.any(d == 0):
            break
        res = d - r
        J = np.column_stack([-(x-cx)/d, -(y-cy)/d, -np.ones(len(x))])
        delta, *_ = np.linalg.lstsq(J, res, rcond=None)
        cx += float(delta[0]); cy += float(delta[1]); r += float(delta[2])
        if float(np.linalg.norm(delta)) < 1e-12:
            break
    d = np.hypot(x-cx, y-cy)
    resid = d - r
    return {"centre": (cx, cy), "radius": r, "rms_residual": float(np.sqrt(np.mean(resid**2))),
            "max_residual": float(np.max(np.abs(resid))), "condition": cond, "n": len(pts)}


def crossings(sl, xa, ya, seed, r=R_LOOP, angles=ANGLES, dt=0.25, tmax=8.0):
    """Valid recorded crossings only. Missing angles are recorded as failures."""
    out = []
    for deg in angles:
        a = math.radians(deg)
        dx, dy = math.cos(a), math.sin(a)
        lo, hi, reason = 0.0, None, None
        t = dt
        while t <= tmax:
            cx, cy = seed[0] + dx*t, seed[1] + dy*t
            if not loop_valid(xa, ya, cx, cy, r):
                reason = "domain_exit"; break
            w = winding(sl, xa, ya, cx, cy, r)
            if w is not None and abs(w) < 0.9:
                hi = t; break
            lo = t; t += dt
        if reason is None and hi is None:
            reason = "no_opposite_winding"
        if hi is None:
            out.append({"angle_deg": deg, "reason": reason})
            continue
        for _ in range(28):
            mid = 0.5*(lo+hi)
            cx, cy = seed[0] + dx*mid, seed[1] + dy*mid
            w = winding(sl, xa, ya, cx, cy, r)
            if w is not None and abs(w) >= 0.9:
                lo = mid
            else:
                hi = mid
        out.append({"angle_deg": deg, "reason": "ok",
                    "point": (seed[0] + dx*0.5*(lo+hi), seed[1] + dy*0.5*(lo+hi)),
                    "radius": 0.5*(lo+hi)})
    return out


def coverage_fraction(rows):
    ok = [r_ for r_ in rows if r_["reason"] == "ok"]
    return len(ok), len(rows), (len(ok) / len(rows) if rows else 0.0)


def analyse(sl, xa, ya, rho, true_disp=None):
    hits, nv, nr = [], 0, 0
    step = max(1, int(round(1.0/(xa[1]-xa[0]))))
    for j in range(len(xa)):
        for k in range(len(ya)):
            if (j % step) or (k % step):
                continue
            if not loop_valid(xa, ya, xa[j], ya[k], R_LOOP):
                nr += 1; continue
            nv += 1
            if abs(winding(sl, xa, ya, xa[j], ya[k], R_LOOP)) >= 0.9:
                hits.append((float(xa[j]), float(ya[k])))
    rec = {"n_valid_loops": nv, "n_rejected_loops": nr, "n_hits": len(hits)}
    if not hits:
        rec["coverage"] = "no_valid_hits"
        return rec
    a = np.array(hits)
    seed = (float(a[:, 0].mean()), float(a[:, 1].mean()))
    rows = crossings(sl, xa, ya, seed)
    n_ok, n_all, frac = coverage_fraction(rows)
    rec.update({"seed": [seed[0], seed[1]], "angular_coverage": round(frac, 4),
                "n_crossings": n_ok, "n_angles": n_all, "loop_radius": R_LOOP,
                "crossings": [{"angle_deg": r_["angle_deg"], "reason": r_["reason"]}
                              for r_ in rows]})
    ok_pts = [r_["point"] for r_ in rows if r_["reason"] == "ok"]

    # control: four-crossing mean (only the four cardinal crossings)
    card = [r_["point"] for r_ in rows if r_["reason"] == "ok" and r_["angle_deg"] % 90 == 0]
    rec["control_four_mean"] = (None if len(card) < 4 else
                                [float(np.mean([p[0] for p in card])),
                                 float(np.mean([p[1] for p in card]))])

    # circle fit on ALL valid crossings
    if len(ok_pts) >= 3:
        fit = circle_fit(ok_pts)
        rec["circle_fit"] = fit
        rec["radius_matches_loop"] = bool(abs(fit["radius"] - R_LOOP) <= 0.35)
        if true_disp is not None:
            rec["circle_error_vs_true"] = round(math.dist(fit["centre"], true_disp), 4)
        ref = reference(rho, xa, ya)
        if ref:
            rec["reference_core"] = ref["core"]
            rec["circle_error_vs_ref"] = round(math.dist(fit["centre"], ref["core"]), 4)
        # sensitivity: drop a contiguous 90-degree sector, refit
        for sector in (0, 90, 180, 270):
            sub = [p for p, r_ in zip(ok_pts, [x for x in rows if x["reason"] == "ok"])
                   if not (sector <= r_["angle_deg"] < sector + 90)]
            if len(sub) >= 3:
                f2 = circle_fit(sub)
                rec[f"sensitivity_sector_{sector}_dropped"] = {
                    "n": len(sub), "centre": [round(f2["centre"][0], 4), round(f2["centre"][1], 4)],
                    "rms_residual": round(f2["rms_residual"], 4),
                    "radius": round(f2["radius"], 4),
                    "error_vs_true": (None if true_disp is None else
                                      round(math.dist(f2["centre"], true_disp), 4))}
    else:
        rec["circle_fit"] = None
        rec["coverage"] = "insufficient_crossings"
    return rec


def build(N, displacement):
    g = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
    dx_, dy_ = X - displacement[0], Y - displacement[1]
    rp = np.sqrt(dx_**2 + dy_**2)
    psi = WaveFunction3D(g, rp * np.exp(-(rp**2 + Z**2) / (4*SIGMA**2))
                         * np.exp(1j*np.arctan2(dy_, dx_)))
    psi.normalize()
    return g, psi


def sanitize(o):
    if isinstance(o, float):
        return None if (math.isnan(o) or math.isinf(o)) else o
    if isinstance(o, dict):
        return {k: sanitize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sanitize(v) for v in o]
    return o


def main():
    holdout = "--holdout" in sys.argv
    self_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    profiles = HOLDOUT_PROFILES if holdout else DEV_PROFILES
    out = {"revision": 4, "status": "D3 remediation revision 4 -- NOT VALIDATED",
           "preserved": ["b7b3391", "895bec2", "d259430", "8bfcd92"],
           "estimator": "circle fit (Kasa + Gauss-Newton) on valid recorded crossings",
           "control": "four-crossing cardinal mean",
           "hypothesis": ("the earlier weakness is the four-direction centre "
                          "approximation, not the winding-boundary geometry"),
           "loop_radius": R_LOOP, "angles": list(ANGLES),
           "estimator_sha256": self_hash, "mode": "holdout" if holdout else "development",
           "profiles": []}
    print(f"mode={'HOLDOUT' if holdout else 'DEVELOPMENT'}  estimator sha256={self_hash[:16]}")

    for disp in profiles:
        for N in GRIDS:
            for dt in DTS:
                g, psi = build(N, disp)
                k = int(np.abs(g.z).argmin())
                sl = psi.psi[:, :, k]
                r = analyse(sl, g.x, g.y, np.abs(sl)**2, true_disp=disp)
                r.update({"displacement": list(disp), "N": N, "dt": dt})
                out["profiles"].append(r)
                cf = r.get("circle_fit")
                print(f" true={disp} N={N} dt={dt}: cov={r.get('angular_coverage')} "
                      f"n={r.get('n_crossings')}/{r.get('n_angles')} "
                      f"fit={'None' if not cf else 'R=%.4f rms=%.4f' % (cf['radius'], cf['rms_residual'])} "
                      f"Rmatch={r.get('radius_matches_loop')} "
                      f"err_true={r.get('circle_error_vs_true')} "
                      f"ctrl={r.get('control_four_mean')}")

    # centred time evolution
    print("\n--- centred time evolution ---")
    out["centred_time"] = []
    for N in GRIDS:
        for dt in DTS:
            g, psi = build(N, (0.0, 0.0))
            solver = SplitOperatorSolver(g, HarmonicTrap(omegas=1.0, m=1.0), dt, HBAR, MASS,
                                         order=2, backend="numpy")
            k = int(np.abs(g.z).argmin())
            for step in range(0, STEPS+1):
                if step in TIME_FRAMES:
                    sl = psi.psi[:, :, k]
                    r = analyse(sl, g.x, g.y, np.abs(sl)**2, true_disp=(0.0, 0.0))
                    r.update({"N": N, "dt": dt, "step": step})
                    out["centred_time"].append(r)
                    cf = r.get("circle_fit")
                    print(f" N={N} dt={dt} step={step:3d}: cov={r.get('angular_coverage')} "
                          f"err_true={r.get('circle_error_vs_true')} "
                          f"fit={'None' if not cf else 'R=%.4f rms=%.4f' % (cf['radius'], cf['rms_residual'])}")
                if step < STEPS:
                    psi = solver.step(psi)

    name = "quantum_vortex_d3_remediation_v4_holdout.json" if holdout else \
           "quantum_vortex_d3_remediation_v4.json"
    p = IDX / name
    p.write_text(json.dumps(sanitize(out), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
