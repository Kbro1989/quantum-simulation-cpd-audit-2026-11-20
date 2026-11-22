# quantumlab — Remediation Plan (CPD audit 2026-11-20)

**Status:** AUTHORIZATION-GATING PLAN. No production code has been modified.
**Input register:** `cpd_defect_register.json` (17 defects; 4 fixed, 13 open).
**Branch:** `remediation/2026-11-20` @ `44f30e3`; baseline `7cb98a7` untouched.
**Scope:** only the 13 open defects below. Historical evidence (`results.json`
`148d01cb…`, `validation_report.md` `1d0f3db8…`) is preserved and not touched by
any item in this plan.

---

## 0. Principle of execution

1. **Smallest defensible correction.** One defect, one scope, no bundling.
2. **Preserve existing behaviour.** Never change a working path to fix another.
3. **Regression tests for every confirmed defect.** No fix ships without a test.
4. **Independent mathematics for the new tests.** Analytic reference or a second
   implementation; never a test that merely re-implements the production function.
5. **Historical evidence untouched.** Reproducible artifacts live in the audit
   directory; nothing is written into the repo.

---

## 1. Defect inventory (open)

| ID | Severity | Class | Title | Owner |
|---|---|---|---|---|
| CPD-P0-1 | P0 | Producer | 1-D potential applied along the wrong axis on a 3-D grid | upstream |
| CPD-V1 | P0 | Producer | vortex winding zero on a node-placed core | upstream |
| CPD-P1-1 | P1 | Producer | legacy solvers freeze time-dependent potential at t=0 | mixed |
| CPD-CONF-1 | P1 | Detached | `quantumlab/config.py` dead and incompatible with `SimulationRunner` | upstream |
| CPD-V2 | P1 | Consumer | default `min_density` hides genuine vortex cores | upstream |
| CPD-C7 | P2 | Consumer | README runtime claim vs example docstring | upstream |
| CPD-C8 | P2 | Detached | `requirements.txt` orphan vs `pyproject.toml` | upstream |
| CPD-C2 | P3 | Consumer | README deps vs `pyproject.toml` floors | upstream |
| CPD-C3 | P3 | Consumer | `64³` speedup published arithmetically wrong | upstream |
| CPD-C5 | P1 | Detached | GPU validation notebook zero outputs | upstream |
| CPD-C6 | P3 | Consumer | stale test count in docs | upstream |
| CPD-DETACHED-1 | P3 | Detached | 8 unreachable modules (2 user-authored) | mixed |
| CPD-VERS-1 | P3 | Detached | no version-consistency gate | upstream |

### Fixed (reference only — do not re-mediate)
C1 (fbdc676), C4 (78eaff6), C9 (586c52e), D-P2-2 (44f30e3). These are the
baseline of this plan; the remediation branch already contains them.

---

## 2. Remediation sequence (authorization-gated)

**Order rationale.** The physics chain (Hamiltonian → solver → wavefunction) is addressed
first because it is the system's fundamental contract; then the time-dependent physics
gap; then the vortex defects (the two already-known upstream defects, which depended on
the same line); then the upstream documentation/claim defects; then the detached-code
cleanup (which is lower scientific risk). Upstream defects are proposed as PRs to the
upstream repos with attribution, not local patches.

### Phase A — Fundamental simulation chain (authorize first)
- **A1 — Hamiltonian → solver → wavefunction.** Ensur the builder wires `hbar`/`m` through
  to the observables at the *call* site (see loss points L1, L2 in
  `cpd_consumer_inventory.md`). **Acceptance:** runner log with `hbar=2, m=3` equals the
  explicit `hbar=2, m=3` energy to the same precision; a unit test builds the chain from
  config and compares to the analytic solution for a Gaussian in the HO.
- **A2 — Absorber norm**. After `abl.apply`, observables divide by the surviving norm, or
  the runner logs post-absorption values separately. **Acceptance:** `probe_08`-style
  measurement: `E/norm` matches `E_true` to `1e-12`.

### Phase B — Time dependence (prerequisite to A success)
- **B1 — Legacy solver bridge.** `SplitStep1D/2D/3D(-GPU)` evaluate `V` at each sub-step
  when `time_dependent=True` (exactly like `SplitOperatorSolver`). **Acceptance:**
  `probe_06f`: `max\|ψ_legacy − ψ_td\|` after 20 steps < `1e-12` for a `DipoleDrive` with
  `phase=0`. **Historical preservation:** the legacy path keeps its current behaviour for
  `phase≠0` inputs (documented as a compatibility mode, not a bug).

