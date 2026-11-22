# CUSTOM-INSTRUCTIONS.md

**Version: 2.1**
**Restored and reconceptualized 2026-11-21**
**Status: RECONSTRUCTED — provisional working specification**

---

## 1. Purpose

This document restores the permanent engineering specification for the
quantum-simulation project after context compression lost the original
`CUSTOM-INSTRUCTIONS.md`. The original document and its exact wording have NOT
been recovered. The historical export `Pasted text(20261116-223357).txt`
(848 KB) is the authoritative source for recovered requirements; this file is
the consolidated operating contract for the forensic audit workspace.

---

## 2. Provenance Model — Version 2.1

This document is distributed into THREE explicit provenance categories:

### 2.1 Recovered (requirements supported by historical conversation evidence)

Requirements that trace to the historical conversation archive
(`Pasted text(20261116-223357).txt`, 848 KB), recovered fully from conversation
history:

| Principle | Recovered status |
|---|---|
| Evidence integrity over claims and summaries | Explicitly recovered |
| No mocks, stubs, synthetic measurements, or placeholders | Explicitly recovered |
| API preservation — maintain backward compatibility | Explicitly recovered |
| Numerical integrity — validate mathematical and physical invariants | Explicitly recovered |
| Provenance — trace every result to source, execution, parameters, and hashes | Explicitly recovered |
| Independent validation — do not use the implementation under test as its own oracle | Explicitly recovered |
| Failure handling — fail explicitly; no silent fallback or fabricated success | Explicitly recovered |
| Baseline preservation — never silently modify frozen historical evidence | Explicitly recovered |
| Scope control — separate implemented, tested, validated, and certified | Explicitly recovered |
| Authorization — do not expand certification scope without approval | Explicitly recovered |
| Remediation — make minimal, targeted, evidence-backed changes | Explicitly recovered |
| Continuity — preserve discoveries, decisions, outstanding defects, and recovery state | Explicitly recovered |

### 2.2 Reconstructed (requirements synthesized from the recovered engineering doctrine)

Consolidated scientific, numerical, architectural, and repository-specific
requirements derived from the recovered doctrine and engineering context:

- Split-step Fourier numerical correctness
- Hermiticity and energy/momentum conservation
- Spatial and temporal convergence
- Absorbing boundary validation
- Vortex topology
- GPU memory residency and backend identity
- NumPy/CuPy compatibility
- Float32 versus float64 numerical behavior
- Statistical benchmarking
- Domain 27 zero-floor classification
- Time-dependent potential evaluation at actual solver substeps

### 2.3 Newly authorized (requirements added after the reconstruction)

Requirements added by this session's engineering work that are not historically
attributable. The following engineering fixes were newly authorized and executed:

- **Legacy solver time-dependent API fix:** `split_step_1d.py`, `split_step_2d.py`,
  `split_step_3d.py`, `split_step_3d_gpu.py` now call `potential.evaluate_at`
  at each substep instead of caching `V` at `t=0`
- **Backend identity API:** added `solver.backend_name` and
  `solver.array_backend` to `SplitOperatorSolver`
- **GPU residency:** verified `evolve()` keeps wavefunction on device between
  steps; `step()` transfers host↔device per call

**

### 2.4 Recovery status

| Material | Recovery status |
|---|---|
| Original pre-v2.0 instructions | Not recovered verbatim |
| Original 12 governing principles | Substantively reconstructed |
| Production CUSTOM-INSTRUCTIONS.md | User-reported v2.1 |
| Audit CUSTOM-INSTRUCTIONS.md | User-reported v2.1 |
| Scientific computing requirements | Substantially recovered |
| Domain 27 engineering doctrine | Recovered through conversation history |
| Legacy time-dependent solver requirements | Recovered from subsequent engineering work |
| Exact original wording and ordering | Unresolved |

**Key rule for this file:** Until the original source is located, this file
identifies itself as a reconstruction, NOT a verbatim restoration. The four
provenance categories (Recovered / Reconstructed / Newly Authorized) distinguish
between original, recovered, reconstructed, and newly authorized material.

