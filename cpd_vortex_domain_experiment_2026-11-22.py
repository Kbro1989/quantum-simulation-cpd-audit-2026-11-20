#!/usr/bin/env python3
"""
cpd_vortex_domain_experiment_2026-11-22.py

EXPERIMENT 1 (of 2): does a larger computational domain recover the missing angular
information?  Separate experiment; the circle-fitting estimator is NOT modified.

Frozen (per instruction):
  * revision 4 estimator -- IMPORTED, not copied, so it cannot drift
    (SHA-256 0b108d82e7ad83b0...)
  * loop radius R = 2.0
  * circle-fitting implementation and fitting procedure
  * acceptance criteria and the revision-4 holdout results

Varied: ONLY the computational domain.  Grid spacing dx is held at the revision-4
value (0.1875) by scaling N with the box, so the domain is the single independent
variable.

Measured per (domain, profile):
  valid angular coverage, largest missing angular sector, accepted crossings,
  circle-fit rms/max residual and condition number, centre error vs the true
  displacement, domain-exit and rejected-crossing counts.
"""
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
IDX = AUD / "pks_research_index"
sys.path.insert(0, str(AUD))
sys.path.insert(0, str(Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")))

import importlib.util
_est = AUD / "cpd_vortex_d3_remediation_v4_2026-11-22.py"
_spec = importlib.util.spec_from_file_location("d3_rev4_frozen", _est)
rev4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rev4)
from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D

DX_TARGET = 12.0 / 64.0          # revision-4 dx at N=64, box (-6, 6)
DOMAINS = (6.0, 8.0, 12.0)       # half-width L
DEV_PROFILES = list(rev4.DEV_PROFILES)


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
    gaps = [(ok[(i+1) % len(ok)] - ok[i]) % 360 for i in range(len(ok))]
    return int(max(gaps))


def main():
    est_hash = hashlib.sha256(Path(rev4.__file__).read_bytes()).hexdigest()
    print("imported estimator:", Path(rev4.__file__).name)
    print("estimator SHA-256:", est_hash[:24])
    print("dx target:", DX_TARGET)

    out = {"experiment": "domain enlargement", "status": "DIAGNOSTIC -- not an acceptance run",
           "frozen_estimator_sha256": est_hash, "loop_radius": rev4.R_LOOP,
           "dx_target": DX_TARGET, "domains": list(DOMAINS),
           "varied": "computational domain half-width L only; dx held constant",
           "runs": []}
    print(f"\n{'L':>5s} {'N':>4s} {'dx':>8s} {'true':>16s} {'cov':>6s} {'gap':>4s} "
          f"{'n':>3s} {'rms':>7s} {'maxres':>7s} {'cond':>8s} {'err':>8s} "
          f"{'exit':>5s} {'rej':>4s}")
    for L in DOMAINS:
        N = max(8, int(round(2 * L / DX_TARGET)))
        dx = 2 * L / N
        for disp in DEV_PROFILES:
            g, psi = build_at(N, disp, L)
            k = int(np.abs(g.z).argmin())
            sl = psi.psi[:, :, k]
            r = rev4.analyse(sl, g.x, g.y, np.abs(sl)**2, true_disp=disp)
            cf = r.get("circle_fit") or {}
            exits = sum(1 for c in r.get("crossings", []) if c["reason"] == "domain_exit")
            row = {"L": L, "N": N, "dx": dx, "displacement": list(disp),
                   "angular_coverage": r.get("angular_coverage"),
                   "largest_missing_sector_deg": largest_gap(r.get("crossings", [])),
                   "n_crossings": r.get("n_crossings"), "n_angles": r.get("n_angles"),
                   "rms_residual": cf.get("rms_residual"),
                   "max_residual": cf.get("max_residual"),
                   "condition": cf.get("condition"),
                   "R_fit": cf.get("radius"),
                   "error_vs_true": r.get("circle_error_vs_true"),
                   "domain_exits": exits,
                   "rejected_loops": r.get("n_rejected_loops")}
            out["runs"].append(row)
            print(f"{L:5.1f} {N:4d} {dx:8.4f} {str(disp):>16s} "
                  f"{r.get('angular_coverage', 0):6.3f} {str(row['largest_missing_sector_deg']):>4s} "
                  f"{r.get('n_crossings', 0):3d} "
                  f"{('None' if cf.get('rms_residual') is None else '%.4f' % cf['rms_residual']):>7s} "
                  f"{('None' if cf.get('max_residual') is None else '%.4f' % cf['max_residual']):>7s} "
                  f"{('None' if cf.get('condition') is None else '%.1f' % cf['condition']):>8s} "
                  f"{('None' if r.get('circle_error_vs_true') is None else '%.4f' % r['circle_error_vs_true']):>8s} "
                  f"{exits:5d} {r.get('n_rejected_loops', 0):4d}")

    p = IDX / "quantum_vortex_domain_experiment.json"
    p.write_text(json.dumps(rev4.sanitize(out), indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
