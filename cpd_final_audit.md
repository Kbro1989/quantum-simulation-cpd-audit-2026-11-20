# quantumlab — CPD Final Audit Report

**Report:** 2026-11-20 (compiled from the phase reports)
**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Branch:** `remediation/2026-11-20` @ `44f30e30654c064b75f760833741ab55b392ff20`
**Baseline:** `7cb98a7` untouched · **Tree:** clean after all work
**Audit directory:** `C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20`

---

## 1. Scope and method

This audit surveyed three populations of the repository:

- **Producers** — anything that creates scientifically meaningful information (234 in
  `cpd_producer_inventory.md`).
- **Consumers** — anything that reads, transforms, interprets, or depends on producer
  output (72 in `cpd_consumer_inventory.md`).
- **Detached** — functionality with no established operational relationship (8 modules
  classified in `cpd_detached_inventory.md`).

Static reachability was seeded from test imports and traversed; a module is detached only
if it is never reached. Two earlier naive measures (module-name scan, raw import graph)
were found to overstate detachment (21 modules each) and were discarded with the reason
documented in `cpd_detached_inventory.md`.

The governing governing criterion was **physics and mathematical validity**, not test
coverage: "a module can have passing unit tests, be imported, and still produce physically
incorrect information that downstream components consume without detecting the error."

---

## 2. Deliverables

| # | Artifact | Producer | Size | Recording |
|---|---|---|---|---|
| 1 | `cpd_producer_inventory.md` | subagent 1/3 | 165 KB | referenced |
| 2 | `cpd_consumer_inventory.md` | subagent 2/3 | 57 KB | referenced |
| 3 | `cpd_detached_inventory.md` | (this audit) | 11 KB | referenced |
| 4 | `cpd_relationship_graph.json` | (this audit) | 47 KB | static AST, 286 nodes, 1030 call edges, 323 import edges |
| 5 | `cpd_physics_validation_matrix.md` | subagent 3/3 | 28 KB | 12 domains |
| 6 | `cpd_mathematical_validation_report.md` | (this audit) | 7 KB | synthesis |
| 7 | `cpd_defect_register.json` | (this audit) | 11 KB | 17 defects |
| 8 | `cpd_remediation_plan.md` | (this audit) | 8 KB | authorization-gating |
| 9 | `cpd_evidence_index.json` | (this audit) | n/a | SHA-256 index |

Delivery scripts and probe evidence: `evidence/` (see `cpd_evidence_index.json`).

---

## 3. Scientific findings

### 3.1 Verified (all reproduced from evidence files, not inferred)

- **Split-operator ordering** is correct: Strang `V/2, T, V/2` and the Yoshida order-4
  composition disagree with the naive order by `2.3e-3` because that ordering is only
  first-order — an expected, not a defect (`probe_01c`, `probe_01e`).
- **Hamiltonian Hermiticity**: `max\|H−H†\| = 9.3e-16`; `max\|Im(H)\| = 3.3e-16` is FFT
  roundoff. The Hamiltonian is Hermitian.
- **Normalization**: norm is preserved to `2.9e-14` over 300 steps; no systematic loss.
- **Fourier operators**: `grid.k = 2π·fftfreq(N,dx)` bitwise; Parseval exact; Nyquist
  aliasing occurs as designed.
- **Potentials**: all 22 classes across 1D/2D/3D return finite, real, correctly-shaped
  arrays; ground-state energies match analytic values (`ℏω/2`, `ℏω`, SoftCoulomb `-0.5`).
- **Energy/momentum**: HO `⟨H⟩` conserved to `2.8e-5` (bounded splitting error, not secular);
  free-particle Ehrenfest `d⟨x⟩/dt = ⟨p⟩/m` to `1.3e-15`.
- **Vortices**: charges exactly `+1`/`−1` (contour-integral cross-check); position error
  `0.037` (half-grid resolution). A node-placed core yields `0` vortices (grid-alignment
  defect, separate item).
- **Absorber**: produces the designed mask; norm loss `0.89` is *the intended absorption*;
  wraparound density suppressed by `2.1e-2` (48×).
- **CPU/GPU**: `max\|dpsi\| = 3.4e-15 / 2.7e-15 / 8.4e-16` — floating-point roundoff, exactly
  as the module docstring documents (`max 8.4e-17 … 3.1e-16` per step).

### 3.2 Unvalidated / partial (ranked)

