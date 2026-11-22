# quantum-simulation CPD audit

**Forensic audit workspace for the QuantumLab / quantum-simulation stack.**
Created 2026-11-20 · first published commit `6734d5a` (2026-11-22) · maintained by Kbro1989.

This repository is **not** the simulation. It is the independent record that asks
whether the simulation's outputs are mathematically and physically defensible, and
whether each claim can be traced to a source. The production library lives at
`C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main`; the upstream
project is `rasidi3112/quantum-simulation`.

---

## 1. How to read this repository

Every claim here carries one of four labels. A file without a label is not evidence.

| label | meaning |
|---|---|
| **VERIFIED** | reproduced from an executed probe or a read-only source examination in this workspace |
| **REPORTED** | taken from an earlier audit, commit message or conversation; not independently reproduced here |
| **INFERRED** | derived from verified material, with the derivation shown |
| **PENDING** | a scaffold or plan; **not** a result |

**Implemented ≠ tested ≠ accepted.** A script that runs is not a validated result.
A probe that passes is not a certified instrument. Nothing in this repository is
certified; the production library is explicitly *not yet certified*
(`cpd_final_audit.md` §6).

---

## 2. Layout

| path | role |
|---|---|
| `cpd_producer_inventory.md` | 234 producers — everything that creates scientifically meaningful information |
| `cpd_consumer_inventory.md` | 72 consumers — everything that reads or transforms producer output |
| `cpd_detached_inventory.md` | 8 detached modules (test-seeded reachability, not a name scan) |
| `cpd_relationship_graph.json` | 286 nodes · 1030 call edges · 323 import edges |
| `cpd_physics_validation_matrix.md` | 12 physics domains |
| `cpd_mathematical_validation_report.md` | mathematical synthesis |
| `cpd_defect_register.json` | 17 defects |
| `cpd_remediation_plan.md` | authorization-gated remediation |
| `cpd_final_audit.md` | the 2026-11-20 audit verdict |
| `cpd_rasidi_kingwen_lineage_2026-11-22.md` | consolidated Git authorship and lineage |
| `cpd_vortex_provenance_2026-11-22.md` | the two meanings of "vortex" |
| `cpd_schauberger_research_atlas_2026-11-22.md` | Schauberger/egg-geometry research seed |
| `evidence/`, `probes/` | probe sources and execution records |
| `nvidia_validation/` | CUDA residency, FFT, precision/zero-floor, memory, power, architecture |
| `quantum_3d_asset_suite/` | generated 3D assets (PLY/OBJ/PNG/GIF) from real physics |
| `pks_research_index/` | PKS historical + mathematical evidence (Wayback, equation audit) |
| `schauberger_sources_2026-11-22/` | retrieved source documents |

---

## 3. Current status (2026-11-22)

### 3.1 Production library

**Not yet certified.** 11 of 12 physics domains independently validated; the
remainder is concentrated in the legacy time-dependent-potential bridge, vortex
grid alignment, and documentation claims that contradict measured runtime
behaviour. Full detail: `cpd_final_audit.md`.

### 3.2 Vortex diagnostics — detector v3

The vortex-line animation is a **visualisation, not a topological verification**.
Detector v3 (`pks_research_index/quantum_vortex_detector_v3.json`,
`cpd_vortex_detector_v3_2026-11-22.py`) separates what the simulation demonstrates
from what it does not:

| diagnostic | result | label |
|---|---|---|
| D1 core depletion | axis density 0.063494 vs annulus 0.009062 — the imposed state has **no depleted core** | **FAIL_INITIAL_CONDITION** |
| D2 phase winding | +1 at radii 2/3/4/5, z = −2/0/+2, every step (two wall-contaminated readings at r=5) | **PASS_WITH_BOUNDARY_CAVEAT** |
| D3 blind localisation | exact at t=0 (error 0.0000); drifts 1.11–2.65 by step 40 | **INITIAL_CONDITION_VALIDATED_ONLY** |
| D4 circulation | Γ = h/m wherever winding is 1 | **PASS_WITH_INDEPENDENCE_CAVEAT** |
| full vortex-line evolution | — | **NOT_CERTIFIED** |

Two implementation defects were found and fixed along the way: the grid convention
(`dx = (hi−lo)/N`, so the origin is a node only for **even** N) and the localisation
method (a winding hit-list is a disc; the core is its centroid). The earlier
corner-minimum detector and its spurious windings are **superseded** — see
`pks_research_index/pks_vortex_detector_v3_2026-11-22.md`.

### 3.3 PKS egg-curve mathematics

Recovered from the rendered PDF (byte-identical across the 2020/2024/2026 captures,
SHA-256 `ec4358df…`). Status of the equation audit:

| equation | status |
|---|---|
| EQ-03 | `ALGEBRAICALLY_VERIFIED` |
| EQ-07, EQ-08 | `ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS` |
| EQ-09 | `SIGN_CONVENTION_UNRESOLVED` (needs the page-8 diagram) |
| EQ-05 | `CLOSURE_PROVEN` |
| EQ-10 | `DISCREPANCY_PRESERVED` |

EQ-05 closure is analytic: both parameter-domain endpoints coincide at
`(0, 1.6018862051)`, the removable singularities at `cos φ = 0` give `r → 1/z₀ = 7/6`,
and the radicand is non-negative over the full domain.

EQ-10's three values are retained, not reconciled: printed equation **5.986907**,
closed-curve integral **7.736654**, source-stated **0.4045**. The page-8 diagram is
the next gate.

---

## 4. Provenance rules

- The published commit `6734d5a` is an **immutable baseline**. Later work is a
  follow-up commit; the baseline is never amended.
- Historical evidence is preserved, not overwritten. Superseded measurements stay
  on disk and are marked superseded.
- Missing measurements are recorded as missing. `cpd_independent_physics_validation.md`
  is a **PENDING** scaffold and must not be read as a completed validation.
- `.gitignore` excludes Python bytecode and caches. Four `__pycache__/*.pyc` files
  remain tracked from the baseline commit; removing them requires a commit.
- `cpd_certification_manifest.json` (v1.0, 72 files) is stale against the current
  tree. It is preserved unchanged; the current inventory is
  `cpd_certification_manifest_v2.json` (359 files). A manifest is a file listing,
  not a certification.
- No claim in this repository exceeds what an executed probe or a read-only source
  examination supports.

---

## 5. Related repositories

| repository | role |
|---|---|
| `Kbro1989/quantum-simulation` | production fork (QuantumLab) |
| `rasidi3112/quantum-simulation` | upstream; original 1D foundation and later physics expansion |
| `Kbro1989/archive-org-api-knowledge-base` | archival retrieval methodology (separate reference) |
