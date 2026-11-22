# quantum-simulation CPD audit

**Forensic audit workspace for the QuantumLab / quantum-simulation stack.**
Created 2026-11-20 · first published commit `6734d5a` (2026-11-22) · maintained by Kbro1989.

This repository is **not** the simulation. It is the independent record that asks
whether the simulation's outputs are mathematically and physically defensible, and
whether each claim can be traced to a source. The production library lives at
`C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main`; the upstream
project is `rasidi3112/quantum-simulation`.

<details>
<summary>🖼️ &nbsp;Visual assets — PNG / GIF &nbsp;·&nbsp; commit-pinned to <code>1f75a65</code> &nbsp;·&nbsp; 5 GIFs, 79 PNGs</summary>

Every link is pinned to commit <code>1f75a65bb63c38939a6a9582de8b561f3f5ac796</code> — the commit that contains all of these assets — so a link never silently changes. Images embed from `raw.githubusercontent.com`: the `blob` URL serves an HTML page, not the image (verified — `text/html` vs `image/gif`).

### ⚠️ Gate 27 — zero-floor assets: re-evaluation required

Domain 27 is the one asset group whose evidence chain is **not** closed. Four concrete flags, each checked against the files on disk:

| flag | evidence |
|---|---|
| **Producer/consumer lineage untracked** | `cpd_producer_inventory.md` and `cpd_consumer_inventory.md` contain **zero** `domain27` rows. The three producers (`generate_validation_artifacts.py`, `physics_integration.py`, `zero_floor_classification.py`) and their consumers are not registered, so no revision can be shown to keep up with them. |
| **Extraction report failed** | `pix2text_extraction_report.json` returns `'Page' object is not subscriptable` for all three PNGs it targets — the extraction did not complete. |
| **CPU/GPU baselines are single-revision** | `domain27_zero_floor_comparison.json` records norms for `complex64`/`complex128` and subnormal handling on an RTX A1000 6GB Laptop (CC 8.6). These are one-shot measurements, not a tracked baseline. |
| **Physics integration unreviewed** | `domain27_zero_floor_physics.json` (D27.3, 9,083 B) has no independent recomputation on record. |

**Required before Gate 27 can be called current:** register the Domain 27 producers/consumers in the inventories, re-run the failed pix2text extraction, re-measure the CPU/GPU baselines against the current tree, and independently recompute D27.3.

<details>
<summary>Gate 27 assets (2 GIFs, 13 PNGs)</summary>

