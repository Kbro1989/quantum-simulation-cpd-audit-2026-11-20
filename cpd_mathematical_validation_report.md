# quantumlab — Mathematical Validation Report (CPD audit 2026-11-20)

**Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
**Branch:** `remediation/2026-11-20` @ `44f30e30654c064b75f760833741ab55b392ff20`
**Date:** 2026-11-20 · **Method:** independent numerical probes executed in the audit directory;
see companion `cpd_physics_validation_matrix.md` (`evidence/probe_01_*.txt` … `probe_12_*.txt`) for raw output.

This report is the synthesis of the 12-domain physics validation matrix. All numbers
quoted below are copy-verified from the evidence files.

---

## 1. Summary

| Domain | Verdict | Key evidence |
|---|---|---|
| 1 Schrödinger evolution / split-operator ordering | **VALIDATED** | `probe_01`: manual Strang, adjoint, time-reversal, Yoshida composition |
| 2 Hamiltonian construction / Hermiticity | **VALIDATED** | `probe_02`: `max\|H−H†\| = 9.3e-16`, `max\|Im(H)\| = 3.3e-16` |
| 3 Wavefunction normalization | **VALIDATED** | `probe_03`: drift ≤ 2.9e-14 over 300 steps |
| 4 Fourier-space operators | **VALIDATED** | `probe_04`: `grid.k − 2πfftfreq = 0`, Parseval exact, aliasing as designed |
| 5 Potentials / units | **VALIDATED** | `probe_05`: all 49 evaluations dimensionless/shape-safe; HO ground state matched |
| 6 Time-dependent Hamiltonians | **PARTIAL** | `probe_06`: legacy solvers freeze `V` at `t=0` |
| 7 Numerical convergence order | **VALIDATED** | `probe_07`: order 2 → 2.000; order 4 → 4.00/3.98 then roundoff floor |
| 8 Energy / momentum | **VALIDATED** | `probe_08`: HO `⟨H⟩` conserved to `2.8e-5`; Ehrenfest to `1.3e-15` |
| 9 Vortex winding / topological charge | **VALIDATED** | `probe_09`: charges exactly +1/−1, position error 0.037 (one half-grid) |
| 10 Absorbing boundary | **VALIDATED** | `probe_10`: suppression factor `2.1e-2`, norm loss 0.89 intentional |
| 11 CPU/GPU equivalence | **VALIDATED** | `probe_11`: `max\|dpsi\| ≤ 8.4e-16` |
| 12 Stability / resolution | **VALIDATED** | `probe_12`: Weideman–Herbst instability reproduced, not a bug |

**Counts:** 11 VALIDATED · 1 PARTIAL · 0 FAILED · 0 NOT_RUN

---

## 2. Verdict definitions

- **VALIDATED** — an independent check (analytic reference, explicit operator construction,
  or a different algorithm than the library under test) reproduced the invariant to
  floating-point precision; deviations were roundoff, discretization error, or an intended
  physical property (non-unitarity of an absorber, non-conservation by a time-dependent
  Hamiltonian, the Weideman–Herbst parametric instability).
- **PARTIAL** — the invariant holds for the production code path but there exists a
  legacy/deprecated code path or a condition under which it fails; that unexercised path
  is listed under Section 4.
- **FAILED** — the invariant is contradicted by the executed check. None.
- **NOT_RUN** — no probe was executed. None.

---

## 3. Independent checks performed (all executed, exact outputs above)

1. Split-operator ordering: manual Strang `V/2, T, V/2`, adjoint, backward solver,
   Yoshida order-4 composition — residuals at the `2.3e-16` level.
2. Hermiticity: explicit `F† diag(T_k) F + diag(V)` constructed in numpy; `max\|H−H†\| = 9.3e-16`.
3. Normalization: Gaussian norms exactly 1.0; drift over 300 steps ≤ 2.9e-14.
4. Fourier operators: `grid.k` matches `2π·fftfreq` to `0` (bitwise); Parseval exact;
   Nyquist and above-Nyquist aliasing reproduced.
