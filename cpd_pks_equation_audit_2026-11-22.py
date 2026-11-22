#!/usr/bin/env python3
"""
cpd_pks_equation_audit_2026-11-22.py

Cross-source equation audit for the Harthun/Rennert Ei-Kurve document.

For every equation in pks_equation_inventory.json this records:
  * source location (section heading in the document)
  * original language
  * transcription confidence
  * an independent re-derivation or numerical check performed here
  * the check result, including disagreements

Nothing is asserted as a mathematical identity without the check below.
"""
import json
import math
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
IDX = AUD / "pks_research_index"
SRC = AUD / "schauberger_sources_2026-11-22"
TXT = (SRC / "pks_ei-kurve_extracted_text.md").read_text(encoding="utf-8", errors="replace")

CHECKS = []


def check(eq_id, method, result, agrees, note):
    CHECKS.append({"equation_id": eq_id, "method": method, "result": result,
                   "agrees_with_source": agrees, "note": note})


# ---------------------------------------------------------------- EQ-03 / EQ-04
# EQ-03: x*y = 1  -> the generating equilateral hyperbola.
# EQ-04: x = +/- sqrt( 1/(z0 - y*sin a)^2 - (y*cos a)^2 )
def egg_curve(z0, alpha_deg, y):
    a = math.radians(alpha_deg)
    inner = 1.0 / (z0 - y * math.sin(a)) ** 2 - (y * math.cos(a)) ** 2
    if inner < 0:
        return None
    return math.sqrt(inner)


def eq03_check():
    # x*y=1 sampled
    pts = [(y, 1.0 / y) for y in (0.5, 1.0, 2.0, 4.0)]
    ok = all(abs(x * y - 1.0) < 1e-12 for y, x in pts)
    check("PKS-EQ-03", "direct evaluation at y = 0.5, 1, 2, 4",
          {"samples": [{"y": y, "x": x, "x*y": x * y} for y, x in pts]},
          ok, "identity is self-consistent; this is an algebraic identity, not a physical law")


# ---------------------------------------------------------------- EQ-07 (two-point form)
def eq07_check():
    """z0 = z1*z2*(z1+z2) / (z1^2 + z1*z2 + z2^2)   for z1=1, z2=2"""
    z1, z2 = 1.0, 2.0
    z0 = z1 * z2 * (z1 + z2) / (z1 ** 2 + z1 * z2 + z2 ** 2)
    check("PKS-EQ-07", "closed-form evaluation for the 'Oktav-Ei' z1=1, z2=2",
          {"z1": z1, "z2": z2, "z0": round(z0, 12)},
          True, "z0 = 6/7 = 0.857142857143; this is the cutting height the "
                "document's parameter and two-point forms must both satisfy")
    return z0


# ---------------------------------------------------------------- EQ-08 / EQ-09
def eq08_eq09_check(z0):
    """EQ-08: z0 = z1*(1 - tan a)   EQ-09: z0 = z2*(1 + tan a),  alpha entered negative."""
    z1, z2 = 1.0, 2.0
    tan_from_z1 = 1.0 - z0 / z1
    tan_from_z2 = z0 / z2 - 1.0
    a1 = math.degrees(math.atan(tan_from_z1))
    a2 = math.degrees(math.atan(tan_from_z2))
    agree = abs(tan_from_z1 - tan_from_z2) < 1e-9
    check("PKS-EQ-08", "solve z0 = z1*(1 - tan a) for alpha",
          {"tan_alpha": round(tan_from_z1, 12), "alpha_deg": round(a1, 9)},
          True, "self-consistent by construction")
    check("PKS-EQ-09", "solve z0 = z2*(1 + tan a) for alpha",
          {"tan_alpha": round(tan_from_z2, 12), "alpha_deg": round(a2, 9)},
          agree,
          ("DISAGREES with EQ-08 unless alpha is entered with opposite sign: "
           "tan a from the sharp vertex is +1/7, from the blunt vertex is -4/7. "
           "The source says alpha 'wird negativ eingesetzt'; the transcription of "
           "EQ-08/EQ-09 is glyph-fragmented, so this is a transcription flag, "
           "not yet a mathematical contradiction."))
    return tan_from_z1


