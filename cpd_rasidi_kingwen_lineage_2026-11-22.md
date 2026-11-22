# Rasidi ↔ Kbro1989 — quantum-simulation development lineage (git-verified)

**Compiled:** 2026-11-22
**Method:** `git` forensics on the local clone. Every row carries a commit hash,
author, date and (where stated) a file/insertion count read from `git show --stat`.
No claim below is taken from a narrative; the pasted recall document was used
only as a hypothesis list and each item was confirmed or corrected against git.

**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Remotes:** `origin` = `git@github.com:Kbro1989/quantum-simulation.git` ·
`upstream` = `git@github.com:rasidi3112/quantum-simulation.git`

## 0. Verified ref state

| Ref | Commit | Date |
|---|---|---|
| `main` (= `origin/main`) | `7cb98a7` | 2026-11-20 |
| `remediation/2026-11-20` | `44f30e3` | 2026-11-20 |
| `upstream/main` | `bf2d342` | 2026-10-24 |
| tag `v1.2.0` | `91022fc` | 2026-10-24 |
| tag `v1.3.0` | `bf2d342` | 2026-10-24 |

Fork position: `upstream/main...main` = **0 upstream-only / 6 local-only**.
`remediation/2026-11-20` = **0 / 10**. The remediation branch is **not pushed**.

Authors, consolidated by email (three git identities are one person):

| Person | Identities | Commits |
|---|---|---|
| Rasidi | `rasidi3112 <129738392+…>`, `Ahmad-Rasidi <129738392+…>`, `rasidi3112 <macbook@Rasidi-MacBook-Pro.local>` | 25 + 11 + 9 = **45** |
| Kbro1989 | `Kbro <kristain33rs@gmail.com>`, `Pick of Gods <149967879+…>` | 12 + 3 = **15** |

Total 60 commits across all refs.

## 1. Timeline A — Rasidi foundation (June 2026)

| Date | Hash | Subject |
|---|---|---|
| 2026-06-13 | `d0a1858` | Initial commit: 1D quantum simulation with clean code and plots |
| 2026-06-13 | `2d9d677` | Add 3D space-time surface plot and apply professional academic scientific styling |
| 2026-06-13 | `2ba1d5c` | Translate README to English and clean code comments |
| 2026-06-14 | `c17817f` | feat: Modularize framework (Phase 11, 1, 4, 5) with multiple potentials, observables, momentum analysis, examples, and tests |
| 2026-06-14 | `14a1ab9` | style: strip all comments and docstrings for clean code appearance |
| 2026-06-14 | `b6db051` | doc: restore root-level image references in README |
| 2026-06-14 | `87dd49c` | doc: include visualization plots for all examples in README gallery |

## 2. Timeline B — Kbro1989 contributions (August 2026)

| Date | Hash | Subject | Scale |
|---|---|---|---|
| 2026-08-02 | `8c54f3f` | Restore workspace files and prepare for upstream sync | — |
| 2026-08-02 | `b59a20e` | feat: Extend framework to full 2D/3D — Grid3D, WaveFunction3D, SplitStep3DSolver, Gaussian2D/3DBarrier, plots_2d, ABL 3D, 3D observables, examples 05/06, 25 tests green | **15 files, +883 / −60** |
| 2026-08-07 | `8d9f209` | Merge pull request #1 from Kbro1989/main (merged by Ahmad-Rasidi) | — |
| 2026-08-20 | `5ff82af` | feat: add GPU-accelerated 3D Split-Step solver and performance benchmarking tools | **12 files, +522** |
| 2026-08-20 | `44b3d5e` | feat: enhance performance benchmarking with multi-run statistics and correctness validation | **6 files, +493 / −122** |
| 2026-08-21 | `9a6d528` | Merge pull request #2 from Kbro1989/main (merged by Ahmad-Rasidi) | **14 files, +893** |

`b59a20e` file list (verified): `examples/05_2d_gaussian_barrier.py`, `examples/06_3d_gaussian_barrier.py`,
`quantumlab/core/{__init__,absorbing_boundary,grid,wavefunction}.py`,
`quantumlab/observables/expectation.py`, `quantumlab/potentials/{__init__,barriers,oscillator}.py`,
`quantumlab/solvers/{__init__,split_step_3d}.py`, `quantumlab/visualization/{__init__,plots_2d}.py`,
`tests/test_3d_solver.py`.

PR #2 branch (`9a6d528^1..9a6d528^2`, verified): `44b3d5e`, `5ff82af`, `aec5d89`.

Later maintenance on the fork:

| Date | Hash | Subject |
|---|---|---|
| 2026-10-04 | `14be7c0`, `01fc975` | Add ALL-FILES.md: 72 files inventory |
| 2026-10-28 | `12d0287` | Merge pull request #3 from rasidi3112/main |
| 2026-11-01 | `95d7c46` | Merge remote-tracking branch 'upstream/main' |
| 2026-11-20 | `7cb98a7` | Merge branch 'main' of github.com:Kbro1989/quantum-simulation |
| 2026-11-20 | `586c52e` | fix(C9): resolve repo root from __file__ in testbench_interlock.py |
| 2026-11-20 | `78eaff6` | docs(C4): correct overstated bit-identical GPU determinism claim |
| 2026-11-20 | `fbdc676` | fix(C1): record unavailable benchmark measurements as null, not zero |
| 2026-11-20 | `44f30e3` | fix(D-P2-2): validate absorbing-boundary arguments instead of corrupting state |

## 3. Timeline C — Rasidi expansion (all 2026-10-24)

