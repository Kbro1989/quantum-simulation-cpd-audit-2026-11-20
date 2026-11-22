# "Vortex" — term provenance and drift classification

**Recorded:** 2026-11-22
**Scope:** the word `vortex` as it exists in `quantum-simulation-main` and in this
audit workspace. This is a provenance record, not a defect claim: nothing here says
the quantum usage is wrong. It says the term denotes a different object than the
one that introduced it.

---

## 1. The two referents

### Referent A — the introducing usage (Kbro1989, intended, omitted from the PR)

Viktor Schauberger's natural fluid flow: the observation of fish holding station
in moving stream water, read as a self-organising centripetal vortex — the
"vortex and the egg" geometry. Implosion rather than explosion; a flow form, not
a topological defect.

### Referent B — the usage that was merged and now exists in the repository

A quantum-mechanical topological defect: the phase winding of a condensate order
parameter. The repository defines it operationally and only this way:

> `README.md:55` — "**Vortex detection** (`vortex_positions`), from the phase
> winding around every grid cell."

Everything downstream of that line inherits Referent B: `examples/11_rotating_bec_vortex_lattice.py`,
`examples/13_two_component_bec.py`, `observables/current.py::vortex_positions`,
and the audit's own `probe_09_vortex`, `validation_artifacts_ext/domain16_*`,
`nvidia_validation/domain27_zero_floor/vortex_core_density_floor`.

## 2. Evidence that Referent A is absent from the record

Recursive content scan (case-insensitive) for `schauberger|viktor|implosion|
centripetal|centrifugal|egg|hold-station|fish` across both trees:

| root | hits |
|---|---|
| `quantum-simulation-main/quantum-simulation-main` | **0** (only `*.egg-info` packaging paths — false positives) |
| `quantum-simulation-cpd-audit-2026-11-20` | **0** |

The omission is therefore total: the introducing framing was not written into the
PR, and nothing since has reintroduced it. Referent B is the only recorded meaning.

## 3. Drift classification

Applying the standing method — original mechanism → obfuscation → drift:

| stage | state |
|---|---|
| Original mechanism | Schauberger natural vortex: centripetal flow form, egg geometry, fish holding station |
| Omission | the framing was left out of the contribution PR |
| Adopted referent | quantum phase-winding topological defect — an acceptable, self-consistent reading of the bare word |
| **Drift** | the term now denotes a different object. The geometry (egg/implosion/centripetal) is absent from the pipeline; the detector measures winding number, not flow form |

**Consequence for the audit:** every vortex-related finding — `CPD-V1` (node-placed
core reads zero winding), `CPD-V2` (default `min_density` masks genuine cores),
`probe_09`, `domain9`, `domain16`, `domain27` — is a correct statement about
**Referent B** and is silent on **Referent A**. No probe in the chain tests the
Schauberger mechanism, because no artifact in the chain encodes it.

## 4. Where Referent A does survive

The introducing mechanism is not lost from the sovereign stack; it is absent only
from this program. Schauberger vortex physics is encoded elsewhere — the
centripetal/centrifugal vortex metric layer and the implosion-engine work. The
drift is local to `quantum-simulation`, not stack-wide.

## 5. What would close the gap

Not a rename — Referent B is legitimate physics and should keep its name. What is
missing is a *second, distinct* representation:

1. a geometric model of the Referent-A flow form (centripetal, egg-profile) as a
   field on the same grid, so both referents can be computed side by side;
2. a probe that measures the Referent-A invariants, so the audit can state
   something about it rather than remaining silent;
3. a one-line provenance note wherever `vortex_positions` is documented, recording
   that the term was introduced under Referent A and is implemented as Referent B.

Until (1) exists, any vortex finding in this audit must be read as Referent B
only. This note is that reading.

## 6. Detector v3 — measured status (2026-11-22)

The vortex-line animation is a **visualisation of Referent B**, not a verification of
it. Detector v3 (`pks_research_index/quantum_vortex_detector_v3.json`,
`cpd_vortex_detector_v3_2026-11-22.py`) measured the imposed state
ψ = A·e^(−r²/4σ²)·e^(i·atan2(y,x)):

| diagnostic | measurement | label |
|---|---|---|
| D1 core depletion | axis ρ = 0.063494 vs annulus ρ = 0.009062 — the axis is a density **maximum** | **FAIL_INITIAL_CONDITION** |
| D2 phase winding | +1 at radii 2/3/4/5, z = −2/0/+2, every step (two wall-contaminated readings at r=5) | **PASS_WITH_BOUNDARY_CAVEAT** |
| D3 blind localisation | exact at t=0 (error 0.0000); drift 1.11–2.65 by step 40 | **INITIAL_CONDITION_VALIDATED_ONLY** |
| D4 circulation | Γ = h/m wherever winding is 1 | **PASS_WITH_INDEPENDENCE_CAVEAT** |

