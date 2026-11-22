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