---

## 3. Governing Principles (Mandatory)

The following principles are mandatory in the reconstructed specification.
These are the 12 core governing principles recovered from historical
conversation records:

1. **Evidence over assertion.** Every engineering claim needs supporting
   evidence. No claim about source behavior, test results, file contents, or
   numerical measurements is made without a corresponding real artifact on disk.

2. **No mocks, stubs, or placeholders.** No fabricated implementation,
   measurements, or outputs presented as real. Zero tolerance for
   placeholders or synthetic data.

3. **No fabricated completion.** Distinguish explicitly: source implementation,
   unit-test success, measured behavior, independently verified result,
   deployed artifact. A test result does NOT establish the completeness of a
   feature.

4. **Preserve API contracts.** Maintain backward compatibility. Do not break
   existing consumers without documented transition.

5. **Numerical integrity.** Validate mathematical and physical invariants.
   Preserve precision, physical meaning, boundary conditions, and
   mathematical correctness.

6. **Provenance preservation.** Maintain source hashes, timestamps, inputs,
   outputs, and execution records. Never overwrite frozen baselines with
   remediation results.

7. **Independent validation.** Do not test an implementation solely against its
   own assumptions. Use independent references.

8. **Explicit failure.** No silent fallback or substitution. When a measurement
   could not run, or a threshold excluded a result, that state must be visible
   and labeled NOT_RUN, null, or equivalent.

9. **Certification gates.** Failed mandatory dimensions cannot be overridden by
   aggregate scores. Certification requires: (a) implementation present,
   (b) test suite passing, (c) measurements recorded, (d) independent
   verification, (e) deployment if applicable.

10. **Frozen baselines.** Preserve historical evidence. Do not overwrite
   frozen baselines with remediation results.

11. **Minimal authorized remediation.** Make minimal, targeted fixes. Do not
   expand scope without authorization.

12. **Residual uncertainty.** Explicitly document what remains unverified.

---

## 4. Additional Recovered Engineering Requirements

These are particularly important to Quantum-simulation and must be part of the
specification:

- NumPy/CuPy backend consistency.
- GPU residency and transfer accounting.
- backend, backend_name, and array_backend identity.
- Static versus time-dependent potential evaluation.
- Correct evaluation of V(x,t) at solver substeps.
- Split-step Fourier numerical accuracy.
- Hermiticity and conservation-law validation.
- Float32 versus float64 behavior.
- Numerical convergence and independent reference implementations.
- Vortex topology and boundary-condition validation.
- Domain 27 zero-floor classification.
- Fail-closed evidence generation (refuse on error, missing observations,
  NaN/Inf, missing provenance, inconsistent IDs, empty observations).
- JSON-to-PNG/GIF numerical traceability.

---

## 5. Legacy solver time-dependent potential corrections

The four legacy solvers and their time-dependent potential corrections must
remain part of the historical engineering record:

- quantumlab/solvers/split_step_1d.py -- fixed 2026-11-21 to call
  potential.evaluate_at at each substep instead of caching V at t=0
- quantumlab/solvers/split_step_2d.py -- fixed 2026-11-21 (same pattern)
- quantumlab/solvers/split_step_3d.py -- fixed 2026-11-21 (same pattern)
- quantumlab/solvers/split_step_3d_gpu.py -- fixed 2026-11-21 (CuPy type-safe)

---

The two authoritative working documents are:

1. quantum-simulation-main/CUSTOM-INSTRUCTIONS.md -- production engineering
   specification (currently reported as v2.1).
2. quantum-simulation-cpd-audit-2026-11-20/CUSTOM-INSTRUCTIONS.md -- forensic
   audit specification (currently reported as v2.1).

Both contain the three provenance categories: Recovered, Reconstructed,
Newly authorized. That distinction must not be discarded.
Either category can be promoted to a third-party advisory doc or a decision
record, but not to "original custom-instruction text."**

---

## 3. Repository Boundaries

There are two distinct repositories/workspaces. They must not be conflated.

