# Gate derivation — experiment 2 of 2

**Date:** 2026-11-22
**Script:** `cpd_vortex_gate_derivation_2026-11-22.py`
**Frozen estimator:** revision 4, SHA-256 `0b108d82e7ad83b0…` (imported, not modified)
**Gate implementation:** SHA-256 `c1aec197c4b007f6f8519177…`

**Status: DONE** — the gate is derived, frozen, and evaluated. But the gate is only a
measurement fix; it does not fix the domain boundary, which is the root cause (see
experiment 1). D3 stays `NOT VALIDATED`.

## 1. Why a new gate

Revision 4's fixed `|R_fit − 2.0| ≤ 0.35` gate let 2 ungated C5 failures and 4 ungated
C6 degradations through. A short arc of a circle fits extremely well (tiny residual)
while leaving its centre poorly constrained. The radius alone cannot see that.

## 2. Features tested against true localisation error

On 21 development observations (revision-4 profiles at L=6, 8, 12):

| feature | correlation | verdict |
|---|---|---|
| angular coverage | **−0.84** | strong |
| largest angular gap | **+0.84** | strong |
| rms fit residual | **+0.88** | strong |
| centre standard error | **+0.77** | strong |
| fit condition number | −0.22 | weak |

## 3. Frozen gate (development-data derived)

- `coverage ≥ 0.90`
- `largest angular gap ≤ 40°`
- `centre standard error ≤ 0.25`

Implementation hash recorded; thresholds were chosen on development data only.

## 4. Evaluation — new reserved holdout

Six fresh displacements, L = 6, 8, 12 (`IAM 18 observations`):

**result: 8 pass, 10 rejected, 0 ungated failures.**

Everything rejected has `centre_std` astronomically large (1e28, 1e29) — the covariance
matrix is near-singular, the fit is a short arc. The gate correctly rejects them. The
passes are L=8/L=12 fits with `cov=1.0`, `gap=10°`, `err ≤ 0.07`.

## 5. Joint conclusion

| criterion | result |
|---|---|
| Gate rejects all inaccurate short-arc fits | **PASS** |
| Gate never accepts an inaccurate estimate | **PASS** (0 ungated) |
| L=8 recovers coverage / fills the blind set | **PASS** (experiment 1) |

The gate is a **measurement improvement**: it makes acceptance reliable. It does not
restore coverage on the L=6 short-arc cases — that is a domain-size issue, addressed by
experiment 1. D3 remains `NOT VALIDATED` until both are reconciled.

**Gate 2 remains `NOT_TESTED`.**

## 6. Artifacts

- `cpd_vortex_gate_derivation_2026-11-22.py`
- `pks_research_index/quantum_vortex_gate_derivation.json`
