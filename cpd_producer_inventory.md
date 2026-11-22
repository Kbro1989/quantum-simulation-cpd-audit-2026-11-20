# QuantumLab Producer Inventory - CPD audit 2026-11-20

- Repository: `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
- Branch `remediation/2026-11-20`, HEAD `44f30e30654c064b75f760833741ab55b392ff20` (clean tree).
- Package: `quantumlab` 1.3.0 (split-step Fourier quantum wave-packet simulator).
- Method: read-only `read_file`/`search_files` + an AST scan of every `*.py` in the repo (definitions, imports, call/attribute sites); cheap import/shape probes. No file in the repo was created, modified, moved or deleted; no git state-changing command was run; no packages installed; the full test suite was not run.

## Scope and counting rule

A **producer** is any class, function or method that creates scientifically meaningful information
(numerical values, state, arrays or artifacts). Inventory granularity is **function-level**: every class
and every function/method defined at module or class top level in the listed files is one producer, including
`__init__`, properties and private helpers. Nested closures (e.g. `envelope` inside `sin2_envelope`) are
not counted separately; they are named inside their enclosing row. Module-level constants (`YOSHIDA_W0`,
`YOSHIDA_W1`, `HARTREE_EV`, `AU_TIME_FS`, `AU_INTENSITY_W_CM2`, `POTENTIAL_REGISTRY`, `_AXIS_INDEX`) and
`__init__.py` re-export lists are not functions and are not counted.

**Total producers: 234**

Call-site notation: `path:line`. Tests are cited as `tests/file.py::test_name:line` (line = test function
definition). 'NONE' means no such site exists anywhere in the repository.

Independent-validation legend: **VERIFIED** = checked against an exact/analytic or independent numerical
reference in `benchmarks/validation_suite.py` (report `benchmarks/validation_report.md`, 27/27 pass) or the GPU
benchmark (`benchmarks/results_2026-11-20_cuda.json`); **PARTIALLY** = unit tests only, or indirect exercise
through a caller; **NONE** = no test and no independent check.

Evidence base for the probes (run on this host, Python 3.11.9 / numpy 2.4.3):
`Grid1D(8,-4,4)` -> `dx=1.0`, `dk=0.7853981634`, `x/k` float64 `(8,)`; `Grid2D(4x6)` -> `X` `(4,6)` float64,
`dk_x=1.5707963`, `dk_y=1.0471976`; `Grid3D(4^3)` -> `X` `(4,4,4)` float64; `WaveFunction*` `psi` complex128,
`probability_density` float64; Gaussian norm `0.9999999999999999`; 1D Parseval `0.9999999999999997`;
`AbsorbingBoundaryLayer` orders 1..6 all finite, min 0.0, max 1.0; `k_volume_element` computes but has no
consumer; `classical_returns(2000)` max `3.1731359` at birth `17.97 deg`; `wavelength_to_omega(800)=0.05695419`;
`intensity_to_field(1e14)=0.05338025`; `ponderomotive_energy=0.21960887`.

---

## Inventory

### `quantumlab/core/grid.py`

#### P1. `Grid1D` - class

- **Definition:** `quantumlab/core/grid.py:3`
- **Signature (verbatim):** `class Grid1D:`
- **Input domain:** N:int, x_min:float, x_max:float
- **Output domain:** object; N,x_min,x_max,L,dx:float; x,k:float64 (N,); dk:float; shape:(N,)
- **Mathematical definition:** L=x_max-x_min; dx=L/N; x=linspace(x_min,x_max,N,endpoint=False); k=2*pi*fftfreq(N,dx); dk=2*pi/L
- **Preconditions / postconditions enforced:** NONE enforced (no validation of N>0, x_max>x_min, types). Post: dx>0 iff L>0; k[0]=0.
- **Actual callers:** runner.py:54; examples/01_gaussian_barrier.py:29; 02:27; 03:28; 04:30; 09:46; 12:51; benchmarks/validation_suite.py:42,52,69,118,135,160,209,248,312; testbench_interlock.py:97
- **Test coverage:** tests/test_potentials.py::test_gaussian_barrier:12; test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_free_particle_matches_analytic_gaussian_spreading:114; test_absorbing_boundary_validation.py::test_valid_arguments_build_a_clean_mask:70
- **Independent validation:** VERIFIED - underpins validation_suite free-spreading/convergence checks (report 1.37e-15, order 2.001/3.997)

#### P2. `Grid1D.__init__` - method

- **Definition:** `quantumlab/core/grid.py:5`
- **Signature (verbatim):** `def __init__(self, N: int, x_min: float, x_max: float):`
- **Input domain:** N:int, x_min:float, x_max:float
- **Output domain:** sets N,x_min,x_max,L,dx,x,k,dk
- **Mathematical definition:** same as class
- **Preconditions / postconditions enforced:** NONE enforced
- **Actual callers:** all Grid1D(...) sites (see Grid1D)
- **Test coverage:** same as Grid1D
- **Independent validation:** VERIFIED - probe: N=8,-4,4 -> dx=1.0, dk=0.7853981634, x/k float64 (8,)

#### P3. `Grid1D.shape` - property

- **Definition:** `quantumlab/core/grid.py:16`
- **Signature (verbatim):** `def shape(self):`
- **Input domain:** none
- **Output domain:** tuple (N,)
- **Mathematical definition:** (N,)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** quantumlab/core/wavefunction.py:11,48,88; potentials/*.py; tests (many)
- **Test coverage:** tests/test_3d_solver.py::test_grid3d_shape:34; test_potentials.py::test_gaussian_barrier:12
- **Independent validation:** PARTIALLY - exercised by every shape assertion; no independent check of the tuple itself

#### P4. `Grid2D` - class

- **Definition:** `quantumlab/core/grid.py:19`
- **Signature (verbatim):** `class Grid2D:`
- **Input domain:** N_x,N_y:int; x_min,x_max,y_min,y_max:float
- **Output domain:** X,Y,K_x,K_y:float64 (N_x,N_y); x,y:float64; dx,dy,L_x,L_y,dk_x,dk_y:float; shape:(N_x,N_y)
- **Mathematical definition:** dx=L_x/N_x; dy=L_y/N_y; meshgrid(indexing='ij'); k_x=2pi ffreq(N_x,dx); K_x,K_y=meshgrid
- **Preconditions / postconditions enforced:** NONE enforced
- **Actual callers:** runner.py:56; examples/05:36,10:34,11:65,174,13:67,108,193; benchmarks/validation_suite.py:111,179,189,283,296
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11; test_new_potentials_and_observables.py::test_harmonic_trap_anisotropic_and_centered:20; test_stationary.py::test_2d_anisotropic_spectrum_lobpcg:21
- **Independent validation:** VERIFIED - 2D/3D validation checks (rotating frame, GP virial) depend on it

#### P5. `Grid2D.__init__` - method

- **Definition:** `quantumlab/core/grid.py:21`
- **Signature (verbatim):** `def __init__(self, N_x: int, x_min: float, x_max: float, N_y: int, y_min: float, y_max: float):`
- **Input domain:** see Grid2D
- **Output domain:** see Grid2D
- **Mathematical definition:** see Grid2D
- **Preconditions / postconditions enforced:** NONE enforced
- **Actual callers:** all Grid2D(...) sites (see Grid2D)
- **Test coverage:** same as Grid2D
- **Independent validation:** VERIFIED - probe: 4x6 grid -> X (4,6) float64, dk_x=1.5707963, dk_y=1.0471976

#### P6. `Grid2D.shape` - property

- **Definition:** `quantumlab/core/grid.py:42`
- **Signature (verbatim):** `def shape(self):`
- **Input domain:** none
- **Output domain:** tuple (N_x,N_y)
- **Mathematical definition:** (N_x,N_y)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** wavefunction.py:48,88; potentials; tests
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11
- **Independent validation:** PARTIALLY

#### P7. `Grid3D` - class

- **Definition:** `quantumlab/core/grid.py:45`
- **Signature (verbatim):** `class Grid3D:`
- **Input domain:** N_x,N_y,N_z:int; x_min..z_max:float
- **Output domain:** X,Y,Z,K_x,K_y,K_z:float64 (N_x,N_y,N_z); dx,dy,dz,dk_x,dk_y,dk_z:float; shape:(N_x,N_y,N_z)
- **Mathematical definition:** dx=L_x/N_x etc; meshgrid('ij'); k_j=2pi ffreq(N_j,dj)
- **Preconditions / postconditions enforced:** NONE enforced
- **Actual callers:** runner.py:60; examples/06:32,07:43,08:70,11:154; benchmarks/validation_suite.py:83,101,122,170,315; benchmarks/perf_comparison.py:85; benchmarks/gpu_split_operator.py:45; visualization/volume_3d.py:343
- **Test coverage:** tests/test_3d_solver.py::test_grid3d_shape:34; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_stationary.py::test_3d_isotropic_degeneracy:29
- **Independent validation:** VERIFIED - 3D norm/energy conservation check (validation_report 2.55e-15, 2.18e-10)

#### P8. `Grid3D.__init__` - method

- **Definition:** `quantumlab/core/grid.py:47`
- **Signature (verbatim):** `def __init__(self, N_x: int, x_min: float, x_max: float,\n                 N_y: int, y_min: float, y_max: float,\n                 N_z: int, z_min: float, z_max: float):`
- **Input domain:** see Grid3D
- **Output domain:** see Grid3D
- **Mathematical definition:** see Grid3D
- **Preconditions / postconditions enforced:** NONE enforced
- **Actual callers:** all Grid3D(...) sites (see Grid3D)
- **Test coverage:** same as Grid3D
- **Independent validation:** VERIFIED - probe: 4^3 grid -> X (4,4,4) float64, dk_z=1.5707963

#### P9. `Grid3D.shape` - property

- **Definition:** `quantumlab/core/grid.py:83`
- **Signature (verbatim):** `def shape(self):`
- **Input domain:** none
- **Output domain:** tuple (N_x,N_y,N_z)
- **Mathematical definition:** (N_x,N_y,N_z)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** wavefunction.py:88; potentials; volume_3d.py; tests
- **Test coverage:** tests/test_3d_solver.py::test_grid3d_shape:34
- **Independent validation:** PARTIALLY


### `quantumlab/core/wavefunction.py`

#### P10. `WaveFunction1D` - class

- **Definition:** `quantumlab/core/wavefunction.py:4`
- **Signature (verbatim):** `class WaveFunction1D:`
- **Input domain:** grid:Grid1D, psi:ndarray=None
- **Output domain:** object; psi complex128 (N,); grid
- **Mathematical definition:** container for psi on Grid1D
- **Preconditions / postconditions enforced:** psi None -> zeros(complex); else shape must equal grid.shape (ValueError)
- **Actual callers:** runner.py:70,74,84; solvers/split_step_1d.py:27; examples/09:30; benchmarks/validation_suite.py:163,252,253
- **Test coverage:** tests/test_gross_pitaevskii.py::test_bright_soliton_propagates_without_dispersion:20; test_multicomponent.py::test_invalid_coupled_configurations:130
- **Independent validation:** VERIFIED - norm/energy conservation and soliton checks

#### P11. `WaveFunction1D.__init__` - method

- **Definition:** `quantumlab/core/wavefunction.py:6`
- **Signature (verbatim):** `def __init__(self, grid: Grid1D, psi: np.ndarray=None):`
- **Input domain:** grid:Grid1D, psi:np.ndarray=None
- **Output domain:** psi complex128 (N,)
- **Mathematical definition:** zeros if None else np.array(psi,dtype=complex)
- **Preconditions / postconditions enforced:** ENFORCED: psi.shape==grid.shape else ValueError
- **Actual callers:** all WaveFunction1D(...) sites; solvers/split_step_1d.py:27
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9; test_gross_pitaevskii.py:23
- **Independent validation:** VERIFIED

#### P12. `WaveFunction1D.probability_density` - property

- **Definition:** `quantumlab/core/wavefunction.py:16`
- **Signature (verbatim):** `def probability_density(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** float64 (N,), rho=|psi|^2
- **Mathematical definition:** |psi|^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables/expectation.py:5; observables/coefficients.py:5; observables/nonlinear.py:8; strongfield.py:132; visualization; tests
- **Test coverage:** tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_gross_pitaevskii.py::test_bright_soliton_propagates_without_dispersion:20
- **Independent validation:** VERIFIED - soliton/free-spreading exact-density checks

#### P13. `WaveFunction1D.norm` - method

- **Definition:** `quantumlab/core/wavefunction.py:19`
- **Signature (verbatim):** `def norm(self) -> float:`
- **Input domain:** none
- **Output domain:** float
- **Mathematical definition:** sum(|psi|^2)*dx
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py; examples; benchmarks/validation_suite.py:95; testbench_interlock.py:102,108
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_norm_and_energy_conservation:50; test_2d_solver.py::test_2d_norm_conservation:11
- **Independent validation:** VERIFIED - norm conservation check 2.55e-15; probe 0.9999999999999999

#### P14. `WaveFunction1D.normalize` - method

- **Definition:** `quantumlab/core/wavefunction.py:22`
- **Signature (verbatim):** `def normalize(self) -> 'WaveFunction1D':`
- **Input domain:** none
- **Output domain:** self (WaveFunction1D)
- **Mathematical definition:** psi /= sqrt(norm) if norm>0
- **Preconditions / postconditions enforced:** ENFORCED: no-op if norm==0 (silent)
- **Actual callers:** benchmarks/validation_suite.py:112,201; examples/11:158; tests
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99; test_rotation.py::test_vortex_is_stationary_with_rotating_frame_energy:48
- **Independent validation:** VERIFIED - normalised states used in validation

#### P15. `WaveFunction1D.fourier_transform` - method

- **Definition:** `quantumlab/core/wavefunction.py:28`
- **Signature (verbatim):** `def fourier_transform(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** complex128 (N,)
- **Mathematical definition:** fft(psi)*dx/sqrt(2pi)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables/expectation.py:77,106; observables/momentum.py:5
- **Test coverage:** indirect: tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_momentum_expectation_and_heisenberg:34
- **Independent validation:** VERIFIED - Parseval probe 0.9999999999999997 vs 0.9999999999999999; Heisenberg checks

#### P16. `WaveFunction1D.copy` - method

- **Definition:** `quantumlab/core/wavefunction.py:31`
- **Signature (verbatim):** `def copy(self) -> 'WaveFunction1D':`
- **Input domain:** none
- **Output domain:** WaveFunction1D (deep copy of psi)
- **Mathematical definition:** WaveFunction1D(grid, psi.copy())
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:156,166; benchmarks/perf_comparison.py:101,123,128; tests/test_3d_gpu_solver.py:82,83
- **Test coverage:** tests/test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73
- **Independent validation:** PARTIALLY - used as test fixture/copy semantics; no independent check

#### P17. `WaveFunction1D.gaussian` - classmethod

- **Definition:** `quantumlab/core/wavefunction.py:35`
- **Signature (verbatim):** `def gaussian(cls, grid: Grid1D, x0: float, k0: float, sigma: float) -> 'WaveFunction1D':`
- **Input domain:** grid:Grid1D, x0,k0,sigma:float
- **Output domain:** WaveFunction1D, normalised
- **Mathematical definition:** exp(-(x-x0)^2/(4 sigma^2))*exp(i k0 x), then normalize
- **Preconditions / postconditions enforced:** ENFORCED: sigma==0 -> division by zero (not guarded)
- **Actual callers:** runner.py:70,74,84; examples; benchmarks/validation_suite.py:44,54,71,85,102,136,191,285,286,297,298; benchmarks/perf_comparison.py:86; benchmarks/gpu_split_operator.py:24; testbench_interlock.py:98
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_free_particle_matches_analytic_gaussian_spreading:114; test_observables.py::test_gaussian_observables_and_uncertainty:7
- **Independent validation:** VERIFIED - free-spreading exact solution 1.37e-15; minimum-uncertainty 4.6e-12

#### P18. `WaveFunction2D` - class

- **Definition:** `quantumlab/core/wavefunction.py:41`
- **Signature (verbatim):** `class WaveFunction2D:`
- **Input domain:** grid:Grid2D, psi=None
- **Output domain:** psi complex128 (N_x,N_y)
- **Mathematical definition:** container
- **Preconditions / postconditions enforced:** shape check (ValueError)
- **Actual callers:** runner.py; solvers/split_step_2d.py:41; examples/11:174,187; 13:117,118; benchmarks/validation_suite.py:112,201
- **Test coverage:** tests/test_rotation.py::test_coherent_state_in_rotating_frame:19; test_new_potentials_and_observables.py::test_vortex_positions_finds_imprinted_vortices:127
- **Independent validation:** VERIFIED

#### P19. `WaveFunction2D.__init__` - method

- **Definition:** `quantumlab/core/wavefunction.py:43`
- **Signature (verbatim):** `def __init__(self, grid: Grid2D, psi: np.ndarray=None):`
- **Input domain:** grid:Grid2D, psi=None
- **Output domain:** psi complex128 (N_x,N_y)
- **Mathematical definition:** zeros or np.array(psi,complex)
- **Preconditions / postconditions enforced:** ENFORCED shape==grid.shape else ValueError
- **Actual callers:** all WaveFunction2D(...) sites
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11
- **Independent validation:** VERIFIED

#### P20. `WaveFunction2D.probability_density` - property

- **Definition:** `quantumlab/core/wavefunction.py:53`
- **Signature (verbatim):** `def probability_density(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** float64 (N_x,N_y)
- **Mathematical definition:** |psi|^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables; visualization; tests
- **Test coverage:** tests/test_rotation.py::test_rotating_frame_energy_conserved_in_anisotropic_trap:61
- **Independent validation:** VERIFIED

#### P21. `WaveFunction2D.norm` - method

- **Definition:** `quantumlab/core/wavefunction.py:56`
- **Signature (verbatim):** `def norm(self) -> float:`
- **Input domain:** none
- **Output domain:** float
- **Mathematical definition:** sum(|psi|^2)*dx*dy
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py; examples; benchmarks/validation_suite.py:95
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11; test_rotation.py::test_coherent_state_in_rotating_frame:19
- **Independent validation:** VERIFIED

#### P22. `WaveFunction2D.normalize` - method

- **Definition:** `quantumlab/core/wavefunction.py:59`
- **Signature (verbatim):** `def normalize(self) -> 'WaveFunction2D':`
- **Input domain:** none
- **Output domain:** self
- **Mathematical definition:** psi/=sqrt(norm) if norm>0
- **Preconditions / postconditions enforced:** silent if norm==0
- **Actual callers:** benchmarks/validation_suite.py:112,201; examples/11:158
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99
- **Independent validation:** VERIFIED

#### P23. `WaveFunction2D.fourier_transform` - method

- **Definition:** `quantumlab/core/wavefunction.py:65`
- **Signature (verbatim):** `def fourier_transform(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** complex128 (N_x,N_y)
- **Mathematical definition:** fft2(psi)*dx*dy/(2pi)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables/expectation.py:77,106; observables/momentum.py:5
- **Test coverage:** indirect: tests/test_3d_observables.py::test_3d_momentum_probability_density:72
- **Independent validation:** VERIFIED - Parseval test (test_3d_observables.py:79)

#### P24. `WaveFunction2D.copy` - method

- **Definition:** `quantumlab/core/wavefunction.py:68`
- **Signature (verbatim):** `def copy(self) -> 'WaveFunction2D':`
- **Input domain:** none
- **Output domain:** WaveFunction2D
- **Mathematical definition:** WaveFunction2D(grid, psi.copy())
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:156,166; benchmarks/perf_comparison.py
- **Test coverage:** tests/test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73
- **Independent validation:** PARTIALLY

#### P25. `WaveFunction2D.gaussian` - classmethod

- **Definition:** `quantumlab/core/wavefunction.py:72`
- **Signature (verbatim):** `def gaussian(cls, grid: Grid2D, x0: float, y0: float, k0_x: float, k0_y: float, sigma_x: float, sigma_y: float) -> 'WaveFunction2D':`
- **Input domain:** grid:Grid2D, x0,y0,k0_x,k0_y,sigma_x,sigma_y
- **Output domain:** WaveFunction2D normalised
- **Mathematical definition:** product of 1D Gaussians in X and Y, then normalize
- **Preconditions / postconditions enforced:** sigma==0 not guarded
- **Actual callers:** runner.py; examples/05:37,13:60; benchmarks/validation_suite.py:102,136,191,285,297
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11; test_rotation.py::test_coherent_state_in_rotating_frame:19
- **Independent validation:** VERIFIED - rotating-frame coherent-state check 1.89e-08

#### P26. `WaveFunction3D` - class

- **Definition:** `quantumlab/core/wavefunction.py:80`
- **Signature (verbatim):** `class WaveFunction3D:`
- **Input domain:** grid:Grid3D, psi=None
- **Output domain:** psi complex128 (N_x,N_y,N_z)
- **Mathematical definition:** container
- **Preconditions / postconditions enforced:** shape check (ValueError)
- **Actual callers:** solvers/split_step_3d.py:65; split_step_3d_gpu.py:93,105,123; examples/11:157
- **Test coverage:** tests/test_3d_solver.py::test_3d_gaussian_norm:53; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42
- **Independent validation:** VERIFIED

#### P27. `WaveFunction3D.__init__` - method

- **Definition:** `quantumlab/core/wavefunction.py:82`
- **Signature (verbatim):** `def __init__(self, grid: Grid3D, psi: np.ndarray=None):`
- **Input domain:** grid:Grid3D, psi=None
- **Output domain:** psi complex128 (N_x,N_y,N_z)
- **Mathematical definition:** zeros or np.array(psi,complex)
- **Preconditions / postconditions enforced:** ENFORCED shape==grid.shape else ValueError
- **Actual callers:** all WaveFunction3D(...) sites
- **Test coverage:** tests/test_3d_solver.py::test_3d_gaussian_norm:53
- **Independent validation:** VERIFIED

#### P28. `WaveFunction3D.probability_density` - property

- **Definition:** `quantumlab/core/wavefunction.py:92`
- **Signature (verbatim):** `def probability_density(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** float64 (N_x,N_y,N_z)
- **Mathematical definition:** |psi|^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables; visualization; tests
- **Test coverage:** tests/test_3d_solver.py::test_3d_gaussian_norm:53
- **Independent validation:** VERIFIED

#### P29. `WaveFunction3D.norm` - method

- **Definition:** `quantumlab/core/wavefunction.py:95`
- **Signature (verbatim):** `def norm(self) -> float:`
- **Input domain:** none
- **Output domain:** float
- **Mathematical definition:** sum(|psi|^2)*dx*dy*dz
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py; examples; benchmarks/validation_suite.py:95
- **Test coverage:** tests/test_3d_solver.py::test_3d_norm_conservation:72; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42
- **Independent validation:** VERIFIED - 3D norm conservation 2.55e-15

#### P30. `WaveFunction3D.normalize` - method

- **Definition:** `quantumlab/core/wavefunction.py:98`
- **Signature (verbatim):** `def normalize(self) -> 'WaveFunction3D':`
- **Input domain:** none
- **Output domain:** self
- **Mathematical definition:** psi/=sqrt(norm) if norm>0
- **Preconditions / postconditions enforced:** silent if norm==0
- **Actual callers:** benchmarks/validation_suite.py:112,201; examples/11:158
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99
- **Independent validation:** VERIFIED

#### P31. `WaveFunction3D.fourier_transform` - method

- **Definition:** `quantumlab/core/wavefunction.py:104`
- **Signature (verbatim):** `def fourier_transform(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** complex128 (N_x,N_y,N_z)
- **Mathematical definition:** fftn(psi)*dx*dy*dz/(2pi)^1.5
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables/expectation.py:77,106; observables/momentum.py:5
- **Test coverage:** indirect: tests/test_3d_observables.py::test_3d_momentum_probability_density:72
- **Independent validation:** VERIFIED - Parseval test

#### P32. `WaveFunction3D.copy` - method

- **Definition:** `quantumlab/core/wavefunction.py:107`
- **Signature (verbatim):** `def copy(self) -> 'WaveFunction3D':`
- **Input domain:** none
- **Output domain:** WaveFunction3D
- **Mathematical definition:** WaveFunction3D(grid, psi.copy())
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:156,166; benchmarks/perf_comparison.py
- **Test coverage:** tests/test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73
- **Independent validation:** PARTIALLY

#### P33. `WaveFunction3D.slice_xy` - method

- **Definition:** `quantumlab/core/wavefunction.py:110`
- **Signature (verbatim):** `def slice_xy(self, z_idx: int=None) -> np.ndarray:`
- **Input domain:** z_idx:int=None
- **Output domain:** float64 (N_x,N_y)
- **Mathematical definition:** probability_density[:,:,z_idx] (default N_z//2)
- **Preconditions / postconditions enforced:** ENFORCED: z_idx out of range -> IndexError (not guarded)
- **Actual callers:** TEST-ONLY: tests/test_3d_solver.py:63
- **Test coverage:** tests/test_3d_solver.py::test_3d_wavefunction_slices_shape:60
- **Independent validation:** PARTIALLY - shape only

#### P34. `WaveFunction3D.slice_xz` - method

- **Definition:** `quantumlab/core/wavefunction.py:116`
- **Signature (verbatim):** `def slice_xz(self, y_idx: int=None) -> np.ndarray:`
- **Input domain:** y_idx:int=None
- **Output domain:** float64 (N_x,N_z)
- **Mathematical definition:** probability_density[:,y_idx,:] (default N_y//2)
- **Preconditions / postconditions enforced:** not guarded
- **Actual callers:** TEST-ONLY: tests/test_3d_solver.py:64
- **Test coverage:** tests/test_3d_solver.py::test_3d_wavefunction_slices_shape:60
- **Independent validation:** PARTIALLY

#### P35. `WaveFunction3D.slice_yz` - method

- **Definition:** `quantumlab/core/wavefunction.py:122`
- **Signature (verbatim):** `def slice_yz(self, x_idx: int=None) -> np.ndarray:`
- **Input domain:** x_idx:int=None
- **Output domain:** float64 (N_y,N_z)
- **Mathematical definition:** probability_density[x_idx,:,:] (default N_x//2)
- **Preconditions / postconditions enforced:** not guarded
- **Actual callers:** TEST-ONLY: tests/test_3d_solver.py:65
- **Test coverage:** tests/test_3d_solver.py::test_3d_wavefunction_slices_shape:60
- **Independent validation:** PARTIALLY

#### P36. `WaveFunction3D.gaussian` - classmethod

- **Definition:** `quantumlab/core/wavefunction.py:129`
- **Signature (verbatim):** `def gaussian(cls, grid: Grid3D, x0: float, y0: float, z0: float,\n                 k0_x: float, k0_y: float, k0_z: float,\n                 sigma_x: float, sigma_y: float, sigma_z: float) -> 'WaveFunction3D':`
- **Input domain:** grid:Grid3D, x0,y0,z0,k0_x,k0_y,k0_z,sigma_x,sigma_y,sigma_z
- **Output domain:** WaveFunction3D normalised
- **Mathematical definition:** product of 3 1D Gaussians, then normalize
- **Preconditions / postconditions enforced:** sigma==0 not guarded
- **Actual callers:** runner.py; examples/06:33,07:59; benchmarks/validation_suite.py:85,102,136,191,285,297
- **Test coverage:** tests/test_3d_solver.py::test_3d_gaussian_norm:53; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24
- **Independent validation:** VERIFIED - minimum-uncertainty 3D check 4.6e-12


### `quantumlab/core/absorbing_boundary.py`

#### P37. `AbsorbingBoundaryLayer` - class

- **Definition:** `quantumlab/core/absorbing_boundary.py:6`
- **Signature (verbatim):** `class AbsorbingBoundaryLayer:`
- **Input domain:** grid:Grid1D/2D/3D, boundary_width:float, order:int=3
- **Output domain:** object; mask float64 grid.shape; boundary_width,order
- **Mathematical definition:** separable polynomial mask, 1 interior -> 0 at edges
- **Preconditions / postconditions enforced:** ENFORCED: boundary_width real finite >0 (TypeError/ValueError); order Integral >=1; grid type else TypeError
- **Actual callers:** runner.py:148; examples/05:42,06:43,07:60,12:64; benchmarks/validation_suite.py:221
- **Test coverage:** tests/test_absorbing_boundary_validation.py (all); test_2d_solver.py::test_absorbing_boundary_1d:36; test_3d_solver.py::test_abl_3d_shape:109; test_split_operator.py::test_absorber_removes_outgoing_flux:124
- **Independent validation:** VERIFIED - mask finiteness/monotonicity tests; HHG check uses absorber

#### P38. `AbsorbingBoundaryLayer.__init__` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:28`
- **Signature (verbatim):** `def __init__(self, grid, boundary_width: float, order: int = 3):`
- **Input domain:** grid, boundary_width:float, order:int=3
- **Output domain:** sets grid,boundary_width,order,mask
- **Mathematical definition:** validates then _build_mask()
- **Preconditions / postconditions enforced:** ENFORCED (see class)
- **Actual callers:** all AbsorbingBoundaryLayer(...) sites
- **Test coverage:** tests/test_absorbing_boundary_validation.py::test_valid_arguments_build_a_clean_mask:70
- **Independent validation:** VERIFIED - probe: orders 1..6 all finite, min 0.0 max 1.0

#### P39. `AbsorbingBoundaryLayer._polynomial_profile` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:53`
- **Signature (verbatim):** `def _polynomial_profile(self, d):`
- **Input domain:** d:ndarray
- **Output domain:** float64 same shape, in [0,1]
- **Mathematical definition:** clip(d,0,1); order<=3: d^2(3-2d); order==4: 6d^5-15d^4+10d^3; else Bernstein sum
- **Preconditions / postconditions enforced:** ENFORCED: clips d to [0,1]
- **Actual callers:** internal: _build_mask_1d:98,102; _2d:117,118,121,122; _3d:137,138,141,142,145,146
- **Test coverage:** indirect: tests/test_absorbing_boundary_validation.py::test_mask_is_monotone_from_edge_to_interior:89 (order 3); test_valid_arguments_build_a_clean_mask:70 (orders 1,3,4,6)
- **Independent validation:** PARTIALLY - orders 1..6 probed finite; general Bernstein branch only order 6 exercised

#### P40. `AbsorbingBoundaryLayer._binomial` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:75`
- **Signature (verbatim):** `def _binomial(self, n, k):`
- **Input domain:** n,k:int
- **Output domain:** int
- **Mathematical definition:** math.comb(n,k)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _polynomial_profile:69,70
- **Test coverage:** indirect: order>4 mask tests
- **Independent validation:** PARTIALLY

#### P41. `AbsorbingBoundaryLayer._build_mask` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:79`
- **Signature (verbatim):** `def _build_mask(self):`
- **Input domain:** none
- **Output domain:** float64 grid.shape
- **Mathematical definition:** dispatch on grid type
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported grid
- **Actual callers:** internal: __init__:51
- **Test coverage:** indirect: all ABL tests
- **Independent validation:** PARTIALLY

#### P42. `AbsorbingBoundaryLayer._build_mask_1d` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:90`
- **Signature (verbatim):** `def _build_mask_1d(self):`
- **Input domain:** none
- **Output domain:** float64 (N,)
- **Mathematical definition:** prod of left/right polynomial profiles; right_edge=x.max()+dx
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _build_mask:82
- **Test coverage:** indirect: tests/test_absorbing_boundary_validation.py::test_interior_is_unity_and_edges_are_absorbed:78
- **Independent validation:** VERIFIED - edge/interior/monotonicity tests

#### P43. `AbsorbingBoundaryLayer._build_mask_2d` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:106`
- **Signature (verbatim):** `def _build_mask_2d(self):`
- **Input domain:** none
- **Output domain:** float64 (N_x,N_y)
- **Mathematical definition:** outer product mask_x[:,None]*mask_y[None,:]
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _build_mask:84
- **Test coverage:** indirect: tests/test_2d_solver.py::test_absorbing_boundary_2d:46
- **Independent validation:** VERIFIED - 2D shape/edge test

#### P44. `AbsorbingBoundaryLayer._build_mask_3d` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:127`
- **Signature (verbatim):** `def _build_mask_3d(self):`
- **Input domain:** none
- **Output domain:** float64 (N_x,N_y,N_z)
- **Mathematical definition:** separable outer product over x,y,z
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _build_mask:86
- **Test coverage:** indirect: tests/test_3d_solver.py::test_abl_3d_corners_absorbed:123
- **Independent validation:** VERIFIED - 3D corner/interior tests

#### P45. `AbsorbingBoundaryLayer.apply` - method

- **Definition:** `quantumlab/core/absorbing_boundary.py:152`
- **Signature (verbatim):** `def apply(self, wavefunction):`
- **Input domain:** wavefunction
- **Output domain:** wavefunction (in-place; psi *= mask)
- **Mathematical definition:** psi *= mask
- **Preconditions / postconditions enforced:** ENFORCED: shape mismatch would broadcast-error (not explicit)
- **Actual callers:** runner.py:163; examples/05:55,06:49
- **Test coverage:** tests/test_2d_solver.py::test_abl_norm_decay:55; test_3d_solver.py::test_abl_3d_norm_decay:134; test_absorbing_boundary_validation.py::test_absorber_still_removes_probability:96
- **Independent validation:** VERIFIED - norm-decay tests; HHG flux absorption


### `quantumlab/core/spectral.py`

#### P46. `ndim` - function

- **Definition:** `quantumlab/core/spectral.py:11`
- **Signature (verbatim):** `def ndim(grid) -> int:`
- **Input domain:** grid:Grid1D/2D/3D
- **Output domain:** int 1/2/3
- **Mathematical definition:** isinstance dispatch
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported grid
- **Actual callers:** solvers/split_operator.py:115,173
- **Test coverage:** indirect: every solver/stationary test
- **Independent validation:** PARTIALLY

#### P47. `wavefunction_class` - function

- **Definition:** `quantumlab/core/spectral.py:21`
- **Signature (verbatim):** `def wavefunction_class(grid):`
- **Input domain:** grid
- **Output domain:** WaveFunction1D/2D/3D class
- **Mathematical definition:** {1:WF1D,2:WF2D,3:WF3D}[ndim(grid)]
- **Preconditions / postconditions enforced:** Propagates ndim TypeError
- **Actual callers:** solvers/split_operator.py:132; multicomponent.py:69; stationary/conjugate_gradient.py:132; eigensolver.py:99; imaginary_time.py:104,222
- **Test coverage:** indirect: all solver/stationary tests
- **Independent validation:** PARTIALLY

#### P48. `volume_element` - function

- **Definition:** `quantumlab/core/spectral.py:26`
- **Signature (verbatim):** `def volume_element(grid) -> float:`
- **Input domain:** grid
- **Output domain:** float dV
- **Mathematical definition:** dx | dx*dy | dx*dy*dz
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** observables/current.py:32,37; observables/nonlinear.py:8,29; solvers/multicomponent.py:68; split_operator.py:133; stationary/conjugate_gradient.py:50; eigensolver.py:98; imaginary_time.py:103,221; strongfield.py:132
- **Test coverage:** tests/test_stationary.py:10 (direct)
- **Independent validation:** VERIFIED - probe: 1.0,1.0,1.0 for unit cells

#### P49. `coordinates` - function

- **Definition:** `quantumlab/core/spectral.py:35`
- **Signature (verbatim):** `def coordinates(grid):`
- **Input domain:** grid
- **Output domain:** tuple of meshes
- **Mathematical definition:** (x,) | (X,Y) | (X,Y,Z)
- **Preconditions / postconditions enforced:** Propagates ndim TypeError
- **Actual callers:** potentials/coulomb.py:24; time_dependent.py:73,96; traps.py:28; stationary/imaginary_time.py:41
- **Test coverage:** indirect: potential tests
- **Independent validation:** PARTIALLY

#### P50. `wavevectors` - function

- **Definition:** `quantumlab/core/spectral.py:45`
- **Signature (verbatim):** `def wavevectors(grid):`
- **Input domain:** grid
- **Output domain:** tuple of k-meshes
- **Mathematical definition:** (k,) | (K_x,K_y) | (K_x,K_y,K_z) in FFT order
- **Preconditions / postconditions enforced:** Propagates ndim TypeError
- **Actual callers:** observables/current.py:14; spectral.k_squared:56
- **Test coverage:** indirect: probability_current tests
- **Independent validation:** PARTIALLY

#### P51. `k_squared` - function

- **Definition:** `quantumlab/core/spectral.py:55`
- **Signature (verbatim):** `def k_squared(grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** float64 grid.shape
- **Mathematical definition:** sum K_j^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers/split_operator.py:137; stationary/conjugate_gradient.py:52; eigensolver.py:48; hamiltonian.py:13
- **Test coverage:** indirect: all spectral checks
- **Independent validation:** VERIFIED - spectra/energies checks

#### P52. `k_volume_element` - function

- **Definition:** `quantumlab/core/spectral.py:59`
- **Signature (verbatim):** `def k_volume_element(grid) -> float:`
- **Input domain:** grid
- **Output domain:** float dk | dk_x*dk_y | dk_x*dk_y*dk_z
- **Mathematical definition:** product of grid dk's
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE - zero references anywhere in repo
- **Test coverage:** NONE
- **Independent validation:** NONE - dead code (probe confirms it computes, but nothing consumes it)


### `quantumlab/potentials/base.py`

#### P53. `Potential` - class

- **Definition:** `quantumlab/potentials/base.py:4`
- **Signature (verbatim):** `class Potential(ABC):`
- **Input domain:** abstract
- **Output domain:** abstract base
- **Mathematical definition:** interface: evaluate(grid)->ndarray
- **Preconditions / postconditions enforced:** abstractmethod evaluate
- **Actual callers:** subclassed at potentials/barriers.py:5,20,35,47,68,96,133; wells.py:5,20,35; oscillator.py:5; periodic.py:5; disorder.py:5; custom.py:5; traps.py:6; coulomb.py:6; apertures.py:11,79; time_dependent.py:16
- **Test coverage:** NONE (abstract; exercised through subclasses)
- **Independent validation:** PARTIALLY - contract enforced by subclass tests

#### P54. `Potential.evaluate` - method (abstractmethod)

- **Definition:** `quantumlab/potentials/base.py:7`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** ndarray
- **Mathematical definition:** abstract
- **Preconditions / postconditions enforced:** abstractmethod
- **Actual callers:** called dynamically at solvers/split_operator.py:143; split_step_1d.py:10; 2d:19; 3d:41; 3d_gpu:60,68; multicomponent.py:71; stationary/*; observables/expectation.py:143; visualization/*
- **Test coverage:** tests/test_potentials.py (all); test_new_potentials_and_observables.py (all)
- **Independent validation:** VERIFIED - through concrete potential tests


### `quantumlab/potentials/apertures.py`

#### P55. `_smooth_step` - function

- **Definition:** `quantumlab/potentials/apertures.py:6`
- **Signature (verbatim):** `def _smooth_step(u):`
- **Input domain:** u:ndarray
- **Output domain:** float64 same shape in (0,1)
- **Mathematical definition:** 0.5*(1+tanh(u))
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: ApertureScreen.evaluate:65,74; StadiumBilliard.evaluate:102
- **Test coverage:** indirect: aperture/stadium tests
- **Independent validation:** PARTIALLY

#### P56. `ApertureScreen` - class

- **Definition:** `quantumlab/potentials/apertures.py:11`
- **Signature (verbatim):** `class ApertureScreen(Potential):`
- **Input domain:** V0, wall_position=0, wall_thickness=1, separation=4, aperture_width=1, n_apertures=2, aperture='slit', smoothing=0.25
- **Output domain:** object; V array
- **Mathematical definition:** opaque screen with n smoothed openings
- **Preconditions / postconditions enforced:** ENFORCED: aperture in {'slit','pinhole'} else ValueError
- **Actual callers:** examples/07_3d_double_slit.py:50; registry potentials/__init__.py:35,36
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26; test_aperture_screen_slits_are_translation_invariant_in_z:41; test_volume_3d.py::test_renderer_writes_png:43
- **Independent validation:** PARTIALLY - geometry tests, no analytic reference

#### P57. `ApertureScreen.__init__` - method

- **Definition:** `quantumlab/potentials/apertures.py:40`
- **Signature (verbatim):** `def __init__(self, V0: float, wall_position: float = 0.0, wall_thickness: float = 1.0,\n                 separation: float = 4.0, aperture_width: float = 1.0, n_apertures: int = 2,\n                 aperture: str = 'slit', smoothing: float = 0.25):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** validation of aperture string
- **Preconditions / postconditions enforced:** ENFORCED aperture string
- **Actual callers:** all ApertureScreen(...) sites
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26
- **Independent validation:** PARTIALLY

#### P58. `ApertureScreen.aperture_centers` - property

- **Definition:** `quantumlab/potentials/apertures.py:55`
- **Signature (verbatim):** `def aperture_centers(self) -> np.ndarray:`
- **Input domain:** none
- **Output domain:** float64 (n_apertures,)
- **Mathematical definition:** (i-(n-1)/2)*separation
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: evaluate:69; tests/test_new_potentials_and_observables.py:38
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26
- **Independent validation:** PARTIALLY

#### P59. `ApertureScreen.evaluate` - method

- **Definition:** `quantumlab/potentials/apertures.py:59`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid2D/Grid3D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V0*wall*(1-opening); wall=smoothstep pair; opening=sum of smoothstep slits/pinholes clipped
- **Preconditions / postconditions enforced:** ENFORCED: TypeError if not Grid2D/Grid3D
- **Actual callers:** solvers (dynamic); tests/test_new_potentials_and_observables.py:30,43
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26; test_aperture_screen_slits_are_translation_invariant_in_z:41
- **Independent validation:** PARTIALLY

#### P60. `StadiumBilliard` - class

- **Definition:** `quantumlab/potentials/apertures.py:79`
- **Signature (verbatim):** `class StadiumBilliard(Potential):`
- **Input domain:** V0, radius, length, smoothing=0.2
- **Output domain:** object
- **Mathematical definition:** soft-walled stadium potential
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/10_quantum_chaos_stadium.py:35; registry potentials/__init__.py:37
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_stadium_is_open_inside_and_closed_outside:47; test_stationary.py::test_lanczos_and_lobpcg_agree_on_chaotic_billiard:38
- **Independent validation:** PARTIALLY - geometry + cross-solver agreement, no analytic energies

#### P61. `StadiumBilliard.__init__` - method

- **Definition:** `quantumlab/potentials/apertures.py:90`
- **Signature (verbatim):** `def __init__(self, V0: float, radius: float, length: float, smoothing: float = 0.2):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all StadiumBilliard(...) sites
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_stadium_is_open_inside_and_closed_outside:47
- **Independent validation:** PARTIALLY

#### P62. `StadiumBilliard.evaluate` - method

- **Definition:** `quantumlab/potentials/apertures.py:96`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid2D
- **Output domain:** float64 (N_x,N_y)
- **Mathematical definition:** V0*smoothstep((dist-R)/s), dist=distance to segment [-L/2,L/2] on x
- **Preconditions / postconditions enforced:** ENFORCED: TypeError if not Grid2D
- **Actual callers:** solvers (dynamic); tests/test_new_potentials_and_observables.py:49; test_stationary.py:40
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_stadium_is_open_inside_and_closed_outside:47; test_stationary.py::test_lanczos_and_lobpcg_agree_on_chaotic_billiard:38
- **Independent validation:** PARTIALLY


### `quantumlab/potentials/barriers.py`

#### P63. `GaussianBarrier` - class

- **Definition:** `quantumlab/potentials/barriers.py:5`
- **Signature (verbatim):** `class GaussianBarrier(Potential):`
- **Input domain:** V0, width, position=0
- **Output domain:** object
- **Mathematical definition:** V0*exp(-((x-position)/width)^2)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/01_gaussian_barrier.py:32; testbench_interlock.py:99; registry potentials/__init__.py:20,21
- **Test coverage:** tests/test_potentials.py::test_gaussian_barrier:12; test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_norm_and_energy_conservation:50
- **Independent validation:** PARTIALLY - peak/edge assertions only

#### P64. `GaussianBarrier.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:7`
- **Signature (verbatim):** `def __init__(self, V0: float, width: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all GaussianBarrier(...) sites
- **Test coverage:** tests/test_potentials.py::test_gaussian_barrier:12
- **Independent validation:** PARTIALLY

#### P65. `GaussianBarrier.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:12`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D/3D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V0*exp(-((X-position)/width)^2)
- **Preconditions / postconditions enforced:** NONE (accepts any grid type; no validation)
- **Actual callers:** solvers (dynamic); tests/test_potentials.py:18; test_solvers.py:12,23
- **Test coverage:** tests/test_potentials.py::test_gaussian_barrier:12; test_solvers.py::test_energy_conservation:20
- **Independent validation:** PARTIALLY

#### P66. `RectangularBarrier` - class

- **Definition:** `quantumlab/potentials/barriers.py:20`
- **Signature (verbatim):** `class RectangularBarrier(Potential):`
- **Input domain:** V0, width, position=0
- **Output domain:** object
- **Mathematical definition:** rectangular barrier
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** registry potentials/__init__.py:24
- **Test coverage:** tests/test_potentials.py::test_rectangular_barrier:25
- **Independent validation:** PARTIALLY

#### P67. `RectangularBarrier.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:22`
- **Signature (verbatim):** `def __init__(self, V0: float, width: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** tests/test_potentials.py:30
- **Test coverage:** tests/test_potentials.py::test_rectangular_barrier:25
- **Independent validation:** PARTIALLY

#### P68. `RectangularBarrier.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:27`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D/3D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** where(|x-position|<=width/2, V0, 0)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic); tests/test_potentials.py:31
- **Test coverage:** tests/test_potentials.py::test_rectangular_barrier:25
- **Independent validation:** PARTIALLY

#### P69. `PotentialStep` - class

- **Definition:** `quantumlab/potentials/barriers.py:35`
- **Signature (verbatim):** `class PotentialStep(Potential):`
- **Input domain:** V0, position=0
- **Output domain:** object
- **Mathematical definition:** step potential
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (registry-only: potentials/__init__.py:25)
- **Test coverage:** NONE (imported unused at tests/test_potentials.py:4)
- **Independent validation:** NONE

#### P70. `PotentialStep.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:37`
- **Signature (verbatim):** `def __init__(self, V0: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P71. `PotentialStep.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:41`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** float64 grid.shape
- **Mathematical definition:** where(x>=position, V0, 0)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P72. `MultipleBarriers` - class

- **Definition:** `quantumlab/potentials/barriers.py:47`
- **Signature (verbatim):** `class MultipleBarriers(Potential):`
- **Input domain:** V0, width, positions:list
- **Output domain:** object
- **Mathematical definition:** sum of rectangles
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/04_multiple_barriers.py:33; registry potentials/__init__.py:26
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P73. `MultipleBarriers.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:49`
- **Signature (verbatim):** `def __init__(self, V0: float, width: float, positions: list):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/04_multiple_barriers.py:33
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P74. `MultipleBarriers.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:54`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V[pos-width/2<=x<=pos+width/2]=V0 for each pos
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic); examples/04:40
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P75. `ResonantTunnelingDiode` - class

- **Definition:** `quantumlab/potentials/barriers.py:68`
- **Signature (verbatim):** `class ResonantTunnelingDiode(Potential):`
- **Input domain:** V0, barrier_width, well_width, position=0
- **Output domain:** object
- **Mathematical definition:** double barrier
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (registry-only: potentials/__init__.py:27)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P76. `ResonantTunnelingDiode.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:70`
- **Signature (verbatim):** `def __init__(self, V0: float, barrier_width: float, well_width: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P77. `ResonantTunnelingDiode.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:76`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** float64 grid.shape
- **Mathematical definition:** two barriers at pos_left/pos_right
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P78. `Gaussian2DBarrier` - class

- **Definition:** `quantumlab/potentials/barriers.py:96`
- **Signature (verbatim):** `class Gaussian2DBarrier(Potential):`
- **Input domain:** V0, width, x0=0, y0=0
- **Output domain:** object
- **Mathematical definition:** isotropic 2D Gaussian
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/05_2d_gaussian_barrier.py:40; registry potentials/__init__.py:22
- **Test coverage:** tests/test_split_operator.py::test_order2_matches_legacy_solvers:26
- **Independent validation:** PARTIALLY

#### P79. `Gaussian2DBarrier.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:117`
- **Signature (verbatim):** `def __init__(self, V0: float, width: float, x0: float = 0.0, y0: float = 0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** tests/test_split_operator.py:34
- **Test coverage:** tests/test_split_operator.py::test_order2_matches_legacy_solvers:26
- **Independent validation:** PARTIALLY

#### P80. `Gaussian2DBarrier.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:123`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid2D/3D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V0*exp(-((X-x0)^2+(Y-y0)^2)/width^2)
- **Preconditions / postconditions enforced:** ENFORCED: TypeError if not 2D/3D
- **Actual callers:** solvers (dynamic); tests/test_split_operator.py:34
- **Test coverage:** tests/test_split_operator.py::test_order2_matches_legacy_solvers:26
- **Independent validation:** PARTIALLY

#### P81. `Gaussian3DBarrier` - class

- **Definition:** `quantumlab/potentials/barriers.py:133`
- **Signature (verbatim):** `class Gaussian3DBarrier(Potential):`
- **Input domain:** V0, width, x0=0,y0=0,z0=0
- **Output domain:** object
- **Mathematical definition:** isotropic 3D Gaussian
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/06_3d_gaussian_barrier.py:41; benchmarks/perf_comparison.py:91; registry potentials/__init__.py:23
- **Test coverage:** tests/test_3d_solver.py::test_gaussian3d_barrier_peak:152; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_split_operator.py::test_order2_matches_legacy_solvers:26
- **Independent validation:** PARTIALLY

#### P82. `Gaussian3DBarrier.__init__` - method

- **Definition:** `quantumlab/potentials/barriers.py:149`
- **Signature (verbatim):** `def __init__(self, V0: float, width: float,\n                 x0: float = 0.0, y0: float = 0.0, z0: float = 0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** tests/test_3d_solver.py:155,166
- **Test coverage:** tests/test_3d_solver.py::test_gaussian3d_barrier_symmetry:163
- **Independent validation:** PARTIALLY

#### P83. `Gaussian3DBarrier.evaluate` - method

- **Definition:** `quantumlab/potentials/barriers.py:157`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid3D
- **Output domain:** float64 (N_x,N_y,N_z)
- **Mathematical definition:** V0*exp(-r^2/width^2)
- **Preconditions / postconditions enforced:** ENFORCED: TypeError if not Grid3D
- **Actual callers:** solvers (dynamic); tests/test_3d_solver.py:156,167
- **Test coverage:** tests/test_3d_solver.py::test_gaussian3d_barrier_peak:152; test_gaussian3d_barrier_symmetry:163
- **Independent validation:** PARTIALLY


### `quantumlab/potentials/coulomb.py`

#### P84. `SoftCoulomb` - class

- **Definition:** `quantumlab/potentials/coulomb.py:6`
- **Signature (verbatim):** `class SoftCoulomb(Potential):`
- **Input domain:** Z=1.0, softening=sqrt(2), center=None
- **Output domain:** object
- **Mathematical definition:** soft-core Coulomb potential
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:210,312; examples/12:86; registry potentials/__init__.py:38
- **Test coverage:** tests/test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33; test_soft_coulomb_gradient_matches_finite_difference:40; test_conjugate_gradient.py::test_linear_ground_states_to_machine_precision:19
- **Independent validation:** VERIFIED - hydrogen E0=-0.5 to 1.94e-14; gradient vs finite difference

#### P85. `SoftCoulomb.__init__` - method

- **Definition:** `quantumlab/potentials/coulomb.py:18`
- **Signature (verbatim):** `def __init__(self, Z: float = 1.0, softening: float = np.sqrt(2.0), center=None):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all SoftCoulomb(...) sites
- **Test coverage:** tests/test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33
- **Independent validation:** VERIFIED

#### P86. `SoftCoulomb._displacements` - method

- **Definition:** `quantumlab/potentials/coulomb.py:23`
- **Signature (verbatim):** `def _displacements(self, grid):`
- **Input domain:** grid
- **Output domain:** tuple of arrays
- **Mathematical definition:** coords - center (broadcast)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: evaluate:30; gradient:35
- **Test coverage:** indirect: SoftCoulomb tests
- **Independent validation:** PARTIALLY

#### P87. `SoftCoulomb.evaluate` - method

- **Definition:** `quantumlab/potentials/coulomb.py:29`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** float64 grid.shape
- **Mathematical definition:** -Z/sqrt(r^2+a^2)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic); tests/test_strongfield.py:44
- **Test coverage:** tests/test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33; test_soft_coulomb_gradient_matches_finite_difference:40
- **Independent validation:** VERIFIED - hydrogen ground state 1.94e-14; probe V(0)=-0.7071 for a=sqrt2

#### P88. `SoftCoulomb.gradient` - method

- **Definition:** `quantumlab/potentials/coulomb.py:33`
- **Signature (verbatim):** `def gradient(self, grid):`
- **Input domain:** grid
- **Output domain:** tuple of float64 arrays
- **Mathematical definition:** Z*d_i/(r^2+a^2)^1.5
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** strongfield.py:127; tests/test_strongfield.py:45
- **Test coverage:** tests/test_strongfield.py::test_soft_coulomb_gradient_matches_finite_difference:40
- **Independent validation:** VERIFIED - finite-difference comparison atol 1e-3


### `quantumlab/potentials/custom.py`

#### P89. `CustomPotential` - class

- **Definition:** `quantumlab/potentials/custom.py:5`
- **Signature (verbatim):** `class CustomPotential(Potential):`
- **Input domain:** func:callable
- **Output domain:** object
- **Mathematical definition:** user potential
- **Preconditions / postconditions enforced:** ENFORCED callable
- **Actual callers:** benchmarks/validation_suite.py:53; tests/test_split_operator.py:67,82
- **Test coverage:** tests/test_potentials.py::test_custom_potential:45; test_new_potentials_and_observables.py::test_custom_potential_3d:57; test_split_operator.py::test_convergence_order:64
- **Independent validation:** VERIFIED - convergence-order check uses CustomPotential

#### P90. `CustomPotential.__init__` - method

- **Definition:** `quantumlab/potentials/custom.py:7`
- **Signature (verbatim):** `def __init__(self, func):`
- **Input domain:** func
- **Output domain:** sets func
- **Mathematical definition:** stores func; no evaluation
- **Preconditions / postconditions enforced:** ENFORCED TypeError if not callable
- **Actual callers:** all CustomPotential(...) sites
- **Test coverage:** tests/test_potentials.py::test_custom_potential:45
- **Independent validation:** PARTIALLY

#### P91. `CustomPotential.evaluate` - method

- **Definition:** `quantumlab/potentials/custom.py:12`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D/3D
- **Output domain:** ndarray
- **Mathematical definition:** func(x) | func(X,Y) | func(X,Y,Z)
- **Preconditions / postconditions enforced:** NONE (return type/shape not validated)
- **Actual callers:** solvers (dynamic); tests/test_potentials.py:49; test_new_potentials_and_observables.py:59
- **Test coverage:** tests/test_potentials.py::test_custom_potential:45; test_new_potentials_and_observables.py::test_custom_potential_3d:57
- **Independent validation:** PARTIALLY


### `quantumlab/potentials/disorder.py`

#### P92. `RandomDisorder` - class

- **Definition:** `quantumlab/potentials/disorder.py:5`
- **Signature (verbatim):** `class RandomDisorder(Potential):`
- **Input domain:** W, cell_width, seed=None
- **Output domain:** object
- **Mathematical definition:** piecewise-constant random disorder
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (registry-only: potentials/__init__.py:33; imported unused at tests/test_potentials.py:8)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P93. `RandomDisorder.__init__` - method

- **Definition:** `quantumlab/potentials/disorder.py:7`
- **Signature (verbatim):** `def __init__(self, W: float, cell_width: float, seed: int=None):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P94. `RandomDisorder.evaluate` - method

- **Definition:** `quantumlab/potentials/disorder.py:12`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** rng.uniform(-W/2,W/2,num_cells)[cell index]
- **Preconditions / postconditions enforced:** NONE (seed=None -> nondeterministic)
- **Actual callers:** NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- **Test coverage:** NONE
- **Independent validation:** NONE


### `quantumlab/potentials/oscillator.py`

#### P95. `HarmonicOscillator` - class

- **Definition:** `quantumlab/potentials/oscillator.py:5`
- **Signature (verbatim):** `class HarmonicOscillator(Potential):`
- **Input domain:** omega, m=1, position=0
- **Output domain:** object
- **Mathematical definition:** harmonic potential
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/02_harmonic_oscillator.py:30; registry potentials/__init__.py:31
- **Test coverage:** tests/test_potentials.py::test_harmonic_oscillator:36; test_2d_solver.py::test_2d_energy_conservation:23; test_3d_solver.py::test_3d_energy_conservation_harmonic:86
- **Independent validation:** PARTIALLY - analytic 1D formula asserted

#### P96. `HarmonicOscillator.__init__` - method

- **Definition:** `quantumlab/potentials/oscillator.py:7`
- **Signature (verbatim):** `def __init__(self, omega: float, m: float=1.0, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all HarmonicOscillator(...) sites
- **Test coverage:** tests/test_potentials.py::test_harmonic_oscillator:36
- **Independent validation:** PARTIALLY

#### P97. `HarmonicOscillator.evaluate` - method

- **Definition:** `quantumlab/potentials/oscillator.py:12`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D/3D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** 0.5*m*omega^2*(x-position)^2 (sum over axes)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic); tests/test_potentials.py:41
- **Test coverage:** tests/test_potentials.py::test_harmonic_oscillator:36; test_2d_solver.py::test_2d_energy_conservation:23
- **Independent validation:** VERIFIED - analytic 1D formula allclose; 2D/3D energy conservation


### `quantumlab/potentials/periodic.py`

#### P98. `CrystalPotential` - class

- **Definition:** `quantumlab/potentials/periodic.py:5`
- **Signature (verbatim):** `class CrystalPotential(Potential):`
- **Input domain:** V0, lattice_spacing, position=0
- **Output domain:** object
- **Mathematical definition:** sin^2 lattice
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (registry-only: potentials/__init__.py:32; imported unused at tests/test_potentials.py:7)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P99. `CrystalPotential.__init__` - method

- **Definition:** `quantumlab/potentials/periodic.py:7`
- **Signature (verbatim):** `def __init__(self, V0: float, lattice_spacing: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P100. `CrystalPotential.evaluate` - method

- **Definition:** `quantumlab/potentials/periodic.py:12`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V0*sin(pi*(x-position)/lattice_spacing)^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- **Test coverage:** NONE
- **Independent validation:** NONE


### `quantumlab/potentials/time_dependent.py`

#### P101. `TimeDependentPotential` - class

- **Definition:** `quantumlab/potentials/time_dependent.py:16`
- **Signature (verbatim):** `class TimeDependentPotential(Potential):`
- **Input domain:** abstract
- **Output domain:** abstract base; time_dependent=True
- **Mathematical definition:** interface evaluate_at(grid,t)
- **Preconditions / postconditions enforced:** abstractmethod evaluate_at; evaluate(grid)=evaluate_at(grid,0)
- **Actual callers:** subclassed at time_dependent.py:27,87
- **Test coverage:** NONE (abstract; exercised through DipoleDrive/TimeDependentCustomPotential)
- **Independent validation:** PARTIALLY

#### P102. `TimeDependentPotential.evaluate_at` - method (abstractmethod)

- **Definition:** `quantumlab/potentials/time_dependent.py:20`
- **Signature (verbatim):** `def evaluate_at(self, grid, t: float) -> np.ndarray:`
- **Input domain:** grid, t:float
- **Output domain:** ndarray
- **Mathematical definition:** abstract
- **Preconditions / postconditions enforced:** abstractmethod
- **Actual callers:** solvers/split_operator.py:191 (dynamic dispatch)
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69; test_dipole_drive_rejects_missing_axis:79
- **Independent validation:** VERIFIED - driven-oscillator Ehrenfest check 5.60e-09

#### P103. `TimeDependentPotential.evaluate` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:23`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid
- **Output domain:** ndarray
- **Mathematical definition:** evaluate_at(grid, 0.0)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE established (subclasses override evaluate_at; generic .evaluate sites target static potentials)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P104. `DipoleDrive` - class

- **Definition:** `quantumlab/potentials/time_dependent.py:27`
- **Signature (verbatim):** `class DipoleDrive(TimeDependentPotential):`
- **Input domain:** base:Potential|None, F0, omega, axis='x', phase=0, envelope=None
- **Output domain:** object; time_dependent=True
- **Mathematical definition:** V(r,t)=V_base(r)-F(t)*r_axis; F(t)=F0*env(t)*sin(omega t+phase)
- **Preconditions / postconditions enforced:** ENFORCED axis in {x,y,z} else ValueError; axis availability checked at evaluate time
- **Actual callers:** benchmarks/validation_suite.py:70,219; examples/12:63; tests/test_split_operator.py:93,107,141
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69; test_split_operator.py::test_driven_oscillator_follows_classical_trajectory:90
- **Independent validation:** VERIFIED - Ehrenfest driven oscillator 5.60e-09; HHG odd-harmonic check

#### P105. `DipoleDrive.__init__` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:53`
- **Signature (verbatim):** `def __init__(self, base: Optional[Potential], F0: float, omega: float,\n                 axis: str = 'x', phase: float = 0.0,\n                 envelope: Optional[Callable[[float], float]] = None):`
- **Input domain:** see class
- **Output domain:** sets fields + cache
- **Mathematical definition:** stores base/F0/omega/axis/phase/envelope; initialises cache
- **Preconditions / postconditions enforced:** ENFORCED axis
- **Actual callers:** all DipoleDrive(...) sites
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_dipole_drive_rejects_missing_axis:79
- **Independent validation:** PARTIALLY

#### P106. `DipoleDrive.force` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:67`
- **Signature (verbatim):** `def force(self, t: float) -> float:`
- **Input domain:** t:float
- **Output domain:** float
- **Mathematical definition:** F0*env(t)*sin(omega*t+phase)
- **Preconditions / postconditions enforced:** ENFORCED: envelope must be callable if given (not validated)
- **Actual callers:** strongfield callbacks; examples/12:68,198,218,233,245; benchmarks/validation_suite.py:224
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69
- **Independent validation:** VERIFIED - driven oscillator + HHG

#### P107. `DipoleDrive._static_parts` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:71`
- **Signature (verbatim):** `def _static_parts(self, grid):`
- **Input domain:** grid
- **Output domain:** tuple (V_base, r_axis)
- **Mathematical definition:** cached base potential and axis coordinate
- **Preconditions / postconditions enforced:** ENFORCED: ValueError if axis unavailable on grid
- **Actual callers:** internal: evaluate_at:83
- **Test coverage:** indirect: DipoleDrive tests
- **Independent validation:** PARTIALLY

#### P108. `DipoleDrive.evaluate_at` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:82`
- **Signature (verbatim):** `def evaluate_at(self, grid, t: float) -> np.ndarray:`
- **Input domain:** grid, t:float
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V_base - force(t)*r_axis
- **Preconditions / postconditions enforced:** ENFORCED axis (via _static_parts)
- **Actual callers:** solvers/split_operator.py:191 (dynamic); tests/test_new_potentials_and_observables.py:76,81
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69; test_dipole_drive_rejects_missing_axis:79
- **Independent validation:** VERIFIED - driven oscillator Ehrenfest

#### P109. `TimeDependentCustomPotential` - class

- **Definition:** `quantumlab/potentials/time_dependent.py:87`
- **Signature (verbatim):** `class TimeDependentCustomPotential(TimeDependentPotential):`
- **Input domain:** func:callable
- **Output domain:** object
- **Mathematical definition:** user V(r,t)
- **Preconditions / postconditions enforced:** ENFORCED callable
- **Actual callers:** tests/test_split_operator.py:108; registry via potentials/__init__.py:15 export
- **Test coverage:** tests/test_split_operator.py::test_time_dependent_custom_potential_matches_dipole_drive:104
- **Independent validation:** PARTIALLY - cross-check vs DipoleDrive

#### P110. `TimeDependentCustomPotential.__init__` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:90`
- **Signature (verbatim):** `def __init__(self, func: Callable):`
- **Input domain:** func
- **Output domain:** sets func
- **Mathematical definition:** stores func; evaluate_at broadcasts func(*coords,t)
- **Preconditions / postconditions enforced:** ENFORCED TypeError
- **Actual callers:** tests/test_split_operator.py:108
- **Test coverage:** tests/test_split_operator.py::test_time_dependent_custom_potential_matches_dipole_drive:104
- **Independent validation:** PARTIALLY

#### P111. `TimeDependentCustomPotential.evaluate_at` - method

- **Definition:** `quantumlab/potentials/time_dependent.py:95`
- **Signature (verbatim):** `def evaluate_at(self, grid, t: float) -> np.ndarray:`
- **Input domain:** grid, t:float
- **Output domain:** float64 grid.shape
- **Mathematical definition:** broadcast_to(func(*coordinates,t), grid.shape).astype(float)
- **Preconditions / postconditions enforced:** ENFORCED: broadcast error if shape mismatch
- **Actual callers:** solvers/split_operator.py:191 (dynamic)
- **Test coverage:** tests/test_split_operator.py::test_time_dependent_custom_potential_matches_dipole_drive:104
- **Independent validation:** PARTIALLY

#### P112. `sin2_envelope` - function

- **Definition:** `quantumlab/potentials/time_dependent.py:99`
- **Signature (verbatim):** `def sin2_envelope(duration: float) -> Callable[[float], float]:`
- **Input domain:** duration:float
- **Output domain:** callable t->float in [0,1]
- **Mathematical definition:** sin^2(pi t/duration) on (0,duration), else 0
- **Preconditions / postconditions enforced:** ENFORRED: duration<=0 -> division issues (not guarded)
- **Actual callers:** tests/test_new_potentials_and_observables.py:70
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69
- **Independent validation:** PARTIALLY

#### P113. `flat_top_envelope` - function

- **Definition:** `quantumlab/potentials/time_dependent.py:108`
- **Signature (verbatim):** `def flat_top_envelope(duration: float, ramp: float) -> Callable[[float], float]:`
- **Input domain:** duration:float, ramp:float
- **Output domain:** callable t->float in [0,1]
- **Mathematical definition:** sin^2 ramps of length ramp, flat 1 between, 0 outside
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 0 < 2*ramp <= duration
- **Actual callers:** benchmarks/validation_suite.py:220; examples/12:63
- **Test coverage:** tests/test_strongfield.py::test_flat_top_envelope:50
- **Independent validation:** VERIFIED - used in HHG validation (odd harmonics, attosecond train)


### `quantumlab/potentials/traps.py`

#### P114. `HarmonicTrap` - class

- **Definition:** `quantumlab/potentials/traps.py:6`
- **Signature (verbatim):** `class HarmonicTrap(Potential):`
- **Input domain:** omegas:float|seq, m=1.0, center=None
- **Output domain:** object
- **Mathematical definition:** anisotropic harmonic trap
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py (many); examples/08:48,74,11:68,71,155,13:68,197,198; benchmarks/gpu_split_operator.py:25
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_harmonic_trap_isotropic_matches_oscillator:15; test_harmonic_trap_anisotropic_and_centered:20; test_stationary.py::test_1d_harmonic_spectrum_lanczos:14
- **Independent validation:** VERIFIED - harmonic spectra exact to 7.28e-14; GP virial

#### P115. `HarmonicTrap.__init__` - method

- **Definition:** `quantumlab/potentials/traps.py:22`
- **Signature (verbatim):** `def __init__(self, omegas, m: float = 1.0, center=None):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all HarmonicTrap(...) sites
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_harmonic_trap_anisotropic_and_centered:20
- **Independent validation:** PARTIALLY

#### P116. `HarmonicTrap.evaluate` - method

- **Definition:** `quantumlab/potentials/traps.py:27`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D/3D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** 0.5*m*sum_j omega_j^2 (r_j-c_j)^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic); tests/test_new_potentials_and_observables.py:17,22
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_harmonic_trap_isotropic_matches_oscillator:15; test_stationary.py::test_1d_harmonic_spectrum_lanczos:14
- **Independent validation:** VERIFIED - exact spectra, virial, rotating frame


### `quantumlab/potentials/wells.py`

#### P117. `InfiniteSquareWell` - class

- **Definition:** `quantumlab/potentials/wells.py:5`
- **Signature (verbatim):** `class InfiniteSquareWell(Potential):`
- **Input domain:** width, position=0, V_inf=1e9
- **Output domain:** object
- **Mathematical definition:** infinite well
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (registry-only: potentials/__init__.py:28)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P118. `InfiniteSquareWell.__init__` - method

- **Definition:** `quantumlab/potentials/wells.py:7`
- **Signature (verbatim):** `def __init__(self, width: float, position: float=0.0, V_inf: float=1000000000.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P119. `InfiniteSquareWell.evaluate` - method

- **Definition:** `quantumlab/potentials/wells.py:12`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** 0 inside |x-position|<=width/2 else V_inf
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P120. `FiniteSquareWell` - class

- **Definition:** `quantumlab/potentials/wells.py:20`
- **Signature (verbatim):** `class FiniteSquareWell(Potential):`
- **Input domain:** V0, width, position=0
- **Output domain:** object
- **Mathematical definition:** finite well
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** registry potentials/__init__.py:29
- **Test coverage:** tests/test_potentials.py::test_potential_factory:52
- **Independent validation:** PARTIALLY - factory/attrs only

#### P121. `FiniteSquareWell.__init__` - method

- **Definition:** `quantumlab/potentials/wells.py:22`
- **Signature (verbatim):** `def __init__(self, V0: float, width: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** tests/test_potentials.py:53
- **Test coverage:** tests/test_potentials.py::test_potential_factory:52
- **Independent validation:** PARTIALLY

#### P122. `FiniteSquareWell.evaluate` - method

- **Definition:** `quantumlab/potentials/wells.py:27`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** 0 inside well else V0
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic, generic .evaluate only)
- **Test coverage:** tests/test_potentials.py::test_potential_factory:52 (indirect)
- **Independent validation:** PARTIALLY

#### P123. `DoubleWell` - class

- **Definition:** `quantumlab/potentials/wells.py:35`
- **Signature (verbatim):** `class DoubleWell(Potential):`
- **Input domain:** V0, barrier_distance, position=0
- **Output domain:** object
- **Mathematical definition:** quartic double well
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/03_double_well.py:31; registry potentials/__init__.py:30
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P124. `DoubleWell.__init__` - method

- **Definition:** `quantumlab/potentials/wells.py:37`
- **Signature (verbatim):** `def __init__(self, V0: float, barrier_distance: float, position: float=0.0):`
- **Input domain:** see class
- **Output domain:** sets fields
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/03_double_well.py:31
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P125. `DoubleWell.evaluate` - method

- **Definition:** `quantumlab/potentials/wells.py:42`
- **Signature (verbatim):** `def evaluate(self, grid) -> np.ndarray:`
- **Input domain:** grid:Grid1D/2D
- **Output domain:** float64 grid.shape
- **Mathematical definition:** V0*((x-position)/barrier_distance)^2-1)^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** solvers (dynamic); examples/03:40
- **Test coverage:** NONE
- **Independent validation:** NONE


### `quantumlab/potentials/__init__.py`

#### P126. `create_potential` - function

- **Definition:** `quantumlab/potentials/__init__.py:41`
- **Signature (verbatim):** `def create_potential(name: str, **kwargs) -> Potential:`
- **Input domain:** name:str, **kwargs
- **Output domain:** Potential instance
- **Mathematical definition:** POTENTIAL_REGISTRY[name.lower()](**kwargs)
- **Preconditions / postconditions enforced:** ENFORCED: ValueError if name unknown
- **Actual callers:** runner.py:141
- **Test coverage:** tests/test_potentials.py::test_potential_factory:52; test_new_potentials_and_observables.py::test_registry_has_new_potentials:63; test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33
- **Independent validation:** PARTIALLY - registry dispatch tested; physics of each entry tested separately


### `quantumlab/solvers/base.py`

#### P127. `Solver` - class

- **Definition:** `quantumlab/solvers/base.py:3`
- **Signature (verbatim):** `class Solver(ABC):`
- **Input domain:** grid, potential, dt, hbar=1, m=1
- **Output domain:** abstract base
- **Mathematical definition:** interface step(wavefunction); backend property
- **Preconditions / postconditions enforced:** abstractmethod step
- **Actual callers:** subclassed at split_operator.py:42; split_step_1d.py:6; 2d:6; 3d:7; 3d_gpu:25
- **Test coverage:** NONE (abstract; exercised through subclasses)
- **Independent validation:** PARTIALLY

#### P128. `Solver.__init__` - method

- **Definition:** `quantumlab/solvers/base.py:5`
- **Signature (verbatim):** `def __init__(self, grid, potential, dt: float, hbar: float=1.0, m: float=1.0):`
- **Input domain:** grid, potential, dt, hbar=1, m=1
- **Output domain:** sets grid,potential,dt,hbar,m
- **Mathematical definition:** plain assignment
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** super().__init__ at split_operator.py:103; split_step_1d.py:9; 2d:18; 3d:39; 3d_gpu:41
- **Test coverage:** indirect: all solver tests
- **Independent validation:** PARTIALLY

#### P129. `Solver.step` - method (abstractmethod)

- **Definition:** `quantumlab/solvers/base.py:13`
- **Signature (verbatim):** `def step(self, wavefunction):`
- **Input domain:** wavefunction
- **Output domain:** wavefunction
- **Mathematical definition:** abstract
- **Preconditions / postconditions enforced:** abstractmethod
- **Actual callers:** called dynamically: runner.py:161; stationary/imaginary_time.py:126; examples/01:39,02:40,03:40,04:40,05:54,06:48,07:83,08:110,11:99; benchmarks/validation_suite.py:143; benchmarks/perf_comparison.py:97,104,122; testbench_interlock.py:106
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_order2_matches_legacy_solvers:26
- **Independent validation:** VERIFIED - through subclass checks

#### P130. `Solver.backend` - property

- **Definition:** `quantumlab/solvers/base.py:17`
- **Signature (verbatim):** `def backend(self) -> str:`
- **Input domain:** none
- **Output domain:** str
- **Mathematical definition:** returns 'scipy-cpu'
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (overridden by SplitOperatorSolver.backend:184, SplitStep3DGPU.backend:140, CoupledGPESolver.backend:78)
- **Test coverage:** NONE
- **Independent validation:** NONE


### `quantumlab/solvers/backends.py`

#### P131. `ArrayBackend` - class (dataclass(frozen=True))

- **Definition:** `quantumlab/solvers/backends.py:13`
- **Signature (verbatim):** `class ArrayBackend:`
- **Input domain:** name, xp, fftn, ifftn, to_device, to_host
- **Output domain:** frozen dataclass
- **Mathematical definition:** backend bundle
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** constructed in numpy_backend:33; cupy_backend:50; tests/test_backends.py:57
- **Test coverage:** tests/test_backends.py::test_emulated_device_array_rejects_host_mixing:68
- **Independent validation:** VERIFIED - emulated-device strictness test

#### P132. `cupy_available` - function

- **Definition:** `quantumlab/solvers/backends.py:22`
- **Signature (verbatim):** `def cupy_available() -> bool:`
- **Input domain:** none
- **Output domain:** bool
- **Mathematical definition:** import cupy and getDeviceCount()>0, else False
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/gpu_split_operator.py:40; get_backend:74,78
- **Test coverage:** tests/test_backends.py::test_backend_selection:145
- **Independent validation:** PARTIALLY

#### P133. `numpy_backend` - function

- **Definition:** `quantumlab/solvers/backends.py:31`
- **Signature (verbatim):** `def numpy_backend(workers: int = -1) -> ArrayBackend:`
- **Input domain:** workers=-1
- **Output domain:** ArrayBackend(name='scipy-cpu')
- **Mathematical definition:** scipy.fft.fftn/ifftn with workers, overwrite_x=True
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: get_backend:72,78
- **Test coverage:** indirect: tests/test_backends.py::test_device_code_path_matches_numpy:97
- **Independent validation:** VERIFIED - CPU reference path

#### P134. `cupy_backend` - function

- **Definition:** `quantumlab/solvers/backends.py:43`
- **Signature (verbatim):** `def cupy_backend(device_id: int = 0) -> ArrayBackend:`
- **Input domain:** device_id=0
- **Output domain:** ArrayBackend(name='cupy')
- **Mathematical definition:** cupyx.scipy.fft with device selection
- **Preconditions / postconditions enforced:** ENFORCED: ValueError if device_id out of range
- **Actual callers:** internal: get_backend:76,78
- **Test coverage:** indirect: tests/test_backends.py::test_real_cupy_matches_cpu:158 (skipif no CUDA)
- **Independent validation:** VERIFIED - GPU benchmark relative_error ~1.1e-14..1.8e-14 on RTX A1000

#### P135. `get_backend` - function

- **Definition:** `quantumlab/solvers/backends.py:60`
- **Signature (verbatim):** `def get_backend(backend='numpy', workers: int = -1, device_id: int = 0) -> ArrayBackend:`
- **Input domain:** backend='numpy', workers=-1, device_id=0
- **Output domain:** ArrayBackend
- **Mathematical definition:** dispatch numpy/cupy/auto/ArrayBackend
- **Preconditions / postconditions enforced:** ENFORCED: ValueError for unknown; RuntimeError if cupy unavailable
- **Actual callers:** solvers/split_operator.py:129
- **Test coverage:** tests/test_backends.py::test_backend_selection:145
- **Independent validation:** PARTIALLY


### `quantumlab/solvers/multicomponent.py`

#### P136. `CoupledGPESolver` - class

- **Definition:** `quantumlab/solvers/multicomponent.py:21`
- **Signature (verbatim):** `class CoupledGPESolver:`
- **Input domain:** grid, potentials:Sequence, couplings, dt, hbar=1,m=1,order=2,imaginary_time=False,rotation=0,damping=0,workers=-1,backend='numpy',device_id=0,t0=0
- **Output domain:** object; n_components,couplings,engine
- **Mathematical definition:** coupled GPE propagator
- **Preconditions / postconditions enforced:** ENFORCED: couplings shape (n,n), symmetric, static potentials only
- **Actual callers:** benchmarks/validation_suite.py:261,272; examples/13:120,201; stationary/imaginary_time.py:219
- **Test coverage:** tests/test_multicomponent.py (all); test_backends.py::test_coupled_solver_device_path_matches_numpy:168
- **Independent validation:** VERIFIED - Bogoliubov/phase-separation/Manakov/virial checks

#### P137. `CoupledGPESolver.__init__` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:38`
- **Signature (verbatim):** `def __init__(self, grid, potentials: Sequence, couplings, dt: float, hbar: float = 1.0,\n                 m: float = 1.0, order: int = 2, imaginary_time: bool = False, rotation: float = 0.0,\n                 damping: float = 0.0, workers: int = -1, backend='numpy', device_id: int = 0,\n                 t0: float = 0.0):`
- **Input domain:** see class
- **Output domain:** sets fields + engine
- **Mathematical definition:** validates couplings; builds SplitOperatorSolver(grid,None,...)
- **Preconditions / postconditions enforced:** ENFORCED (see class)
- **Actual callers:** all CoupledGPESolver(...) sites
- **Test coverage:** tests/test_multicomponent.py::test_invalid_coupled_configurations:130
- **Independent validation:** PARTIALLY

#### P138. `CoupledGPESolver.t` - property

- **Definition:** `quantumlab/solvers/multicomponent.py:74`
- **Signature (verbatim):** `def t(self) -> float:`
- **Input domain:** none
- **Output domain:** float
- **Mathematical definition:** t0+steps_taken*dt
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** tests/test_multicomponent.py:73,88
- **Test coverage:** tests/test_multicomponent.py::test_bogoliubov_spin_mode_frequency:63
- **Independent validation:** PARTIALLY

#### P139. `CoupledGPESolver.backend` - property

- **Definition:** `quantumlab/solvers/multicomponent.py:78`
- **Signature (verbatim):** `def backend(self) -> str:`
- **Input domain:** none
- **Output domain:** str
- **Mathematical definition:** engine backend name
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** NONE (no call site)
- **Test coverage:** NONE
- **Independent validation:** NONE

#### P140. `CoupledGPESolver._densities` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:81`
- **Signature (verbatim):** `def _densities(self, psis, rescale: bool):`
- **Input domain:** psis, rescale:bool
- **Output domain:** list of arrays
- **Mathematical definition:** |psi_j|^2, optionally rescaled to target norms
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _potential_half_step:97,99,101
- **Test coverage:** indirect: coupled tests
- **Independent validation:** PARTIALLY

#### P141. `CoupledGPESolver._effective_potentials` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:88`
- **Signature (verbatim):** `def _effective_potentials(self, rhos):`
- **Input domain:** rhos
- **Output domain:** list of arrays
- **Mathematical definition:** V_i + sum_j g_ij rho_j
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _potential_half_step:97,99,101
- **Test coverage:** indirect: coupled tests
- **Independent validation:** PARTIALLY

#### P142. `CoupledGPESolver._potential_half_step` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:93`
- **Signature (verbatim):** `def _potential_half_step(self, psis, w):`
- **Input domain:** psis, w
- **Output domain:** list of arrays
- **Mathematical definition:** exp(-i c V_eff h/2hbar) psi (frozen density real-time; midpoint rescaled imaginary/damped)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _advance:111,113
- **Test coverage:** indirect: coupled tests
- **Independent validation:** VERIFIED - Manakov/virial/Bogoliubov

#### P143. `CoupledGPESolver._norm` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:104`
- **Signature (verbatim):** `def _norm(self, psi) -> float:`
- **Input domain:** psi
- **Output domain:** float
- **Mathematical definition:** sum|psi|^2*dV
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _advance:109,117
- **Test coverage:** indirect: coupled tests
- **Independent validation:** PARTIALLY

#### P144. `CoupledGPESolver._advance` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:107`
- **Signature (verbatim):** `def _advance(self, psis):`
- **Input domain:** psis
- **Output domain:** list of arrays
- **Mathematical definition:** Strang/Yoshida over components with renormalisation
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: step:132; evolve:141
- **Test coverage:** indirect: coupled tests
- **Independent validation:** VERIFIED

#### P145. `CoupledGPESolver._upload` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:123`
- **Signature (verbatim):** `def _upload(self, states):`
- **Input domain:** states
- **Output domain:** list of device arrays
- **Mathematical definition:** to_device(psi) per component
- **Preconditions / postconditions enforced:** ENFORCED: ValueError if len(states)!=n_components
- **Actual callers:** internal: step:132; evolve:139
- **Test coverage:** tests/test_multicomponent.py::test_invalid_coupled_configurations:130
- **Independent validation:** PARTIALLY

#### P146. `CoupledGPESolver._download` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:128`
- **Signature (verbatim):** `def _download(self, psis):`
- **Input domain:** psis
- **Output domain:** tuple of WaveFunction
- **Mathematical definition:** wf_class(grid, to_host(p))
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: step:132; evolve:143,144
- **Test coverage:** indirect: coupled tests
- **Independent validation:** PARTIALLY

#### P147. `CoupledGPESolver.step` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:131`
- **Signature (verbatim):** `def step(self, states):`
- **Input domain:** states
- **Output domain:** tuple of WaveFunction
- **Mathematical definition:** one coupled step
- **Preconditions / postconditions enforced:** ENFORCED via _upload
- **Actual callers:** tests/test_multicomponent.py:140
- **Test coverage:** tests/test_multicomponent.py::test_invalid_coupled_configurations:130
- **Independent validation:** VERIFIED

#### P148. `CoupledGPESolver.evolve` - method

- **Definition:** `quantumlab/solvers/multicomponent.py:134`
- **Signature (verbatim):** `def evolve(self, states, n_steps: int, callback=None, callback_interval: int = 1):`
- **Input domain:** states, n_steps, callback=None, callback_interval=1
- **Output domain:** tuple of WaveFunction
- **Mathematical definition:** n_steps coupled steps with callbacks
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/13:142,217; benchmarks/validation_suite.py:264,275; stationary/imaginary_time.py:229
- **Test coverage:** tests/test_multicomponent.py::test_bogoliubov_spin_mode_frequency:63; test_energy_and_populations_conserved_in_real_time:95
- **Independent validation:** VERIFIED


### `quantumlab/solvers/split_operator.py`

#### P149. `SplitOperatorSolver` - class

- **Definition:** `quantumlab/solvers/split_operator.py:42`
- **Signature (verbatim):** `class SplitOperatorSolver(Solver):`
- **Input domain:** grid, potential, dt, hbar=1,m=1,order=2,nonlinearity=0,imaginary_time=False,absorber=None,workers=-1,t0=0,rotation=0,damping=0,backend='numpy',device_id=0
- **Output domain:** object; propagators
- **Mathematical definition:** generic split-operator propagator
- **Preconditions / postconditions enforced:** ENFORCED: order in {2,4}; order=4+imaginary_time ValueError; imaginary_time+time_dependent ValueError; damping>=0; damping requires order=2 real; rotation requires 2D/3D
- **Actual callers:** runner.py:106; multicomponent.py:60; stationary/imaginary_time.py:100; benchmarks/validation_suite.py (many); examples/07:60,08:99,09:34,11:76,12:64
- **Test coverage:** tests/test_split_operator.py (all); test_rotation.py (all); test_gross_pitaevskii.py (all); test_backends.py (all)
- **Independent validation:** VERIFIED - 27/27 validation checks; convergence orders 2.001/3.997

#### P150. `SplitOperatorSolver.__init__` - method

- **Definition:** `quantumlab/solvers/split_operator.py:98`
- **Signature (verbatim):** `def __init__(self, grid, potential, dt: float, hbar: float = 1.0, m: float = 1.0,\n                 order: int = 2, nonlinearity: float = 0.0, imaginary_time: bool = False,\n                 absorber=None, workers: int = -1, t0: float = 0.0,\n                 rotation: float = 0.0, damping: float = 0.0,\n                 backend='numpy', device_id: int = 0):`
- **Input domain:** see class
- **Output domain:** sets fields, builds operators
- **Mathematical definition:** validates; evaluates static V; builds _U_T/_U_V_half; sets _c
- **Preconditions / postconditions enforced:** ENFORCED (see class)
- **Actual callers:** all SplitOperatorSolver(...) sites
- **Test coverage:** tests/test_split_operator.py::test_invalid_configurations_raise:134
- **Independent validation:** PARTIALLY

#### P151. `SplitOperatorSolver.update_operators` - method

- **Definition:** `quantumlab/solvers/split_operator.py:148`
- **Signature (verbatim):** `def update_operators(self):`
- **Input domain:** none
- **Output domain:** sets _U_T,_U_x_half,_U_yz,_U_V_half
- **Mathematical definition:** exp(c*T_k*h/hbar) etc per substep weight w
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: __init__:146
- **Test coverage:** indirect: all solver tests
- **Independent validation:** VERIFIED - convergence/norm/energy checks

#### P152. `SplitOperatorSolver._rotating_kinetic_parts` - method

- **Definition:** `quantumlab/solvers/split_operator.py:166`
- **Signature (verbatim):** `def _rotating_kinetic_parts(self):`
- **Input domain:** none
- **Output domain:** (H_x,H_yz)
- **Mathematical definition:** H_x=hbar^2 k_x^2/2m+Omega hbar y k_x; H_yz=hbar^2 k_y^2/2m-O hbar x k_y (+z term in 3D)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: update_operators:160
- **Test coverage:** indirect: test_rotation.py (all)
- **Independent validation:** VERIFIED - rotating-frame exact trajectory 1.89e-08; vortex eigenstate 1.15e-08

#### P153. `SplitOperatorSolver.t` - property

- **Definition:** `quantumlab/solvers/split_operator.py:179`
- **Signature (verbatim):** `def t(self) -> float:`
- **Input domain:** none
- **Output domain:** float
- **Mathematical definition:** t0+steps_taken*dt
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:75,164,196,205,265,276; examples/07:81,85,88,90,93; 08:112,113,117,126; 09:39; 11:102,107,110,127; tests/test_split_operator.py:60,99; test_rotation.py:30,42
- **Test coverage:** tests/test_split_operator.py::test_norm_and_energy_conservation:50; test_evolve_callback_schedule:144
- **Independent validation:** PARTIALLY

#### P154. `SplitOperatorSolver.backend` - property

- **Definition:** `quantumlab/solvers/split_operator.py:184`
- **Signature (verbatim):** `def backend(self) -> str:`
- **Input domain:** none
- **Output domain:** str
- **Mathematical definition:** backend name
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:172; tests/test_3d_gpu_solver.py:44,130,153; test_backends.py:103,164
- **Test coverage:** tests/test_backends.py::test_device_code_path_matches_numpy:97
- **Independent validation:** PARTIALLY

#### P155. `SplitOperatorSolver.potential_at` - method

- **Definition:** `quantumlab/solvers/split_operator.py:187`
- **Signature (verbatim):** `def potential_at(self, t: float) -> np.ndarray:`
- **Input domain:** t:float
- **Output domain:** float64 grid.shape (host)
- **Mathematical definition:** static V or potential.evaluate_at(grid,t)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** stationary/imaginary_time.py:105; internal _potential_on_device:196
- **Test coverage:** indirect: imaginary-time tests
- **Independent validation:** PARTIALLY

#### P156. `SplitOperatorSolver._potential_on_device` - method

- **Definition:** `quantumlab/solvers/split_operator.py:193`
- **Signature (verbatim):** `def _potential_on_device(self, t):`
- **Input domain:** t
- **Output domain:** device array
- **Mathematical definition:** static device V or to_device(potential_at(t))
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _potential_half_step:204
- **Test coverage:** indirect: solver tests
- **Independent validation:** PARTIALLY

#### P157. `SplitOperatorSolver._potential_half_step` - method

- **Definition:** `quantumlab/solvers/split_operator.py:198`
- **Signature (verbatim):** `def _potential_half_step(self, psi, t, w):`
- **Input domain:** psi, t, w
- **Output domain:** psi (in place)
- **Mathematical definition:** exp(-i c (V+g|psi|^2) h/2hbar) psi; midpoint density variant when renormalising
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _strang:239,241
- **Test coverage:** indirect: all dynamics tests
- **Independent validation:** VERIFIED - soliton, GP, driven, HHG

#### P158. `SplitOperatorSolver._kinetic_step` - method

- **Definition:** `quantumlab/solvers/split_operator.py:225`
- **Signature (verbatim):** `def _kinetic_step(self, psi, w):`
- **Input domain:** psi, w
- **Output domain:** psi
- **Mathematical definition:** FFT -> multiply U_T (or rotated 3-factor) -> IFFT
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _strang:240; multicomponent.py:112
- **Test coverage:** indirect: all dynamics tests
- **Independent validation:** VERIFIED - convergence order + exact solutions

#### P159. `SplitOperatorSolver._strang` - method

- **Definition:** `quantumlab/solvers/split_operator.py:238`
- **Signature (verbatim):** `def _strang(self, psi, t, w):`
- **Input domain:** psi, t, w
- **Output domain:** psi
- **Mathematical definition:** V(h/2) T(h) V(h/2) at t and t+w*dt
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _advance:253
- **Test coverage:** indirect: all dynamics tests
- **Independent validation:** VERIFIED

#### P160. `SplitOperatorSolver._norm` - method

- **Definition:** `quantumlab/solvers/split_operator.py:243`
- **Signature (verbatim):** `def _norm(self, psi) -> float:`
- **Input domain:** psi
- **Output domain:** float
- **Mathematical definition:** sum|psi|^2*dV
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _advance:250,256
- **Test coverage:** indirect: norm tests
- **Independent validation:** PARTIALLY

#### P161. `SplitOperatorSolver._advance` - method

- **Definition:** `quantumlab/solvers/split_operator.py:246`
- **Signature (verbatim):** `def _advance(self, psi):`
- **Input domain:** psi
- **Output domain:** psi
- **Mathematical definition:** Yoshida/Strang composition + renormalisation + absorber
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: step:271; evolve:281
- **Test coverage:** indirect: all dynamics tests
- **Independent validation:** VERIFIED

#### P162. `SplitOperatorSolver._upload` - method

- **Definition:** `quantumlab/solvers/split_operator.py:264`
- **Signature (verbatim):** `def _upload(self, wavefunction):`
- **Input domain:** wavefunction
- **Output domain:** device complex array
- **Mathematical definition:** to_device(np.array(psi,complex))
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: step:271; evolve:279
- **Test coverage:** indirect: backend tests
- **Independent validation:** PARTIALLY

#### P163. `SplitOperatorSolver._download` - method

- **Definition:** `quantumlab/solvers/split_operator.py:267`
- **Signature (verbatim):** `def _download(self, psi):`
- **Input domain:** psi
- **Output domain:** WaveFunction
- **Mathematical definition:** wf_class(grid, to_host(psi))
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: step:271; evolve:283,284
- **Test coverage:** indirect: backend tests
- **Independent validation:** PARTIALLY

#### P164. `SplitOperatorSolver.step` - method

- **Definition:** `quantumlab/solvers/split_operator.py:270`
- **Signature (verbatim):** `def step(self, wavefunction):`
- **Input domain:** wavefunction
- **Output domain:** WaveFunction
- **Mathematical definition:** one full step (upload/advance/download)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:161; stationary/imaginary_time.py:126; examples/07:83,08:110,11:99; benchmarks/validation_suite.py:143; testbench_interlock.py:106
- **Test coverage:** tests/test_split_operator.py::test_order2_matches_legacy_solvers:26; test_norm_and_energy_conservation:50
- **Independent validation:** VERIFIED

#### P165. `SplitOperatorSolver.evolve` - method

- **Definition:** `quantumlab/solvers/split_operator.py:273`
- **Signature (verbatim):** `def evolve(self, wavefunction, n_steps: int, callback=None, callback_interval: int = 1):`
- **Input domain:** wavefunction, n_steps, callback=None, callback_interval=1
- **Output domain:** WaveFunction
- **Mathematical definition:** n_steps with callbacks; keeps psi on device
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner? no; stationary/imaginary_time.py:130,229; examples/09:37,12:72,13:142,217; benchmarks/validation_suite.py (many)
- **Test coverage:** tests/test_split_operator.py::test_free_particle_matches_analytic_gaussian_spreading:114; test_absorber_removes_outgoing_flux:124; test_backends.py::test_device_absorber_and_callbacks:109
- **Independent validation:** VERIFIED


### `quantumlab/solvers/split_step_1d.py`

#### P166. `SplitStep1DSolver` - class

- **Definition:** `quantumlab/solvers/split_step_1d.py:6`
- **Signature (verbatim):** `class SplitStep1DSolver(Solver):`
- **Input domain:** grid, potential, dt, hbar=1, m=1
- **Output domain:** object
- **Mathematical definition:** legacy 1D Strang SSFM
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:115; examples/01:33,02:31,03:32,04:34; testbench_interlock.py:100
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9; test_energy_conservation:20
- **Independent validation:** VERIFIED - matches SplitOperatorSolver order 2 to 1e-12

#### P167. `SplitStep1DSolver.__init__` - method

- **Definition:** `quantumlab/solvers/split_step_1d.py:8`
- **Signature (verbatim):** `def __init__(self, grid, potential, dt: float, hbar: float=1.0, m: float=1.0):`
- **Input domain:** see class
- **Output domain:** sets V,T_k,U_V,U_T
- **Mathematical definition:** evaluates potential; builds propagators
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all SplitStep1DSolver(...) sites
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9
- **Independent validation:** PARTIALLY

#### P168. `SplitStep1DSolver.update_operators` - method

- **Definition:** `quantumlab/solvers/split_step_1d.py:16`
- **Signature (verbatim):** `def update_operators(self):`
- **Input domain:** none
- **Output domain:** sets U_V,U_T
- **Mathematical definition:** exp(-i V dt/2hbar), exp(-i T_k dt/hbar)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: __init__:14
- **Test coverage:** indirect: test_solvers
- **Independent validation:** PARTIALLY

#### P169. `SplitStep1DSolver.step` - method

- **Definition:** `quantumlab/solvers/split_step_1d.py:20`
- **Signature (verbatim):** `def step(self, wavefunction: WaveFunction1D) -> WaveFunction1D:`
- **Input domain:** wavefunction:WaveFunction1D
- **Output domain:** WaveFunction1D
- **Mathematical definition:** U_V FFT U_T IFFT U_V
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:161; examples/01:39,02:40,03:40,04:40; tests
- **Test coverage:** tests/test_solvers.py::test_norm_conservation:9; test_energy_conservation:20
- **Independent validation:** VERIFIED


### `quantumlab/solvers/split_step_2d.py`

#### P170. `SplitStep2DSolver` - class

- **Definition:** `quantumlab/solvers/split_step_2d.py:6`
- **Signature (verbatim):** `class SplitStep2DSolver(Solver):`
- **Input domain:** grid, potential, dt, hbar=1, m=1
- **Output domain:** object
- **Mathematical definition:** legacy 2D Strang SSFM
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:117; examples/05:41
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11; test_2d_energy_conservation:23
- **Independent validation:** VERIFIED - matches SplitOperatorSolver order 2

#### P171. `SplitStep2DSolver.__init__` - method

- **Definition:** `quantumlab/solvers/split_step_2d.py:17`
- **Signature (verbatim):** `def __init__(self, grid, potential, dt: float, hbar: float = 1.0, m: float = 1.0):`
- **Input domain:** see class
- **Output domain:** sets V,T_k,U_V,U_T
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all SplitStep2DSolver(...) sites
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11
- **Independent validation:** PARTIALLY

#### P172. `SplitStep2DSolver.update_operators` - method

- **Definition:** `quantumlab/solvers/split_step_2d.py:25`
- **Signature (verbatim):** `def update_operators(self):`
- **Input domain:** none
- **Output domain:** sets U_V,U_T
- **Mathematical definition:** exp(-i V dt/2hbar), exp(-i T_k dt/hbar)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: __init__:23
- **Test coverage:** indirect: test_2d_solver
- **Independent validation:** PARTIALLY

#### P173. `SplitStep2DSolver.step` - method

- **Definition:** `quantumlab/solvers/split_step_2d.py:30`
- **Signature (verbatim):** `def step(self, wavefunction: WaveFunction2D) -> WaveFunction2D:`
- **Input domain:** wavefunction:WaveFunction2D
- **Output domain:** WaveFunction2D
- **Mathematical definition:** U_V FFT2 U_T IFFT2 U_V
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:161; examples/05:54; tests
- **Test coverage:** tests/test_2d_solver.py::test_2d_norm_conservation:11; test_2d_energy_conservation:23
- **Independent validation:** VERIFIED


### `quantumlab/solvers/split_step_3d.py`

#### P174. `SplitStep3DSolver` - class

- **Definition:** `quantumlab/solvers/split_step_3d.py:7`
- **Signature (verbatim):** `class SplitStep3DSolver(Solver):`
- **Input domain:** grid, potential, dt, hbar=1, m=1, workers=-1
- **Output domain:** object
- **Mathematical definition:** legacy 3D Strang SSFM
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:121; examples/06:42; benchmarks/perf_comparison.py:94
- **Test coverage:** tests/test_3d_solver.py::test_3d_norm_conservation:72; test_3d_energy_conservation_harmonic:86; test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73
- **Independent validation:** VERIFIED - CPU/GPU parity 1e-5; energy conservation

#### P175. `SplitStep3DSolver.__init__` - method

- **Definition:** `quantumlab/solvers/split_step_3d.py:37`
- **Signature (verbatim):** `def __init__(self, grid, potential, dt: float, hbar: float = 1.0,\n                 m: float = 1.0, workers: int = -1):`
- **Input domain:** see class
- **Output domain:** sets V,T_k,U_V,U_T
- **Mathematical definition:** none
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** all SplitStep3DSolver(...) sites
- **Test coverage:** tests/test_3d_solver.py::test_3d_norm_conservation:72
- **Independent validation:** PARTIALLY

#### P176. `SplitStep3DSolver.update_operators` - method

- **Definition:** `quantumlab/solvers/split_step_3d.py:49`
- **Signature (verbatim):** `def update_operators(self):`
- **Input domain:** none
- **Output domain:** sets U_V,U_T
- **Mathematical definition:** exp(-i V dt/2hbar), exp(-i T_k dt/hbar)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: __init__:47
- **Test coverage:** indirect: test_3d_solver
- **Independent validation:** PARTIALLY

#### P177. `SplitStep3DSolver.step` - method

- **Definition:** `quantumlab/solvers/split_step_3d.py:54`
- **Signature (verbatim):** `def step(self, wavefunction: WaveFunction3D) -> WaveFunction3D:`
- **Input domain:** wavefunction:WaveFunction3D
- **Output domain:** WaveFunction3D
- **Mathematical definition:** U_V FFTN U_T IFFTN U_V
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** runner.py:161; examples/06:48; benchmarks; tests
- **Test coverage:** tests/test_3d_solver.py::test_3d_norm_conservation:72; test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73
- **Independent validation:** VERIFIED


### `quantumlab/solvers/split_step_3d_gpu.py`

#### P178. `SplitStep3DGPU` - class

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:25`
- **Signature (verbatim):** `class SplitStep3DGPU(Solver):`
- **Input domain:** grid, potential, dt, hbar=1,m=1,device_id=0,renormalize_interval=0
- **Output domain:** object; cupy or cpu fallback
- **Mathematical definition:** GPU 3D SSFM with CPU fallback
- **Preconditions / postconditions enforced:** ENFORCED: device_id validated when CuPy present; invalid -> warn + CPU fallback
- **Actual callers:** runner.py:120; benchmarks/perf_comparison.py:117
- **Test coverage:** tests/test_3d_gpu_solver.py (all); test_benchmark_failure_handling.py (monkeypatched)
- **Independent validation:** VERIFIED - GPU benchmark relative_error 1.1e-14..1.8e-14 on RTX A1000; CPU/GPU parity test

#### P179. `SplitStep3DGPU.__init__` - method

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:31`
- **Signature (verbatim):** `def __init__(\n        self,\n        grid,\n        potential,\n        dt: float,\n        hbar: float = 1.0,\n        m: float = 1.0,\n        device_id: int = 0,\n        renormalize_interval: int = 0,\n    ):`
- **Input domain:** see class
- **Output domain:** sets V,T_k on device, operators
- **Mathematical definition:** evaluates potential; builds propagators
- **Preconditions / postconditions enforced:** ENFORCED device_id (conditional)
- **Actual callers:** all SplitStep3DGPU(...) sites
- **Test coverage:** tests/test_3d_gpu_solver.py::test_cpu_fallback_produces_valid_result:112
- **Independent validation:** PARTIALLY

#### P180. `SplitStep3DGPU.update_operators` - method

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:78`
- **Signature (verbatim):** `def update_operators(self) -> None:`
- **Input domain:** none
- **Output domain:** sets U_V,U_T
- **Mathematical definition:** exp(-i V dt/2hbar), exp(-i T_k dt/hbar) on device
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: __init__:76
- **Test coverage:** indirect: GPU tests
- **Independent validation:** PARTIALLY

#### P181. `SplitStep3DGPU.step` - method

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:87`
- **Signature (verbatim):** `def step(self, wavefunction: WaveFunction3D) -> WaveFunction3D:`
- **Input domain:** wavefunction:WaveFunction3D
- **Output domain:** WaveFunction3D
- **Mathematical definition:** one GPU step; optional renormalisation every interval
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/perf_comparison.py:97,104,122; tests
- **Test coverage:** tests/test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_3d_gpu_matches_cpu:73
- **Independent validation:** VERIFIED

#### P182. `SplitStep3DGPU.step_sequence` - method

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:107`
- **Signature (verbatim):** `def step_sequence(self, initial_wf: WaveFunction3D, steps: int) -> WaveFunction3D:`
- **Input domain:** initial_wf:WaveFunction3D, steps:int
- **Output domain:** WaveFunction3D
- **Mathematical definition:** in-VRAM multi-step
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/perf_comparison.py:123,128
- **Test coverage:** tests/test_3d_gpu_solver.py::test_step_sequence_matches_individual_steps:95
- **Independent validation:** VERIFIED - matches individual steps to 1e-12

#### P183. `SplitStep3DGPU._step_gpu_internal` - method

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:125`
- **Signature (verbatim):** `def _step_gpu_internal(self, psi_gpu):`
- **Input domain:** psi_gpu
- **Output domain:** device array
- **Mathematical definition:** U_V FFT U_T IFFT U_V + optional renormalisation
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: step:92; step_sequence:121
- **Test coverage:** indirect: GPU tests
- **Independent validation:** PARTIALLY

#### P184. `SplitStep3DGPU.backend` - property

- **Definition:** `quantumlab/solvers/split_step_3d_gpu.py:140`
- **Signature (verbatim):** `def backend(self) -> str:`
- **Input domain:** none
- **Output domain:** str 'cupy'|'scipy-cpu'
- **Mathematical definition:** gpu flag
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** tests/test_3d_gpu_solver.py:44,130,153
- **Test coverage:** tests/test_3d_gpu_solver.py::test_backend_property:151
- **Independent validation:** PARTIALLY


### `quantumlab/stationary/conjugate_gradient.py`

#### P185. `ground_state_pcg` - function

- **Definition:** `quantumlab/stationary/conjugate_gradient.py:24`
- **Signature (verbatim):** `def ground_state_pcg(grid, potential, initial=None, nonlinearity: float = 0.0, rotation: float = 0.0,\n                     tol: float = 1e-8, max_iter: int = 10000, hbar: float = 1.0, m: float = 1.0,\n                     callback=None, callback_interval: int = 100, workers: int = -1):`
- **Input domain:** grid, potential, initial=None, nonlinearity=0, rotation=0, tol=1e-8, max_iter=10000, hbar=1,m=1, callback=None, callback_interval=100, workers=-1
- **Output domain:** (WaveFunction, ConvergenceInfo)
- **Mathematical definition:** preconditioned nonlinear CG on the sphere; E=<psi|H|psi>-(g/2)int|psi|^4
- **Preconditions / postconditions enforced:** ENFORCED: ValueError if potential.time_dependent
- **Actual callers:** benchmarks/validation_suite.py:312,317; examples/11:169
- **Test coverage:** tests/test_conjugate_gradient.py (all)
- **Independent validation:** VERIFIED - hydrogen E0=-0.5 to 7.77e-16; GP virial 5.79e-10


### `quantumlab/stationary/eigensolver.py`

#### P186. `eigenstates` - function

- **Definition:** `quantumlab/stationary/eigensolver.py:17`
- **Signature (verbatim):** `def eigenstates(grid, potential, n_states: int = 6, hbar: float = 1.0, m: float = 1.0,\n                tol: float = None, max_iter: int = 1000, seed: int = 0,\n                method: str = 'auto', workers: int = -1) -> Tuple[np.ndarray, List]:`
- **Input domain:** grid, potential, n_states=6, hbar=1,m=1,tol=None,max_iter=1000,seed=0,method='auto',workers=-1
- **Output domain:** (energies ndarray (n_states,), states list[WaveFunction])
- **Mathematical definition:** matrix-free H via FFT; LOBPCG (k-space preconditioned) or Lanczos (ARPACK)
- **Preconditions / postconditions enforced:** ENFORCED: ValueError for unknown method; LOBPCG non-convergence RuntimeWarning
- **Actual callers:** benchmarks/validation_suite.py:119,124,211; examples/10:41,12:94
- **Test coverage:** tests/test_stationary.py (all); test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33
- **Independent validation:** VERIFIED - exact harmonic spectra 7.28e-14/1.42e-13; hydrogen -0.5 to 1.94e-14


### `quantumlab/stationary/hamiltonian.py`

#### P187. `apply_hamiltonian` - function

- **Definition:** `quantumlab/stationary/hamiltonian.py:6`
- **Signature (verbatim):** `def apply_hamiltonian(psi: np.ndarray, grid, V: np.ndarray, hbar: float = 1.0, m: float = 1.0,\n                      nonlinearity: float = 0.0, workers: int = -1, rotation: float = 0.0) -> np.ndarray:`
- **Input domain:** psi:ndarray, grid, V:ndarray, hbar=1,m=1,nonlinearity=0,workers=-1,rotation=0
- **Output domain:** ndarray grid.shape
- **Mathematical definition:** H psi = -hbar^2/2m nabla^2 psi + (V+g|psi|^2) psi - Omega L_z psi (spectral derivatives)
- **Preconditions / postconditions enforced:** NONE (V shape not validated)
- **Actual callers:** stationary/conjugate_gradient.py:63; imaginary_time.py:31,184
- **Test coverage:** tests/test_stationary.py::test_3d_isotropic_degeneracy:29; test_rotation.py::test_rotating_hamiltonian_has_vortex_eigenstate:126
- **Independent validation:** VERIFIED - vortex eigenstate H psi=(2-Omega)psi to 1e-12; residual checks


### `quantumlab/stationary/imaginary_time.py`

#### P188. `ConvergenceInfo` - class (dataclass)

- **Definition:** `quantumlab/stationary/imaginary_time.py:18`
- **Signature (verbatim):** `class ConvergenceInfo:`
- **Input domain:** converged,steps,energy,chemical_potential,residual
- **Output domain:** dataclass
- **Mathematical definition:** container
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** constructed in ground_state:139; excited_states (via ground_state)
- **Test coverage:** indirect: test_stationary.py (all)
- **Independent validation:** PARTIALLY

#### P189. `_inner` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:26`
- **Signature (verbatim):** `def _inner(a, b, dV):`
- **Input domain:** a,b,dV
- **Output domain:** complex
- **Mathematical definition:** sum(conj(a)*b)*dV
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: _energy_and_mu:32,35,36; ground_state:115,116; _coupled_energy_mu:185,187,189
- **Test coverage:** indirect: stationary tests
- **Independent validation:** PARTIALLY

#### P190. `_energy_and_mu` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:30`
- **Signature (verbatim):** `def _energy_and_mu(psi, grid, V, hbar, m, g, dV, rotation=0.0):`
- **Input domain:** psi,grid,V,hbar,m,g,dV,rotation=0
- **Output domain:** (energy,mu,residual)
- **Mathematical definition:** E=<T>+<V>+(g/2)int|psi|^4; mu=<H_GP>; residual=||H_GP psi-mu psi||
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: ground_state:132,138
- **Test coverage:** indirect: test_stationary.py::test_ground_state_error_is_second_order_in_dtau:63
- **Independent validation:** VERIFIED - dtau^2 residual ratio 3.99

#### P191. `_default_guess` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:40`
- **Signature (verbatim):** `def _default_guess(grid):`
- **Input domain:** grid
- **Output domain:** complex128 grid.shape
- **Mathematical definition:** exp(-r^2/(2 width^2)), width=min(ptp(coords))/8
- **Preconditions / postconditions enforced:** ENFORCED: none (min ptp could be 0 -> division by zero)
- **Actual callers:** stationary/conjugate_gradient.py:54; internal ground_state:109; excited_states:157
- **Test coverage:** indirect: stationary tests
- **Independent validation:** PARTIALLY

#### P192. `ground_state` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:47`
- **Signature (verbatim):** `def ground_state(grid, potential, dtau: float = 0.01, nonlinearity: float = 0.0,\n                 initial=None, tol: float = 1e-11, max_steps: int = 50000,\n                 check_interval: int = 20, hbar: float = 1.0, m: float = 1.0,\n                 orthogonal_to: Optional[List] = None, workers: int = -1,\n                 rotation: float = 0.0, backend='numpy'):`
- **Input domain:** grid, potential, dtau=0.01, nonlinearity=0, initial=None, tol=1e-11, max_steps=50000, check_interval=20, hbar=1,m=1, orthogonal_to=None, workers=-1, rotation=0, backend='numpy'
- **Output domain:** (WaveFunction, ConvergenceInfo)
- **Mathematical definition:** imaginary-time relaxation via SplitOperatorSolver(order=2,imaginary_time=True); optional Gram-Schmidt; dtau sequence continuation
- **Preconditions / postconditions enforced:** ENFORCED: orthogonal_to only for linear (ValueError); propagates solver validations
- **Actual callers:** benchmarks/validation_suite.py:129,172,181,182,290; examples/08:83,11:71,162
- **Test coverage:** tests/test_stationary.py (all); test_gross_pitaevskii.py (all); test_rotation.py (all); test_backends.py::test_ground_state_on_device_backend:136
- **Independent validation:** VERIFIED - exact 3D ground state 6.95e-10; GP virial; dtau^2

#### P193. `excited_states` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:142`
- **Signature (verbatim):** `def excited_states(grid, potential, n_states: int, dtau: float = 0.01, tol: float = 1e-11,\n                   max_steps: int = 50000, seed: int = 0, hbar: float = 1.0, m: float = 1.0,\n                   workers: int = -1):`
- **Input domain:** grid, potential, n_states, dtau=0.01, tol=1e-11, max_steps=50000, seed=0, hbar=1,m=1, workers=-1
- **Output domain:** (energies ndarray, states list, infos list)
- **Mathematical definition:** imaginary time + Gram-Schmidt against converged states
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/10:44
- **Test coverage:** tests/test_stationary.py::test_imaginary_time_excited_states_match_lanczos:54
- **Independent validation:** VERIFIED - matches Lanczos to 1e-8

#### P194. `CoupledConvergenceInfo` - class (dataclass)

- **Definition:** `quantumlab/stationary/imaginary_time.py:171`
- **Signature (verbatim):** `class CoupledConvergenceInfo:`
- **Input domain:** converged,steps,energy,chemical_potentials,residuals
- **Output domain:** dataclass
- **Mathematical definition:** container
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** constructed in coupled_ground_state:237
- **Test coverage:** indirect: test_multicomponent.py (all)
- **Independent validation:** PARTIALLY

#### P195. `_coupled_energy_mu` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:179`
- **Signature (verbatim):** `def _coupled_energy_mu(psis, grid, Vs, g, hbar, m, rotation, dV):`
- **Input domain:** psis,grid,Vs,g,hbar,m,rotation,dV
- **Output domain:** (energy,mus,residuals)
- **Mathematical definition:** E=sum_i(<T>_i+<V_i>)+0.5 sum_ij g_ij int n_i n_j; per-component mu and residual
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** internal: coupled_ground_state:231,236
- **Test coverage:** indirect: coupled tests
- **Independent validation:** VERIFIED - Manakov/virial

#### P196. `coupled_ground_state` - function

- **Definition:** `quantumlab/stationary/imaginary_time.py:195`
- **Signature (verbatim):** `def coupled_ground_state(grid, potentials, couplings, initial, dtau: float = 0.005, tol: float = 1e-11,\n                         max_steps: int = 50000, check_interval: int = 20, hbar: float = 1.0,\n                         m: float = 1.0, rotation: float = 0.0, backend='numpy', workers: int = -1):`
- **Input domain:** grid, potentials, couplings, initial, dtau=0.005, tol=1e-11, max_steps=50000, check_interval=20, hbar=1,m=1, rotation=0, backend='numpy', workers=-1
- **Output domain:** (states tuple, CoupledConvergenceInfo)
- **Mathematical definition:** imaginary-time coupled GPE at fixed populations
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:289,301; examples/13:73,198
- **Test coverage:** tests/test_multicomponent.py::test_manakov_point_total_density_equals_single_component:32; test_coupled_virial_theorem:107
- **Independent validation:** VERIFIED - Manakov point 1.76e-07; virial 2.27e-06


### `quantumlab/observables/coefficients.py`

#### P197. `transmission_coefficient` - function

- **Definition:** `quantumlab/observables/coefficients.py:4`
- **Signature (verbatim):** `def transmission_coefficient(wf, barrier_position: float=0.0) -> float:`
- **Input domain:** wf, barrier_position=0.0
- **Output domain:** float
- **Mathematical definition:** int_{x>=barrier_position} |psi|^2 dx
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** examples/01:48,04:49
- **Test coverage:** tests/test_3d_observables.py::test_3d_transmission_reflection_sum_to_norm:63
- **Independent validation:** PARTIALLY - T+R=norm and half-splitting only

#### P198. `reflection_coefficient` - function

- **Definition:** `quantumlab/observables/coefficients.py:18`
- **Signature (verbatim):** `def reflection_coefficient(wf, barrier_position: float=0.0) -> float:`
- **Input domain:** wf, barrier_position=0.0
- **Output domain:** float
- **Mathematical definition:** int_{x<barrier_position} |psi|^2 dx
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** examples/01:47,04:48
- **Test coverage:** tests/test_3d_observables.py::test_3d_transmission_reflection_sum_to_norm:63
- **Independent validation:** PARTIALLY


### `quantumlab/observables/current.py`

#### P199. `gradient` - function

- **Definition:** `quantumlab/observables/current.py:11`
- **Signature (verbatim):** `def gradient(psi: np.ndarray, grid):`
- **Input domain:** psi:ndarray, grid
- **Output domain:** tuple of arrays
- **Mathematical definition:** spectral gradient (ifftn(1j K psi_k)) per axis
- **Preconditions / postconditions enforced:** Propagates ndim TypeError
- **Actual callers:** strongfield.py:130; internal probability_current:23; angular_momentum_z_expectation:30
- **Test coverage:** indirect: test_new_potentials_and_observables.py::test_probability_current_of_moving_gaussian:84; test_strongfield.py::test_soft_coulomb_gradient_matches_finite_difference:40
- **Independent validation:** VERIFIED - current integrates to momentum; Lz exact

#### P200. `probability_current` - function

- **Definition:** `quantumlab/observables/current.py:17`
- **Signature (verbatim):** `def probability_current(wf, hbar: float = 1.0, m: float = 1.0):`
- **Input domain:** wf, hbar=1,m=1
- **Output domain:** tuple of arrays
- **Mathematical definition:** j=(hbar/m) Im(psi* grad psi)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** TEST-ONLY: tests/test_new_potentials_and_observables.py:87,95
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_probability_current_of_moving_gaussian:84; test_probability_current_integrates_to_momentum_3d:91
- **Independent validation:** VERIFIED - j=2*rho for moving Gaussian; integrates to <p>

#### P201. `angular_momentum_z_expectation` - function

- **Definition:** `quantumlab/observables/current.py:26`
- **Signature (verbatim):** `def angular_momentum_z_expectation(wf, hbar: float = 1.0) -> float:`
- **Input domain:** wf, hbar=1
- **Output domain:** float
- **Mathematical definition:** <psi|-i hbar (x d_y - y d_x)|psi>
- **Preconditions / postconditions enforced:** ENFORCED: TypeError unless Grid2D/Grid3D
- **Actual callers:** benchmarks/validation_suite.py:114; examples/11:104,13:225
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99; test_rotation.py (all)
- **Independent validation:** VERIFIED - <Lz>=1 to 2.22e-16; vortex lattice

#### P202. `autocorrelation` - function

- **Definition:** `quantumlab/observables/current.py:35`
- **Signature (verbatim):** `def autocorrelation(psi0, psi_t, grid) -> complex:`
- **Input domain:** psi0, psi_t, grid
- **Output domain:** complex
- **Mathematical definition:** C(t)=<psi0|psi_t>=int conj(psi0) psi_t dV
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:142,203
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_autocorrelation_spectrum_peaks_at_eigenenergies:107; test_rotation.py::test_vortex_is_stationary_with_rotating_frame_energy:48
- **Independent validation:** VERIFIED - Feit-Fleck peaks; vortex phase 1.15e-08

#### P203. `vortex_positions` - function

- **Definition:** `quantumlab/observables/current.py:40`
- **Signature (verbatim):** `def vortex_positions(wf, min_density: float = 0.2, smoothing: float = 1.0):`
- **Input domain:** wf, min_density=0.2, smoothing=1.0
- **Output domain:** (positions (n,2), charges (n,))
- **Mathematical definition:** phase winding per plaquette, 2pi q; density-masked
- **Preconditions / postconditions enforced:** ENFORCED: TypeError unless Grid2D
- **Actual callers:** examples/11:101,114,175,187; 13:222,223,229,230
- **Test coverage:** tests/test_new_potentials_and_observables.py::test_vortex_positions_finds_imprinted_vortices:127
- **Independent validation:** PARTIALLY - imprinted-vortex positions/charges; no independent analytic field


### `quantumlab/observables/expectation.py`

#### P204. `position_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:4`
- **Signature (verbatim):** `def position_expectation(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** int x |psi|^2 dx
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** benchmarks/validation_suite.py:77,197; runner.py:171; examples; testbench_interlock.py:110
- **Test coverage:** tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_rotation.py::test_coherent_state_in_rotating_frame:19
- **Independent validation:** VERIFIED - Ehrenfest driven oscillator 5.60e-09; rotating frame 1.89e-08

#### P205. `position_squared_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:15`
- **Signature (verbatim):** `def position_squared_expectation(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** int x^2 |psi|^2 dx
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** internal: position_uncertainty:28
- **Test coverage:** indirect: test_observables.py::test_gaussian_observables_and_uncertainty:7
- **Independent validation:** VERIFIED - uncertainty product 4.6e-12

#### P206. `position_uncertainty` - function

- **Definition:** `quantumlab/observables/expectation.py:26`
- **Signature (verbatim):** `def position_uncertainty(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** sqrt(max(<x^2>-<x>^2,0))
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** benchmarks/validation_suite.py:103; examples/01:44,05:65,08:61
- **Test coverage:** tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24
- **Independent validation:** VERIFIED - Heisenberg 4.6e-12

#### P207. `y_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:32`
- **Signature (verbatim):** `def y_expectation(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** int Y |psi|^2 dV
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 2D/3D
- **Actual callers:** benchmarks/validation_suite.py:198; examples/05:64
- **Test coverage:** tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24; test_rotation.py::test_coherent_state_in_rotating_frame:19
- **Independent validation:** VERIFIED - rotating frame 1.89e-08

#### P208. `y_squared_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:41`
- **Signature (verbatim):** `def y_squared_expectation(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** int Y^2 |psi|^2 dV
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 2D/3D
- **Actual callers:** internal: y_uncertainty:52
- **Test coverage:** indirect: test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24
- **Independent validation:** VERIFIED

#### P209. `y_uncertainty` - function

- **Definition:** `quantumlab/observables/expectation.py:50`
- **Signature (verbatim):** `def y_uncertainty(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** sqrt(max(<y^2>-<y>^2,0))
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 2D/3D
- **Actual callers:** benchmarks/validation_suite.py:104; examples/05:66,08:61
- **Test coverage:** tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24
- **Independent validation:** VERIFIED

#### P210. `z_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:56`
- **Signature (verbatim):** `def z_expectation(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** int Z |psi|^2 dV
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 3D
- **Actual callers:** TEST-ONLY: tests/test_3d_observables.py:28,60; test_rotation.py:45
- **Test coverage:** tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24; test_3d_z_expectation_rejects_lower_dimensions:54; test_rotation.py::test_coherent_state_in_rotating_frame_3d:36
- **Independent validation:** PARTIALLY

#### P211. `z_squared_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:63`
- **Signature (verbatim):** `def z_squared_expectation(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** int Z^2 |psi|^2 dV
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 3D
- **Actual callers:** internal: z_uncertainty:72
- **Test coverage:** indirect: test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24
- **Independent validation:** VERIFIED

#### P212. `z_uncertainty` - function

- **Definition:** `quantumlab/observables/expectation.py:70`
- **Signature (verbatim):** `def z_uncertainty(wf) -> float:`
- **Input domain:** wf
- **Output domain:** float
- **Mathematical definition:** sqrt(max(<z^2>-<z>^2,0))
- **Preconditions / postconditions enforced:** ENFORCED: ValueError unless 3D
- **Actual callers:** benchmarks/validation_suite.py:105; examples/08:61
- **Test coverage:** tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24
- **Independent validation:** VERIFIED

#### P213. `momentum_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:76`
- **Signature (verbatim):** `def momentum_expectation(wf, direction: str='x', hbar: float=1.0) -> float:`
- **Input domain:** wf, direction='x', hbar=1
- **Output domain:** float
- **Mathematical definition:** int hbar k |phi|^2 dk (phi=fourier_transform)
- **Preconditions / postconditions enforced:** ENFORCED: ValueError for invalid direction per dimension; TypeError for unsupported wf
- **Actual callers:** testbench_interlock.py:111
- **Test coverage:** tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_momentum_expectation_and_heisenberg:34
- **Independent validation:** VERIFIED - Heisenberg 4.6e-12

#### P214. `momentum_squared_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:105`
- **Signature (verbatim):** `def momentum_squared_expectation(wf, direction: str='x', hbar: float=1.0) -> float:`
- **Input domain:** wf, direction='x', hbar=1
- **Output domain:** float
- **Mathematical definition:** int (hbar k)^2 |phi|^2 dk
- **Preconditions / postconditions enforced:** ENFORCED: ValueError/TypeError as above
- **Actual callers:** internal: kinetic_energy_expectation:156,159,160,163,164,165; momentum_uncertainty:136
- **Test coverage:** indirect: Heisenberg tests
- **Independent validation:** VERIFIED

#### P215. `momentum_uncertainty` - function

- **Definition:** `quantumlab/observables/expectation.py:134`
- **Signature (verbatim):** `def momentum_uncertainty(wf, direction: str='x', hbar: float=1.0) -> float:`
- **Input domain:** wf, direction='x', hbar=1
- **Output domain:** float
- **Mathematical definition:** sqrt(max(<p^2>-<p>^2,0))
- **Preconditions / postconditions enforced:** ENFORCED: ValueError/TypeError as above
- **Actual callers:** benchmarks/validation_suite.py:103,104,105
- **Test coverage:** tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_momentum_expectation_and_heisenberg:34
- **Independent validation:** VERIFIED - Heisenberg 4.6e-12

#### P216. `potential_energy_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:140`
- **Signature (verbatim):** `def potential_energy_expectation(wf, potential) -> float:`
- **Input domain:** wf, potential
- **Output domain:** float
- **Mathematical definition:** int V |psi|^2 dV (0 if potential None)
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** benchmarks/validation_suite.py:173,303,318; examples/08:85; observables/nonlinear.py:13,19,30
- **Test coverage:** tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54; test_multicomponent.py::test_coupled_virial_theorem:107
- **Independent validation:** VERIFIED - GP/coupled virial

#### P217. `kinetic_energy_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:154`
- **Signature (verbatim):** `def kinetic_energy_expectation(wf, hbar: float=1.0, m: float=1.0) -> float:`
- **Input domain:** wf, hbar=1,m=1
- **Output domain:** float
- **Mathematical definition:** sum_axis <p_axis^2>/(2m)
- **Preconditions / postconditions enforced:** ENFORCED: TypeError for unsupported wf type
- **Actual callers:** benchmarks/validation_suite.py:173,302,318; examples/08:84; observables/nonlinear.py:13,19,30
- **Test coverage:** tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54; test_multicomponent.py::test_coupled_virial_theorem:107
- **Independent validation:** VERIFIED - GP/coupled virial

#### P218. `total_energy_expectation` - function

- **Definition:** `quantumlab/observables/expectation.py:170`
- **Signature (verbatim):** `def total_energy_expectation(wf, potential, hbar: float=1.0, m: float=1.0) -> float:`
- **Input domain:** wf, potential, hbar=1,m=1
- **Output domain:** float
- **Mathematical definition:** <T>+<V>
- **Preconditions / postconditions enforced:** Propagates TypeError
- **Actual callers:** benchmarks/validation_suite.py:86,97; runner.py:170; examples/02:36,44,03:47; testbench_interlock.py:103,109
- **Test coverage:** tests/test_solvers.py::test_energy_conservation:20; test_2d_solver.py::test_2d_energy_conservation:23; test_split_operator.py::test_norm_and_energy_conservation:50
- **Independent validation:** VERIFIED - energy conservation 2.18e-10 (order 4, 500 steps)


### `quantumlab/observables/momentum.py`

#### P219. `get_momentum_wavefunction` - function

- **Definition:** `quantumlab/observables/momentum.py:4`
- **Signature (verbatim):** `def get_momentum_wavefunction(wf):`
- **Input domain:** wf
- **Output domain:** ((k...), phi_shifted) fftshifted
- **Mathematical definition:** fftshift of fourier_transform and k axes
- **Preconditions / postconditions enforced:** ENFORCED: implicit (assumes WaveFunction type)
- **Actual callers:** internal: get_momentum_probability_density:24,27,30
- **Test coverage:** indirect: test_3d_observables.py::test_3d_momentum_probability_density:72
- **Independent validation:** PARTIALLY

#### P220. `get_momentum_probability_density` - function

- **Definition:** `quantumlab/observables/momentum.py:22`
- **Signature (verbatim):** `def get_momentum_probability_density(wf):`
- **Input domain:** wf
- **Output domain:** ((k...), |phi|^2) fftshifted
- **Mathematical definition:** |fftshift(phi)|^2
- **Preconditions / postconditions enforced:** ENFORCED: implicit
- **Actual callers:** visualization/plots_1d.py:52
- **Test coverage:** tests/test_3d_observables.py::test_3d_momentum_probability_density:72
- **Independent validation:** VERIFIED - Parseval norm equality 1e-10


### `quantumlab/observables/nonlinear.py`

#### P221. `interaction_energy` - function

- **Definition:** `quantumlab/observables/nonlinear.py:6`
- **Signature (verbatim):** `def interaction_energy(wf, nonlinearity: float) -> float:`
- **Input domain:** wf, nonlinearity
- **Output domain:** float
- **Mathematical definition:** (g/2) int |psi|^4 dV
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:173,318; examples/08:86
- **Test coverage:** tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54; test_conjugate_gradient.py::test_gp_ground_state_without_dtau_floor:27
- **Independent validation:** VERIFIED - GP virial 2.32e-06 / CG 5.79e-10

#### P222. `gross_pitaevskii_energy` - function

- **Definition:** `quantumlab/observables/nonlinear.py:11`
- **Signature (verbatim):** `def gross_pitaevskii_energy(wf, potential, nonlinearity: float, hbar: float = 1.0, m: float = 1.0) -> float:`
- **Input domain:** wf, potential, nonlinearity, hbar=1,m=1
- **Output domain:** float
- **Mathematical definition:** <T>+<V>+(g/2)int|psi|^4
- **Preconditions / postconditions enforced:** Propagates TypeError
- **Actual callers:** examples/09:55,57
- **Test coverage:** tests/test_gross_pitaevskii.py::test_gp_energy_conserved_in_real_time:40; test_rotation.py::test_rotating_gp_ground_state_with_vortex_lattice_beats_vortex_free_state:98
- **Independent validation:** VERIFIED - energy conservation rel 1e-6

#### P223. `chemical_potential` - function

- **Definition:** `quantumlab/observables/nonlinear.py:17`
- **Signature (verbatim):** `def chemical_potential(wf, potential, nonlinearity: float, hbar: float = 1.0, m: float = 1.0) -> float:`
- **Input domain:** wf, potential, nonlinearity, hbar=1,m=1
- **Output domain:** float
- **Mathematical definition:** <T>+<V>+g int|psi|^4
- **Preconditions / postconditions enforced:** Propagates TypeError
- **Actual callers:** TEST-ONLY: tests/test_gross_pitaevskii.py:69
- **Test coverage:** tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54
- **Independent validation:** PARTIALLY - cross-checked against ConvergenceInfo.chemical_potential

#### P224. `coupled_gp_energy` - function

- **Definition:** `quantumlab/observables/nonlinear.py:23`
- **Signature (verbatim):** `def coupled_gp_energy(states, potentials, couplings, hbar: float = 1.0, m: float = 1.0) -> float:`
- **Input domain:** states, potentials, couplings, hbar=1,m=1
- **Output domain:** float
- **Mathematical definition:** sum_i(<T>_i+<V_i>)+0.5 sum_ij g_ij int n_i n_j
- **Preconditions / postconditions enforced:** Propagates TypeError
- **Actual callers:** TEST-ONLY: tests/test_multicomponent.py:100,102
- **Test coverage:** tests/test_multicomponent.py::test_energy_and_populations_conserved_in_real_time:95
- **Independent validation:** VERIFIED - conservation rel 1e-9

#### P225. `miscibility_overlap` - function

- **Definition:** `quantumlab/observables/nonlinear.py:38`
- **Signature (verbatim):** `def miscibility_overlap(wf_a, wf_b) -> float:`
- **Input domain:** wf_a, wf_b
- **Output domain:** float
- **Mathematical definition:** int n_a n_b / sqrt(int n_a^2 int n_b^2)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/13:76,200
- **Test coverage:** tests/test_multicomponent.py::test_miscibility_overlap:122
- **Independent validation:** PARTIALLY - identity/orthogonality limits only


### `quantumlab/strongfield.py`

#### P226. `wavelength_to_omega` - function

- **Definition:** `quantumlab/strongfield.py:17`
- **Signature (verbatim):** `def wavelength_to_omega(wavelength_nm: float) -> float:`
- **Input domain:** wavelength_nm:float
- **Output domain:** float (a.u.)
- **Mathematical definition:** 45.56335253/wavelength_nm
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:217; examples/12:59,87
- **Test coverage:** tests/test_strongfield.py::test_laser_unit_conversions:14
- **Independent validation:** VERIFIED - 800 nm -> 1.5498 eV (probe 0.05695419)

#### P227. `intensity_to_field` - function

- **Definition:** `quantumlab/strongfield.py:22`
- **Signature (verbatim):** `def intensity_to_field(intensity_w_cm2: float) -> float:`
- **Input domain:** intensity_w_cm2:float
- **Output domain:** float (a.u.)
- **Mathematical definition:** sqrt(I/3.50944758e16)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:219; examples/12:61,90,260
- **Test coverage:** tests/test_strongfield.py::test_laser_unit_conversions:14
- **Independent validation:** VERIFIED - probe 1e14 -> 0.05338025

#### P228. `ponderomotive_energy` - function

- **Definition:** `quantumlab/strongfield.py:27`
- **Signature (verbatim):** `def ponderomotive_energy(field: float, omega: float) -> float:`
- **Input domain:** field, omega
- **Output domain:** float (a.u.)
- **Mathematical definition:** E0^2/(4 omega^2)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/12:91,260
- **Test coverage:** tests/test_strongfield.py::test_laser_unit_conversions:14
- **Independent validation:** VERIFIED - probe 0.21960887

#### P229. `classical_returns` - function

- **Definition:** `quantumlab/strongfield.py:32`
- **Signature (verbatim):** `def classical_returns(n_phases: int = 2000):`
- **Input domain:** n_phases=2000
- **Output domain:** (birth_phase, return_phase, return_energy/U_p)
- **Mathematical definition:** three-step model; x=cos phi-cos phi0+(phi-phi0) sin phi0; brentq first crossing; E=2Up(sin phi_r-sin phi0)^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:214; examples/12:137
- **Test coverage:** tests/test_strongfield.py::test_classical_three_step_maximum:22
- **Independent validation:** VERIFIED - max 3.1731, birth 17 deg, return 252 deg; probe 3.1731359 at 17.97 deg

#### P230. `classical_cutoff` - function

- **Definition:** `quantumlab/strongfield.py:65`
- **Signature (verbatim):** `def classical_cutoff(ionisation_potential: float, field: float, omega: float) -> float:`
- **Input domain:** ionisation_potential, field, omega
- **Output domain:** float
- **Mathematical definition:** Ip + max(E_return)/Up * Up
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** TEST-ONLY: tests/test_strongfield.py:30
- **Test coverage:** tests/test_strongfield.py::test_classical_three_step_maximum:22
- **Independent validation:** PARTIALLY

#### P231. `harmonic_spectrum` - function

- **Definition:** `quantumlab/strongfield.py:70`
- **Signature (verbatim):** `def harmonic_spectrum(signal: np.ndarray, dt: float, omega0: float, window: bool = True):`
- **Input domain:** signal, dt, omega0, window=True
- **Output domain:** (omega/omega0, |rfft|^2)
- **Mathematical definition:** Hann window then |FFT|^2 vs harmonic order
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:226; examples/12:77,106
- **Test coverage:** tests/test_strongfield.py::test_harmonic_spectrum_peaks_at_harmonic_orders:60
- **Independent validation:** VERIFIED - HHG odd-harmonic ratio 2.3e3

#### P232. `gabor_transform` - function

- **Definition:** `quantumlab/strongfield.py:83`
- **Signature (verbatim):** `def gabor_transform(signal: np.ndarray, dt: float, omega0: float, orders, width: float,\n                    times=None):`
- **Input domain:** signal, dt, omega0, orders, width, times=None
- **Output domain:** (times, orders, map[time,order])
- **Mathematical definition:** |int a(t') exp(-(t'-t)^2/2sigma^2) exp(-i omega t') dt'|^2
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** examples/12:136,170
- **Test coverage:** tests/test_strongfield.py::test_gabor_transform_locates_burst:72
- **Independent validation:** PARTIALLY - burst localization only

#### P233. `attosecond_pulses` - function

- **Definition:** `quantumlab/strongfield.py:107`
- **Signature (verbatim):** `def attosecond_pulses(signal: np.ndarray, dt: float, omega0: float, order_min: float, order_max: float):`
- **Input domain:** signal, dt, omega0, order_min, order_max
- **Output domain:** float64 (len(signal),)
- **Mathematical definition:** |ifft(band-filtered spectrum)|^2 (analytic signal)
- **Preconditions / postconditions enforced:** NONE
- **Actual callers:** benchmarks/validation_suite.py:235; examples/12:188
- **Test coverage:** tests/test_strongfield.py::test_attosecond_pulses_from_harmonic_comb:83
- **Independent validation:** VERIFIED - half-cycle burst spacing 3.08e-03

#### P234. `dipole_acceleration` - function

- **Definition:** `quantumlab/strongfield.py:119`
- **Signature (verbatim):** `def dipole_acceleration(wf, base_potential, force: float) -> float:`
- **Input domain:** wf, base_potential, force
- **Output domain:** float
- **Mathematical definition:** a(t)=< -dV0/dx > + F(t) (Ehrenfest)
- **Preconditions / postconditions enforced:** ENFORCED: implicit (base_potential must have gradient or evaluate)
- **Actual callers:** benchmarks/validation_suite.py:224; examples/12:68
- **Test coverage:** tests/test_strongfield.py::test_dipole_acceleration_obeys_ehrenfest_in_harmonic_trap:96
- **Independent validation:** VERIFIED - a=-<x>+F to 1e-10; drives HHG spectrum


---

## (a) Producer counts by module

| Module | Producers |
|---|---|
| `quantumlab/core/grid.py` | 9 |
| `quantumlab/core/wavefunction.py` | 27 |
| `quantumlab/core/absorbing_boundary.py` | 9 |
| `quantumlab/core/spectral.py` | 7 |
| `quantumlab/potentials/base.py` | 2 |
| `quantumlab/potentials/apertures.py` | 8 |
| `quantumlab/potentials/barriers.py` | 21 |
| `quantumlab/potentials/coulomb.py` | 5 |
| `quantumlab/potentials/custom.py` | 3 |
| `quantumlab/potentials/disorder.py` | 3 |
| `quantumlab/potentials/oscillator.py` | 3 |
| `quantumlab/potentials/periodic.py` | 3 |
| `quantumlab/potentials/time_dependent.py` | 13 |
| `quantumlab/potentials/traps.py` | 3 |
| `quantumlab/potentials/wells.py` | 9 |
| `quantumlab/potentials/__init__.py` | 1 |
| `quantumlab/solvers/base.py` | 4 |
| `quantumlab/solvers/backends.py` | 5 |
| `quantumlab/solvers/multicomponent.py` | 13 |
| `quantumlab/solvers/split_operator.py` | 17 |
| `quantumlab/solvers/split_step_1d.py` | 4 |
| `quantumlab/solvers/split_step_2d.py` | 4 |
| `quantumlab/solvers/split_step_3d.py` | 4 |
| `quantumlab/solvers/split_step_3d_gpu.py` | 7 |
| `quantumlab/stationary/conjugate_gradient.py` | 1 |
| `quantumlab/stationary/eigensolver.py` | 1 |
| `quantumlab/stationary/hamiltonian.py` | 1 |
| `quantumlab/stationary/imaginary_time.py` | 9 |
| `quantumlab/observables/coefficients.py` | 2 |
| `quantumlab/observables/current.py` | 5 |
| `quantumlab/observables/expectation.py` | 15 |
| `quantumlab/observables/momentum.py` | 2 |
| `quantumlab/observables/nonlinear.py` | 5 |
| `quantumlab/strongfield.py` | 9 |
| **Total** | **234** |

Grouped: core = 52; potentials = 74; solvers = 58; stationary = 12; observables = 29; strongfield = 9.

## (b) Producers with NO caller anywhere (unconsumed)

These have no call/instantiation site in the repository. Abstract base classes are listed separately at the
end because they are consumed through subclassing, not called.

- `quantumlab/core/spectral.py::k_volume_element` - NONE - zero references anywhere in repo
- `quantumlab/potentials/barriers.py::PotentialStep` - NONE (registry-only: potentials/__init__.py:25)
- `quantumlab/potentials/barriers.py::PotentialStep.__init__` - NONE
- `quantumlab/potentials/barriers.py::PotentialStep.evaluate` - NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- `quantumlab/potentials/barriers.py::ResonantTunnelingDiode` - NONE (registry-only: potentials/__init__.py:27)
- `quantumlab/potentials/barriers.py::ResonantTunnelingDiode.__init__` - NONE
- `quantumlab/potentials/barriers.py::ResonantTunnelingDiode.evaluate` - NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- `quantumlab/potentials/disorder.py::RandomDisorder` - NONE (registry-only: potentials/__init__.py:33; imported unused at tests/test_potentials.py:8)
- `quantumlab/potentials/disorder.py::RandomDisorder.__init__` - NONE
- `quantumlab/potentials/disorder.py::RandomDisorder.evaluate` - NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- `quantumlab/potentials/periodic.py::CrystalPotential` - NONE (registry-only: potentials/__init__.py:32; imported unused at tests/test_potentials.py:7)
- `quantumlab/potentials/periodic.py::CrystalPotential.__init__` - NONE
- `quantumlab/potentials/periodic.py::CrystalPotential.evaluate` - NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- `quantumlab/potentials/time_dependent.py::TimeDependentPotential.evaluate` - NONE established (subclasses override evaluate_at; generic .evaluate sites target static potentials)
- `quantumlab/potentials/wells.py::InfiniteSquareWell` - NONE (registry-only: potentials/__init__.py:28)
- `quantumlab/potentials/wells.py::InfiniteSquareWell.__init__` - NONE
- `quantumlab/potentials/wells.py::InfiniteSquareWell.evaluate` - NONE (no call site; only generic Potential.evaluate dispatch could reach it)
- `quantumlab/solvers/base.py::Solver.backend` - NONE (overridden by SplitOperatorSolver.backend:184, SplitStep3DGPU.backend:140, CoupledGPESolver.backend:78)
- `quantumlab/solvers/multicomponent.py::CoupledGPESolver.backend` - NONE (no call site)

Abstract bases with no direct caller (consumed via `class X(Base)`): `quantumlab.potentials.base.Potential`,
`quantumlab.potentials.time_dependent.TimeDependentPotential`, `quantumlab.solvers.base.Solver`.

## (c) Producers with NO test coverage

No direct test and no indirect exercise through a tested caller.

- `quantumlab/core/spectral.py::k_volume_element`
- `quantumlab/potentials/base.py::Potential`
- `quantumlab/potentials/barriers.py::PotentialStep`
- `quantumlab/potentials/barriers.py::PotentialStep.__init__`
- `quantumlab/potentials/barriers.py::PotentialStep.evaluate`
- `quantumlab/potentials/barriers.py::MultipleBarriers`
- `quantumlab/potentials/barriers.py::MultipleBarriers.__init__`
- `quantumlab/potentials/barriers.py::MultipleBarriers.evaluate`
- `quantumlab/potentials/barriers.py::ResonantTunnelingDiode`
- `quantumlab/potentials/barriers.py::ResonantTunnelingDiode.__init__`
- `quantumlab/potentials/barriers.py::ResonantTunnelingDiode.evaluate`
- `quantumlab/potentials/disorder.py::RandomDisorder`
- `quantumlab/potentials/disorder.py::RandomDisorder.__init__`
- `quantumlab/potentials/disorder.py::RandomDisorder.evaluate`
- `quantumlab/potentials/periodic.py::CrystalPotential`
- `quantumlab/potentials/periodic.py::CrystalPotential.__init__`
- `quantumlab/potentials/periodic.py::CrystalPotential.evaluate`
- `quantumlab/potentials/time_dependent.py::TimeDependentPotential`
- `quantumlab/potentials/time_dependent.py::TimeDependentPotential.evaluate`
- `quantumlab/potentials/wells.py::InfiniteSquareWell`
- `quantumlab/potentials/wells.py::InfiniteSquareWell.__init__`
- `quantumlab/potentials/wells.py::InfiniteSquareWell.evaluate`
- `quantumlab/potentials/wells.py::DoubleWell`
- `quantumlab/potentials/wells.py::DoubleWell.__init__`
- `quantumlab/potentials/wells.py::DoubleWell.evaluate`
- `quantumlab/solvers/base.py::Solver`
- `quantumlab/solvers/base.py::Solver.backend`
- `quantumlab/solvers/multicomponent.py::CoupledGPESolver.backend`

## (d) Five producers whose mathematical contract is most safety-critical

1. **`quantumlab.solvers.split_operator.SplitOperatorSolver._kinetic_step` (+ `_strang`/`_advance`)** - the
   core propagator. A wrong kinetic phase or splitting weight breaks unitarity and every dynamics result; it
   is the single most reused numerical contract in the package. Independent evidence: convergence orders
   2.001/3.997, exact free-Gaussian spreading 1.37e-15, exact soliton 1.46e-09, 3D norm 2.55e-15, energy 2.18e-10.
2. **`quantumlab.core.wavefunction.WaveFunction1D/2D/3D.fourier_transform`** - fixes the momentum-space measure
   (`dx^d/(2 pi)^{d/2}`). An error propagates into `momentum_expectation`, `kinetic_energy_expectation` and
   `total_energy_expectation`, i.e. into every reported energy. Independent evidence: Parseval probe
   0.9999999999999997 and the 3D Parseval test; Heisenberg product 4.6e-12.
3. **`quantumlab.stationary.eigensolver.eigenstates`** - produces the energies and eigenstates used as physical
   predictions (e.g. the hydrogen ionisation potential). Independent evidence: exact harmonic spectra to
   7.28e-14 (Lanczos) / 1.42e-13 (LOBPCG), soft-core hydrogen -0.5 to 1.94e-14, Lanczos/LOBPCG agreement 1e-9.
4. **`quantumlab.core.absorbing_boundary.AbsorbingBoundaryLayer._polynomial_profile` (+ `apply`)** - the mask
   is applied every step; a bad profile silently deletes the state or injects NaN (the documented defect
   D-P2-2 fixed at HEAD). Independent evidence: finiteness/monotonicity/edge tests and the HHG flux-absorption
   check; probe confirms finite [0,1] masks for orders 1..6.
5. **`quantumlab.potentials.coulomb.SoftCoulomb.evaluate` (+ `gradient`)** - the strong-field model potential;
   its analytic gradient enters `dipole_acceleration` and therefore the HHG/attosecond spectra. Independent
   evidence: hydrogen ground state -0.5 to 1.94e-14, gradient vs central finite differences atol 1e-3, HHG
   odd-harmonic ratio 2.3e3.

Runners-up: `SplitOperatorSolver._potential_half_step` (nonlinear/imaginary-time midpoint),
`CoupledGPESolver._potential_half_step` (coupled densities), `observables.current.probability_current`
(continuity equation), `strongfield.harmonic_spectrum` (HHG readout).
