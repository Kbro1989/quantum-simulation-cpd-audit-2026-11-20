# Backend Independence Audit

Generated: 2026-11-21 | D27.3 - CPU/GPU independence verification |
Audit target: C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20

## Status

**PENDING — the independent re-execution has not been performed.**

- The table under "Expected findings" is **REPORTED** — values from an earlier
  recorded run, not produced by this audit. The `gpu_*` rows are empty (`-`).
- The CPU/GPU independence comparison itself is **PENDING**: no independent
  re-execution has been run as of this audit.
- This file is a plan plus inherited numbers. It is **not** a completed
  independence verification and must not be cited as one.

Executed CPU/GPU evidence that exists elsewhere: `cpd_final_audit.md` §3.1
(`max‖dpsi‖ = 3.4e-15 / 2.7e-15 / 8.4e-16`, roundoff-scale).

## Method

1. Trace each variable's producer function
2. Execute the same computation on CPU (numpy) and GPU (cupy) independently
3. Compare results with a hardened tolerance

## Expected findings

| Variable | CPU (reported) | GPU (reported) | Expected agreement |
|----------|----------------|----------------|--------------------|
| cpu_energy | 0.7499948325323975 | 0.7499948325323964 | 1.1e-15 |
| gpu_energy | - | - | - |
| cpu_center | -0.23911383818807963 | -0.23911383818807755 | 2.1e-15 |
| gpu_center | - | - | - |
| cpu_center_variance | 0.46894652786954766 | 0.46894652786955143 | 3.8e-15 |
| gpu_center_variance | - | - | - |
| fft_normalization | 63.99999999999999 | 64.0 | 1e-14 |

## CPU/GPU Independence Verification

Key question: Are both backends computing from the SAME wavefunction state?

Evidence: The test_energy_threshold_with_zero_floor() function creates TWO separate
WaveFunction1D instances (psi0 for CPU, psi0 for GPU). Each is evolved independently
on its own backend. They should agree to numerical precision.

Recommendation: Run the same producer code on both backends and compare.
If agreement is tight (1e-10), the CPU/GPU implementations are independent.
If agreement is loose, investigate backend-specific behavior.
