# CPD — Detached Inventory

**Repo:** `C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main`
**Branch:** `remediation/2026-11-20` · **HEAD:** `44f30e3`
**Date:** 2026-11-20 · **Method:** static reachability from test imports (`evidence/scan_reachability.py`)

> **Detached does not mean defective.** It means the operational relationship has not been
> established. Each item below is classified rather than condemned.

---

## 1. How this was determined

A static import graph was built among all 49 modules, seeded with the modules the test files
import, then traversed. A module is **detached** if it is never reached.

Two earlier naive measures were discarded because they overstate:

| Measure | Result | Why rejected |
|---|---|---|
| "no test imports this module by name" | 21 modules | treats `visualization.animation` as detached although `test_runner.py` reaches it via `runner.py` |
| raw import graph without `__init__` canonicalisation | 21 modules | package-prefix imports (`from quantumlab.stationary import x`) resolved to nothing |
| **reachability from test seeds** | **8 modules** | used below |

---

## 2. Detached modules — 8 of 49

| Module | Authored by | Class | Evidence | Operational relationship |
|---|---|---|---|---|
| `quantumlab.config` | upstream `c17817f` | **Dead + incompatible** | no importer anywhere; output cannot drive `SimulationRunner` (3 mismatches, verified) | **Not established.** Would raise or mis-configure if used. |
| `quantumlab.constants` | upstream `c17817f` | **Dead** | no importer anywhere | **Not established.** |
| `quantumlab` (`__init__.py`) | upstream `c17817f` | **Weakly connected** | declares `__version__`; nothing asserts it against `pyproject.toml` | Declares metadata only. |
| `quantumlab.core` (`__init__.py`) | **Kbro `8c54f3f`** | **Weakly connected** | package init; re-exports not enumerated or tested | **Not established.** User-authored. |
| `quantumlab.visualization` (`__init__.py`) | upstream `c17817f` | **Weakly connected** | re-exports plots modules; `__all__` never asserted | **Not established.** |
| `quantumlab.visualization.plots_1d` | upstream `c17817f` | **Disconnected production capability** | no test; not reached from any test seed | **Unclear** — plotting code that nothing verifies. |
| `quantumlab.visualization.plots_2d` | **Kbro `b59a20e`** | **Disconnected production capability** | no test; not reached | **Unclear** — user-authored, unverified. |
| `quantumlab.visualization.plots_3d` | upstream `c17817f` | **Disconnected production capability** | no test; not reached | **Unclear.** |

### 2.1 Reached only indirectly — **not** detached

These have no test that names them, but are reachable through a tested module, so their
operational relationship **is** established:

`observables.current` · `observables.nonlinear` · `potentials.apertures` · `potentials.base` ·
`potentials.coulomb` · `potentials.time_dependent` · `potentials.traps` · `solvers.base` ·
`stationary.conjugate_gradient` · `stationary.eigensolver` · `stationary.hamiltonian` ·
`stationary.imaginary_time` · `visualization.animation` · `visualization.style`

---

## 3. Detached scripts and artifacts

| Item | Class | Evidence |
|---|---|---|
| `benchmarks/validation_suite.py` | **Disconnected production capability** | generates the committed 27/27 validation report; not run in CI; no test |
| `benchmarks/gpu_split_operator.py` | **Disconnected production capability** | the script behind the published Tesla T4 table; no test |
| `benchmarks/perf_comparison.py` | **Connected** | imported by `tests/test_benchmark_failure_handling.py` via importlib (the naive scan missed this — stated as a scan limit) |
| `examples/01`–`examples/13` | **Optional / unverified** | no tests; documented numeric claims have no committed artifact |
| `setup.py` | **Optional** | packaging stub |
| `testbench_interlock.py` | **User-authored, detached** | no test imports it; the C9 fix is held up by manual runs only |

---

## 4. Orphaned configuration fields

`quantumlab/config.py` declares fields the runner never reads:

| Field in `DEFAULT_CONFIG` | Read by `runner.py`? |
|---|---|
| `units` | no |
| `wavefunction.type` / `x0` / `k0` / `sigma` (as a nested block) | runner reads a flat `wavefunction` block with `type`, `x0`, `k0`, `sigma` — shapes differ |
| `solver.t_max` | runner reads `num_steps` |
| `solver.absorbing_boundary` (bool) | runner expects a dict `{width, order}` |
| `solver.boundary_strength` | **never read anywhere** |
| `visualization.live_plot` / `save_plots` / `save_animation` / `animation_fps` / `theme` | runner reads none of these |
| `export.enabled` / `format` | runner writes only an npz; `format` unused |

---

## 5. Disposition — do not repair detached code from assumption

| Class | Count | Recommended action |
|---|---|---|
| Dead | 1 | `constants.py` — delete, or wire and test |
| Dead + incompatible | 1 | `config.py` — reconcile schema with `SimulationRunner`, or delete |
| Weakly connected (metadata/package init) | 4 | add cheap contract tests (version consistency, `__all__` resolvability) |
| Disconnected production capability | 3 | decide: wire into a test, or mark experimental |
| Detached scripts | 3 | bring `validation_suite.py` and `gpu_split_operator.py` into CI |
| Optional | 2 | leave; capture example artifacts to make doc claims checkable |

**Nothing in this section was modified.** This inventory determines what gets repaired; it is not
a repair authorisation.
