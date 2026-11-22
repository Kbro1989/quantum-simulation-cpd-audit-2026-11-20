# Independent Physics Validation - Quantum Simulation CPD

Generated: 2026-11-21 | Framework: Independent re-computation of physics observables |
Audit target: C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20

## Status
- NOT YET EXECUTED
- No independent re-computation has been performed as of this audit.
- This file is a placeholder pending Phase 2 execution.

## Scope

Variables targeted for independent verification:

| Variable | Domain | Independent method | Acceptance criterion |
|----------|--------|--------------------|---------------------|
| cpu_energy | D27.3 | Re-run split_step_3d with same initial conditions | CPU energy within 1e-10 of original |
| gpu_energy | D27.3 | Re-run with GPU backend | GPU energy within 1e-10 of original |
| cpu_center | D27.3 | Re-compute <x> from wavefunction | |diff| < 1e-10 |
| gpu_center | D27.3 | Re-compute <x> from GPU wavefunction | |diff| < 1e-10 |
| cpu_center_variance | D27.3 | Re-compute <x^2> - <x>^2 | |diff| < 1e-10 |
| gpu_center_variance | D27.3 | Re-compute <x^2> - <x>^2 | |diff| < 1e-10 |
| fft_normalization | D27.3 | Independent FFT implementation | |diff| < 1e-12 |
| relative_l2_error | D27.3 | Independent computation | |diff| < 1e-14 |
| phase_agreement | D27.3 | Independent phase comparison | max_phase_diff < 1e-10 |

## Pending Actions

1. Re-execute probe_01 through probe_12 with frozen baseline hashes
2. Independently recompute D27.3 physics values from raw wavefunction
3. Verify CPU/GPU agreement independently
4. Cross-check zero-floor classifications against mathematical definitions

## Evidence Preservation

All original evidence files are preserved in the audit workspace:
- domain27_zero_floor/domain27_zero_floor_physics.json
- domain27_zero_floor/domain27_zero_floor_comparison.json
- probes/probe_01-12.py and execution records
- nvidia_validation/domain19-24/*.json and run logs
- (Original PNGs preserved as failed baseline: R4, not deleted)