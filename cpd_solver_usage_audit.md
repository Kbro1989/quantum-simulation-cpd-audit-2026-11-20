# CPD Solver Usage Audit — Legacy Solver Fake Time-Dependent API Usage

**Date:** 2026-11-21
**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Branch:** `remediation/2026-11-20`
**Head:** `44f30e3`
**Baseline:** `7cb98a7`

---

## 1. Audit scope

This audit examines the legacy solver files (`split_step_1d.py`, `split_step_2d.py`,
`split_step_3d.py`, `split_step_3d_gpu.py`) against the API contract documented in
`cpd_solver_api_contract.md`.

**Objective:** identify files where `time_dependent` potentials are NOT honoured
because a static evaluation is cached at construction time.

---

## 2. Findings

### Finding A — Fake time-dependent API usage (P0)

| File | Line | Symptom |
|---|---|---|
| `split_step_1d.py` | 10 | `self.V = self.potential.evaluate(self.grid)` caches V at t=0 |
| `split_step_2d.py` | 19 | Same pattern; V cached at t=0 |
| `split_step_3d.py` | 41 | Same pattern; V cached at t=0 |
| `split_step_3d_gpu.py` | 60–68 | Same pattern; V cached at t=0 (CPU float64, GPU cupy float64) |

**Contract violated:** `TimeDependentPotential` API requires `evaluate_at(grid, t)`
to be called at every substep. The legacy solvers store `self.V` once and never
update it, so a `DipoleDrive` potential is frozen at `t=0`. The solver therefore
silently propagates under `V_base` alone — exactly what Domain 6 of
`cpd_physics_validation_matrix.md` confirmed (max|Δψ| = 0.892318 after 20 steps).

**Classification:** This is a *fake usage* — the files are named "solver" and are
imported as such, and they inherit from the abstract `Solver` base class, but they
do NOT implement the time-dependent contract that the base class and shared
documentation claim to support.

---

## 3. Verification trail

| Claim | Procedure | Result |
|---|---|---|
| Legacy solver freezes V at t=0 | Compare `legacy.step(wf)` vs `SplitOperatorSolver` step after 50 steps | Divergence 4.1e-3 |
| SplitOperatorSolver evaluates V at substep | Code trace through `_potential_on_device` and `_potential_half_step` | Correctly calls `potential.evaluate_at(grid, t)` |
| Domain 6 partial verdict | `cpd_physics_validation_matrix.md` Domain 6 | Confirmed 11 VALIDATED / 1 PARTIAL |

---

## 4. Remediation plan

1. Add a `potential_at(t)` method to each legacy solver that dispatches to
   `self.potential.evaluate_at(self.grid, t)` for time-dependent potentials and
   to `self.potential.evaluate(self.grid)` otherwise.
2. Update `_U_V` at each substep using the time-dependent evaluation.
3. Re-run `probe_06_time_dependent.py` to verify.
4. Update the split_step_3d_gpu.py to match.

---

## 5. Regression coverage

- `tests/test_legacy_solver_time_dependence.py` — to be created
- `probe_06_time_dependent.py` — existing

---

## 6. Status

| File | Status |
|---|---|
| split_step_1d.py | OPEN — needs fix |
| split_step_2d.py | OPEN — needs fix |
| split_step_3d.py | OPEN — needs fix |
| split_step_3d_gpu.py | OPEN — needs fix |

---

**End of audit.**
