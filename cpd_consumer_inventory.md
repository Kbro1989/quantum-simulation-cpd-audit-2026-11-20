# QuantumLab — Consumer Inventory (CPD audit, 2026-11-20)

Repo: `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
Branch `remediation/2026-11-20`, HEAD `44f30e3`, clean tree.
Mode: strictly read-only on the repo; all probes were cheap CPU-only and run from the repo root.
Companion audit dir: `C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20`.

## 0. Definitions and method

- **Consumer** = a module-level public callable/class that reads, transforms, interprets or
  depends on producer output (wavefunction `psi`/`probability_density`, `grid`, `potential`,
  solver state, or a saved simulation artifact). Internal helpers are folded into their caller.
- **Preservation verdicts**: `VERIFIED` (meaning preserved; evidence cited), `PARTIAL`
  (preserved only under a stated condition), `LOSSY` (information destroyed/re-interpreted),
  `NOT_VERIFIED` (could not be checked without an expensive/GPU run).
- **Test coverage** cites `file:line`; `none` means no test references the qualified name.
- Line numbers are 1-based and refer to HEAD `44f30e3`.
- Probes actually executed are labelled `[probe]`; code-reading claims are labelled `[code]`.

- **Verification evidence.** The numerical findings L1-L7 were executed by the CPD audit
  (session `deleg_1c5a10e6`, 2026-11-20); supporting probes are stored in
  `evidence/probe_E_consumer_correctness_run.txt` and the subagent transcript
  `task-1.log`. The relationship-graph evidence for this inventory is
  `cpd_relationship_graph.json`.

**Total consumers inventoried: 72** (C01–C72).

---

## 1. Consumer inventory

### C01 `quantumlab.runner.SimulationRunner._validate_config` — quantumlab/runner.py:41
1. Identity: `SimulationRunner._validate_config(cfg, sim_name)`.
2. Producer inputs: the YAML `cfg` dict (loaded at runner.py:35-36). Reads keys
   `dimension, grid, wavefunction, potential, dt, num_steps` (runner.py:43).
3. Transformation: set-difference of required keys (runner.py:44).
4. Information handling: all other keys (`hbar`, `m`, `gpu`, `backend`, `solver`,
   `absorbing_boundary`, `snapshot_interval`, `log_interval`, `save_state`, `animation`)
   are accepted without validation; no type/range checks.
5. Output contract: `None`; raises `ValueError` listing missing keys (runner.py:46).
6. Preservation: **PARTIAL** — presence-only validation; `log_interval=0` later causes
   `ZeroDivisionError` at runner.py:169 `[code]`.
7. Test coverage: tests/test_runner.py:94-98 (`test_runner_missing_keys_raises`).

### C02 `quantumlab.runner.SimulationRunner._build_grid` — quantumlab/runner.py:48
1. Identity: `SimulationRunner._build_grid(dim, cfg)`.
2. Producer inputs: `cfg["N"]`, `cfg["L"]` (runner.py:51-52); for dim 3 also
   `Nx/Ny/Nz`, `Lx/Ly/Lz` (runner.py:58-59).
3. Transformation: `Grid1D(N,-L/2,L/2)` / `Grid2D(N,…,N,…)` / `Grid3D(...)` (runner.py:53-60).
4. Information handling: **dim 2 ignores `Nx/Ny` and forces a square grid** (runner.py:56);
   `N`/`L` cast with `int()`/`float()` (runner.py:51-52), truncating non-integral `N`.
5. Output contract: a `Grid1D/2D/3D` instance.
6. Preservation: **PARTIAL** — 2-D `Nx/Ny` silently dropped `[code]`.
7. Test coverage: tests/test_runner.py:55-62 (1D/2D/3D `N,L` path only).

### C03 `quantumlab.runner.SimulationRunner._build_wavefunction` — quantumlab/runner.py:63
1. Identity: `SimulationRunner._build_wavefunction(grid, cfg)`.
2. Producer inputs: `cfg["wavefunction"]` fields `x0,sigma,k0` (runner.py:66-67),
   `y0,k0_x,k0_y,sigma_y` (runner.py:77-81), `z0,k0_z,sigma_z` (runner.py:87-94).
3. Transformation: dispatches to `WaveFunction1D/2D/3D.gaussian` (runner.py:69-95).
4. Information handling: unknown wavefunction `type` is ignored — the key `wfc` is read but
   `wfc.get("type")` is never used; every config is treated as a Gaussian `[code]`.
5. Output contract: a normalized `WaveFunction*` (normalisation inside `gaussian`,
   core/wavefunction.py:35-39,72-78,129-138).
6. Preservation: **LOSSY** — `wavefunction.type` discarded; non-Gaussian configs impossible.
7. Test coverage: tests/test_runner.py:55-62 (1D/2D/3D Gaussian branches).

### C04 `quantumlab.runner.SimulationRunner._build_solver` — quantumlab/runner.py:98
1. Identity: `SimulationRunner._build_solver(grid, potential, cfg)`.
2. Producer inputs: `cfg["dt"]` (runner.py:100), `hbar` (101), `m` (102), `gpu` (103),
   `solver`, `order`, `nonlinearity`, `rotation`, `damping`, `backend` (105-113).
3. Transformation: constructs `SplitOperatorSolver` (106-113) or `SplitStep1D/2D/3DSolver`
   (115-117) or `SplitStep3DGPU` (120).
4. Information handling: **`gpu=True` is silently ignored when `solver='split_operator'`**
   (the `gpu` local at 103 is unused in the 105-113 branch; `backend` defaults to `"numpy"`).
   An unrecognised `solver` string falls through to the dim dispatch (114-121).
5. Output contract: a `Solver` instance.
6. Preservation: **LOSSY** — `gpu` flag dropped on the split-operator path; unknown solver
   names silently re-dispatched. `[probe]` config `gpu=True, solver='split_operator'` logged
   `[scipy-cpu]`.
7. Test coverage: tests/test_runner.py:66-72 (split_operator), 26-32/55-62 (gpu 3D path).

### C05 `quantumlab.runner.SimulationRunner.run` — quantumlab/runner.py:124
1. Identity: `SimulationRunner.run(sim_name=None)`.
2. Producer inputs: `self.config["simulations"]` (125); per-sim `cfg` (135-143);
   `cfg["absorbing_boundary"]` (145-148); `num_steps` (150); `snapshot_interval` (151);
   `log_interval` (169); `save_state` (181); `animation` (185-198).
3. Transformation: builds grid/potential/wf/solver (140-143), steps (161), applies ABL
   (162-163), snapshots (165-167), logs `E`,`<x>` (169-172), saves `.npz` (182), renders
   animation (186-198).
4. Information handling:
   - `E = total_energy_expectation(wf_current, potential)` (170) omits `hbar`/`m`; the
     observable defaults are `hbar=1.0, m=1.0` (expectation.py:170). `[probe]` with
     `hbar=2,m=3`: logged `E=2.125287`, true `E=2.833611`.
   - No norm division after `abl.apply` (163); `[probe]` free packet + ABL: norm `2e-6`,
     logged `E=6.6e-5` vs `E/norm=30.5`.
   - `potential` re-evaluation: `potential_energy_expectation` calls
     `potential.evaluate(grid)` (expectation.py:143) → for a time-dependent potential this is
     `V(t=0)` (time_dependent.py:23-24). `[probe]` DipoleDrive: `E(V0)=0.665055` vs
     `E(V(t))=0.612336`. Not reachable from `SimulationRunner` because `DipoleDrive` is not
     in `POTENTIAL_REGISTRY` (potentials/__init__.py:19-39).
   - `np.savez(..., params=cfg)` (182) pickles a dict; reader must use `allow_pickle=True`
     (tests/test_runner.py:90). Grid object not saved.
   - Animation branch `dim >= 2` (186) admits 3-D, but `WavePacketAnimator` is 2-D only
     (animation.py:51). `[probe]` 3-D `WavePacketAnimator._init_frame` → `TypeError: Invalid
     shape (16, 16, 16) for image data`.
5. Output contract: `results[name] = {final_wavefunction, snapshots, snap_times, config}`
   (174-179); optional `{name}_state.npz` (182); optional `{name}_evolution.{mp4|gif}` (196).
6. Preservation: **LOSSY** — energy/`<x>` logs wrong for `hbar≠1`/`m≠1`, after absorption,
   and for time-dependent potentials; 3-D animation crashes; `wavefunction.type` ignored.
7. Test coverage: tests/test_runner.py:55-103 (all branches except animation, ABL, and
   `hbar/m≠1`).

### C06 `quantumlab.observables.expectation.position_expectation` — expectation.py:4
1. Identity: `position_expectation(wf)`.
2. Producer inputs: `wf.probability_density` (5), `wf.grid.x|X` (7,9,11), `dx` (7-11).
3. Transformation: `float(np.sum(coord*prob)*dV)` per dimension (6-11).
4. Information handling: no norm division; `prob` is `|psi|²` (core/wavefunction.py:16,53,92).
5. Output contract: printed/logged float (runner.py:171-172).
6. Preservation: **PARTIAL** — correct only for `‖psi‖=1`; after ABL the value is scaled by
   the norm `[probe]` (`<x>_logged=2e-6` vs `<x>/norm=0.892`).
7. Test coverage: tests/test_observables.py:7-21; tests/test_3d_observables.py:24-31.

### C07 `position_squared_expectation` — expectation.py:15
1-3. Reads `prob` (16), `grid.x|X` (18,20,22); `sum(coord²·prob)·dV`.
4. No norm division.
5. Float.
6. **PARTIAL** (same norm condition as C06).
7. tests/test_3d_observables.py:24-31 (indirect via uncertainty).

### C08 `position_uncertainty` — expectation.py:26
1-3. Calls C06/C07 (27-28); `sqrt(max(var,0))` (30).
4. `max(variance,0)` clamps negative round-off (30).
5. Float.
6. **VERIFIED** for normalised states; `max(...,0)` hides negative-variance round-off.
7. tests/test_observables.py:7-21; tests/test_3d_observables.py:24-31.

### C09 `y_expectation` — expectation.py:32
1-3. Reads `prob` (33), `grid.Y` (35,37); `sum(Y·prob)·dx·dy`.
4. No norm division; raises `ValueError` for 1-D (39).
5. Float.
6. **PARTIAL**.
7. tests/test_3d_observables.py:24-31; tests/test_rotation.py:9,198.

### C10 `y_squared_expectation` — expectation.py:41
Same pattern as C07 with `grid.Y` (44,46). **PARTIAL**. tests/test_3d_observables.py:24-31.

### C11 `y_uncertainty` — expectation.py:50
Calls C09/C10 (51-52); `sqrt(max(var,0))` (54). **VERIFIED** (normalised). tests/test_3d_observables.py:24-31; tests/test_rotation.py:198.

### C12 `z_expectation` — expectation.py:56
Reads `prob` (58), `grid.Z` (59); 3-D only (61). No norm division. **PARTIAL**.
tests/test_3d_observables.py:24-31.

### C13 `z_squared_expectation` — expectation.py:63
Same pattern with `grid.Z` (66). **PARTIAL**. tests/test_3d_observables.py:24-31.

### C14 `z_uncertainty` — expectation.py:70
Calls C12/C13 (71-72); `sqrt(max(var,0))` (74). **VERIFIED** (normalised).
tests/test_3d_observables.py:24-31.

### C15 `momentum_expectation` — expectation.py:76
1. Identity: `momentum_expectation(wf, direction='x', hbar=1.0)`.
2. Producer inputs: `wf.fourier_transform()` (77), `wf.grid.k|K_x|K_y|K_z` (82,86-88,94-98),
   `dk` (83,91,101).
3. Transformation: `sum(p·|phi|²)·dk` (83,91,101).
4. Information handling: no norm division; `phi` includes the `dx/√(2π)` factor
   (core/wavefunction.py:29,66,105). Direction validation (80-81,89-90,99-100).
5. Output contract: float.
6. **PARTIAL** — correct only for `‖psi‖=1`.
7. tests/test_observables.py:7-21; tests/test_3d_observables.py:34-45.

### C16 `momentum_squared_expectation` — expectation.py:105
Same pattern with `p²=(hbar·k)²` (111,115-117,123-127). **PARTIAL**.
tests/test_3d_observables.py:34-45 (indirect).

### C17 `momentum_uncertainty` — expectation.py:134
Calls C15/C16 (135-136); `sqrt(max(var,0))` (138). **VERIFIED** (normalised).
tests/test_observables.py:7-21; tests/test_3d_observables.py:34-45.

### C18 `potential_energy_expectation` — expectation.py:140
1. Identity: `potential_energy_expectation(wf, potential)`.
2. Producer inputs: `potential.evaluate(wf.grid)` (143), `wf.probability_density` (144),
   `grid.dx|dx·dy|dx·dy·dz` (146,148,150).
3. Transformation: `float(sum(V·prob)·dV)` (146,148,150).
4. Information handling: **re-evaluates the potential at `t=0`** for time-dependent
   potentials (time_dependent.py:23-24); no norm division; `potential=None` → `0.0` (141-142).
5. Output contract: float.
6. **LOSSY** for time-dependent `V` (wrong time) and for `‖psi‖≠1` (scaled) `[probe]`.
7. tests/test_conjugate_gradient.py:9; tests/test_gross_pitaevskii.py:9; tests/test_multicomponent.py:9.

### C19 `kinetic_energy_expectation` — expectation.py:154
1. Identity: `kinetic_energy_expectation(wf, hbar=1.0, m=1.0)`.
2. Producer inputs: C16 per axis (156-166).
3. Transformation: `mean_p2/(2m)` summed over axes (157,161,166).
4. Information handling: `hbar`/`m` default to 1 (154); no norm division.
5. Output contract: float.
6. **PARTIAL** — wrong if caller omits `hbar`/`m` (this is the runner defect, C05).
7. tests/test_conjugate_gradient.py:9; tests/test_gross_pitaevskii.py:9; tests/test_multicomponent.py:9.

### C20 `total_energy_expectation` — expectation.py:170
1. Identity: `total_energy_expectation(wf, potential, hbar=1.0, m=1.0)`.
2. Producer inputs: C19 (171), C18 (172).
3. Transformation: `T_exp + V_exp` (173).
4. Information handling: defaults `hbar=m=1` (170); no norm division; `V` at `t=0`.
5. Output contract: float (logged at runner.py:170).
6. **LOSSY** — `[probe]` runner with `hbar=2,m=3`: logged `2.125287` vs true `2.833611`.
7. tests/test_2d_solver.py; tests/test_3d_solver.py; tests/test_3d_gpu_solver.py;
   tests/test_rotation.py:9,68,83; tests/test_solvers.py; tests/test_split_operator.py:12.

### C21 `transmission_coefficient` — coefficients.py:4
1. Identity: `transmission_coefficient(wf, barrier_position=0.0)`.
2. Producer inputs: `wf.probability_density` (5), `wf.grid.x|X` (7,10,13), `dx` (8,11,14).
3. Transformation: `float(sum(prob[mask])·dV)` with `mask = coord >= barrier_position` (7-14).
4. Information handling: no norm division → returns the norm fraction, not a probability.
5. Output contract: float.
6. **PARTIAL** — test explicitly asserts `T+R == wf.norm()` (tests/test_3d_observables.py:67),
   i.e. the "coefficient" is un-normalised.
7. tests/test_3d_observables.py:63-69.

### C22 `reflection_coefficient` — coefficients.py:18
Same pattern with `mask = coord < barrier_position` (21-28). **PARTIAL**.
tests/test_3d_observables.py:63-69.

### C23 `get_momentum_wavefunction` — momentum.py:4
1. Identity: `get_momentum_wavefunction(wf)`.
2. Producer inputs: `wf.fourier_transform()` (5), `wf.grid.k_x|k_y|k_z|k` (7-19).
3. Transformation: `np.fft.fftshift` on grids and `phi` (7-19).
4. Information handling: returns shifted `k` meshes and shifted `phi`; no copy of `phi`
   (`fftshift` returns a new array).
5. Output contract: `((kx,ky[,kz]), phi_shifted)`.
6. **VERIFIED** (pure re-indexing).
7. Test coverage: **none** (only `get_momentum_probability_density` is imported by tests).

### C24 `get_momentum_probability_density` — momentum.py:22
1. Identity: `get_momentum_probability_density(wf)`.
2. Producer inputs: C23 (24,27,30), `|phi|²` (25,28,31).
3. Transformation: `np.abs(phi)**2`.
4. Information handling: none beyond C23.
5. Output contract: `((kx,ky[,kz]), prob_k)`.
6. **VERIFIED**.
7. tests/test_3d_observables.py:72-80 (Parseval check).

### C25 `interaction_energy` — nonlinear.py:6
1. Identity: `interaction_energy(wf, nonlinearity)`.
2. Producer inputs: `wf.probability_density` (8), `volume_element(wf.grid)` (8).
3. Transformation: `0.5·g·sum(rho²)·dV` (8).
4. Information handling: no norm division (correct: energy of the actual state).
5. Output contract: float.
6. **VERIFIED**.
7. tests/test_conjugate_gradient.py:9; tests/test_gross_pitaevskii.py:9.

### C26 `gross_pitaevskii_energy` — nonlinear.py:11
1. Identity: `gross_pitaevskii_energy(wf, potential, nonlinearity, hbar=1.0, m=1.0)`.
2. Producer inputs: C19 (13), C18 (13), C25 (14).
3. Transformation: sum of the three terms (13-14).
4. Information handling: `hbar`/`m` default 1; no norm division.
5. Output contract: float.
6. **PARTIAL**.
7. tests/test_gross_pitaevskii.py:9; tests/test_rotation.py:10,108.

### C27 `chemical_potential` — nonlinear.py:17
Same inputs as C26; `T+V+2·E_int` (19-20). **PARTIAL**.
tests/test_gross_pitaevskii.py:9; tests/test_multicomponent.py:9.

### C28 `coupled_gp_energy` — nonlinear.py:23
1. Identity: `coupled_gp_energy(states, potentials, couplings, hbar=1.0, m=1.0)`.
2. Producer inputs: `states[i].probability_density` (32), `potentials[i]` via C18 (30-31),
   `volume_element(states[0].grid)` (29), `couplings` (28).
3. Transformation: `Σ_i(⟨T⟩+⟨V⟩) + ½Σ_ij g_ij∫n_i n_j` (30-34).
4. Information handling: `g = np.asarray(couplings, dtype=float)` (28) — a complex coupling
   would warn/discard; no norm division.
5. Output contract: float.
6. **PARTIAL**.
7. tests/test_multicomponent.py:9.

### C29 `miscibility_overlap` — nonlinear.py:38
1. Identity: `miscibility_overlap(wf_a, wf_b)`.
2. Producer inputs: `wf_a.probability_density`, `wf_b.probability_density` (43).
3. Transformation: `sum(n_a n_b)/sqrt(sum(n_a²)·sum(n_b²))` (44).
4. Information handling: `dV` cancels (dimensionless ratio); no norm division needed.
5. Output contract: float in `[0,1]`.
6. **VERIFIED**.
7. tests/test_multicomponent.py:122.

### C30 `gradient` — current.py:11
1. Identity: `gradient(psi, grid)`.
2. Producer inputs: `psi` (13), `wavevectors(grid)` (14).
3. Transformation: `ifftn(1j·K·fftn(psi))` per axis (13-14).
4. Information handling: spectral derivative; truncated to grid dimension (12-14).
5. Output contract: tuple of derivative arrays.
6. **VERIFIED**.
7. Test coverage: **none direct** (used internally by C31/C32; tests exercise it indirectly).

### C31 `probability_current` — current.py:17
1. Identity: `probability_current(wf, hbar=1.0, m=1.0)`.
2. Producer inputs: `wf.psi` (22), C30 (23), `wf.grid` (23).
3. Transformation: `(hbar/m)·Im(conj(psi)·d)` (23).
4. Information handling: `hbar`/`m` default 1; no norm division (current density).
5. Output contract: tuple of current arrays.
6. **VERIFIED** for `hbar=m=1`; **PARTIAL** otherwise.
7. tests/test_new_potentials_and_observables.py:84-96.

### C32 `angular_momentum_z_expectation` — current.py:26
1. Identity: `angular_momentum_z_expectation(wf, hbar=1.0)`.
2. Producer inputs: `wf.grid` (28), C30 (30), `wf.grid.X|Y` (31), `wf.psi` (32),
   `volume_element` (32).
3. Transformation: `-i·hbar·(X·∂_y − Y·∂_x)` (31); `Re(sum(conj(psi)·Lz_psi)·dV)` (32).
4. Information handling: `hbar` defaults 1; no norm division; 2-D/3-D only (28-29).
5. Output contract: float.
6. **PARTIAL** (norm condition).
7. tests/test_new_potentials_and_observables.py:99-104; tests/test_rotation.py:9,58,110,140;
   tests/test_conjugate_gradient.py:9.

### C33 `autocorrelation` — current.py:35
1. Identity: `autocorrelation(psi0, psi_t, grid)`.
2. Producer inputs: `psi0`, `psi_t` (37), `volume_element(grid)` (37).
3. Transformation: `complex(sum(conj(psi0)·psi_t)·dV)` (37).
4. Information handling: no norm division (overlap amplitude).
5. Output contract: complex.
6. **VERIFIED**.
7. tests/test_new_potentials_and_observables.py:107-124; tests/test_rotation.py:10,55.

### C34 `vortex_positions` — current.py:40
1. Identity: `vortex_positions(wf, min_density=0.2, smoothing=1.0)`.
2. Producer inputs: `wf.grid` (63-65), `wf.psi` (66), `wf.probability_density` (74).
3. Transformation: `phase=angle(psi)` (66); plaquette circulation from wrapped node-phase
   differences (71-72); `charge=rint(circ/2π)` (73); `rho=gaussian_filter(prob,
   sigma=(smoothing/dx, smoothing/dy))` (74); `keep=(charge!=0)&(rho[:-1,:-1] >
   min_density·rho.max())` (75); `positions=column_stack([x[i]+dx/2, y[j]+dy/2])` (77).
4. Information handling:
   - **Grid-alignment-dependent winding**: the discrete sum uses node phases only.
     `[probe]` single vortex at a grid node `(0,0)` → 0 plaquettes, circulation exactly
     `0.0000`; at `(0.125,0)` (half-cell) → 0; at `(0.0625,0.0625)` (quarter-cell) →
     one plaquette, circulation `6.2832`. With the repo test's own centres
     `(-2.0,1.0)`/`(2.5,-1.5)` (both grid nodes) a *single* vortex is missed (`n=0`), and
     `(0.5,2.5)` yields **two** plaquettes both charge `-1`.
   - **Threshold at the plaquette corner, not the neighbourhood**: `rho[:-1,:-1]` (75) is
     the lower-left node value. `[probe]` off-grid vortex at `(3.0625,0.0625)` in a compact
     condensate: core/max smoothed density `0.1870 < 0.2` → dropped by the default, found
     with `min_density=0.0`.
   - Positions are plaquette centres, so a detected vortex is reported up to half a cell
     from the true core (test centres are reported at `±0.0625`).
5. Output contract: `(positions (n,2), charges (n,))`.
6. Preservation: **LOSSY** — vortices missed/duplicated depending on grid alignment; real
   cores in dilute regions masked by the default `min_density`.
7. Test coverage: tests/test_new_potentials_and_observables.py:127-140 (only off-grid,
   multi-vortex, tolerance `dx` — does not exercise the defects).

### C35 `plot_wavefunction_1d` — plots_1d.py:7
1. Identity: `plot_wavefunction_1d(wf, potential=None, title=…, save_path=None, show=True, theme='light')`.
2. Producer inputs: `wf.grid.x` (10), `wf.probability_density` (11), `np.real(wf.psi)` (12),
   `potential.evaluate(wf.grid)` (14).
3. Transformation: `scale_factor = 0.5·max_prob/max_v` (18); `V·scale_factor` (20-21).
4. Information handling: **potential is rescaled into probability units** (18-21) and
   `Re(ψ)` is plotted on the same axis as `|ψ|²` (24-26) — mixed units; the y-axis label
   `"Amplitude / Probability Density"` (29) admits the ambiguity.
5. Output contract: matplotlib figure; optional `savefig` (34); `plt.show()` (36).
6. Preservation: **LOSSY** (visual unit change; documented only by the legend "scaled").
7. Test coverage: **none**.

### C36 `plot_dual_space_1d` — plots_1d.py:40
1. Identity: `plot_dual_space_1d(...)`.
2. Producer inputs: `wf.grid.x` (43), `wf.probability_density` (44), C24 (52).
3. Transformation: two panels; `k,prob_k = get_momentum_probability_density(wf)` (52).
4. Information handling: none beyond C23/C24.
5. Output contract: figure; `savefig` (63); `show` (65).
6. **VERIFIED**.
7. Test coverage: **none**.

### C37 `plot_density_2d` — plots_2d.py:8
1. Identity: `plot_density_2d(wf, potential=None, …)`.
2. Producer inputs: `wf.grid.x|y` (39-40), `wf.probability_density.T` (41),
   `potential.evaluate(wf.grid).T` (51).
3. Transformation: `imshow` with `extent` (43-48); optional `LogNorm` (44-45); contour of
   normalised `V` (52-54).
4. Information handling: `V_norm=(V-V.min())/(V.max()-V.min()+1e-30)` (52) — the potential
   overlay is normalised per frame, so its absolute scale is discarded; `1e-30` guards /0.
5. Output contract: figure; `savefig` (64); `show` (66).
6. **PARTIAL** (V scale discarded by design).
7. Test coverage: **none**.

### C38 `plot_density_snapshots_2d` — plots_2d.py:71
1. Identity: `plot_density_snapshots_2d(wf_list, times, potential=None, ncols=4, …)`.
2. Producer inputs: `wf_list[i].probability_density.T` (108), `wf_list[0].grid.x|y` (101-102),
   `potential.evaluate(wf.grid).T` (113).
3. Transformation: shared `global_max` (99); `imshow` per frame (109-111); contour (116).
4. Information handling: **all frames are drawn with `wf_list[0]`'s grid extent** (101-103);
   if snapshots use different grids the axes are silently wrong. `V_norm` per frame (114).
   Empty `wf_list` → `i` unbound at line 122.
5. Output contract: figure; `savefig` (128); `show` (130).
6. **PARTIAL**.
7. Test coverage: **none**.

### C39 `plot_orthogonal_slices_3d` — plots_2d.py:135
1. Identity: `plot_orthogonal_slices_3d(wf3d, potential=None, …)`.
2. Producer inputs: `wf3d.grid` (156), `wf3d.probability_density` (162), `grid.N_x|N_y|N_z`
   (157-159,165-170), `potential` (via panels).
3. Transformation: centroid from index-weighted probability (165-167); slices
   `prob[:,:,cz].T`, `prob[:,cy,:].T`, `prob[cx,:,:].T` (172-174); `global_max` (176).
4. Information handling: centroid uses **integer index space**, not physical coordinates
   (165-167) — for unequal `dx,dy,dz` the centroid is biased; slices are transposed for
   `imshow` (correct for `indexing='ij'` grids, core/grid.py:34,71).
5. Output contract: 3-panel figure; `savefig` (205); `show` (207).
6. **PARTIAL** (index-space centroid).
7. Test coverage: **none**.

### C40 `plot_space_time_3d` — plots_3d.py:5
1. Identity: `plot_space_time_3d(grid, t_arr, space_time_data, x_range=None, …)`.
2. Producer inputs: `grid.x` (9), `t_arr` (18), `space_time_data` (14,17).
3. Transformation: optional `x_range` boolean slice (10-14); `meshgrid(x_plot,t_arr)` (18);
   `plot_surface` (20).
4. Information handling: assumes `space_time_data` is `(n_times, N_x)`; a 1-D input would
   fail at `[:, indices]` (14). No shape validation.
5. Output contract: 3-D surface figure; `savefig` (37); `show` (39).
6. **PARTIAL**.
7. Test coverage: **none**.

### C41 `quantumlab.visualization.animation.WavePacketAnimator` — animation.py:13
1. Identity: `WavePacketAnimator(wf_series, times, grid, potential=None, theme='dark', log_scale=False, fps=30)` (18).
2. Producer inputs: `wf_series[i].probability_density` (42,45,51,78), `grid.x|y` (52-53),
   `potential.evaluate(grid)` (62), `times` (72,80).
3. Transformation: global colour scale over all frames (42-47); `density.T` (51,78);
   `imshow` (55-59); potential contour (65-66); `FuncAnimation` (87-92); FFMpeg/Pillow writer
   (94-101).
4. Information handling:
   - **2-D only**: `density = probability_density.T` (51) and `imshow` (55). `[probe]` a 3-D
     `WaveFunction3D` gives `TypeError: Invalid shape (16, 16, 16) for image data`; runner.py:186
     nevertheless calls this for `dim >= 2`.
   - `global_min` (43-47) raises `ValueError` if any frame has no positive density; all-zero
     frames break the animation.
   - Uses `self.grid` for every frame (52-53) — mixed-grid series are silently misaligned.
5. Output contract: `{name}_evolution.{mp4|gif}` (runner.py:196); prints
   `"Animation saved: …"` (105).
6. Preservation: **LOSSY** for 3-D input (crash) and mixed-grid series.
7. Test coverage: **none**.

### C42 `extract_isosurface` — volume_3d.py:35
1. Identity: `extract_isosurface(field, level, grid, step_size=1)`.
2. Producer inputs: `field` (43,46), `grid.dx|dy|dz` (45), `grid.x|y|z[0]` (47).
3. Transformation: `marching_cubes(field, level, spacing)` (46); `verts += origin` (47);
   face normals (49-50).
4. Information handling: returns `None` when `level` is outside the field range (43-44);
   normals divided by `norm + 1e-30` (50).
5. Output contract: `(verts, faces, normals)` or `None`.
6. **VERIFIED**.
7. tests/test_volume_3d.py:20-29.

### C43 `IsosurfaceRenderer` — volume_3d.py:64
1. Identity: `IsosurfaceRenderer(grid, levels=(0.5,0.15,0.03), alphas=None, color_by='phase', reference_peak=None, potential=None, potential_level=0.5, theme='dark', step_size=1, …)` (87).
2. Producer inputs: `grid` (93-95), `potential.evaluate(grid)` (112), `psi` passed to `draw`
   (167,193-194).
3. Transformation: levels sorted descending (98); alphas default `linspace(0.9,0.18,n)` (100);
   potential mesh at `V.min()+potential_level·(V.max()-V.min())` (114); per-level marching cubes
   (209); phase colours via `_sample_phase` at face centroids (214-215); Lambert shading (120-123).
4. Information handling:
   - `_sample_phase` (54-61) trilinearly interpolates `Re/Im` then `arctan2`; across the
     `±π` branch cut this silently produces wrong phase (no unwrapping).
   - `reference_peak=None` → per-frame peak (195), so levels are not comparable across frames
     unless the caller passes the global peak.
   - `V.max() > V.min()` guard (113) skips a flat potential silently.
5. Output contract: matplotlib figure (`draw`, 231); `save` writes PNG (233-238).
6. **PARTIAL** (phase interpolation; per-frame scale default).
7. tests/test_volume_3d.py:43-48,81-89.

### C44 `IsosurfaceAnimation` — volume_3d.py:246
1. Identity: `IsosurfaceAnimation(output_path, grid, n_frames, fps=20, dpi=100, elev=22, azim_start=-60, orbit_degrees=90, …)` (261).
2. Producer inputs: `grid` (275), `psi` per `add_frame` (290-295), `n_frames` (291).
3. Transformation: camera orbit `frac = frames_written/max(n_frames-1,1)` (291);
   `azim = azim_start + orbit_degrees·frac` (292); `elev` lerp (293); `renderer.draw` (294);
   `writer.grab_frame` (296).
4. Information handling: frames beyond `n_frames` are not rejected; `n_frames=1` → `max(…,1)`
   guard (291). Writer chosen by suffix (277-283).
5. Output contract: MP4/GIF at `output_path`; `frames_written` counter (284,297).
6. **VERIFIED**.
7. tests/test_volume_3d.py:51-58.

### C45 `animate_isosurfaces` — volume_3d.py:305
1. Identity: `animate_isosurfaces(snapshots, times, grid, output_path, …, fixed_scale=True, …)` (305).
2. Producer inputs: `snapshots` (318,323), `times` (323), `grid` (320).
3. Transformation: `fixed_scale` sets `reference_peak = max(|s|²)` (317-318); streams frames
   through `IsosurfaceAnimation` (320-324).
4. Information handling: `fixed_scale=True` is the default, so levels are comparable; progress
   prints every 10 frames (325-326).
5. Output contract: `Path(output_path)` (327).
6. **VERIFIED**.
7. tests/test_volume_3d.py:61-65.

### C46 `export_interactive_html` — volume_3d.py:330
1. Identity: `export_interactive_html(snapshots, times, grid, output_path, level=0.1, stride=2, title=…)` (330).
2. Producer inputs: `snapshots` (346,349,361), `times` (361), `grid` (343-345).
3. Transformation: builds a sub-grid (343-345); `peak = max(|s|²)` (346); `psi[::stride,…]`
   (349); `extract_isosurface(|psi|², level·peak, sub)` (350); `_sample_phase(psi, verts, sub)`
   (354); Plotly `Mesh3d` frames (355-361).
4. Information handling: **sub-grid spacing mismatch** — `sub = Grid3D(len(x[::stride]), x[0],
   x[0]+L_x, …)` (343-345) gives `dx_sub = L/ceil(N/stride)`, which equals `stride·dx` only
   when `stride | N`. `[probe]` `N=25, stride=2`: true `dx=0.320000`, `stride·dx=0.640000`,
   `sub.dx=0.615385` (≈4 % axis error), and the last sample is `3.680` vs sub-grid `3.385`.
   Phase is then sampled on the wrong grid (354).
5. Output contract: HTML file with Plotly CDN (376).
6. **PARTIAL** (axis scaling for non-dividing stride).
7. tests/test_volume_3d.py:68-72 (uses `stride=1`, which hides the defect).

### C47 `set_style` — style.py:3
1. Identity: `set_style(theme='light')`.
2. Producer inputs: none (mutates `plt.rcParams`).
3. Transformation: `plt.style.use` + `rcParams.update` (4-11).
4. Information handling: global matplotlib state; `theme` other than `'dark'` falls back to
   `'default'` (9-11) without warning.
5. Output contract: `None`.
6. **VERIFIED**.
7. Test coverage: **none** (exercised indirectly by every plot test).

### C48 `cupy_available` — backends.py:22
1. Identity: `cupy_available()`.
2. Producer inputs: `cupy.cuda.runtime.getDeviceCount()` (25-26).
3. Transformation: `try/except` → bool (24-28).
4. Information handling: swallows all exceptions (27-28).
5. Output contract: bool.
6. **VERIFIED**.
7. tests/test_backends.py:19,149,155.

### C49 `numpy_backend` — backends.py:31
1. Identity: `numpy_backend(workers=-1)`.
2. Producer inputs: none.
3. Transformation: builds `ArrayBackend(name='scipy-cpu', xp=np, fftn/ifftn=partial(scipy.fft…,
   workers, overwrite_x=True), to_device=np.asarray, to_host=np.asarray)` (33-40).
4. Information handling: **`to_host=np.asarray` returns the same object (no copy)** (39);
   `overwrite_x=True` (36-37) permits the FFT to destroy its input.
5. Output contract: `ArrayBackend`.
6. **PARTIAL** (aliasing / in-place overwrite contract).
7. Test coverage: **none direct** (reached only via `get_backend('numpy')`).

### C50 `cupy_backend` — backends.py:43
1. Identity: `cupy_backend(device_id=0)`.
2. Producer inputs: `cupy.cuda.runtime.getDeviceCount()` (46), `cupy.cuda.Device(device_id)` (49).
3. Transformation: validates `device_id` (47-48); builds `ArrayBackend(name='cupy', xp=cupy,
   fftn/ifftn=cupyx.scipy.fft…, to_device=cupy.asarray, to_host=cupy.asnumpy)` (50-57).
4. Information handling: `cupy.asarray`/`cupy.asnumpy` are true host↔device copies (55-56).
5. Output contract: `ArrayBackend`.
6. **VERIFIED**.
7. tests/test_backends.py:155-165 (real CuPy path, skipif no device).

### C51 `get_backend` — backends.py:60
1. Identity: `get_backend(backend='numpy', workers=-1, device_id=0)`.
2. Producer inputs: the `backend` spec (69-79).
3. Transformation: passes through `ArrayBackend` (69-70); `'numpy'`→C49 (71-72);
   `'cupy'`→C50 or `RuntimeError` (73-76); `'auto'`→C50 if available else C49 (77-78);
   else `ValueError` (79).
4. Information handling: `'auto'` silently degrades to CPU (78).
5. Output contract: `ArrayBackend`.
6. **VERIFIED**.
7. tests/test_backends.py:145-152.

### C52 `apply_hamiltonian` — stationary/hamiltonian.py:6
1. Identity: `apply_hamiltonian(psi, grid, V, hbar=1.0, m=1.0, nonlinearity=0.0, workers=-1, rotation=0.0)` (6).
2. Producer inputs: `psi` (14-17), `grid` (13,19-21), `V` (16-17), `hbar`, `m`, `g`, `rotation`.
3. Transformation: `T_k = hbar²k²/2m` (13); `H_psi = ifftn(T_k·fftn(psi))` (14-15);
   `V_eff = V + g|psi|²` if `g≠0` (16); `H_psi += V_eff·psi` (17); rotation term
   `-rotation·(-i hbar (X∂_y − Y∂_x)psi)` (18-22).
4. Information handling: `V` is expected N-D; a 1-D `V` on an N-D grid would broadcast
   silently (no shape check). Rotation on a 1-D grid raises `AttributeError` (`grid.K_x`).
5. Output contract: complex array `H_psi`.
6. **PARTIAL** (no shape validation).
7. tests/test_stationary.py:33-36; tests/test_rotation.py:126.

### C53 `eigenstates` — stationary/eigensolver.py:17
1. Identity: `eigenstates(grid, potential, n_states=6, hbar=1.0, m=1.0, tol=None, max_iter=1000, seed=0, method='auto', workers=-1)` (17).
2. Producer inputs: `grid` (44-48), `potential.evaluate(grid)` (47), `hbar`, `m`, `n_states`.
3. Transformation: matrix-free `LinearOperator` (54-60); `method='auto'` → lanczos below
   20000 points (62-63); `eigsh`/`lobpcg` (66,86); sort (94-96); normalise
   `psi /= sqrt(sum(psi²)·dV)` (102-103); fix global sign (105-107).
4. Information handling:
   - `V = np.asarray(potential.evaluate(grid), dtype=float)` (47) — **complex `V` is cast
     with a `ComplexWarning`, silently discarding the imaginary part** `[probe: numpy
     np.asarray(complex, dtype=float) → ComplexWarning + real part]`.
   - `matvec`/`precondition` take `.real` of the inverse FFT (57,74) — imaginary part of a
     complex trial vector is discarded; the operator is declared `dtype=float` (60,77).
   - LOBPCG residual check warns but still returns (88-90).
5. Output contract: `(energies (n_states,), states [WaveFunction])` (109).
6. **PARTIAL** (complex potentials silently truncated).
7. tests/test_stationary.py:14-44; tests/test_strongfield.py:33-37.

### C54 `ground_state_pcg` — stationary/conjugate_gradient.py:24
1. Identity: `ground_state_pcg(grid, potential, initial=None, nonlinearity=0.0, rotation=0.0, tol=1e-8, max_iter=10000, hbar=1.0, m=1.0, callback=None, callback_interval=100, workers=-1)` (24).
2. Producer inputs: `grid` (50-52), `potential.evaluate(grid)` (51), `initial.psi` (54),
   `hbar`, `m`, `g`, `rotation`.
3. Transformation: `V` (51); `T_k` (52); `inner` (56-57); `h_psi` via C52 (62-63);
   `quartic` (65-66); `energy_from = ⟨psi|Hpsi⟩ − ½g∫|psi|⁴` (68-70); PCG loop with
   preconditioner (78-130).
4. Information handling: `np.asarray(..., dtype=float)` (51) — same complex-`V` truncation as
   C53. `alpha = max(1.0, mu - V.min())` (91) keeps the preconditioner positive.
5. Output contract: `(WaveFunction, ConvergenceInfo(converged, steps, energy, mu, residual))`
   (132; dataclass at imaginary_time.py:17-23).
6. **PARTIAL**.
7. tests/test_conjugate_gradient.py:19-62.

### C55 `ground_state` — stationary/imaginary_time.py:47
1. Identity: `ground_state(grid, potential, dtau=0.01, nonlinearity=0.0, initial=None, tol=1e-11, max_steps=50000, check_interval=20, hbar=1.0, m=1.0, orthogonal_to=None, workers=-1, rotation=0.0, backend='numpy')` (47).
2. Producer inputs: `grid` (100-105), `potential` (100-102), `initial.psi` (111), `orthogonal_to`
   (106), `hbar`, `m`, `g`, `rotation`, `backend`.
3. Transformation: builds `SplitOperatorSolver(..., imaginary_time=True)` (100-102);
   `V = solver.potential_at(0.0)` (105); Gram–Schmidt `project` (113-116); loop
   `solver.evolve(wf, check_interval)` (130); `_energy_and_mu` (132,138).
4. Information handling: `_energy_and_mu` (30-37) calls `apply_hamiltonian` **without**
   `nonlinearity` (31) and adds `g|psi|²psi` separately (34) — correct, but the linear and
   nonlinear parts are evaluated with different code paths. `dtau` sequence continuation
   (90-97) re-enters recursively. `backend='cupy'` keeps `psi` on device between checks
   (129-130) and downloads at the end (split_operator.py:284).
5. Output contract: `(WaveFunction, ConvergenceInfo)` (139).
6. **VERIFIED** (tested to 1e-7…1e-12).
7. tests/test_stationary.py:46-79; tests/test_gross_pitaevskii.py:54;
   tests/test_rotation.py:75-96; tests/test_backends.py:136-142.

### C56 `excited_states` — stationary/imaginary_time.py:142
1. Identity: `excited_states(grid, potential, n_states, dtau=0.01, tol=1e-11, max_steps=50000, seed=0, hbar=1.0, m=1.0, workers=-1)` (142).
2. Producer inputs: `grid` (156-160), `potential` (161), `seed` (156).
3. Transformation: seeded random guess `envelope·rng.standard_normal(grid.shape)` (160);
   calls C55 with `orthogonal_to=states` (161-163).
4. Information handling: uses the private RNG `np.random.default_rng(seed)` (156) —
   deterministic for a fixed seed. `orthogonal_to` requires `g=0` (98-99).
5. Output contract: `(energies, states, infos)` (167).
6. **VERIFIED**.
7. tests/test_stationary.py:54-61.

### C57 `coupled_ground_state` — stationary/imaginary_time.py:195
1. Identity: `coupled_ground_state(grid, potentials, couplings, initial, dtau=0.005, tol=1e-11, max_steps=50000, check_interval=20, hbar=1.0, m=1.0, rotation=0.0, backend='numpy', workers=-1)` (195).
2. Producer inputs: `grid` (219-223), `potentials[i].evaluate(grid)` (223), `initial[i].psi` (224),
   `couplings` (218).
3. Transformation: `CoupledGPESolver` (219-220); `Vs` (223); `states` (224); loop
   `solver.evolve(states, check_interval)` (229); `_coupled_energy_mu` (231,236).
4. Information handling: `np.asarray(p.evaluate(grid), dtype=float)` (223) — complex-`V`
   truncation as C53. `_coupled_energy_mu` (179-192) normalises `mu`/`residual` per component
   by `N` (183,187,189).
5. Output contract: `(states, CoupledConvergenceInfo)` (237; dataclass 170-176).
6. **PARTIAL**.
7. tests/test_multicomponent.py:32,77,107.

### C58 `wavelength_to_omega` — strongfield.py:17
Reads `wavelength_nm` (19); `45.56335253/λ`. Unit conversion (nm → a.u. angular frequency).
**VERIFIED**. tests/test_strongfield.py:14-19.

### C59 `intensity_to_field` — strongfield.py:22
Reads `intensity_w_cm2` (24); `sqrt(I/3.50944758e16)`. **VERIFIED**.
tests/test_strongfield.py:14-19.

### C60 `ponderomotive_energy` — strongfield.py:27
Reads `field`, `omega` (29); `E₀²/(4ω²)`. **VERIFIED**. tests/test_strongfield.py:14-19.

### C61 `classical_returns` — strongfield.py:32
Reads `n_phases` (51); deterministic sweep + `brentq` (52-58). **VERIFIED**.
tests/test_strongfield.py:22-30.

### C62 `classical_cutoff` — strongfield.py:65
Reads `ionisation_potential`, `field`, `omega` (67); calls C61 with default 2000 phases.
**VERIFIED**. tests/test_strongfield.py:22-30.

### C63 `harmonic_spectrum` — strongfield.py:70
1. Identity: `harmonic_spectrum(signal, dt, omega0, window=True)` (70).
2. Producer inputs: `signal` (75), `dt` (79), `omega0` (80).
3. Transformation: `s = np.asarray(signal, dtype=float)` (75); optional Hann window (77);
   `spectrum = |rfft(s)|²` (78); `omega = 2π·rfftfreq(len(s), dt)` (79).
4. Information handling: **`dtype=float` cast silently discards the imaginary part of a complex
   dipole signal** (`ComplexWarning`) `[probe]`. No amplitude normalisation (arbitrary units).
5. Output contract: `(omega/omega0, spectrum)` (80).
6. **PARTIAL**.
7. tests/test_strongfield.py:60-69.

### C64 `gabor_transform` — strongfield.py:83
1. Identity: `gabor_transform(signal, dt, omega0, orders, width, times=None)` (83).
2. Producer inputs: `signal` (92), `dt` (93,96,99), `orders` (95), `width` (96,102), `times` (94).
3. Transformation: `s = np.asarray(signal, dtype=float)` (92); `t = arange(len(s))·dt` (93);
   default `times = t[::max(1, len(s)//400)]` (94); `half = ceil(6·width/dt)` (96); windowed
   DFT `|Σ exp(-(t'-tc)²/2σ²)·s·e^{-iωt'}·dt|²` (98-103).
4. Information handling: complex-signal cast (92) as C63; **default time grid truncated to
   ≤400 samples** (94) — silent loss of time resolution; window truncated at `±6σ`
   (documented, 88-90).
5. Output contract: `(times, orders, map[time,order])` (104).
6. **PARTIAL**.
7. tests/test_strongfield.py:72-80.

### C65 `attosecond_pulses` — strongfield.py:107
1. Identity: `attosecond_pulses(signal, dt, omega0, order_min, order_max)` (107).
2. Producer inputs: `signal` (112), `dt` (114), `omega0` (114), band edges (115).
3. Transformation: `spec = fft(s)` (113); `orders = 2π·fftfreq(len(s),dt)/omega0` (114);
   `keep = (orders>=min)&(orders<=max)` (115); `|ifft(where(keep,spec,0))|²` (116).
4. Information handling: **positive band only** → analytic signal (documented, 115);
   `np.asarray(..., dtype=float)` would discard a complex signal's imaginary part.
5. Output contract: intensity envelope array (116).
6. **VERIFIED** for real signals.
7. tests/test_strongfield.py:83-93.

### C66 `dipole_acceleration` — strongfield.py:119
1. Identity: `dipole_acceleration(wf, base_potential, force)` (119).
2. Producer inputs: `wf.grid` (125), `base_potential.gradient(grid)[0]` (127) or
   `gradient(base_potential.evaluate(grid).astype(complex), grid)[0]` (129-130),
   `wf.probability_density` (132), `force` (132), `volume_element` (131).
3. Transformation: `-sum(dV·prob)·dV + force` (132).
4. Information handling: no norm division; `base_potential=None` → `AttributeError` at 130
   (no guard). Uses the analytic `gradient` when present (SoftCoulomb, coulomb.py:33-38),
   else a spectral derivative.
5. Output contract: float.
6. **PARTIAL**.
7. tests/test_strongfield.py:96-101.

### C67 `probe_gpu_status` — benchmarks/perf_comparison.py:42
1. Identity: `probe_gpu_status()` (42).
2. Producer inputs: `cupy` import (52), `getDeviceCount` (59), `getDeviceProperties(0)["name"]`
   (71), `driverGetVersion` (75).
3. Transformation: returns `{state, reason, device, cuda, cupy}` (54-80).
4. Information handling: every failure path returns a distinct `reason`; absent values are
   `None`, never sentinels (54-67,72-77).
5. Output contract: dict consumed by C68 (111) and printed (296).
6. **VERIFIED**.
7. tests/test_benchmark_failure_handling.py:68-77,80-84.

### C68 `benchmark` — benchmarks/perf_comparison.py:83
1. Identity: `benchmark(N, steps=50, num_runs=3, warmup_steps=3)` (83).
2. Producer inputs: `Grid3D` (85), `WaveFunction3D.gaussian` (86-90), `Gaussian3DBarrier` (91),
   `SplitStep3DSolver` (94), `SplitStep3DGPU` (117), `probe_gpu_status` (111).
3. Transformation: CPU warm-up (96-97) + timed loop (99-105); GPU probe (111); GPU warm-up
   covering both `step` and `step_sequence` (120-123); timed `step_sequence` (125-129);
   `rel_diff = ‖psi_cpu − psi_gpu‖/(‖psi_cpu‖+1e-30)` (134-135); fallback nulling (138-146).
4. Information handling: **measures `SplitStep3DGPU`, not `SplitOperatorSolver(backend='cupy')`** —
   the newer GPU solver is not benchmarked. `rel_diff` compares the last CPU run against the
   last GPU run. Timings rounded to 4 dp in the returned dict (163-167). `memory_mb` assumes
   complex128 (157).
5. Output contract: result dict (159-177) → `results.json` (300-301).
6. **PARTIAL** (coverage gap for the newer solver; rounding).
7. tests/test_benchmark_failure_handling.py:39-53,91-119,178-185,230-255,258-313.

### C69 `collect_environment` — benchmarks/perf_comparison.py:180
1. Identity: `collect_environment(argv=None, sizes=None, steps=None, num_runs=None, warmup_steps=None)` (180).
2. Producer inputs: `platform`, `sys.version`, `np.__version__`, `scipy.__version__` (183-188),
   `cupy` (203-213), `git rev-parse` (217-223), `git status --porcelain` (226-228).
3. Transformation: builds the metadata dict; absent values `None` (189-194,207-213,223,230).
4. Information handling: `git_dirty` is a bool derived from non-empty porcelain (226-228).
5. Output contract: metadata dict → `<output stem>.meta.json` (304-310).
6. **VERIFIED**.
7. tests/test_benchmark_failure_handling.py:126-153.

### C70 `check` — benchmarks/validation_suite.py:31
1. Identity: `check(category, name, reference, measured_desc, error, tolerance)` (31).
2. Producer inputs: the measured `error` and `tolerance` (32).
3. Transformation: `passed = error <= tolerance` (32); appends to global `RESULTS` (33);
   prints PASS/FAIL (34).
4. Information handling: `RESULTS` is module-global mutable state (28,33); no precision guard.
5. Output contract: `None`; side effect on `RESULTS` and stdout.
6. **VERIFIED**.
7. Test coverage: **none** (script not imported by tests).

### C71 `write_report` — benchmarks/validation_suite.py:323
1. Identity: `write_report(path, elapsed)` (323).
2. Producer inputs: global `RESULTS` (338), `platform.python_version()`, `np.__version__` (329),
   `elapsed` (330).
3. Transformation: formats markdown rows `|cat|name|ref|metric|err|tol|result|` (338-340);
   `cell()` escapes `|` (335-336); appends `n_pass/len(RESULTS)` (341-342); `Path.write_text`
   (343).
4. Information handling: errors formatted `:.2e` and tolerances `:.0e` (339) — precision
   truncated in the report; `**FAIL**` markup (340).
5. Output contract: `benchmarks/validation_report.md` (355-356).
6. **VERIFIED**.
7. Test coverage: **none**.

### C72 `main` — benchmarks/validation_suite.py:346
1. Identity: `main()` (346).
2. Producer inputs: none (calls the 15 check functions, 350-352).
3. Transformation: reconfigures stdout encoding (347-348); times the run (349,356); writes the
   report (355-356); returns `0`/`1` (359).
4. Information handling: a failing check does not stop the run (all checks executed).
5. Output contract: exit code + `validation_report.md` + stdout summary (357-359).
6. **VERIFIED**.
7. Test coverage: **none**.

---

## 2. Suspected-loss investigation (confirm / refute)

### S1. `runner.py` logs energy via `total_energy_expectation(wf, potential)` without `hbar`/`m` — **CONFIRMED**
- Call site: runner.py:170. Observable defaults: expectation.py:170 (`hbar: float=1.0, m: float=1.0`),
  propagated to `kinetic_energy_expectation` (expectation.py:154,171).
- Solver configuration: runner.py:101-102 reads `hbar`/`m` from cfg (default 1.0) and passes them
  to the solver (runner.py:107,115-120).
- `[probe]` config `hbar=2.0, m=3.0`, 1-D harmonic trap, 3 steps: runner logged
  `E=2.125287`; recomputing with the configured constants gives `E=2.833611`. The kinetic part
  alone: `T_default=0.624168` vs `T_true=0.832223`.
- Impact: every `E=` log line is wrong whenever `hbar≠1` or `m≠1`.

### S2. `runner.py` reads potential parameters for solver construction vs. what the observable re-evaluates — **CONFIRMED at the observable level; latent in the runner**
- Solver construction: runner.py:141 `create_potential(cfg["potential"]["type"], **params)`.
- Observable re-evaluation: expectation.py:143 `V = potential.evaluate(wf.grid)`; for a
  `TimeDependentPotential` this is `evaluate_at(grid, 0.0)` (time_dependent.py:23-24).
- `[probe]` `DipoleDrive(HarmonicTrap(1.0), F0=1.0, omega=0.6)`, t=1.0:
  `E(V(t=0))=0.665055` vs `E(V(t))=0.612336` (diff `0.0527`).
- Reachability: `SimulationRunner` cannot construct a time-dependent potential because
  `DipoleDrive`/`TimeDependentCustomPotential` are absent from `POTENTIAL_REGISTRY`
  (potentials/__init__.py:19-39). So the runner path is latent; direct observable use is affected.

### S3. `vortex_positions` re-evaluates the potential/density and applies a density threshold at the plaquette rather than the neighbourhood — **CONFIRMED**
- Density: `rho = gaussian_filter(wf.probability_density, sigma=(smoothing/g.dx, smoothing/g.dy))`
  (current.py:74). Threshold: `keep = (charge != 0) & (rho[:-1, :-1] > min_density * rho.max())`
  (current.py:75) — `rho[:-1,:-1]` is the plaquette's lower-left **node**, not its centre or a
  neighbourhood maximum.
- `[probe]` off-grid vortex at `(3.0625, 0.0625)` in a compact condensate: core/max smoothed
  density `0.1870 < 0.2` → default returns `n=0`; `min_density=0.0` returns the vortex.
- Note: `vortex_positions` does **not** read a potential at all (only `wf.psi`, `wf.grid`,
  `wf.probability_density`, current.py:63-77); the "re-evaluates the potential" part of the
  suspicion is **refuted**.

### S4. `vortex_positions` grid-alignment-dependent winding — **CONFIRMED** (prior audit defect)
- Mechanism: circulation is summed from node phases only (current.py:71-72) and rounded with
  `np.rint(circ/2π)` (current.py:73).
- `[probe]` single vortex, `Grid2D(64,-8,8,64,-8,8)` (`dx=0.25`), envelope `exp(-r²/32)`,
  core `0.25`:
  - centre `(0.0,0.0)` (grid node): all four adjacent plaquettes circulation `0.0000` → **0 vortices**.
  - centre `(0.125,0.0)` (half-cell): circulation `0.0000` → **0 vortices**.
  - centre `(0.0625,0.0625)` (quarter-cell): one plaquette circulation `6.2832` → 1 vortex.
- `[probe]` repo test centres: single vortex at `(-2.0,1.0)` (grid node) → `n=0`;
  `(2.5,-1.5)` (grid node) → `n=0`; `(0.5,2.5)` with `q=-1` → **two** plaquettes, both charge
  `-1` (double count). The committed test passes only because the three-vortex product moves
  the winding onto plaquettes and the tolerance is `dx` (tests/test_new_potentials_and_observables.py:139).

### S5. Observables that do not divide by the norm — **CONFIRMED**
- `position_expectation`/`position_squared` (expectation.py:7,9,11,18,20,22),
  `momentum_expectation`/`momentum_squared` (expectation.py:83,91,101,112,120,130),
  `potential_energy_expectation` (expectation.py:146,148,150),
  `kinetic_energy_expectation` (expectation.py:157,161,166),
  `total_energy_expectation` (expectation.py:173),
  `transmission_coefficient`/`reflection_coefficient` (coefficients.py:8,11,14,22,25,28),
  `probability_current` (current.py:23), `angular_momentum_z_expectation` (current.py:32),
  `autocorrelation` (current.py:37), `dipole_acceleration` (strongfield.py:132).
- For `‖psi‖=1` this is correct; for `‖psi‖≠1` every value scales by the norm.
- `[probe]` free packet + ABL, norm `2e-6`: logged `E=6.6e-5` vs `E/norm=30.5`; `<x>_logged=2e-6`
  vs `<x>/norm=0.892`.
- The test suite explicitly encodes the un-normalised contract:
  tests/test_3d_observables.py:67 asserts `T + R == wf.norm()`.

### S6. Any place where a 1-D array could be broadcast against an N-D grid — **REFUTED for the listed consumers**
- All coordinate arithmetic in the consumers is guarded by `isinstance(wf, WaveFunction1D/2D/3D)`
  branches that select `grid.x` vs `grid.X/Y/Z`: expectation.py:6-11,16-24,34-39,43-48,57-68;
  coefficients.py:6-14,20-28; current.py:28-32.
- The nearest risk is `potential_energy_expectation` (expectation.py:143-150): it does
  `V * prob` with no shape check, so a producer returning a 1-D `V` on an N-D grid would
  broadcast silently. Every potential in `POTENTIAL_REGISTRY` dispatches on grid type
  (barriers.py:12-18, oscillator.py:12-20, traps.py:27-35, coulomb.py:23-31, etc.), so this is
  **not reachable through the registry**. Verdict: **NOT_VERIFIED** as an actual defect;
  no confirmed instance found.

---

## 3. Ranked information-loss points

| Rank | Loss | Location | Evidence | Preserved meaning? | Scientific impact |
|---|---|---|---|---|---|
| L1 | Energy log uses `hbar=m=1` while solver uses cfg `hbar`,`m` | runner.py:170; expectation.py:170 | `[probe]` logged 2.125287 vs true 2.833611 | LOSSY | High — all energy logs wrong for non-atomic units |
| L2 | No norm division after ABL; energy/`<x>` scaled by norm | runner.py:162-163,170-171 | `[probe]` norm 2e-6; E 6.6e-5 vs 30.5 | LOSSY | High — logs meaningless once absorber acts |
| L3 | Vortex winding depends on grid alignment; misses/duplicates vortices | current.py:71-73 | `[probe]` node→0, half-cell→0, quarter-cell→1; q=-1 node→2 | LOSSY | High — vortex counts/positions wrong |
| L4 | Density threshold applied at plaquette corner; default 0.2 masks real cores | current.py:75 | `[probe]` core/max 0.187 dropped, found at 0.0 | LOSSY | High — real vortices silently dropped |
| L5 | `gpu=True` silently ignored when `solver='split_operator'` | runner.py:103-113 | `[probe]` backend `scipy-cpu` | LOSSY | Medium — silent CPU fallback, no GPU result |
| L6 | 3-D animation config crashes (`dim>=2` gate) | runner.py:186; animation.py:51 | `[probe]` `TypeError: Invalid shape (16,16,16) for image data` | LOSSY | Medium — feature unusable for 3-D |
| L7 | Time-dependent `V` re-evaluated at `t=0` by the observable | expectation.py:143; time_dependent.py:23-24 | `[probe]` 0.665055 vs 0.612336 | LOSSY | Medium — wrong potential energy (latent in runner) |
| L8 | Complex→real casts discard imaginary parts (`ComplexWarning`) | eigensolver.py:47; conjugate_gradient.py:51; imaginary_time.py:223; multicomponent.py:70-71; split_operator.py:143; strongfield.py:75,92 | `[probe]` numpy warns + discards | LOSSY | Medium — complex/absorbing potentials and complex dipole signals silently truncated |
| L9 | Observables omit norm division | expectation.py:7-173; coefficients.py:4-30; current.py:17-37 | `[code]`+`[probe]` | PARTIAL | Medium — wrong for any un-normalised state |
| L10 | Potential overlay rescaled to probability units; `Re(ψ)` mixed with `|ψ|²` | plots_1d.py:18-26 | `[code]` | LOSSY (visual) | Medium — misleading plot scale |
| L11 | Snapshot/animation frames all use the first frame's grid | plots_2d.py:101-103; animation.py:52-53 | `[code]` | PARTIAL | Low — silent misalignment if grids differ |
| L12 | Sub-grid spacing mismatch in HTML export when `stride∤N` | volume_3d.py:343-345 | `[probe]` dx 0.320 vs sub.dx 0.615 | PARTIAL | Low — ~4 % axis scaling |
| L13 | Phase interpolated across the ±π branch cut | volume_3d.py:54-61,214-215 | `[code]` | PARTIAL | Low — wrong face colours near cuts |
| L14 | `gabor_transform` default time grid truncated to ≤400 samples | strongfield.py:94 | `[code]` | PARTIAL | Low — lost time resolution |
| L15 | `log_interval=0` → `ZeroDivisionError` | runner.py:169 | `[code]` | LOSSY | Low — crash on a plausible config |
| L16 | Unknown `solver` string silently re-dispatched | runner.py:105-121 | `[code]` | PARTIAL | Low — typo silent |
| L17 | 2-D `Nx/Ny` ignored (square grid forced) | runner.py:56 | `[code]` | LOSSY | Low — anisotropic 2-D grids impossible |
| L18 | `wavefunction.type` ignored (always Gaussian) | runner.py:65 | `[code]` | LOSSY | Low — non-Gaussian configs impossible |
| L19 | `np.savez(params=cfg)` pickles a dict; needs `allow_pickle=True` | runner.py:182 | `[code]`+tests/test_runner.py:90 | PARTIAL | Low — portability |
| L20 | `numpy_backend.to_host=np.asarray` aliases (no copy); `overwrite_x=True` | backends.py:36-39 | `[code]` | PARTIAL | Low — aliasing/in-place risk |
| L21 | `eigensolver` `.real` discards imaginary part of complex trial vectors | eigensolver.py:57,74 | `[code]` | PARTIAL | Low — only for complex vectors (X0 is real) |
| L22 | Benchmark measures `SplitStep3DGPU`, not `SplitOperatorSolver(backend='cupy')` | perf_comparison.py:117,128 | `[code]` | NOT_VERIFIED (coverage gap) | Low — newer GPU path unbenchmarked |
| L23 | Timings rounded to 4 dp; report errors to 2 sig figs | perf_comparison.py:163-167; validation_suite.py:339 | `[code]` | PARTIAL | Low — precision truncation |

---

## 4. Consumers with no test coverage

Directly untested (no test references the qualified name):

- `quantumlab.visualization.animation.WavePacketAnimator` (animation.py:13) — none
- `quantumlab.visualization.plots_1d.plot_wavefunction_1d` (plots_1d.py:7) — none
- `quantumlab.visualization.plots_1d.plot_dual_space_1d` (plots_1d.py:40) — none
- `quantumlab.visualization.plots_2d.plot_density_2d` (plots_2d.py:8) — none
- `quantumlab.visualization.plots_2d.plot_density_snapshots_2d` (plots_2d.py:71) — none
- `quantumlab.visualization.plots_2d.plot_orthogonal_slices_3d` (plots_2d.py:135) — none
- `quantumlab.visualization.plots_3d.plot_space_time_3d` (plots_3d.py:5) — none
- `quantumlab.visualization.style.set_style` (style.py:3) — none
- `quantumlab.observables.momentum.get_momentum_wavefunction` (momentum.py:4) — none
- `quantumlab.observables.current.gradient` (current.py:11) — none direct (indirect via C31/C32)
- `quantumlab.solvers.backends.numpy_backend` (backends.py:31) — none direct
- `quantumlab.solvers.backends.cupy_backend` (backends.py:43) — covered only by the
  device-gated real-CuPy test (tests/test_backends.py:155-165); no CPU-runnable test
- `benchmarks.validation_suite.check` (validation_suite.py:31) — none
- `benchmarks.validation_suite.write_report` (validation_suite.py:323) — none
- `benchmarks.validation_suite.main` (validation_suite.py:346) — none

Partially tested (branch coverage gaps):

- `quantumlab.runner.SimulationRunner.run` — no test for the `animation` branch
  (runner.py:185-198) or the `absorbing_boundary` branch (runner.py:145-148); no test with
  `hbar≠1`/`m≠1`.
- `quantumlab.runner.SimulationRunner._build_solver` — `gpu=True`+`solver='split_operator'`
  and the `backend` key are untested.
- `quantumlab.runner.SimulationRunner._build_grid` — 3-D `Nx/Ny/Nz`, `Lx/Ly/Lz` untested.
- `quantumlab.runner.SimulationRunner._build_wavefunction` — 2-D/3-D branches untested.

---

## 5. Counts

- Total consumers inventoried: **72** (C01–C72).
- Consumers with **no** test coverage: **15** (listed in §4).
- Consumers with **partial** branch coverage: **4** (runner methods listed in §4).
- Confirmed loss points: **L1–L8, L10, L15–L19** (16 confirmed); partial/suspected: L9,
  L11–L14, L20–L23.
- Refuted suspicions: S3 (potential re-read by `vortex_positions`), S6 (1-D vs N-D broadcast).
