#!/usr/bin/env python3
"""
cpd_vortex_gate_derivation_2026-11-22.py

EXPERIMENT 2 (of 2): derive a diagnostic acceptance gate independently of the
revision-4 fixed radius tolerance.

Separate experiment; the circle-fitting estimator is NOT modified.

Motivation: revision 4's fixed |R_fit - 2.0| <= 0.35 gate let inaccurate estimates
through (2 ungated C5 failures, 4 ungated C6 degradations).  A low residual alone is
not evidence of a good centre: a SHORT ARC of a circle fits extremely well while
leaving the centre poorly constrained.  Angular coverage and conditioning must
therefore be part of the gate.

Procedure
  1. Assemble DEVELOPMENT observations (revision-4 dev profiles + the domain
     experiment at L = 6, 8, 12).
  2. For each, compute features: coverage, largest angular gap, n crossings,
     rms/max radial residual, fit condition number, and the CENTRE STANDARD ERROR
     from the Gauss-Newton parameter covariance  sigma^2 (J^T J)^-1.
  3. Relate features to true localisation error.
  4. Derive and FREEZE a gate (implementation + thresholds), recording its hash.
  5. Evaluate the frozen gate against a NEW reserved holdout.

The five revision-4 holdout displacements are NOT used here -- they are no longer
blind for gate development.
"""
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

AUD = Path(r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20")
IDX = AUD / "pks_research_index"
sys.path.insert(0, str(AUD))
sys.path.insert(0, str(Path(r"C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main")))

import importlib.util
_est = AUD / "cpd_vortex_d3_remediation_v4_2026-11-22.py"
_spec = importlib.util.spec_from_file_location("d3_rev4_frozen", _est)
rev4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rev4)
from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D

DX_TARGET = 12.0 / 64.0
DEV_PROFILES = list(rev4.DEV_PROFILES)
HOLDOUT_PROFILES = [(2.0, 2.0), (-2.0, -2.0), (1.0, -2.0), (-2.0, 1.0), (2.5, 0.25), (-0.5, 2.5)]

# --- frozen gate thresholds, chosen on development data only ---
GATE_MIN_COVERAGE = 0.90
GATE_MAX_GAP_DEG = 40.0
GATE_MAX_CENTRE_STD = 0.25


def build_at(N, displacement, L):
    g = Grid3D(N, -L, L, N, -L, L, N, -L, L)
    X, Y, Z = np.meshgrid(g.x, g.x, g.x, indexing="ij")
    dx_, dy_ = X - displacement[0], Y - displacement[1]
    rp = np.sqrt(dx_**2 + dy_**2)
    psi = WaveFunction3D(g, rp * np.exp(-(rp**2 + Z**2) / (4.0 * rev4.SIGMA**2))
                         * np.exp(1j*np.arctan2(dy_, dx_)))
    psi.normalize()
    return g, psi


def largest_gap(rows):
    ok = sorted(r_["angle_deg"] for r_ in rows if r_["reason"] == "ok")
    if len(ok) < 2:
        return None
    return int(max((ok[(i+1) % len(ok)] - ok[i]) % 360 for i in range(len(ok))))


def _valid_crossing_points(xa, ya, sl, R_LOOP):
    """Valid crossing loop centres from the frozen estimator's own rules."""
    step = max(1, int(round(1.0/(xa[1]-xa[0]))))
    out = []
    for j in range(len(xa)):
        for k in range(len(ya)):
            if (j % step) or (k % step):
                continue
            if not rev4.loop_valid(xa, ya, xa[j], ya[k], R_LOOP):
                continue
            if abs(rev4.winding(sl, xa, ya, xa[j], ya[k], R_LOOP)) >= 0.9:
                out.append((float(xa[j]), float(ya[k])))
    return out