Two implementation defects were found and fixed: the grid convention
(`dx = (hi−lo)/N`, so the origin is a node only for **even** N — N=49 places it at
−0.122449) and the localisation method (a winding hit-list is a **disc**; the core is
its centroid). The earlier corner-minimum detector and its spurious windings are
**superseded**.

**Full vortex-line evolution: NOT_CERTIFIED.** D1 fails for the supplied initial
condition, and D4 is computed from the same phase increments as D2, so it is not an
independent check. The next physics gates are a regularised initial state
(ψ ∝ r·e^(−r²/4σ²)·e^(iθ), so the amplitude vanishes on the axis) and an independent
velocity-field circulation integral.

### 6.1 Regularized state — both gates closed (2026-11-22)

`cpd_vortex_regularized_2026-11-22.py` repeats the measurement with
ψ = A·r⊥·exp(−(r⊥²+z²)/4σ²)·exp(iθ), which vanishes linearly on the axis.

| diagnostic | gaussian | regularized |
|---|---|---|
| D1 core depletion | FAIL (axis ρ 0.063494 > annulus 0.009062) | **PASS** (axis ρ = 0.000000) |
| D2 winding | PASS with caveat | **PASS** (+1.000, r = 2/3/4, N=48 and N=64) |
| D3 localisation | exact at t=0 only | exact at t = 0–20 (N=48); drifts to 1.20–1.77 by step 40 |
| D4 circulation | restated D2 | **independent velocity-field route**, Γ/(h/m) = 0.99–1.02 |

The circulation is now computed from **v = (ℏ/m)·Im(∇ψ/ψ)** integrated around the
loop — a gradient of the complex field, not a phase-difference sum — so D4 no longer
restates D2. The residual is discretization error: ~1% at N=48, ~0.5% at N=64.

D3 remains the open item. Full evolution stays `NOT_CERTIFIED`.
Artifact: `pks_research_index/pks_vortex_regularized_2026-11-22.md`.

### 6.2 Gate 1 — D3 convergence: FAILS

`cpd_vortex_gate1_d3_convergence_2026-11-22.py` — separate gate, N ∈ {48,64} ×
dt ∈ {0.005, 0.0025}, steps 0–200, three z-slices, reference = central local density
minimum (no phase).

The reference stays at **(0,0) for every frame of every run** — the vortex is
stationary. The winding-centroid detector drifts to 1.2–2.6 grid units, is **worse**
at N=64 than N=48, is insensitive to halving dt, and `competing_minima = 1`
throughout. Diagnosis: **detector bias**, not physical motion and not instability.
Winding around the detected core remains +1 at r = 3, 4.

The first reference implementation (global density minimum) failed the same way as
the old corner detector — the Gaussian tail beats the core — and was corrected to a
local minimum inside a declared region.

Artifact: `pks_research_index/quantum_vortex_gate1_d3.json`,
`pks_research_index/pks_vortex_gate1_d3_2026-11-22.md`.

### 6.3 D3 remediation candidate — NOT VALIDATED

`cpd_vortex_d3_remediation_2026-11-22.py` — three estimators (baseline centroid,
disc intersection, boundary bisection) against an independent density reference, on
N ∈ {48, 64, 96} × dt ∈ {0.005, 0.0025}, with pre-declared acceptance criteria.

| criterion | result |
|---|---|
| bounded error ≤ 1.0 | **FAIL** |
| refinement not worse | **FAIL** |
| the two new estimators agree | **FAIL** — no frame where both answer |
| unambiguous | **PASS** — competing minima = 1 |
| blind displaced profiles | **FAIL** — disc intersection empty on all three |

The disc-intersection estimator is empty in all 33 frames of all six runs. A check on
whether N=64 is special (an 8x8 floor plane) found it is **not** — N=64 is 64 points
per axis; an 8x8 plane would be N=8 — but it exposed the mechanism: the ±1 hit set
grows from ~41 points to ~180 and spreads, so the two radii's discs share no common
point. The estimator's premise (the ±1 region is one disc) is what fails.

The reference qualification is preserved: the density minimum is an independent
observable, not ground truth — exposed to density noise, grid anisotropy and core
structure, and confined to a declared central region.

Artifact: `pks_research_index/quantum_vortex_d3_remediation.json`,
`pks_research_index/pks_vortex_d3_remediation_2026-11-22.md`.

