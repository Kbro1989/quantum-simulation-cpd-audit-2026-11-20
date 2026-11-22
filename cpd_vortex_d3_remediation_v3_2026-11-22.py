#!/usr/bin/env python3
"""
cpd_vortex_d3_remediation_v3_2026-11-22.py

D3 REMEDIATION REVISION 3 -- diagnostics and directional assumption.  NOT VALIDATED.

Preserved immutable: b7b3391 (Gate 1), 895bec2 (revision 1), d259430 (revision 2).

Revision 2 kept the estimators but lost the bisection failure diagnostics: a
`domain_exit` reason was overwritten by `no_bracket`, so the actual termination
cause per direction was unrecoverable.  This revision:

  1. preserves the real termination reason for every direction;
  2. stores the complete bisection result per blind profile -- coverage,
     start_winding, directions, all crossings, per-direction terminal reason,
     last valid radius and last observed winding;
  3. distinguishes start_not_interior / domain_exit / no_opposite_winding /
     refinement_failed;
  4. re-runs the SAME three displaced profiles (parameters unchanged) as the
     revision-2 comparison baseline;
  5. identifies the failing direction(s) per profile without inferring a cause
     from the missing core.

Priority 2 -- the directional assumption:
  6. compares the centroid seed against a verified-interior-hit seed;
  7. adds a diagnostic angular scan around the verified interior seed (diagnostic
     evidence only -- it does NOT silently replace the estimator);
  8. keeps the original four-direction results as the revision-2 baseline.

Blind-profile discipline: the original three displacements have been inspected, so
they are no longer independent validation.  They are kept as a COMPARISON baseline,
and a fresh set of four displacements is reserved for independent blind validation.
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

BOX = (-6.0, 6.0)
HBAR, MASS, SIGMA = 1.0, 1.0, 1.0
RADII = (2.0, 3.0)
DIRECTIONS = (("xp", 1, 0), ("xn", -1, 0), ("yp", 0, 1), ("yn", 0, -1))

# revision-2 comparison set (parameters unchanged)
BASELINE_PROFILES = [(1.5, -1.0), (-2.0, 1.5), (0.0, 2.5)]
# fresh independent validation set -- never inspected during estimator development
FRESH_PROFILES = [(2.25, 0.75), (-1.25, -2.25), (0.75, -2.75), (-2.75, -0.75)]


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


def hit_set(sl, xa, ya, radius, spacing=1.0):
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
    return {"core": core[:2], "density": core[2], "annulus": annulus,
            "prominence": ((annulus - core[2]) / annulus) if (annulus and annulus > 0) else None,
            "competing": len(mins), "region": rmax}


# ---------------------------------------------------------------- bisection
def bisect(sl, xa, ya, start, r=2.0, tmax=8.0, dt=0.25):
    """Four-direction boundary bisection with full per-direction diagnostics."""
    w0 = winding(sl, xa, ya, start[0], start[1], r)
    out = {"start": [start[0], start[1]], "start_winding": w0,
           "start_classified_interior": (w0 is not None and abs(w0) >= 0.9),
           "crossings": [], "directions": {}}

    if w0 is None:
        out["coverage"] = "start_not_interior"
        out["termination"] = "start loop outside valid domain"
        return out
    if abs(w0) < 0.9:
        out["coverage"] = "start_not_interior"
        out["termination"] = "start loop not +-1 (winding=%.4f)" % w0
        return out

    for name, dx, dy in DIRECTIONS:
        lo, hi = 0.0, None
        last_t, last_w = 0.0, w0
        reason, t = None, dt
        while t <= tmax:
            cx, cy = start[0] + dx*t, start[1] + dy*t
            if not loop_valid(xa, ya, cx, cy, r):
                reason = "domain_exit"
                break
            w = winding(sl, xa, ya, cx, cy, r)
            if w is None:
                reason = "domain_exit"
                break
            last_t, last_w = t, w
            if abs(w) < 0.9:
                hi = t
                break
            lo = t
            t += dt
        if reason is None and hi is None:
            reason = "no_opposite_winding"
        if reason is not None:
            out["directions"][name] = {"reason": reason, "last_valid_radius": last_t,
                                       "last_winding": last_w}
            continue
        for _ in range(28):
            mid = 0.5*(lo + hi)
            cx, cy = start[0] + dx*mid, start[1] + dy*mid
            w = winding(sl, xa, ya, cx, cy, r)
            if w is None:
                out["directions"][name] = {"reason": "refinement_failed",
                                           "last_valid_radius": lo, "last_winding": None}
                break
            if abs(w) >= 0.9:
                lo = mid
            else:
                hi = mid
        else:
            out["crossings"].append((start[0] + dx*0.5*(lo+hi), start[1] + dy*0.5*(lo+hi)))
            out["directions"][name] = {"reason": "ok", "last_valid_radius": 0.5*(lo+hi),
                                       "last_winding": None}
            continue
        if name not in out["directions"]:
            out["directions"][name] = {"reason": "refinement_failed",
                                       "last_valid_radius": lo, "last_winding": None}

    out["coverage"] = "ok" if len(out["crossings"]) == 4 else "partial_brackets"
    if len(out["crossings"]) == 4:
        c = np.array(out["crossings"])
        core = (float(c[:, 0].mean()), float(c[:, 1].mean()))
        out["core"] = core
        out["extent"] = float(np.max(np.linalg.norm(c - core, axis=1)))
    else:
        out["core"] = None
        out["extent"] = None
    return out


def angular_scan(sl, xa, ya, seed, r=2.0, step_deg=10, tmax=8.0, dt=0.25):
    """Diagnostic only: crossing radius as a function of angle around the seed."""
    rows = []
    for deg in range(0, 360, step_deg):
        a = math.radians(deg)
        dx, dy = math.cos(a), math.sin(a)
        lo, hi = 0.0, None
        t = dt
        while t <= tmax:
            cx, cy = seed[0] + dx*t, seed[1] + dy*t
            if not loop_valid(xa, ya, cx, cy, r):
                break
            w = winding(sl, xa, ya, cx, cy, r)
            if w is not None and abs(w) < 0.9:
                hi = t
                break
            lo = t
            t += dt
        rows.append({"angle_deg": deg,
                     "crossing_radius": (None if hi is None else 0.5*(lo+hi)),
                     "reason": ("ok" if hi is not None else
                                ("domain_exit" if not loop_valid(xa, ya, seed[0]+dx*t, seed[1]+dy*t, r)
                                 else "no_opposite_winding"))})
    ok = [r_["crossing_radius"] for r_ in rows if r_["crossing_radius"] is not None]
    return {"seed": [seed[0], seed[1]], "angles": rows,
            "n_ok": len(ok), "min_radius": (min(ok) if ok else None),
            "max_radius": (max(ok) if ok else None),
            "mean_radius": (float(np.mean(ok)) if ok else None)}


def sanitize(o):
    if isinstance(o, float):
        return None if (math.isnan(o) or math.isinf(o)) else o
    if isinstance(o, dict):
        return {k: sanitize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sanitize(v) for v in o]
    return o


def build(N, displacement):
    g = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
    dx_, dy_ = X - displacement[0], Y - displacement[1]
    rp = np.sqrt(dx_**2 + dy_**2)
    psi = WaveFunction3D(g, rp * np.exp(-(rp**2 + Z**2) / (4*SIGMA**2))
                         * np.exp(1j*np.arctan2(dy_, dx_)))
    psi.normalize()
    return g, psi


def analyse_profile(disp, N=48, label=""):
    g, psi = build(N, disp)
    k = int(np.abs(g.z).argmin())
    sl = psi.psi[:, :, k]
    rho = np.abs(sl) ** 2
    ref = reference(rho, g.x, g.y)
    hits, nv, nr = hit_set(sl, g.x, g.y, 2.0)
    a = np.array(hits) if hits else None
    centroid_seed = (float(a[:, 0].mean()), float(a[:, 1].mean())) if a is not None else None
    # verified-interior-hit seed: a valid hit whose own winding is +-1
    hit_seed = hits[0] if hits else None

    rec = {"label": label, "displacement": list(disp), "grid_N": N,
           "reference_core": ref["core"] if ref else None,
           "n_valid_loops": nv, "n_rejected_loops": nr, "n_hits": len(hits)}
    for seed_name, seed in (("centroid_seed", centroid_seed), ("verified_hit_seed", hit_seed)):
        if seed is None:
            rec[seed_name] = None
            continue
        b = bisect(sl, g.x, g.y, seed)
        b["seed"] = [seed[0], seed[1]]
        if b.get("core") is not None:
            b["error_vs_true"] = round(math.dist(b["core"], disp), 4)
            if ref:
                b["error_vs_ref"] = round(math.dist(b["core"], ref["core"]), 4)
        rec[seed_name] = b
        rec[seed_name + "_angular_scan"] = angular_scan(sl, g.x, g.y, seed)
    return rec


def main():
    out = {"revision": 3, "status": "D3 remediation revision 3 -- NOT VALIDATED",
           "preserved": ["b7b3391 (Gate 1)", "895bec2 (revision 1)", "d259430 (revision 2)"],
           "bisection_termination_reasons":
               ["start_not_interior", "domain_exit", "no_opposite_winding", "refinement_failed"],
           "blind_profile_discipline":
               "the original three displacements were inspected during development and are "
               "retained as a COMPARISON baseline only; four fresh displacements are "
               "reserved for independent blind validation",
           "baseline_profiles": list(BASELINE_PROFILES),
           "fresh_profiles": list(FRESH_PROFILES),
           "baseline_comparison": [], "fresh_validation": []}

    print("=== BASELINE COMPARISON (revision-2 profiles, parameters unchanged) ===")
    for disp in BASELINE_PROFILES:
        r = analyse_profile(disp, label="baseline")
        out["baseline_comparison"].append(r)
        for seed_name in ("centroid_seed", "verified_hit_seed"):
            b = r.get(seed_name)
            if b:
                print(f" true={disp} {seed_name}: coverage={b.get('coverage')} "
                      f"core={b.get('core')} err_true={b.get('error_vs_true')}")
                print(f"    directions={ {k: v['reason'] for k, v in b['directions'].items()} }")

    print("\n=== FRESH INDEPENDENT VALIDATION ===")
    for disp in FRESH_PROFILES:
        r = analyse_profile(disp, label="fresh")
        out["fresh_validation"].append(r)
        for seed_name in ("centroid_seed", "verified_hit_seed"):
            b = r.get(seed_name)
            if b:
                print(f" true={disp} {seed_name}: coverage={b.get('coverage')} "
                      f"core={b.get('core')} err_true={b.get('error_vs_true')}")
                print(f"    directions={ {k: v['reason'] for k, v in b['directions'].items()} }")

    p = IDX / "quantum_vortex_d3_remediation_v3.json"
    p.write_text(json.dumps(sanitize(out), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