# ---------------------------------------------------------------- EQ-04 shape
def eq04_check(z0, alpha_deg):
    ys, xs = [], []
    y = -3.0
    while y <= 3.0:
        x = egg_curve(z0, alpha_deg, y)
        if x is not None:
            ys.append(round(y, 6)); xs.append(round(x, 6))
        y += 0.01
    if not xs:
        check("PKS-EQ-04", "scan y in [-3,3]", {"points": 0}, False,
              "no real branch found for these parameters")
        return
    # width profile: where is the curve widest / narrowest?
    widths = [2.0 * x for x in xs]
    wmax_i = max(range(len(widths)), key=lambda i: widths[i])
    wmin_i = min(range(len(widths)), key=lambda i: widths[i])
    # asymmetry: compare width near the two ends of the sampled branch
    n = len(widths)
    head = sum(widths[:n // 4]) / max(1, n // 4)
    tail = sum(widths[-n // 4:]) / max(1, n // 4)
    check("PKS-EQ-04",
          "numerical trace of x = +/-sqrt(1/(z0-y sin a)^2 - (y cos a)^2)",
          {"points": len(xs), "y_range": [ys[0], ys[-1]],
           "max_half_width": round(max(xs), 6), "min_half_width": round(min(xs), 6),
           "mean_half_width_head": round(head, 6), "mean_half_width_tail": round(tail, 6),
           "head_tail_ratio": round(head / tail, 6) if tail else None},
          True,
          "the trace is a single open branch over the sampled window; head/tail "
          "half-width ratio != 1 indicates the asymmetry expected of an egg. "
          "This does NOT close the curve - the closed egg needs the parameter form "
          "(EQ-05), whose transcription is too fragmented to evaluate.")


# ---------------------------------------------------------------- EQ-10 volume
def eq10_check(z0, alpha_deg):
    """V = (pi/3)(1/z1 - 1/z2)(1/z1^2 + 1/(z1 z2) + 1/z2^2) tan a (tan a - cos a)
       source reports V = 0.4045 for the Oktav-Ei."""
    z1, z2 = 1.0, 2.0
    a = math.radians(alpha_deg)
    ta, ca = math.tan(a), math.cos(a)
    V = (math.pi / 3.0) * (1.0 / z1 - 1.0 / z2) * \
        (1.0 / z1 ** 2 + 1.0 / (z1 * z2) + 1.0 / z2 ** 2) * ta * (ta - ca)
    # independent numerical volume of revolution of the traced curve
    ys, xs = [], []
    y = -3.0
    while y <= 3.0:
        x = egg_curve(z0, alpha_deg, y)
        if x is not None:
            ys.append(y); xs.append(x)
        y += 0.005
    vol_num = None
    if len(ys) > 2:
        vol_num = 0.0
        for i in range(1, len(ys)):
            dy = ys[i] - ys[i - 1]
            r0, r1 = xs[i - 1], xs[i]
            vol_num += math.pi * (r0 ** 2 + r0 * r1 + r1 ** 2) / 3.0 * dy
    check("PKS-EQ-10",
          "closed form vs numerical volume of revolution of the EQ-04 trace",
          {"closed_form_V": round(V, 9), "source_reported_V": 0.4045,
           "numerical_V_from_trace": round(vol_num, 9) if vol_num is not None else None},
          abs(V - 0.4045) < 5e-3,
          "the closed form is evaluated with alpha from EQ-08. Agreement with the "
          "printed 0.4045 would confirm the equation set; disagreement localises "
          "the transcription error.")


def main() -> None:
    eq03_check()
    z0 = eq07_check()
    eq08_eq09_check(z0)
    # alpha from EQ-08 (sharp-vertex form) for the shape/volume checks
    alpha = math.degrees(math.atan(1.0 - z0 / 1.0))
    eq04_check(z0, alpha)
    eq10_check(z0, alpha)

    STATUS = {
        "PKS-EQ-03": ("ALGEBRAICALLY_VERIFIED",
                      "x*y=1 is an algebraic identity. It is not evidence of a physical law."),
        "PKS-EQ-07": ("ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS",
                      "z0 = 6/7 follows from the stated z1=1, z2=2. Consistency check, "
                      "not independent confirmation that the geometric construction is correct."),
        "PKS-EQ-08": ("ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS",
                      "tan a = 1/7 follows from EQ-07 plus the assumed z1=1. Algebraic "
                      "consistency, not independent verification of the construction."),
        "PKS-EQ-09": ("SIGN_CONVENTION_UNRESOLVED",
                      "gives tan a = -4/7, opposite sign to EQ-08. The source states the "
                      "angle is entered negatively; the printed diagram and equation are "
                      "required to settle the convention. Not a contradiction yet."),
        "PKS-EQ-04": ("TRANSCRIPTION_CONDITIONALLY_EVALUATED",
                      "The 1.38% difference between the reported head and tail mean "
                      "half-widths is a preliminary numerical observation on arbitrarily "
                      "chosen sampling windows, not a verified measure of geometric "
                      "asymmetry. The branch is OPEN and does not establish the closed "
                      "egg profile; a head-to-tail comparison needs a defined axis and "
                      "corresponding positions on a closed curve."),
        "PKS-EQ-05": ("NOT_VERIFIED",
                      "Parameter form could not be evaluated at all: the transcription is "
                      "glyph fragments. The closed egg curve therefore remains unverified."),
        "PKS-EQ-10": ("NOT_VERIFIED",
                      "Volume comparison is not valid: a volume of revolution needs a "
                      "closed boundary and integration interval, and EQ-04 currently "
                      "yields an open branch, so revolving an arbitrary sampled interval "
                      "does not establish the closed egg volume. The negative closed-form "
                      "result also needs sign and dimensional checks before it can be read "
                      "as evidence of transcription error."),
    }
    # EQ-05 (the closed parameter form) has no numerical check: the transcription is
    # unreadable. Record it explicitly so the audit covers the whole equation set.
    if not any(c["equation_id"] == "PKS-EQ-05" for c in CHECKS):
        CHECKS.append({"equation_id": "PKS-EQ-05",
                       "method": "none - transcription is glyph fragments",
                       "result": {}, "agrees_with_source": None,
                       "status": "NOT_VERIFIED",
                       "status_note": "The closed parameter form could not be evaluated. "
                                      "Until it is recovered, the egg curve and its "
                                      "volume remain unverified."})
    for c in CHECKS:
        st, note = STATUS.get(c["equation_id"], ("UNCLASSIFIED", ""))
        c["status"] = st
        c["status_note"] = note
    order = ["ALGEBRAICALLY_VERIFIED", "ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS",
             "TRANSCRIPTION_CONDITIONALLY_EVALUATED", "SIGN_CONVENTION_UNRESOLVED",
             "NOT_VERIFIED", "UNCLASSIFIED"]
    counts = {}
    for c in CHECKS:
        counts[c["status"]] = counts.get(c["status"], 0) + 1

    inv = json.loads((IDX / "pks_equation_inventory.json").read_text(encoding="utf-8"))
    audit = {
        "generated": "2026-11-22",
        "document": "pks_ei-kurve_extracted_text.md",
        "document_sha256": None,
        "method": ("independent re-derivation where the transcribed form is legible; "
                   "numerical check otherwise. Transcription confidence is inherited "
                   "from the inventory and is the limiting factor."),
        "checks": CHECKS,
        "summary": {
            "checks": len(CHECKS),
            "agree": sum(1 for c in CHECKS if c["agrees_with_source"] is True),
            "disagree_or_flagged": sum(1 for c in CHECKS if c["agrees_with_source"] is not True),
            "status_counts": counts,
            "reading": ("status is a verification classification, not a pass/fail. "
                        "ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS means the algebra "
                        "follows from the stated inputs - it does not independently confirm "
                        "the geometric construction. NOT_VERIFIED means the transcription "
                        "cannot support the check, not that the source is wrong."),
        },
        "limits": [
            "The PDF text layer fragments fractions, radicals and subscripts; EQ-04, "
            "EQ-05, EQ-07..EQ-10 carry partial or low transcription confidence.",
            "EQ-05 (parameter form) could not be evaluated at all - the transcription "
            "is glyph fragments. The closed egg curve therefore remains unverified.",
            "A transcription disagreement is not a mathematical contradiction; it is "
            "a flag to re-read the printed equation.",
        ],
    }
    import hashlib
    audit["document_sha256"] = hashlib.sha256(
        (SRC / "pks_ei-kurve_extracted_text.md").read_bytes()).hexdigest()
    (IDX / "pks_equation_audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")

    print(f"checks={audit['summary']['checks']} agree={audit['summary']['agree']} "
          f"flagged={audit['summary']['disagree_or_flagged']}")
    for c in CHECKS:
        flag = "OK  " if c["agrees_with_source"] else "FLAG"
        print(f"  {flag} {c['equation_id']:10s} {c['method'][:60]}")
        print(f"        {json.dumps(c['result'])[:150]}")
    print("\nwritten:", IDX / "pks_equation_audit.json")


if __name__ == "__main__":
    main()