| Workspace | Role |
|---|---|
| `quantum-simulation-main` | Production library: `quantumlab`, solvers, observables, potentials, visualization, examples |
| `quantum-simulation-cpd-audit-2026-11-20` | Forensic audit: probes, NVIDIA validation, numerical evidence, remediation plan, final audit |

**Boundary rule:** Audit findings are the subject. Production code is the object.
Do not promote audit artifacts to production facts without source verification.

---

## 4. Three-authority model (2026-11-21)

This document is a **reconstruction** of the audit-workspace companion. Three
distinct authorities are preserved:

1. **Recovered Historical Instructions** — exact historical wording wherever
   available, with provenance. Historical conversation export:
   `Pasted text(20261116-223357).txt` (848 KB), recovered from the 2026-11-16
   conversation archive. Explicitly recovered principles — no mocks, no
   fabricated execution, evidence before implementation, preserve
   implementations, preserve immutable baselines, SHA-256 provenance, no
   silent fallbacks, independent numerical validation, preserve negative
   results, separate implementation from certification, no unauthorized
   production modifications, preserve historical failures.

2. **Quantum-Simulation Operating Contract** — this document. Consolidated
   scientific, numerical, architectural, and repository-specific requirements
   for the quantum-simulation project.

3. **Current Project State Ledger** — actual implementation status, execution
   evidence, defects, hashes, and authorization. The authoritative record of
   what is currently built, tested, verified, or blocked.

---

## 5. Evidence Management

### 5.1 Evidence-chain discipline

Every recorded finding must map to:

1. **Implementation** — the source file that produces the value.
2. **Measurement** — the raw output file (JSON, log, or script output).
3. **Artifact** — the visualization (PNG/GIF) that illustrates the result.

A finding is not "verified" until all three are present and cross-checkable.

### 5.2 Evidence index

`cpd_evidence_index.json` — the single source of evidence traceability.

### 5.3 Defect register

`cpd_defect_register.json` — structured records with file, line, observed
behavior, root cause, fix, and verification delta.

### 5.4 Related .md files as variable sources

The audit workspace documents its findings across several Markdown files.
Each file defines a set of variables that must be checked for validity when
recording or comparing findings.

| File | Role | Key variable names |
|---|---|---|
| `cpd_producer_inventory.md` | Producers of computational data — pipeline runs, model mappings | `producer`, `input`, `output`, `pipeline`, `model_mapping` |
| `cpd_consumer_inventory.md` | Consumers of computational data — consumers, targets, relationships | `consumer`, `target`, `input`, `output` |
| `cpd_relationship_graph.json` | Relationships between components (source → consumer → output) | `source`, `consumer`, `output`, `relationship_type` |
| `cpd_final_audit.md` | Consolidated audit findings | `domain`, `verdict`, `evidence_path`, `defect_found` |
| `cpd_mathematical_validation_report.md` | Mathematical validation results (12 domains) | `domain`, `verdict`, `residual`, `independent_check` |
| `cpd_physics_validation_matrix.md` | Physics correctness assessment (12 domains) | `domain`, `invariant`, `residual`, `verdict`, `probe_script` |
| `cpd_remediation_plan.md` | Remediation sequencing and gates | `defect_id`, `probe_script`, `fix`, `verdict`, `confirmation` |
| `cpd_detached_inventory.md` | Detached inventory (remote/provenance) | `remote_uri`, `local_path`, `model_ref`, `status` |

**Verification rule:** No finding may be recorded in `cpd_evidence_index.json` unless
all three columns are present and cross-checkable: implementation path, measured
output path, and artifact path. When editing these .md files, verify variable
names match their JSON definitions exactly.

---

## 6. Domain 27 — Zero-Floor Taxonomy (restored)

### 6.1 Classification classes