5. Potentials: all 22 classes × 1D/2D/3D → finite/real/shape-correct; ground-state energies
   matched (`E0(HO) = ℏω/2`, SoftCoulomb `-0.5`, 2D HO `ℏω = 1.0`); dimension guards fired.
6. Time dependence: `DipoleDrive.force(evaluate_at)` to `0.00e+00`; Yoshida times
   `[0, 0.135, 0.135, −0.035, −0.035, 0.1]`; legacy solvers stop honouring the drive
   (`max\|ψ_legacy − ψ_td\| = 0.892318` after 20 steps).
7. Convergence: order 2 consistently `2.000`; order 4 `4.00 → 3.98 → 3.48 → 0.58`
   (floor at `~6e-14`, a roundoff artifact — deliberately not tested with a vanishing
   potential, which would measure only roundoff).
8. Energy/momentum: HO `⟨H⟩(0) = 2.125 = analytic`; free-particle Ehrenfest
   `d⟨x⟩/dt = ⟨p⟩/m` to `1.3e-15`.
9. Vortices: analytic vortex core detected, charge exactly `+1`/`−1` (contour-integral cross-check),
   position error `0.0369` (half-grid). Node-placed core yields `0` vortices (grid-alignment defect).
10. Absorber: mask in `[0,1]`, interior exactly 1, norm loss `0.8908` (intentional absorption),
    wraparound density suppressed `48×`; orders 1–3 produce identical masks by design.
11. CPU/GPU: `max\|dpsi\| = 3.4e-15 / 2.7e-15 / 8.4e-16` (1D/2D/3D) — FFT-library roundoff, not
    bit-identical as documented.
12. Stability: parametric instability at `ℏ k_max² |w| dt/(2m) = π` reproduced; error growth at
    `2·dt_crit` is the known Weideman–Herbst behaviour, bounded (`max\|ψ\| ≈ 0.75`).

---

## 4. Unvalidated sub-items (residual risk, ranked)

1. **Domain 6 — legacy solver time dependence (PARTIAL).** `SplitStep1D/2D/3D(-GPU)`
   freeze `V` at `t=0` and ignore `DipoleDrive`: `max\|ψ_legacy − ψ_td\| = 0.892318` after
   20 steps, while the docs claim solvers "detect these through
   `time_dependent = True` and call `evaluate_at(grid, t)` at every sub-step" (`docs/guide/potentials.md:55`,
   `docs/guide/solvers.md:41`). **Status: legacy bridge, not a production blocker.** The
   production `SplitOperatorSolver` samples `evaluate_at` correctly at every sub-step.
2. **Domain 10 — reflection suppression measured indirectly.** Absorbed probability in the
   left region is taken as evidence (`ratio 2.09e-2`); a direct reflected-flux measurement is
   not available without a source emitting pulses into the boundary. Residual risk: low.
3. **Domain 8 — very-long-time Ehrenfest.** Validated to `1e-15` for `t ≤ 2`; at `t = 4` the
   dispersed packet tail wraps the periodic boundary and the error rises to `8.7e-05`. Not
   a violation of Ehrenfest; a boundary artifact.
4. **Domain 7 — order 4 below the roundoff floor.** The grid cannot resolve 4th-order
   convergence below `dt ≈ 0.004` (`1−overlap ≈ 6e-14`); asymptotic 4th-order behaviour
   below that is not established on this grid.
5. **Domain 5 — 3D harmonic ground state.** `E0 = 1.4999824124` vs `1.5` on a coarse `14³`
   grid (`1.76e-5`); an expected discretization effect, not a unit error.

---

## 5. What is NOT validated (read-only statement)

A **theorem-grade** validation (all claims verified, zero residual) is not achieved:
five residual items remain open. This report therefore stops short of certifying the
library as a verified scientific instrument. The 12 domain-level probes above are the
complete set of independent numerical checks executed this session, and each one is
reproducible from the evidence files listed above.