### Phase C — Vortices (the two known upstream defects)
- **C1 — Node-alignment.** Compute the total winding of all plaquettes around each candidate
  core before applying the density mask (does not itself reject a core; the mask remains).
  **Acceptance:** `probe_09a` (single vortex on a grid *node* → detected, charge `+1`):
  previously `0`.
- **C2 — Default density.** Change `vortex_positions` default `min_density` from `0.2` to
  `0.0` and require the caller to pass the threshold when they need it. **Acceptance:**
  `probe_09b`: core at `rho/rho.max() = 0.185` found at the default.
- **Regression:** `tests/test_new_potentials_and_observables.py::test_vortex_on_node` (new)
  + existing tests remain green.

### Phase D — Upstream defects (propose PRs, separate commits)
- **D1 — 1-D potential axis.** `quantumlab/potentials/*` return 1-D for a `Grid1D` but are
  constructed on 3-D grids; the shape check should be in the *potential* (producer), not
  the solver (consumer). **Acceptance:** `CrystalPotential.evaluate(Grid3D(16,16,16)).shape
  == (16,16,16)`; a test asserts shapes against `grid.shape` for every potential class.
- **D2 — README / docs claims.** Correct `docs/guide/gpu.md:25` (`7.6x` → `7.5x`), `README.md:453`,
  `README.md:413-416` vs `pyproject.toml`, and the `docs/getting-started.md:66` runtime claim
  vs `examples/11`'s own docstring (~30–40 min on CPU). **Acceptance:** the three numbers
  agree with the code: `33.1/4.4 = 7.52`; `gpu: true` on `split_operator` resolves to
  `scipy-cpu` at runtime (verified with `probe_L5_runtime.py`).

### Phase E — Detached-code cleanup (decide and do, do not silently patch)
- **E1 — `quantumlab/config.py`.** Either wire the schema into `SimulationRunner` (the
  documented intent) or mark the module `@deprecated` and remove its callers. **Acceptance:**
  a config produced by `load_config()` is consumable by `SimulationRunner`; otherwise it is
  explicitly deprecated and the registry documents why.
- **E2 — Unreachable modules.** Decide, per module: `plotting_1d/2d/3d`, `volume_3d` — wire
  into `SimulationRunner.animation` (so the capability is used), or mark `experimental` and
  add a smoke test. **Acceptance:** a smoke test renders one `plot_wavefunction_1d` to a
  bytes buffer and reads it back.
- **E3 — Version consistency.** Add a gate: `quantumlab.__version__ == pyproject.toml:7 ==
  CITATION.cff:19`. **Acceptance:** `import quantumlab; quantumlab.__version__ == '1.3.0'`.

---

## 3. Acceptance gates (all must pass before any item is closed)

| Gate | Requirement |
|---|---|
| G1 | each open defect has a commit or PR with regression test |
| G2 | regression tests pass against the committed baseline `7cb98a7` and the remediation branch |
| G3 | independent verification for every new test (analytic or second-implementation reference) |
| G4 | historical `results.json` unchanged (`sha256 148d01cb…`); `validation_report.md` unchanged (`1d0f3db8…`) |
| G5 | no new mock, placeholder, or fabricated value anywhere in the remediation (verified by `grep -R "Mock\|TODO\|FIXME"` and by reading the tests) |
| G6 | every patch is diffed and attributed (upstream / user / shared) in the review record |

---

## 4. Notes on scope and restraint

- **No broad rewrites.** Each item is one function or one call site.
- **No cross-hexagon or domain-wide refactors** are in scope for this audit.
- **The 4 previously fixed items (C1/C4/C9/D-P2-2) remain exactly as committed.**
- **Upstream-only changes** (D1, C1, C2, D2, E1, E3) are proposed against the upstream
  repos with attribution; the audit directory holds the evidence and the acceptance harness.

---

## 5. Sign-off

Pending authorization to (a) apply Phase A–B changes to the remediation branch, and
(b) push the upstream PRs in Phase D as separate commits. Until authorization is given,
this plan is read-only.