### 6.4 Revision 2 — geometry corrected, still NOT VALIDATED

Revision 1's bilinear sampler **clamped out-of-domain loop samples to the grid edge**,
which can manufacture winding; every revision-1 estimate was contaminated. Revision 2
rejects any loop not wholly inside the domain and records valid vs rejected counts.

| estimator | rev 1 max err | rev 2 max err |
|---|---|---|
| baseline centroid (control) | 2.71–3.36 | 0.49–1.48 |
| disc intersection | empty / 0.13 | 0.0994–0.1326 (coverage 9–33/33) |
| boundary bisection | 1.07–2.78 | **0.2433–0.7415, 33/33** |

The revision-1 hit-set growth was **boundary contamination, not phase structure**;
rejected counts are now constant (80 at R=2, 188 at R=3).

Acceptance (separable evaluator, N=96 included, control excluded): bounded **FAIL**,
refinement **FAIL**, agreement **PASS**, unambiguous **PASS**, blind **FAIL**.
**D3 remains `NOT VALIDATED`.**

Artifact: `pks_research_index/quantum_vortex_d3_remediation_v2.json`,
`cpd_vortex_d3_acceptance_2026-11-22.py`.

### 6.5 Revision 3 — diagnostics, root cause of the blind failures

`cpd_vortex_d3_remediation_v3_2026-11-22.py`. The `domain_exit` → `no_bracket`
overwrite is fixed; every direction keeps its real termination reason, last valid
radius and last observed winding, and all four crossings are stored.

Across 56 direction attempts (7 profiles × 2 seeds × 4 directions):

| reason | count |
|---|---|
| `ok` | 47 |
| **`domain_exit`** | **9** |
| `no_opposite_winding` | 0 |
| `refinement_failed` | 0 |
| `start_not_interior` | 0 |

Both seeds — hit-set centroid and verified-interior-hit — fail **identically**, so the
cause is not the seed. The angular scan shows the failed angles point exactly at the
nearest domain edge. **Cause: the valid-domain boundary** — the outward walk uses a
loop of radius 2.0 in a domain only 11.75 wide (`[-6, 5.75]`).

**Silent-bias hazard:** when the centroid seed is off-centre and all four directions
still return `ok`, the crossing mean is biased (errors 0.88–0.95) rather than failing.
The four-crossing mean is unbiased only when the seed is the core.

**Blind-profile discipline:** the original three displacements are now a comparison
baseline only; four fresh displacements are reserved for independent validation. Both
sets **FAIL**. Disc-intersection is qualified as an adaptively refined numerical
feasibility approximation, not an exact method.

**D3 remains `NOT VALIDATED`.** Gate 2 remains `NOT_TESTED`.

Artifact: `pks_research_index/quantum_vortex_d3_remediation_v3.json`,
`pks_research_index/pks_vortex_d3_remediation_v3_2026-11-22.md`.

### 6.6 Revision 4 — circle fitting, hypothesis confirmed, still NOT VALIDATED

Every valid crossing lies on the circle of radius R centred on the vortex, so the
centre can be fitted without assuming the four-crossing mean is unbiased.

**Hypothesis confirmed:** the four-crossing control returned `None` in nearly every
case (fewer than four cardinal crossings survive the domain) while the fit answered.
At N=64 the centred case fits to **0.0002** with `R_fit = 2.0000`.

Acceptance: C1 bounded **PASS**, C2 refinement **PASS**, C3 radius gate **PASS**,
C5 reserved blind holdout **FAIL** (14 pass / 4 gated-out / 2 ungated), C6 sector-drop
sensitivity **FAIL**. The estimator SHA-256 is identical across development and
holdout runs — frozen before evaluation.

**Operating envelope** — accuracy is governed by angular coverage:

| coverage | max error |
|---|---|
| 0.5 | 1.81 |
| 0.6 | 1.07 |
| 0.7–0.8 | 0.42–0.55 |
| 0.9–1.0 | 0.00–0.09 |

Coverage is limited by the valid-domain boundary (revision 3's finding), so this is a
domain-size constraint on the estimator, recorded as an operating constraint and not
claimed as general localization. The ±0.35 radius gate misses some degraded fits;
tightening it would be tuning against the holdout, so it is reported instead.

**D3 remains `NOT VALIDATED`. Gate 2 remains `NOT_TESTED`.**

Artifacts: `pks_research_index/quantum_vortex_d3_remediation_v4.json`,
`pks_research_index/quantum_vortex_d3_remediation_v4_holdout.json`,
`cpd_vortex_d3_acceptance_v4_2026-11-22.py`.
