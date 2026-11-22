# D3 remediation revision 4 — circle fitting

**Date:** 2026-11-22
**Script:** `cpd_vortex_d3_remediation_v4_2026-11-22.py`
**Evaluator:** `cpd_vortex_d3_acceptance_v4_2026-11-22.py`
**Measurements:** `pks_research_index/quantum_vortex_d3_remediation_v4.json` (development),
`..._v4_holdout.json` (reserved holdout)
**Preserved immutable:** `b7b3391`, `895bec2`, `d259430`, `8bfcd92`.

**Status: NOT VALIDATED.** Circle fitting is a genuine improvement and confirms the
hypothesis, but it fails the predeclared criteria and has a quantified operating
envelope.

---

## 1. Hypothesis

For an isolated unit-winding vortex, the set of loop centres whose radius-R loop
encloses it is the disc `|c − x_v| < R`, whose boundary is a **circle of radius R
centred on the vortex**. Every recorded crossing lies on that circle, so fitting it
recovers the centre **without assuming the four-crossing mean is unbiased**.

**Hypothesis: the earlier weakness was the four-direction centre approximation, not
the winding-boundary geometry.**

## 2. Result — hypothesis confirmed

The four-crossing control returned **`None` in nearly every case** (fewer than four
cardinal crossings survive the domain), while the circle fit produced an answer. Where
both answered, the fit was far better:

| true displacement | circle-fit error | four-crossing control |
|---|---|---|
| (0.5, 1.25) N=48 | **0.0074** | (0.5000, 1.2679) → 0.018 |
| (0.5, 1.25) N=64 | **0.0412** | (0.4687, 1.1562) → 0.108 |

Centred time evolution — the strongest result:

| run | step 0 | step 100 | step 200 |
|---|---|---|---|
| N=48 dt=.005 | 0.0231 | 0.1451 | 0.0937 |
| N=48 dt=.0025 | 0.0231 | 0.0420 | 0.1451 |
| N=64 dt=.005 | **0.0000** | **0.0002** | 0.0150 |
| N=64 dt=.0025 | **0.0000** | **0.0000** | **0.0002** |

At N=64 the fit recovers the vortex to ~0.0002 with `R_fit = 2.0000` exactly.

## 3. Independent radius gate

`R_fit` should equal the loop radius (2.0). This is a **self-consistency gate that
needs no ground truth**: a fit whose radius is not ≈ R is not the expected disc
boundary. It works — on the worst holdout profile it rejects a fit with
`R_fit = 1.18` and error 1.81.

## 4. Acceptance — overall FAIL

| criterion | result |
|---|---|
| C1 bounded ≤ 1.0 (radius-gated) | **PASS** — all four runs, max 0.547 |
| C2 refinement 48→64 | **PASS** (0.5023 → 0.5473) |
| C3 radius gate | **PASS** — 7/7 in every run, R ∈ [1.94, 2.17] |
| C5 reserved blind holdout ≤ 0.5 | **FAIL** — 14 pass, 4 gated-out, **2 ungated failures** |
| C6 sector-drop sensitivity | **FAIL** — 4 ungated degradations the ±0.35 gate misses |

The estimator file SHA-256 is **identical** across the development and holdout runs
(`0b108d82e7ad83b0…`) — it was frozen before the holdout was evaluated.

## 5. Operating envelope (the honest constraint)

Accuracy is governed by **angular coverage**, not by the estimator's core math:

| coverage | n | max error | mean error |
|---|---|---|---|
| 0.5 | 2 | 1.8149 | 1.8149 |
| 0.6 | 6 | 1.0688 | 0.6215 |
| 0.7 | 8 | 0.4199 | 0.3711 |
| 0.8 | 20 | 0.5473 | 0.3166 |
| 0.9 | 2 | 0.0000 | 0.0000 |
| 1.0 | 10 | 0.0897 | 0.0312 |

**Operating constraint:** the estimator needs coverage ≳ 0.9 for sub-0.1 accuracy,
degrades through 0.6–0.8, and fails below ~0.6. Coverage is limited by the
valid-domain boundary (revision 3's finding), so this is a **domain-size constraint
on the estimator**, not a defect in the fit.

This is recorded as an operating constraint, **not** claimed as general localization.

## 6. Blind-profile discipline

The four revision-3 displacements had been inspected, so they were used for
development/comparison only. A **reserved holdout of five fresh displacements** —
(1.75, 2.25), (−2.5, −1.75), (2.75, −2.25), (−1.75, 2.75), (0.5, 1.25) — was frozen
before evaluation and used only for C5.

## 7. Disposition

- **D2** topology detection works.
- **D3** circle fitting is a real improvement and confirms the hypothesis; it passes
  C1/C2/C3 and the centred time evolution, but **fails C5 and C6**, so **D3 remains
  `NOT VALIDATED`**.
- **Gate limitation:** the ±0.35 radius tolerance misses some degraded fits
  (e.g. `R_fit = 1.69`, error 1.04). Tightening it would be tuning against the
  holdout, so it is reported instead.
- **Gate 2** remains `NOT_TESTED`.

## 8. Next

- The gate should be derived from the fit's own residual/conditioning rather than a
  fixed radius tolerance.
- Coverage is the binding constraint; enlarging the domain (or reducing the loop
  radius) would widen the envelope, but that changes the experiment, not the estimator.