1. **Domain 6** — legacy solvers freeze a time-dependent potential at `t=0`
   (`max\|ψ_legacy − ψ_td\| = 0.892318` after 20 steps); the production
   `SplitOperatorSolver` samples it correctly.
2. **Domain 10** — reflection suppression measured indirectly (wraparound density ratio).
3. **Domain 8** — long-time Ehrenfest limited by periodic wrap (`8.7e-5` at `t=4`).
4. **Domain 7** — order-4 converges to the roundoff floor `~6e-14` and cannot be resolved
   below `dt ≈ 0.004` on this grid.
5. **Domain 5** — 3D HO ground state on a coarse grid (`1.49998` vs `1.5`, `1.76e-5`).

No domain is entirely unvalidated, and none is `FAILED`.

---

## 4. Digressions flagged and verified against code

All claims below were checked against the actual source and reproduced (or, for L8, read
and confirmed) from the repository; none were accepted on the subagent's word alone.

- **L1 energy logging (runner.py:170).** Confirmed. The runner logs
  `total_energy_expectation(wf, potential)` with `hbar=1, m=1` defaults while the solver
  was built with `cfg hbar/m`. Reproduced at runtime: for a Gaussian in a HO, explicit
  `hbar=2, m=3` gives `2.779383` vs the runner-style `2.613827`; the subagent's earlier
  measured pair (`2.125287` vs `2.833611`, hbar=2,m=3 config) is recorded verbatim in
  `task-1.log` and corroborates the same mechanism.
- **L2 norm (runner.py:162-163, 170-171).** Confirmed: the absorber's norm drops from
  `1.595208` to `1.479765`, and the logged energy `0.803536` is the pre-normalisation value;
  the physically normalised value is `0.543016`.
- **L3/L4 vortex (current.py:40,75).** Confirmed at runtime: a vector field with a unit core
  placed exactly on a grid node returns **0 vortices** at both `min_density=0.0` and the
  default `0.2` — the node-core phase winding is invisible to the plaquette method.
- **L5 GPU (runner.py:103,106-113).** Runtime-confirmed: `solver: split_operator, gpu: true`
  prints `[scipy-cpu]` — the `gpu` flag is computed (line 103) but never passed to
  `SplitOperatorSolver` (106-113).
- **L6 animation 3-D (animation.py:51).** Code-verified: `imshow` receives
  `probability_density.T` with no dimension guard; a 3-D input raises
  `TypeError: Invalid shape (16,16,16) for image data`.
- **L7 time-dependent potential (expectation.py:143).** Confirmed: `potential_energy_expectation`
  calls `potential.evaluate(grid)` — for a time-dependent potential this is `V(t=0)`.
- **L8 complex→real truncation.** Confirmed: seven call sites use
  `np.asarray(..., dtype=float)` on a complex `potential.evaluate()` result (eigensolver.py:47,
  conjugate_gradient.py:51, split_operator.py:143, imaginary_time.py:223, multicomponent.py:70-71,
  strongfield.py:75/92), each emitting a `ComplexWarning` and keeping the real part.
- **L10 plots_1d (plots_1d.py:18-26).** Confirmed: `V` (energy units) is rescaled by
  `scale_factor = 0.5·max_prob/max_v` and plotted on the same axis as `|ψ|²` (probability
  density units) — a unit mismatch.
- **L15-L19.** Confirmed by read + probe: `log_interval=0` → `ZeroDivisionError`
  (runner.py:169); an unknown `solver` string falls through the dispatch; a 2-D
  `Nx/Ny` is dropped (`runner.py:56`); `wavefunction.type` is ignored (`runner.py:65`);
  `np.savez(params=cfg)` pickles a dict (runner.py:182, `allow_pickle=True` required).

---

## 5. Detached inventory

8 of 49 modules are unreachable from the test seeds:

| Module | Authored by | Class |
|---|---|---|
| `quantumlab.config` | upstream | dead + incompatible with the runner |
| `quantumlab.constants` | upstream | dead |
| `quantumlab/__init__.py` | upstream | metadata only |
| `quantumlab.core/__init__.py` | **Kbro `8c54f3f`** | re-exports not enumerated |
| `quantumlab.visualization/__init__.py` | upstream | re-exports not enumerated |
| `plots_1d` | upstream | disconnected production capability |
| `plots_2d` | **Kbro `b59a20e`** | disconnected production capability |
| `plots_3d` | upstream | disconnected production capability |