| asset | |
|---|---|
| [gaussian_evolution.gif](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_current_evolution/gaussian_evolution.gif) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_current_evolution/gaussian_evolution.gif" width="300" alt="gaussian_evolution.gif"> |
| [vortex_evolution.gif](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/vortex_core_density_floor/vortex_evolution.gif) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/vortex_core_density_floor/vortex_evolution.gif" width="300" alt="vortex_evolution.gif"> |
| [classification_breakdown.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/energy_threshold_with_zero_floor/classification_breakdown.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/energy_threshold_with_zero_floor/classification_breakdown.png" width="300" alt="classification_breakdown.png"> |
| [cpu_vs_gpu_energy.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/energy_threshold_with_zero_floor/cpu_vs_gpu_energy.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/energy_threshold_with_zero_floor/cpu_vs_gpu_energy.png" width="300" alt="cpu_vs_gpu_energy.png"> |
| [energy_distribution.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/energy_threshold_with_zero_floor/energy_distribution.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/energy_threshold_with_zero_floor/energy_distribution.png" width="300" alt="energy_distribution.png"> |
| [fft_magnitude_spectrum.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/fft_numerical_zeros/fft_magnitude_spectrum.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/fft_numerical_zeros/fft_magnitude_spectrum.png" width="300" alt="fft_magnitude_spectrum.png"> |
| [fft_zero_components.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/fft_numerical_zeros/fft_zero_components.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/fft_numerical_zeros/fft_zero_components.png" width="300" alt="fft_zero_components.png"> |
| [phase_agreement.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/fft_numerical_zeros/phase_agreement.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/fft_numerical_zeros/phase_agreement.png" width="300" alt="phase_agreement.png"> |
| [gaussian_center.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_current_evolution/gaussian_center.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_current_evolution/gaussian_center.png" width="300" alt="gaussian_center.png"> |
| [gaussian_variance.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_current_evolution/gaussian_variance.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_current_evolution/gaussian_variance.png" width="300" alt="gaussian_variance.png"> |
| [gaussian_tail_abs_sq.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_tail_decay/gaussian_tail_abs_sq.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_tail_decay/gaussian_tail_abs_sq.png" width="300" alt="gaussian_tail_abs_sq.png"> |
| [tail_threshold_summary.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_tail_decay/tail_threshold_summary.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/gaussian_tail_decay/tail_threshold_summary.png" width="300" alt="tail_threshold_summary.png"> |
| [cpu_vs_gpu_density.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/vortex_core_density_floor/cpu_vs_gpu_density.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/vortex_core_density_floor/cpu_vs_gpu_density.png" width="300" alt="cpu_vs_gpu_density.png"> |
| [vortex_core_density.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/vortex_core_density_floor/vortex_core_density.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/vortex_core_density_floor/vortex_core_density.png" width="300" alt="vortex_core_density.png"> |

</details>

### Animations (GIF)

| asset | |
|---|---|
| [vortex_line_evolution.gif](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_evolution.gif) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_evolution.gif" width="360" alt="vortex_line_evolution.gif"> |
| [vortex_line_evolution_v2.gif](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_evolution_v2.gif) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_evolution_v2.gif" width="360" alt="vortex_line_evolution_v2.gif"> |
| [bec_ground_state_evolution.gif](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_evolution.gif) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_evolution.gif" width="360" alt="bec_ground_state_evolution.gif"> |

### 3D asset suite

| frame | |
|---|---|
| [vortex_line_frame_000.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_000.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_000.png" width="300" alt="vortex_line_frame_000.png"> |
| [vortex_line_frame_010.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_010.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_010.png" width="300" alt="vortex_line_frame_010.png"> |
| [vortex_line_frame_020.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_020.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_020.png" width="300" alt="vortex_line_frame_020.png"> |
| [vortex_line_frame_030.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_030.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_030.png" width="300" alt="vortex_line_frame_030.png"> |
| [vortex_line_frame_040.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_040.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/A_vortex_line/vortex_line_frame_040.png" width="300" alt="vortex_line_frame_040.png"> |
| [bec_ground_state_frame_100.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_frame_100.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_frame_100.png" width="300" alt="bec_ground_state_frame_100.png"> |
| [bec_ground_state_frame_200.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_frame_200.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_frame_200.png" width="300" alt="bec_ground_state_frame_200.png"> |
| [bec_ground_state_frame_300.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_frame_300.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/quantum_3d_asset_suite/B_bec_ground_state/bec_ground_state_frame_300.png" width="300" alt="bec_ground_state_frame_300.png"> |

### Validation artifacts (domains 1–18)

<details><summary>validation_artifacts/ (29 PNGs)</summary>

| asset | |
|---|---|
| [domain10_absorber_masks.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain10_absorber_masks.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain10_absorber_masks.png" width="260" alt="domain10_absorber_masks.png"> |
| [domain10_absorber_norm.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain10_absorber_norm.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain10_absorber_norm.png" width="260" alt="domain10_absorber_norm.png"> |
| [domain11_cpu_gpu.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain11_cpu_gpu.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain11_cpu_gpu.png" width="260" alt="domain11_cpu_gpu.png"> |
| [domain12_stability.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain12_stability.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain12_stability.png" width="260" alt="domain12_stability.png"> |
| [domain1_strang_1d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_1d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_1d.png" width="260" alt="domain1_strang_1d.png"> |
| [domain1_strang_1d_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_1d_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_1d_after.png" width="260" alt="domain1_strang_1d_after.png"> |
| [domain1_strang_2d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_2d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_2d.png" width="260" alt="domain1_strang_2d.png"> |
| [domain1_strang_2d_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_2d_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain1_strang_2d_after.png" width="260" alt="domain1_strang_2d_after.png"> |
| [domain2_hermiticity_1d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain2_hermiticity_1d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain2_hermiticity_1d.png" width="260" alt="domain2_hermiticity_1d.png"> |
| [domain3_norm_1d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_1d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_1d.png" width="260" alt="domain3_norm_1d.png"> |
| [domain3_norm_1d_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_1d_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_1d_after.png" width="260" alt="domain3_norm_1d_after.png"> |
| [domain3_norm_2d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_2d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_2d.png" width="260" alt="domain3_norm_2d.png"> |
| [domain3_norm_2d_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_2d_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_2d_after.png" width="260" alt="domain3_norm_2d_after.png"> |
| [domain3_norm_3d_slice.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_3d_slice.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_3d_slice.png" width="260" alt="domain3_norm_3d_slice.png"> |
| [domain3_norm_3d_slice_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_3d_slice_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain3_norm_3d_slice_after.png" width="260" alt="domain3_norm_3d_slice_after.png"> |
| [domain4_fourier_1d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain4_fourier_1d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain4_fourier_1d.png" width="260" alt="domain4_fourier_1d.png"> |
| [domain5_barrier_3d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_barrier_3d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_barrier_3d.png" width="260" alt="domain5_barrier_3d.png"> |
| [domain5_potential_1d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_potential_1d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_potential_1d.png" width="260" alt="domain5_potential_1d.png"> |
| [domain5_potential_2d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_potential_2d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_potential_2d.png" width="260" alt="domain5_potential_2d.png"> |
| [domain5_potential_3d_slice.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_potential_3d_slice.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain5_potential_3d_slice.png" width="260" alt="domain5_potential_3d_slice.png"> |
| [domain6_td_step0.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step0.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step0.png" width="260" alt="domain6_td_step0.png"> |
| [domain6_td_step1.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step1.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step1.png" width="260" alt="domain6_td_step1.png"> |
| [domain6_td_step10.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step10.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step10.png" width="260" alt="domain6_td_step10.png"> |
| [domain6_td_step5.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step5.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain6_td_step5.png" width="260" alt="domain6_td_step5.png"> |
| [domain7_convergence.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain7_convergence.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain7_convergence.png" width="260" alt="domain7_convergence.png"> |
| [domain8_energy_momentum.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain8_energy_momentum.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain8_energy_momentum.png" width="260" alt="domain8_energy_momentum.png"> |
| [domain9_vortex_1.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain9_vortex_1.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain9_vortex_1.png" width="260" alt="domain9_vortex_1.png"> |
| [domain9_vortex_gaussian.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain9_vortex_gaussian.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain9_vortex_gaussian.png" width="260" alt="domain9_vortex_gaussian.png"> |
| [domain9_vortex_pair.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain9_vortex_pair.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts/domain9_vortex_pair.png" width="260" alt="domain9_vortex_pair.png"> |

</details>

<details><summary>validation_artifacts_ext/ (20 PNGs)</summary>

| asset | |
|---|---|
| [domain13_gaussian_1d_width.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_1d_width.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_1d_width.png" width="260" alt="domain13_gaussian_1d_width.png"> |
| [domain13_gaussian_2d_aniso.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_2d_aniso.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_2d_aniso.png" width="260" alt="domain13_gaussian_2d_aniso.png"> |
| [domain13_gaussian_2d_aniso_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_2d_aniso_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_2d_aniso_after.png" width="260" alt="domain13_gaussian_2d_aniso_after.png"> |
| [domain13_gaussian_3d_slice.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_3d_slice.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_gaussian_3d_slice.png" width="260" alt="domain13_gaussian_3d_slice.png"> |
| [domain13_parseval.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_parseval.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain13_parseval.png" width="260" alt="domain13_parseval.png"> |
| [domain14_gaussian_vortex_superposition.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_gaussian_vortex_superposition.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_gaussian_vortex_superposition.png" width="260" alt="domain14_gaussian_vortex_superposition.png"> |
| [domain14_superposition_1d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_1d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_1d.png" width="260" alt="domain14_superposition_1d.png"> |
| [domain14_superposition_1d_after.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_1d_after.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_1d_after.png" width="260" alt="domain14_superposition_1d_after.png"> |
| [domain14_superposition_2d.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_2d.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_2d.png" width="260" alt="domain14_superposition_2d.png"> |
| [domain14_superposition_vortices.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_vortices.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain14_superposition_vortices.png" width="260" alt="domain14_superposition_vortices.png"> |
| [domain15_grid_translation.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain15_grid_translation.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain15_grid_translation.png" width="260" alt="domain15_grid_translation.png"> |
| [domain15_threshold_sensitivity.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain15_threshold_sensitivity.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain15_threshold_sensitivity.png" width="260" alt="domain15_threshold_sensitivity.png"> |
| [domain15_vortex_charges.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain15_vortex_charges.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain15_vortex_charges.png" width="260" alt="domain15_vortex_charges.png"> |
| [domain16_straight_vortex.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain16_straight_vortex.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain16_straight_vortex.png" width="260" alt="domain16_straight_vortex.png"> |
| [domain16_vortex_ring.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain16_vortex_ring.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain16_vortex_ring.png" width="260" alt="domain16_vortex_ring.png"> |
| [domain17_threshold_map.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain17_threshold_map.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain17_threshold_map.png" width="260" alt="domain17_threshold_map.png"> |
| [domain17_underflow.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain17_underflow.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain17_underflow.png" width="260" alt="domain17_underflow.png"> |
| [domain17_zero_taxonomy.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain17_zero_taxonomy.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain17_zero_taxonomy.png" width="260" alt="domain17_zero_taxonomy.png"> |
| [domain18_cpu_gpu_precision.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain18_cpu_gpu_precision.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain18_cpu_gpu_precision.png" width="260" alt="domain18_cpu_gpu_precision.png"> |
| [domain18_resolution_crosscheck.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain18_resolution_crosscheck.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/validation_artifacts_ext/domain18_resolution_crosscheck.png" width="260" alt="domain18_resolution_crosscheck.png"> |

</details>

### PKS egg-curve pages (rendered, 200 DPI)

| page | |
|---|---|
| [eikurve_p01.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p01.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p01.png" width="260" alt="eikurve_p01.png"> |
| [eikurve_p02.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p02.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p02.png" width="260" alt="eikurve_p02.png"> |
| [eikurve_p03.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p03.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p03.png" width="260" alt="eikurve_p03.png"> |
| [eikurve_p04.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p04.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p04.png" width="260" alt="eikurve_p04.png"> |
| [eikurve_p05.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p05.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p05.png" width="260" alt="eikurve_p05.png"> |
| [eikurve_p06.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p06.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p06.png" width="260" alt="eikurve_p06.png"> |
| [eikurve_p07.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p07.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p07.png" width="260" alt="eikurve_p07.png"> |
| [eikurve_p08.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p08.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p08.png" width="260" alt="eikurve_p08.png"> |
| [eikurve_p09.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p09.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p09.png" width="260" alt="eikurve_p09.png"> |
| [eikurve_p10.png](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p10.png) | <img src="https://raw.githubusercontent.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/1f75a65bb63c38939a6a9582de8b561f3f5ac796/pks_research_index/pks_eikurve_pages/eikurve_p10.png" width="260" alt="eikurve_p10.png"> |

</details>

---

## 1. How to read this repository

Every claim here carries one of four labels. A file without a label is not evidence.

| label | meaning |
|---|---|
| **VERIFIED** | reproduced from an executed probe or a read-only source examination in this workspace |
| **REPORTED** | taken from an earlier audit, commit message or conversation; not independently reproduced here |
| **INFERRED** | derived from verified material, with the derivation shown |
| **PENDING** | a scaffold or plan; **not** a result |

**Implemented ≠ tested ≠ accepted.** A script that runs is not a validated result.
A probe that passes is not a certified instrument. Nothing in this repository is
certified; the production library is explicitly *not yet certified*
(`cpd_final_audit.md` §6).

---

## 2. Layout

| path | role |
|---|---|
| `cpd_producer_inventory.md` | 234 producers — everything that creates scientifically meaningful information |
| `cpd_consumer_inventory.md` | 72 consumers — everything that reads or transforms producer output |
| `cpd_detached_inventory.md` | 8 detached modules (test-seeded reachability, not a name scan) |
| `cpd_relationship_graph.json` | 286 nodes · 1030 call edges · 323 import edges |
| `cpd_physics_validation_matrix.md` | 12 physics domains |
| `cpd_mathematical_validation_report.md` | mathematical synthesis |
| `cpd_defect_register.json` | 17 defects |
| `cpd_remediation_plan.md` | authorization-gated remediation |
| `cpd_final_audit.md` | the 2026-11-20 audit verdict |
| `cpd_rasidi_kingwen_lineage_2026-11-22.md` | consolidated Git authorship and lineage |
| `cpd_vortex_provenance_2026-11-22.md` | the two meanings of "vortex" |
| `cpd_schauberger_research_atlas_2026-11-22.md` | Schauberger/egg-geometry research seed |
| `evidence/`, `probes/` | probe sources and execution records |
| `nvidia_validation/` | CUDA residency, FFT, precision/zero-floor, memory, power, architecture |
| `quantum_3d_asset_suite/` | generated 3D assets (PLY/OBJ/PNG/GIF) from real physics |
| `pks_research_index/` | PKS historical + mathematical evidence (Wayback, equation audit) |
| `schauberger_sources_2026-11-22/` | retrieved source documents |

---

## 3. Current status (2026-11-22)

### 3.1 Production library

**Not yet certified.** 11 of 12 physics domains independently validated; the
remainder is concentrated in the legacy time-dependent-potential bridge, vortex
grid alignment, and documentation claims that contradict measured runtime
behaviour. Full detail: `cpd_final_audit.md`.

### 3.2 Vortex diagnostics — detector v3

The vortex-line animation is a **visualisation, not a topological verification**.
Detector v3 (`pks_research_index/quantum_vortex_detector_v3.json`,
`cpd_vortex_detector_v3_2026-11-22.py`) separates what the simulation demonstrates
from what it does not:

| diagnostic | result | label |
|---|---|---|
| D1 core depletion | axis density 0.063494 vs annulus 0.009062 — the imposed state has **no depleted core** | **FAIL_INITIAL_CONDITION** |
| D2 phase winding | +1 at radii 2/3/4/5, z = −2/0/+2, every step (two wall-contaminated readings at r=5) | **PASS_WITH_BOUNDARY_CAVEAT** |
| D3 blind localisation | exact at t=0 (error 0.0000); drifts 1.11–2.65 by step 40 | **INITIAL_CONDITION_VALIDATED_ONLY** |
| D4 circulation | Γ = h/m wherever winding is 1 | **PASS_WITH_INDEPENDENCE_CAVEAT** |
| full vortex-line evolution | — | **NOT_CERTIFIED** |

Two implementation defects were found and fixed along the way: the grid convention
(`dx = (hi−lo)/N`, so the origin is a node only for **even** N) and the localisation
method (a winding hit-list is a disc; the core is its centroid). The earlier
corner-minimum detector and its spurious windings are **superseded** — see
`pks_research_index/pks_vortex_detector_v3_2026-11-22.md`.

**Regularized state (2026-11-22).** The Gaussian state above is singular — its
amplitude is maximal on its own axis. The regular profile
`ψ = A·r⊥·exp(−(r⊥²+z²)/4σ²)·exp(iθ)` vanishes on the axis and closes two gates:

| diagnostic | gaussian | regularized |
|---|---|---|
| D1 core depletion | FAIL | **PASS** — axis ρ = 0.000000 vs annulus 0.016170, every frame |
| D2 winding = 1 | PASS with caveat | **PASS** — +1.000 at r = 2/3/4, both grids |
| D3 localisation | exact at t=0 only | exact at t = 0–20 (N=48); **still uncertified late** |
| D4 circulation | restated D2 | **independent velocity-field route**, Γ/(h/m) = 0.99–1.02 |

Artifact: `pks_research_index/pks_vortex_regularized_2026-11-22.md` and
`quantum_vortex_regularized.json`. Full evolution remains `NOT_CERTIFIED` — D3
degrades after step 20 and the circulation residual is ~1% at N=48.

**Gate 1 — D3 convergence (2026-11-22): FAILS its acceptance condition.** With an
independent reference (central local density minimum, no phase), the reference core
stays at **(0,0) for all 200 steps, all runs, all slices** — the vortex is stationary,
as a centred vortex in a symmetric trap should be. The winding-centroid detector
drifts to 1.2–2.6 grid units and gets **worse** at N=64 than N=48; halving dt changes
nothing, and `competing_minima = 1` throughout. Diagnosis: **detector bias** — the
±1 hit-list is a disc whose centroid is ill-conditioned, not physical motion and not
numerical instability. Winding around the detected core stays +1 at r = 3, 4.
Artifact: `pks_research_index/quantum_vortex_gate1_d3.json`,
`pks_vortex_gate1_d3_2026-11-22.md`.

### 3.3 PKS egg-curve mathematics

Recovered from the rendered PDF (byte-identical across the 2020/2024/2026 captures,
SHA-256 `ec4358df…`). Status of the equation audit:

| equation | status |
|---|---|
| EQ-03 | `ALGEBRAICALLY_VERIFIED` |
| EQ-07, EQ-08 | `ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS` |
| EQ-09 | `SIGN_CONVENTION_UNRESOLVED` (needs the page-8 diagram) |
| EQ-05 | `CLOSURE_PROVEN` |
| EQ-10 | `DISCREPANCY_PRESERVED` |

EQ-05 closure is analytic: both parameter-domain endpoints coincide at
`(0, 1.6018862051)`, the removable singularities at `cos φ = 0` give `r → 1/z₀ = 7/6`,
and the radicand is non-negative over the full domain.

EQ-10's three values are retained, not reconciled: printed equation **5.986907**,
closed-curve integral **7.736654**, source-stated **0.4045**. The page-8 diagram is
the next gate.

### 3.4 Open gates

- **Gate 27 assets need re-evaluation.** See the flagged block in the visual-assets
  dropdown at the top of this page: untracked producer/consumer lineage, a failed
  pix2text extraction, single-revision CPU/GPU baselines, unreviewed D27.3.
- **EQ-09** awaits the page-8 diagram of the Harthun/Rennert PDF.
- **EQ-10** volume discrepancy unresolved (5.986907 / 7.736654 / 0.4045).
- **Vortex-line evolution** is `NOT_CERTIFIED`. The regularized state closed D1
  (core depletion) and D4 (independent velocity-field circulation, ratio 0.99–1.02),
  but **Gate 1 failed**: D3 does not converge under refinement and the drift is
  detector bias, not physical motion — see §3.2.
- **Gate 2 — GPE stationarity** is `NOT_TESTED`. Separate gate, not started.

---

## 4. Provenance rules

- The published commit `6734d5a` is an **immutable baseline**. Later work is a
  follow-up commit; the baseline is never amended.
- Historical evidence is preserved, not overwritten. Superseded measurements stay
  on disk and are marked superseded.
- Missing measurements are recorded as missing. `cpd_independent_physics_validation.md`
  is a **PENDING** scaffold and must not be read as a completed validation.
- `.gitignore` excludes Python bytecode and caches. Four `__pycache__/*.pyc` files
  were tracked in the baseline `6734d5a`; they were **removed from the index in
  `1f75a65`** and are absent from `f0bd4c0`. The baseline commit itself is unchanged
  and still contains them — history is preserved, not rewritten.
- `cpd_certification_manifest.json` (v1.0, 72 files) is stale against the current
  tree. It is preserved unchanged; the current inventory is
  `cpd_certification_manifest_v2.json` (359 files). A manifest is a file listing,
  not a certification.
- No claim in this repository exceeds what an executed probe or a read-only source
  examination supports.

---

## 5. Related repositories

| repository | role |
|---|---|
| `Kbro1989/quantum-simulation` | production fork (QuantumLab) |
| `rasidi3112/quantum-simulation` | upstream; original 1D foundation and later physics expansion |
| `Kbro1989/archive-org-api-knowledge-base` | archival retrieval methodology (separate reference) |

---

<details>
<summary>🌐 &nbsp;Browser views — HTML &nbsp;·&nbsp; commit-pinned to <code>1f75a65</code></summary>

Open any of these in a browser. All are pinned to commit <code>1f75a65bb63c38939a6a9582de8b561f3f5ac796</code> and open on GitHub itself — no local server, no file path.

| view | what it is |
|---|---|
| [validation_index.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/nvidia_validation/domain27_zero_floor/validation_index.html) | Domain 27 zero-floor validation index |
| [schaubergerfiles_vortex.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/schaubergerfiles_vortex.html) | Schauberger vortex source page |
| [tudelft_thesis_record.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/tudelft_thesis_record.html) | TU Delft hyperbolic-funnel thesis record |
| [wolfram_coordinate_systems.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/wolfram_coordinate_systems.html) | Wolfram coordinate systems |
| [wolfram_vector_analysis.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/wolfram_vector_analysis.html) | Wolfram vector analysis |
| [arxiv_2108.04013_abs.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/arxiv_2108.04013_abs.html) | paper abstract — arxiv_2108.04013 |
| [arxiv_2211.01560_abs.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/arxiv_2211.01560_abs.html) | paper abstract — arxiv_2211.01560 |
| [arxiv_2607.22244_abs.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/arxiv_2607.22244_abs.html) | paper abstract — arxiv_2607.22244 |
| [arxiv_cond-mat_0102003_abs.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/arxiv_cond-mat_0102003_abs.html) | paper abstract — arxiv_cond-mat_0102003 |
| [patent_AT138296B.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/patent_AT138296B.html) | patent — patent_AT138296B |
| [patent_GB1084286A.html](https://github.com/Kbro1989/quantum-simulation-cpd-audit-2026-11-20/blob/1f75a65bb63c38939a6a9582de8b561f3f5ac796/schauberger_sources_2026-11-22/patent_GB1084286A.html) | patent — patent_GB1084286A |

Excluded: five `*_BLOCKED_js_challenge.html` files (`pks_ei-kurve`, `pks_ei-kurve_retry`,
`pks_patents`, `pks_viktor`, `pks_walter`) — those are the origin's JavaScript challenge
interstitials, not content.

</details>
