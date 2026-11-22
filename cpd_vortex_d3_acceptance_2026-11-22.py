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
SRC = IDX / "quantum_vortex_d3_remediation_v2.json"

REPLACEMENTS = ("disc_intersection", "boundary_bisection")
CONTROL = "baseline_centroid"


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    acc = d["acceptance_criteria"]
    BOUND = acc["bounded_error"]; REF = acc["refine_factor"]
    AGREE = acc["agree"]; BLIND = acc["blind"]

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

    # ---------- C2 refinement ----------
    print("\n[C2] refinement: err(N=64) <= %.1f * err(N=48); N=96 reported" % REF)
    c2 = True
    for est in REPLACEMENTS:
        for dt in (0.005, 0.0025):
            a = slice_stats.get((48, dt, est), (None,))[0]
            b = slice_stats.get((64, dt, est), (None,))[0]
            c = slice_stats.get((96, dt, est), (None,))[0]
            if a is None or b is None:
                ok = False
                print(f"   {est} dt={dt}: N48={a} N64={b} N96={c} -> FAIL (insufficient)")
            else:
                ok = b <= REF * a
                print(f"   {est} dt={dt}: N48={a:.4f} N64={b:.4f} N96={c} -> {'PASS' if ok else 'FAIL'}")
            c2 &= ok

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