| Class | Meaning |
|---|---|
| `EXACT_ZERO` | Numerically represented exact zero |
| `SUBNORMAL` | Nonzero IEEE-754 subnormal |
| `NORMAL` | Representable normal floating-point value |
| `UNDERFLOW_ZERO` | Nonzero mathematical result rounded to zero |
| `GPU_FTZ_ZERO` | Subnormal flushed to zero by GPU execution |
| `CANCELLATION_ZERO` | Result lost through floating-point cancellation |
| `NAN` | Not-a-Number |
| `POS_INF` | Positive infinity |
| `NEG_INF` | Negative infinity |
| `NULL` | Missing or unavailable measurement (not numerical zero) |

### 6.2 Classification storage

The JSON payload stores:

- `dtype` — numpy dtype (e.g., `float32`, `float64`)
- `device` — `"cpu"` or `"cuda"`
- `precision` — the scalar precision value
- `classification` — one of the 10 classes above

### 6.3 Key finding

GPU float32 subnormals are flushed to zero because of CUDA flush-to-zero.
This differs from CPU behavior. The classification must record `device` and
`precision` separately, not rely on a single global label.

---

## 7. Forensic audit deliverables

| File | Purpose |
|---|---|
| `cpd_final_audit.md` | Consolidated audit findings |
| `cpd_defect_register.json` | Structured defect records |
| `cpd_producer_inventory.md` | Producers of computational data |
| `cpd_consumer_inventory.md` | Consumers of computational data |
| `cpd_relationship_graph.json` | Relationships between components |
| `cpd_evidence_index.json` | Evidence provenance and indexing |
| `cpd_mathematical_validation_report.md` | Mathematical validation |
| `cpd_physics_validation_matrix.md` | Physics correctness assessment |
| `cpd_remediation_plan.md` | Remediation sequencing and gates |
| `final_payload.json` | Consolidated machine-readable output |
| `final_schema.json` | Payload structure and contract |

---


## 8. Domain 27 — Physics Integration Evidence Contract

### 8.1 Required contract

1. Execute physics integration script.
2. Validate numerical JSON output.
3. Record SHA-256 hash.
4. Generate PNG/GIF exclusively from validated JSON observations.
5. Trace every plotted value to source JSON field.
6. Record generator and input hashes in provenance manifest.
7. Independently verify artifact counts, hashes, and numerical consistency.

### 8.2 Scope boundary

| Area | Scope |
|---|---|
| D27.2 | Scalar floating-point zero classification and CUDA comparisons |
| D27.3 | 1D/2D physics integration |
| 3D solver | Existing capability (separate workstream) |
| 3D Domain 27 integration | Current work (not certified) |
| 3D certification | Not established |

Classification being dimension-independent does not establish physics integration
is dimension-independent.

### 8.3 Verification status

The reported 13/13 artifact traceability in conversation is a historical claim,
not fresh independent verification. Independent verification still required.

---

## 9. Scientific Reference Hierarchy

| Source | Intended use |
|---|---|
| arXiv — https://arxiv.org/ | Research papers, numerical methods |
| Wolfram MathWorld — https://mathworld.wolfram.com/ | Mathematical identities |
| Wolfram Language Documentation — https://reference.wolfram.com/language/ | Computational definitions |
| NIST — https://www.nist.gov/ | Measurement science, constants |
| NIST DLMF — https://dlmf.nist.gov/ | Special functions |
| APS Journals — https://journals.aps.org/ | Peer-reviewed physics |
| NASA ADS — https://ui.adsabs.harvard.edu/ | Literature discovery |

---

## 10. Current Engineering Priorities

### Priority 1: Solver backend API

- Verify `solver.backend` remains a string.
- Verify `solver.backend_name` returns correct string.
- Verify `solver.array_backend` returns correct `ArrayBackend`.
- Verify `gpu=True` honored for `split_operator` with no explicit backend.
- Verify `gpu=True` respected for `split_step_3d` and `step()` with CuPy.
- Record `backend` selection logic in run log before and after fix.

### Priority 2: GPU residency

- `evolve()` keeps wavefunction on GPU between steps.
- `step()` transfers host↔device per call.
- `evolve()` does not transfer unless input on CPU side.
- Measure download bytes for `evolve()` and `step()` separately.

### Priority 3: Domain 27 classification

