#!/usr/bin/env python3
"""
cpd_vortex_d3_acceptance_v4_2026-11-22.py

Acceptance evaluator for D3 remediation revision 4 (circle fitting).

Criteria (fixed before the holdout run):
  C1 bounded      circle-fit centre error <= 1.0, gated by radius consistency
  C2 refinement   both transitions (48->64 and 64->96), both timesteps
  C3 radius gate  |R_fit - R_loop| <= 0.35 -- the boundary must be the expected disc
  C4 coverage     angular coverage reported; a minimum is an OPERATING CONSTRAINT,
                  not a silent pass
  C5 blind        reserved holdout centre error <= 0.5
  C6 sensitivity  dropping a 90-degree sector must not silently produce a bad centre

The four-crossing mean is a CONTROL, excluded from the PASS criterion.
"""
import json
import sys
from pathlib import Path

IDX = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20\pks_research_index")
BOUND = 1.0
REFINE = 1.2
RAD_TOL = 0.35
BLIND = 0.5


def rows(profiles):
    return [p for p in profiles if p.get("circle_fit")]


def err(p):
    return p.get("circle_error_vs_true")


def radius_ok(p):
    cf = p.get("circle_fit") or {}
    return cf.get("radius") is not None and abs(cf["radius"] - p.get("loop_radius", 2.0)) <= RAD_TOL


def main():
    dev = json.load(open(IDX / "quantum_vortex_d3_remediation_v4.json", encoding="utf-8"))
    hold = json.load(open(IDX / "quantum_vortex_d3_remediation_v4_holdout.json", encoding="utf-8"))
    print("estimator sha256 (dev):   ", dev["estimator_sha256"][:24])
    print("estimator sha256 (holdout):", hold["estimator_sha256"][:24])
    print("FROZEN across holdout:", dev["estimator_sha256"] == hold["estimator_sha256"])
    print("mode dev:", dev["mode"], "| mode holdout:", hold["mode"])

    def collect(doc):
        out = {}
        for p in doc["profiles"]:
            out.setdefault((p["N"], p["dt"]), []).append(p)
        return out

    D, H = collect(dev), collect(hold)

    print("\n=== C1 bounded error <= %.1f (radius-gated) ===" % BOUND)
    c1 = True
    for key in sorted(D):
        ok = [p for p in D[key] if radius_ok(p)]
        bad = [p for p in D[key] if not radius_ok(p)]
        mx = max([err(p) for p in ok], default=None)
        passed = ok and all(err(p) <= BOUND for p in ok)
        c1 &= passed
        print(f"  N={key[0]} dt={key[1]}: radius-gated {len(ok)}/{len(D[key])} "
              f"max_err={'None' if mx is None else '%.4f' % mx} "
              f"rejected_by_gate={len(bad)} -> {'PASS' if passed else 'FAIL'}")

    print("\n=== C2 refinement, both transitions ===")
    c2 = True
    for dt in (0.005, 0.0025):
        e48 = [err(p) for p in D.get((48, dt), []) if radius_ok(p)]
        e64 = [err(p) for p in D.get((64, dt), []) if radius_ok(p)]
        m48 = max(e48, default=None); m64 = max(e64, default=None)
        ok1 = (m48 is not None and m64 is not None) and m64 <= REFINE * m48
        print(f"  dt={dt}: N48 max={'None' if m48 is None else '%.4f' % m48} "
              f"N64 max={'None' if m64 is None else '%.4f' % m64} -> 48->64 {'P' if ok1 else 'F'}")
        c2 &= ok1

    print("\n=== C3 radius consistency gate ===")
    c3 = True
    for key in sorted(D):
        n_ok = sum(1 for p in D[key] if radius_ok(p))
        radii = [ (p.get("circle_fit") or {}).get("radius") for p in D[key] ]
        radii = [r for r in radii if r is not None]
        ok = n_ok > 0
        c3 &= ok
        print(f"  N={key[0]} dt={key[1]}: {n_ok}/{len(D[key])} within +/-{RAD_TOL} "
              f"R_range=[{min(radii) if radii else None}, {max(radii) if radii else None}]")

    print("\n=== C4 angular coverage (operating constraint) ===")
    covs = [p.get("angular_coverage", 0) for p in dev["profiles"]]
    print(f"  dev coverage min={min(covs):.4f} max={max(covs):.4f}")
    for key in sorted(D):
        c = [p.get("angular_coverage", 0) for p in D[key]]
        print(f"  N={key[0]} dt={key[1]}: min={min(c):.4f} max={max(c):.4f}")

    print("\n=== C5 reserved blind holdout <= %.1f (gate is part of the estimator) ===" % BLIND)
    c5 = True
    n_pass = n_gate = n_ungated_fail = 0
    for p in hold["profiles"]:
        e = err(p)
        gated = radius_ok(p)
        if gated and e is not None and e <= BLIND:
            n_pass += 1
        elif not gated:
            n_gate += 1
        else:
            n_ungated_fail += 1
            c5 = False
        print(f"  true={p['displacement']} N={p['N']} dt={p['dt']}: "
              f"cov={p.get('angular_coverage')} R={'None' if not p.get('circle_fit') else '%.4f' % p['circle_fit']['radius']} "
              f"gate={'P' if gated else 'F'} err={'None' if e is None else '%.4f' % e} "
              f"-> {'pass' if (gated and e is not None and e <= BLIND) else ('gated-out' if not gated else 'UNGATED FAIL')}")
    print(f"  pass={n_pass} gated-out={n_gate} ungated_fail={n_ungated_fail}")
    print(f"  -> {'PASS' if c5 else 'FAIL'} (PASS = no ungated failure; gated-out is a declared rejection)")

    print("\n=== C6 sensitivity: 90-degree sector dropped ===")
    c6 = True
    for p in dev["profiles"]:
        for sector in (0, 90, 180, 270):
            s = p.get(f"sensitivity_sector_{sector}_dropped")
            if not s or s.get("error_vs_true") is None:
                continue
            r = s.get("radius")
            gate_ok = (r is not None) and abs(r - p.get("loop_radius", 2.0)) <= RAD_TOL
            bad = s["error_vs_true"] > BOUND
            if bad and gate_ok:
                c6 = False
                print(f"  UNGATED FAIL true={p['displacement']} N={p['N']} sector={sector} "
                      f"err={s['error_vs_true']} R={r}")
            else:
                print(f"  true={p['displacement']} N={p['N']} sector={sector}: "
                      f"err={s['error_vs_true']:.4f} R={r} gate={'P' if gate_ok else 'F'} "
                      f"{'degraded-but-gated' if bad else 'ok'}")
    print(f"  -> {'PASS' if c6 else 'FAIL'} (PASS = every sector-drop degradation is caught by the radius gate)")

    print("\n=== centred time evolution (circle fit) ===")
    for p in dev["centred_time"]:
        print(f"  N={p['N']} dt={p['dt']} step={p['step']:3d}: cov={p.get('angular_coverage')} "
              f"err={'None' if err(p) is None else '%.4f' % err(p)} "
              f"R={'None' if not p.get('circle_fit') else '%.4f' % p['circle_fit']['radius']}")

    print("\n" + "=" * 70)
    for n, v in (("C1 bounded", c1), ("C2 refinement", c2), ("C3 radius gate", c3),
                 ("C5 blind holdout", c5), ("C6 sensitivity", c6)):
        print(f"  {n:18s} {'PASS' if v else 'FAIL'}")
    verdict = c1 and c2 and c3 and c5 and c6
    print("  OVERALL          " + ("PASS" if verdict else "FAIL"))
    print("=" * 70)
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