33 commits in one day, merged through PRs #3–#12:

| Hash | Subject |
|---|---|
| `18e4085` | fix: runner crash on CPU solvers and add 3D observables |
| `e85f38b` | feat: generic split-operator engine, eigensolvers and Gross–Pitaevskii |
| `04982e1` | feat: 3D isosurface renderer with phase colouring and animations |
| `eda4be6` | feat: 3D showcase examples and validation suite |
| `1689547` | docs: README for v1.1 with 3D gallery and validation results |
| `9290714` | docs: show the original first-release images in the README |
| `0704a26` | Merge pull request #3 (advanced-dynamics-3d) |
| `b1e02f1` | ci: GitHub Actions tests on Python 3.10–3.14 and validation job |
| `123cdf7` | feat: rotating frame, damped GPE, vortex detection and CuPy GPU backend |
| `0de8a26` | feat: rotating-BEC vortex-lattice example and GPU benchmark |
| `9ff3049` | docs: README for v1.2 with CI badge, vortex lattice and GPU usage |
| `2b74702` | fix: roundoff-based tolerance for the 3D norm-conservation check |
| `b6514f8` | Merge pull request #4 (ci-rotating-bec-gpu) |
| `e215a3f` | docs: add MIT LICENSE and CITATION.cff for the v1.2.0 release |
| `91022fc` | Merge pull request #5 (release-v1.2.0) → **tag v1.2.0** |
| `d0339a4` | feat: Colab notebook to validate the GPU backend on real CUDA hardware |
| `1045d0d` | docs: real-GPU validation results on an NVIDIA Tesla T4 |
| `d604bd1` | Merge pull request #6 (colab-gpu-validation) |
| `393f6f1` | docs: documentation site with MkDocs Material and GitHub Pages |
| `5d52a7e` | Merge pull request #7 (docs-site) |
| `d7c2759` | feat: strong-field physics module and soft-core Coulomb atom |
| `da8bf8e` | feat: high-harmonic generation example and validation checks |
| `e5290f1` | docs: strong-field guide, API page, example 12 and README updates |
| `597515e` | Merge pull request #9 (high-harmonic-generation) |
| `e64e4ab` | feat: coupled multi-component Gross–Pitaevskii solver |
| `45638b3` | feat: two-component BEC example and validation checks |
| `6b6d6b1` | docs: two-component condensates guide, example 13 and README updates |
| `60d04f1` | Merge pull request #10 (two-component-bec) |
| `3c43870` | feat: conjugate-gradient ground-state minimiser and dτ continuation |
| `f8f1653` | feat: converged 3D vortex lattice in example 11 |
| `42197cb` | docs: energy minimisation guide, example 11 results and validation table |
| `dc50b81` | Merge pull request #11 (converged-3d-vortex-lattice) |
| `b8a2c4d` | chore: release v1.3.0 |
| `bf2d342` | Merge pull request #12 (release/v1.3.0) → **tag v1.3.0** |

## 4. Corrections to the pasted recall document

Evidence classes: **VERIFIED** (hash read this session) · **REFUTED** · **UNVERIFIED** (no local evidence).

| Pasted claim | Disposition | Evidence |
|---|---|---|
| "August 6, 2026 first PR integration and LinkedIn interaction" | **REFUTED (date)** | merge `8d9f209` is dated **2026-08-07**; no LinkedIn record exists on disk |
| "October 23–24, 2026 major expansion" | **REFUTED (date)** | every expansion commit is dated **2026-10-24**; nothing on the 23rd |
| "merge commit 9a6d528, 893 additions across 14 files and three commits" | **VERIFIED** | `git show --stat 9a6d528` = 14 files, 893 insertions; branch `9a6d528^1..9a6d528^2` = `44b3d5e`, `5ff82af`, `aec5d89` |
| "releases v1.1–v1.3" | **PARTLY VERIFIED** | `v1.1` is a docs commit (`1689547`); tags present locally are **v1.2.0** (`91022fc`) and **v1.3.0** (`bf2d342`); no `v1.1` tag |
| "25/25 passing" | **UNVERIFIED** | commit `b59a20e` message says "25 tests green"; not re-executed here |
| "Your contributions included Grid3D, WaveFunction3D, SplitStep3DSolver, Gaussian 2D/3D barriers, 3D ABL, multidimensional observables, probability-current, GPU 3D, CPU/GPU benchmarking, examples and tests" | **VERIFIED** | file lists of `b59a20e`, `5ff82af`, `44b3d5e` |
| "Ahmad Rasidi (rasidi3112) was a LinkedIn and GitHub connection… July 31 PR welcome, August 6 interaction" | **UNVERIFIED** | no local archive; GitHub-side merges confirm collaboration but not LinkedIn content |
| "three separate timelines (your engineering / Rasidi's development / your forensic investigation)" | **VERIFIED as a framing** | timelines A/B/C above; the forensic timeline is the CPD audit (`cpd_defect_register.json`) |

## 5. What this lineage does and does not establish

**Established:** commit authorship, dates, merge direction, file scope, and the
fact that Kbro1989's 2D/3D + GPU work entered upstream through PRs #1 and #2,
merged by Rasidi on 2026-08-07 and 2026-08-21.

**Not established:** that any specific Rasidi feature (Timeline C) is a direct
technical dependency on the Kbro1989 contributions. Rasidi's 2026-10-24 work
was built on the merged upstream tree, so it *contains* that code, but no
per-feature dependency is claimed here.

**Not established:** any LinkedIn comment, message or conversation content.
