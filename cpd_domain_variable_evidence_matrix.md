# Domain Evidence Matrix — Quantum Simulation CPD Audit

Generated: 2026-11-21 | Framework: evidence-integrity audit (R1–R5 classification)

## Legend

| Class | Meaning | Can support certification? |
|-------|---------|---------------------------|
| R1 | Actual execution against production, captured inputs/outputs | Yes, subject to independent validation |
| R2 | Derived from genuine traceable measurements | Yes, if reproducible |
| R3 | Artificially generated input / controlled test fixture | Only for defined test |
| R4 | Stubbed solver, fabricated output, hardcoded values, simulated hardware | No |
| R5 | Provenance, execution, or source relationship cannot be established | No |

## D27.3 — Zero-Floor Taxonomy | Domain Variables Evidence Matrix

| Variable | Domain | Mathematical def | Units | Producer function | Consumer function | Type | Shape | Classification | Verification | Evidence file | Artifact states |
|----------|--------|------------------|-------|-------------------|-------------------|------|-------|---------------|--------------|----------------|
| cpu_energy | D27.3 | <psi|H|psi> | J | split_step_3d + potential_at(t) | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | CPU: 0.7499948325323975 |
| gpu_energy | D27.3 | <psi|H|psi> | J | split_step_3d_gpu + potential_at(t) | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | GPU: 0.7499948325323964 |
| energy_disagreement | D27.3 | |cpu - gpu| | J | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Cross-backend | domain27_zero_floor_physics.json | 1.1102e-15 |
| cpu_kinetic | D27.3 | <psi|T|psi> | J | split_step_3d | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | 2.9614547268403566 |
| gpu_kinetic | D27.3 | <psi|T|psi> | J | split_step_3d_gpu | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | 2.9614547268403406 |
| cpu_center | D27.3 | <psi|x|psi> | m | split_step_2d (1D) | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | -0.23911383818807963 |
| gpu_center | D27.3 | <psi|x|psi> | m | split_step_2d_gpu | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | -0.23911383818807755 |
| center_disagreement | D27.3 | |cpu - gpu| | m | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Cross-backend | domain27_zero_floor_physics.json | 2.08167e-15 |
| cpu_center_variance | D27.3 | <psi|x^2|psi> - <x>^2 | m^2 | split_step_1d | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | 0.46894652786954766 |
| gpu_center_variance | D27.3 | <psi|x^2|psi> - <x>^2 | m^2 | split_step_2d_gpu | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | 0.46894652786955143 |
| tail_analysis | D27.3 | probability(x < threshold) | 1 | domain27_zero_floor_physics.json | tail_analysis | dict | 6 keys | R2 | Derivation | domain27_zero_floor_physics.json | 6 threshold keys |
| phase_agreement | D27.3 | CPU vs GPU phase alignment | deg | fft_numerical_zeros | domain27_zero_floor_physics.json | dict | 2 keys | R1 | Direct execution | domain27_zero_floor_physics.json | max_phase_diff, phase_diff_std |
| zero_component_counts | D27.3 | count of |FFT| < threshold | counts | fft_analysis | domain27_zero_floor_physics.json | dict | 3 keys | R2 | Derivation | domain27_zero_floor_physics.json | 3 thresholds |
| cpu_final_norm | D27.3 | |psi(T)| | 1 | split_step_3d | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | 1.0000000000000007 |
| gpu_final_norm | D27.3 | |psi(T)| | 1 | split_step_3d_gpu | domain27_zero_floor_physics.json | scalar | (1,) | R1 | Direct execution | domain27_zero_floor_physics.json | 1.000000000000003 |

## D27.3 Visualization Variables — CAN NOT SUPPORT EVIDENCE (R4)

| PNG file | Generator | Actual status | Evidence class |
|----------|-----------|---------------|---------------|
| classification_breakdown.png | generate_validation_artifacts.py | pix2text extraction failed ('Page' object is not subscriptable) | R4 | Invalid — Pix2Text extraction failed |
| cpu_vs_gpu_energy.png | generate_validation_artifacts.py | Pix2Text extraction failed | R4 | Invalid |
| energy_distribution.png | generate_validation_artifacts.py | Pix2Text extraction failed | R4 | Invalid |

## Key Finding

The domain27_zero_floor PNG files are INVALID evidence. They were produced by a Pix2Text
PDF extraction pipeline that failed with 'Page' object is not subscriptable. The generator
attempts to plot arrays from scalar-valued JSON fields (cpu_energy is a float, not a list).
The underlying physics data (domain27_zero_floor_physics.json) is R1 — real measured values.

## D27.3 vs D19-D24 Evidence Population

| Domain | Evidence status | Notes |
|--------|-----------------|-------|
| D19-D24 | R1/R2 evidence | JSON files contain real measurements; PNGs not yet independently verified |
| D27.3 (JSON) | R1 evidence | domain27_zero_floor_physics.json and domain27_zero_floor_comparison.json contain real values |
| D27.3 (PNGs) | R4 evidence | 3 PNGs generated from failed Pix2Text extraction |

## Adjacent Domains (D1-D12) — Probe Execution Records

| Domain | Probe | Status | Key result |
|--------|--------|--------|-----------|
| D1 | probe_01_strang_ordering.txt | Passed | Strang splitting O(dt^3): max |step - manual| = 2.289e-16 |
| D2 | probe_02_hermiticity.txt | Passed | max|H-H^dagger| = 9.339e-16 |
| D3 | probe_03_normalization.txt | Passed | Norm drift < 2.887e-15 |
| D4 | probe_04_fourier.txt | Passed | Parseval diff = 0.0 |
| D5 | probe_05_potentials.txt | Passed | All potentials finite/real |
| D6 | probe_06_time_dependent.txt | Passed | Time-dependent V(x,t) evaluated correctly at all t |
| D7 | probe_07_convergence.txt | Passed | Order=2 convergence observed |
| D8 | probe_08_energy_momentum.txt | Passed | Energy conserved |
| D9 | probe_09_vortex.txt | Passed | Vortex charges detected |
| D10 | probe_10_absorber.txt | Passed | Absorbing boundary mask works |
| D11 | probe_11_cpu_gpu.txt | Passed | CPU/GPU max|dpsi| = 3.423e-15 |
| D12 | probe_12_resolution.txt | Passed | Resolution sweep stable |

## D13-D18 — Extended Validation (Unverified)

| Domain | Notes |
|--------|-------|
| D13-D18 | No dedicated probe scripts or execution records found in evidence/ for these domains |
| D19-D24 | Domain JSON files exist but independent verification not yet performed |

## Open Issues

- 3 PNG visualization files in domain27_zero_floor/ are invalid (Pix2Text extraction failed) |
- Generator expects arrays, JSON has scalars — schema mismatch |
- Domains D13-D18 lack dedicated probe scripts |
- Domains D19-D24 JSON files exist but independent verification not yet performed |
- 204-test result, 2026-11-21 is historical reported, not freshly executed |
- Domain 27 zero-floor taxonomy class definitions not yet extracted from actual source |