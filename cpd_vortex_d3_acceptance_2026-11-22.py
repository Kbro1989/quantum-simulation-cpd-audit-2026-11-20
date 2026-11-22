#!/usr/bin/env python3
"""
cpd_vortex_d3_acceptance_2026-11-22.py

Separable acceptance evaluator for the D3 remediation.  Reads the measurement
JSON; applies the criteria that were fixed BEFORE the run; prints a verdict.

  * replacement estimators only -- the baseline centroid is a CONTROL and is
    excluded from the PASS criterion
  * spatial refinement uses N = 48, 64, 96
  * temporal frames are reported separately from frame-slice observations
"""
import json
import math
import sys
from pathlib import Path

IDX = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20\pks_research_index")
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else IDX / "quantum_vortex_d3_remediation_v2.json"

REPLACEMENTS = ("disc_intersection", "boundary_bisection")
CONTROL = "baseline_centroid"


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    acc = d.get("acceptance_criteria") or {
        "bounded_error": 1.0, "refine_factor": 1.2, "agree": 0.5, "blind": 0.5}
    BOUND = acc["bounded_error"]; REF = acc["refine_factor"]
    AGREE = acc["agree"]; BLIND = acc["blind"]

    if "fresh_validation" in d:
        # ---- revision-3 diagnostic schema: independent blind validation ----
        print("=" * 78)
        print("D3 REVISION 3 — FRESH INDEPENDENT BLIND VALIDATION")
        print("source:", SRC.name)
        print("discipline:", d["blind_profile_discipline"])
        print("=" * 78)
        for group in ("baseline_comparison", "fresh_validation"):
            rows = d[group]
            print(f"\n--- {group} ({len(rows)} profiles) ---")
            ok_all = True
            for r in rows:
                line = []
                for seed_name in ("centroid_seed", "verified_hit_seed"):
                    b = r.get(seed_name)
                    if not b:
                        line.append(f"{seed_name}=none"); ok_all = False; continue
                    e = b.get("error_vs_true")
                    good = (b.get("coverage") == "ok") and (e is not None) and e <= BLIND
                    ok_all &= good
                    line.append(f"{seed_name}: cov={b.get('coverage')} "
                                f"err={'None' if e is None else '%.4f' % e} "
                                f"{'P' if good else 'F'}")
                print(f"  true={r['displacement']}  " + " | ".join(line))
            print(f"  -> {group}: {'PASS' if ok_all else 'FAIL'}")
        print("\nDiagnostic termination reasons observed:")
        reasons = {}
        for group in ("baseline_comparison", "fresh_validation"):
            for r in d[group]:
                for seed_name in ("centroid_seed", "verified_hit_seed"):
                    b = r.get(seed_name) or {}
                    for k, v in (b.get("directions") or {}).items():
                        reasons[v["reason"]] = reasons.get(v["reason"], 0) + 1
        for k, v in sorted(reasons.items()):
            print(f"   {k}: {v}")
        print("\nNote: revision 3 is DIAGNOSTIC. D3 remains NOT VALIDATED.")
        return 0


    print("=" * 78)
    print("D3 REMEDIATION REVISION 2 — ACCEPTANCE EVALUATION")
    print("criteria fixed before the run:", json.dumps(acc))
    print("control (excluded from PASS):", CONTROL)
    print("=" * 78)

    # ---------- temporal frames, per estimator ----------
    print("\n--- TEMPORAL FRAMES (z = 0 slice) ---")
    print(f"{'run':>14s} {'est':>18s} {'frames':>7s} {'answers':>8s} {'max_err':>9s}")
    frame_stats = {}
    for run in d["runs"]:
        key = f"N={run['N']} dt={run['dt']}"
        for est in REPLACEMENTS + (CONTROL,):
            errs, ans = [], 0
            for fr in run["frames"]:
                s = fr["slices"]["0.0"][est]
                if s.get("core") is not None:
                    ans += 1
                    if s.get("err_vs_ref") is not None:
                        errs.append(s["err_vs_ref"])
            mx = max(errs) if errs else None
            frame_stats[(run["N"], run["dt"], est)] = (mx, ans, len(run["frames"]))
            print(f"{key:>14s} {est:>18s} {len(run['frames']):>7d} {ans:>8d} "
                  f"{('None' if mx is None else f'{mx:.4f}'):>9s}")

    # ---------- frame-slice observations (all z) ----------
    print("\n--- FRAME-SLICE OBSERVATIONS (all z-slices) ---")
    print(f"{'run':>14s} {'est':>18s} {'obs':>5s} {'answers':>8s} {'max_err':>9s}")
    slice_stats = {}
    for run in d["runs"]:
        key = f"N={run['N']} dt={run['dt']}"
        for est in REPLACEMENTS + (CONTROL,):
            errs, ans, tot = [], 0, 0
            for fr in run["frames"]:
                for z, s in fr["slices"].items():
                    tot += 1
                    r = s[est]
                    if r.get("core") is not None:
                        ans += 1
                        if r.get("err_vs_ref") is not None:
                            errs.append(r["err_vs_ref"])
            mx = max(errs) if errs else None
            slice_stats[(run["N"], run["dt"], est)] = (mx, ans, tot)
            print(f"{key:>14s} {est:>18s} {tot:>5d} {ans:>8d} "
                  f"{('None' if mx is None else f'{mx:.4f}'):>9s}")

    # ---------- C1 bounded ----------
    print("\n[C1] bounded error <= %.2f (replacements only, frame-slices)" % BOUND)
    c1 = True
    for (N, dt, est), (mx, ans, tot) in slice_stats.items():
        if est == CONTROL:
            continue
        ok = mx is not None and mx <= BOUND and ans == tot
        c1 &= ok
        print(f"   N={N} dt={dt} {est:>18s} max={mx} answers={ans}/{tot} -> {'PASS' if ok else 'FAIL'}")

    # ---------- C2 refinement (both directions, both timesteps) ----------
    print("\n[C2] refinement, both directions: err(64) <= %.1f*err(48) AND err(96) <= %.1f*err(64)" % (REF, REF))
    c2 = True
    for est in REPLACEMENTS:
        for dt in (0.005, 0.0025):
            e48 = slice_stats.get((48, dt, est), (None,))[0]
            e64 = slice_stats.get((64, dt, est), (None,))[0]
            e96 = slice_stats.get((96, dt, est), (None,))[0]
            ok1 = (e48 is not None and e64 is not None) and e64 <= REF * e48
            ok2 = (e64 is not None and e96 is not None) and e96 <= REF * e64
            c2 &= (ok1 and ok2)
            print(f"   {est} dt={dt}: N48={e48} N64={e64} N96={e96} "
                  f"48->64 {'P' if ok1 else 'F'} 64->96 {'P' if ok2 else 'F'}")

    # ---------- C3 agreement ----------
    print("\n[C3] |B - C| <= %.2f (frames where both answer)" % AGREE)
    c3 = True
    any_pair = False
    for run in d["runs"]:
        diffs = [fr["slices"][z]["B_vs_C"] for fr in run["frames"]
                 for z in fr["slices"] if fr["slices"][z].get("B_vs_C") is not None]
        if diffs:
            any_pair = True
            ok = max(diffs) <= AGREE
            c3 &= ok
            print(f"   N={run['N']} dt={run['dt']}: n={len(diffs)} max|B-C|={max(diffs):.4f} -> {'PASS' if ok else 'FAIL'}")
        else:
            c3 = False
            print(f"   N={run['N']} dt={run['dt']}: no comparable observations -> FAIL")
    if not any_pair:
        c3 = False

    # ---------- C4 unambiguous ----------
    print("\n[C4] unambiguous (competing minima == 1)")
    comp = [fr["slices"][z]["reference"]["competing"] for run in d["runs"]
            for fr in run["frames"] for z in fr["slices"]]
    c4 = max(comp) == 1
    print(f"   max competing = {max(comp)}, distinct = {sorted(set(comp))} -> {'PASS' if c4 else 'FAIL'}")

    # ---------- C5 blind ----------
    print("\n[C5] blind displaced profiles <= %.2f (replacements only)" % BLIND)
    c5 = True
    for b in d["blind_tests"]:
        row = []
        for est in REPLACEMENTS:
            r = b.get(est)
            ok = r is not None and r["error"] <= BLIND
            shown = "None" if r is None else "%.4f" % r["error"]
            row.append(est + "=" + shown + "->" + ("P" if ok else "F"))
            c5 &= ok
        print(f"   true={b['true']} ref={b['reference']} " + "  ".join(row))

    # ---------- verdict ----------
    print("\n" + "=" * 78)
    for name, v in (("C1 bounded", c1), ("C2 refinement", c2), ("C3 agreement", c3),
                    ("C4 unambiguous", c4), ("C5 blind", c5)):
        print(f"  {name:16s} {'PASS' if v else 'FAIL'}")
    verdict = c1 and c2 and c3 and c4 and c5
    print("  OVERALL          " + ("PASS" if verdict else "FAIL"))
    print("=" * 78)
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