def centre_std(xa, ya, sl, centre, radius):
    """Centre standard error from the Gauss-Newton parameter covariance."""
    pts = _valid_crossing_points(xa, ya, sl, rev4.R_LOOP)
    if len(pts) < 4:
        return None
    xc, yc, rr = float(centre[0]), float(centre[1]), float(radius)
    J = None
    for _ in range(60):
        xs = np.array([p[0] for p in pts]) - xc
        ys = np.array([p[1] for p in pts]) - yc
        d = np.hypot(xs, ys)
        if np.any(d == 0):
            return None
        res = d - rr
        J = np.column_stack([(-xs)/d, (-ys)/d, -np.ones(len(pts))])
        step, *_ = np.linalg.lstsq(J, res, rcond=None)
        xc += float(step[0]); yc += float(step[1]); rr += float(step[2])
        if float(np.linalg.norm(step)) < 1e-12:
            break
    sig2 = float(np.sum((d-rr)**2))/(len(pts)-3)
    try:
        cov = sig2*np.linalg.inv(J.T@J)
        return float(math.sqrt(max(cov[0,0]+cov[1,1], 0.0)))
    except np.linalg.LinAlgError:
        return None


def feature_from_analysis(rec, xa, ya, sl):
    out = {"valid": rec.get("angular_coverage") != "no_valid_hits",
           "coverage": rec.get("angular_coverage"),
           "largest_gap_deg": largest_gap(rec.get("crossings", [])),
           "n_crossings": rec.get("n_crossings"), "n_angles": rec.get("n_angles"),
           "domain_exits": rec.get("n_rejected_loops"),
           "rejected_loops": rec.get("n_rejected_loops")}
    cf = rec.get("circle_fit")
    if cf and len(rec.get("crossings", [])) >= 3:
        out.update({"R_fit": cf.get("radius"),
                    "rms_residual": cf.get("rms_residual"),
                    "max_residual": cf.get("max_residual"),
                    "condition": cf.get("condition"),
                    "centre": cf.get("centre")})
        std = centre_std(xa, ya, sl, cf["centre"], cf["radius"])
        if std is not None:
            out["centre_std"] = std
        err = rec.get("circle_error_vs_true")
        out["error_vs_true"] = None if err is None else round(err, 4)
        out["gate_accept"] = (rec.get("angular_coverage", 0) >= GATE_MIN_COVERAGE) and \
            (out["largest_gap_deg"] is not None and out["largest_gap_deg"] <= GATE_MAX_GAP_DEG) \
            and (out.get("centre_std") is not None and out["centre_std"] <= GATE_MAX_CENTRE_STD)
        out["ungated_fail"] = bool(out["gate_accept"] and out["error_vs_true"] is not None
                                   and out["error_vs_true"] > 1.0)
    else:
        out["valid"] = False
    return out


