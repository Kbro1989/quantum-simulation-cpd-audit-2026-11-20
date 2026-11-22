# D3 remediation candidate — NOT VALIDATED

**Date:** 2026-11-22
**Script:** `cpd_vortex_d3_remediation_2026-11-22.py`
**Measurements:** `pks_research_index/quantum_vortex_d3_remediation.json`
**Baseline (immutable):** Gate 1, commit `b7b3391`.

Remediation **candidate**. It does not pass and is not promoted.

---

## 1. Estimators and pre-declared acceptance

| id | estimator |
|---|---|
| A | `baseline_centroid` — the Gate 1 estimator, kept for comparison |
| B | `disc_intersection` — intersect the ±1 discs from two loop radii |
| C | `boundary_bisection` — bisect the winding +1 → 0 boundary along ±x, ±y |

Criteria fixed **before** running: bounded error ≤ 1.0; err(N=64) ≤ 1.2·err(N=48);
|B − C| ≤ 0.5; competing minima == 1; blind displaced profiles within 0.5.

## 2. Verdict

| criterion | result |
|---|---|
| bounded error ≤ 1.0 | **FAIL** — A 2.71–3.36; B 33/33 empty; C 1.07–2.78 |
| refinement not worse | **FAIL** — B no data; C worse at N=64 (1.58 vs 1.07) |
| B/C agreement | **FAIL** — no frame where both answer |
| unambiguous | **PASS** — competing minima = 1 in every frame of every run |
| blind displaced profiles | **FAIL** — B returns nothing on all three |

Estimator B is **empty in all 33 frames of all six runs**. Estimator C answers in
12–21 of 33 frames with error 1.07–2.78 — better than A, but not converging.

An earlier revision of B that kept only discs near the **median** hit covered 6–21 of
33 frames; removing that heuristic dropped coverage to 0. Both fail.

## 3. Why B fails — and the N=64 question

A separate line of enquiry asked whether N=64 is special (an 8x8 floor plane). It is
not: **N=64 is 64 points per axis** — a 64x64 transverse plane, 64^3 = 262,144 points.
An 8x8 plane would be **N=8**. `8x8 = 64` is a count coincidence, not a structure.

But the question exposed the mechanism. The ±1 hit set is **not a clean disc**:

| step | N=48 hits (R=2 + R=3) | N=64 hits |
|---|---|---|
| 0 | 41 | 44 |
| 60 | 86 | 100 |
| 120 | 91 | 65 |
| 200 | 176 | 186 |

The hit region grows ~4x and spreads, so discs from the two radii have **no common
point** — the intersection is empty. Some ±1 hits are loops that wind without
containing the vortex: the phase field carries structure beyond one coherent core.
So the fault is not the median heuristic; it is the premise that the ±1 region is a
single disc.

## 4. Reference qualification

The density minimum is used as an independent **observable** (density, not phase) and
was stable: (0,0) for the centred vortex, and it tracked all three displaced profiles
exactly. It is **not** ground truth — it is exposed to density noise, grid anisotropy
and core structure, and is confined to a declared central region (r ≤ 3). Prominence
vs its annulus, competing-minimum count and separation, region-size sensitivity, and
grid-index vs physical coordinates are recorded per frame. The region is defined from
the grid, never from a detector's candidate coordinates.

## 5. Disposition

- **D2** topology detection works under the tested conditions.
- **D3** spatial localization fails: the baseline fails on convergence, both
  replacements fail on coverage.
- **D3 remediation is not validated.** Candidates recorded, not promoted.
- **Gate 2** (GPE stationarity) remains `NOT_TESTED`. Not started.

## 6. Next steps (not taken)

- Use the **density local minimum as the primary localizer** (stable here) with
  winding as topological confirmation, rather than deriving position from winding.
- Report coverage and hit-count explicitly so an ambiguous frame is visible.
- Diagnose the late-time growth of the ±1 hit set: genuine phase structure (extra
  defects) or sampling aliasing? The detector surfaced a physics question that should
  not be buried.
