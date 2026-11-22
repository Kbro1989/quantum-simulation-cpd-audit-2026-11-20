# D3 remediation revision 2 — geometry corrected, still NOT VALIDATED

**Date:** 2026-11-22
**Script:** `cpd_vortex_d3_remediation_v2_2026-11-22.py`
**Evaluator:** `cpd_vortex_d3_acceptance_2026-11-22.py`
**Measurements:** `pks_research_index/quantum_vortex_d3_remediation_v2.json`
**Preserved immutable:** `b7b3391` (Gate 1 failure), `895bec2` (revision 1).

---

## 1. The defect that revision 1 hid

Revision 1's bilinear sampler **clamped out-of-domain loop samples to the grid edge**.
A loop hanging off the domain therefore re-sampled boundary values, which can
manufacture winding. Every estimate in revision 1 was contaminated by that.

Revision 2 rejects any loop not wholly inside the valid interpolation domain. Nothing
is clamped. Valid and rejected loop counts are recorded per frame, grid and z-slice.

## 2. Effect — an order of magnitude

| estimator | revision 1 max err | revision 2 max err |
|---|---|---|
| baseline centroid (**control**, excluded from PASS) | 2.71–3.36 | 0.49–1.48 |
| disc intersection | empty / 0.13 | 0.0994–0.1326, coverage 9–33 of 33 |
| boundary bisection | 1.07–2.78 | **0.2433–0.7415, 33/33 frames** |

**The revision-1 "hit-set growth" was boundary contamination, not phase structure.**
Rejected-loop counts are now constant — 80 for R=2 and 188 for R=3 on every frame —
so the growth was an artefact of clamped sampling, and no physical claim can rest on
it. Boundary contamination is now excluded *and* quantified.

## 3. Corrections applied

1. Bilinear sampling rejects out-of-domain loops; the whole loop must lie inside the
   domain.
2. `hit_set` keeps boundary-valid centres only and records valid vs rejected counts.
3. Hit-set growth reassessed on valid loops only — see §2.
4. The fixed 0.5-unit disc lattice is replaced by a **continuous feasibility test**
   (max-min slack over the true disc intersection, adaptive refinement). Reference
   containment is reported as a diagnostic only, never an estimator input.
5. Boundary bisection verifies the starting classification, requires a **valid**
   opposite-classification bracket in each direction, rejects invalid loops, and
   retains all four crossing coordinates.
6. The original centroid is kept as a **control**, excluded from the PASS criterion.
7. Acceptance is a separate executable, includes N=96 in refinement, and reports
   temporal frames separately from frame-slice observations.
8. Output is strict JSON — NaN → null.

## 4. Acceptance — overall FAIL

Replacements only; control excluded.

| criterion | result |
|---|---|
| bounded error ≤ 1.0 | **FAIL** — disc intersection coverage 9–33/33; bisection passes all 6 runs |
| refinement not worse (N=64 ≤ 1.2·N=48; N=96 reported) | **FAIL** — disc intersection 0.1326 vs 0.0994 |
| B/C agreement ≤ 0.5 | **PASS** — 0.029–0.133 |
| unambiguous | **PASS** — competing minima = 1 |
| blind displaced ≤ 0.5 | **FAIL** — bisection returns nothing on 2 of 3 |

Per-run detail (frame-slices, max error / answers):

| run | disc intersection | boundary bisection |
|---|---|---|
| N=48 dt=.005 | 0.0994, 9/33 | 0.5778, 33/33 |
| N=48 dt=.0025 | 0.0994, 18/33 | 0.2433, 33/33 |
| N=64 dt=.005 | 0.1326, 27/33 | 0.2695, 33/33 |
| N=64 dt=.0025 | 0.1326, **33/33** | 0.0001, 33/33 |
| N=96 dt=.005 | 0.0994, 12/33 | 0.7415, 33/33 |
| N=96 dt=.0025 | 0.0994, 21/33 | 0.2433, 33/33 |

**Boundary bisection is now good** — full coverage, error under 0.75 — but it fails
the blind displaced tests on two of three profiles, so it cannot be promoted on the
strength of the centred case alone. **Disc intersection is accurate but
inconsistent.** Neither passes the predeclared criteria, so **D3 remains
`NOT VALIDATED`**.

## 5. Disposition

- **D2** topology detection works.
- **D3** spatial localization: geometry corrected, estimators improved, **still not
  validated**.
- **Gate 2** (GPE stationarity) remains `NOT_TESTED`. Not started.

## 6. Next

- Fix boundary bisection's blind failures — two displaced profiles return nothing;
  find which direction fails to bracket and why.
- Give disc intersection a reported coverage rather than silence.
- Only then re-run the acceptance evaluator; do not promote until every criterion
  passes on valid loops, including displaced cores.