def sanitize(o):
    if isinstance(o, float):
        return None if (math.isnan(o) or math.isinf(o)) else o
    if isinstance(o, dict):
        return {k: sanitize(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sanitize(v) for v in o]
    return o


def collect(profiles, domains, tag):
    out = []
    for L in domains:
        N = max(8, int(round(2 * L / DX_TARGET)))
        for disp in profiles:
            g, psi = build_at(N, disp, L)
            k = int(np.abs(g.z).argmin())
            sl = psi.psi[:, :, k]
            rec = rev4.analyse(sl, g.x, g.y, np.abs(sl)**2, true_disp=disp)
            f = feature_from_analysis(rec, g.x, g.y, sl)
            f.update({"profile_set": tag, "L": L, "N": N, "dx": 2*L/N,
                      "displacement": list(disp)})
            out.append(f)
    return out


def main():
    est_hash = hashlib.sha256(Path(rev4.__file__).read_bytes()).hexdigest()
    gate_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("frozen estimator sha256:", est_hash[:24])
    print("gate implementation sha256:", gate_hash[:24])
    print("gate thresholds: coverage>=%.2f gap<=%.0f centre_std<=%.2f"
          % (GATE_MIN_COVERAGE, GATE_MAX_GAP_DEG, GATE_MAX_CENTRE_STD))

    dev = collect(DEV_PROFILES, (6.0, 8.0, 12.0), "development")
    print("\n=== DEVELOPMENT observations: %d ===" % len(dev))
    print("%5s %16s %6s %4s %7s %7s %7s %8s %5s" % (
        "L", "true", "cov", "gap", "rms", "cond", "cstd", "err", "gate"))
    for f in dev:
        print("%5.1f %16s %6.3f %4s %7s %7s %7s %8s %5s" % (
            f["L"], str(f["displacement"]),
            f.get("coverage", 0), str(f.get("largest_gap_deg")),
            ("None" if f.get("rms_residual") is None else "%.4f" % f["rms_residual"]),
            ("None" if f.get("condition") is None else "%.1f" % f["condition"]),
            ("None" if f.get("centre_std") is None else "%.4f" % f["centre_std"]),
            str(f.get("error_vs_true")), str(f.get("gate_accept"))))

    ok = [f for f in dev if f.get("valid")]
    bad = [f for f in ok if f["error_vs_true"] > 1.0]
    print("\nfeature vs error on development data:")
    for key in ("coverage", "largest_gap_deg", "rms_residual", "condition", "centre_std"):
        pairs = [(f[key], f["error_vs_true"]) for f in ok if f.get(key) is not None]
        if not pairs:
            continue
        xs = np.array([p[0] for p in pairs]); ys = np.array([p[1] for p in pairs])
        c = float(np.corrcoef(xs, ys)[0, 1]) if len(xs) > 2 and xs.std() > 0 else float("nan")
        print("  %-16s n=%3d corr_with_error=%+.4f" % (key, len(pairs), c))
    print("  bad (err>1.0): %d" % len(bad))
    for f in bad:
        print("    L=%.1f true=%s cov=%s gap=%s cstd=%s err=%s"
              % (f["L"], str(f["displacement"]), f.get("coverage"),
                 f.get("largest_gap_deg"), f.get("centre_std"), f["error_vs_true"]))

    print("\n=== RESERVED HOLDOUT (frozen gate) ===")
    hold = collect(HOLDOUT_PROFILES, (6.0, 8.0, 12.0), "holdout")
    n_pass = n_rej = n_ungated = 0
    for f in hold:
        if not f.get("valid"):
            n_rej += 1
            print("  true=%s L=%.1f: no fit" % (str(f["displacement"]), f["L"]))
            continue
        good = f["gate_accept"] and f["error_vs_true"] <= 1.0
        if f["gate_accept"] and f["error_vs_true"] > 1.0:
            n_ungated += 1
        elif f["gate_accept"]:
            n_pass += 1
        else:
            n_rej += 1
        print("  true=%s L=%.1f: cov=%.3f gap=%s cstd=%s err=%s gate=%s %s"
              % (str(f["displacement"]), f["L"], f.get("coverage"),
                 f.get("largest_gap_deg"), f.get("centre_std"),
                 f.get("error_vs_true"), "P" if f["gate_accept"] else "F",
                 ("UNGATED FAIL" if (f["gate_accept"] and f["error_vs_true"] > 1.0)
                  else ("pass" if f["gate_accept"] else "rejected"))))
    print("\nholdout: pass=%d rejected=%d UNGATED=%d" % (n_pass, n_rej, n_ungated))

    out = {"experiment": "independent diagnostic gate derivation",
           "status": "DIAGNOSTIC -- gate frozen before holdout evaluation",
           "frozen_estimator_sha256": est_hash,
           "gate_implementation_sha256": gate_hash,
           "gate_thresholds": {"min_coverage": GATE_MIN_COVERAGE,
                               "max_gap_deg": GATE_MAX_GAP_DEG,
                               "max_centre_std": GATE_MAX_CENTRE_STD},
           "derivation_data": "development profiles at L=6,8,12 only",
           "holdout_profiles": [list(p) for p in HOLDOUT_PROFILES],
           "development": dev, "holdout": hold,
           "holdout_summary": {"pass": n_pass, "rejected": n_rej, "ungated": n_ungated}}
    p = IDX / "quantum_vortex_gate_derivation.json"
    p.write_text(json.dumps(sanitize(out), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
