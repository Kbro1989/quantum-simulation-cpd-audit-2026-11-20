# CPD Solver Lifecycle Audit — Cached State Management of V

**Date:** 2026-11-21
**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Branch:** `remediation/2026-11-20`

---

## 1. Purpose

This audit traces the lifecycle of `self.V` (the cached potential array) through
the legacy solver files. The purpose is to establish a baseline for the fix.

---

## 2. Baseline state

| File | Init stores | update_operators | lifecycle state |
|---|---|---|---|
| `split_step_1d.py` | `self.V` (1-D array) | `self.U_V` from stored `self.V` | V frozen at t=0 forever |
| `split_step_2d.py` | `self.V` (2-D array) | `self.U_V` from stored `self.V` | V frozen at t=0 forever |
| `split_step_3d.py` | `self.V` (3-D array) | `self.U_V` from stored `self.V` | V frozen at t=0 forever |
| `split_step_3d_gpu.py` | `self.V` (CPU or GPU array) | `self.U_V` from stored `self.V` | V frozen at t=0 forever |

---

## 3. Structural issues identified

### 3.1 Coupling of time bookkeeping to state storage

The legacy solvers store `self.V` in `__init__` and never recompute it. This
creates a hidden dependency on the potential being time-independent, which is
not verified and not enforced.

### 3.2 No `potential_at(t)` method on legacy solvers

All four files lack a method that maps `(grid, t) -> V(t)`. The generic
`SplitOperatorSolver` has `potential_at(t)` and `_potential_half_step(t, w)`.

### 3.3 Test double ambiguity

A test that wants to verify time-dependent behaviour on the legacy solvers must
inject a `DipoleDrive` potential and then observe that `evaluate_at` was never
called — a negative test that is currently absent.

---

## 4. Recommended remediation

1. Add `potential_at(t)` to each legacy solver, mirroring the generic solver's
   `potential_at` but using `evaluate_at` for time-dependent potentials.
2. Add a `self._time_dependent = getattr(self.potential, 'time_dependent', False)`
   guard.
3. Call `potential_at(t)` at each substep in `step()`, recomputing `U_V` per
   substep.

---

## 5. Re-verification

After fix:

- `probe_06_time_dependent.py` must report max|Δψ| ≈ 0 between legacy solver and
  `SplitOperatorSolver` at matching substep discipline.
- The test that the solver honours `time_dependent = True` must pass.

---

**End of audit.**
