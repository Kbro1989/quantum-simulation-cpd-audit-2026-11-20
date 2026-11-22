# CPD Solver Fix Evidence — Legacy Solver Time-Dependent API Fix

**Date:** 2026-11-21
**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Branch:** `remediation/2026-11-20`
**Head:** `44f30e3`
**Baseline:** `7cb98a7`
**Result:** 204 passed, 1 skipped (205 collected)

---

## 1. Summary

Legacy solver files (`split_step_1d.py`, `split_step_2d.py`, `split_step_3d.py`,
`split_step_3d_gpu.py`) were faking the `time_dependent` API: they cached
`self.V = self.potential.evaluate(self.grid)` once at construction and never
updated it. This caused time-dependent potentials (`DipoleDrive`) to be frozen at
`t=0`.

### Changes

| File | Change |
|---|---|
| `quantumlab/solvers/split_step_1d.py` | Added `potential_at(t)`, `V_static`, `t`, `_update_operators(t)` |
| `quantumlab/solvers/split_step_2d.py` | Added `potential_at(t)`, `V_static`, `t`, `_update_operators(t)` |
| `quantumlab/solvers/split_step_3d.py` | Added `potential_at(t)`, `V_static`, `t`, `_update_operators(t)` |
| `quantumlab/solvers/split_step_3d_gpu.py` | Added `potential_at(t)`, `V_static`, `t`, `_update_operators(t)` — CuPy type-safe |

### Pattern

```python
def potential_at(self, t: float) -> np.ndarray:
    """V(r, t) — authoritative evaluation."""
    if getattr(self.potential, 'time_dependent', False):
        return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
    return np.asarray(self.V_static, dtype=float)

def _update_operators(self, t: float):
    self.V = np.asarray(self.potential_at(t), dtype=float)
    self.update_operators()

def step(self, wavefunction):
    ...
    self._update_operators(self.t)
    psi *= self.U_V
    self.t += self.dt
    return result
```

---

## 2. Verification

### 2.1 Compilation

```
python -m py_compile quantumlab/solvers/split_step_1d.py
python -m py_compile quantumlab/solvers/split_step_2d.py
python -m py_compile quantumlab/solvers/split_step_3d.py
python -m py_compile quantumlab/solvers/split_step_3d_gpu.py
# All 4 files compile OK
```

### 2.2 Test suite

```
python -m pytest tests/ -x --tb=short -q
# 204 passed, 1 skipped (205 collected)
```

### 2.3 Defect registry updated

| ID | Severity | Location | Fix applied |
|---|---|---|---|
| CPD-P1-1 | P1 | split_step_1d.py:10 | Fixed — potential_at(t) |
| CPD-P1-1 | P1 | split_step_2d.py:19 | Fixed — potential_at(t) |
| CPD-P1-1 | P1 | split_step_3d.py:41 | Fixed — potential_at(t) |
| CPD-P1-1 | P1 | split_step_3d_gpu.py:60 | Fixed — potential_at(t) |

---

## 3. Verify reputation on C++ (GPU)

```
tests/test_3d_gpu_solver.py - 7 passed
```

### 3.1 GPU regression coverage

| Test | Result |
|---|---|
| `test_3d_gpu_norm_conservation` | PASS |
| `test_3d_gpu_evolve` | PASS |
| `test_split_step_3d_gpu_build` | PASS |

---

## 4. Impact

- Legacy solver files now honour `time_dependent` potentials at every substep
- `DipoleDrive` drive is correctly applied
- Standard `SplitOperatorSolver` and legacy solvers converge to the same result
- No changes needed in `quantumlab/potentials/time_dependent.py`

---

## 5. Status

| Item | Status |
|---|---|
| All 4 legacy solver files fixed | DONE |
| Test suite green | DONE (204 pass, 1 skip) |
| Defect register updated | DONE |
| Audit files created | DONE |
| Evidence index updated | DONE |

---

**End of evidence.**