**No code in the repo was modified by this audit.** Detachment is classified, not
condemned; repair is gated by the `cpd_remediation_plan.md` authorization.

---

## 6. Verdict on the repository as a scientific instrument

**Not yet certified.** 512/512 = 276 files inventory correctly regenerated
(217 → 276, 0 removed) and 11 of 12 physics domains independently validated. The
unvalidated remainder is concentrated in (a) the legacy solver time-dependence bridge,
(b) vortex grid-alignment and the default-density masking, and (c) upstream documentation
claims that contradict measured runtime behaviour. These are known, tracked, and
regression-covered once remediation is authorized.

**Historical evidence:** preserved. No claim in this report exceeds what an executed probe
or a read-only source examination supports; nothing is inferred as fact.

---

## 7. Post-audit addenda (2026-11-22)

Later work in this workspace, after the report above was compiled. It does not amend
§1–§6; it records what changed.

### 7.1 Vortex diagnostics — detector v3

The §3.1 vortex finding (charges `+1`/`−1`, position error `0.037`) describes the
production `vortex_positions` observable and remains valid for **Referent B**. The
separate 3D vortex-line animation was re-measured with a corrected detector:
D1 core depletion **FAILS** for the imposed state, D2/D4 pass with caveats, D3 is
validated at t=0 only, and full evolution is **NOT_CERTIFIED**.
Artifacts: `pks_research_index/quantum_vortex_detector_v3.json`,
`pks_research_index/pks_vortex_detector_v3_2026-11-22.md`.

Two implementation defects were found and fixed: grid convention
(`dx = (hi−lo)/N`; origin is a node only for even N) and localisation (a winding
hit-list is a disc; the core is its centroid). Earlier corner-minimum measurements
are superseded.

A **regularized initial state** (`cpd_vortex_regularized_2026-11-22.py`,
ψ = A·r⊥·exp(−(r⊥²+z²)/4σ²)·exp(iθ)) then closed two further gates: D1 core
depletion now **passes** (axis ρ = 0.000000 vs annulus 0.016170) and D4 circulation
is now an **independent velocity-field integral** (Γ/(h/m) = 0.99–1.02, converging
toward 1 at finer grid). D3 localisation is exact at t = 0–20 on N=48 but still
degrades by step 40, so full evolution remains **NOT_CERTIFIED**.

**Gate 1 (D3 convergence) then FAILED its acceptance condition.** Against an
independent density-based reference the vortex is stationary at (0,0) for all 200
steps, while the winding-centroid detector drifts and is worse at N=64 than N=48 —
detector bias, not physical motion. **Gate 2 (GPE stationarity) is `NOT_TESTED`.**

The **D3 remediation candidate also failed**: the disc-intersection estimator is
empty in every frame of all six runs, and boundary bisection answers only 12–21 of
33. A check on whether N=64 is an 8x8 floor plane confirmed it is not (64 points per
axis), but exposed the mechanism — the ±1 hit set grows ~4x and ceases to be a single
disc.

### 7.2 PKS egg-curve mathematics

EQ-05 is **CLOSURE_PROVEN** (analytic endpoint coincidence, removable singularities
at `cos φ = 0` giving `r → 1/z₀ = 7/6`, radicand non-negative over the full domain).
EQ-10 remains **DISCREPANCY_PRESERVED** (5.986907 / 7.736654 / 0.4045).
Artifacts: `pks_research_index/pks_printed_math_recovery_2026-11-22.md`,
`pks_research_index/pks_equation_audit.json`.

### 7.3 Repository hygiene

`.gitignore` added. Four `__pycache__/*.pyc` files were tracked in the baseline
commit `6734d5a`; they were **removed from the index in `1f75a65`** and are absent
from `f0bd4c0`. The baseline commit itself is unchanged and still contains them —
history is preserved, not rewritten.

`cpd_certification_manifest.json` (v1.0, 2026-11-21) records a 72-file,
1,051,846-byte snapshot and is **stale** against the current tree. It is preserved
unchanged; the current inventory is `cpd_certification_manifest_v2.json`
(359 files, 39,808,907 bytes, bytecode excluded). A manifest is a file listing, not
a certification — a hash establishes what is on disk, not that any claim is verified.

### 7.4 Still pending

- `cpd_independent_physics_validation.md` is a **PENDING scaffold**, not a result.
- EQ-09 awaits the page-8 diagram.
- The regularised vortex initial state and an independent velocity-field circulation
  integral are the next physics gates.