- Verify classification produces correct labels for representative samples
  (0.0, 1e-320, 5e-324, 5e-323, 2.2, inf, nan, 1e-45, 1e-44).
- Preserve `GPU_FTZ_ZERO` vs `EXACT_ZERO` distinction.
- JSON output includes `dtype`, `device`, `precision`.

### Priority 4: Consumer correctness

- Trace solver output into observables, energy, vortex, training data.
- Verify GPU results not misclassified as CPU.

### Priority 5: Certification

- Run `python -m pytest tests/`.
- Run `python -m pytest benchmarks/validation_suite.py`.
- Produce verification report.

---

## 11. Session Continuity Protocol

### 11.1 Session gate (every session start)

1. **Repository and working directory** — repo, path, branch.
2. **Current branch and commit** — `git branch --show-current`, `git rev-parse HEAD`.
3. **Uncommitted changes** — `git status --short`.
4. **Instruction-file version** — `CUSTOM-INSTRUCTIONS.md` hash.
5. **Implementation state** — tests passing, failing.
6. **Latest verified test results** — test counts from last successful run.
7. **Outstanding defects** — open tickets, blocked items.
8. **Frozen artifacts and hashes** — SHA-256 of frozen baselines.

### 11.2 Session close (every session end)

Factual change report:

1. What changed (file, line, behavior).
2. What was tested — suite, test count, passed/failed.
3. What failed — why; whose work is in progress.
4. What remains unverified — explicitly named.
5. New hashes of changed artifacts.

---

## 12. Relationships to the outside audit ecosystem

This audit workspace concerns the quantum-simulation project, which comprises:

- `quantum-simulation-main` — the production library (target for work)
- `quantum-simulation-cpd-audit-2026-11-20` — this forensic audit workspace

All work is confined to computational quantum science. Do not import runtime
modules, scripts, or artifacts from any other program into this workspace.

---

## 13. Recovery Position

This document is a **reconstructed** specification for the audit workspace.

| Item | Provenance |
|---|---|
| Evidence management | Reconstructed from D27.3 conversation |
| D27.3 contract | Reconstructed from conversation traceability |
| Scope boundary | Reconstructed from conversation |
| Reference hierarchy | Reconstructed from conversation references |
| Priorities | Reconstructed from engineering priorities list |
| Session continuity | Reconstructed from conversation requirements |
| Legacy solver fix (Section 7, §3.13) | Reconstructed from conversation |
| Existing content (1–2) | Derived from earlier restoration |

**Last updated: 2026-11-21**
**Reconstructed from: composer-paste evidence (2026-11-21)**

**Three-authority model (2026-11-21):** This document is a RECONSTRUCTION.
Three distinct authorities are preserved:

1. **Recovered Historical Instructions** — exact historical wording wherever
   available, with provenance. Historical conversation export:
   `Pasted text(20261116-223357).txt` (848 KB), recovered from the 2026-11-16
   conversation archive. Explicitly recovered principles — no mocks, no
   fabricated execution, evidence before implementation, preserve
   implementations, preserve immutable baselines, SHA-256 provenance, no
   silent fallbacks, independent numerical validation, preserve negative
   results, separate implementation from certification, no unauthorized
   production modifications, preserve historical failures.

2. **Quantum-Simulation Operating Contract** — this document. Consolidated
   scientific, numerical, architectural, and repository-specific requirements
   for the quantum-simulation project.

3. **Current Project State Ledger** — actual implementation status, execution
   evidence, defects, hashes, and authorization. The authoritative record of
   what is currently built, tested, verified, or blocked.

**Important:** This document is a RECONSTRUCTION. Do not represent it as a
verbatim copy of the original custom instructions. The original document and
its exact wording have NOT been recovered. The historical export
`Pasted text(20261116-223357).txt` is the authoritative source for recovered
historical requirements; this file is the consolidated operating contract.

**Original-version identity: UNRESOLVED.** This document cannot be verified as
the verbatim original. The provenance categories above (Recovered / Reconstructed
/ Newly Authorized) shall be used for future consistency. Do not claim this file
is the original.

