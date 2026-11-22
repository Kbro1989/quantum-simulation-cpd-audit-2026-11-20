# CPD Solver API Contract — Time-Dependent Solver Interface

**Date:** 2026-11-21
**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Branch:** `remediation/2026-11-20`

---

## 1. Contract definition

### 1.1 TimeDependentPotential interface (established)

| Method | Semantics |
|---|---|
| `evaluate(grid)` | Evaluate at t=0 (used by the generic solver as a fallback) |
| `evaluate_at(grid, t)` | Evaluate at time t (authoritative for time-dependent potentials) |
| `time_dependent = True` | Boolean flag marking the potential as time-dependent |

### 1.2 Solver interface (established)

| Attribute/method | Semantics |
|---|---|
| `potential` | Reference to the `Potential` object |
| `potential_at(t)` | V(r, t) — authoritative for any solver |
| `_potential_half_step(psi, t, w)` | Apply V at time t with substep weight w |
| `time_dependent` | bool flag — True when potential has `time_dependent = True` |

### 1.3 Legacy solver legacy API (documented in code)

| Attribute/method | Semantics |
|---|---|
| `SplitStep1DSolver.__init__` | Stores `self.V = self.potential.evaluate(self.grid)` |
| `SplitStep1DSolver.update_operators` | Pre-computes `U_V`, `U_T` from stored `V` |
| `SplitStep1DSolver.step` | Uses cached `U_V`, `U_T` only |

---

## 2. Breakage classification

### 2.1 What the code currently does

| File | Line | Behaviour |
|---|---|---|
| `split_step_1d.py` | 10 | `self.V = self.potential.evaluate(self.grid)` |
| `split_step_1d.py` | 17 | `self.U_V = np.exp(-1j * self.V * self.dt / (2.0 * self.hbar))` |
| `split_step_2d.py` | 19 | Same — V cached once |
| `split_step_3d.py` | 41 | Same — V cached once |
| `split_step_3d_gpu.py` | 60–68 | Same — V cached once (CPU or GPU) |

### 2.2 Breakage

For a time-dependent potential, `self.V` is a snapshot at `t=0`. The `step`
method applies this frozen `self.U_V` at every substep. The result:

- `DipoleDrive` contributes zero force after `t=0`
- The legacy solver silently ignores the drive (Domain 6 PARTIAL verdict)
- `SplitOperatorSolver` correctly evaluates `potential.evaluate_at` at every
  substep — the mismatch is both real and documented

---

## 3. Required change (summary)

Each legacy solver must:

1. Store a reference to `self.potential` (already done via `super().__init__`)
2. Add a `potential_at(t)` method: if `time_dependent`, return
   `self.potential.evaluate_at(self.grid, t)`; else return cached static V
3. In `step()`, recompute `U_V` at each substep using `potential_at(t)`

---

## 4. Integration points

| Module | Existing contract | Required change |
|---|---|---|
| `quantumlab/solvers/split_step_1d.py` | `Solver` base | Add `potential_at(t)`, use at substep |
| `quantumlab/solvers/split_step_2d.py` | `Solver` base | Add `potential_at(t)`, use at substep |
| `quantumlab/solvers/split_step_3d.py` | `Solver` base | Add `potential_at(t)`, use at substep |
| `quantumlab/solvers/split_step_3d_gpu.py` | `Solver` base | Add `potential_at(t)`, use at substep |
| `quantumlab/potentials/time_dependent.py` | `evaluate` → `evaluate_at(grid, 0)` | No change required (already correct) |

---

**End of contract.**
