# D3 remediation revision 3 — diagnostics and the directional assumption

**Date:** 2026-11-22
**Script:** `cpd_vortex_d3_remediation_v3_2026-11-22.py`
**Evaluator:** `cpd_vortex_d3_acceptance_2026-11-22.py` (accepts the JSON path as argv[1])
**Measurements:** `pks_research_index/quantum_vortex_d3_remediation_v3.json`
**Preserved immutable:** `b7b3391`, `895bec2`, `d259430` (revision 2).

Revision 3 is **diagnostic**. D3 remains `NOT VALIDATED`.

---

## 1. Priority 1 — bisection failure diagnostics

The `domain_exit` → `no_bracket` overwrite is fixed. Every direction now keeps its real
termination reason, together with the last valid radius and last observed winding, and
all four crossing coordinates are stored.

Result across 7 profiles × 2 seeds × 4 directions = 56 direction attempts:

| termination reason | count |
|---|---|
| `ok` | 47 |
| **`domain_exit`** | **9** |
| `no_opposite_winding` | 0 |
| `refinement_failed` | 0 |
| `start_not_interior` | 0 |

**`domain_exit` is the only failure mode.** No direction ever failed to find an
opposite-classification loop, and no refinement ever failed to converge.

## 2. Priority 2 — is it the seed, the cardinal assumption, or the domain?

Both seeds were tested: the hit-set **centroid** and a **verified-interior-hit**.

| profile | centroid seed | verified-hit seed |
|---|---|---|
| (-2.0, 1.5) | `xn` domain_exit | `xn` domain_exit |
| (0.0, 2.5) | `yp` domain_exit | `yp` domain_exit |
| (2.25, 0.75) | `xp` domain_exit | `xp` domain_exit |
| (-1.25, -2.25) | `yn` domain_exit | `yn` domain_exit |
| (0.75, -2.75) | `yn` domain_exit | `yn` domain_exit |
| (-2.75, -0.75) | `xn` domain_exit | `xn` domain_exit |

**Identical failures for both seeds** — the cause is neither the centroid seed nor the
cardinal directions as such.

The **angular scan** settles it: the failed angles are exactly those pointing at the
nearest domain edge.

| profile | failed angles | pointing |
|---|---|---|
| (0.0, 2.5) | 50–130° | +y, toward y = 5.75 |
| (2.25, 0.75) | 0–40°, 320–350° | +x, toward x = 5.75 |
| (-1.25, -2.25) | 240–300° | −y, toward y = −6 |
| (-2.75, -0.75) | 100–260° | −x, toward x = −6 |

**Cause: the valid-domain boundary.** The outward walk uses a loop of radius 2.0 in a
domain only 11.75 wide (`x ∈ [-6, 5.75]`, asymmetric), so for any vortex more than
about 2 units from the centre the walk reaches the domain edge before it reaches the
edge of the ±1 disc.

## 3. A hazard found on the way

When the centroid seed is **off-centre** and all four directions still return `ok`,
the four crossings are at different radii and their mean is **biased** — a silent
wrong answer, not a failure:

| profile | centroid-seed error |
|---|---|
| (1.5, -1.0) | 0.0000 |
| (-2.0, 1.5) | 0.9014 |
| (-1.25, -2.25) | 0.9520 |
| (0.75, -2.75) | 0.8839 |

The four-crossing mean is only unbiased when the seed **is** the core. That is a
structural limitation of the estimator, independent of the domain problem.

## 4. Blind-profile discipline

The original three displacements were inspected during development, so they are no
longer independent. They are retained as a **comparison baseline only**. Four **fresh**
displacements — (2.25, 0.75), (-1.25, -2.25), (0.75, -2.75), (-2.75, -0.75) — are
reserved for independent validation and were not used to shape any estimator.

Both sets **FAIL**. Fresh-set independent validation: **FAIL**.

## 5. Priority 3 — acceptance

The evaluator now checks refinement in **both** directions (48→64 and 64→96) for both
timesteps and both replacement estimators, with N=96 inside the calculation:

| estimator | 48→64 | 64→96 |
|---|---|---|
| disc intersection | **F** (0.0994 → 0.1326) | P (0.1326 → 0.0994) |
| boundary bisection | P | **F** (0.2695 → 0.7415; 0.0001 → 0.2433) |

Neither estimator refines monotonically, so C2 fails for both.

**Qualification:** the disc-intersection result is an **adaptively refined numerical
feasibility approximation** (coarse-to-fine max-min slack), not an exact continuous
feasibility method. It is not claimed as exact.

## 6. Disposition

- **D2** topology detection works.
- **D3** spatial localization: root cause of the revision-2 blind failures identified
  (valid-domain boundary, not the seed, not the cardinal assumption) and a silent
  bias hazard documented. **Still `NOT VALIDATED`.**
- **Gate 2** remains `NOT_TESTED`.

## 7. Next — diagnostic-supported, not yet an estimator

The crossings all lie on a circle of radius ≈ r centred on the vortex, so the centre
can be **fitted** from many crossings rather than averaged from four. The angular scan
already produces that data. Any such change must be validated on the **fresh** profiles
and must report `domain_exit` coverage explicitly rather than returning `None`.
