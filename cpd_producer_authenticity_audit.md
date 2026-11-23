# Producer-Authenticity Audit - Quantum Simulation CPD

Generated: 2026-11-21 | Framework: R1-R6 evidence classification |
Audit target: C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20

## Classification Legend

| Class | Meaning | Scientific standing |
|-------|---------|---------------------|
| R1 | Actual execution against implemented solver | Potentially valid measurement |
| R2 | Independent analytical or numerical reference | Independent validation |
| R3 | Synthetic input generated for testing | Valid test fixture, not empirical |
| R4 | Derived visualization or transformation | Depends on source evidence |
| R5 | Mock, stub, hardcoded, or fabricated output | Invalid as execution evidence |
| R6 | Historical report without reproducible execution artifacts | Unverified historical claim |

## Producer-Authenticity Audit Findings

| Evidence class | Domain | Item | Status | Classification | Finding |
|---------------|--------|------|---------------|---------------|---------|
| Production source | D1-D24 (all domains) | quantumlab solvers (split_step_1d.py, 2d.py, 3d.py, 3d_gpu.py) | Upstream files (quantum-simulation-main fork) | RR1 | Time-dependent API fix (potential_at(t), V_static, t, _update_operators(t)) reported. Historical claim needs fresh execution verification. |
| Production source | D1-D24 (all domains) | quantumlab potentials (base.py, barriers.py, time_dependent.py) | Upstream files on disk | RR2 | Potential classes exist but execution traces not in evidence/. Need to verify actual solver calls. |
| Execution record | D19 (CUDA residency) | g0_domain19_results.json + g0_domain19_run.log | Real execution: g0_domain19_run.log (4162 bytes) | RR1 | Execution record exists. Verify that the probe script actually executed the production solver against GPU. |
| Execution record | D20 (FFT performance) | domain20_fft_performance.json + domain20_run.log | Real execution: domain20_run.log (2754 bytes) | RR1 | Execution record exists. Check warm-up handling, repeated runs, GPU clock/thermal tracking. |
| Execution record | D21 (precision zero floor) | domain21_precision_zero_floor.json | Script on disk, JSON results present | RR1 | Script present but no run log. Verify execution was performed. |
| Execution record | D22 (memory scaling) | domain22_memory_scaling.json + domain22_run.log | Real execution: domain22_run.log (5100 bytes) | RR1 | Execution record exists. Verify VRAM baseline and theoretical baselines are from actual GPU. |
| Execution record | D23 (power/thermal) | domain23_power_thermal.json (123KB) + domain23_run.log | Real execution: domain23_run.log (1376 bytes) | RR2 | Large file size suggests actual data collected. nvml_available field must be verified: True = real NVML telemetry, False = simulated. |
| Execution record | D24 (architecture comparison) | domain24_architecture_comparison.json + domain24_run.log | Real execution: domain24_run.log (1603 bytes) | RR1 | Execution record exists. measurement_framework.ready field needs verification. |
| Production code | D27.3 (zero floor) | zero_floor_classification.py + physics_integration.py + generate_validation_artifacts.py | Source code on disk | RR2 | Generator expects arrays but JSON has scalars - schema mismatch. Generator bug, not evidence defect. Pix2Text extraction failed on all 12 PNGs. |
| Execution record | D27.3 (zero floor) | domain27_zero_floor_physics.json (9083 bytes) | JSON results, scalar physics values | RR1 | Scalar physics values. CPU (0.7499948325323975) vs GPU (0.7499948325323964) differ at 1.1e-15. CPU center -0.239 vs GPU center -0.239. REAL EXECUTION RESULTS. Schema mismatch with generator is separate issue. |
| Execution record | D27.3 (zero floor) | domain27_zero_floor_comparison.json (3148 bytes) | JSON results | RR1 | Contains real measured values for FTZ, NaN/Inf propagation, vortex core precision. |
| Visualization artifact | D27.3 (zero floor) | pix2text_extraction_report.json | Extraction FAILED | RR4 | ALL 12 PNG visualization files are invalid. They were produced by Pix2Text PDF extraction which failed. These PNGs CANNOT support scientific evidence. |
| Probe execution | D1-D12 (12 domains) | 12 probe scripts + 12 probe_XX.txt execution records | All 12 probes executed | RR1 | All 12 domain probes have execution records with numerical results. D6 (time-dependent) shows V(x,t) evaluated at multiple times. D11 (CPU/GPU) shows max|dpsi| ~3.4e-15. |
| Probe script | D13-D18 (extended validation) | probe scripts for D13-D18 not documented | No dedicated probes found | RR6 | D13-D18 lack dedicated probe scripts in evidence/. Domain 15 visualization exists but no execution record found. |
| Not found | D25-D26 | Domain definitions and artifacts | Not found | RR6 | D25 and D26 do not exist in the workspace. Do not invent assignments. |
| Defect report | D1-D12 (legacy solvers) | split_step_1d.py, split_step_2d.py, split_step_3d.py, split_step_3d_gpu.py | Reported defect: frozen time-dependent potential at t=0 | RR6 | Reported defect is historical, not independently verified. The 204-test figure needs fresh execution to certify. |