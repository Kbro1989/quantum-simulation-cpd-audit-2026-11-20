
## Grid1D  [quantumlab/core/grid.py:3] (class)
SIG: class Grid1D(...):
EXT_CALLS (66):
  benchmarks/validation_suite.py:42: grid = Grid1D(1024, -60.0, 60.0)
  benchmarks/validation_suite.py:52: grid = Grid1D(256, -12.0, 12.0)
  benchmarks/validation_suite.py:69: grid = Grid1D(512, -30.0, 30.0)
  benchmarks/validation_suite.py:118: grid = Grid1D(256, -12.0, 12.0)
  benchmarks/validation_suite.py:135: grid = Grid1D(256, -12.0, 12.0)
  benchmarks/validation_suite.py:160: grid = Grid1D(2048, -60.0, 60.0)
  benchmarks/validation_suite.py:209: grid = Grid1D(4096, -200.0, 200.0)
  benchmarks/validation_suite.py:248: box = Grid1D(256, -20 * np.pi, 20 * np.pi)
  benchmarks/validation_suite.py:312: _, info = ground_state_pcg(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), tol=1e-10)
  examples/01_gaussian_barrier.py:29: grid = Grid1D(N, -L / 2, L / 2)
  examples/02_harmonic_oscillator.py:27: grid = Grid1D(N, -L / 2, L / 2)
  examples/03_double_well.py:28: grid = Grid1D(N, -L / 2, L / 2)
  examples/04_multiple_barriers.py:30: grid = Grid1D(N, -L / 2, L / 2)
  examples/09_soliton_collision.py:46: grid = Grid1D(2048, -40.0, 40.0)
  examples/12_high_harmonic_generation.py:51: GRID = Grid1D(4096, -200.0, 200.0)
  quantumlab/runner.py:54: return Grid1D(N, -L / 2.0, L / 2.0)
  testbench_interlock.py:97: grid = Grid1D(N=1024, x_min=-50.0, x_max=50.0)
  tests/test_2d_solver.py:38: grid = Grid1D(256, -50.0, 50.0)
  tests/test_2d_solver.py:57: grid = Grid1D(256, -50.0, 50.0)
  tests/test_absorbing_boundary_validation.py:17: Grid1D(32, -10.0, 10.0),
  tests/test_absorbing_boundary_validation.py:79: grid = Grid1D(64, -20.0, 20.0)
  tests/test_absorbing_boundary_validation.py:90: grid = Grid1D(64, -20.0, 20.0)
  tests/test_absorbing_boundary_validation.py:99: grid = Grid1D(64, -20.0, 20.0)
  tests/test_backends.py:76: '1d_barrier_order4': lambda: (Grid1D(256, -20.0, 20.0), GaussianBarrier(3.0, 1.0, 0.0), dict(order=4),
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:78: '1d_driven': lambda: (Grid1D(128, -15.0, 15.0), DipoleDrive(HarmonicTrap(1.0), 0.4, 0.7), dict(order=4),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:110: grid = Grid1D(256, -20.0, 20.0)
  tests/test_conjugate_gradient.py:14: (Grid1D(256, -12.0, 12.0), HarmonicTrap(1.0), {}, 0.5),
  tests/test_conjugate_gradient.py:15: (Grid1D(2048, -100.0, 100.0), SoftCoulomb(), {}, -0.5),                       # V < 0
  tests/test_conjugate_gradient.py:16: (Grid1D(256, -12.0, 12.0), HarmonicTrap(2.0, m=0.5), dict(hbar=0.7, m=0.5), 0.7),
  tests/test_conjugate_gradient.py:42: grid = Grid1D(256, -12.0, 12.0)
  tests/test_conjugate_gradient.py:64: ground_state_pcg(Grid1D(64, -6.0, 6.0), HarmonicTrap(1.0), tol=1e-8,
  tests/test_conjugate_gradient.py:68: ground_state_pcg(Grid1D(32, -4.0, 4.0), DipoleDrive(None, 1.0, 1.0))
  tests/test_gross_pitaevskii.py:21: grid = Grid1D(2048, -60.0, 60.0)
  tests/test_gross_pitaevskii.py:34: grid = Grid1D(2048, -60.0, 60.0)
  tests/test_gross_pitaevskii.py:57: grid, omegas, g = Grid1D(256, -12.0, 12.0), 1.0, 20.0
  tests/test_multicomponent.py:49: return Grid1D(256, -20 * np.pi, 20 * np.pi)       # periodic, dk = 0.05
  tests/test_multicomponent.py:131: grid = Grid1D(32, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:75: grid = Grid1D(8, -1.0, 1.0)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
  tests/test_new_potentials_and_observables.py:85: grid = Grid1D(512, -25.0, 25.0)
  tests/test_new_potentials_and_observables.py:109: grid = Grid1D(256, -12.0, 12.0)
  tests/test_observables.py:8: grid = Grid1D(1024, -50.0, 50.0)
  tests/test_potentials.py:13: grid = Grid1D(256, -10.0, 10.0)
  tests/test_potentials.py:26: grid = Grid1D(256, -10.0, 10.0)
  tests/test_potentials.py:37: grid = Grid1D(128, -5.0, 5.0)
  tests/test_potentials.py:46: grid = Grid1D(128, -5.0, 5.0)
  tests/test_rotation.py:116: SplitOperatorSolver(Grid1D(32, -4.0, 4.0), None, 0.01, rotation=0.5)
  tests/test_solvers.py:10: grid = Grid1D(512, -25.0, 25.0)
  tests/test_solvers.py:21: grid = Grid1D(512, -25.0, 25.0)
  tests/test_split_operator.py:28: grid = Grid1D(256, -20.0, 20.0)
  tests/test_split_operator.py:51: grid = Grid1D(512, -30.0, 30.0)
  tests/test_split_operator.py:66: grid = Grid1D(256, -12.0, 12.0)
  tests/test_split_operator.py:81: grid = Grid1D(256, -12.0, 12.0)
  tests/test_split_operator.py:94: grid = Grid1D(512, -30.0, 30.0)
  tests/test_split_operator.py:105: grid = Grid1D(256, -20.0, 20.0)
  tests/test_split_operator.py:115: grid = Grid1D(1024, -60.0, 60.0)
  tests/test_split_operator.py:125: grid = Grid1D(512, -20.0, 20.0)
  tests/test_split_operator.py:135: grid = Grid1D(64, -5.0, 5.0)
  tests/test_split_operator.py:145: grid = Grid1D(64, -5.0, 5.0)
  tests/test_stationary.py:15: grid = Grid1D(256, -12.0, 12.0)
  tests/test_stationary.py:55: grid = Grid1D(256, -10.0, 10.0)
  tests/test_stationary.py:64: grid = Grid1D(256, -10.0, 10.0)
  tests/test_strongfield.py:34: energies, _ = eigenstates(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), n_states=2)
  tests/test_strongfield.py:98: grid = Grid1D(256, -12.0, 12.0)
EXT_OTHER (70):
  benchmarks/validation_suite.py:42: grid = Grid1D(1024, -60.0, 60.0)
  benchmarks/validation_suite.py:52: grid = Grid1D(256, -12.0, 12.0)
  benchmarks/validation_suite.py:69: grid = Grid1D(512, -30.0, 30.0)
  benchmarks/validation_suite.py:118: grid = Grid1D(256, -12.0, 12.0)
  benchmarks/validation_suite.py:135: grid = Grid1D(256, -12.0, 12.0)
  benchmarks/validation_suite.py:160: grid = Grid1D(2048, -60.0, 60.0)
  benchmarks/validation_suite.py:209: grid = Grid1D(4096, -200.0, 200.0)
  benchmarks/validation_suite.py:248: box = Grid1D(256, -20 * np.pi, 20 * np.pi)
  benchmarks/validation_suite.py:312: _, info = ground_state_pcg(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), tol=1e-10)
  examples/01_gaussian_barrier.py:29: grid = Grid1D(N, -L / 2, L / 2)
  examples/02_harmonic_oscillator.py:27: grid = Grid1D(N, -L / 2, L / 2)
  examples/03_double_well.py:28: grid = Grid1D(N, -L / 2, L / 2)
  examples/04_multiple_barriers.py:30: grid = Grid1D(N, -L / 2, L / 2)
  examples/09_soliton_collision.py:46: grid = Grid1D(2048, -40.0, 40.0)
  examples/12_high_harmonic_generation.py:51: GRID = Grid1D(4096, -200.0, 200.0)
  quantumlab/core/absorbing_boundary.py:81: if isinstance(self.grid, Grid1D):
  quantumlab/core/spectral.py:16: elif isinstance(grid, Grid1D):
  quantumlab/core/wavefunction.py:6: def __init__(self, grid: Grid1D, psi: np.ndarray=None):
  quantumlab/core/wavefunction.py:35: def gaussian(cls, grid: Grid1D, x0: float, k0: float, sigma: float) -> 'WaveFunction1D':
  quantumlab/runner.py:54: return Grid1D(N, -L / 2.0, L / 2.0)
  testbench_interlock.py:97: grid = Grid1D(N=1024, x_min=-50.0, x_max=50.0)
  tests/test_2d_solver.py:38: grid = Grid1D(256, -50.0, 50.0)
  tests/test_2d_solver.py:57: grid = Grid1D(256, -50.0, 50.0)
  tests/test_absorbing_boundary_validation.py:17: Grid1D(32, -10.0, 10.0),
  tests/test_absorbing_boundary_validation.py:79: grid = Grid1D(64, -20.0, 20.0)
  tests/test_absorbing_boundary_validation.py:90: grid = Grid1D(64, -20.0, 20.0)
  tests/test_absorbing_boundary_validation.py:99: grid = Grid1D(64, -20.0, 20.0)
  tests/test_backends.py:76: '1d_barrier_order4': lambda: (Grid1D(256, -20.0, 20.0), GaussianBarrier(3.0, 1.0, 0.0), dict(order=4),
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:78: '1d_driven': lambda: (Grid1D(128, -15.0, 15.0), DipoleDrive(HarmonicTrap(1.0), 0.4, 0.7), dict(order=4),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:110: grid = Grid1D(256, -20.0, 20.0)
  tests/test_conjugate_gradient.py:14: (Grid1D(256, -12.0, 12.0), HarmonicTrap(1.0), {}, 0.5),
  tests/test_conjugate_gradient.py:15: (Grid1D(2048, -100.0, 100.0), SoftCoulomb(), {}, -0.5),                       # V < 0
  tests/test_conjugate_gradient.py:16: (Grid1D(256, -12.0, 12.0), HarmonicTrap(2.0, m=0.5), dict(hbar=0.7, m=0.5), 0.7),
  tests/test_conjugate_gradient.py:42: grid = Grid1D(256, -12.0, 12.0)
  tests/test_conjugate_gradient.py:64: ground_state_pcg(Grid1D(64, -6.0, 6.0), HarmonicTrap(1.0), tol=1e-8,
  tests/test_conjugate_gradient.py:68: ground_state_pcg(Grid1D(32, -4.0, 4.0), DipoleDrive(None, 1.0, 1.0))
  tests/test_gross_pitaevskii.py:21: grid = Grid1D(2048, -60.0, 60.0)
  tests/test_gross_pitaevskii.py:34: grid = Grid1D(2048, -60.0, 60.0)
  tests/test_gross_pitaevskii.py:57: grid, omegas, g = Grid1D(256, -12.0, 12.0), 1.0, 20.0
  tests/test_multicomponent.py:49: return Grid1D(256, -20 * np.pi, 20 * np.pi)       # periodic, dk = 0.05
  tests/test_multicomponent.py:131: grid = Grid1D(32, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:75: grid = Grid1D(8, -1.0, 1.0)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
  tests/test_new_potentials_and_observables.py:85: grid = Grid1D(512, -25.0, 25.0)
  tests/test_new_potentials_and_observables.py:109: grid = Grid1D(256, -12.0, 12.0)
  tests/test_observables.py:8: grid = Grid1D(1024, -50.0, 50.0)
  tests/test_potentials.py:13: grid = Grid1D(256, -10.0, 10.0)
  tests/test_potentials.py:26: grid = Grid1D(256, -10.0, 10.0)
  tests/test_potentials.py:37: grid = Grid1D(128, -5.0, 5.0)
  tests/test_potentials.py:46: grid = Grid1D(128, -5.0, 5.0)
  tests/test_rotation.py:116: SplitOperatorSolver(Grid1D(32, -4.0, 4.0), None, 0.01, rotation=0.5)
  tests/test_solvers.py:10: grid = Grid1D(512, -25.0, 25.0)
  tests/test_solvers.py:21: grid = Grid1D(512, -25.0, 25.0)
  tests/test_split_operator.py:28: grid = Grid1D(256, -20.0, 20.0)
  tests/test_split_operator.py:51: grid = Grid1D(512, -30.0, 30.0)
  tests/test_split_operator.py:66: grid = Grid1D(256, -12.0, 12.0)
  tests/test_split_operator.py:81: grid = Grid1D(256, -12.0, 12.0)
  tests/test_split_operator.py:94: grid = Grid1D(512, -30.0, 30.0)
  tests/test_split_operator.py:105: grid = Grid1D(256, -20.0, 20.0)
  tests/test_split_operator.py:115: grid = Grid1D(1024, -60.0, 60.0)
  tests/test_split_operator.py:125: grid = Grid1D(512, -20.0, 20.0)
  tests/test_split_operator.py:135: grid = Grid1D(64, -5.0, 5.0)
  tests/test_split_operator.py:145: grid = Grid1D(64, -5.0, 5.0)
  tests/test_stationary.py:15: grid = Grid1D(256, -12.0, 12.0)
  tests/test_stationary.py:55: grid = Grid1D(256, -10.0, 10.0)
  tests/test_stationary.py:64: grid = Grid1D(256, -10.0, 10.0)
  tests/test_strongfield.py:34: energies, _ = eigenstates(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), n_states=2)
  tests/test_strongfield.py:98: grid = Grid1D(256, -12.0, 12.0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (33): benchmarks/validation_suite.py:14(quantumlab.core.grid), examples/01_gaussian_barrier.py:4(quantumlab.core.grid), examples/02_harmonic_oscillator.py:4(quantumlab.core.grid), examples/03_double_well.py:3(quantumlab.core.grid), examples/04_multiple_barriers.py:3(quantumlab.core.grid), examples/09_soliton_collision.py:19(quantumlab.core.grid), examples/12_high_harmonic_generation.py:40(quantumlab.core.grid), quantumlab/core/__init__.py:1(quantumlab.core.grid), quantumlab/core/absorbing_boundary.py:4(quantumlab.core.grid), quantumlab/core/spectral.py:7(quantumlab.core.grid), quantumlab/core/wavefunction.py:2(quantumlab.core.grid), quantumlab/potentials/barriers.py:3(quantumlab.core.grid), quantumlab/potentials/custom.py:3(quantumlab.core.grid), quantumlab/potentials/disorder.py:3(quantumlab.core.grid), quantumlab/potentials/oscillator.py:3(quantumlab.core.grid), quantumlab/potentials/periodic.py:3(quantumlab.core.grid), quantumlab/potentials/wells.py:3(quantumlab.core.grid), quantumlab/runner.py:11(quantumlab.core.grid), testbench_interlock.py:34(quantumlab.core.grid), tests/test_2d_solver.py:3(quantumlab.core.grid), tests/test_absorbing_boundary_validation.py:13(quantumlab.core.grid), tests/test_backends.py:14(quantumlab.core.grid), tests/test_conjugate_gradient.py:3(quantumlab.core.grid), tests/test_gross_pitaevskii.py:3(quantumlab.core.grid), tests/test_multicomponent.py:3(quantumlab.core.grid), tests/test_new_potentials_and_observables.py:3(quantumlab.core.grid), tests/test_observables.py:3(quantumlab.core.grid), tests/test_potentials.py:3(quantumlab.core.grid), tests/test_rotation.py:3(quantumlab.core.grid), tests/test_solvers.py:3(quantumlab.core.grid), tests/test_split_operator.py:3(quantumlab.core.grid), tests/test_stationary.py:3(quantumlab.core.grid), tests/test_strongfield.py:3(quantumlab.core.grid)

## Grid1D.__init__  [quantumlab/core/grid.py:5] (method)
SIG: def __init__(self, N: int, x_min: float, x_max: float):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Grid1D.shape  [quantumlab/core/grid.py:16] (method)
SIG: def shape(self):
EXT_CALLS (0):
EXT_OTHER (46):
  benchmarks/validation_suite.py:93: roundoff = fft_pairs * np.finfo(float).eps * np.log2(np.prod(grid.shape))
  examples/07_3d_double_slit.py:56: print(f'Grid {grid.N_x}×{grid.N_y}×{grid.N_z} = {np.prod(grid.shape):,} points, dt = {dt}')
  examples/08_3d_bec_time_of_flight.py:78: print(f'Grid {grid.N_x}×{grid.N_y}×{grid.N_z} = {np.prod(grid.shape):,} points, '
  examples/13_two_component_bec.py:116: noise = 1e-4 * (rng.standard_normal(grid.shape) + 1j * rng.standard_normal(grid.shape))
  quantumlab/core/wavefunction.py:11: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:12: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/core/wavefunction.py:46: self.psi = np.zeros(grid.shape, dtype=complex)
  quantumlab/core/wavefunction.py:48: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:49: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/core/wavefunction.py:85: self.psi = np.zeros(grid.shape, dtype=complex)
  quantumlab/core/wavefunction.py:87: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:88: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/potentials/apertures.py:68: opening = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:56: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:62: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:84: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:91: V = np.zeros(grid.shape)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/traps.py:32: V = np.zeros(grid.shape)
  quantumlab/solvers/multicomponent.py:44: if g.shape != (self.n_components, self.n_components):
  quantumlab/solvers/multicomponent.py:70: self._V = [self._be.to_device(np.zeros(grid.shape) if p is None else
  quantumlab/solvers/split_operator.py:142: self._V_static = (np.zeros(grid.shape) if potential is None
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:44: shape = grid.shape
  quantumlab/stationary/eigensolver.py:45: axes = tuple(range(len(shape)))
  quantumlab/stationary/eigensolver.py:46: size = int(np.prod(shape))
  quantumlab/stationary/eigensolver.py:52: return v.reshape(shape + (-1,)), v.ndim == 1
  quantumlab/stationary/eigensolver.py:102: psi = vecs[:, j].reshape(shape) / np.sqrt(dV)
  quantumlab/stationary/eigensolver.py:105: idx = np.unravel_index(np.argmax(np.abs(psi)), shape)
  quantumlab/stationary/imaginary_time.py:160: guess = envelope * rng.standard_normal(grid.shape)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  tests/test_2d_solver.py:50: assert abl.mask.shape == (128, 128)
  tests/test_3d_observables.py:76: assert prob_k.shape == grid.shape
  tests/test_3d_solver.py:36: assert grid.shape == (32, 32, 32)
  tests/test_3d_solver.py:37: assert grid.X.shape == (32, 32, 32)
  tests/test_3d_solver.py:38: assert grid.K_x.shape == (32, 32, 32)
  tests/test_3d_solver.py:63: assert wf.slice_xy().shape == (32, 32)
  tests/test_3d_solver.py:64: assert wf.slice_xz().shape == (32, 32)
  tests/test_3d_solver.py:65: assert wf.slice_yz().shape == (32, 32)
  tests/test_3d_solver.py:112: assert abl.mask.shape == (32, 32, 32)
  tests/test_absorbing_boundary_validation.py:72: assert abl.mask.shape == grid.shape
  tests/test_absorbing_boundary_validation.py:112: assert abl.mask.shape == GRIDS[0].shape
  tests/test_potentials.py:19: assert V.shape == (256,)
  tests/test_strongfield.py:78: i, j = np.unravel_index(np.argmax(G), G.shape)
  tests/test_volume_3d.py:29: assert extract_isosurface(np.zeros(grid.shape), 1.0, grid) is None
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Grid2D  [quantumlab/core/grid.py:19] (class)
SIG: class Grid2D(...):
EXT_CALLS (52):
  benchmarks/validation_suite.py:111: grid = Grid2D(128, -8.0, 8.0, 128, -8.0, 8.0)
  benchmarks/validation_suite.py:179: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  benchmarks/validation_suite.py:189: grid = Grid2D(128, -12.0, 12.0, 128, -12.0, 12.0)
  benchmarks/validation_suite.py:283: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  benchmarks/validation_suite.py:296: grid = Grid2D(80, -9.0, 9.0, 80, -9.0, 9.0)
  examples/05_2d_gaussian_barrier.py:36: grid = Grid2D(Nx, -Lx / 2, Lx / 2, Ny, -Ly / 2, Ly / 2)
  examples/10_quantum_chaos_stadium.py:34: grid = Grid2D(176, -5.5, 5.5, 96, -3.0, 3.0)
  examples/11_rotating_bec_vortex_lattice.py:65: grid = Grid2D(128, -10.0, 10.0, 128, -10.0, 10.0)
  examples/11_rotating_bec_vortex_lattice.py:174: mid = WaveFunction2D(Grid2D(grid3.N_x, -10.0, 10.0, grid3.N_y, -10.0, 10.0), wf3.psi[:, :, k0])
  examples/13_two_component_bec.py:67: grid = Grid2D(96, -9.0, 9.0, 96, -9.0, 9.0)
  examples/13_two_component_bec.py:108: grid = Grid2D(N, -L / 2, L / 2, N, -L / 2, L / 2)
  examples/13_two_component_bec.py:193: grid = Grid2D(128, -10.0, 10.0, 128, -10.0, 10.0)
  quantumlab/runner.py:56: return Grid2D(N, -L / 2.0, L / 2.0, N, -L / 2.0, L / 2.0)
  tests/test_2d_solver.py:13: grid = Grid2D(128, -20.0, 20.0, 128, -20.0, 20.0)
  tests/test_2d_solver.py:25: grid = Grid2D(128, -10.0, 10.0, 128, -10.0, 10.0)
  tests/test_2d_solver.py:48: grid = Grid2D(128, -20.0, 20.0, 128, -20.0, 20.0)
  tests/test_3d_observables.py:57: grid = Grid2D(32, -5.0, 5.0, 32, -5.0, 5.0)
  tests/test_absorbing_boundary_validation.py:18: Grid2D(16, -10.0, 10.0, 16, -10.0, 10.0),
  tests/test_backends.py:80: '2d_gpe_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap(1.0),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:84: '2d_damped_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap((1.0, 1.1)),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:124: grid = Grid2D(32, -6.0, 6.0, 32, -6.0, 6.0)
  tests/test_backends.py:137: grid = Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0)
  tests/test_backends.py:170: grid = Grid2D(40, -7.0, 7.0, 40, -7.0, 7.0)
  tests/test_conjugate_gradient.py:50: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_gross_pitaevskii.py:41: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_gross_pitaevskii.py:59: grid, omegas, g = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0), (1.0, 1.3), 50.0
  tests/test_multicomponent.py:21: grid = Grid2D(48, -7.0, 7.0, 48, -7.0, 7.0)
  tests/test_multicomponent.py:34: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_multicomponent.py:96: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_multicomponent.py:109: grid = Grid2D(80, -9.0, 9.0, 80, -9.0, 9.0)
  tests/test_multicomponent.py:123: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:21: grid = Grid2D(16, -4.0, 4.0, 16, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:48: grid = Grid2D(128, -8.0, 8.0, 128, -6.0, 6.0)
  tests/test_new_potentials_and_observables.py:100: grid = Grid2D(128, -8.0, 8.0, 128, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:129: grid = Grid2D(128, -8.0, 8.0, 128, -8.0, 8.0)
  tests/test_rotation.py:24: grid = Grid2D(128, -12.0, 12.0, 128, -12.0, 12.0)
  tests/test_rotation.py:50: grid = Grid2D(128, -12.0, 12.0, 128, -12.0, 12.0)
  tests/test_rotation.py:63: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_rotation.py:76: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_rotation.py:90: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_rotation.py:100: grid = Grid2D(96, -8.0, 8.0, 96, -8.0, 8.0)
  tests/test_rotation.py:117: grid = Grid2D(16, -4.0, 4.0, 16, -4.0, 4.0)
  tests/test_rotation.py:127: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_rotation.py:137: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_split_operator.py:32: grid = Grid2D(64, -10.0, 10.0, 64, -10.0, 10.0)
  tests/test_stationary.py:22: grid = Grid2D(96, -9.0, 9.0, 96, -9.0, 9.0)
  tests/test_stationary.py:39: grid = Grid2D(64, -6.0, 6.0, 64, -4.0, 4.0)
  tests/test_stationary.py:74: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_strongfield.py:42: grid = Grid2D(600, -6.0, 6.0, 600, -6.0, 6.0)
  tests/test_volume_3d.py:78: IsosurfaceRenderer(Grid2D(8, -1, 1, 8, -1, 1))
EXT_OTHER (73):
  benchmarks/validation_suite.py:111: grid = Grid2D(128, -8.0, 8.0, 128, -8.0, 8.0)
  benchmarks/validation_suite.py:179: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  benchmarks/validation_suite.py:189: grid = Grid2D(128, -12.0, 12.0, 128, -12.0, 12.0)
  benchmarks/validation_suite.py:283: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  benchmarks/validation_suite.py:296: grid = Grid2D(80, -9.0, 9.0, 80, -9.0, 9.0)
  examples/05_2d_gaussian_barrier.py:36: grid = Grid2D(Nx, -Lx / 2, Lx / 2, Ny, -Ly / 2, Ly / 2)
  examples/10_quantum_chaos_stadium.py:34: grid = Grid2D(176, -5.5, 5.5, 96, -3.0, 3.0)
  examples/11_rotating_bec_vortex_lattice.py:65: grid = Grid2D(128, -10.0, 10.0, 128, -10.0, 10.0)
  examples/11_rotating_bec_vortex_lattice.py:174: mid = WaveFunction2D(Grid2D(grid3.N_x, -10.0, 10.0, grid3.N_y, -10.0, 10.0), wf3.psi[:, :, k0])
  examples/13_two_component_bec.py:67: grid = Grid2D(96, -9.0, 9.0, 96, -9.0, 9.0)
  examples/13_two_component_bec.py:108: grid = Grid2D(N, -L / 2, L / 2, N, -L / 2, L / 2)
  examples/13_two_component_bec.py:193: grid = Grid2D(128, -10.0, 10.0, 128, -10.0, 10.0)
  quantumlab/core/absorbing_boundary.py:83: elif isinstance(self.grid, Grid2D):
  quantumlab/core/spectral.py:14: elif isinstance(grid, Grid2D):
  quantumlab/core/wavefunction.py:43: def __init__(self, grid: Grid2D, psi: np.ndarray=None):
  quantumlab/core/wavefunction.py:72: def gaussian(cls, grid: Grid2D, x0: float, y0: float, k0_x: float, k0_y: float, sigma_x: float, sigma_y: float) -> 'WaveFunction2D':
  quantumlab/observables/current.py:28: if not isinstance(wf.grid, (Grid2D, Grid3D)):
  quantumlab/observables/current.py:63: if not isinstance(wf.grid, Grid2D):
  quantumlab/potentials/apertures.py:60: if not isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/apertures.py:97: if not isinstance(grid, Grid2D):
  quantumlab/potentials/barriers.py:13: if isinstance(grid, Grid2D):
  quantumlab/potentials/barriers.py:28: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:42: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:55: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:81: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:124: if isinstance(grid, Grid2D):
  quantumlab/potentials/custom.py:15: elif isinstance(grid, Grid2D):
  quantumlab/potentials/disorder.py:14: if isinstance(grid, Grid2D):
  quantumlab/potentials/oscillator.py:17: elif isinstance(grid, Grid2D):
  quantumlab/potentials/periodic.py:13: if isinstance(grid, Grid2D):
  quantumlab/potentials/wells.py:13: if isinstance(grid, Grid2D):
  quantumlab/potentials/wells.py:28: if isinstance(grid, Grid2D):
  quantumlab/potentials/wells.py:43: if isinstance(grid, Grid2D):
  quantumlab/runner.py:56: return Grid2D(N, -L / 2.0, L / 2.0, N, -L / 2.0, L / 2.0)
  tests/test_2d_solver.py:13: grid = Grid2D(128, -20.0, 20.0, 128, -20.0, 20.0)
  tests/test_2d_solver.py:25: grid = Grid2D(128, -10.0, 10.0, 128, -10.0, 10.0)
  tests/test_2d_solver.py:48: grid = Grid2D(128, -20.0, 20.0, 128, -20.0, 20.0)
  tests/test_3d_observables.py:57: grid = Grid2D(32, -5.0, 5.0, 32, -5.0, 5.0)
  tests/test_absorbing_boundary_validation.py:18: Grid2D(16, -10.0, 10.0, 16, -10.0, 10.0),
  tests/test_backends.py:80: '2d_gpe_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap(1.0),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:84: '2d_damped_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap((1.0, 1.1)),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:124: grid = Grid2D(32, -6.0, 6.0, 32, -6.0, 6.0)
  tests/test_backends.py:137: grid = Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0)
  tests/test_backends.py:170: grid = Grid2D(40, -7.0, 7.0, 40, -7.0, 7.0)
  tests/test_conjugate_gradient.py:50: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_gross_pitaevskii.py:41: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_gross_pitaevskii.py:59: grid, omegas, g = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0), (1.0, 1.3), 50.0
  tests/test_multicomponent.py:21: grid = Grid2D(48, -7.0, 7.0, 48, -7.0, 7.0)
  tests/test_multicomponent.py:34: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_multicomponent.py:96: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_multicomponent.py:109: grid = Grid2D(80, -9.0, 9.0, 80, -9.0, 9.0)
  tests/test_multicomponent.py:123: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:21: grid = Grid2D(16, -4.0, 4.0, 16, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:48: grid = Grid2D(128, -8.0, 8.0, 128, -6.0, 6.0)
  tests/test_new_potentials_and_observables.py:100: grid = Grid2D(128, -8.0, 8.0, 128, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:129: grid = Grid2D(128, -8.0, 8.0, 128, -8.0, 8.0)
  tests/test_rotation.py:24: grid = Grid2D(128, -12.0, 12.0, 128, -12.0, 12.0)
  tests/test_rotation.py:50: grid = Grid2D(128, -12.0, 12.0, 128, -12.0, 12.0)
  tests/test_rotation.py:63: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_rotation.py:76: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_rotation.py:90: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_rotation.py:100: grid = Grid2D(96, -8.0, 8.0, 96, -8.0, 8.0)
  tests/test_rotation.py:117: grid = Grid2D(16, -4.0, 4.0, 16, -4.0, 4.0)
  tests/test_rotation.py:127: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_rotation.py:137: grid = Grid2D(96, -10.0, 10.0, 96, -10.0, 10.0)
  tests/test_split_operator.py:32: grid = Grid2D(64, -10.0, 10.0, 64, -10.0, 10.0)
  tests/test_stationary.py:22: grid = Grid2D(96, -9.0, 9.0, 96, -9.0, 9.0)
  tests/test_stationary.py:39: grid = Grid2D(64, -6.0, 6.0, 64, -4.0, 4.0)
  tests/test_stationary.py:74: grid = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_strongfield.py:42: grid = Grid2D(600, -6.0, 6.0, 600, -6.0, 6.0)
  tests/test_volume_3d.py:78: IsosurfaceRenderer(Grid2D(8, -1, 1, 8, -1, 1))
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (33): benchmarks/validation_suite.py:14(quantumlab.core.grid), examples/05_2d_gaussian_barrier.py:3(quantumlab.core.grid), examples/10_quantum_chaos_stadium.py:24(quantumlab.core.grid), examples/11_rotating_bec_vortex_lattice.py:42(quantumlab.core.grid), examples/13_two_component_bec.py:39(quantumlab.core.grid), quantumlab/core/__init__.py:1(quantumlab.core.grid), quantumlab/core/absorbing_boundary.py:4(quantumlab.core.grid), quantumlab/core/spectral.py:7(quantumlab.core.grid), quantumlab/core/wavefunction.py:2(quantumlab.core.grid), quantumlab/observables/current.py:7(quantumlab.core.grid), quantumlab/potentials/apertures.py:3(quantumlab.core.grid), quantumlab/potentials/barriers.py:3(quantumlab.core.grid), quantumlab/potentials/custom.py:3(quantumlab.core.grid), quantumlab/potentials/disorder.py:3(quantumlab.core.grid), quantumlab/potentials/oscillator.py:3(quantumlab.core.grid), quantumlab/potentials/periodic.py:3(quantumlab.core.grid), quantumlab/potentials/wells.py:3(quantumlab.core.grid), quantumlab/runner.py:11(quantumlab.core.grid), tests/test_2d_solver.py:3(quantumlab.core.grid), tests/test_3d_observables.py:55(quantumlab.core.grid), tests/test_absorbing_boundary_validation.py:13(quantumlab.core.grid), tests/test_backends.py:14(quantumlab.core.grid), tests/test_conjugate_gradient.py:3(quantumlab.core.grid), tests/test_gross_pitaevskii.py:3(quantumlab.core.grid), tests/test_multicomponent.py:3(quantumlab.core.grid), tests/test_new_potentials_and_observables.py:3(quantumlab.core.grid), tests/test_potentials.py:3(quantumlab.core.grid), tests/test_rotation.py:3(quantumlab.core.grid), tests/test_split_operator.py:3(quantumlab.core.grid), tests/test_stationary.py:3(quantumlab.core.grid), tests/test_stationary.py:73(quantumlab.core.grid), tests/test_strongfield.py:3(quantumlab.core.grid), tests/test_volume_3d.py:76(quantumlab.core.grid)

## Grid2D.__init__  [quantumlab/core/grid.py:21] (method)
SIG: def __init__(self, N_x: int, x_min: float, x_max: float, N_y: int, y_min: float, y_max: float):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Grid2D.shape  [quantumlab/core/grid.py:42] (method)
SIG: def shape(self):
EXT_CALLS (0):
EXT_OTHER (46):
  benchmarks/validation_suite.py:93: roundoff = fft_pairs * np.finfo(float).eps * np.log2(np.prod(grid.shape))
  examples/07_3d_double_slit.py:56: print(f'Grid {grid.N_x}×{grid.N_y}×{grid.N_z} = {np.prod(grid.shape):,} points, dt = {dt}')
  examples/08_3d_bec_time_of_flight.py:78: print(f'Grid {grid.N_x}×{grid.N_y}×{grid.N_z} = {np.prod(grid.shape):,} points, '
  examples/13_two_component_bec.py:116: noise = 1e-4 * (rng.standard_normal(grid.shape) + 1j * rng.standard_normal(grid.shape))
  quantumlab/core/wavefunction.py:11: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:12: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/core/wavefunction.py:46: self.psi = np.zeros(grid.shape, dtype=complex)
  quantumlab/core/wavefunction.py:48: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:49: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/core/wavefunction.py:85: self.psi = np.zeros(grid.shape, dtype=complex)
  quantumlab/core/wavefunction.py:87: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:88: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/potentials/apertures.py:68: opening = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:56: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:62: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:84: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:91: V = np.zeros(grid.shape)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/traps.py:32: V = np.zeros(grid.shape)
  quantumlab/solvers/multicomponent.py:44: if g.shape != (self.n_components, self.n_components):
  quantumlab/solvers/multicomponent.py:70: self._V = [self._be.to_device(np.zeros(grid.shape) if p is None else
  quantumlab/solvers/split_operator.py:142: self._V_static = (np.zeros(grid.shape) if potential is None
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:44: shape = grid.shape
  quantumlab/stationary/eigensolver.py:45: axes = tuple(range(len(shape)))
  quantumlab/stationary/eigensolver.py:46: size = int(np.prod(shape))
  quantumlab/stationary/eigensolver.py:52: return v.reshape(shape + (-1,)), v.ndim == 1
  quantumlab/stationary/eigensolver.py:102: psi = vecs[:, j].reshape(shape) / np.sqrt(dV)
  quantumlab/stationary/eigensolver.py:105: idx = np.unravel_index(np.argmax(np.abs(psi)), shape)
  quantumlab/stationary/imaginary_time.py:160: guess = envelope * rng.standard_normal(grid.shape)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  tests/test_2d_solver.py:50: assert abl.mask.shape == (128, 128)
  tests/test_3d_observables.py:76: assert prob_k.shape == grid.shape
  tests/test_3d_solver.py:36: assert grid.shape == (32, 32, 32)
  tests/test_3d_solver.py:37: assert grid.X.shape == (32, 32, 32)
  tests/test_3d_solver.py:38: assert grid.K_x.shape == (32, 32, 32)
  tests/test_3d_solver.py:63: assert wf.slice_xy().shape == (32, 32)
  tests/test_3d_solver.py:64: assert wf.slice_xz().shape == (32, 32)
  tests/test_3d_solver.py:65: assert wf.slice_yz().shape == (32, 32)
  tests/test_3d_solver.py:112: assert abl.mask.shape == (32, 32, 32)
  tests/test_absorbing_boundary_validation.py:72: assert abl.mask.shape == grid.shape
  tests/test_absorbing_boundary_validation.py:112: assert abl.mask.shape == GRIDS[0].shape
  tests/test_potentials.py:19: assert V.shape == (256,)
  tests/test_strongfield.py:78: i, j = np.unravel_index(np.argmax(G), G.shape)
  tests/test_volume_3d.py:29: assert extract_isosurface(np.zeros(grid.shape), 1.0, grid) is None
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Grid3D  [quantumlab/core/grid.py:45] (class)
SIG: class Grid3D(...):
EXT_CALLS (35):
  benchmarks/gpu_split_operator.py:45: grid = Grid3D(n, -10.0, 10.0, n, -10.0, 10.0, n, -10.0, 10.0)
  benchmarks/perf_comparison.py:85: grid = Grid3D(N, -L / 2, L / 2, N, -L / 2, L / 2, N, -L / 2, L / 2)
  benchmarks/validation_suite.py:83: grid = Grid3D(48, -10.0, 10.0, 48, -10.0, 10.0, 48, -10.0, 10.0)
  benchmarks/validation_suite.py:101: grid = Grid3D(64, -20.0, 20.0, 64, -20.0, 20.0, 64, -20.0, 20.0)
  benchmarks/validation_suite.py:122: grid = Grid3D(40, -8.0, 8.0, 40, -8.0, 8.0, 40, -8.0, 8.0)
  benchmarks/validation_suite.py:170: grid = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0)
  benchmarks/validation_suite.py:315: grid = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0)
  examples/06_3d_gaussian_barrier.py:32: grid = Grid3D(N, -L/2, L/2, N, -L/2, L/2, N, -L/2, L/2)
  examples/07_3d_double_slit.py:43: grid = Grid3D(128, -24.0, 24.0, 96, -16.0, 16.0, 96, -16.0, 16.0)
  examples/08_3d_bec_time_of_flight.py:70: grid = Grid3D(150, -15.0, 15.0, 176, -17.5, 17.5, 176, -17.5, 17.5)
  examples/11_rotating_bec_vortex_lattice.py:154: grid3 = Grid3D(128, -10.0, 10.0, 128, -10.0, 10.0, 64, -(Z + 3.0), Z + 3.0)
  quantumlab/runner.py:60: return Grid3D(Nx, -Lx / 2.0, Lx / 2.0, Ny, -Ly / 2.0, Ly / 2.0, Nz, -Lz / 2.0, Lz / 2.0)
  quantumlab/visualization/volume_3d.py:343: sub = Grid3D(len(grid.x[::stride]), grid.x[0], grid.x[0] + grid.L_x,
  tests/test_3d_gpu_solver.py:20: return Grid3D(32, -10.0, 10.0, 32, -10.0, 10.0, 32, -10.0, 10.0)
  tests/test_3d_gpu_solver.py:114: grid = Grid3D(32, -10.0, 10.0, 32, -10.0, 10.0, 32, -10.0, 10.0)
  tests/test_3d_observables.py:17: grid = Grid3D(64, -20.0, 20.0, 64, -20.0, 20.0, 64, -20.0, 20.0)
  tests/test_3d_solver.py:17: return Grid3D(N, -L, L, N, -L, L, N, -L, L)
  tests/test_absorbing_boundary_validation.py:19: Grid3D(8, -10.0, 10.0, 8, -10.0, 10.0, 8, -10.0, 10.0),
  tests/test_backends.py:88: '3d_imaginary_rotating': lambda: (Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:159: grid = Grid3D(32, -6.0, 6.0, 32, -6.0, 6.0, 32, -6.0, 6.0)
  tests/test_conjugate_gradient.py:17: (Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0), HarmonicTrap((1.0, 1.2, 1.4)), {}, 1.8),
  tests/test_conjugate_gradient.py:30: grid = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0)
  tests/test_gross_pitaevskii.py:61: grid, omegas, g = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0), (1.0, 1.2, 1.4), 60.0
  tests/test_gross_pitaevskii.py:73: grid = Grid3D(40, -8.0, 8.0, 40, -8.0, 8.0, 40, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:16: grid = Grid3D(16, -4.0, 4.0, 16, -4.0, 4.0, 16, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:27: grid = Grid3D(64, -8.0, 8.0, 64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:42: grid = Grid3D(32, -8.0, 8.0, 32, -8.0, 8.0, 16, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:58: grid = Grid3D(8, -1.0, 1.0, 8, -1.0, 1.0, 8, -1.0, 1.0)
  tests/test_new_potentials_and_observables.py:92: grid = Grid3D(32, -8.0, 8.0, 32, -8.0, 8.0, 32, -8.0, 8.0)
  tests/test_rotation.py:37: grid = Grid3D(48, -9.0, 9.0, 48, -9.0, 9.0, 32, -6.0, 6.0)
  tests/test_split_operator.py:36: grid = Grid3D(24, -8.0, 8.0, 24, -8.0, 8.0, 24, -8.0, 8.0)
  tests/test_stationary.py:30: grid = Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0)
  tests/test_stationary.py:47: grid = Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0)
  tests/test_volume_3d.py:17: return Grid3D(24, -4.0, 4.0, 24, -4.0, 4.0, 24, -4.0, 4.0)
EXT_OTHER (60):
  benchmarks/gpu_split_operator.py:45: grid = Grid3D(n, -10.0, 10.0, n, -10.0, 10.0, n, -10.0, 10.0)
  benchmarks/perf_comparison.py:85: grid = Grid3D(N, -L / 2, L / 2, N, -L / 2, L / 2, N, -L / 2, L / 2)
  benchmarks/validation_suite.py:83: grid = Grid3D(48, -10.0, 10.0, 48, -10.0, 10.0, 48, -10.0, 10.0)
  benchmarks/validation_suite.py:101: grid = Grid3D(64, -20.0, 20.0, 64, -20.0, 20.0, 64, -20.0, 20.0)
  benchmarks/validation_suite.py:122: grid = Grid3D(40, -8.0, 8.0, 40, -8.0, 8.0, 40, -8.0, 8.0)
  benchmarks/validation_suite.py:170: grid = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0)
  benchmarks/validation_suite.py:315: grid = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0)
  examples/06_3d_gaussian_barrier.py:32: grid = Grid3D(N, -L/2, L/2, N, -L/2, L/2, N, -L/2, L/2)
  examples/07_3d_double_slit.py:43: grid = Grid3D(128, -24.0, 24.0, 96, -16.0, 16.0, 96, -16.0, 16.0)
  examples/08_3d_bec_time_of_flight.py:70: grid = Grid3D(150, -15.0, 15.0, 176, -17.5, 17.5, 176, -17.5, 17.5)
  examples/11_rotating_bec_vortex_lattice.py:154: grid3 = Grid3D(128, -10.0, 10.0, 128, -10.0, 10.0, 64, -(Z + 3.0), Z + 3.0)
  quantumlab/core/absorbing_boundary.py:85: elif isinstance(self.grid, Grid3D):
  quantumlab/core/spectral.py:12: if isinstance(grid, Grid3D):
  quantumlab/core/wavefunction.py:82: def __init__(self, grid: Grid3D, psi: np.ndarray=None):
  quantumlab/core/wavefunction.py:129: def gaussian(cls, grid: Grid3D, x0: float, y0: float, z0: float,
  quantumlab/observables/current.py:28: if not isinstance(wf.grid, (Grid2D, Grid3D)):
  quantumlab/potentials/apertures.py:60: if not isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/apertures.py:70: if isinstance(grid, Grid3D) and self.aperture == 'pinhole':
  quantumlab/potentials/barriers.py:15: elif isinstance(grid, Grid3D):
  quantumlab/potentials/barriers.py:28: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:42: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:55: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:81: if isinstance(grid, (Grid2D, Grid3D)):
  quantumlab/potentials/barriers.py:127: elif isinstance(grid, Grid3D):
  quantumlab/potentials/barriers.py:158: if not isinstance(grid, Grid3D):
  quantumlab/potentials/custom.py:13: if isinstance(grid, Grid3D):
  quantumlab/potentials/oscillator.py:13: if isinstance(grid, Grid3D):
  quantumlab/runner.py:60: return Grid3D(Nx, -Lx / 2.0, Lx / 2.0, Ny, -Ly / 2.0, Ly / 2.0, Nz, -Lz / 2.0, Lz / 2.0)
  quantumlab/visualization/volume_3d.py:35: def extract_isosurface(field: np.ndarray, level: float, grid: Grid3D, step_size: int = 1):
  quantumlab/visualization/volume_3d.py:54: def _sample_phase(psi: np.ndarray, points: np.ndarray, grid: Grid3D) -> np.ndarray:
  quantumlab/visualization/volume_3d.py:87: def __init__(self, grid: Grid3D, levels: Sequence[float] = (0.5, 0.15, 0.03),
  quantumlab/visualization/volume_3d.py:93: if not isinstance(grid, Grid3D):
  quantumlab/visualization/volume_3d.py:261: def __init__(self, output_path, grid: Grid3D, n_frames: int, fps: int = 20, dpi: int = 100,
  quantumlab/visualization/volume_3d.py:305: def animate_isosurfaces(snapshots: Sequence[np.ndarray], times: Sequence[float], grid: Grid3D,
  quantumlab/visualization/volume_3d.py:330: def export_interactive_html(snapshots: Sequence[np.ndarray], times: Sequence[float], grid: Grid3D,
  quantumlab/visualization/volume_3d.py:343: sub = Grid3D(len(grid.x[::stride]), grid.x[0], grid.x[0] + grid.L_x,
  tests/test_3d_gpu_solver.py:20: return Grid3D(32, -10.0, 10.0, 32, -10.0, 10.0, 32, -10.0, 10.0)
  tests/test_3d_gpu_solver.py:114: grid = Grid3D(32, -10.0, 10.0, 32, -10.0, 10.0, 32, -10.0, 10.0)
  tests/test_3d_observables.py:17: grid = Grid3D(64, -20.0, 20.0, 64, -20.0, 20.0, 64, -20.0, 20.0)
  tests/test_3d_solver.py:16: def _make_grid(N: int = 32, L: float = 10.0) -> Grid3D:
  tests/test_3d_solver.py:17: return Grid3D(N, -L, L, N, -L, L, N, -L, L)
  tests/test_3d_solver.py:20: def _make_gaussian_wf(grid: Grid3D, x0: float = -3.0, k0_x: float = 1.5,
  tests/test_absorbing_boundary_validation.py:19: Grid3D(8, -10.0, 10.0, 8, -10.0, 10.0, 8, -10.0, 10.0),
  tests/test_backends.py:88: '3d_imaginary_rotating': lambda: (Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:159: grid = Grid3D(32, -6.0, 6.0, 32, -6.0, 6.0, 32, -6.0, 6.0)
  tests/test_conjugate_gradient.py:17: (Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0), HarmonicTrap((1.0, 1.2, 1.4)), {}, 1.8),
  tests/test_conjugate_gradient.py:30: grid = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0)
  tests/test_gross_pitaevskii.py:61: grid, omegas, g = Grid3D(48, -8.0, 8.0, 48, -8.0, 8.0, 48, -8.0, 8.0), (1.0, 1.2, 1.4), 60.0
  tests/test_gross_pitaevskii.py:73: grid = Grid3D(40, -8.0, 8.0, 40, -8.0, 8.0, 40, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:16: grid = Grid3D(16, -4.0, 4.0, 16, -4.0, 4.0, 16, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:27: grid = Grid3D(64, -8.0, 8.0, 64, -8.0, 8.0, 64, -8.0, 8.0)
  tests/test_new_potentials_and_observables.py:42: grid = Grid3D(32, -8.0, 8.0, 32, -8.0, 8.0, 16, -4.0, 4.0)
  tests/test_new_potentials_and_observables.py:58: grid = Grid3D(8, -1.0, 1.0, 8, -1.0, 1.0, 8, -1.0, 1.0)
  tests/test_new_potentials_and_observables.py:92: grid = Grid3D(32, -8.0, 8.0, 32, -8.0, 8.0, 32, -8.0, 8.0)
  tests/test_rotation.py:37: grid = Grid3D(48, -9.0, 9.0, 48, -9.0, 9.0, 32, -6.0, 6.0)
  tests/test_split_operator.py:36: grid = Grid3D(24, -8.0, 8.0, 24, -8.0, 8.0, 24, -8.0, 8.0)
  tests/test_stationary.py:30: grid = Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0)
  tests/test_stationary.py:47: grid = Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0)
  tests/test_volume_3d.py:17: return Grid3D(24, -4.0, 4.0, 24, -4.0, 4.0, 24, -4.0, 4.0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (30): benchmarks/gpu_split_operator.py:14(quantumlab.core.grid), benchmarks/perf_comparison.py:35(quantumlab.core.grid), benchmarks/validation_suite.py:14(quantumlab.core.grid), examples/06_3d_gaussian_barrier.py:3(quantumlab.core.grid), examples/07_3d_double_slit.py:20(quantumlab.core.grid), examples/08_3d_bec_time_of_flight.py:31(quantumlab.core.grid), examples/11_rotating_bec_vortex_lattice.py:42(quantumlab.core.grid), quantumlab/core/__init__.py:1(quantumlab.core.grid), quantumlab/core/absorbing_boundary.py:4(quantumlab.core.grid), quantumlab/core/spectral.py:7(quantumlab.core.grid), quantumlab/core/wavefunction.py:2(quantumlab.core.grid), quantumlab/observables/current.py:7(quantumlab.core.grid), quantumlab/potentials/apertures.py:3(quantumlab.core.grid), quantumlab/potentials/barriers.py:3(quantumlab.core.grid), quantumlab/potentials/custom.py:3(quantumlab.core.grid), quantumlab/potentials/oscillator.py:3(quantumlab.core.grid), quantumlab/runner.py:11(quantumlab.core.grid), quantumlab/visualization/volume_3d.py:18(quantumlab.core.grid), tests/test_3d_gpu_solver.py:7(quantumlab.core.grid), tests/test_3d_observables.py:3(quantumlab.core.grid), tests/test_3d_solver.py:3(quantumlab.core.grid), tests/test_absorbing_boundary_validation.py:13(quantumlab.core.grid), tests/test_backends.py:14(quantumlab.core.grid), tests/test_conjugate_gradient.py:3(quantumlab.core.grid), tests/test_gross_pitaevskii.py:3(quantumlab.core.grid), tests/test_new_potentials_and_observables.py:3(quantumlab.core.grid), tests/test_rotation.py:3(quantumlab.core.grid), tests/test_split_operator.py:3(quantumlab.core.grid), tests/test_stationary.py:3(quantumlab.core.grid), tests/test_volume_3d.py:3(quantumlab.core.grid)

## Grid3D.__init__  [quantumlab/core/grid.py:47] (method)
SIG: def __init__(self, N_x: int, x_min: float, x_max: float,
                 N_y: int, y_min: float, y_max: float,
                 N_z: int, z_min: float, z_max: float):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Grid3D.shape  [quantumlab/core/grid.py:83] (method)
SIG: def shape(self):
EXT_CALLS (0):
EXT_OTHER (46):
  benchmarks/validation_suite.py:93: roundoff = fft_pairs * np.finfo(float).eps * np.log2(np.prod(grid.shape))
  examples/07_3d_double_slit.py:56: print(f'Grid {grid.N_x}×{grid.N_y}×{grid.N_z} = {np.prod(grid.shape):,} points, dt = {dt}')
  examples/08_3d_bec_time_of_flight.py:78: print(f'Grid {grid.N_x}×{grid.N_y}×{grid.N_z} = {np.prod(grid.shape):,} points, '
  examples/13_two_component_bec.py:116: noise = 1e-4 * (rng.standard_normal(grid.shape) + 1j * rng.standard_normal(grid.shape))
  quantumlab/core/wavefunction.py:11: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:12: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/core/wavefunction.py:46: self.psi = np.zeros(grid.shape, dtype=complex)
  quantumlab/core/wavefunction.py:48: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:49: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/core/wavefunction.py:85: self.psi = np.zeros(grid.shape, dtype=complex)
  quantumlab/core/wavefunction.py:87: if psi.shape != grid.shape:
  quantumlab/core/wavefunction.py:88: raise ValueError(f'psi shape {psi.shape} does not match grid shape {grid.shape}')
  quantumlab/potentials/apertures.py:68: opening = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:56: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:62: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:84: V = np.zeros(grid.shape)
  quantumlab/potentials/barriers.py:91: V = np.zeros(grid.shape)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/traps.py:32: V = np.zeros(grid.shape)
  quantumlab/solvers/multicomponent.py:44: if g.shape != (self.n_components, self.n_components):
  quantumlab/solvers/multicomponent.py:70: self._V = [self._be.to_device(np.zeros(grid.shape) if p is None else
  quantumlab/solvers/split_operator.py:142: self._V_static = (np.zeros(grid.shape) if potential is None
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:44: shape = grid.shape
  quantumlab/stationary/eigensolver.py:45: axes = tuple(range(len(shape)))
  quantumlab/stationary/eigensolver.py:46: size = int(np.prod(shape))
  quantumlab/stationary/eigensolver.py:52: return v.reshape(shape + (-1,)), v.ndim == 1
  quantumlab/stationary/eigensolver.py:102: psi = vecs[:, j].reshape(shape) / np.sqrt(dV)
  quantumlab/stationary/eigensolver.py:105: idx = np.unravel_index(np.argmax(np.abs(psi)), shape)
  quantumlab/stationary/imaginary_time.py:160: guess = envelope * rng.standard_normal(grid.shape)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  tests/test_2d_solver.py:50: assert abl.mask.shape == (128, 128)
  tests/test_3d_observables.py:76: assert prob_k.shape == grid.shape
  tests/test_3d_solver.py:36: assert grid.shape == (32, 32, 32)
  tests/test_3d_solver.py:37: assert grid.X.shape == (32, 32, 32)
  tests/test_3d_solver.py:38: assert grid.K_x.shape == (32, 32, 32)
  tests/test_3d_solver.py:63: assert wf.slice_xy().shape == (32, 32)
  tests/test_3d_solver.py:64: assert wf.slice_xz().shape == (32, 32)
  tests/test_3d_solver.py:65: assert wf.slice_yz().shape == (32, 32)
  tests/test_3d_solver.py:112: assert abl.mask.shape == (32, 32, 32)
  tests/test_absorbing_boundary_validation.py:72: assert abl.mask.shape == grid.shape
  tests/test_absorbing_boundary_validation.py:112: assert abl.mask.shape == GRIDS[0].shape
  tests/test_potentials.py:19: assert V.shape == (256,)
  tests/test_strongfield.py:78: i, j = np.unravel_index(np.argmax(G), G.shape)
  tests/test_volume_3d.py:29: assert extract_isosurface(np.zeros(grid.shape), 1.0, grid) is None
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction1D  [quantumlab/core/wavefunction.py:4] (class)
SIG: class WaveFunction1D(...):
EXT_CALLS (9):
  benchmarks/validation_suite.py:163: wf = solver.evolve(WaveFunction1D(grid, psi), 4000)
  benchmarks/validation_suite.py:252: return (WaveFunction1D(box, np.sqrt(n) * (1 + 1e-6 * np.cos(k * box.x)) + 0j),
  benchmarks/validation_suite.py:253: WaveFunction1D(box, np.sqrt(n) * (1 - 1e-6 * np.cos(k * box.x)) + 0j))
  examples/09_soliton_collision.py:30: return WaveFunction1D(grid, left + right)
  quantumlab/solvers/split_step_1d.py:27: return WaveFunction1D(self.grid, psi)
  tests/test_gross_pitaevskii.py:23: wf = WaveFunction1D(grid, _bright_soliton(grid, kappa, x0, v))
  tests/test_gross_pitaevskii.py:35: wf = WaveFunction1D(grid, _bright_soliton(grid, 1.0, 0.0, 0.0))
  tests/test_multicomponent.py:53: return (WaveFunction1D(grid, np.sqrt(n) * (1 + eps * np.cos(k * grid.x)) + 0j),
  tests/test_multicomponent.py:54: WaveFunction1D(grid, np.sqrt(n) * (1 - eps * np.cos(k * grid.x)) + 0j))
EXT_OTHER (53):
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:163: wf = solver.evolve(WaveFunction1D(grid, psi), 4000)
  benchmarks/validation_suite.py:252: return (WaveFunction1D(box, np.sqrt(n) * (1 + 1e-6 * np.cos(k * box.x)) + 0j),
  benchmarks/validation_suite.py:253: WaveFunction1D(box, np.sqrt(n) * (1 - 1e-6 * np.cos(k * box.x)) + 0j))
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/09_soliton_collision.py:30: return WaveFunction1D(grid, left + right)
  quantumlab/core/spectral.py:23: return {1: WaveFunction1D, 2: WaveFunction2D, 3: WaveFunction3D}[ndim(grid)]
  quantumlab/observables/coefficients.py:6: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/coefficients.py:20: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/expectation.py:6: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/expectation.py:17: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/expectation.py:79: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/expectation.py:108: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/expectation.py:145: if isinstance(wf, WaveFunction1D):
  quantumlab/observables/expectation.py:155: if isinstance(wf, WaveFunction1D):
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/solvers/split_step_1d.py:20: def step(self, wavefunction: WaveFunction1D) -> WaveFunction1D:
  quantumlab/solvers/split_step_1d.py:27: return WaveFunction1D(self.grid, psi)
  quantumlab/visualization/plots_1d.py:7: def plot_wavefunction_1d(wf: WaveFunction1D, potential=None, title: str='Wave Function State', save_path: str=None, show: bool=True, theme: str='light'):
  quantumlab/visualization/plots_1d.py:40: def plot_dual_space_1d(wf: WaveFunction1D, title: str='Dual Space Analysis', save_path: str=None, show: bool=True, theme: str='light'):
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_gross_pitaevskii.py:23: wf = WaveFunction1D(grid, _bright_soliton(grid, kappa, x0, v))
  tests/test_gross_pitaevskii.py:35: wf = WaveFunction1D(grid, _bright_soliton(grid, 1.0, 0.0, 0.0))
  tests/test_multicomponent.py:53: return (WaveFunction1D(grid, np.sqrt(n) * (1 + eps * np.cos(k * grid.x)) + 0j),
  tests/test_multicomponent.py:54: WaveFunction1D(grid, np.sqrt(n) * (1 - eps * np.cos(k * grid.x)) + 0j))
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_runner.py:36: 'sim_1d': WaveFunction1D,
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
INT_CALLS (1): quantumlab/core/wavefunction.py:32
INT_OTHER (1): quantumlab/core/wavefunction.py:32
IMPORTS (26): benchmarks/validation_suite.py:15(quantumlab.core.wavefunction), examples/01_gaussian_barrier.py:5(quantumlab.core.wavefunction), examples/02_harmonic_oscillator.py:5(quantumlab.core.wavefunction), examples/03_double_well.py:4(quantumlab.core.wavefunction), examples/04_multiple_barriers.py:4(quantumlab.core.wavefunction), examples/09_soliton_collision.py:20(quantumlab.core.wavefunction), quantumlab/core/__init__.py:2(quantumlab.core.wavefunction), quantumlab/core/spectral.py:8(quantumlab.core.wavefunction), quantumlab/observables/coefficients.py:2(quantumlab.core.wavefunction), quantumlab/observables/expectation.py:2(quantumlab.core.wavefunction), quantumlab/observables/momentum.py:2(quantumlab.core.wavefunction), quantumlab/runner.py:12(quantumlab.core.wavefunction), quantumlab/solvers/split_step_1d.py:4(quantumlab.core.wavefunction), quantumlab/visualization/plots_1d.py:3(quantumlab.core.wavefunction), testbench_interlock.py:35(quantumlab.core.wavefunction), tests/test_2d_solver.py:4(quantumlab.core.wavefunction), tests/test_absorbing_boundary_validation.py:98(quantumlab.core.wavefunction), tests/test_backends.py:15(quantumlab.core.wavefunction), tests/test_gross_pitaevskii.py:4(quantumlab.core.wavefunction), tests/test_multicomponent.py:4(quantumlab.core.wavefunction), tests/test_new_potentials_and_observables.py:4(quantumlab.core.wavefunction), tests/test_observables.py:4(quantumlab.core.wavefunction), tests/test_runner.py:5(quantumlab.core.wavefunction), tests/test_solvers.py:4(quantumlab.core.wavefunction), tests/test_split_operator.py:4(quantumlab.core.wavefunction), tests/test_strongfield.py:4(quantumlab.core.wavefunction)

## WaveFunction1D.__init__  [quantumlab/core/wavefunction.py:6] (method)
SIG: def __init__(self, grid: Grid1D, psi: np.ndarray=None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction1D.probability_density  [quantumlab/core/wavefunction.py:16] (method)
SIG: def probability_density(self) -> np.ndarray:
EXT_CALLS (0):
EXT_OTHER (69):
  benchmarks/validation_suite.py:48: 'max |ρ − ρ_exact|', float(np.max(np.abs(wf.probability_density - exact))), 1e-9)
  benchmarks/validation_suite.py:166: 'max |ρ − ρ_exact|', float(np.max(np.abs(wf.probability_density - exact))), 1e-8)
  benchmarks/validation_suite.py:256: return float(np.sum((states[0].probability_density - states[1].probability_density)
  benchmarks/validation_suite.py:292: 'max |n₁ + n₂ − n|', float(np.max(np.abs(s1.probability_density + s2.probability_density
  benchmarks/validation_suite.py:293: - single.probability_density))), 1e-6)
  benchmarks/validation_suite.py:304: nn = [s.probability_density for s in states]
  examples/01_gaussian_barrier.py:35: space_time[0, :] = wf.probability_density
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:33: space_time[0, :] = wf.probability_density
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:34: space_time[0, :] = wf.probability_density
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:36: space_time[0, :] = wf.probability_density
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/06_3d_gaussian_barrier.py:53: prob = wf_current.probability_density
  examples/07_3d_double_slit.py:66: peak0 = float(wf.probability_density.max())
  examples/07_3d_double_slit.py:86: T = np.sum(wf.probability_density[grid.X > x_cut]) * grid.dx * grid.dy * grid.dz
  examples/07_3d_double_slit.py:92: T = np.sum(wf.probability_density[grid.X > x_cut]) * grid.dx * grid.dy * grid.dz
  examples/08_3d_bec_time_of_flight.py:120: rho = wf.probability_density
  examples/09_soliton_collision.py:35: rows, times = [wf.probability_density], [0.0]
  examples/09_soliton_collision.py:38: rows.append(wf.probability_density)
  examples/09_soliton_collision.py:58: rho = wf.probability_density
  examples/10_quantum_chaos_stadium.py:63: ax.imshow(states[n].probability_density.T, origin='lower', cmap='magma',
  examples/11_rotating_bec_vortex_lattice.py:81: vmax = float(wf.probability_density.max())
  examples/11_rotating_bec_vortex_lattice.py:82: im_d = ax_d.imshow(wf.probability_density.T, origin='lower', extent=extent, cmap='inferno', vmin=0, vmax=vmax)
  examples/11_rotating_bec_vortex_lattice.py:105: im_d.set_data(wf.probability_density.T)
  examples/11_rotating_bec_vortex_lattice.py:122: ax.imshow(wf.probability_density.T, origin='lower', extent=extent, cmap='inferno')
  examples/11_rotating_bec_vortex_lattice.py:151: mu_peak = g2 * float(gaussian_filter(wf.probability_density, 1.0 / grid.dx).max())
  examples/11_rotating_bec_vortex_lattice.py:202: rho = wf3.probability_density
  examples/12_high_harmonic_generation.py:70: dens.append(wf.probability_density[::2].astype(np.float32))
  examples/13_two_component_bec.py:93: ax.imshow(two_colour(s1.probability_density, s2.probability_density), origin='lower', extent=extent)
  examples/13_two_component_bec.py:131: im = ax.imshow(two_colour(wf1.probability_density, wf2.probability_density, vmax=2 * n), origin='lower',
  examples/13_two_component_bec.py:143: s = state[0].probability_density - state[1].probability_density
  examples/13_two_component_bec.py:152: im.set_data(two_colour(state[0].probability_density, state[1].probability_density, vmax=2 * n))
  examples/13_two_component_bec.py:205: vmax = max(s1.probability_density.max(), s2.probability_density.max())
  examples/13_two_component_bec.py:206: im = ax.imshow(two_colour(s1.probability_density, s2.probability_density, vmax), origin='lower', extent=extent)
  examples/13_two_component_bec.py:218: im.set_data(two_colour(state[0].probability_density, state[1].probability_density, vmax))
  examples/13_two_component_bec.py:231: n1, n2 = s1.probability_density, s2.probability_density
  quantumlab/observables/coefficients.py:5: prob = wf.probability_density
  quantumlab/observables/coefficients.py:19: prob = wf.probability_density
  quantumlab/observables/current.py:74: rho = gaussian_filter(wf.probability_density, sigma=(smoothing / g.dx, smoothing / g.dy), mode='constant')
  quantumlab/observables/expectation.py:5: prob = wf.probability_density
  quantumlab/observables/expectation.py:16: prob = wf.probability_density
  quantumlab/observables/expectation.py:33: prob = wf.probability_density
  quantumlab/observables/expectation.py:42: prob = wf.probability_density
  quantumlab/observables/expectation.py:58: prob = wf.probability_density
  quantumlab/observables/expectation.py:65: prob = wf.probability_density
  quantumlab/observables/expectation.py:144: prob = wf.probability_density
  quantumlab/observables/nonlinear.py:8: return float(0.5 * nonlinearity * np.sum(wf.probability_density ** 2) * volume_element(wf.grid))
  quantumlab/observables/nonlinear.py:32: n = [s.probability_density for s in states]
  quantumlab/observables/nonlinear.py:43: na, nb = wf_a.probability_density, wf_b.probability_density
  quantumlab/strongfield.py:132: return float(-np.sum(dV * wf.probability_density) * volume_element(grid) + force)
  quantumlab/visualization/animation.py:42: self.global_max = max(wf.probability_density.max() for wf in self.wf_series)
  quantumlab/visualization/animation.py:45: min(wf.probability_density[wf.probability_density > 0].min()
  quantumlab/visualization/animation.py:51: density = self.wf_series[0].probability_density.T
  quantumlab/visualization/animation.py:78: density = self.wf_series[frame].probability_density.T
  quantumlab/visualization/plots_1d.py:11: prob = wf.probability_density
  quantumlab/visualization/plots_1d.py:44: prob_x = wf.probability_density
  quantumlab/visualization/plots_2d.py:41: density = wf.probability_density.T   # transpose so x→col, y→row for imshow
  quantumlab/visualization/plots_2d.py:99: global_max = max(wf.probability_density.max() for wf in wf_list)
  quantumlab/visualization/plots_2d.py:108: density = wf.probability_density.T
  quantumlab/visualization/plots_2d.py:162: prob = wf3d.probability_density
  tests/test_gross_pitaevskii.py:29: assert np.max(np.abs(wf.probability_density - exact)) < tol
  tests/test_gross_pitaevskii.py:37: assert wf.probability_density.max() < 0.5
  tests/test_multicomponent.py:41: np.testing.assert_allclose(s1.probability_density + s2.probability_density, single.probability_density,
  tests/test_multicomponent.py:58: s = states[0].probability_density - states[1].probability_density
  tests/test_multicomponent.py:116: n = [s.probability_density for s in states]
  tests/test_new_potentials_and_observables.py:88: np.testing.assert_allclose(j, 2.0 * wf.probability_density, atol=1e-12)
  tests/test_split_operator.py:121: np.testing.assert_allclose(wf.probability_density, exact, atol=1e-10)
INT_CALLS (0): 
INT_OTHER (6): quantumlab/core/wavefunction.py:20, quantumlab/core/wavefunction.py:57, quantumlab/core/wavefunction.py:96, quantumlab/core/wavefunction.py:114, quantumlab/core/wavefunction.py:120, quantumlab/core/wavefunction.py:126
IMPORTS (0): 

## WaveFunction1D.norm  [quantumlab/core/wavefunction.py:19] (method)
SIG: def norm(self) -> float:
EXT_CALLS (57):
  benchmarks/perf_comparison.py:134: rel_diff = float(np.linalg.norm(wf_cpu.psi - wf_gpu.psi) /
  benchmarks/perf_comparison.py:135: (np.linalg.norm(wf_cpu.psi) + 1e-30))
  benchmarks/validation_suite.py:95: '|‖ψ‖ − 1|', abs(wf.norm() - 1.0), roundoff)
  examples/01_gaussian_barrier.py:42: norm = wf_current.norm()
  examples/04_multiple_barriers.py:43: norm = wf_current.norm()
  examples/05_2d_gaussian_barrier.py:62: norm  = wf_current.norm()
  examples/06_3d_gaussian_barrier.py:52: norm = wf_current.norm()
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:119: print(f'  norm after flight = {wf.norm():.12f}')
  examples/09_soliton_collision.py:61: print(f'    norm   {wf0.norm():.10f} → {wf.norm():.10f}')
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/13_two_component_bec.py:119: norms0 = (wf1.norm(), wf2.norm())
  examples/13_two_component_bec.py:165: print(f'    populations conserved: relative drift {abs(state[0].norm() / norms0[0] - 1):.1e}, '
  examples/13_two_component_bec.py:166: f'{abs(state[1].norm() / norms0[1] - 1):.1e}')
  quantumlab/stationary/eigensolver.py:88: residuals = np.linalg.norm(H.matmat(vecs) - vecs * energies, axis=0) / np.linalg.norm(vecs, axis=0)
  quantumlab/visualization/volume_3d.py:50: normals /= np.linalg.norm(normals, axis=1, keepdims=True) + 1e-30
  quantumlab/visualization/volume_3d.py:106: self.light = np.asarray(light_direction, dtype=float) / np.linalg.norm(light_direction)
  testbench_interlock.py:102: norm0 = wf.norm()
  testbench_interlock.py:108: norm1 = wf.norm()
  tests/test_2d_solver.py:17: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:21: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:60: initial_norm = wf.norm()
  tests/test_2d_solver.py:62: final_norm = wf.norm()
  tests/test_3d_gpu_solver.py:49: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:129: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:145: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_observables.py:67: assert T + R == pytest.approx(wf.norm(), abs=1e-12)
  tests/test_3d_observables.py:80: assert norm_k == pytest.approx(wf.norm(), abs=1e-10)
  tests/test_3d_solver.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:79: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:83: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:143: norm_before = wf.norm()
  tests/test_3d_solver.py:145: assert wf.norm() < norm_before
  tests/test_absorbing_boundary_validation.py:101: before = wf.norm()
  tests/test_absorbing_boundary_validation.py:103: assert wf.norm() < before
  tests/test_backends.py:117: wf0, 40, callback=lambda n, t, wf: seen.append(wf.norm()), callback_interval=10)
  tests/test_conjugate_gradient.py:24: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_conjugate_gradient.py:45: assert wf.norm() == pytest.approx(np.sum(np.abs(guess) ** 2) * grid.dx, rel=1e-12)
  tests/test_gross_pitaevskii.py:30: assert wf.norm() == pytest.approx(2.0 * kappa, abs=1e-10)
  tests/test_gross_pitaevskii.py:50: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_multicomponent.py:44: assert (s1.norm(), s2.norm()) == (pytest.approx(0.3, abs=1e-12), pytest.approx(0.7, abs=1e-12))
  tests/test_multicomponent.py:103: assert out[0].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_multicomponent.py:104: assert out[1].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_rotation.py:33: assert wf.norm() == pytest.approx(1.0, abs=1e-11)
  tests/test_rotation.py:86: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_rotation.py:95: assert wf.norm() == pytest.approx(3.0, abs=1e-10)
  tests/test_runner.py:60: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:72: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:81: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_solvers.py:14: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_solvers.py:18: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:129: assert free.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:131: assert absorbed.norm() < 0.01
  tests/test_stationary.py:51: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_volume_3d.py:23: radii = np.linalg.norm(verts, axis=1)
  tests/test_volume_3d.py:25: np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1.0, atol=1e-6)
EXT_OTHER (78):
  benchmarks/perf_comparison.py:134: rel_diff = float(np.linalg.norm(wf_cpu.psi - wf_gpu.psi) /
  benchmarks/perf_comparison.py:135: (np.linalg.norm(wf_cpu.psi) + 1e-30))
  benchmarks/validation_suite.py:95: '|‖ψ‖ − 1|', abs(wf.norm() - 1.0), roundoff)
  examples/01_gaussian_barrier.py:42: norm = wf_current.norm()
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/04_multiple_barriers.py:43: norm = wf_current.norm()
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:62: norm  = wf_current.norm()
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:52: norm = wf_current.norm()
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:119: print(f'  norm after flight = {wf.norm():.12f}')
  examples/09_soliton_collision.py:61: print(f'    norm   {wf0.norm():.10f} → {wf.norm():.10f}')
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/13_two_component_bec.py:61: wf.psi *= np.sqrt(norm)
  examples/13_two_component_bec.py:119: norms0 = (wf1.norm(), wf2.norm())
  examples/13_two_component_bec.py:165: print(f'    populations conserved: relative drift {abs(state[0].norm() / norms0[0] - 1):.1e}, '
  examples/13_two_component_bec.py:166: f'{abs(state[1].norm() / norms0[1] - 1):.1e}')
  quantumlab/solvers/multicomponent.py:117: norm = self._norm(p)
  quantumlab/solvers/multicomponent.py:118: out.append(p * np.sqrt(target / norm) if norm > 0 else p)
  quantumlab/solvers/split_operator.py:256: norm = self._norm(psi)
  quantumlab/solvers/split_operator.py:257: if norm > 0:
  quantumlab/solvers/split_operator.py:258: psi *= np.sqrt(self._target_norm / norm)
  quantumlab/solvers/split_step_3d_gpu.py:102: norm = np.sqrt(np.sum(np.abs(psi)**2) * self.grid.dx * self.grid.dy * self.grid.dz)
  quantumlab/solvers/split_step_3d_gpu.py:103: if norm > 0:
  quantumlab/solvers/split_step_3d_gpu.py:104: psi /= norm
  quantumlab/solvers/split_step_3d_gpu.py:134: norm = cp.sqrt(cp.sum(cp.abs(psi_gpu)**2) * self.grid.dx * self.grid.dy * self.grid.dz)
  quantumlab/solvers/split_step_3d_gpu.py:135: if norm > 0:
  quantumlab/solvers/split_step_3d_gpu.py:136: psi_gpu /= norm
  quantumlab/stationary/eigensolver.py:88: residuals = np.linalg.norm(H.matmat(vecs) - vecs * energies, axis=0) / np.linalg.norm(vecs, axis=0)
  quantumlab/visualization/animation.py:49: norm = LogNorm(vmin=self.global_min, vmax=self.global_max) if self.log_scale else None
  quantumlab/visualization/animation.py:57: interpolation='bilinear', norm=norm,
  quantumlab/visualization/plots_2d.py:44: norm = LogNorm(vmin=max(density.max() * 1e-6, density[density > 0].min()),
  quantumlab/visualization/plots_2d.py:48: cmap=cmap, interpolation='bilinear', norm=norm)
  quantumlab/visualization/volume_3d.py:50: normals /= np.linalg.norm(normals, axis=1, keepdims=True) + 1e-30
  quantumlab/visualization/volume_3d.py:106: self.light = np.asarray(light_direction, dtype=float) / np.linalg.norm(light_direction)
  testbench_interlock.py:102: norm0 = wf.norm()
  testbench_interlock.py:108: norm1 = wf.norm()
  tests/test_2d_solver.py:17: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:21: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:60: initial_norm = wf.norm()
  tests/test_2d_solver.py:62: final_norm = wf.norm()
  tests/test_3d_gpu_solver.py:49: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:129: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:145: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_observables.py:67: assert T + R == pytest.approx(wf.norm(), abs=1e-12)
  tests/test_3d_observables.py:80: assert norm_k == pytest.approx(wf.norm(), abs=1e-10)
  tests/test_3d_solver.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:79: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:83: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:143: norm_before = wf.norm()
  tests/test_3d_solver.py:145: assert wf.norm() < norm_before
  tests/test_absorbing_boundary_validation.py:101: before = wf.norm()
  tests/test_absorbing_boundary_validation.py:103: assert wf.norm() < before
  tests/test_backends.py:117: wf0, 40, callback=lambda n, t, wf: seen.append(wf.norm()), callback_interval=10)
  tests/test_conjugate_gradient.py:24: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_conjugate_gradient.py:45: assert wf.norm() == pytest.approx(np.sum(np.abs(guess) ** 2) * grid.dx, rel=1e-12)
  tests/test_gross_pitaevskii.py:30: assert wf.norm() == pytest.approx(2.0 * kappa, abs=1e-10)
  tests/test_gross_pitaevskii.py:50: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_multicomponent.py:16: wf.psi *= np.sqrt(norm)
  tests/test_multicomponent.py:44: assert (s1.norm(), s2.norm()) == (pytest.approx(0.3, abs=1e-12), pytest.approx(0.7, abs=1e-12))
  tests/test_multicomponent.py:103: assert out[0].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_multicomponent.py:104: assert out[1].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_rotation.py:33: assert wf.norm() == pytest.approx(1.0, abs=1e-11)
  tests/test_rotation.py:86: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_rotation.py:95: assert wf.norm() == pytest.approx(3.0, abs=1e-10)
  tests/test_runner.py:60: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:72: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:81: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_solvers.py:14: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_solvers.py:18: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:129: assert free.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:131: assert absorbed.norm() < 0.01
  tests/test_stationary.py:51: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_volume_3d.py:23: radii = np.linalg.norm(verts, axis=1)
  tests/test_volume_3d.py:25: np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1.0, atol=1e-6)
INT_CALLS (3): quantumlab/core/wavefunction.py:23, quantumlab/core/wavefunction.py:60, quantumlab/core/wavefunction.py:99
INT_OTHER (3): quantumlab/core/wavefunction.py:23, quantumlab/core/wavefunction.py:60, quantumlab/core/wavefunction.py:99
IMPORTS (0): 

## WaveFunction1D.normalize  [quantumlab/core/wavefunction.py:22] (method)
SIG: def normalize(self) -> 'WaveFunction1D':
EXT_CALLS (5):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:158: wf3.normalize()
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
EXT_OTHER (5):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:158: wf3.normalize()
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
INT_CALLS (3): quantumlab/core/wavefunction.py:38, quantumlab/core/wavefunction.py:77, quantumlab/core/wavefunction.py:137
INT_OTHER (3): quantumlab/core/wavefunction.py:38, quantumlab/core/wavefunction.py:77, quantumlab/core/wavefunction.py:137
IMPORTS (0): 

## WaveFunction1D.fourier_transform  [quantumlab/core/wavefunction.py:28] (method)
SIG: def fourier_transform(self) -> np.ndarray:
EXT_CALLS (3):
  quantumlab/observables/expectation.py:77: phi = wf.fourier_transform()
  quantumlab/observables/expectation.py:106: phi = wf.fourier_transform()
  quantumlab/observables/momentum.py:5: phi = wf.fourier_transform()
EXT_OTHER (3):
  quantumlab/observables/expectation.py:77: phi = wf.fourier_transform()
  quantumlab/observables/expectation.py:106: phi = wf.fourier_transform()
  quantumlab/observables/momentum.py:5: phi = wf.fourier_transform()
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction1D.copy  [quantumlab/core/wavefunction.py:31] (method)
SIG: def copy(self) -> 'WaveFunction1D':
EXT_CALLS (16):
  benchmarks/perf_comparison.py:101: wf_cpu = wf.copy()
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/08_3d_bec_time_of_flight.py:116: snapshots_html.append(wf.psi.copy())
  examples/11_rotating_bec_vortex_lattice.py:184: current, alive, k = pos3.copy(), np.ones(len(pos3), dtype=bool), k0
  quantumlab/config.py:9: config[k] = v.copy()
  quantumlab/runner.py:156: snapshots.append(wf.copy())
  quantumlab/runner.py:166: snapshots.append(wf_current.copy())
  quantumlab/solvers/split_step_1d.py:21: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_2d.py:32: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d.py:56: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d_gpu.py:95: psi = wavefunction.psi.copy()
  tests/test_3d_gpu_solver.py:82: wf_gpu = gaussian_wf.copy()
  tests/test_3d_gpu_solver.py:83: wf_cpu = gaussian_wf.copy()
EXT_OTHER (16):
  benchmarks/perf_comparison.py:101: wf_cpu = wf.copy()
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/08_3d_bec_time_of_flight.py:116: snapshots_html.append(wf.psi.copy())
  examples/11_rotating_bec_vortex_lattice.py:184: current, alive, k = pos3.copy(), np.ones(len(pos3), dtype=bool), k0
  quantumlab/config.py:9: config[k] = v.copy()
  quantumlab/runner.py:156: snapshots.append(wf.copy())
  quantumlab/runner.py:166: snapshots.append(wf_current.copy())
  quantumlab/solvers/split_step_1d.py:21: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_2d.py:32: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d.py:56: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d_gpu.py:95: psi = wavefunction.psi.copy()
  tests/test_3d_gpu_solver.py:82: wf_gpu = gaussian_wf.copy()
  tests/test_3d_gpu_solver.py:83: wf_cpu = gaussian_wf.copy()
INT_CALLS (3): quantumlab/core/wavefunction.py:32, quantumlab/core/wavefunction.py:69, quantumlab/core/wavefunction.py:108
INT_OTHER (3): quantumlab/core/wavefunction.py:32, quantumlab/core/wavefunction.py:69, quantumlab/core/wavefunction.py:108
IMPORTS (0): 

## WaveFunction1D.gaussian  [quantumlab/core/wavefunction.py:35] (method)
SIG: def gaussian(cls, grid: Grid1D, x0: float, k0: float, sigma: float) -> 'WaveFunction1D':
EXT_CALLS (69):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
EXT_OTHER (69):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction2D  [quantumlab/core/wavefunction.py:41] (class)
SIG: class WaveFunction2D(...):
EXT_CALLS (12):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:174: mid = WaveFunction2D(Grid2D(grid3.N_x, -10.0, 10.0, grid3.N_y, -10.0, 10.0), wf3.psi[:, :, k0])
  examples/11_rotating_bec_vortex_lattice.py:187: p, _ = vortex_positions(WaveFunction2D(mid.grid, wf3.psi[:, :, k]))
  examples/13_two_component_bec.py:117: wf1 = WaveFunction2D(grid, np.sqrt(n) * (1 + noise))
  examples/13_two_component_bec.py:118: wf2 = WaveFunction2D(grid, np.sqrt(n) * (1 - noise))
  quantumlab/solvers/split_step_2d.py:41: return WaveFunction2D(self.grid, psi)
  tests/test_conjugate_gradient.py:53: seed = WaveFunction2D(grid, no_vortex.psi * np.exp(1j * np.arctan2(grid.Y - 0.3, grid.X - 0.2)))
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_new_potentials_and_observables.py:135: pos, charge = vortex_positions(WaveFunction2D(grid, psi))
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:105: lattice = solver.evolve(WaveFunction2D(grid, seed), 3000)
EXT_OTHER (47):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/11_rotating_bec_vortex_lattice.py:174: mid = WaveFunction2D(Grid2D(grid3.N_x, -10.0, 10.0, grid3.N_y, -10.0, 10.0), wf3.psi[:, :, k0])
  examples/11_rotating_bec_vortex_lattice.py:187: p, _ = vortex_positions(WaveFunction2D(mid.grid, wf3.psi[:, :, k]))
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  examples/13_two_component_bec.py:117: wf1 = WaveFunction2D(grid, np.sqrt(n) * (1 + noise))
  examples/13_two_component_bec.py:118: wf2 = WaveFunction2D(grid, np.sqrt(n) * (1 - noise))
  quantumlab/core/spectral.py:23: return {1: WaveFunction1D, 2: WaveFunction2D, 3: WaveFunction3D}[ndim(grid)]
  quantumlab/observables/coefficients.py:9: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/coefficients.py:23: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:8: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:19: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:34: if isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:43: if isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:84: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:113: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:147: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/expectation.py:158: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/momentum.py:12: elif isinstance(wf, WaveFunction2D):
  quantumlab/observables/momentum.py:26: elif isinstance(wf, WaveFunction2D):
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/solvers/split_step_2d.py:30: def step(self, wavefunction: WaveFunction2D) -> WaveFunction2D:
  quantumlab/solvers/split_step_2d.py:41: return WaveFunction2D(self.grid, psi)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_conjugate_gradient.py:53: seed = WaveFunction2D(grid, no_vortex.psi * np.exp(1j * np.arctan2(grid.Y - 0.3, grid.X - 0.2)))
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_new_potentials_and_observables.py:135: pos, charge = vortex_positions(WaveFunction2D(grid, psi))
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_rotation.py:105: lattice = solver.evolve(WaveFunction2D(grid, seed), 3000)
  tests/test_runner.py:37: 'sim_2d': WaveFunction2D,
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
INT_CALLS (1): quantumlab/core/wavefunction.py:69
INT_OTHER (1): quantumlab/core/wavefunction.py:69
IMPORTS (20): benchmarks/validation_suite.py:15(quantumlab.core.wavefunction), examples/05_2d_gaussian_barrier.py:4(quantumlab.core.wavefunction), examples/11_rotating_bec_vortex_lattice.py:43(quantumlab.core.wavefunction), examples/13_two_component_bec.py:40(quantumlab.core.wavefunction), quantumlab/core/__init__.py:2(quantumlab.core.wavefunction), quantumlab/core/spectral.py:8(quantumlab.core.wavefunction), quantumlab/observables/coefficients.py:2(quantumlab.core.wavefunction), quantumlab/observables/expectation.py:2(quantumlab.core.wavefunction), quantumlab/observables/momentum.py:2(quantumlab.core.wavefunction), quantumlab/runner.py:12(quantumlab.core.wavefunction), quantumlab/solvers/split_step_2d.py:4(quantumlab.core.wavefunction), tests/test_2d_solver.py:4(quantumlab.core.wavefunction), tests/test_3d_observables.py:56(quantumlab.core.wavefunction), tests/test_backends.py:15(quantumlab.core.wavefunction), tests/test_conjugate_gradient.py:4(quantumlab.core.wavefunction), tests/test_multicomponent.py:4(quantumlab.core.wavefunction), tests/test_new_potentials_and_observables.py:4(quantumlab.core.wavefunction), tests/test_rotation.py:4(quantumlab.core.wavefunction), tests/test_runner.py:5(quantumlab.core.wavefunction), tests/test_split_operator.py:4(quantumlab.core.wavefunction)

## WaveFunction2D.__init__  [quantumlab/core/wavefunction.py:43] (method)
SIG: def __init__(self, grid: Grid2D, psi: np.ndarray=None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction2D.probability_density  [quantumlab/core/wavefunction.py:53] (method)
SIG: def probability_density(self) -> np.ndarray:
EXT_CALLS (0):
EXT_OTHER (69):
  benchmarks/validation_suite.py:48: 'max |ρ − ρ_exact|', float(np.max(np.abs(wf.probability_density - exact))), 1e-9)
  benchmarks/validation_suite.py:166: 'max |ρ − ρ_exact|', float(np.max(np.abs(wf.probability_density - exact))), 1e-8)
  benchmarks/validation_suite.py:256: return float(np.sum((states[0].probability_density - states[1].probability_density)
  benchmarks/validation_suite.py:292: 'max |n₁ + n₂ − n|', float(np.max(np.abs(s1.probability_density + s2.probability_density
  benchmarks/validation_suite.py:293: - single.probability_density))), 1e-6)
  benchmarks/validation_suite.py:304: nn = [s.probability_density for s in states]
  examples/01_gaussian_barrier.py:35: space_time[0, :] = wf.probability_density
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:33: space_time[0, :] = wf.probability_density
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:34: space_time[0, :] = wf.probability_density
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:36: space_time[0, :] = wf.probability_density
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/06_3d_gaussian_barrier.py:53: prob = wf_current.probability_density
  examples/07_3d_double_slit.py:66: peak0 = float(wf.probability_density.max())
  examples/07_3d_double_slit.py:86: T = np.sum(wf.probability_density[grid.X > x_cut]) * grid.dx * grid.dy * grid.dz
  examples/07_3d_double_slit.py:92: T = np.sum(wf.probability_density[grid.X > x_cut]) * grid.dx * grid.dy * grid.dz
  examples/08_3d_bec_time_of_flight.py:120: rho = wf.probability_density
  examples/09_soliton_collision.py:35: rows, times = [wf.probability_density], [0.0]
  examples/09_soliton_collision.py:38: rows.append(wf.probability_density)
  examples/09_soliton_collision.py:58: rho = wf.probability_density
  examples/10_quantum_chaos_stadium.py:63: ax.imshow(states[n].probability_density.T, origin='lower', cmap='magma',
  examples/11_rotating_bec_vortex_lattice.py:81: vmax = float(wf.probability_density.max())
  examples/11_rotating_bec_vortex_lattice.py:82: im_d = ax_d.imshow(wf.probability_density.T, origin='lower', extent=extent, cmap='inferno', vmin=0, vmax=vmax)
  examples/11_rotating_bec_vortex_lattice.py:105: im_d.set_data(wf.probability_density.T)
  examples/11_rotating_bec_vortex_lattice.py:122: ax.imshow(wf.probability_density.T, origin='lower', extent=extent, cmap='inferno')
  examples/11_rotating_bec_vortex_lattice.py:151: mu_peak = g2 * float(gaussian_filter(wf.probability_density, 1.0 / grid.dx).max())
  examples/11_rotating_bec_vortex_lattice.py:202: rho = wf3.probability_density
  examples/12_high_harmonic_generation.py:70: dens.append(wf.probability_density[::2].astype(np.float32))
  examples/13_two_component_bec.py:93: ax.imshow(two_colour(s1.probability_density, s2.probability_density), origin='lower', extent=extent)
  examples/13_two_component_bec.py:131: im = ax.imshow(two_colour(wf1.probability_density, wf2.probability_density, vmax=2 * n), origin='lower',
  examples/13_two_component_bec.py:143: s = state[0].probability_density - state[1].probability_density
  examples/13_two_component_bec.py:152: im.set_data(two_colour(state[0].probability_density, state[1].probability_density, vmax=2 * n))
  examples/13_two_component_bec.py:205: vmax = max(s1.probability_density.max(), s2.probability_density.max())
  examples/13_two_component_bec.py:206: im = ax.imshow(two_colour(s1.probability_density, s2.probability_density, vmax), origin='lower', extent=extent)
  examples/13_two_component_bec.py:218: im.set_data(two_colour(state[0].probability_density, state[1].probability_density, vmax))
  examples/13_two_component_bec.py:231: n1, n2 = s1.probability_density, s2.probability_density
  quantumlab/observables/coefficients.py:5: prob = wf.probability_density
  quantumlab/observables/coefficients.py:19: prob = wf.probability_density
  quantumlab/observables/current.py:74: rho = gaussian_filter(wf.probability_density, sigma=(smoothing / g.dx, smoothing / g.dy), mode='constant')
  quantumlab/observables/expectation.py:5: prob = wf.probability_density
  quantumlab/observables/expectation.py:16: prob = wf.probability_density
  quantumlab/observables/expectation.py:33: prob = wf.probability_density
  quantumlab/observables/expectation.py:42: prob = wf.probability_density
  quantumlab/observables/expectation.py:58: prob = wf.probability_density
  quantumlab/observables/expectation.py:65: prob = wf.probability_density
  quantumlab/observables/expectation.py:144: prob = wf.probability_density
  quantumlab/observables/nonlinear.py:8: return float(0.5 * nonlinearity * np.sum(wf.probability_density ** 2) * volume_element(wf.grid))
  quantumlab/observables/nonlinear.py:32: n = [s.probability_density for s in states]
  quantumlab/observables/nonlinear.py:43: na, nb = wf_a.probability_density, wf_b.probability_density
  quantumlab/strongfield.py:132: return float(-np.sum(dV * wf.probability_density) * volume_element(grid) + force)
  quantumlab/visualization/animation.py:42: self.global_max = max(wf.probability_density.max() for wf in self.wf_series)
  quantumlab/visualization/animation.py:45: min(wf.probability_density[wf.probability_density > 0].min()
  quantumlab/visualization/animation.py:51: density = self.wf_series[0].probability_density.T
  quantumlab/visualization/animation.py:78: density = self.wf_series[frame].probability_density.T
  quantumlab/visualization/plots_1d.py:11: prob = wf.probability_density
  quantumlab/visualization/plots_1d.py:44: prob_x = wf.probability_density
  quantumlab/visualization/plots_2d.py:41: density = wf.probability_density.T   # transpose so x→col, y→row for imshow
  quantumlab/visualization/plots_2d.py:99: global_max = max(wf.probability_density.max() for wf in wf_list)
  quantumlab/visualization/plots_2d.py:108: density = wf.probability_density.T
  quantumlab/visualization/plots_2d.py:162: prob = wf3d.probability_density
  tests/test_gross_pitaevskii.py:29: assert np.max(np.abs(wf.probability_density - exact)) < tol
  tests/test_gross_pitaevskii.py:37: assert wf.probability_density.max() < 0.5
  tests/test_multicomponent.py:41: np.testing.assert_allclose(s1.probability_density + s2.probability_density, single.probability_density,
  tests/test_multicomponent.py:58: s = states[0].probability_density - states[1].probability_density
  tests/test_multicomponent.py:116: n = [s.probability_density for s in states]
  tests/test_new_potentials_and_observables.py:88: np.testing.assert_allclose(j, 2.0 * wf.probability_density, atol=1e-12)
  tests/test_split_operator.py:121: np.testing.assert_allclose(wf.probability_density, exact, atol=1e-10)
INT_CALLS (0): 
INT_OTHER (6): quantumlab/core/wavefunction.py:20, quantumlab/core/wavefunction.py:57, quantumlab/core/wavefunction.py:96, quantumlab/core/wavefunction.py:114, quantumlab/core/wavefunction.py:120, quantumlab/core/wavefunction.py:126
IMPORTS (0): 

## WaveFunction2D.norm  [quantumlab/core/wavefunction.py:56] (method)
SIG: def norm(self) -> float:
EXT_CALLS (57):
  benchmarks/perf_comparison.py:134: rel_diff = float(np.linalg.norm(wf_cpu.psi - wf_gpu.psi) /
  benchmarks/perf_comparison.py:135: (np.linalg.norm(wf_cpu.psi) + 1e-30))
  benchmarks/validation_suite.py:95: '|‖ψ‖ − 1|', abs(wf.norm() - 1.0), roundoff)
  examples/01_gaussian_barrier.py:42: norm = wf_current.norm()
  examples/04_multiple_barriers.py:43: norm = wf_current.norm()
  examples/05_2d_gaussian_barrier.py:62: norm  = wf_current.norm()
  examples/06_3d_gaussian_barrier.py:52: norm = wf_current.norm()
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:119: print(f'  norm after flight = {wf.norm():.12f}')
  examples/09_soliton_collision.py:61: print(f'    norm   {wf0.norm():.10f} → {wf.norm():.10f}')
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/13_two_component_bec.py:119: norms0 = (wf1.norm(), wf2.norm())
  examples/13_two_component_bec.py:165: print(f'    populations conserved: relative drift {abs(state[0].norm() / norms0[0] - 1):.1e}, '
  examples/13_two_component_bec.py:166: f'{abs(state[1].norm() / norms0[1] - 1):.1e}')
  quantumlab/stationary/eigensolver.py:88: residuals = np.linalg.norm(H.matmat(vecs) - vecs * energies, axis=0) / np.linalg.norm(vecs, axis=0)
  quantumlab/visualization/volume_3d.py:50: normals /= np.linalg.norm(normals, axis=1, keepdims=True) + 1e-30
  quantumlab/visualization/volume_3d.py:106: self.light = np.asarray(light_direction, dtype=float) / np.linalg.norm(light_direction)
  testbench_interlock.py:102: norm0 = wf.norm()
  testbench_interlock.py:108: norm1 = wf.norm()
  tests/test_2d_solver.py:17: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:21: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:60: initial_norm = wf.norm()
  tests/test_2d_solver.py:62: final_norm = wf.norm()
  tests/test_3d_gpu_solver.py:49: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:129: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:145: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_observables.py:67: assert T + R == pytest.approx(wf.norm(), abs=1e-12)
  tests/test_3d_observables.py:80: assert norm_k == pytest.approx(wf.norm(), abs=1e-10)
  tests/test_3d_solver.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:79: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:83: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:143: norm_before = wf.norm()
  tests/test_3d_solver.py:145: assert wf.norm() < norm_before
  tests/test_absorbing_boundary_validation.py:101: before = wf.norm()
  tests/test_absorbing_boundary_validation.py:103: assert wf.norm() < before
  tests/test_backends.py:117: wf0, 40, callback=lambda n, t, wf: seen.append(wf.norm()), callback_interval=10)
  tests/test_conjugate_gradient.py:24: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_conjugate_gradient.py:45: assert wf.norm() == pytest.approx(np.sum(np.abs(guess) ** 2) * grid.dx, rel=1e-12)
  tests/test_gross_pitaevskii.py:30: assert wf.norm() == pytest.approx(2.0 * kappa, abs=1e-10)
  tests/test_gross_pitaevskii.py:50: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_multicomponent.py:44: assert (s1.norm(), s2.norm()) == (pytest.approx(0.3, abs=1e-12), pytest.approx(0.7, abs=1e-12))
  tests/test_multicomponent.py:103: assert out[0].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_multicomponent.py:104: assert out[1].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_rotation.py:33: assert wf.norm() == pytest.approx(1.0, abs=1e-11)
  tests/test_rotation.py:86: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_rotation.py:95: assert wf.norm() == pytest.approx(3.0, abs=1e-10)
  tests/test_runner.py:60: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:72: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:81: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_solvers.py:14: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_solvers.py:18: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:129: assert free.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:131: assert absorbed.norm() < 0.01
  tests/test_stationary.py:51: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_volume_3d.py:23: radii = np.linalg.norm(verts, axis=1)
  tests/test_volume_3d.py:25: np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1.0, atol=1e-6)
EXT_OTHER (78):
  benchmarks/perf_comparison.py:134: rel_diff = float(np.linalg.norm(wf_cpu.psi - wf_gpu.psi) /
  benchmarks/perf_comparison.py:135: (np.linalg.norm(wf_cpu.psi) + 1e-30))
  benchmarks/validation_suite.py:95: '|‖ψ‖ − 1|', abs(wf.norm() - 1.0), roundoff)
  examples/01_gaussian_barrier.py:42: norm = wf_current.norm()
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/04_multiple_barriers.py:43: norm = wf_current.norm()
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:62: norm  = wf_current.norm()
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:52: norm = wf_current.norm()
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:119: print(f'  norm after flight = {wf.norm():.12f}')
  examples/09_soliton_collision.py:61: print(f'    norm   {wf0.norm():.10f} → {wf.norm():.10f}')
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/13_two_component_bec.py:61: wf.psi *= np.sqrt(norm)
  examples/13_two_component_bec.py:119: norms0 = (wf1.norm(), wf2.norm())
  examples/13_two_component_bec.py:165: print(f'    populations conserved: relative drift {abs(state[0].norm() / norms0[0] - 1):.1e}, '
  examples/13_two_component_bec.py:166: f'{abs(state[1].norm() / norms0[1] - 1):.1e}')
  quantumlab/solvers/multicomponent.py:117: norm = self._norm(p)
  quantumlab/solvers/multicomponent.py:118: out.append(p * np.sqrt(target / norm) if norm > 0 else p)
  quantumlab/solvers/split_operator.py:256: norm = self._norm(psi)
  quantumlab/solvers/split_operator.py:257: if norm > 0:
  quantumlab/solvers/split_operator.py:258: psi *= np.sqrt(self._target_norm / norm)
  quantumlab/solvers/split_step_3d_gpu.py:102: norm = np.sqrt(np.sum(np.abs(psi)**2) * self.grid.dx * self.grid.dy * self.grid.dz)
  quantumlab/solvers/split_step_3d_gpu.py:103: if norm > 0:
  quantumlab/solvers/split_step_3d_gpu.py:104: psi /= norm
  quantumlab/solvers/split_step_3d_gpu.py:134: norm = cp.sqrt(cp.sum(cp.abs(psi_gpu)**2) * self.grid.dx * self.grid.dy * self.grid.dz)
  quantumlab/solvers/split_step_3d_gpu.py:135: if norm > 0:
  quantumlab/solvers/split_step_3d_gpu.py:136: psi_gpu /= norm
  quantumlab/stationary/eigensolver.py:88: residuals = np.linalg.norm(H.matmat(vecs) - vecs * energies, axis=0) / np.linalg.norm(vecs, axis=0)
  quantumlab/visualization/animation.py:49: norm = LogNorm(vmin=self.global_min, vmax=self.global_max) if self.log_scale else None
  quantumlab/visualization/animation.py:57: interpolation='bilinear', norm=norm,
  quantumlab/visualization/plots_2d.py:44: norm = LogNorm(vmin=max(density.max() * 1e-6, density[density > 0].min()),
  quantumlab/visualization/plots_2d.py:48: cmap=cmap, interpolation='bilinear', norm=norm)
  quantumlab/visualization/volume_3d.py:50: normals /= np.linalg.norm(normals, axis=1, keepdims=True) + 1e-30
  quantumlab/visualization/volume_3d.py:106: self.light = np.asarray(light_direction, dtype=float) / np.linalg.norm(light_direction)
  testbench_interlock.py:102: norm0 = wf.norm()
  testbench_interlock.py:108: norm1 = wf.norm()
  tests/test_2d_solver.py:17: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:21: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:60: initial_norm = wf.norm()
  tests/test_2d_solver.py:62: final_norm = wf.norm()
  tests/test_3d_gpu_solver.py:49: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:129: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:145: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_observables.py:67: assert T + R == pytest.approx(wf.norm(), abs=1e-12)
  tests/test_3d_observables.py:80: assert norm_k == pytest.approx(wf.norm(), abs=1e-10)
  tests/test_3d_solver.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:79: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:83: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:143: norm_before = wf.norm()
  tests/test_3d_solver.py:145: assert wf.norm() < norm_before
  tests/test_absorbing_boundary_validation.py:101: before = wf.norm()
  tests/test_absorbing_boundary_validation.py:103: assert wf.norm() < before
  tests/test_backends.py:117: wf0, 40, callback=lambda n, t, wf: seen.append(wf.norm()), callback_interval=10)
  tests/test_conjugate_gradient.py:24: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_conjugate_gradient.py:45: assert wf.norm() == pytest.approx(np.sum(np.abs(guess) ** 2) * grid.dx, rel=1e-12)
  tests/test_gross_pitaevskii.py:30: assert wf.norm() == pytest.approx(2.0 * kappa, abs=1e-10)
  tests/test_gross_pitaevskii.py:50: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_multicomponent.py:16: wf.psi *= np.sqrt(norm)
  tests/test_multicomponent.py:44: assert (s1.norm(), s2.norm()) == (pytest.approx(0.3, abs=1e-12), pytest.approx(0.7, abs=1e-12))
  tests/test_multicomponent.py:103: assert out[0].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_multicomponent.py:104: assert out[1].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_rotation.py:33: assert wf.norm() == pytest.approx(1.0, abs=1e-11)
  tests/test_rotation.py:86: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_rotation.py:95: assert wf.norm() == pytest.approx(3.0, abs=1e-10)
  tests/test_runner.py:60: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:72: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:81: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_solvers.py:14: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_solvers.py:18: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:129: assert free.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:131: assert absorbed.norm() < 0.01
  tests/test_stationary.py:51: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_volume_3d.py:23: radii = np.linalg.norm(verts, axis=1)
  tests/test_volume_3d.py:25: np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1.0, atol=1e-6)
INT_CALLS (3): quantumlab/core/wavefunction.py:23, quantumlab/core/wavefunction.py:60, quantumlab/core/wavefunction.py:99
INT_OTHER (3): quantumlab/core/wavefunction.py:23, quantumlab/core/wavefunction.py:60, quantumlab/core/wavefunction.py:99
IMPORTS (0): 

## WaveFunction2D.normalize  [quantumlab/core/wavefunction.py:59] (method)
SIG: def normalize(self) -> 'WaveFunction2D':
EXT_CALLS (5):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:158: wf3.normalize()
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
EXT_OTHER (5):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:158: wf3.normalize()
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
INT_CALLS (3): quantumlab/core/wavefunction.py:38, quantumlab/core/wavefunction.py:77, quantumlab/core/wavefunction.py:137
INT_OTHER (3): quantumlab/core/wavefunction.py:38, quantumlab/core/wavefunction.py:77, quantumlab/core/wavefunction.py:137
IMPORTS (0): 

## WaveFunction2D.fourier_transform  [quantumlab/core/wavefunction.py:65] (method)
SIG: def fourier_transform(self) -> np.ndarray:
EXT_CALLS (3):
  quantumlab/observables/expectation.py:77: phi = wf.fourier_transform()
  quantumlab/observables/expectation.py:106: phi = wf.fourier_transform()
  quantumlab/observables/momentum.py:5: phi = wf.fourier_transform()
EXT_OTHER (3):
  quantumlab/observables/expectation.py:77: phi = wf.fourier_transform()
  quantumlab/observables/expectation.py:106: phi = wf.fourier_transform()
  quantumlab/observables/momentum.py:5: phi = wf.fourier_transform()
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction2D.copy  [quantumlab/core/wavefunction.py:68] (method)
SIG: def copy(self) -> 'WaveFunction2D':
EXT_CALLS (16):
  benchmarks/perf_comparison.py:101: wf_cpu = wf.copy()
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/08_3d_bec_time_of_flight.py:116: snapshots_html.append(wf.psi.copy())
  examples/11_rotating_bec_vortex_lattice.py:184: current, alive, k = pos3.copy(), np.ones(len(pos3), dtype=bool), k0
  quantumlab/config.py:9: config[k] = v.copy()
  quantumlab/runner.py:156: snapshots.append(wf.copy())
  quantumlab/runner.py:166: snapshots.append(wf_current.copy())
  quantumlab/solvers/split_step_1d.py:21: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_2d.py:32: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d.py:56: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d_gpu.py:95: psi = wavefunction.psi.copy()
  tests/test_3d_gpu_solver.py:82: wf_gpu = gaussian_wf.copy()
  tests/test_3d_gpu_solver.py:83: wf_cpu = gaussian_wf.copy()
EXT_OTHER (16):
  benchmarks/perf_comparison.py:101: wf_cpu = wf.copy()
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/08_3d_bec_time_of_flight.py:116: snapshots_html.append(wf.psi.copy())
  examples/11_rotating_bec_vortex_lattice.py:184: current, alive, k = pos3.copy(), np.ones(len(pos3), dtype=bool), k0
  quantumlab/config.py:9: config[k] = v.copy()
  quantumlab/runner.py:156: snapshots.append(wf.copy())
  quantumlab/runner.py:166: snapshots.append(wf_current.copy())
  quantumlab/solvers/split_step_1d.py:21: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_2d.py:32: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d.py:56: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d_gpu.py:95: psi = wavefunction.psi.copy()
  tests/test_3d_gpu_solver.py:82: wf_gpu = gaussian_wf.copy()
  tests/test_3d_gpu_solver.py:83: wf_cpu = gaussian_wf.copy()
INT_CALLS (3): quantumlab/core/wavefunction.py:32, quantumlab/core/wavefunction.py:69, quantumlab/core/wavefunction.py:108
INT_OTHER (3): quantumlab/core/wavefunction.py:32, quantumlab/core/wavefunction.py:69, quantumlab/core/wavefunction.py:108
IMPORTS (0): 

## WaveFunction2D.gaussian  [quantumlab/core/wavefunction.py:72] (method)
SIG: def gaussian(cls, grid: Grid2D, x0: float, y0: float, k0_x: float, k0_y: float, sigma_x: float, sigma_y: float) -> 'WaveFunction2D':
EXT_CALLS (69):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
EXT_OTHER (69):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction3D  [quantumlab/core/wavefunction.py:80] (class)
SIG: class WaveFunction3D(...):
EXT_CALLS (5):
  examples/11_rotating_bec_vortex_lattice.py:157: wf3 = WaveFunction3D(grid3, wf.psi[:, :, None] * profile_z[None, None, :])
  quantumlab/solvers/split_step_3d.py:65: return WaveFunction3D(self.grid, psi)
  quantumlab/solvers/split_step_3d_gpu.py:93: return WaveFunction3D(self.grid, cp.asnumpy(psi_gpu))
  quantumlab/solvers/split_step_3d_gpu.py:105: return WaveFunction3D(self.grid, psi)
  quantumlab/solvers/split_step_3d_gpu.py:123: return WaveFunction3D(self.grid, cp.asnumpy(psi_gpu))
EXT_OTHER (44):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/11_rotating_bec_vortex_lattice.py:157: wf3 = WaveFunction3D(grid3, wf.psi[:, :, None] * profile_z[None, None, :])
  quantumlab/core/spectral.py:23: return {1: WaveFunction1D, 2: WaveFunction2D, 3: WaveFunction3D}[ndim(grid)]
  quantumlab/observables/coefficients.py:12: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/coefficients.py:26: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:10: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:21: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:36: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:45: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:57: if isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:64: if isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:92: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:121: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:149: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/expectation.py:162: elif isinstance(wf, WaveFunction3D):
  quantumlab/observables/momentum.py:6: if isinstance(wf, WaveFunction3D):
  quantumlab/observables/momentum.py:23: if isinstance(wf, WaveFunction3D):
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  quantumlab/solvers/split_step_3d.py:54: def step(self, wavefunction: WaveFunction3D) -> WaveFunction3D:
  quantumlab/solvers/split_step_3d.py:65: return WaveFunction3D(self.grid, psi)
  quantumlab/solvers/split_step_3d_gpu.py:87: def step(self, wavefunction: WaveFunction3D) -> WaveFunction3D:
  quantumlab/solvers/split_step_3d_gpu.py:93: return WaveFunction3D(self.grid, cp.asnumpy(psi_gpu))
  quantumlab/solvers/split_step_3d_gpu.py:105: return WaveFunction3D(self.grid, psi)
  quantumlab/solvers/split_step_3d_gpu.py:107: def step_sequence(self, initial_wf: WaveFunction3D, steps: int) -> WaveFunction3D:
  quantumlab/solvers/split_step_3d_gpu.py:123: return WaveFunction3D(self.grid, cp.asnumpy(psi_gpu))
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_solver.py:21: sigma: float = 1.0) -> WaveFunction3D:
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_runner.py:38: 'sim_3d': WaveFunction3D,
  tests/test_runner.py:39: 'sim_3d_gpu': WaveFunction3D,
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
INT_CALLS (1): quantumlab/core/wavefunction.py:108
INT_OTHER (1): quantumlab/core/wavefunction.py:108
IMPORTS (23): benchmarks/gpu_split_operator.py:15(quantumlab.core.wavefunction), benchmarks/perf_comparison.py:36(quantumlab.core.wavefunction), benchmarks/validation_suite.py:15(quantumlab.core.wavefunction), examples/06_3d_gaussian_barrier.py:4(quantumlab.core.wavefunction), examples/07_3d_double_slit.py:21(quantumlab.core.wavefunction), examples/08_3d_bec_time_of_flight.py:32(quantumlab.core.wavefunction), examples/11_rotating_bec_vortex_lattice.py:43(quantumlab.core.wavefunction), quantumlab/core/__init__.py:2(quantumlab.core.wavefunction), quantumlab/core/spectral.py:8(quantumlab.core.wavefunction), quantumlab/observables/coefficients.py:2(quantumlab.core.wavefunction), quantumlab/observables/expectation.py:2(quantumlab.core.wavefunction), quantumlab/observables/momentum.py:2(quantumlab.core.wavefunction), quantumlab/runner.py:12(quantumlab.core.wavefunction), quantumlab/solvers/split_step_3d.py:4(quantumlab.core.wavefunction), quantumlab/solvers/split_step_3d_gpu.py:12(quantumlab.core.wavefunction), tests/test_3d_gpu_solver.py:8(quantumlab.core.wavefunction), tests/test_3d_observables.py:4(quantumlab.core.wavefunction), tests/test_3d_solver.py:4(quantumlab.core.wavefunction), tests/test_backends.py:15(quantumlab.core.wavefunction), tests/test_new_potentials_and_observables.py:4(quantumlab.core.wavefunction), tests/test_rotation.py:4(quantumlab.core.wavefunction), tests/test_runner.py:5(quantumlab.core.wavefunction), tests/test_split_operator.py:4(quantumlab.core.wavefunction)

## WaveFunction3D.__init__  [quantumlab/core/wavefunction.py:82] (method)
SIG: def __init__(self, grid: Grid3D, psi: np.ndarray=None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction3D.probability_density  [quantumlab/core/wavefunction.py:92] (method)
SIG: def probability_density(self) -> np.ndarray:
EXT_CALLS (0):
EXT_OTHER (69):
  benchmarks/validation_suite.py:48: 'max |ρ − ρ_exact|', float(np.max(np.abs(wf.probability_density - exact))), 1e-9)
  benchmarks/validation_suite.py:166: 'max |ρ − ρ_exact|', float(np.max(np.abs(wf.probability_density - exact))), 1e-8)
  benchmarks/validation_suite.py:256: return float(np.sum((states[0].probability_density - states[1].probability_density)
  benchmarks/validation_suite.py:292: 'max |n₁ + n₂ − n|', float(np.max(np.abs(s1.probability_density + s2.probability_density
  benchmarks/validation_suite.py:293: - single.probability_density))), 1e-6)
  benchmarks/validation_suite.py:304: nn = [s.probability_density for s in states]
  examples/01_gaussian_barrier.py:35: space_time[0, :] = wf.probability_density
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:33: space_time[0, :] = wf.probability_density
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:34: space_time[0, :] = wf.probability_density
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:36: space_time[0, :] = wf.probability_density
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/06_3d_gaussian_barrier.py:53: prob = wf_current.probability_density
  examples/07_3d_double_slit.py:66: peak0 = float(wf.probability_density.max())
  examples/07_3d_double_slit.py:86: T = np.sum(wf.probability_density[grid.X > x_cut]) * grid.dx * grid.dy * grid.dz
  examples/07_3d_double_slit.py:92: T = np.sum(wf.probability_density[grid.X > x_cut]) * grid.dx * grid.dy * grid.dz
  examples/08_3d_bec_time_of_flight.py:120: rho = wf.probability_density
  examples/09_soliton_collision.py:35: rows, times = [wf.probability_density], [0.0]
  examples/09_soliton_collision.py:38: rows.append(wf.probability_density)
  examples/09_soliton_collision.py:58: rho = wf.probability_density
  examples/10_quantum_chaos_stadium.py:63: ax.imshow(states[n].probability_density.T, origin='lower', cmap='magma',
  examples/11_rotating_bec_vortex_lattice.py:81: vmax = float(wf.probability_density.max())
  examples/11_rotating_bec_vortex_lattice.py:82: im_d = ax_d.imshow(wf.probability_density.T, origin='lower', extent=extent, cmap='inferno', vmin=0, vmax=vmax)
  examples/11_rotating_bec_vortex_lattice.py:105: im_d.set_data(wf.probability_density.T)
  examples/11_rotating_bec_vortex_lattice.py:122: ax.imshow(wf.probability_density.T, origin='lower', extent=extent, cmap='inferno')
  examples/11_rotating_bec_vortex_lattice.py:151: mu_peak = g2 * float(gaussian_filter(wf.probability_density, 1.0 / grid.dx).max())
  examples/11_rotating_bec_vortex_lattice.py:202: rho = wf3.probability_density
  examples/12_high_harmonic_generation.py:70: dens.append(wf.probability_density[::2].astype(np.float32))
  examples/13_two_component_bec.py:93: ax.imshow(two_colour(s1.probability_density, s2.probability_density), origin='lower', extent=extent)
  examples/13_two_component_bec.py:131: im = ax.imshow(two_colour(wf1.probability_density, wf2.probability_density, vmax=2 * n), origin='lower',
  examples/13_two_component_bec.py:143: s = state[0].probability_density - state[1].probability_density
  examples/13_two_component_bec.py:152: im.set_data(two_colour(state[0].probability_density, state[1].probability_density, vmax=2 * n))
  examples/13_two_component_bec.py:205: vmax = max(s1.probability_density.max(), s2.probability_density.max())
  examples/13_two_component_bec.py:206: im = ax.imshow(two_colour(s1.probability_density, s2.probability_density, vmax), origin='lower', extent=extent)
  examples/13_two_component_bec.py:218: im.set_data(two_colour(state[0].probability_density, state[1].probability_density, vmax))
  examples/13_two_component_bec.py:231: n1, n2 = s1.probability_density, s2.probability_density
  quantumlab/observables/coefficients.py:5: prob = wf.probability_density
  quantumlab/observables/coefficients.py:19: prob = wf.probability_density
  quantumlab/observables/current.py:74: rho = gaussian_filter(wf.probability_density, sigma=(smoothing / g.dx, smoothing / g.dy), mode='constant')
  quantumlab/observables/expectation.py:5: prob = wf.probability_density
  quantumlab/observables/expectation.py:16: prob = wf.probability_density
  quantumlab/observables/expectation.py:33: prob = wf.probability_density
  quantumlab/observables/expectation.py:42: prob = wf.probability_density
  quantumlab/observables/expectation.py:58: prob = wf.probability_density
  quantumlab/observables/expectation.py:65: prob = wf.probability_density
  quantumlab/observables/expectation.py:144: prob = wf.probability_density
  quantumlab/observables/nonlinear.py:8: return float(0.5 * nonlinearity * np.sum(wf.probability_density ** 2) * volume_element(wf.grid))
  quantumlab/observables/nonlinear.py:32: n = [s.probability_density for s in states]
  quantumlab/observables/nonlinear.py:43: na, nb = wf_a.probability_density, wf_b.probability_density
  quantumlab/strongfield.py:132: return float(-np.sum(dV * wf.probability_density) * volume_element(grid) + force)
  quantumlab/visualization/animation.py:42: self.global_max = max(wf.probability_density.max() for wf in self.wf_series)
  quantumlab/visualization/animation.py:45: min(wf.probability_density[wf.probability_density > 0].min()
  quantumlab/visualization/animation.py:51: density = self.wf_series[0].probability_density.T
  quantumlab/visualization/animation.py:78: density = self.wf_series[frame].probability_density.T
  quantumlab/visualization/plots_1d.py:11: prob = wf.probability_density
  quantumlab/visualization/plots_1d.py:44: prob_x = wf.probability_density
  quantumlab/visualization/plots_2d.py:41: density = wf.probability_density.T   # transpose so x→col, y→row for imshow
  quantumlab/visualization/plots_2d.py:99: global_max = max(wf.probability_density.max() for wf in wf_list)
  quantumlab/visualization/plots_2d.py:108: density = wf.probability_density.T
  quantumlab/visualization/plots_2d.py:162: prob = wf3d.probability_density
  tests/test_gross_pitaevskii.py:29: assert np.max(np.abs(wf.probability_density - exact)) < tol
  tests/test_gross_pitaevskii.py:37: assert wf.probability_density.max() < 0.5
  tests/test_multicomponent.py:41: np.testing.assert_allclose(s1.probability_density + s2.probability_density, single.probability_density,
  tests/test_multicomponent.py:58: s = states[0].probability_density - states[1].probability_density
  tests/test_multicomponent.py:116: n = [s.probability_density for s in states]
  tests/test_new_potentials_and_observables.py:88: np.testing.assert_allclose(j, 2.0 * wf.probability_density, atol=1e-12)
  tests/test_split_operator.py:121: np.testing.assert_allclose(wf.probability_density, exact, atol=1e-10)
INT_CALLS (0): 
INT_OTHER (6): quantumlab/core/wavefunction.py:20, quantumlab/core/wavefunction.py:57, quantumlab/core/wavefunction.py:96, quantumlab/core/wavefunction.py:114, quantumlab/core/wavefunction.py:120, quantumlab/core/wavefunction.py:126
IMPORTS (0): 

## WaveFunction3D.norm  [quantumlab/core/wavefunction.py:95] (method)
SIG: def norm(self) -> float:
EXT_CALLS (57):
  benchmarks/perf_comparison.py:134: rel_diff = float(np.linalg.norm(wf_cpu.psi - wf_gpu.psi) /
  benchmarks/perf_comparison.py:135: (np.linalg.norm(wf_cpu.psi) + 1e-30))
  benchmarks/validation_suite.py:95: '|‖ψ‖ − 1|', abs(wf.norm() - 1.0), roundoff)
  examples/01_gaussian_barrier.py:42: norm = wf_current.norm()
  examples/04_multiple_barriers.py:43: norm = wf_current.norm()
  examples/05_2d_gaussian_barrier.py:62: norm  = wf_current.norm()
  examples/06_3d_gaussian_barrier.py:52: norm = wf_current.norm()
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:119: print(f'  norm after flight = {wf.norm():.12f}')
  examples/09_soliton_collision.py:61: print(f'    norm   {wf0.norm():.10f} → {wf.norm():.10f}')
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/13_two_component_bec.py:119: norms0 = (wf1.norm(), wf2.norm())
  examples/13_two_component_bec.py:165: print(f'    populations conserved: relative drift {abs(state[0].norm() / norms0[0] - 1):.1e}, '
  examples/13_two_component_bec.py:166: f'{abs(state[1].norm() / norms0[1] - 1):.1e}')
  quantumlab/stationary/eigensolver.py:88: residuals = np.linalg.norm(H.matmat(vecs) - vecs * energies, axis=0) / np.linalg.norm(vecs, axis=0)
  quantumlab/visualization/volume_3d.py:50: normals /= np.linalg.norm(normals, axis=1, keepdims=True) + 1e-30
  quantumlab/visualization/volume_3d.py:106: self.light = np.asarray(light_direction, dtype=float) / np.linalg.norm(light_direction)
  testbench_interlock.py:102: norm0 = wf.norm()
  testbench_interlock.py:108: norm1 = wf.norm()
  tests/test_2d_solver.py:17: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:21: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:60: initial_norm = wf.norm()
  tests/test_2d_solver.py:62: final_norm = wf.norm()
  tests/test_3d_gpu_solver.py:49: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:129: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:145: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_observables.py:67: assert T + R == pytest.approx(wf.norm(), abs=1e-12)
  tests/test_3d_observables.py:80: assert norm_k == pytest.approx(wf.norm(), abs=1e-10)
  tests/test_3d_solver.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:79: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:83: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:143: norm_before = wf.norm()
  tests/test_3d_solver.py:145: assert wf.norm() < norm_before
  tests/test_absorbing_boundary_validation.py:101: before = wf.norm()
  tests/test_absorbing_boundary_validation.py:103: assert wf.norm() < before
  tests/test_backends.py:117: wf0, 40, callback=lambda n, t, wf: seen.append(wf.norm()), callback_interval=10)
  tests/test_conjugate_gradient.py:24: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_conjugate_gradient.py:45: assert wf.norm() == pytest.approx(np.sum(np.abs(guess) ** 2) * grid.dx, rel=1e-12)
  tests/test_gross_pitaevskii.py:30: assert wf.norm() == pytest.approx(2.0 * kappa, abs=1e-10)
  tests/test_gross_pitaevskii.py:50: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_multicomponent.py:44: assert (s1.norm(), s2.norm()) == (pytest.approx(0.3, abs=1e-12), pytest.approx(0.7, abs=1e-12))
  tests/test_multicomponent.py:103: assert out[0].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_multicomponent.py:104: assert out[1].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_rotation.py:33: assert wf.norm() == pytest.approx(1.0, abs=1e-11)
  tests/test_rotation.py:86: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_rotation.py:95: assert wf.norm() == pytest.approx(3.0, abs=1e-10)
  tests/test_runner.py:60: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:72: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:81: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_solvers.py:14: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_solvers.py:18: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:129: assert free.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:131: assert absorbed.norm() < 0.01
  tests/test_stationary.py:51: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_volume_3d.py:23: radii = np.linalg.norm(verts, axis=1)
  tests/test_volume_3d.py:25: np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1.0, atol=1e-6)
EXT_OTHER (78):
  benchmarks/perf_comparison.py:134: rel_diff = float(np.linalg.norm(wf_cpu.psi - wf_gpu.psi) /
  benchmarks/perf_comparison.py:135: (np.linalg.norm(wf_cpu.psi) + 1e-30))
  benchmarks/validation_suite.py:95: '|‖ψ‖ − 1|', abs(wf.norm() - 1.0), roundoff)
  examples/01_gaussian_barrier.py:42: norm = wf_current.norm()
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/04_multiple_barriers.py:43: norm = wf_current.norm()
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:62: norm  = wf_current.norm()
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:52: norm = wf_current.norm()
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:119: print(f'  norm after flight = {wf.norm():.12f}')
  examples/09_soliton_collision.py:61: print(f'    norm   {wf0.norm():.10f} → {wf.norm():.10f}')
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/13_two_component_bec.py:61: wf.psi *= np.sqrt(norm)
  examples/13_two_component_bec.py:119: norms0 = (wf1.norm(), wf2.norm())
  examples/13_two_component_bec.py:165: print(f'    populations conserved: relative drift {abs(state[0].norm() / norms0[0] - 1):.1e}, '
  examples/13_two_component_bec.py:166: f'{abs(state[1].norm() / norms0[1] - 1):.1e}')
  quantumlab/solvers/multicomponent.py:117: norm = self._norm(p)
  quantumlab/solvers/multicomponent.py:118: out.append(p * np.sqrt(target / norm) if norm > 0 else p)
  quantumlab/solvers/split_operator.py:256: norm = self._norm(psi)
  quantumlab/solvers/split_operator.py:257: if norm > 0:
  quantumlab/solvers/split_operator.py:258: psi *= np.sqrt(self._target_norm / norm)
  quantumlab/solvers/split_step_3d_gpu.py:102: norm = np.sqrt(np.sum(np.abs(psi)**2) * self.grid.dx * self.grid.dy * self.grid.dz)
  quantumlab/solvers/split_step_3d_gpu.py:103: if norm > 0:
  quantumlab/solvers/split_step_3d_gpu.py:104: psi /= norm
  quantumlab/solvers/split_step_3d_gpu.py:134: norm = cp.sqrt(cp.sum(cp.abs(psi_gpu)**2) * self.grid.dx * self.grid.dy * self.grid.dz)
  quantumlab/solvers/split_step_3d_gpu.py:135: if norm > 0:
  quantumlab/solvers/split_step_3d_gpu.py:136: psi_gpu /= norm
  quantumlab/stationary/eigensolver.py:88: residuals = np.linalg.norm(H.matmat(vecs) - vecs * energies, axis=0) / np.linalg.norm(vecs, axis=0)
  quantumlab/visualization/animation.py:49: norm = LogNorm(vmin=self.global_min, vmax=self.global_max) if self.log_scale else None
  quantumlab/visualization/animation.py:57: interpolation='bilinear', norm=norm,
  quantumlab/visualization/plots_2d.py:44: norm = LogNorm(vmin=max(density.max() * 1e-6, density[density > 0].min()),
  quantumlab/visualization/plots_2d.py:48: cmap=cmap, interpolation='bilinear', norm=norm)
  quantumlab/visualization/volume_3d.py:50: normals /= np.linalg.norm(normals, axis=1, keepdims=True) + 1e-30
  quantumlab/visualization/volume_3d.py:106: self.light = np.asarray(light_direction, dtype=float) / np.linalg.norm(light_direction)
  testbench_interlock.py:102: norm0 = wf.norm()
  testbench_interlock.py:108: norm1 = wf.norm()
  tests/test_2d_solver.py:17: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:21: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_2d_solver.py:60: initial_norm = wf.norm()
  tests/test_2d_solver.py:62: final_norm = wf.norm()
  tests/test_3d_gpu_solver.py:49: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:129: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_gpu_solver.py:145: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_observables.py:67: assert T + R == pytest.approx(wf.norm(), abs=1e-12)
  tests/test_3d_observables.py:80: assert norm_k == pytest.approx(wf.norm(), abs=1e-10)
  tests/test_3d_solver.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:79: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:83: assert wf_current.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_3d_solver.py:143: norm_before = wf.norm()
  tests/test_3d_solver.py:145: assert wf.norm() < norm_before
  tests/test_absorbing_boundary_validation.py:101: before = wf.norm()
  tests/test_absorbing_boundary_validation.py:103: assert wf.norm() < before
  tests/test_backends.py:117: wf0, 40, callback=lambda n, t, wf: seen.append(wf.norm()), callback_interval=10)
  tests/test_conjugate_gradient.py:24: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_conjugate_gradient.py:45: assert wf.norm() == pytest.approx(np.sum(np.abs(guess) ** 2) * grid.dx, rel=1e-12)
  tests/test_gross_pitaevskii.py:30: assert wf.norm() == pytest.approx(2.0 * kappa, abs=1e-10)
  tests/test_gross_pitaevskii.py:50: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_multicomponent.py:16: wf.psi *= np.sqrt(norm)
  tests/test_multicomponent.py:44: assert (s1.norm(), s2.norm()) == (pytest.approx(0.3, abs=1e-12), pytest.approx(0.7, abs=1e-12))
  tests/test_multicomponent.py:103: assert out[0].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_multicomponent.py:104: assert out[1].norm() == pytest.approx(0.5, abs=1e-12)
  tests/test_rotation.py:33: assert wf.norm() == pytest.approx(1.0, abs=1e-11)
  tests/test_rotation.py:86: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_rotation.py:95: assert wf.norm() == pytest.approx(3.0, abs=1e-10)
  tests/test_runner.py:60: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:72: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_runner.py:81: assert wf.norm() == pytest.approx(1.0, abs=1e-10)
  tests/test_solvers.py:14: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_solvers.py:18: assert wf_current.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:57: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:129: assert free.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_split_operator.py:131: assert absorbed.norm() < 0.01
  tests/test_stationary.py:51: assert wf.norm() == pytest.approx(1.0, abs=1e-12)
  tests/test_volume_3d.py:23: radii = np.linalg.norm(verts, axis=1)
  tests/test_volume_3d.py:25: np.testing.assert_allclose(np.linalg.norm(normals, axis=1), 1.0, atol=1e-6)
INT_CALLS (3): quantumlab/core/wavefunction.py:23, quantumlab/core/wavefunction.py:60, quantumlab/core/wavefunction.py:99
INT_OTHER (3): quantumlab/core/wavefunction.py:23, quantumlab/core/wavefunction.py:60, quantumlab/core/wavefunction.py:99
IMPORTS (0): 

## WaveFunction3D.normalize  [quantumlab/core/wavefunction.py:98] (method)
SIG: def normalize(self) -> 'WaveFunction3D':
EXT_CALLS (5):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:158: wf3.normalize()
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
EXT_OTHER (5):
  benchmarks/validation_suite.py:112: wf = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  benchmarks/validation_suite.py:201: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  examples/11_rotating_bec_vortex_lattice.py:158: wf3.normalize()
  tests/test_new_potentials_and_observables.py:103: wf = WaveFunction2D(grid, z ** abs(ell) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
  tests/test_rotation.py:52: wf0 = WaveFunction2D(grid, (grid.X + 1j * grid.Y) * np.exp(-(grid.X ** 2 + grid.Y ** 2) / 2)).normalize()
INT_CALLS (3): quantumlab/core/wavefunction.py:38, quantumlab/core/wavefunction.py:77, quantumlab/core/wavefunction.py:137
INT_OTHER (3): quantumlab/core/wavefunction.py:38, quantumlab/core/wavefunction.py:77, quantumlab/core/wavefunction.py:137
IMPORTS (0): 

## WaveFunction3D.fourier_transform  [quantumlab/core/wavefunction.py:104] (method)
SIG: def fourier_transform(self) -> np.ndarray:
EXT_CALLS (3):
  quantumlab/observables/expectation.py:77: phi = wf.fourier_transform()
  quantumlab/observables/expectation.py:106: phi = wf.fourier_transform()
  quantumlab/observables/momentum.py:5: phi = wf.fourier_transform()
EXT_OTHER (3):
  quantumlab/observables/expectation.py:77: phi = wf.fourier_transform()
  quantumlab/observables/expectation.py:106: phi = wf.fourier_transform()
  quantumlab/observables/momentum.py:5: phi = wf.fourier_transform()
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction3D.copy  [quantumlab/core/wavefunction.py:107] (method)
SIG: def copy(self) -> 'WaveFunction3D':
EXT_CALLS (16):
  benchmarks/perf_comparison.py:101: wf_cpu = wf.copy()
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/08_3d_bec_time_of_flight.py:116: snapshots_html.append(wf.psi.copy())
  examples/11_rotating_bec_vortex_lattice.py:184: current, alive, k = pos3.copy(), np.ones(len(pos3), dtype=bool), k0
  quantumlab/config.py:9: config[k] = v.copy()
  quantumlab/runner.py:156: snapshots.append(wf.copy())
  quantumlab/runner.py:166: snapshots.append(wf_current.copy())
  quantumlab/solvers/split_step_1d.py:21: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_2d.py:32: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d.py:56: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d_gpu.py:95: psi = wavefunction.psi.copy()
  tests/test_3d_gpu_solver.py:82: wf_gpu = gaussian_wf.copy()
  tests/test_3d_gpu_solver.py:83: wf_cpu = gaussian_wf.copy()
EXT_OTHER (16):
  benchmarks/perf_comparison.py:101: wf_cpu = wf.copy()
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/08_3d_bec_time_of_flight.py:116: snapshots_html.append(wf.psi.copy())
  examples/11_rotating_bec_vortex_lattice.py:184: current, alive, k = pos3.copy(), np.ones(len(pos3), dtype=bool), k0
  quantumlab/config.py:9: config[k] = v.copy()
  quantumlab/runner.py:156: snapshots.append(wf.copy())
  quantumlab/runner.py:166: snapshots.append(wf_current.copy())
  quantumlab/solvers/split_step_1d.py:21: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_2d.py:32: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d.py:56: psi = wavefunction.psi.copy()
  quantumlab/solvers/split_step_3d_gpu.py:95: psi = wavefunction.psi.copy()
  tests/test_3d_gpu_solver.py:82: wf_gpu = gaussian_wf.copy()
  tests/test_3d_gpu_solver.py:83: wf_cpu = gaussian_wf.copy()
INT_CALLS (3): quantumlab/core/wavefunction.py:32, quantumlab/core/wavefunction.py:69, quantumlab/core/wavefunction.py:108
INT_OTHER (3): quantumlab/core/wavefunction.py:32, quantumlab/core/wavefunction.py:69, quantumlab/core/wavefunction.py:108
IMPORTS (0): 

## WaveFunction3D.slice_xy  [quantumlab/core/wavefunction.py:110] (method)
SIG: def slice_xy(self, z_idx: int=None) -> np.ndarray:
EXT_CALLS (1):
  tests/test_3d_solver.py:63: assert wf.slice_xy().shape == (32, 32)
EXT_OTHER (4):
  quantumlab/visualization/plots_2d.py:172: slice_xy = prob[:, :, cz].T
  quantumlab/visualization/plots_2d.py:176: global_max = max(slice_xy.max(), slice_xz.max(), slice_yz.max())
  quantumlab/visualization/plots_2d.py:183: (gs[0], slice_xy, grid.x, grid.y, 'x', 'y', f'XY  (z = {grid.z[cz]:.1f})'),
  tests/test_3d_solver.py:63: assert wf.slice_xy().shape == (32, 32)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction3D.slice_xz  [quantumlab/core/wavefunction.py:116] (method)
SIG: def slice_xz(self, y_idx: int=None) -> np.ndarray:
EXT_CALLS (1):
  tests/test_3d_solver.py:64: assert wf.slice_xz().shape == (32, 32)
EXT_OTHER (4):
  quantumlab/visualization/plots_2d.py:173: slice_xz = prob[:, cy, :].T
  quantumlab/visualization/plots_2d.py:176: global_max = max(slice_xy.max(), slice_xz.max(), slice_yz.max())
  quantumlab/visualization/plots_2d.py:184: (gs[1], slice_xz, grid.x, grid.z, 'x', 'z', f'XZ  (y = {grid.y[cy]:.1f})'),
  tests/test_3d_solver.py:64: assert wf.slice_xz().shape == (32, 32)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction3D.slice_yz  [quantumlab/core/wavefunction.py:122] (method)
SIG: def slice_yz(self, x_idx: int=None) -> np.ndarray:
EXT_CALLS (1):
  tests/test_3d_solver.py:65: assert wf.slice_yz().shape == (32, 32)
EXT_OTHER (4):
  quantumlab/visualization/plots_2d.py:174: slice_yz = prob[cx, :, :].T
  quantumlab/visualization/plots_2d.py:176: global_max = max(slice_xy.max(), slice_xz.max(), slice_yz.max())
  quantumlab/visualization/plots_2d.py:185: (gs[2], slice_yz, grid.y, grid.z, 'y', 'z', f'YZ  (x = {grid.x[cx]:.1f})'),
  tests/test_3d_solver.py:65: assert wf.slice_yz().shape == (32, 32)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## WaveFunction3D.gaussian  [quantumlab/core/wavefunction.py:129] (method)
SIG: def gaussian(cls, grid: Grid3D, x0: float, y0: float, z0: float,
                 k0_x: float, k0_y: float, k0_z: float,
                 sigma_x: float, sigma_y: float, sigma_z: float) -> 'WaveFunction3D':
EXT_CALLS (69):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
EXT_OTHER (69):
  benchmarks/gpu_split_operator.py:24: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.5, 1.5, 1.5)
  benchmarks/perf_comparison.py:86: wf = WaveFunction3D.gaussian(
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:54: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  benchmarks/validation_suite.py:71: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1 / np.sqrt(2))
  benchmarks/validation_suite.py:85: wf = WaveFunction3D.gaussian(grid, 1.0, -0.5, 0.0, 1.0, 0.5, -0.3, 1.0, 0.8, 1.1)
  benchmarks/validation_suite.py:102: wf = WaveFunction3D.gaussian(grid, 1.5, -2.0, 0.5, 1.2, -0.8, 0.4, 2.0, 2.5, 1.8)
  benchmarks/validation_suite.py:136: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  benchmarks/validation_suite.py:191: wf = WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  benchmarks/validation_suite.py:285: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:286: b = WaveFunction2D.gaussian(grid, -1.0, 0.5, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:297: a = WaveFunction2D.gaussian(grid, 1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  benchmarks/validation_suite.py:298: b = WaveFunction2D.gaussian(grid, -1.5, 0.0, 0.0, 0.0, 1.0, 1.0)
  examples/01_gaussian_barrier.py:30: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/02_harmonic_oscillator.py:28: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/03_double_well.py:29: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/04_multiple_barriers.py:31: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  examples/05_2d_gaussian_barrier.py:37: wf   = WaveFunction2D.gaussian(grid, x0, y0, k0_x, 0.0, sigma_x, sigma_y)
  examples/06_3d_gaussian_barrier.py:33: wf   = WaveFunction3D.gaussian(
  examples/07_3d_double_slit.py:59: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, k0, 0.0, 0.0, sigma_x, sigma_t, sigma_t)
  examples/13_two_component_bec.py:60: wf = WaveFunction2D.gaussian(grid, dx, 0.0, 0.0, 0.0, 1.8, 1.8)
  quantumlab/runner.py:70: return WaveFunction1D.gaussian(
  quantumlab/runner.py:74: return WaveFunction2D.gaussian(
  quantumlab/runner.py:84: return WaveFunction3D.gaussian(
  testbench_interlock.py:98: wf = WaveFunction1D.gaussian(grid, x0=x0, k0=k0, sigma=3.5)
  tests/test_2d_solver.py:14: wf = WaveFunction2D.gaussian(grid, x0=-5.0, y0=0.0, k0_x=2.0, k0_y=0.0, sigma_x=1.0, sigma_y=1.0)
  tests/test_2d_solver.py:26: wf = WaveFunction2D.gaussian(grid, x0=0.0, y0=0.0, k0_x=0.0, k0_y=0.0, sigma_x=1.5, sigma_y=1.5)
  tests/test_2d_solver.py:58: wf = WaveFunction1D.gaussian(grid, x0=47.0, k0=0.0, sigma=1.5)
  tests/test_3d_gpu_solver.py:25: return WaveFunction3D.gaussian(
  tests/test_3d_gpu_solver.py:115: wf = WaveFunction3D.gaussian(
  tests/test_3d_observables.py:20: wf = WaveFunction3D.gaussian(grid, **params)
  tests/test_3d_observables.py:58: wf = WaveFunction2D.gaussian(grid, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0)
  tests/test_3d_solver.py:22: return WaveFunction3D.gaussian(
  tests/test_3d_solver.py:89: wf = WaveFunction3D.gaussian(
  tests/test_3d_solver.py:137: wf = WaveFunction3D.gaussian(
  tests/test_absorbing_boundary_validation.py:100: wf = WaveFunction1D.gaussian(grid, x0=15.0, k0=0.0, sigma=1.0)
  tests/test_backends.py:77: WaveFunction1D.gaussian(Grid1D(256, -20.0, 20.0), -5.0, 2.0, 1.0)),
  tests/test_backends.py:79: WaveFunction1D.gaussian(Grid1D(128, -15.0, 15.0), 0.0, 0.0, 1.0)),
  tests/test_backends.py:82: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:86: WaveFunction2D.gaussian(Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0),
  tests/test_backends.py:91: WaveFunction3D.gaussian(Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 16, -5.0, 5.0),
  tests/test_backends.py:111: wf0 = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_backends.py:125: wf0 = WaveFunction2D.gaussian(grid, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0)
  tests/test_backends.py:160: wf0 = WaveFunction3D.gaussian(grid, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_backends.py:171: a = WaveFunction2D.gaussian(grid, 1.0, 0.0, 0.3, 0.0, 1.0, 1.0)
  tests/test_backends.py:172: b = WaveFunction2D.gaussian(grid, -1.0, 0.0, 0.0, 0.2, 1.0, 1.0)
  tests/test_multicomponent.py:15: wf = WaveFunction2D.gaussian(grid, x0, y0, kx, ky, s, s)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:86: wf = WaveFunction1D.gaussian(grid, 0.0, 2.0, 2.0)
  tests/test_new_potentials_and_observables.py:93: wf = WaveFunction3D.gaussian(grid, 0.0, 0.0, 0.0, 1.0, -0.5, 0.3, 1.2, 1.2, 1.2)
  tests/test_new_potentials_and_observables.py:111: wf0 = WaveFunction1D.gaussian(grid, 1.5, 0.0, 0.7)
  tests/test_observables.py:13: wf = WaveFunction1D.gaussian(grid, x0, k0, sigma)
  tests/test_rotation.py:15: return WaveFunction2D.gaussian(grid, x0, 0.0, 0.0, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
  tests/test_rotation.py:39: wf = WaveFunction3D.gaussian(grid, x0, 0.0, 0.0, 0.0, 0.0, 0.0, *[1 / np.sqrt(2)] * 3)
  tests/test_rotation.py:65: wf = WaveFunction2D.gaussian(grid, 1.0, -0.5, 0.3, 0.8, 0.8, 0.7)
  tests/test_solvers.py:11: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_solvers.py:22: wf = WaveFunction1D.gaussian(grid, x0=-5.0, k0=2.0, sigma=1.0)
  tests/test_split_operator.py:29: wf = WaveFunction1D.gaussian(grid, -5.0, 2.0, 1.0)
  tests/test_split_operator.py:33: wf = WaveFunction2D.gaussian(grid, -3.0, 0.0, 2.0, 0.0, 1.0, 1.0)
  tests/test_split_operator.py:37: wf = WaveFunction3D.gaussian(grid, -2.0, 0.0, 0.0, 1.5, 0.0, 0.0, 1.0, 1.0, 1.0)
  tests/test_split_operator.py:53: wf = WaveFunction1D.gaussian(grid, -8.0, 2.0, 1.5)
  tests/test_split_operator.py:68: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.5, 0.8)
  tests/test_split_operator.py:83: wf0 = WaveFunction1D.gaussian(grid, -2.0, 1.0, 0.8)
  tests/test_split_operator.py:95: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0 / np.sqrt(2.0))
  tests/test_split_operator.py:106: wf0 = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_split_operator.py:117: wf = WaveFunction1D.gaussian(grid, 0.0, k0, sigma0)
  tests/test_split_operator.py:126: wf = WaveFunction1D.gaussian(grid, 0.0, 4.0, 1.0)
  tests/test_split_operator.py:146: wf = WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0)
  tests/test_strongfield.py:99: wf = WaveFunction1D.gaussian(grid, 1.3, 0.4, 0.8)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## AbsorbingBoundaryLayer  [quantumlab/core/absorbing_boundary.py:6] (class)
SIG: class AbsorbingBoundaryLayer(...):
EXT_CALLS (25):
  benchmarks/validation_suite.py:221: solver = SplitOperatorSolver(grid, laser, 0.05, order=4, absorber=AbsorbingBoundaryLayer(grid, 40.0))
  examples/05_2d_gaussian_barrier.py:42: abl       = AbsorbingBoundaryLayer(grid, boundary_width, order=3)
  examples/06_3d_gaussian_barrier.py:43: abl       = AbsorbingBoundaryLayer(grid, boundary_width, order=3)
  examples/07_3d_double_slit.py:60: solver = SplitOperatorSolver(grid, screen, dt, order=2, absorber=AbsorbingBoundaryLayer(grid, 3.0))
  examples/12_high_harmonic_generation.py:64: solver = SplitOperatorSolver(GRID, laser, DT, order=4, absorber=AbsorbingBoundaryLayer(GRID, 40.0))
  quantumlab/runner.py:148: abl = AbsorbingBoundaryLayer(grid, float(abl_cfg["width"]), int(abl_cfg.get("order", 3)))
  tests/test_2d_solver.py:39: abl = AbsorbingBoundaryLayer(grid, boundary_width=10.0, order=3)
  tests/test_2d_solver.py:49: abl = AbsorbingBoundaryLayer(grid, boundary_width=5.0, order=3)
  tests/test_2d_solver.py:59: abl = AbsorbingBoundaryLayer(grid, boundary_width=10.0, order=3)
  tests/test_3d_solver.py:111: abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=3)
  tests/test_3d_solver.py:118: abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=3)
  tests/test_3d_solver.py:126: abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=3)
  tests/test_3d_solver.py:142: abl = AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3)
  tests/test_absorbing_boundary_validation.py:31: AbsorbingBoundaryLayer(grid, bw)
  tests/test_absorbing_boundary_validation.py:38: AbsorbingBoundaryLayer(grid, bw)
  tests/test_absorbing_boundary_validation.py:44: AbsorbingBoundaryLayer(GRIDS[0], bw)
  tests/test_absorbing_boundary_validation.py:55: AbsorbingBoundaryLayer(grid, 3.0, order=order)
  tests/test_absorbing_boundary_validation.py:61: AbsorbingBoundaryLayer(GRIDS[0], 3.0, order=order)
  tests/test_absorbing_boundary_validation.py:71: abl = AbsorbingBoundaryLayer(grid, 3.0, order=order)
  tests/test_absorbing_boundary_validation.py:80: abl = AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3)
  tests/test_absorbing_boundary_validation.py:91: abl = AbsorbingBoundaryLayer(grid, boundary_width=5.0, order=3)
  tests/test_absorbing_boundary_validation.py:102: AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3).apply(wf)
  tests/test_absorbing_boundary_validation.py:111: abl = AbsorbingBoundaryLayer(GRIDS[0], np.float64(3.0), order=np.int64(3))
  tests/test_backends.py:112: abl = AbsorbingBoundaryLayer(grid, 4.0)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
EXT_OTHER (25):
  benchmarks/validation_suite.py:221: solver = SplitOperatorSolver(grid, laser, 0.05, order=4, absorber=AbsorbingBoundaryLayer(grid, 40.0))
  examples/05_2d_gaussian_barrier.py:42: abl       = AbsorbingBoundaryLayer(grid, boundary_width, order=3)
  examples/06_3d_gaussian_barrier.py:43: abl       = AbsorbingBoundaryLayer(grid, boundary_width, order=3)
  examples/07_3d_double_slit.py:60: solver = SplitOperatorSolver(grid, screen, dt, order=2, absorber=AbsorbingBoundaryLayer(grid, 3.0))
  examples/12_high_harmonic_generation.py:64: solver = SplitOperatorSolver(GRID, laser, DT, order=4, absorber=AbsorbingBoundaryLayer(GRID, 40.0))
  quantumlab/runner.py:148: abl = AbsorbingBoundaryLayer(grid, float(abl_cfg["width"]), int(abl_cfg.get("order", 3)))
  tests/test_2d_solver.py:39: abl = AbsorbingBoundaryLayer(grid, boundary_width=10.0, order=3)
  tests/test_2d_solver.py:49: abl = AbsorbingBoundaryLayer(grid, boundary_width=5.0, order=3)
  tests/test_2d_solver.py:59: abl = AbsorbingBoundaryLayer(grid, boundary_width=10.0, order=3)
  tests/test_3d_solver.py:111: abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=3)
  tests/test_3d_solver.py:118: abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=3)
  tests/test_3d_solver.py:126: abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=3)
  tests/test_3d_solver.py:142: abl = AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3)
  tests/test_absorbing_boundary_validation.py:31: AbsorbingBoundaryLayer(grid, bw)
  tests/test_absorbing_boundary_validation.py:38: AbsorbingBoundaryLayer(grid, bw)
  tests/test_absorbing_boundary_validation.py:44: AbsorbingBoundaryLayer(GRIDS[0], bw)
  tests/test_absorbing_boundary_validation.py:55: AbsorbingBoundaryLayer(grid, 3.0, order=order)
  tests/test_absorbing_boundary_validation.py:61: AbsorbingBoundaryLayer(GRIDS[0], 3.0, order=order)
  tests/test_absorbing_boundary_validation.py:71: abl = AbsorbingBoundaryLayer(grid, 3.0, order=order)
  tests/test_absorbing_boundary_validation.py:80: abl = AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3)
  tests/test_absorbing_boundary_validation.py:91: abl = AbsorbingBoundaryLayer(grid, boundary_width=5.0, order=3)
  tests/test_absorbing_boundary_validation.py:102: AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3).apply(wf)
  tests/test_absorbing_boundary_validation.py:111: abl = AbsorbingBoundaryLayer(GRIDS[0], np.float64(3.0), order=np.int64(3))
  tests/test_backends.py:112: abl = AbsorbingBoundaryLayer(grid, 4.0)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (12): benchmarks/validation_suite.py:18(quantumlab.core.absorbing_boundary), examples/05_2d_gaussian_barrier.py:7(quantumlab.core.absorbing_boundary), examples/06_3d_gaussian_barrier.py:7(quantumlab.core.absorbing_boundary), examples/07_3d_double_slit.py:22(quantumlab.core.absorbing_boundary), examples/12_high_harmonic_generation.py:41(quantumlab.core.absorbing_boundary), quantumlab/core/__init__.py:3(quantumlab.core.absorbing_boundary), quantumlab/runner.py:13(quantumlab.core.absorbing_boundary), tests/test_2d_solver.py:8(quantumlab.core.absorbing_boundary), tests/test_3d_solver.py:8(quantumlab.core.absorbing_boundary), tests/test_absorbing_boundary_validation.py:12(quantumlab.core.absorbing_boundary), tests/test_backends.py:16(quantumlab.core.absorbing_boundary), tests/test_split_operator.py:11(quantumlab.core.absorbing_boundary)

## AbsorbingBoundaryLayer.__init__  [quantumlab/core/absorbing_boundary.py:28] (method)
SIG: def __init__(self, grid, boundary_width: float, order: int = 3):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## AbsorbingBoundaryLayer._polynomial_profile  [quantumlab/core/absorbing_boundary.py:53] (method)
SIG: def _polynomial_profile(self, d):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (12): quantumlab/core/absorbing_boundary.py:98, quantumlab/core/absorbing_boundary.py:102, quantumlab/core/absorbing_boundary.py:117, quantumlab/core/absorbing_boundary.py:118, quantumlab/core/absorbing_boundary.py:121, quantumlab/core/absorbing_boundary.py:122, quantumlab/core/absorbing_boundary.py:137, quantumlab/core/absorbing_boundary.py:138, quantumlab/core/absorbing_boundary.py:141, quantumlab/core/absorbing_boundary.py:142, quantumlab/core/absorbing_boundary.py:145, quantumlab/core/absorbing_boundary.py:146
INT_OTHER (12): quantumlab/core/absorbing_boundary.py:98, quantumlab/core/absorbing_boundary.py:102, quantumlab/core/absorbing_boundary.py:117, quantumlab/core/absorbing_boundary.py:118, quantumlab/core/absorbing_boundary.py:121, quantumlab/core/absorbing_boundary.py:122, quantumlab/core/absorbing_boundary.py:137, quantumlab/core/absorbing_boundary.py:138, quantumlab/core/absorbing_boundary.py:141, quantumlab/core/absorbing_boundary.py:142, quantumlab/core/absorbing_boundary.py:145, quantumlab/core/absorbing_boundary.py:146
IMPORTS (0): 

## AbsorbingBoundaryLayer._binomial  [quantumlab/core/absorbing_boundary.py:75] (method)
SIG: def _binomial(self, n, k):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/core/absorbing_boundary.py:69, quantumlab/core/absorbing_boundary.py:70
INT_OTHER (2): quantumlab/core/absorbing_boundary.py:69, quantumlab/core/absorbing_boundary.py:70
IMPORTS (0): 

## AbsorbingBoundaryLayer._build_mask  [quantumlab/core/absorbing_boundary.py:79] (method)
SIG: def _build_mask(self):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/core/absorbing_boundary.py:51
INT_OTHER (1): quantumlab/core/absorbing_boundary.py:51
IMPORTS (0): 

## AbsorbingBoundaryLayer._build_mask_1d  [quantumlab/core/absorbing_boundary.py:90] (method)
SIG: def _build_mask_1d(self):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/core/absorbing_boundary.py:82
INT_OTHER (1): quantumlab/core/absorbing_boundary.py:82
IMPORTS (0): 

## AbsorbingBoundaryLayer._build_mask_2d  [quantumlab/core/absorbing_boundary.py:106] (method)
SIG: def _build_mask_2d(self):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/core/absorbing_boundary.py:84
INT_OTHER (1): quantumlab/core/absorbing_boundary.py:84
IMPORTS (0): 

## AbsorbingBoundaryLayer._build_mask_3d  [quantumlab/core/absorbing_boundary.py:127] (method)
SIG: def _build_mask_3d(self):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/core/absorbing_boundary.py:86
INT_OTHER (1): quantumlab/core/absorbing_boundary.py:86
IMPORTS (0): 

## AbsorbingBoundaryLayer.apply  [quantumlab/core/absorbing_boundary.py:152] (method)
SIG: def apply(self, wavefunction):
EXT_CALLS (6):
  examples/05_2d_gaussian_barrier.py:55: abl.apply(wf_current)
  examples/06_3d_gaussian_barrier.py:49: abl.apply(wf_current)
  quantumlab/runner.py:163: abl.apply(wf_current)
  tests/test_2d_solver.py:61: abl.apply(wf)
  tests/test_3d_solver.py:144: abl.apply(wf)
  tests/test_absorbing_boundary_validation.py:102: AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3).apply(wf)
EXT_OTHER (6):
  examples/05_2d_gaussian_barrier.py:55: abl.apply(wf_current)
  examples/06_3d_gaussian_barrier.py:49: abl.apply(wf_current)
  quantumlab/runner.py:163: abl.apply(wf_current)
  tests/test_2d_solver.py:61: abl.apply(wf)
  tests/test_3d_solver.py:144: abl.apply(wf)
  tests/test_absorbing_boundary_validation.py:102: AbsorbingBoundaryLayer(grid, boundary_width=4.0, order=3).apply(wf)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## ndim  [quantumlab/core/spectral.py:11] (function)
SIG: def ndim(grid) -> int:
EXT_CALLS (3):
  quantumlab/solvers/split_operator.py:115: if rotation != 0.0 and ndim(grid) < 2:
  quantumlab/solvers/split_operator.py:173: if ndim(g) == 3:
  quantumlab/stationary/imaginary_time.py:90: if np.ndim(dtau) > 0:
EXT_OTHER (6):
  quantumlab/solvers/split_operator.py:115: if rotation != 0.0 and ndim(grid) < 2:
  quantumlab/solvers/split_operator.py:173: if ndim(g) == 3:
  quantumlab/solvers/split_operator.py:231: yz_axes = (1,) if psi.ndim == 2 else (1, 2)
  quantumlab/stationary/eigensolver.py:52: return v.reshape(shape + (-1,)), v.ndim == 1
  quantumlab/stationary/imaginary_time.py:90: if np.ndim(dtau) > 0:
  tests/test_backends.py:28: if isinstance(x, np.ndarray) and not isinstance(x, DeviceArray) and x.ndim > 0:
INT_CALLS (5): quantumlab/core/spectral.py:23, quantumlab/core/spectral.py:27, quantumlab/core/spectral.py:37, quantumlab/core/spectral.py:47, quantumlab/core/spectral.py:60
INT_OTHER (5): quantumlab/core/spectral.py:23, quantumlab/core/spectral.py:27, quantumlab/core/spectral.py:37, quantumlab/core/spectral.py:47, quantumlab/core/spectral.py:60
IMPORTS (1): quantumlab/solvers/split_operator.py:35(quantumlab.core.spectral)

## wavefunction_class  [quantumlab/core/spectral.py:21] (function)
SIG: def wavefunction_class(grid):
EXT_CALLS (6):
  quantumlab/solvers/multicomponent.py:69: self._wf_class = wavefunction_class(grid)
  quantumlab/solvers/split_operator.py:132: self._wf_class = wavefunction_class(grid)
  quantumlab/stationary/conjugate_gradient.py:132: return wavefunction_class(grid)(grid, psi), ConvergenceInfo(converged, it, E0, mu, residual)
  quantumlab/stationary/eigensolver.py:99: wf_class = wavefunction_class(grid)
  quantumlab/stationary/imaginary_time.py:104: wf_class = wavefunction_class(grid)
  quantumlab/stationary/imaginary_time.py:222: wf_class = wavefunction_class(grid)
EXT_OTHER (6):
  quantumlab/solvers/multicomponent.py:69: self._wf_class = wavefunction_class(grid)
  quantumlab/solvers/split_operator.py:132: self._wf_class = wavefunction_class(grid)
  quantumlab/stationary/conjugate_gradient.py:132: return wavefunction_class(grid)(grid, psi), ConvergenceInfo(converged, it, E0, mu, residual)
  quantumlab/stationary/eigensolver.py:99: wf_class = wavefunction_class(grid)
  quantumlab/stationary/imaginary_time.py:104: wf_class = wavefunction_class(grid)
  quantumlab/stationary/imaginary_time.py:222: wf_class = wavefunction_class(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): quantumlab/solvers/multicomponent.py:18(quantumlab.core.spectral), quantumlab/solvers/split_operator.py:35(quantumlab.core.spectral), quantumlab/stationary/conjugate_gradient.py:19(quantumlab.core.spectral), quantumlab/stationary/eigensolver.py:14(quantumlab.core.spectral), quantumlab/stationary/imaginary_time.py:14(quantumlab.core.spectral)

## volume_element  [quantumlab/core/spectral.py:26] (function)
SIG: def volume_element(grid) -> float:
EXT_CALLS (12):
  quantumlab/observables/current.py:32: return float(np.real(np.sum(np.conj(wf.psi) * Lz_psi) * volume_element(wf.grid)))
  quantumlab/observables/current.py:37: return complex(np.sum(np.conj(psi0) * psi_t) * volume_element(grid))
  quantumlab/observables/nonlinear.py:8: return float(0.5 * nonlinearity * np.sum(wf.probability_density ** 2) * volume_element(wf.grid))
  quantumlab/observables/nonlinear.py:29: dV = volume_element(states[0].grid)
  quantumlab/solvers/multicomponent.py:68: self._dV = volume_element(grid)
  quantumlab/solvers/split_operator.py:133: self._dV = volume_element(grid)
  quantumlab/stationary/conjugate_gradient.py:50: dV = volume_element(grid)
  quantumlab/stationary/eigensolver.py:98: dV = volume_element(grid)
  quantumlab/stationary/imaginary_time.py:103: dV = volume_element(grid)
  quantumlab/stationary/imaginary_time.py:221: dV = volume_element(grid)
  quantumlab/strongfield.py:132: return float(-np.sum(dV * wf.probability_density) * volume_element(grid) + force)
  tests/test_stationary.py:10: dV = volume_element(states[0].grid)
EXT_OTHER (12):
  quantumlab/observables/current.py:32: return float(np.real(np.sum(np.conj(wf.psi) * Lz_psi) * volume_element(wf.grid)))
  quantumlab/observables/current.py:37: return complex(np.sum(np.conj(psi0) * psi_t) * volume_element(grid))
  quantumlab/observables/nonlinear.py:8: return float(0.5 * nonlinearity * np.sum(wf.probability_density ** 2) * volume_element(wf.grid))
  quantumlab/observables/nonlinear.py:29: dV = volume_element(states[0].grid)
  quantumlab/solvers/multicomponent.py:68: self._dV = volume_element(grid)
  quantumlab/solvers/split_operator.py:133: self._dV = volume_element(grid)
  quantumlab/stationary/conjugate_gradient.py:50: dV = volume_element(grid)
  quantumlab/stationary/eigensolver.py:98: dV = volume_element(grid)
  quantumlab/stationary/imaginary_time.py:103: dV = volume_element(grid)
  quantumlab/stationary/imaginary_time.py:221: dV = volume_element(grid)
  quantumlab/strongfield.py:132: return float(-np.sum(dV * wf.probability_density) * volume_element(grid) + force)
  tests/test_stationary.py:10: dV = volume_element(states[0].grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (9): quantumlab/observables/current.py:8(quantumlab.core.spectral), quantumlab/observables/nonlinear.py:3(quantumlab.core.spectral), quantumlab/solvers/multicomponent.py:18(quantumlab.core.spectral), quantumlab/solvers/split_operator.py:35(quantumlab.core.spectral), quantumlab/stationary/conjugate_gradient.py:19(quantumlab.core.spectral), quantumlab/stationary/eigensolver.py:14(quantumlab.core.spectral), quantumlab/stationary/imaginary_time.py:14(quantumlab.core.spectral), quantumlab/strongfield.py:131(quantumlab.core.spectral), tests/test_stationary.py:6(quantumlab.core.spectral)

## coordinates  [quantumlab/core/spectral.py:35] (function)
SIG: def coordinates(grid):
EXT_CALLS (5):
  quantumlab/potentials/coulomb.py:24: coords = coordinates(grid)
  quantumlab/potentials/time_dependent.py:73: coords = coordinates(grid)
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/traps.py:28: coords = coordinates(grid)
  quantumlab/stationary/imaginary_time.py:41: coords = coordinates(grid)
EXT_OTHER (5):
  quantumlab/potentials/coulomb.py:24: coords = coordinates(grid)
  quantumlab/potentials/time_dependent.py:73: coords = coordinates(grid)
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/traps.py:28: coords = coordinates(grid)
  quantumlab/stationary/imaginary_time.py:41: coords = coordinates(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): quantumlab/potentials/coulomb.py:3(quantumlab.core.spectral), quantumlab/potentials/time_dependent.py:11(quantumlab.core.spectral), quantumlab/potentials/traps.py:3(quantumlab.core.spectral), quantumlab/stationary/imaginary_time.py:14(quantumlab.core.spectral)

## wavevectors  [quantumlab/core/spectral.py:45] (function)
SIG: def wavevectors(grid):
EXT_CALLS (1):
  quantumlab/observables/current.py:14: return tuple(ifftn(1j * K * psi_k) for K in wavevectors(grid))
EXT_OTHER (1):
  quantumlab/observables/current.py:14: return tuple(ifftn(1j * K * psi_k) for K in wavevectors(grid))
INT_CALLS (1): quantumlab/core/spectral.py:56
INT_OTHER (1): quantumlab/core/spectral.py:56
IMPORTS (1): quantumlab/observables/current.py:8(quantumlab.core.spectral)

## k_squared  [quantumlab/core/spectral.py:55] (function)
SIG: def k_squared(grid) -> np.ndarray:
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:137: self._T_k = self.hbar ** 2 * k_squared(grid) / (2.0 * self.m)
  quantumlab/stationary/conjugate_gradient.py:52: T_k = hbar ** 2 * k_squared(grid) / (2.0 * m)
  quantumlab/stationary/eigensolver.py:48: T_k = hbar ** 2 * k_squared(grid) / (2.0 * m)
  quantumlab/stationary/hamiltonian.py:13: T_k = hbar ** 2 * k_squared(grid) / (2.0 * m)
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:137: self._T_k = self.hbar ** 2 * k_squared(grid) / (2.0 * self.m)
  quantumlab/stationary/conjugate_gradient.py:52: T_k = hbar ** 2 * k_squared(grid) / (2.0 * m)
  quantumlab/stationary/eigensolver.py:48: T_k = hbar ** 2 * k_squared(grid) / (2.0 * m)
  quantumlab/stationary/hamiltonian.py:13: T_k = hbar ** 2 * k_squared(grid) / (2.0 * m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): quantumlab/solvers/split_operator.py:35(quantumlab.core.spectral), quantumlab/stationary/conjugate_gradient.py:19(quantumlab.core.spectral), quantumlab/stationary/eigensolver.py:14(quantumlab.core.spectral), quantumlab/stationary/hamiltonian.py:3(quantumlab.core.spectral)

## k_volume_element  [quantumlab/core/spectral.py:59] (function)
SIG: def k_volume_element(grid) -> float:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Potential  [quantumlab/potentials/base.py:4] (class)
SIG: class Potential(...):
EXT_CALLS (0):
EXT_OTHER (21):
  quantumlab/potentials/__init__.py:41: def create_potential(name: str, **kwargs) -> Potential:
  quantumlab/potentials/apertures.py:11: class ApertureScreen(Potential):
  quantumlab/potentials/apertures.py:79: class StadiumBilliard(Potential):
  quantumlab/potentials/barriers.py:5: class GaussianBarrier(Potential):
  quantumlab/potentials/barriers.py:20: class RectangularBarrier(Potential):
  quantumlab/potentials/barriers.py:35: class PotentialStep(Potential):
  quantumlab/potentials/barriers.py:47: class MultipleBarriers(Potential):
  quantumlab/potentials/barriers.py:68: class ResonantTunnelingDiode(Potential):
  quantumlab/potentials/barriers.py:96: class Gaussian2DBarrier(Potential):
  quantumlab/potentials/barriers.py:133: class Gaussian3DBarrier(Potential):
  quantumlab/potentials/coulomb.py:6: class SoftCoulomb(Potential):
  quantumlab/potentials/custom.py:5: class CustomPotential(Potential):
  quantumlab/potentials/disorder.py:5: class RandomDisorder(Potential):
  quantumlab/potentials/oscillator.py:5: class HarmonicOscillator(Potential):
  quantumlab/potentials/periodic.py:5: class CrystalPotential(Potential):
  quantumlab/potentials/time_dependent.py:16: class TimeDependentPotential(Potential):
  quantumlab/potentials/time_dependent.py:53: def __init__(self, base: Optional[Potential], F0: float, omega: float,
  quantumlab/potentials/traps.py:6: class HarmonicTrap(Potential):
  quantumlab/potentials/wells.py:5: class InfiniteSquareWell(Potential):
  quantumlab/potentials/wells.py:20: class FiniteSquareWell(Potential):
  quantumlab/potentials/wells.py:35: class DoubleWell(Potential):
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (11): quantumlab/potentials/__init__.py:1(quantumlab.potentials.base), quantumlab/potentials/apertures.py:2(quantumlab.potentials.base), quantumlab/potentials/barriers.py:2(quantumlab.potentials.base), quantumlab/potentials/coulomb.py:2(quantumlab.potentials.base), quantumlab/potentials/custom.py:2(quantumlab.potentials.base), quantumlab/potentials/disorder.py:2(quantumlab.potentials.base), quantumlab/potentials/oscillator.py:2(quantumlab.potentials.base), quantumlab/potentials/periodic.py:2(quantumlab.potentials.base), quantumlab/potentials/time_dependent.py:10(quantumlab.potentials.base), quantumlab/potentials/traps.py:2(quantumlab.potentials.base), quantumlab/potentials/wells.py:2(quantumlab.potentials.base)

## Potential.evaluate  [quantumlab/potentials/base.py:7] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## _smooth_step  [quantumlab/potentials/apertures.py:6] (function)
SIG: def _smooth_step(u):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (3): quantumlab/potentials/apertures.py:65, quantumlab/potentials/apertures.py:74, quantumlab/potentials/apertures.py:102
INT_OTHER (3): quantumlab/potentials/apertures.py:65, quantumlab/potentials/apertures.py:74, quantumlab/potentials/apertures.py:102
IMPORTS (0): 

## ApertureScreen  [quantumlab/potentials/apertures.py:11] (class)
SIG: class ApertureScreen(...):
EXT_CALLS (4):
  examples/07_3d_double_slit.py:50: screen = ApertureScreen(V0=60.0, wall_position=wall_x, wall_thickness=1.0, separation=separation,
  tests/test_new_potentials_and_observables.py:28: screen = ApertureScreen(V0=50.0, wall_position=0.0, wall_thickness=1.0, separation=4.0,
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_volume_3d.py:44: screen = ApertureScreen(V0=5.0, wall_position=2.0, separation=2.0, aperture='pinhole')
EXT_OTHER (7):
  examples/07_3d_double_slit.py:50: screen = ApertureScreen(V0=60.0, wall_position=wall_x, wall_thickness=1.0, separation=separation,
  quantumlab/potentials/__init__.py:35: 'aperture_screen':     ApertureScreen,
  quantumlab/potentials/__init__.py:36: 'double_slit':         ApertureScreen,
  tests/test_new_potentials_and_observables.py:28: screen = ApertureScreen(V0=50.0, wall_position=0.0, wall_thickness=1.0, separation=4.0,
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:65: assert isinstance(create_potential('double_slit', V0=1.0), ApertureScreen)
  tests/test_volume_3d.py:44: screen = ApertureScreen(V0=5.0, wall_position=2.0, separation=2.0, aperture='pinhole')
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): examples/07_3d_double_slit.py:23(quantumlab.potentials), tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), tests/test_volume_3d.py:4(quantumlab.potentials), quantumlab/potentials/__init__.py:14(quantumlab.potentials.apertures)

## ApertureScreen.__init__  [quantumlab/potentials/apertures.py:40] (method)
SIG: def __init__(self, V0: float, wall_position: float = 0.0, wall_thickness: float = 1.0,
                 separation: float = 4.0, aperture_width: float = 1.0, n_apertures: int = 2,
                 aperture: str = 'slit', smoothing: float = 0.25):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## ApertureScreen.aperture_centers  [quantumlab/potentials/apertures.py:55] (method)
SIG: def aperture_centers(self) -> np.ndarray:
EXT_CALLS (0):
EXT_OTHER (1):
  tests/test_new_potentials_and_observables.py:38: np.testing.assert_allclose(screen.aperture_centers, [-2.0, 2.0])
INT_CALLS (0): 
INT_OTHER (1): quantumlab/potentials/apertures.py:69
IMPORTS (0): 

## ApertureScreen.evaluate  [quantumlab/potentials/apertures.py:59] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## StadiumBilliard  [quantumlab/potentials/apertures.py:79] (class)
SIG: class StadiumBilliard(...):
EXT_CALLS (3):
  examples/10_quantum_chaos_stadium.py:35: stadium = StadiumBilliard(V0=300.0, radius=radius, length=length, smoothing=0.08)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_stationary.py:40: pot = StadiumBilliard(V0=40.0, radius=2.5, length=3.0, smoothing=0.3)
EXT_OTHER (5):
  examples/10_quantum_chaos_stadium.py:35: stadium = StadiumBilliard(V0=300.0, radius=radius, length=length, smoothing=0.08)
  quantumlab/potentials/__init__.py:37: 'stadium':             StadiumBilliard,
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:66: assert isinstance(create_potential('stadium', V0=1.0, radius=1.0, length=1.0), StadiumBilliard)
  tests/test_stationary.py:40: pot = StadiumBilliard(V0=40.0, radius=2.5, length=3.0, smoothing=0.3)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): examples/10_quantum_chaos_stadium.py:25(quantumlab.potentials), tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), tests/test_stationary.py:4(quantumlab.potentials), quantumlab/potentials/__init__.py:14(quantumlab.potentials.apertures)

## StadiumBilliard.__init__  [quantumlab/potentials/apertures.py:90] (method)
SIG: def __init__(self, V0: float, radius: float, length: float, smoothing: float = 0.2):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## StadiumBilliard.evaluate  [quantumlab/potentials/apertures.py:96] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## GaussianBarrier  [quantumlab/potentials/barriers.py:5] (class)
SIG: class GaussianBarrier(...):
EXT_CALLS (9):
  examples/01_gaussian_barrier.py:32: potential = GaussianBarrier(V0, barrier_width, barrier_center)
  testbench_interlock.py:99: pot = GaussianBarrier(V0=V0, width=1.2, position=0.0)
  tests/test_2d_solver.py:15: potential = GaussianBarrier(V0=5.0, width=2.0, position=0.0)
  tests/test_backends.py:76: '1d_barrier_order4': lambda: (Grid1D(256, -20.0, 20.0), GaussianBarrier(3.0, 1.0, 0.0), dict(order=4),
  tests/test_potentials.py:17: pot = GaussianBarrier(V0, width, pos)
  tests/test_solvers.py:12: potential = GaussianBarrier(V0=5.0, width=2.0, position=0.0)
  tests/test_solvers.py:23: potential = GaussianBarrier(V0=4.0, width=1.5, position=0.0)
  tests/test_split_operator.py:30: pot, legacy = GaussianBarrier(4.0, 1.0, 0.0), SplitStep1DSolver
  tests/test_split_operator.py:52: pot = GaussianBarrier(3.0, 1.0, 0.0)
EXT_OTHER (11):
  examples/01_gaussian_barrier.py:32: potential = GaussianBarrier(V0, barrier_width, barrier_center)
  quantumlab/potentials/__init__.py:20: 'gaussian_barrier':    GaussianBarrier,
  quantumlab/potentials/__init__.py:21: 'barrier':             GaussianBarrier,
  testbench_interlock.py:99: pot = GaussianBarrier(V0=V0, width=1.2, position=0.0)
  tests/test_2d_solver.py:15: potential = GaussianBarrier(V0=5.0, width=2.0, position=0.0)
  tests/test_backends.py:76: '1d_barrier_order4': lambda: (Grid1D(256, -20.0, 20.0), GaussianBarrier(3.0, 1.0, 0.0), dict(order=4),
  tests/test_potentials.py:17: pot = GaussianBarrier(V0, width, pos)
  tests/test_solvers.py:12: potential = GaussianBarrier(V0=5.0, width=2.0, position=0.0)
  tests/test_solvers.py:23: potential = GaussianBarrier(V0=4.0, width=1.5, position=0.0)
  tests/test_split_operator.py:30: pot, legacy = GaussianBarrier(4.0, 1.0, 0.0), SplitStep1DSolver
  tests/test_split_operator.py:52: pot = GaussianBarrier(3.0, 1.0, 0.0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (9): benchmarks/validation_suite.py:16(quantumlab.potentials), testbench_interlock.py:37(quantumlab.potentials), tests/test_backends.py:17(quantumlab.potentials), tests/test_split_operator.py:5(quantumlab.potentials), examples/01_gaussian_barrier.py:6(quantumlab.potentials.barriers), quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers), tests/test_2d_solver.py:5(quantumlab.potentials.barriers), tests/test_potentials.py:4(quantumlab.potentials.barriers), tests/test_solvers.py:5(quantumlab.potentials.barriers)

## GaussianBarrier.__init__  [quantumlab/potentials/barriers.py:7] (method)
SIG: def __init__(self, V0: float, width: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## GaussianBarrier.evaluate  [quantumlab/potentials/barriers.py:12] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## RectangularBarrier  [quantumlab/potentials/barriers.py:20] (class)
SIG: class RectangularBarrier(...):
EXT_CALLS (1):
  tests/test_potentials.py:30: pot = RectangularBarrier(V0, width, pos)
EXT_OTHER (2):
  quantumlab/potentials/__init__.py:24: 'rectangular_barrier': RectangularBarrier,
  tests/test_potentials.py:30: pot = RectangularBarrier(V0, width, pos)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers), tests/test_potentials.py:4(quantumlab.potentials.barriers)

## RectangularBarrier.__init__  [quantumlab/potentials/barriers.py:22] (method)
SIG: def __init__(self, V0: float, width: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## RectangularBarrier.evaluate  [quantumlab/potentials/barriers.py:27] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## PotentialStep  [quantumlab/potentials/barriers.py:35] (class)
SIG: class PotentialStep(...):
EXT_CALLS (0):
EXT_OTHER (1):
  quantumlab/potentials/__init__.py:25: 'potential_step':      PotentialStep,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers), tests/test_potentials.py:4(quantumlab.potentials.barriers)

## PotentialStep.__init__  [quantumlab/potentials/barriers.py:37] (method)
SIG: def __init__(self, V0: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## PotentialStep.evaluate  [quantumlab/potentials/barriers.py:41] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## MultipleBarriers  [quantumlab/potentials/barriers.py:47] (class)
SIG: class MultipleBarriers(...):
EXT_CALLS (1):
  examples/04_multiple_barriers.py:33: potential = MultipleBarriers(V0, width, positions)
EXT_OTHER (2):
  examples/04_multiple_barriers.py:33: potential = MultipleBarriers(V0, width, positions)
  quantumlab/potentials/__init__.py:26: 'multiple_barriers':   MultipleBarriers,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/04_multiple_barriers.py:5(quantumlab.potentials.barriers), quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers)

## MultipleBarriers.__init__  [quantumlab/potentials/barriers.py:49] (method)
SIG: def __init__(self, V0: float, width: float, positions: list):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## MultipleBarriers.evaluate  [quantumlab/potentials/barriers.py:54] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## ResonantTunnelingDiode  [quantumlab/potentials/barriers.py:68] (class)
SIG: class ResonantTunnelingDiode(...):
EXT_CALLS (0):
EXT_OTHER (1):
  quantumlab/potentials/__init__.py:27: 'rtd':                 ResonantTunnelingDiode,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (1): quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers)

## ResonantTunnelingDiode.__init__  [quantumlab/potentials/barriers.py:70] (method)
SIG: def __init__(self, V0: float, barrier_width: float, well_width: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## ResonantTunnelingDiode.evaluate  [quantumlab/potentials/barriers.py:76] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Gaussian2DBarrier  [quantumlab/potentials/barriers.py:96] (class)
SIG: class Gaussian2DBarrier(...):
EXT_CALLS (2):
  examples/05_2d_gaussian_barrier.py:40: potential = Gaussian2DBarrier(V0=V0, width=barrier_width, x0=0.0, y0=0.0)
  tests/test_split_operator.py:34: pot, legacy = Gaussian2DBarrier(3.0, 1.0), SplitStep2DSolver
EXT_OTHER (3):
  examples/05_2d_gaussian_barrier.py:40: potential = Gaussian2DBarrier(V0=V0, width=barrier_width, x0=0.0, y0=0.0)
  quantumlab/potentials/__init__.py:22: 'gaussian_2d_barrier': Gaussian2DBarrier,
  tests/test_split_operator.py:34: pot, legacy = Gaussian2DBarrier(3.0, 1.0), SplitStep2DSolver
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (3): tests/test_split_operator.py:5(quantumlab.potentials), examples/05_2d_gaussian_barrier.py:5(quantumlab.potentials.barriers), quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers)

## Gaussian2DBarrier.__init__  [quantumlab/potentials/barriers.py:117] (method)
SIG: def __init__(self, V0: float, width: float, x0: float = 0.0, y0: float = 0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Gaussian2DBarrier.evaluate  [quantumlab/potentials/barriers.py:123] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Gaussian3DBarrier  [quantumlab/potentials/barriers.py:133] (class)
SIG: class Gaussian3DBarrier(...):
EXT_CALLS (9):
  benchmarks/perf_comparison.py:91: potential = Gaussian3DBarrier(V0=5.0, width=4.0)
  examples/06_3d_gaussian_barrier.py:41: potential = Gaussian3DBarrier(V0=V0, width=barrier_width, x0=0.0, y0=0.0, z0=0.0)
  tests/test_3d_gpu_solver.py:34: return Gaussian3DBarrier(V0=4.0, width=2.0)
  tests/test_3d_gpu_solver.py:120: potential = Gaussian3DBarrier(V0=4.0, width=2.0)
  tests/test_3d_gpu_solver.py:139: potential = Gaussian3DBarrier(V0=V0, width=width)
  tests/test_3d_solver.py:76: potential = Gaussian3DBarrier(V0=4.0, width=2.0, x0=0.0, y0=0.0, z0=0.0)
  tests/test_3d_solver.py:155: barrier = Gaussian3DBarrier(V0=5.0, width=2.0, x0=0.0, y0=0.0, z0=0.0)
  tests/test_3d_solver.py:166: barrier = Gaussian3DBarrier(V0=5.0, width=2.0)
  tests/test_split_operator.py:38: pot, legacy = Gaussian3DBarrier(3.0, 1.0), SplitStep3DSolver
EXT_OTHER (10):
  benchmarks/perf_comparison.py:91: potential = Gaussian3DBarrier(V0=5.0, width=4.0)
  examples/06_3d_gaussian_barrier.py:41: potential = Gaussian3DBarrier(V0=V0, width=barrier_width, x0=0.0, y0=0.0, z0=0.0)
  quantumlab/potentials/__init__.py:23: 'gaussian_3d_barrier': Gaussian3DBarrier,
  tests/test_3d_gpu_solver.py:34: return Gaussian3DBarrier(V0=4.0, width=2.0)
  tests/test_3d_gpu_solver.py:120: potential = Gaussian3DBarrier(V0=4.0, width=2.0)
  tests/test_3d_gpu_solver.py:139: potential = Gaussian3DBarrier(V0=V0, width=width)
  tests/test_3d_solver.py:76: potential = Gaussian3DBarrier(V0=4.0, width=2.0, x0=0.0, y0=0.0, z0=0.0)
  tests/test_3d_solver.py:155: barrier = Gaussian3DBarrier(V0=5.0, width=2.0, x0=0.0, y0=0.0, z0=0.0)
  tests/test_3d_solver.py:166: barrier = Gaussian3DBarrier(V0=5.0, width=2.0)
  tests/test_split_operator.py:38: pot, legacy = Gaussian3DBarrier(3.0, 1.0), SplitStep3DSolver
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (6): tests/test_split_operator.py:5(quantumlab.potentials), benchmarks/perf_comparison.py:37(quantumlab.potentials.barriers), examples/06_3d_gaussian_barrier.py:5(quantumlab.potentials.barriers), quantumlab/potentials/__init__.py:2(quantumlab.potentials.barriers), tests/test_3d_gpu_solver.py:9(quantumlab.potentials.barriers), tests/test_3d_solver.py:5(quantumlab.potentials.barriers)

## Gaussian3DBarrier.__init__  [quantumlab/potentials/barriers.py:149] (method)
SIG: def __init__(self, V0: float, width: float,
                 x0: float = 0.0, y0: float = 0.0, z0: float = 0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Gaussian3DBarrier.evaluate  [quantumlab/potentials/barriers.py:157] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SoftCoulomb  [quantumlab/potentials/coulomb.py:6] (class)
SIG: class SoftCoulomb(...):
EXT_CALLS (6):
  benchmarks/validation_suite.py:210: atom = SoftCoulomb()
  benchmarks/validation_suite.py:312: _, info = ground_state_pcg(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), tol=1e-10)
  examples/12_high_harmonic_generation.py:86: atom = SoftCoulomb(Z=1.0, softening=np.sqrt(2.0))
  tests/test_conjugate_gradient.py:15: (Grid1D(2048, -100.0, 100.0), SoftCoulomb(), {}, -0.5),                       # V < 0
  tests/test_strongfield.py:34: energies, _ = eigenstates(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), n_states=2)
  tests/test_strongfield.py:43: pot = SoftCoulomb(Z=2.0, softening=0.8, center=(0.5, -1.0))
EXT_OTHER (8):
  benchmarks/validation_suite.py:210: atom = SoftCoulomb()
  benchmarks/validation_suite.py:312: _, info = ground_state_pcg(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), tol=1e-10)
  examples/12_high_harmonic_generation.py:86: atom = SoftCoulomb(Z=1.0, softening=np.sqrt(2.0))
  quantumlab/potentials/__init__.py:38: 'soft_coulomb':        SoftCoulomb,
  tests/test_conjugate_gradient.py:15: (Grid1D(2048, -100.0, 100.0), SoftCoulomb(), {}, -0.5),                       # V < 0
  tests/test_strongfield.py:34: energies, _ = eigenstates(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), n_states=2)
  tests/test_strongfield.py:37: assert isinstance(create_potential('soft_coulomb'), SoftCoulomb)
  tests/test_strongfield.py:43: pot = SoftCoulomb(Z=2.0, softening=0.8, center=(0.5, -1.0))
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): benchmarks/validation_suite.py:16(quantumlab.potentials), examples/12_high_harmonic_generation.py:42(quantumlab.potentials), tests/test_conjugate_gradient.py:5(quantumlab.potentials), tests/test_strongfield.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:13(quantumlab.potentials.coulomb)

## SoftCoulomb.__init__  [quantumlab/potentials/coulomb.py:18] (method)
SIG: def __init__(self, Z: float = 1.0, softening: float = np.sqrt(2.0), center=None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SoftCoulomb._displacements  [quantumlab/potentials/coulomb.py:23] (method)
SIG: def _displacements(self, grid):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/potentials/coulomb.py:30, quantumlab/potentials/coulomb.py:35
INT_OTHER (2): quantumlab/potentials/coulomb.py:30, quantumlab/potentials/coulomb.py:35
IMPORTS (0): 

## SoftCoulomb.evaluate  [quantumlab/potentials/coulomb.py:29] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SoftCoulomb.gradient  [quantumlab/potentials/coulomb.py:33] (method)
SIG: def gradient(self, grid):
EXT_CALLS (5):
  quantumlab/observables/current.py:23: return tuple((hbar / m) * np.imag(np.conj(psi) * d) for d in gradient(psi, wf.grid))
  quantumlab/observables/current.py:30: d_dx, d_dy = gradient(wf.psi, wf.grid)[:2]
  quantumlab/strongfield.py:127: dV = base_potential.gradient(grid)[0]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  tests/test_strongfield.py:45: gx, gy = pot.gradient(grid)
EXT_OTHER (5):
  quantumlab/observables/current.py:23: return tuple((hbar / m) * np.imag(np.conj(psi) * d) for d in gradient(psi, wf.grid))
  quantumlab/observables/current.py:30: d_dx, d_dy = gradient(wf.psi, wf.grid)[:2]
  quantumlab/strongfield.py:127: dV = base_potential.gradient(grid)[0]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  tests/test_strongfield.py:45: gx, gy = pot.gradient(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/observables/__init__.py:6(quantumlab.observables.current), quantumlab/strongfield.py:129(quantumlab.observables.current)

## CustomPotential  [quantumlab/potentials/custom.py:5] (class)
SIG: class CustomPotential(...):
EXT_CALLS (5):
  benchmarks/validation_suite.py:53: pot = CustomPotential(lambda x: 0.1 * x ** 4 - x ** 2 + 2.0 * np.exp(-x ** 2))
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:48: pot = CustomPotential(func)
  tests/test_split_operator.py:67: pot = CustomPotential(lambda x: 0.1 * x ** 4 - x ** 2 + 2.0 * np.exp(-x ** 2))
  tests/test_split_operator.py:82: pot = CustomPotential(lambda x: 0.1 * x ** 4 - x ** 2)
EXT_OTHER (5):
  benchmarks/validation_suite.py:53: pot = CustomPotential(lambda x: 0.1 * x ** 4 - x ** 2 + 2.0 * np.exp(-x ** 2))
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:48: pot = CustomPotential(func)
  tests/test_split_operator.py:67: pot = CustomPotential(lambda x: 0.1 * x ** 4 - x ** 2 + 2.0 * np.exp(-x ** 2))
  tests/test_split_operator.py:82: pot = CustomPotential(lambda x: 0.1 * x ** 4 - x ** 2)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): benchmarks/validation_suite.py:16(quantumlab.potentials), tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), tests/test_split_operator.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:11(quantumlab.potentials.custom), tests/test_potentials.py:9(quantumlab.potentials.custom)

## CustomPotential.__init__  [quantumlab/potentials/custom.py:7] (method)
SIG: def __init__(self, func):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## CustomPotential.evaluate  [quantumlab/potentials/custom.py:12] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## RandomDisorder  [quantumlab/potentials/disorder.py:5] (class)
SIG: class RandomDisorder(...):
EXT_CALLS (0):
EXT_OTHER (1):
  quantumlab/potentials/__init__.py:33: 'disorder':            RandomDisorder,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/potentials/__init__.py:10(quantumlab.potentials.disorder), tests/test_potentials.py:8(quantumlab.potentials.disorder)

## RandomDisorder.__init__  [quantumlab/potentials/disorder.py:7] (method)
SIG: def __init__(self, W: float, cell_width: float, seed: int=None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## RandomDisorder.evaluate  [quantumlab/potentials/disorder.py:12] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## HarmonicOscillator  [quantumlab/potentials/oscillator.py:5] (class)
SIG: class HarmonicOscillator(...):
EXT_CALLS (5):
  examples/02_harmonic_oscillator.py:30: potential = HarmonicOscillator(omega, m)
  tests/test_2d_solver.py:27: potential = HarmonicOscillator(omega=1.0, m=1.0, position=0.0)
  tests/test_3d_solver.py:94: potential = HarmonicOscillator(omega=1.0, m=1.0)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_potentials.py:40: pot = HarmonicOscillator(omega, m, position=0.0)
EXT_OTHER (6):
  examples/02_harmonic_oscillator.py:30: potential = HarmonicOscillator(omega, m)
  quantumlab/potentials/__init__.py:31: 'harmonic':            HarmonicOscillator,
  tests/test_2d_solver.py:27: potential = HarmonicOscillator(omega=1.0, m=1.0, position=0.0)
  tests/test_3d_solver.py:94: potential = HarmonicOscillator(omega=1.0, m=1.0)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_potentials.py:40: pot = HarmonicOscillator(omega, m, position=0.0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (6): tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), examples/02_harmonic_oscillator.py:6(quantumlab.potentials.oscillator), quantumlab/potentials/__init__.py:8(quantumlab.potentials.oscillator), tests/test_2d_solver.py:6(quantumlab.potentials.oscillator), tests/test_3d_solver.py:6(quantumlab.potentials.oscillator), tests/test_potentials.py:6(quantumlab.potentials.oscillator)

## HarmonicOscillator.__init__  [quantumlab/potentials/oscillator.py:7] (method)
SIG: def __init__(self, omega: float, m: float=1.0, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## HarmonicOscillator.evaluate  [quantumlab/potentials/oscillator.py:12] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## CrystalPotential  [quantumlab/potentials/periodic.py:5] (class)
SIG: class CrystalPotential(...):
EXT_CALLS (0):
EXT_OTHER (1):
  quantumlab/potentials/__init__.py:32: 'crystal':             CrystalPotential,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/potentials/__init__.py:9(quantumlab.potentials.periodic), tests/test_potentials.py:7(quantumlab.potentials.periodic)

## CrystalPotential.__init__  [quantumlab/potentials/periodic.py:7] (method)
SIG: def __init__(self, V0: float, lattice_spacing: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## CrystalPotential.evaluate  [quantumlab/potentials/periodic.py:12] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## TimeDependentPotential  [quantumlab/potentials/time_dependent.py:16] (class)
SIG: class TimeDependentPotential(...):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (0): 
INT_OTHER (2): quantumlab/potentials/time_dependent.py:27, quantumlab/potentials/time_dependent.py:87
IMPORTS (1): quantumlab/potentials/__init__.py:15(quantumlab.potentials.time_dependent)

## TimeDependentPotential.evaluate_at  [quantumlab/potentials/time_dependent.py:20] (method)
SIG: def evaluate_at(self, grid, t: float) -> np.ndarray:
EXT_CALLS (3):
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
EXT_OTHER (3):
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
INT_CALLS (1): quantumlab/potentials/time_dependent.py:24
INT_OTHER (1): quantumlab/potentials/time_dependent.py:24
IMPORTS (0): 

## TimeDependentPotential.evaluate  [quantumlab/potentials/time_dependent.py:23] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (33):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (33):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (1): quantumlab/potentials/time_dependent.py:77
INT_OTHER (1): quantumlab/potentials/time_dependent.py:77
IMPORTS (0): 

## DipoleDrive  [quantumlab/potentials/time_dependent.py:27] (class)
SIG: class DipoleDrive(...):
EXT_CALLS (11):
  benchmarks/validation_suite.py:70: solver = SplitOperatorSolver(grid, DipoleDrive(HarmonicTrap(omega), F0, Omega), 0.01, order=4)
  benchmarks/validation_suite.py:219: laser = DipoleDrive(atom, F0=sf.intensity_to_field(1e14), omega=w,
  examples/12_high_harmonic_generation.py:63: laser = DipoleDrive(atom, F0=field, omega=omega, envelope=flat_top_envelope(duration, N_RAMP * period))
  tests/test_backends.py:78: '1d_driven': lambda: (Grid1D(128, -15.0, 15.0), DipoleDrive(HarmonicTrap(1.0), 0.4, 0.7), dict(order=4),
  tests/test_conjugate_gradient.py:68: ground_state_pcg(Grid1D(32, -4.0, 4.0), DipoleDrive(None, 1.0, 1.0))
  tests/test_multicomponent.py:137: CoupledGPESolver(grid, (DipoleDrive(None, 1.0, 1.0), None), np.eye(2), 0.01)
  tests/test_new_potentials_and_observables.py:73: drive = DipoleDrive(None, F0=2.0, omega=1.0, envelope=env)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
  tests/test_split_operator.py:93: pot = DipoleDrive(HarmonicTrap(omega), F0=F0, omega=Omega)
  tests/test_split_operator.py:107: a = DipoleDrive(HarmonicTrap(1.0), F0=0.3, omega=1.7)
  tests/test_split_operator.py:141: SplitOperatorSolver(grid, DipoleDrive(None, 1.0, 1.0), 0.01, imaginary_time=True)
EXT_OTHER (11):
  benchmarks/validation_suite.py:70: solver = SplitOperatorSolver(grid, DipoleDrive(HarmonicTrap(omega), F0, Omega), 0.01, order=4)
  benchmarks/validation_suite.py:219: laser = DipoleDrive(atom, F0=sf.intensity_to_field(1e14), omega=w,
  examples/12_high_harmonic_generation.py:63: laser = DipoleDrive(atom, F0=field, omega=omega, envelope=flat_top_envelope(duration, N_RAMP * period))
  tests/test_backends.py:78: '1d_driven': lambda: (Grid1D(128, -15.0, 15.0), DipoleDrive(HarmonicTrap(1.0), 0.4, 0.7), dict(order=4),
  tests/test_conjugate_gradient.py:68: ground_state_pcg(Grid1D(32, -4.0, 4.0), DipoleDrive(None, 1.0, 1.0))
  tests/test_multicomponent.py:137: CoupledGPESolver(grid, (DipoleDrive(None, 1.0, 1.0), None), np.eye(2), 0.01)
  tests/test_new_potentials_and_observables.py:73: drive = DipoleDrive(None, F0=2.0, omega=1.0, envelope=env)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
  tests/test_split_operator.py:93: pot = DipoleDrive(HarmonicTrap(omega), F0=F0, omega=Omega)
  tests/test_split_operator.py:107: a = DipoleDrive(HarmonicTrap(1.0), F0=0.3, omega=1.7)
  tests/test_split_operator.py:141: SplitOperatorSolver(grid, DipoleDrive(None, 1.0, 1.0), 0.01, imaginary_time=True)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (8): benchmarks/validation_suite.py:16(quantumlab.potentials), examples/12_high_harmonic_generation.py:42(quantumlab.potentials), tests/test_backends.py:17(quantumlab.potentials), tests/test_conjugate_gradient.py:5(quantumlab.potentials), tests/test_multicomponent.py:5(quantumlab.potentials), tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), tests/test_split_operator.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:15(quantumlab.potentials.time_dependent)

## DipoleDrive.__init__  [quantumlab/potentials/time_dependent.py:53] (method)
SIG: def __init__(self, base: Optional[Potential], F0: float, omega: float,
                 axis: str = 'x', phase: float = 0.0,
                 envelope: Optional[Callable[[float], float]] = None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## DipoleDrive.force  [quantumlab/potentials/time_dependent.py:67] (method)
SIG: def force(self, t: float) -> float:
EXT_CALLS (8):
  benchmarks/validation_suite.py:224: callback=lambda n, t, wf: acc.append(sf.dipole_acceleration(wf, atom, laser.force(t))))
  examples/12_high_harmonic_generation.py:68: acc.append(dipole_acceleration(wf, atom, laser.force(t)))
  examples/12_high_harmonic_generation.py:198: F = np.array([laser.force(x) for x in t[m]])
  examples/12_high_harmonic_generation.py:218: ax2.plot(t / period, [laser.force(x_) for x_ in t], color='#7fd4ff', lw=0.8)
  examples/12_high_harmonic_generation.py:233: axf.plot(tf / period, [laser.force(x_) for x_ in tf], color='#7fd4ff', lw=1)
  examples/12_high_harmonic_generation.py:245: dot.set_data([td[k] / period], [laser.force(td[k])])
  tests/test_new_potentials_and_observables.py:74: assert drive.force(5.0) == pytest.approx(2.0 * np.sin(5.0))
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
EXT_OTHER (9):
  benchmarks/validation_suite.py:224: callback=lambda n, t, wf: acc.append(sf.dipole_acceleration(wf, atom, laser.force(t))))
  examples/12_high_harmonic_generation.py:68: acc.append(dipole_acceleration(wf, atom, laser.force(t)))
  examples/12_high_harmonic_generation.py:198: F = np.array([laser.force(x) for x in t[m]])
  examples/12_high_harmonic_generation.py:218: ax2.plot(t / period, [laser.force(x_) for x_ in t], color='#7fd4ff', lw=0.8)
  examples/12_high_harmonic_generation.py:233: axf.plot(tf / period, [laser.force(x_) for x_ in tf], color='#7fd4ff', lw=1)
  examples/12_high_harmonic_generation.py:245: dot.set_data([td[k] / period], [laser.force(td[k])])
  quantumlab/strongfield.py:132: return float(-np.sum(dV * wf.probability_density) * volume_element(grid) + force)
  tests/test_new_potentials_and_observables.py:74: assert drive.force(5.0) == pytest.approx(2.0 * np.sin(5.0))
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
INT_CALLS (1): quantumlab/potentials/time_dependent.py:84
INT_OTHER (1): quantumlab/potentials/time_dependent.py:84
IMPORTS (0): 

## DipoleDrive._static_parts  [quantumlab/potentials/time_dependent.py:71] (method)
SIG: def _static_parts(self, grid):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/potentials/time_dependent.py:83
INT_OTHER (1): quantumlab/potentials/time_dependent.py:83
IMPORTS (0): 

## DipoleDrive.evaluate_at  [quantumlab/potentials/time_dependent.py:82] (method)
SIG: def evaluate_at(self, grid, t: float) -> np.ndarray:
EXT_CALLS (3):
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
EXT_OTHER (3):
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
INT_CALLS (1): quantumlab/potentials/time_dependent.py:24
INT_OTHER (1): quantumlab/potentials/time_dependent.py:24
IMPORTS (0): 

## TimeDependentCustomPotential  [quantumlab/potentials/time_dependent.py:87] (class)
SIG: class TimeDependentCustomPotential(...):
EXT_CALLS (1):
  tests/test_split_operator.py:108: b = TimeDependentCustomPotential(lambda x, t: 0.5 * x ** 2 - 0.3 * np.sin(1.7 * t) * x)
EXT_OTHER (1):
  tests/test_split_operator.py:108: b = TimeDependentCustomPotential(lambda x, t: 0.5 * x ** 2 - 0.3 * np.sin(1.7 * t) * x)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): tests/test_split_operator.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:15(quantumlab.potentials.time_dependent)

## TimeDependentCustomPotential.__init__  [quantumlab/potentials/time_dependent.py:90] (method)
SIG: def __init__(self, func: Callable):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## TimeDependentCustomPotential.evaluate_at  [quantumlab/potentials/time_dependent.py:95] (method)
SIG: def evaluate_at(self, grid, t: float) -> np.ndarray:
EXT_CALLS (3):
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
EXT_OTHER (3):
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  tests/test_new_potentials_and_observables.py:76: np.testing.assert_allclose(drive.evaluate_at(grid, 5.0), -drive.force(5.0) * grid.x)
  tests/test_new_potentials_and_observables.py:81: DipoleDrive(None, 1.0, 1.0, axis='z').evaluate_at(Grid1D(8, -1.0, 1.0), 0.0)
INT_CALLS (1): quantumlab/potentials/time_dependent.py:24
INT_OTHER (1): quantumlab/potentials/time_dependent.py:24
IMPORTS (0): 

## sin2_envelope  [quantumlab/potentials/time_dependent.py:99] (function)
SIG: def sin2_envelope(duration: float) -> Callable[[float], float]:
EXT_CALLS (1):
  tests/test_new_potentials_and_observables.py:70: env = sin2_envelope(10.0)
EXT_OTHER (1):
  tests/test_new_potentials_and_observables.py:70: env = sin2_envelope(10.0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:15(quantumlab.potentials.time_dependent)

## flat_top_envelope  [quantumlab/potentials/time_dependent.py:108] (function)
SIG: def flat_top_envelope(duration: float, ramp: float) -> Callable[[float], float]:
EXT_CALLS (4):
  benchmarks/validation_suite.py:220: envelope=flat_top_envelope(20 * period, 3 * period))
  examples/12_high_harmonic_generation.py:63: laser = DipoleDrive(atom, F0=field, omega=omega, envelope=flat_top_envelope(duration, N_RAMP * period))
  tests/test_strongfield.py:51: env = flat_top_envelope(10.0, 2.0)
  tests/test_strongfield.py:57: flat_top_envelope(3.0, 2.0)
EXT_OTHER (4):
  benchmarks/validation_suite.py:220: envelope=flat_top_envelope(20 * period, 3 * period))
  examples/12_high_harmonic_generation.py:63: laser = DipoleDrive(atom, F0=field, omega=omega, envelope=flat_top_envelope(duration, N_RAMP * period))
  tests/test_strongfield.py:51: env = flat_top_envelope(10.0, 2.0)
  tests/test_strongfield.py:57: flat_top_envelope(3.0, 2.0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): benchmarks/validation_suite.py:16(quantumlab.potentials), examples/12_high_harmonic_generation.py:42(quantumlab.potentials), tests/test_strongfield.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:15(quantumlab.potentials.time_dependent)

## HarmonicTrap  [quantumlab/potentials/traps.py:6] (class)
SIG: class HarmonicTrap(...):
EXT_CALLS (74):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/validation_suite.py:70: solver = SplitOperatorSolver(grid, DipoleDrive(HarmonicTrap(omega), F0, Omega), 0.01, order=4)
  benchmarks/validation_suite.py:84: pot = HarmonicTrap((1.0, 1.3, 0.8))
  benchmarks/validation_suite.py:119: E, _ = eigenstates(grid, HarmonicTrap(1.0), n_states=10, method='lanczos')
  benchmarks/validation_suite.py:124: E, _ = eigenstates(grid, HarmonicTrap(w), n_states=6, method='lobpcg')
  benchmarks/validation_suite.py:129: _, info = ground_state(grid, HarmonicTrap(w), dtau=0.01)
  benchmarks/validation_suite.py:137: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.05, order=4)
  benchmarks/validation_suite.py:171: trap, g = HarmonicTrap((1.0, 1.2, 1.4)), 60.0
  benchmarks/validation_suite.py:180: trap = HarmonicTrap((1.0, 1.3))
  benchmarks/validation_suite.py:192: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:202: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:284: trap, G = HarmonicTrap((1.0, 1.3)), 60.0
  benchmarks/validation_suite.py:301: states, _ = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G2, (a, b), dtau=0.005)
  benchmarks/validation_suite.py:303: V = sum(potential_energy_expectation(s, HarmonicTrap(1.0)) for s in states)
  benchmarks/validation_suite.py:316: trap, g = HarmonicTrap((1.0, 1.2, 1.4)), 60.0
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  examples/08_3d_bec_time_of_flight.py:74: trap = HarmonicTrap(omegas)
  examples/11_rotating_bec_vortex_lattice.py:68: trap = HarmonicTrap((np.sqrt(1.0 + eps_x), np.sqrt(1.0 + eps_y)))
  examples/11_rotating_bec_vortex_lattice.py:71: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, nonlinearity=g2)
  examples/11_rotating_bec_vortex_lattice.py:155: trap3 = HarmonicTrap((np.sqrt(1.0 + eps_x), np.sqrt(1.0 + eps_y), omega_z))
  examples/13_two_component_bec.py:68: trap = HarmonicTrap(1.0)
  examples/13_two_component_bec.py:197: trap = HarmonicTrap((np.sqrt(1.0 + eps_x), np.sqrt(1.0 + eps_y)))
  examples/13_two_component_bec.py:198: (s1, s2), info = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G,
  tests/test_backends.py:78: '1d_driven': lambda: (Grid1D(128, -15.0, 15.0), DipoleDrive(HarmonicTrap(1.0), 0.4, 0.7), dict(order=4),
  tests/test_backends.py:80: '2d_gpe_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap(1.0),
  tests/test_backends.py:84: '2d_damped_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap((1.0, 1.1)),
  tests/test_backends.py:89: HarmonicTrap((1.0, 1.0, 1.5)),
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:128: b = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, rotation=0.3)
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:140: wf_n, info_n = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0)
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:162: gpu_solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, backend='cupy', **kwargs)
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_conjugate_gradient.py:14: (Grid1D(256, -12.0, 12.0), HarmonicTrap(1.0), {}, 0.5),
  tests/test_conjugate_gradient.py:16: (Grid1D(256, -12.0, 12.0), HarmonicTrap(2.0, m=0.5), dict(hbar=0.7, m=0.5), 0.7),
  tests/test_conjugate_gradient.py:17: (Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0), HarmonicTrap((1.0, 1.2, 1.4)), {}, 1.8),
  tests/test_conjugate_gradient.py:31: trap, g = HarmonicTrap((1.0, 1.2, 1.4)), 60.0
  tests/test_conjugate_gradient.py:44: wf, info = ground_state_pcg(grid, HarmonicTrap(1.0), initial=guess, nonlinearity=5.0, tol=1e-9)
  tests/test_conjugate_gradient.py:51: trap, g, Om = HarmonicTrap(1.0), 300.0, 0.8
  tests/test_conjugate_gradient.py:64: ground_state_pcg(Grid1D(64, -6.0, 6.0), HarmonicTrap(1.0), tol=1e-8,
  tests/test_gross_pitaevskii.py:42: trap = HarmonicTrap((1.0, 1.0))
  tests/test_gross_pitaevskii.py:46: shaken = HarmonicTrap((1.0, 1.0), center=(1.0, 0.0))
  tests/test_gross_pitaevskii.py:62: trap = HarmonicTrap(omegas)
  tests/test_gross_pitaevskii.py:74: trap = HarmonicTrap(1.0)
  tests/test_multicomponent.py:22: t1, t2 = HarmonicTrap((1.0, 1.2)), HarmonicTrap((1.3, 0.9))
  tests/test_multicomponent.py:35: trap, g = HarmonicTrap((1.0, 1.3)), 60.0
  tests/test_multicomponent.py:97: traps = (HarmonicTrap((1.0, 1.1)), HarmonicTrap((1.05, 0.95), center=(0.3, 0.0)))
  tests/test_multicomponent.py:110: trap = HarmonicTrap(1.0)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:110: trap = HarmonicTrap(1.0)
  tests/test_rotation.py:27: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=order, rotation=Om)
  tests/test_rotation.py:40: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:53: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:64: trap, Om = HarmonicTrap((1.0, 1.4)), 0.5
  tests/test_rotation.py:77: trap = HarmonicTrap(1.0)
  tests/test_rotation.py:93: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, damping=0.05, nonlinearity=5.0)
  tests/test_rotation.py:101: trap, g, Om = HarmonicTrap(1.0), 300.0, 0.8
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_rotation.py:138: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, rotation=0.6)
  tests/test_split_operator.py:93: pot = DipoleDrive(HarmonicTrap(omega), F0=F0, omega=Omega)
  tests/test_split_operator.py:107: a = DipoleDrive(HarmonicTrap(1.0), F0=0.3, omega=1.7)
  tests/test_split_operator.py:139: SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, imaginary_time=True)
  tests/test_stationary.py:16: energies, states = eigenstates(grid, HarmonicTrap(1.3), n_states=8, method='lanczos')
  tests/test_stationary.py:24: energies, _ = eigenstates(grid, HarmonicTrap((wx, wy)), n_states=6, method='lobpcg')
  tests/test_stationary.py:31: energies, states = eigenstates(grid, HarmonicTrap(1.0), n_states=4)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_stationary.py:48: wf, info = ground_state(grid, HarmonicTrap((1.0, 1.2, 1.4)), dtau=0.01)
  tests/test_stationary.py:56: pot = HarmonicTrap(1.0)
  tests/test_stationary.py:65: pot = HarmonicTrap(1.0)
  tests/test_stationary.py:75: trap, g = HarmonicTrap((1.0, 1.3)), 50.0
  tests/test_strongfield.py:100: a = dipole_acceleration(wf, HarmonicTrap(1.0), force=0.25)
EXT_OTHER (76):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/validation_suite.py:70: solver = SplitOperatorSolver(grid, DipoleDrive(HarmonicTrap(omega), F0, Omega), 0.01, order=4)
  benchmarks/validation_suite.py:84: pot = HarmonicTrap((1.0, 1.3, 0.8))
  benchmarks/validation_suite.py:119: E, _ = eigenstates(grid, HarmonicTrap(1.0), n_states=10, method='lanczos')
  benchmarks/validation_suite.py:124: E, _ = eigenstates(grid, HarmonicTrap(w), n_states=6, method='lobpcg')
  benchmarks/validation_suite.py:129: _, info = ground_state(grid, HarmonicTrap(w), dtau=0.01)
  benchmarks/validation_suite.py:137: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.05, order=4)
  benchmarks/validation_suite.py:171: trap, g = HarmonicTrap((1.0, 1.2, 1.4)), 60.0
  benchmarks/validation_suite.py:180: trap = HarmonicTrap((1.0, 1.3))
  benchmarks/validation_suite.py:192: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:202: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:284: trap, G = HarmonicTrap((1.0, 1.3)), 60.0
  benchmarks/validation_suite.py:301: states, _ = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G2, (a, b), dtau=0.005)
  benchmarks/validation_suite.py:303: V = sum(potential_energy_expectation(s, HarmonicTrap(1.0)) for s in states)
  benchmarks/validation_suite.py:316: trap, g = HarmonicTrap((1.0, 1.2, 1.4)), 60.0
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  examples/08_3d_bec_time_of_flight.py:74: trap = HarmonicTrap(omegas)
  examples/11_rotating_bec_vortex_lattice.py:68: trap = HarmonicTrap((np.sqrt(1.0 + eps_x), np.sqrt(1.0 + eps_y)))
  examples/11_rotating_bec_vortex_lattice.py:71: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, nonlinearity=g2)
  examples/11_rotating_bec_vortex_lattice.py:155: trap3 = HarmonicTrap((np.sqrt(1.0 + eps_x), np.sqrt(1.0 + eps_y), omega_z))
  examples/13_two_component_bec.py:68: trap = HarmonicTrap(1.0)
  examples/13_two_component_bec.py:197: trap = HarmonicTrap((np.sqrt(1.0 + eps_x), np.sqrt(1.0 + eps_y)))
  examples/13_two_component_bec.py:198: (s1, s2), info = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G,
  quantumlab/potentials/__init__.py:34: 'harmonic_trap':       HarmonicTrap,
  tests/test_backends.py:78: '1d_driven': lambda: (Grid1D(128, -15.0, 15.0), DipoleDrive(HarmonicTrap(1.0), 0.4, 0.7), dict(order=4),
  tests/test_backends.py:80: '2d_gpe_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap(1.0),
  tests/test_backends.py:84: '2d_damped_rotating': lambda: (Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0), HarmonicTrap((1.0, 1.1)),
  tests/test_backends.py:89: HarmonicTrap((1.0, 1.0, 1.5)),
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:128: b = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, rotation=0.3)
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:140: wf_n, info_n = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0)
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:162: gpu_solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, backend='cupy', **kwargs)
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_conjugate_gradient.py:14: (Grid1D(256, -12.0, 12.0), HarmonicTrap(1.0), {}, 0.5),
  tests/test_conjugate_gradient.py:16: (Grid1D(256, -12.0, 12.0), HarmonicTrap(2.0, m=0.5), dict(hbar=0.7, m=0.5), 0.7),
  tests/test_conjugate_gradient.py:17: (Grid3D(32, -7.0, 7.0, 32, -7.0, 7.0, 32, -7.0, 7.0), HarmonicTrap((1.0, 1.2, 1.4)), {}, 1.8),
  tests/test_conjugate_gradient.py:31: trap, g = HarmonicTrap((1.0, 1.2, 1.4)), 60.0
  tests/test_conjugate_gradient.py:44: wf, info = ground_state_pcg(grid, HarmonicTrap(1.0), initial=guess, nonlinearity=5.0, tol=1e-9)
  tests/test_conjugate_gradient.py:51: trap, g, Om = HarmonicTrap(1.0), 300.0, 0.8
  tests/test_conjugate_gradient.py:64: ground_state_pcg(Grid1D(64, -6.0, 6.0), HarmonicTrap(1.0), tol=1e-8,
  tests/test_gross_pitaevskii.py:42: trap = HarmonicTrap((1.0, 1.0))
  tests/test_gross_pitaevskii.py:46: shaken = HarmonicTrap((1.0, 1.0), center=(1.0, 0.0))
  tests/test_gross_pitaevskii.py:62: trap = HarmonicTrap(omegas)
  tests/test_gross_pitaevskii.py:74: trap = HarmonicTrap(1.0)
  tests/test_multicomponent.py:22: t1, t2 = HarmonicTrap((1.0, 1.2)), HarmonicTrap((1.3, 0.9))
  tests/test_multicomponent.py:35: trap, g = HarmonicTrap((1.0, 1.3)), 60.0
  tests/test_multicomponent.py:97: traps = (HarmonicTrap((1.0, 1.1)), HarmonicTrap((1.05, 0.95), center=(0.3, 0.0)))
  tests/test_multicomponent.py:110: trap = HarmonicTrap(1.0)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:64: assert isinstance(create_potential('harmonic_trap', omegas=1.0), HarmonicTrap)
  tests/test_new_potentials_and_observables.py:110: trap = HarmonicTrap(1.0)
  tests/test_rotation.py:27: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=order, rotation=Om)
  tests/test_rotation.py:40: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:53: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:64: trap, Om = HarmonicTrap((1.0, 1.4)), 0.5
  tests/test_rotation.py:77: trap = HarmonicTrap(1.0)
  tests/test_rotation.py:93: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, damping=0.05, nonlinearity=5.0)
  tests/test_rotation.py:101: trap, g, Om = HarmonicTrap(1.0), 300.0, 0.8
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_rotation.py:138: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, rotation=0.6)
  tests/test_split_operator.py:93: pot = DipoleDrive(HarmonicTrap(omega), F0=F0, omega=Omega)
  tests/test_split_operator.py:107: a = DipoleDrive(HarmonicTrap(1.0), F0=0.3, omega=1.7)
  tests/test_split_operator.py:139: SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, imaginary_time=True)
  tests/test_stationary.py:16: energies, states = eigenstates(grid, HarmonicTrap(1.3), n_states=8, method='lanczos')
  tests/test_stationary.py:24: energies, _ = eigenstates(grid, HarmonicTrap((wx, wy)), n_states=6, method='lobpcg')
  tests/test_stationary.py:31: energies, states = eigenstates(grid, HarmonicTrap(1.0), n_states=4)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_stationary.py:48: wf, info = ground_state(grid, HarmonicTrap((1.0, 1.2, 1.4)), dtau=0.01)
  tests/test_stationary.py:56: pot = HarmonicTrap(1.0)
  tests/test_stationary.py:65: pot = HarmonicTrap(1.0)
  tests/test_stationary.py:75: trap, g = HarmonicTrap((1.0, 1.3)), 50.0
  tests/test_strongfield.py:100: a = dipole_acceleration(wf, HarmonicTrap(1.0), force=0.25)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (15): benchmarks/gpu_split_operator.py:16(quantumlab.potentials), benchmarks/validation_suite.py:16(quantumlab.potentials), examples/08_3d_bec_time_of_flight.py:33(quantumlab.potentials), examples/11_rotating_bec_vortex_lattice.py:44(quantumlab.potentials), examples/13_two_component_bec.py:41(quantumlab.potentials), tests/test_backends.py:17(quantumlab.potentials), tests/test_conjugate_gradient.py:5(quantumlab.potentials), tests/test_gross_pitaevskii.py:5(quantumlab.potentials), tests/test_multicomponent.py:5(quantumlab.potentials), tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), tests/test_rotation.py:5(quantumlab.potentials), tests/test_split_operator.py:5(quantumlab.potentials), tests/test_stationary.py:4(quantumlab.potentials), tests/test_strongfield.py:5(quantumlab.potentials), quantumlab/potentials/__init__.py:12(quantumlab.potentials.traps)

## HarmonicTrap.__init__  [quantumlab/potentials/traps.py:22] (method)
SIG: def __init__(self, omegas, m: float = 1.0, center=None):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## HarmonicTrap.evaluate  [quantumlab/potentials/traps.py:27] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## InfiniteSquareWell  [quantumlab/potentials/wells.py:5] (class)
SIG: class InfiniteSquareWell(...):
EXT_CALLS (0):
EXT_OTHER (1):
  quantumlab/potentials/__init__.py:28: 'infinite_well':       InfiniteSquareWell,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/potentials/__init__.py:7(quantumlab.potentials.wells), tests/test_potentials.py:5(quantumlab.potentials.wells)

## InfiniteSquareWell.__init__  [quantumlab/potentials/wells.py:7] (method)
SIG: def __init__(self, width: float, position: float=0.0, V_inf: float=1000000000.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## InfiniteSquareWell.evaluate  [quantumlab/potentials/wells.py:12] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## FiniteSquareWell  [quantumlab/potentials/wells.py:20] (class)
SIG: class FiniteSquareWell(...):
EXT_CALLS (0):
EXT_OTHER (2):
  quantumlab/potentials/__init__.py:29: 'finite_well':         FiniteSquareWell,
  tests/test_potentials.py:54: assert isinstance(pot, FiniteSquareWell)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/potentials/__init__.py:7(quantumlab.potentials.wells), tests/test_potentials.py:5(quantumlab.potentials.wells)

## FiniteSquareWell.__init__  [quantumlab/potentials/wells.py:22] (method)
SIG: def __init__(self, V0: float, width: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## FiniteSquareWell.evaluate  [quantumlab/potentials/wells.py:27] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## DoubleWell  [quantumlab/potentials/wells.py:35] (class)
SIG: class DoubleWell(...):
EXT_CALLS (1):
  examples/03_double_well.py:31: potential = DoubleWell(V0, barrier_distance)
EXT_OTHER (2):
  examples/03_double_well.py:31: potential = DoubleWell(V0, barrier_distance)
  quantumlab/potentials/__init__.py:30: 'double_well':         DoubleWell,
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (3): examples/03_double_well.py:5(quantumlab.potentials.wells), quantumlab/potentials/__init__.py:7(quantumlab.potentials.wells), tests/test_potentials.py:5(quantumlab.potentials.wells)

## DoubleWell.__init__  [quantumlab/potentials/wells.py:37] (method)
SIG: def __init__(self, V0: float, barrier_distance: float, position: float=0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## DoubleWell.evaluate  [quantumlab/potentials/wells.py:42] (method)
SIG: def evaluate(self, grid) -> np.ndarray:
EXT_CALLS (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
EXT_OTHER (34):
  examples/08_3d_bec_time_of_flight.py:48: V = HarmonicTrap(omegas).evaluate(grid)
  quantumlab/observables/expectation.py:143: V = potential.evaluate(wf.grid)
  quantumlab/potentials/time_dependent.py:77: V_base = np.zeros(grid.shape) if self.base is None else self.base.evaluate(grid)
  quantumlab/solvers/multicomponent.py:71: np.asarray(p.evaluate(grid), dtype=float)) for p in self.potentials]
  quantumlab/solvers/split_operator.py:143: else np.asarray(potential.evaluate(grid), dtype=float))
  quantumlab/solvers/split_step_1d.py:10: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_2d.py:19: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d.py:41: self.V = self.potential.evaluate(self.grid)
  quantumlab/solvers/split_step_3d_gpu.py:60: self.V = cp.asarray(self.potential.evaluate(self.grid), dtype=cp.float64)
  quantumlab/solvers/split_step_3d_gpu.py:68: self.V = np.asarray(self.potential.evaluate(self.grid), dtype=np.float64)
  quantumlab/stationary/conjugate_gradient.py:51: V = np.zeros(grid.shape) if potential is None else np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/eigensolver.py:47: V = np.asarray(potential.evaluate(grid), dtype=float)
  quantumlab/stationary/imaginary_time.py:223: Vs = [np.zeros(grid.shape) if p is None else np.asarray(p.evaluate(grid), dtype=float) for p in potentials]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  quantumlab/visualization/animation.py:62: V = self.potential.evaluate(self.grid).T
  quantumlab/visualization/plots_1d.py:14: V = potential.evaluate(wf.grid)
  quantumlab/visualization/plots_2d.py:51: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/plots_2d.py:113: V = potential.evaluate(wf.grid).T
  quantumlab/visualization/volume_3d.py:112: V = potential.evaluate(grid)
  tests/test_3d_solver.py:156: V = barrier.evaluate(grid)
  tests/test_3d_solver.py:167: V = barrier.evaluate(grid)
  tests/test_new_potentials_and_observables.py:17: np.testing.assert_allclose(HarmonicTrap(1.7).evaluate(grid), HarmonicOscillator(1.7).evaluate(grid))
  tests/test_new_potentials_and_observables.py:22: V = HarmonicTrap((1.0, 2.0), center=(0.5, -1.0)).evaluate(grid)
  tests/test_new_potentials_and_observables.py:30: V = screen.evaluate(grid)
  tests/test_new_potentials_and_observables.py:43: V = ApertureScreen(V0=10.0, aperture='slit', n_apertures=3).evaluate(grid)
  tests/test_new_potentials_and_observables.py:49: V = StadiumBilliard(V0=30.0, radius=2.0, length=4.0, smoothing=0.1).evaluate(grid)
  tests/test_new_potentials_and_observables.py:59: V = CustomPotential(lambda x, y, z: x * y * z).evaluate(grid)
  tests/test_potentials.py:18: V = pot.evaluate(grid)
  tests/test_potentials.py:31: V = pot.evaluate(grid)
  tests/test_potentials.py:41: V = pot.evaluate(grid)
  tests/test_potentials.py:49: V = pot.evaluate(grid)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
  tests/test_strongfield.py:44: V = pot.evaluate(grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## create_potential  [quantumlab/potentials/__init__.py:41] (function)
SIG: def create_potential(name: str, **kwargs) -> Potential:
EXT_CALLS (7):
  quantumlab/runner.py:141: potential = create_potential(cfg["potential"]["type"], **cfg["potential"]["params"])
  tests/test_new_potentials_and_observables.py:64: assert isinstance(create_potential('harmonic_trap', omegas=1.0), HarmonicTrap)
  tests/test_new_potentials_and_observables.py:65: assert isinstance(create_potential('double_slit', V0=1.0), ApertureScreen)
  tests/test_new_potentials_and_observables.py:66: assert isinstance(create_potential('stadium', V0=1.0, radius=1.0, length=1.0), StadiumBilliard)
  tests/test_potentials.py:53: pot = create_potential('finite_well', V0=10.0, width=3.0)
  tests/test_potentials.py:58: create_potential('nonexistent_potential')
  tests/test_strongfield.py:37: assert isinstance(create_potential('soft_coulomb'), SoftCoulomb)
EXT_OTHER (7):
  quantumlab/runner.py:141: potential = create_potential(cfg["potential"]["type"], **cfg["potential"]["params"])
  tests/test_new_potentials_and_observables.py:64: assert isinstance(create_potential('harmonic_trap', omegas=1.0), HarmonicTrap)
  tests/test_new_potentials_and_observables.py:65: assert isinstance(create_potential('double_slit', V0=1.0), ApertureScreen)
  tests/test_new_potentials_and_observables.py:66: assert isinstance(create_potential('stadium', V0=1.0, radius=1.0, length=1.0), StadiumBilliard)
  tests/test_potentials.py:53: pot = create_potential('finite_well', V0=10.0, width=3.0)
  tests/test_potentials.py:58: create_potential('nonexistent_potential')
  tests/test_strongfield.py:37: assert isinstance(create_potential('soft_coulomb'), SoftCoulomb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): quantumlab/runner.py:14(quantumlab.potentials), tests/test_new_potentials_and_observables.py:5(quantumlab.potentials), tests/test_potentials.py:10(quantumlab.potentials), tests/test_strongfield.py:5(quantumlab.potentials)

## Solver  [quantumlab/solvers/base.py:3] (class)
SIG: class Solver(...):
EXT_CALLS (0):
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:42: class SplitOperatorSolver(Solver):
  quantumlab/solvers/split_step_1d.py:6: class SplitStep1DSolver(Solver):
  quantumlab/solvers/split_step_2d.py:6: class SplitStep2DSolver(Solver):
  quantumlab/solvers/split_step_3d.py:7: class SplitStep3DSolver(Solver):
  quantumlab/solvers/split_step_3d_gpu.py:25: class SplitStep3DGPU(Solver):
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (6): quantumlab/solvers/__init__.py:1(quantumlab.solvers.base), quantumlab/solvers/split_operator.py:33(quantumlab.solvers.base), quantumlab/solvers/split_step_1d.py:3(quantumlab.solvers.base), quantumlab/solvers/split_step_2d.py:3(quantumlab.solvers.base), quantumlab/solvers/split_step_3d.py:3(quantumlab.solvers.base), quantumlab/solvers/split_step_3d_gpu.py:11(quantumlab.solvers.base)

## Solver.__init__  [quantumlab/solvers/base.py:5] (method)
SIG: def __init__(self, grid, potential, dt: float, hbar: float=1.0, m: float=1.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Solver.step  [quantumlab/solvers/base.py:13] (method)
SIG: def step(self, wavefunction):
EXT_CALLS (39):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (91):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## Solver.backend  [quantumlab/solvers/base.py:17] (method)
SIG: def backend(self) -> str:
EXT_CALLS (0):
EXT_OTHER (37):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/perf_comparison.py:113: backend = "unavailable"
  benchmarks/perf_comparison.py:137: backend = solver_gpu.backend
  benchmarks/perf_comparison.py:138: if backend != "cupy":
  benchmarks/perf_comparison.py:144: "reason": f"solver_fell_back_to:{backend}",
  benchmarks/perf_comparison.py:149: backend = "unavailable"
  benchmarks/perf_comparison.py:155: run_status = "PASSED" if (status["state"] == "ok" and backend == "cupy") else "UNAVAILABLE"
  benchmarks/perf_comparison.py:168: 'backend': backend,
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/backends.py:69: if isinstance(backend, ArrayBackend):
  quantumlab/solvers/backends.py:70: return backend
  quantumlab/solvers/backends.py:71: if backend == 'numpy':
  quantumlab/solvers/backends.py:73: if backend == 'cupy':
  quantumlab/solvers/backends.py:77: if backend == 'auto':
  quantumlab/solvers/multicomponent.py:62: backend=backend, device_id=device_id, t0=t0)
  quantumlab/solvers/split_operator.py:129: self._be = get_backend(backend, workers=workers, device_id=device_id)
  quantumlab/stationary/imaginary_time.py:94: check_interval, hbar, m, orthogonal_to, workers, rotation, backend)
  quantumlab/stationary/imaginary_time.py:102: rotation=rotation, backend=backend)
  quantumlab/stationary/imaginary_time.py:220: rotation=rotation, backend=backend, workers=workers)
  tests/test_3d_gpu_solver.py:44: assert solver.backend == "cupy"
  tests/test_3d_gpu_solver.py:130: assert solver.backend == "scipy-cpu"
  tests/test_3d_gpu_solver.py:153: assert solver.backend in ("cupy", "scipy-cpu")
  tests/test_backends.py:57: backend = ArrayBackend(
  tests/test_backends.py:65: return backend, calls
  tests/test_backends.py:99: backend, calls = _strict_backend()
  tests/test_backends.py:101: dev_solver = SplitOperatorSolver(grid, potential, 0.01, backend=backend, **kwargs)
  tests/test_backends.py:103: assert dev_solver.backend == 'emulated-device'
  tests/test_backends.py:113: backend, calls = _strict_backend()
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:126: backend, _ = _strict_backend()
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:138: backend, _ = _strict_backend()
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:164: assert gpu_solver.backend == 'cupy'
  tests/test_backends.py:175: backend, calls = _strict_backend()
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_benchmark_failure_handling.py:197: backend = "cupy"
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## ArrayBackend  [quantumlab/solvers/backends.py:13] (class)
SIG: class ArrayBackend(...):
EXT_CALLS (1):
  tests/test_backends.py:57: backend = ArrayBackend(
EXT_OTHER (1):
  tests/test_backends.py:57: backend = ArrayBackend(
INT_CALLS (2): quantumlab/solvers/backends.py:33, quantumlab/solvers/backends.py:50
INT_OTHER (6): quantumlab/solvers/backends.py:31, quantumlab/solvers/backends.py:33, quantumlab/solvers/backends.py:43, quantumlab/solvers/backends.py:50, quantumlab/solvers/backends.py:60, quantumlab/solvers/backends.py:69
IMPORTS (1): tests/test_backends.py:19(quantumlab.solvers.backends)

## cupy_available  [quantumlab/solvers/backends.py:22] (function)
SIG: def cupy_available() -> bool:
EXT_CALLS (3):
  benchmarks/gpu_split_operator.py:40: gpu = cupy_available()
  tests/test_backends.py:149: if not cupy_available():
  tests/test_backends.py:155: @pytest.mark.skipif(not cupy_available(), reason='CuPy with a CUDA device is not available')
EXT_OTHER (3):
  benchmarks/gpu_split_operator.py:40: gpu = cupy_available()
  tests/test_backends.py:149: if not cupy_available():
  tests/test_backends.py:155: @pytest.mark.skipif(not cupy_available(), reason='CuPy with a CUDA device is not available')
INT_CALLS (2): quantumlab/solvers/backends.py:74, quantumlab/solvers/backends.py:78
INT_OTHER (2): quantumlab/solvers/backends.py:74, quantumlab/solvers/backends.py:78
IMPORTS (2): benchmarks/gpu_split_operator.py:18(quantumlab.solvers.backends), tests/test_backends.py:19(quantumlab.solvers.backends)

## numpy_backend  [quantumlab/solvers/backends.py:31] (function)
SIG: def numpy_backend(workers: int = -1) -> ArrayBackend:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/solvers/backends.py:72, quantumlab/solvers/backends.py:78
INT_OTHER (2): quantumlab/solvers/backends.py:72, quantumlab/solvers/backends.py:78
IMPORTS (0): 

## cupy_backend  [quantumlab/solvers/backends.py:43] (function)
SIG: def cupy_backend(device_id: int = 0) -> ArrayBackend:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/solvers/backends.py:76, quantumlab/solvers/backends.py:78
INT_OTHER (2): quantumlab/solvers/backends.py:76, quantumlab/solvers/backends.py:78
IMPORTS (0): 

## get_backend  [quantumlab/solvers/backends.py:60] (function)
SIG: def get_backend(backend='numpy', workers: int = -1, device_id: int = 0) -> ArrayBackend:
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:129: self._be = get_backend(backend, workers=workers, device_id=device_id)
  tests/test_backends.py:146: assert get_backend('numpy').name == 'scipy-cpu'
  tests/test_backends.py:148: get_backend('opencl')
  tests/test_backends.py:150: assert get_backend('auto').name == 'scipy-cpu'
  tests/test_backends.py:152: get_backend('cupy')
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:129: self._be = get_backend(backend, workers=workers, device_id=device_id)
  tests/test_backends.py:146: assert get_backend('numpy').name == 'scipy-cpu'
  tests/test_backends.py:148: get_backend('opencl')
  tests/test_backends.py:150: assert get_backend('auto').name == 'scipy-cpu'
  tests/test_backends.py:152: get_backend('cupy')
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): quantumlab/solvers/split_operator.py:34(quantumlab.solvers.backends), tests/test_backends.py:19(quantumlab.solvers.backends)

## CoupledGPESolver  [quantumlab/solvers/multicomponent.py:21] (class)
SIG: class CoupledGPESolver(...):
EXT_CALLS (15):
  benchmarks/validation_suite.py:261: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], 0.01, order=4)
  benchmarks/validation_suite.py:272: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], 0.01, order=4)
  examples/13_two_component_bec.py:120: solver = CoupledGPESolver(grid, (None, None), [[g, g12], [g12, g]], dt, order=2)
  examples/13_two_component_bec.py:201: solver = CoupledGPESolver(grid, (trap, trap), G, 0.005, rotation=Om, damping=gamma)
  quantumlab/stationary/imaginary_time.py:219: solver = CoupledGPESolver(grid, potentials, g, dtau, hbar, m, order=2, imaginary_time=True,
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_multicomponent.py:25: c = CoupledGPESolver(grid, (t1, t2), [[20.0, 0.0], [0.0, 35.0]], 0.01, order=4, rotation=0.3).evolve((a, b), 60)
  tests/test_multicomponent.py:69: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], dt, order=4)
  tests/test_multicomponent.py:83: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], dt, order=4)
  tests/test_multicomponent.py:101: out = CoupledGPESolver(grid, traps, G, 0.005, order=4).evolve(state, 300)
  tests/test_multicomponent.py:133: CoupledGPESolver(grid, (None, None), [[1.0, 0.5], [0.4, 1.0]], 0.01)       # not symmetric
  tests/test_multicomponent.py:135: CoupledGPESolver(grid, (None, None), [[1.0]], 0.01)                        # wrong shape
  tests/test_multicomponent.py:137: CoupledGPESolver(grid, (DipoleDrive(None, 1.0, 1.0), None), np.eye(2), 0.01)
  tests/test_multicomponent.py:138: solver = CoupledGPESolver(grid, (None, None), np.eye(2), 0.01)
EXT_OTHER (15):
  benchmarks/validation_suite.py:261: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], 0.01, order=4)
  benchmarks/validation_suite.py:272: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], 0.01, order=4)
  examples/13_two_component_bec.py:120: solver = CoupledGPESolver(grid, (None, None), [[g, g12], [g12, g]], dt, order=2)
  examples/13_two_component_bec.py:201: solver = CoupledGPESolver(grid, (trap, trap), G, 0.005, rotation=Om, damping=gamma)
  quantumlab/stationary/imaginary_time.py:219: solver = CoupledGPESolver(grid, potentials, g, dtau, hbar, m, order=2, imaginary_time=True,
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_multicomponent.py:25: c = CoupledGPESolver(grid, (t1, t2), [[20.0, 0.0], [0.0, 35.0]], 0.01, order=4, rotation=0.3).evolve((a, b), 60)
  tests/test_multicomponent.py:69: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], dt, order=4)
  tests/test_multicomponent.py:83: solver = CoupledGPESolver(box, (None, None), [[g, g12], [g12, g]], dt, order=4)
  tests/test_multicomponent.py:101: out = CoupledGPESolver(grid, traps, G, 0.005, order=4).evolve(state, 300)
  tests/test_multicomponent.py:133: CoupledGPESolver(grid, (None, None), [[1.0, 0.5], [0.4, 1.0]], 0.01)       # not symmetric
  tests/test_multicomponent.py:135: CoupledGPESolver(grid, (None, None), [[1.0]], 0.01)                        # wrong shape
  tests/test_multicomponent.py:137: CoupledGPESolver(grid, (DipoleDrive(None, 1.0, 1.0), None), np.eye(2), 0.01)
  tests/test_multicomponent.py:138: solver = CoupledGPESolver(grid, (None, None), np.eye(2), 0.01)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): benchmarks/validation_suite.py:246(quantumlab.solvers.multicomponent), examples/13_two_component_bec.py:42(quantumlab.solvers.multicomponent), quantumlab/stationary/imaginary_time.py:217(quantumlab.solvers.multicomponent), tests/test_backends.py:169(quantumlab.solvers.multicomponent), tests/test_multicomponent.py:7(quantumlab.solvers.multicomponent)

## CoupledGPESolver.__init__  [quantumlab/solvers/multicomponent.py:38] (method)
SIG: def __init__(self, grid, potentials: Sequence, couplings, dt: float, hbar: float = 1.0,
                 m: float = 1.0, order: int = 2, imaginary_time: bool = False, rotation: float = 0.0,
                 damping: float = 0.0, workers: int = -1, backend='numpy', device_id: int = 0,
                 t0: float = 0.0):
EXT_CALLS (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (5):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## CoupledGPESolver.t  [quantumlab/solvers/multicomponent.py:74] (method)
SIG: def t(self) -> float:
EXT_CALLS (0):
EXT_OTHER (116):
  benchmarks/validation_suite.py:43: sigma0, k0, t = 1.0, 1.0, 5.0
  benchmarks/validation_suite.py:45: sigma_t = sigma0 * np.sqrt(1 + (t / (2 * sigma0 ** 2)) ** 2)
  benchmarks/validation_suite.py:46: exact = np.exp(-(grid.x - k0 * t) ** 2 / (2 * sigma_t ** 2)) / np.sqrt(2 * np.pi * sigma_t ** 2)
  benchmarks/validation_suite.py:75: t = solver.t
  benchmarks/validation_suite.py:76: x_cl = F0 / (omega ** 2 - Omega ** 2) * (np.sin(Omega * t) - Omega / omega * np.sin(omega * t))
  benchmarks/validation_suite.py:164: exact = (1.0 / np.cosh(grid.x + 20.0 - 1.5 * solver.t)) ** 2
  benchmarks/validation_suite.py:196: t = solver.t
  benchmarks/validation_suite.py:197: err = max(err, abs(position_expectation(wf) - x0 * np.cos(t) * np.cos(Om * t)),
  benchmarks/validation_suite.py:198: abs(y_expectation(wf) + x0 * np.cos(t) * np.sin(Om * t)))
  benchmarks/validation_suite.py:205: '|C(t) − exact|', abs(C - np.exp(-1j * (2.0 - Om) * solver.t)), 1e-7)
  benchmarks/validation_suite.py:224: callback=lambda n, t, wf: acc.append(sf.dipole_acceleration(wf, atom, laser.force(t))))
  benchmarks/validation_suite.py:236: t = np.arange(1, len(acc) + 1) * 0.05
  benchmarks/validation_suite.py:237: m = (t > 8 * period) & (t < 12 * period)
  benchmarks/validation_suite.py:240: spacing = np.diff(t[m][peaks]) / period
  benchmarks/validation_suite.py:265: err = max(err, abs(spin(state, k) - 4e-6 * np.cos(omega * solver.t)) / 4e-6)
  benchmarks/validation_suite.py:273: state, t, amp = seeded(k), [], []
  benchmarks/validation_suite.py:276: t.append(solver.t)
  benchmarks/validation_suite.py:278: t, amp = np.array(t), np.array(amp)
  benchmarks/validation_suite.py:279: rate = np.polyfit(t[amp > 1.2e-4], np.log(amp[amp > 1.2e-4]), 1)[0]
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:45: times.append(t)
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:44: times.append(t)
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/07_3d_double_slit.py:81: anim.add_frame(wf.psi * display_gain, solver.t)
  examples/07_3d_double_slit.py:85: anim.add_frame(wf.psi * display_gain, solver.t)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:112: anim.add_frame(wf.psi, solver.t)
  examples/08_3d_bec_time_of_flight.py:113: times.append(solver.t)
  examples/08_3d_bec_time_of_flight.py:117: times_html.append(solver.t)
  examples/08_3d_bec_time_of_flight.py:126: renderer.save(wf.psi, 'output/08_bec_tof_final.png', t=solver.t, elev=25, azim=-30,
  examples/09_soliton_collision.py:39: times.append(solver.t)
  examples/11_rotating_bec_vortex_lattice.py:102: times.append(solver.t)
  examples/11_rotating_bec_vortex_lattice.py:107: title.set_text(f'Vortex-lattice formation in a rotating BEC    t = {solver.t:6.1f}')
  examples/11_rotating_bec_vortex_lattice.py:110: print(f'    t = {solver.t:6.1f}   vortices = {counts[-1]:3d}   ⟨L_z⟩/N = {Lz[-1]:6.2f}')
  examples/11_rotating_bec_vortex_lattice.py:127: ax.set_title(f'Vortex lattice at t = {solver.t:.0f}\nspacing {a:.2f} ± {a_std:.2f} (Feynman {a_feynman:.2f})',
  examples/12_high_harmonic_generation.py:68: acc.append(dipole_acceleration(wf, atom, laser.force(t)))
  examples/12_high_harmonic_generation.py:101: t, acc, dens, laser, wf_end = run(intensity, states[0], atom, record_density=True)
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/12_high_harmonic_generation.py:189: m = (t > 8 * period) & (t < 12 * period)
  examples/12_high_harmonic_generation.py:192: spacing = np.diff(t[m][pk]) / period
  examples/12_high_harmonic_generation.py:197: ax.plot(t[m] / period, P[m] / P[m].max(), color='#ffb000', lw=1.4, label='attosecond bursts (H11–H21)')
  examples/12_high_harmonic_generation.py:198: F = np.array([laser.force(x) for x in t[m]])
  examples/12_high_harmonic_generation.py:199: ax.plot(t[m] / period, 0.5 * F / np.abs(F).max() - 0.6, color='#7fd4ff', lw=1.0, label='laser field (scaled)')
  examples/12_high_harmonic_generation.py:210: td = t[9::10][:len(dens)]
  examples/12_high_harmonic_generation.py:218: ax2.plot(t / period, [laser.force(x_) for x_ in t], color='#7fd4ff', lw=0.8)
  examples/13_two_component_bec.py:144: times.append(solver.t)
  examples/13_two_component_bec.py:153: title.set_text(f'Phase separation of a binary BEC   t = {solver.t:5.1f}')
  examples/13_two_component_bec.py:219: title.set_text(f'Two-component vortex lattices   t = {solver.t:5.1f}')
  examples/13_two_component_bec.py:224: print(f'    t = {solver.t:5.1f}: vortices {n1v} + {n2v}, '
  quantumlab/potentials/time_dependent.py:68: env = 1.0 if self.envelope is None else float(self.envelope(t))
  quantumlab/potentials/time_dependent.py:69: return self.F0 * env * np.sin(self.omega * t + self.phase)
  quantumlab/potentials/time_dependent.py:84: return V_base - self.force(t) * r_axis
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/time_dependent.py:102: if t <= 0.0 or t >= duration:
  quantumlab/potentials/time_dependent.py:104: return float(np.sin(np.pi * t / duration) ** 2)
  quantumlab/potentials/time_dependent.py:118: if t <= 0.0 or t >= duration:
  quantumlab/potentials/time_dependent.py:120: if t < ramp:
  quantumlab/potentials/time_dependent.py:121: return float(np.sin(0.5 * np.pi * t / ramp) ** 2)
  quantumlab/potentials/time_dependent.py:122: if t > duration - ramp:
  quantumlab/potentials/time_dependent.py:123: return float(np.sin(0.5 * np.pi * (duration - t) / ramp) ** 2)
  quantumlab/solvers/split_operator.py:191: return np.asarray(self.potential.evaluate_at(self.grid, t), dtype=float)
  quantumlab/solvers/split_operator.py:196: return self._be.to_device(self.potential_at(t))
  quantumlab/solvers/split_operator.py:204: V = self._potential_on_device(t)
  quantumlab/solvers/split_operator.py:239: psi = self._potential_half_step(psi, t, w)
  quantumlab/solvers/split_operator.py:241: return self._potential_half_step(psi, t + w * self.dt, w)
  quantumlab/solvers/split_operator.py:251: t = self.t
  quantumlab/solvers/split_operator.py:253: psi = self._strang(psi, t, w)
  quantumlab/solvers/split_operator.py:254: t += w * self.dt
  quantumlab/solvers/split_operator.py:283: callback(n, self.t, self._download(psi))
  quantumlab/strongfield.py:93: t = np.arange(len(s)) * dt
  quantumlab/strongfield.py:94: times = t[::max(1, len(s) // 400)] if times is None else np.asarray(times, dtype=float)
  quantumlab/strongfield.py:101: ts = t[lo:hi]
  quantumlab/visualization/plots_2d.py:105: for i, (wf, t) in enumerate(zip(wf_list, times)):
  quantumlab/visualization/plots_2d.py:118: ax.set_title(f't = {t:.2f}', fontsize=9, color=text_color)
  quantumlab/visualization/volume_3d.py:230: self._time.set_text('' if t is None else f't = {t:6.2f}')
  quantumlab/visualization/volume_3d.py:235: fig = self.draw(psi, t=t, elev=elev, azim=azim, title=title, note=note, overlays=overlays)
  quantumlab/visualization/volume_3d.py:294: self.renderer.draw(psi, t=t, elev=elev, azim=azim, title=self.title, note=self.note,
  quantumlab/visualization/volume_3d.py:323: for i, (psi, t) in enumerate(zip(snapshots, times)):
  quantumlab/visualization/volume_3d.py:324: anim.add_frame(psi, t)
  quantumlab/visualization/volume_3d.py:361: frames = [go.Frame(data=[mesh_for(s)], name=f'{t:.2f}') for s, t in zip(snapshots, times)]
  tests/test_gross_pitaevskii.py:26: t = solver.t
  tests/test_gross_pitaevskii.py:27: exact = (kappa / np.cosh(kappa * (grid.x - x0 - v * t))) ** 2
  tests/test_multicomponent.py:73: assert _spin_amplitude(state, k) == pytest.approx(4e-6 * np.cos(omega * solver.t), abs=1e-12)
  tests/test_multicomponent.py:85: t, amp = [], []
  tests/test_multicomponent.py:88: t.append(solver.t)
  tests/test_multicomponent.py:90: t, amp = np.array(t), np.array(amp)
  tests/test_multicomponent.py:92: assert np.polyfit(t[m], np.log(amp[m]), 1)[0] == pytest.approx(gamma, rel=1e-3)
  tests/test_rotation.py:30: t = solver.t
  tests/test_rotation.py:31: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=tol)
  tests/test_rotation.py:32: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=tol)
  tests/test_rotation.py:42: t = solver.t
  tests/test_rotation.py:43: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=1e-7)
  tests/test_rotation.py:44: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=1e-7)
  tests/test_rotation.py:57: assert np.angle(C * np.exp(1j * (2.0 - Om) * solver.t)) == pytest.approx(0.0, abs=1e-7)
  tests/test_split_operator.py:60: assert solver.t == pytest.approx(3.0)
  tests/test_split_operator.py:99: t = solver.t
  tests/test_split_operator.py:100: x_cl = F0 / (omega ** 2 - Omega ** 2) * (np.sin(Omega * t) - (Omega / omega) * np.sin(omega * t))
  tests/test_split_operator.py:108: b = TimeDependentCustomPotential(lambda x, t: 0.5 * x ** 2 - 0.3 * np.sin(1.7 * t) * x)
  tests/test_split_operator.py:116: sigma0, k0, t = 1.0, 1.0, 5.0
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:119: sigma_t = sigma0 * np.sqrt(1.0 + (t / (2.0 * sigma0 ** 2)) ** 2)
  tests/test_split_operator.py:120: exact = np.exp(-(grid.x - k0 * t) ** 2 / (2.0 * sigma_t ** 2)) / np.sqrt(2.0 * np.pi * sigma_t ** 2)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
  tests/test_strongfield.py:52: assert [env(t) for t in (-1.0, 0.0, 10.0, 11.0)] == [0.0, 0.0, 0.0, 0.0]
  tests/test_strongfield.py:62: t = np.arange(0, 400 * 2 * np.pi / w0, dt)
  tests/test_strongfield.py:63: sig = np.sin(w0 * t) + 1e-3 * np.sin(5 * w0 * t)
  tests/test_strongfield.py:74: t = np.arange(0, 1000, dt)
  tests/test_strongfield.py:75: sig = np.exp(-((t - 600) / 20) ** 2) * np.cos(9 * w0 * t)
  tests/test_strongfield.py:86: t = np.arange(0, 20 * 2 * np.pi / w0, dt)
  tests/test_strongfield.py:87: sig = sum(np.cos(q * w0 * t) for q in range(11, 22, 2))
  tests/test_strongfield.py:90: mid = (t > 5 * period) & (t < 15 * period)
  tests/test_strongfield.py:91: peaks = t[mid][np.r_[False, (P[mid][1:-1] > P[mid][:-2]) & (P[mid][1:-1] > P[mid][2:]), False]
INT_CALLS (0): 
INT_OTHER (1): quantumlab/solvers/multicomponent.py:143
IMPORTS (0): 

## CoupledGPESolver.backend  [quantumlab/solvers/multicomponent.py:78] (method)
SIG: def backend(self) -> str:
EXT_CALLS (0):
EXT_OTHER (36):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/perf_comparison.py:113: backend = "unavailable"
  benchmarks/perf_comparison.py:137: backend = solver_gpu.backend
  benchmarks/perf_comparison.py:138: if backend != "cupy":
  benchmarks/perf_comparison.py:144: "reason": f"solver_fell_back_to:{backend}",
  benchmarks/perf_comparison.py:149: backend = "unavailable"
  benchmarks/perf_comparison.py:155: run_status = "PASSED" if (status["state"] == "ok" and backend == "cupy") else "UNAVAILABLE"
  benchmarks/perf_comparison.py:168: 'backend': backend,
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/backends.py:69: if isinstance(backend, ArrayBackend):
  quantumlab/solvers/backends.py:70: return backend
  quantumlab/solvers/backends.py:71: if backend == 'numpy':
  quantumlab/solvers/backends.py:73: if backend == 'cupy':
  quantumlab/solvers/backends.py:77: if backend == 'auto':
  quantumlab/solvers/split_operator.py:129: self._be = get_backend(backend, workers=workers, device_id=device_id)
  quantumlab/stationary/imaginary_time.py:94: check_interval, hbar, m, orthogonal_to, workers, rotation, backend)
  quantumlab/stationary/imaginary_time.py:102: rotation=rotation, backend=backend)
  quantumlab/stationary/imaginary_time.py:220: rotation=rotation, backend=backend, workers=workers)
  tests/test_3d_gpu_solver.py:44: assert solver.backend == "cupy"
  tests/test_3d_gpu_solver.py:130: assert solver.backend == "scipy-cpu"
  tests/test_3d_gpu_solver.py:153: assert solver.backend in ("cupy", "scipy-cpu")
  tests/test_backends.py:57: backend = ArrayBackend(
  tests/test_backends.py:65: return backend, calls
  tests/test_backends.py:99: backend, calls = _strict_backend()
  tests/test_backends.py:101: dev_solver = SplitOperatorSolver(grid, potential, 0.01, backend=backend, **kwargs)
  tests/test_backends.py:103: assert dev_solver.backend == 'emulated-device'
  tests/test_backends.py:113: backend, calls = _strict_backend()
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:126: backend, _ = _strict_backend()
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:138: backend, _ = _strict_backend()
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:164: assert gpu_solver.backend == 'cupy'
  tests/test_backends.py:175: backend, calls = _strict_backend()
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_benchmark_failure_handling.py:197: backend = "cupy"
INT_CALLS (0): 
INT_OTHER (1): quantumlab/solvers/multicomponent.py:62
IMPORTS (0): 

## CoupledGPESolver._densities  [quantumlab/solvers/multicomponent.py:81] (method)
SIG: def _densities(self, psis, rescale: bool):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (3): quantumlab/solvers/multicomponent.py:97, quantumlab/solvers/multicomponent.py:99, quantumlab/solvers/multicomponent.py:101
INT_OTHER (3): quantumlab/solvers/multicomponent.py:97, quantumlab/solvers/multicomponent.py:99, quantumlab/solvers/multicomponent.py:101
IMPORTS (0): 

## CoupledGPESolver._effective_potentials  [quantumlab/solvers/multicomponent.py:88] (method)
SIG: def _effective_potentials(self, rhos):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (3): quantumlab/solvers/multicomponent.py:97, quantumlab/solvers/multicomponent.py:99, quantumlab/solvers/multicomponent.py:101
INT_OTHER (3): quantumlab/solvers/multicomponent.py:97, quantumlab/solvers/multicomponent.py:99, quantumlab/solvers/multicomponent.py:101
IMPORTS (0): 

## CoupledGPESolver._potential_half_step  [quantumlab/solvers/multicomponent.py:93] (method)
SIG: def _potential_half_step(self, psis, w):
EXT_CALLS (2):
  quantumlab/solvers/split_operator.py:239: psi = self._potential_half_step(psi, t, w)
  quantumlab/solvers/split_operator.py:241: return self._potential_half_step(psi, t + w * self.dt, w)
EXT_OTHER (2):
  quantumlab/solvers/split_operator.py:239: psi = self._potential_half_step(psi, t, w)
  quantumlab/solvers/split_operator.py:241: return self._potential_half_step(psi, t + w * self.dt, w)
INT_CALLS (2): quantumlab/solvers/multicomponent.py:111, quantumlab/solvers/multicomponent.py:113
INT_OTHER (2): quantumlab/solvers/multicomponent.py:111, quantumlab/solvers/multicomponent.py:113
IMPORTS (0): 

## CoupledGPESolver._norm  [quantumlab/solvers/multicomponent.py:104] (method)
SIG: def _norm(self, psi) -> float:
EXT_CALLS (2):
  quantumlab/solvers/split_operator.py:250: self._target_norm = 1.0 if self.imaginary_time else self._norm(psi)
  quantumlab/solvers/split_operator.py:256: norm = self._norm(psi)
EXT_OTHER (2):
  quantumlab/solvers/split_operator.py:250: self._target_norm = 1.0 if self.imaginary_time else self._norm(psi)
  quantumlab/solvers/split_operator.py:256: norm = self._norm(psi)
INT_CALLS (2): quantumlab/solvers/multicomponent.py:109, quantumlab/solvers/multicomponent.py:117
INT_OTHER (2): quantumlab/solvers/multicomponent.py:109, quantumlab/solvers/multicomponent.py:117
IMPORTS (0): 

## CoupledGPESolver._advance  [quantumlab/solvers/multicomponent.py:107] (method)
SIG: def _advance(self, psis):
EXT_CALLS (2):
  quantumlab/solvers/split_operator.py:271: return self._download(self._advance(self._upload(wavefunction)))
  quantumlab/solvers/split_operator.py:281: psi = self._advance(psi)
EXT_OTHER (2):
  quantumlab/solvers/split_operator.py:271: return self._download(self._advance(self._upload(wavefunction)))
  quantumlab/solvers/split_operator.py:281: psi = self._advance(psi)
INT_CALLS (2): quantumlab/solvers/multicomponent.py:132, quantumlab/solvers/multicomponent.py:141
INT_OTHER (2): quantumlab/solvers/multicomponent.py:132, quantumlab/solvers/multicomponent.py:141
IMPORTS (0): 

## CoupledGPESolver._upload  [quantumlab/solvers/multicomponent.py:123] (method)
SIG: def _upload(self, states):
EXT_CALLS (2):
  quantumlab/solvers/split_operator.py:271: return self._download(self._advance(self._upload(wavefunction)))
  quantumlab/solvers/split_operator.py:279: psi = self._upload(wavefunction)
EXT_OTHER (2):
  quantumlab/solvers/split_operator.py:271: return self._download(self._advance(self._upload(wavefunction)))
  quantumlab/solvers/split_operator.py:279: psi = self._upload(wavefunction)
INT_CALLS (2): quantumlab/solvers/multicomponent.py:132, quantumlab/solvers/multicomponent.py:139
INT_OTHER (2): quantumlab/solvers/multicomponent.py:132, quantumlab/solvers/multicomponent.py:139
IMPORTS (0): 

## CoupledGPESolver._download  [quantumlab/solvers/multicomponent.py:128] (method)
SIG: def _download(self, psis):
EXT_CALLS (3):
  quantumlab/solvers/split_operator.py:271: return self._download(self._advance(self._upload(wavefunction)))
  quantumlab/solvers/split_operator.py:283: callback(n, self.t, self._download(psi))
  quantumlab/solvers/split_operator.py:284: return self._download(psi)
EXT_OTHER (3):
  quantumlab/solvers/split_operator.py:271: return self._download(self._advance(self._upload(wavefunction)))
  quantumlab/solvers/split_operator.py:283: callback(n, self.t, self._download(psi))
  quantumlab/solvers/split_operator.py:284: return self._download(psi)
INT_CALLS (3): quantumlab/solvers/multicomponent.py:132, quantumlab/solvers/multicomponent.py:143, quantumlab/solvers/multicomponent.py:144
INT_OTHER (3): quantumlab/solvers/multicomponent.py:132, quantumlab/solvers/multicomponent.py:143, quantumlab/solvers/multicomponent.py:144
IMPORTS (0): 

## CoupledGPESolver.step  [quantumlab/solvers/multicomponent.py:131] (method)
SIG: def step(self, states):
EXT_CALLS (39):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (91):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## CoupledGPESolver.evolve  [quantumlab/solvers/multicomponent.py:134] (method)
SIG: def evolve(self, states, n_steps: int, callback=None, callback_interval: int = 1):
EXT_CALLS (55):
  benchmarks/gpu_split_operator.py:26: solver.evolve(wf0, 2)                        # warm-up (FFT plans, CUDA kernels)
  benchmarks/gpu_split_operator.py:28: wf = solver.evolve(wf0, steps)               # includes the final device → host copy
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:57: return SplitOperatorSolver(grid, pot, dt, order=order).evolve(wf0, int(round(2.0 / dt))).psi
  benchmarks/validation_suite.py:74: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:88: wf = SplitOperatorSolver(grid, pot, 0.01, order=4).evolve(wf, n_steps)
  benchmarks/validation_suite.py:163: wf = solver.evolve(WaveFunction1D(grid, psi), 4000)
  benchmarks/validation_suite.py:195: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:203: C = autocorrelation(wf0.psi, solver.evolve(wf0, 500).psi, grid)
  benchmarks/validation_suite.py:223: solver.evolve(states[0], int(round(20 * period / 0.05)),
  benchmarks/validation_suite.py:264: state = solver.evolve(state, 500)
  benchmarks/validation_suite.py:275: state = solver.evolve(state, 100)
  examples/09_soliton_collision.py:37: wf = solver.evolve(wf, record_every)
  examples/12_high_harmonic_generation.py:72: wf = solver.evolve(wf0, int(round(duration / DT)), callback=record)
  examples/13_two_component_bec.py:142: state = solver.evolve(state, 20)
  examples/13_two_component_bec.py:217: state = solver.evolve(state, 250)
  quantumlab/stationary/imaginary_time.py:130: wf = solver.evolve(wf, check_interval)
  quantumlab/stationary/imaginary_time.py:229: states = solver.evolve(states, check_interval)
  tests/test_backends.py:100: ref = SplitOperatorSolver(grid, potential, 0.01, backend='numpy', **kwargs).evolve(wf0, 30)
  tests/test_backends.py:102: out = dev_solver.evolve(wf0, 30)
  tests/test_backends.py:115: ref = SplitOperatorSolver(grid, None, 0.01, absorber=abl).evolve(wf0, 40)
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:163: gpu = gpu_solver.evolve(wf0, 50)
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_conjugate_gradient.py:54: lattice = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om).evolve(seed, 1500)
  tests/test_gross_pitaevskii.py:25: wf = solver.evolve(wf, 4000)
  tests/test_gross_pitaevskii.py:36: wf = SplitOperatorSolver(grid, None, 0.01, nonlinearity=0.0).evolve(wf, 1000)
  tests/test_gross_pitaevskii.py:48: wf = SplitOperatorSolver(grid, shaken, 0.005, nonlinearity=g, order=4).evolve(wf0, 400)
  tests/test_multicomponent.py:25: c = CoupledGPESolver(grid, (t1, t2), [[20.0, 0.0], [0.0, 35.0]], 0.01, order=4, rotation=0.3).evolve((a, b), 60)
  tests/test_multicomponent.py:26: r1 = SplitOperatorSolver(grid, t1, 0.01, order=4, nonlinearity=20.0, rotation=0.3).evolve(a, 60)
  tests/test_multicomponent.py:27: r2 = SplitOperatorSolver(grid, t2, 0.01, order=4, nonlinearity=35.0, rotation=0.3).evolve(b, 60)
  tests/test_multicomponent.py:72: state = solver.evolve(state, 500)
  tests/test_multicomponent.py:87: state = solver.evolve(state, 100)
  tests/test_multicomponent.py:101: out = CoupledGPESolver(grid, traps, G, 0.005, order=4).evolve(state, 300)
  tests/test_rotation.py:29: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:41: wf = solver.evolve(wf, 300)
  tests/test_rotation.py:54: wf = solver.evolve(wf0, 500)
  tests/test_rotation.py:71: wf = SplitOperatorSolver(grid, trap, 0.005, order=4, rotation=Om).evolve(wf, 600)
  tests/test_rotation.py:82: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:94: wf = solver.evolve(wf, 200)
  tests/test_rotation.py:105: lattice = solver.evolve(WaveFunction2D(grid, seed), 3000)
  tests/test_split_operator.py:56: wf = solver.evolve(wf, 300)
  tests/test_split_operator.py:72: return SplitOperatorSolver(grid, pot, dt, order=o).evolve(wf0, int(round(T / dt))).psi
  tests/test_split_operator.py:84: ref = SplitOperatorSolver(grid, pot, 0.0005, order=4).evolve(wf0, 4000).psi
  tests/test_split_operator.py:85: e2 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=2).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:86: e4 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=4).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:98: wf = solver.evolve(wf, 100)
  tests/test_split_operator.py:109: wa = SplitOperatorSolver(grid, a, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:110: wb = SplitOperatorSolver(grid, b, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:127: free = SplitOperatorSolver(grid, None, 0.01).evolve(wf, 1000)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
EXT_OTHER (55):
  benchmarks/gpu_split_operator.py:26: solver.evolve(wf0, 2)                        # warm-up (FFT plans, CUDA kernels)
  benchmarks/gpu_split_operator.py:28: wf = solver.evolve(wf0, steps)               # includes the final device → host copy
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:57: return SplitOperatorSolver(grid, pot, dt, order=order).evolve(wf0, int(round(2.0 / dt))).psi
  benchmarks/validation_suite.py:74: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:88: wf = SplitOperatorSolver(grid, pot, 0.01, order=4).evolve(wf, n_steps)
  benchmarks/validation_suite.py:163: wf = solver.evolve(WaveFunction1D(grid, psi), 4000)
  benchmarks/validation_suite.py:195: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:203: C = autocorrelation(wf0.psi, solver.evolve(wf0, 500).psi, grid)
  benchmarks/validation_suite.py:223: solver.evolve(states[0], int(round(20 * period / 0.05)),
  benchmarks/validation_suite.py:264: state = solver.evolve(state, 500)
  benchmarks/validation_suite.py:275: state = solver.evolve(state, 100)
  examples/09_soliton_collision.py:37: wf = solver.evolve(wf, record_every)
  examples/12_high_harmonic_generation.py:72: wf = solver.evolve(wf0, int(round(duration / DT)), callback=record)
  examples/13_two_component_bec.py:142: state = solver.evolve(state, 20)
  examples/13_two_component_bec.py:217: state = solver.evolve(state, 250)
  quantumlab/stationary/imaginary_time.py:130: wf = solver.evolve(wf, check_interval)
  quantumlab/stationary/imaginary_time.py:229: states = solver.evolve(states, check_interval)
  tests/test_backends.py:100: ref = SplitOperatorSolver(grid, potential, 0.01, backend='numpy', **kwargs).evolve(wf0, 30)
  tests/test_backends.py:102: out = dev_solver.evolve(wf0, 30)
  tests/test_backends.py:115: ref = SplitOperatorSolver(grid, None, 0.01, absorber=abl).evolve(wf0, 40)
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:163: gpu = gpu_solver.evolve(wf0, 50)
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_conjugate_gradient.py:54: lattice = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om).evolve(seed, 1500)
  tests/test_gross_pitaevskii.py:25: wf = solver.evolve(wf, 4000)
  tests/test_gross_pitaevskii.py:36: wf = SplitOperatorSolver(grid, None, 0.01, nonlinearity=0.0).evolve(wf, 1000)
  tests/test_gross_pitaevskii.py:48: wf = SplitOperatorSolver(grid, shaken, 0.005, nonlinearity=g, order=4).evolve(wf0, 400)
  tests/test_multicomponent.py:25: c = CoupledGPESolver(grid, (t1, t2), [[20.0, 0.0], [0.0, 35.0]], 0.01, order=4, rotation=0.3).evolve((a, b), 60)
  tests/test_multicomponent.py:26: r1 = SplitOperatorSolver(grid, t1, 0.01, order=4, nonlinearity=20.0, rotation=0.3).evolve(a, 60)
  tests/test_multicomponent.py:27: r2 = SplitOperatorSolver(grid, t2, 0.01, order=4, nonlinearity=35.0, rotation=0.3).evolve(b, 60)
  tests/test_multicomponent.py:72: state = solver.evolve(state, 500)
  tests/test_multicomponent.py:87: state = solver.evolve(state, 100)
  tests/test_multicomponent.py:101: out = CoupledGPESolver(grid, traps, G, 0.005, order=4).evolve(state, 300)
  tests/test_rotation.py:29: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:41: wf = solver.evolve(wf, 300)
  tests/test_rotation.py:54: wf = solver.evolve(wf0, 500)
  tests/test_rotation.py:71: wf = SplitOperatorSolver(grid, trap, 0.005, order=4, rotation=Om).evolve(wf, 600)
  tests/test_rotation.py:82: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:94: wf = solver.evolve(wf, 200)
  tests/test_rotation.py:105: lattice = solver.evolve(WaveFunction2D(grid, seed), 3000)
  tests/test_split_operator.py:56: wf = solver.evolve(wf, 300)
  tests/test_split_operator.py:72: return SplitOperatorSolver(grid, pot, dt, order=o).evolve(wf0, int(round(T / dt))).psi
  tests/test_split_operator.py:84: ref = SplitOperatorSolver(grid, pot, 0.0005, order=4).evolve(wf0, 4000).psi
  tests/test_split_operator.py:85: e2 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=2).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:86: e4 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=4).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:98: wf = solver.evolve(wf, 100)
  tests/test_split_operator.py:109: wa = SplitOperatorSolver(grid, a, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:110: wb = SplitOperatorSolver(grid, b, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:127: free = SplitOperatorSolver(grid, None, 0.01).evolve(wf, 1000)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitOperatorSolver  [quantumlab/solvers/split_operator.py:42] (class)
SIG: class SplitOperatorSolver(...):
EXT_CALLS (60):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:57: return SplitOperatorSolver(grid, pot, dt, order=order).evolve(wf0, int(round(2.0 / dt))).psi
  benchmarks/validation_suite.py:70: solver = SplitOperatorSolver(grid, DipoleDrive(HarmonicTrap(omega), F0, Omega), 0.01, order=4)
  benchmarks/validation_suite.py:88: wf = SplitOperatorSolver(grid, pot, 0.01, order=4).evolve(wf, n_steps)
  benchmarks/validation_suite.py:137: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.05, order=4)
  benchmarks/validation_suite.py:162: solver = SplitOperatorSolver(grid, None, 0.005, nonlinearity=-1.0, order=4)
  benchmarks/validation_suite.py:192: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:202: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:221: solver = SplitOperatorSolver(grid, laser, 0.05, order=4, absorber=AbsorbingBoundaryLayer(grid, 40.0))
  examples/07_3d_double_slit.py:60: solver = SplitOperatorSolver(grid, screen, dt, order=2, absorber=AbsorbingBoundaryLayer(grid, 3.0))
  examples/08_3d_bec_time_of_flight.py:99: solver = SplitOperatorSolver(grid, None, dt, nonlinearity=g, order=2)
  examples/09_soliton_collision.py:34: solver = SplitOperatorSolver(grid, None, dt, nonlinearity=g, order=4)
  examples/11_rotating_bec_vortex_lattice.py:76: solver = SplitOperatorSolver(grid, trap, dt, nonlinearity=g2, rotation=Om, damping=gamma)
  examples/12_high_harmonic_generation.py:64: solver = SplitOperatorSolver(GRID, laser, DT, order=4, absorber=AbsorbingBoundaryLayer(GRID, 40.0))
  quantumlab/runner.py:106: return SplitOperatorSolver(
  quantumlab/solvers/multicomponent.py:60: self._engine = SplitOperatorSolver(grid, None, dt, hbar, m, order=order, imaginary_time=imaginary_time,
  quantumlab/stationary/imaginary_time.py:100: solver = SplitOperatorSolver(grid, potential, dtau, hbar, m, order=2,
  tests/test_backends.py:100: ref = SplitOperatorSolver(grid, potential, 0.01, backend='numpy', **kwargs).evolve(wf0, 30)
  tests/test_backends.py:101: dev_solver = SplitOperatorSolver(grid, potential, 0.01, backend=backend, **kwargs)
  tests/test_backends.py:115: ref = SplitOperatorSolver(grid, None, 0.01, absorber=abl).evolve(wf0, 40)
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:128: b = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, rotation=0.3)
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:162: gpu_solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, backend='cupy', **kwargs)
  tests/test_conjugate_gradient.py:54: lattice = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om).evolve(seed, 1500)
  tests/test_gross_pitaevskii.py:24: solver = SplitOperatorSolver(grid, None, 0.005, nonlinearity=-1.0, order=order)
  tests/test_gross_pitaevskii.py:36: wf = SplitOperatorSolver(grid, None, 0.01, nonlinearity=0.0).evolve(wf, 1000)
  tests/test_gross_pitaevskii.py:48: wf = SplitOperatorSolver(grid, shaken, 0.005, nonlinearity=g, order=4).evolve(wf0, 400)
  tests/test_multicomponent.py:26: r1 = SplitOperatorSolver(grid, t1, 0.01, order=4, nonlinearity=20.0, rotation=0.3).evolve(a, 60)
  tests/test_multicomponent.py:27: r2 = SplitOperatorSolver(grid, t2, 0.01, order=4, nonlinearity=35.0, rotation=0.3).evolve(b, 60)
  tests/test_new_potentials_and_observables.py:112: solver = SplitOperatorSolver(grid, trap, 0.05, order=4)
  tests/test_rotation.py:27: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=order, rotation=Om)
  tests/test_rotation.py:40: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:53: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:71: wf = SplitOperatorSolver(grid, trap, 0.005, order=4, rotation=Om).evolve(wf, 600)
  tests/test_rotation.py:79: solver = SplitOperatorSolver(grid, trap, 0.01, damping=0.3)
  tests/test_rotation.py:93: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, damping=0.05, nonlinearity=5.0)
  tests/test_rotation.py:104: solver = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om)
  tests/test_rotation.py:116: SplitOperatorSolver(Grid1D(32, -4.0, 4.0), None, 0.01, rotation=0.5)
  tests/test_rotation.py:119: SplitOperatorSolver(grid, None, 0.01, damping=-0.1)
  tests/test_rotation.py:121: SplitOperatorSolver(grid, None, 0.01, damping=0.1, order=4)
  tests/test_rotation.py:123: SplitOperatorSolver(grid, None, 0.01, damping=0.1, imaginary_time=True)
  tests/test_split_operator.py:40: b = SplitOperatorSolver(grid, pot, 0.02, order=2)
  tests/test_split_operator.py:54: solver = SplitOperatorSolver(grid, pot, 0.01, order=order)
  tests/test_split_operator.py:72: return SplitOperatorSolver(grid, pot, dt, order=o).evolve(wf0, int(round(T / dt))).psi
  tests/test_split_operator.py:84: ref = SplitOperatorSolver(grid, pot, 0.0005, order=4).evolve(wf0, 4000).psi
  tests/test_split_operator.py:85: e2 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=2).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:86: e4 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=4).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:96: solver = SplitOperatorSolver(grid, pot, 0.01, order=4)
  tests/test_split_operator.py:109: wa = SplitOperatorSolver(grid, a, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:110: wb = SplitOperatorSolver(grid, b, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:127: free = SplitOperatorSolver(grid, None, 0.01).evolve(wf, 1000)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
  tests/test_split_operator.py:137: SplitOperatorSolver(grid, None, 0.01, order=3)
  tests/test_split_operator.py:139: SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, imaginary_time=True)
  tests/test_split_operator.py:141: SplitOperatorSolver(grid, DipoleDrive(None, 1.0, 1.0), 0.01, imaginary_time=True)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
EXT_OTHER (60):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:57: return SplitOperatorSolver(grid, pot, dt, order=order).evolve(wf0, int(round(2.0 / dt))).psi
  benchmarks/validation_suite.py:70: solver = SplitOperatorSolver(grid, DipoleDrive(HarmonicTrap(omega), F0, Omega), 0.01, order=4)
  benchmarks/validation_suite.py:88: wf = SplitOperatorSolver(grid, pot, 0.01, order=4).evolve(wf, n_steps)
  benchmarks/validation_suite.py:137: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.05, order=4)
  benchmarks/validation_suite.py:162: solver = SplitOperatorSolver(grid, None, 0.005, nonlinearity=-1.0, order=4)
  benchmarks/validation_suite.py:192: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:202: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  benchmarks/validation_suite.py:221: solver = SplitOperatorSolver(grid, laser, 0.05, order=4, absorber=AbsorbingBoundaryLayer(grid, 40.0))
  examples/07_3d_double_slit.py:60: solver = SplitOperatorSolver(grid, screen, dt, order=2, absorber=AbsorbingBoundaryLayer(grid, 3.0))
  examples/08_3d_bec_time_of_flight.py:99: solver = SplitOperatorSolver(grid, None, dt, nonlinearity=g, order=2)
  examples/09_soliton_collision.py:34: solver = SplitOperatorSolver(grid, None, dt, nonlinearity=g, order=4)
  examples/11_rotating_bec_vortex_lattice.py:76: solver = SplitOperatorSolver(grid, trap, dt, nonlinearity=g2, rotation=Om, damping=gamma)
  examples/12_high_harmonic_generation.py:64: solver = SplitOperatorSolver(GRID, laser, DT, order=4, absorber=AbsorbingBoundaryLayer(GRID, 40.0))
  quantumlab/runner.py:106: return SplitOperatorSolver(
  quantumlab/solvers/multicomponent.py:60: self._engine = SplitOperatorSolver(grid, None, dt, hbar, m, order=order, imaginary_time=imaginary_time,
  quantumlab/stationary/imaginary_time.py:100: solver = SplitOperatorSolver(grid, potential, dtau, hbar, m, order=2,
  tests/test_backends.py:100: ref = SplitOperatorSolver(grid, potential, 0.01, backend='numpy', **kwargs).evolve(wf0, 30)
  tests/test_backends.py:101: dev_solver = SplitOperatorSolver(grid, potential, 0.01, backend=backend, **kwargs)
  tests/test_backends.py:115: ref = SplitOperatorSolver(grid, None, 0.01, absorber=abl).evolve(wf0, 40)
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:128: b = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, rotation=0.3)
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:162: gpu_solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, backend='cupy', **kwargs)
  tests/test_conjugate_gradient.py:54: lattice = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om).evolve(seed, 1500)
  tests/test_gross_pitaevskii.py:24: solver = SplitOperatorSolver(grid, None, 0.005, nonlinearity=-1.0, order=order)
  tests/test_gross_pitaevskii.py:36: wf = SplitOperatorSolver(grid, None, 0.01, nonlinearity=0.0).evolve(wf, 1000)
  tests/test_gross_pitaevskii.py:48: wf = SplitOperatorSolver(grid, shaken, 0.005, nonlinearity=g, order=4).evolve(wf0, 400)
  tests/test_multicomponent.py:26: r1 = SplitOperatorSolver(grid, t1, 0.01, order=4, nonlinearity=20.0, rotation=0.3).evolve(a, 60)
  tests/test_multicomponent.py:27: r2 = SplitOperatorSolver(grid, t2, 0.01, order=4, nonlinearity=35.0, rotation=0.3).evolve(b, 60)
  tests/test_new_potentials_and_observables.py:112: solver = SplitOperatorSolver(grid, trap, 0.05, order=4)
  tests/test_rotation.py:27: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=order, rotation=Om)
  tests/test_rotation.py:40: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:53: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, rotation=Om)
  tests/test_rotation.py:71: wf = SplitOperatorSolver(grid, trap, 0.005, order=4, rotation=Om).evolve(wf, 600)
  tests/test_rotation.py:79: solver = SplitOperatorSolver(grid, trap, 0.01, damping=0.3)
  tests/test_rotation.py:93: solver = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, damping=0.05, nonlinearity=5.0)
  tests/test_rotation.py:104: solver = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om)
  tests/test_rotation.py:116: SplitOperatorSolver(Grid1D(32, -4.0, 4.0), None, 0.01, rotation=0.5)
  tests/test_rotation.py:119: SplitOperatorSolver(grid, None, 0.01, damping=-0.1)
  tests/test_rotation.py:121: SplitOperatorSolver(grid, None, 0.01, damping=0.1, order=4)
  tests/test_rotation.py:123: SplitOperatorSolver(grid, None, 0.01, damping=0.1, imaginary_time=True)
  tests/test_split_operator.py:40: b = SplitOperatorSolver(grid, pot, 0.02, order=2)
  tests/test_split_operator.py:54: solver = SplitOperatorSolver(grid, pot, 0.01, order=order)
  tests/test_split_operator.py:72: return SplitOperatorSolver(grid, pot, dt, order=o).evolve(wf0, int(round(T / dt))).psi
  tests/test_split_operator.py:84: ref = SplitOperatorSolver(grid, pot, 0.0005, order=4).evolve(wf0, 4000).psi
  tests/test_split_operator.py:85: e2 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=2).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:86: e4 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=4).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:96: solver = SplitOperatorSolver(grid, pot, 0.01, order=4)
  tests/test_split_operator.py:109: wa = SplitOperatorSolver(grid, a, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:110: wb = SplitOperatorSolver(grid, b, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:127: free = SplitOperatorSolver(grid, None, 0.01).evolve(wf, 1000)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
  tests/test_split_operator.py:137: SplitOperatorSolver(grid, None, 0.01, order=3)
  tests/test_split_operator.py:139: SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, order=4, imaginary_time=True)
  tests/test_split_operator.py:141: SplitOperatorSolver(grid, DipoleDrive(None, 1.0, 1.0), 0.01, imaginary_time=True)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (17): benchmarks/gpu_split_operator.py:17(quantumlab.solvers.split_operator), benchmarks/validation_suite.py:20(quantumlab.solvers.split_operator), examples/07_3d_double_slit.py:24(quantumlab.solvers.split_operator), examples/08_3d_bec_time_of_flight.py:35(quantumlab.solvers.split_operator), examples/09_soliton_collision.py:21(quantumlab.solvers.split_operator), examples/11_rotating_bec_vortex_lattice.py:46(quantumlab.solvers.split_operator), examples/12_high_harmonic_generation.py:43(quantumlab.solvers.split_operator), quantumlab/runner.py:17(quantumlab.solvers.split_operator), quantumlab/solvers/multicomponent.py:17(quantumlab.solvers.split_operator), quantumlab/stationary/imaginary_time.py:12(quantumlab.solvers.split_operator), tests/test_backends.py:18(quantumlab.solvers.split_operator), tests/test_conjugate_gradient.py:6(quantumlab.solvers.split_operator), tests/test_gross_pitaevskii.py:6(quantumlab.solvers.split_operator), tests/test_multicomponent.py:6(quantumlab.solvers.split_operator), tests/test_new_potentials_and_observables.py:9(quantumlab.solvers.split_operator), tests/test_rotation.py:6(quantumlab.solvers.split_operator), tests/test_split_operator.py:10(quantumlab.solvers.split_operator)

## SplitOperatorSolver.__init__  [quantumlab/solvers/split_operator.py:98] (method)
SIG: def __init__(self, grid, potential, dt: float, hbar: float = 1.0, m: float = 1.0,
                 order: int = 2, nonlinearity: float = 0.0, imaginary_time: bool = False,
                 absorber=None, workers: int = -1, t0: float = 0.0,
                 rotation: float = 0.0, damping: float = 0.0,
                 backend='numpy', device_id: int = 0):
EXT_CALLS (4):
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (4):
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (1): quantumlab/solvers/split_operator.py:103
INT_OTHER (1): quantumlab/solvers/split_operator.py:103
IMPORTS (0): 

## SplitOperatorSolver.update_operators  [quantumlab/solvers/split_operator.py:148] (method)
SIG: def update_operators(self):
EXT_CALLS (4):
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
EXT_OTHER (4):
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
INT_CALLS (1): quantumlab/solvers/split_operator.py:146
INT_OTHER (1): quantumlab/solvers/split_operator.py:146
IMPORTS (0): 

## SplitOperatorSolver._rotating_kinetic_parts  [quantumlab/solvers/split_operator.py:166] (method)
SIG: def _rotating_kinetic_parts(self):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/solvers/split_operator.py:160
INT_OTHER (1): quantumlab/solvers/split_operator.py:160
IMPORTS (0): 

## SplitOperatorSolver.t  [quantumlab/solvers/split_operator.py:179] (method)
SIG: def t(self) -> float:
EXT_CALLS (0):
EXT_OTHER (108):
  benchmarks/validation_suite.py:43: sigma0, k0, t = 1.0, 1.0, 5.0
  benchmarks/validation_suite.py:45: sigma_t = sigma0 * np.sqrt(1 + (t / (2 * sigma0 ** 2)) ** 2)
  benchmarks/validation_suite.py:46: exact = np.exp(-(grid.x - k0 * t) ** 2 / (2 * sigma_t ** 2)) / np.sqrt(2 * np.pi * sigma_t ** 2)
  benchmarks/validation_suite.py:75: t = solver.t
  benchmarks/validation_suite.py:76: x_cl = F0 / (omega ** 2 - Omega ** 2) * (np.sin(Omega * t) - Omega / omega * np.sin(omega * t))
  benchmarks/validation_suite.py:164: exact = (1.0 / np.cosh(grid.x + 20.0 - 1.5 * solver.t)) ** 2
  benchmarks/validation_suite.py:196: t = solver.t
  benchmarks/validation_suite.py:197: err = max(err, abs(position_expectation(wf) - x0 * np.cos(t) * np.cos(Om * t)),
  benchmarks/validation_suite.py:198: abs(y_expectation(wf) + x0 * np.cos(t) * np.sin(Om * t)))
  benchmarks/validation_suite.py:205: '|C(t) − exact|', abs(C - np.exp(-1j * (2.0 - Om) * solver.t)), 1e-7)
  benchmarks/validation_suite.py:224: callback=lambda n, t, wf: acc.append(sf.dipole_acceleration(wf, atom, laser.force(t))))
  benchmarks/validation_suite.py:236: t = np.arange(1, len(acc) + 1) * 0.05
  benchmarks/validation_suite.py:237: m = (t > 8 * period) & (t < 12 * period)
  benchmarks/validation_suite.py:240: spacing = np.diff(t[m][peaks]) / period
  benchmarks/validation_suite.py:265: err = max(err, abs(spin(state, k) - 4e-6 * np.cos(omega * solver.t)) / 4e-6)
  benchmarks/validation_suite.py:273: state, t, amp = seeded(k), [], []
  benchmarks/validation_suite.py:276: t.append(solver.t)
  benchmarks/validation_suite.py:278: t, amp = np.array(t), np.array(amp)
  benchmarks/validation_suite.py:279: rate = np.polyfit(t[amp > 1.2e-4], np.log(amp[amp > 1.2e-4]), 1)[0]
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:45: times.append(t)
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:44: times.append(t)
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/07_3d_double_slit.py:81: anim.add_frame(wf.psi * display_gain, solver.t)
  examples/07_3d_double_slit.py:85: anim.add_frame(wf.psi * display_gain, solver.t)
  examples/07_3d_double_slit.py:88: best_T, psi_analysis, t_analysis = T, wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:90: psi_showcase, t_showcase = wf.psi.copy(), solver.t
  examples/07_3d_double_slit.py:93: print(f'  t = {solver.t:5.2f}   norm = {wf.norm():.4f}   transmitted = {T:.4f}')
  examples/08_3d_bec_time_of_flight.py:112: anim.add_frame(wf.psi, solver.t)
  examples/08_3d_bec_time_of_flight.py:113: times.append(solver.t)
  examples/08_3d_bec_time_of_flight.py:117: times_html.append(solver.t)
  examples/08_3d_bec_time_of_flight.py:126: renderer.save(wf.psi, 'output/08_bec_tof_final.png', t=solver.t, elev=25, azim=-30,
  examples/09_soliton_collision.py:39: times.append(solver.t)
  examples/11_rotating_bec_vortex_lattice.py:102: times.append(solver.t)
  examples/11_rotating_bec_vortex_lattice.py:107: title.set_text(f'Vortex-lattice formation in a rotating BEC    t = {solver.t:6.1f}')
  examples/11_rotating_bec_vortex_lattice.py:110: print(f'    t = {solver.t:6.1f}   vortices = {counts[-1]:3d}   ⟨L_z⟩/N = {Lz[-1]:6.2f}')
  examples/11_rotating_bec_vortex_lattice.py:127: ax.set_title(f'Vortex lattice at t = {solver.t:.0f}\nspacing {a:.2f} ± {a_std:.2f} (Feynman {a_feynman:.2f})',
  examples/12_high_harmonic_generation.py:68: acc.append(dipole_acceleration(wf, atom, laser.force(t)))
  examples/12_high_harmonic_generation.py:101: t, acc, dens, laser, wf_end = run(intensity, states[0], atom, record_density=True)
  examples/12_high_harmonic_generation.py:102: print(f'Propagated {len(t)} steps; probability left in the box: {wf_end.norm():.3f} '
  examples/12_high_harmonic_generation.py:189: m = (t > 8 * period) & (t < 12 * period)
  examples/12_high_harmonic_generation.py:192: spacing = np.diff(t[m][pk]) / period
  examples/12_high_harmonic_generation.py:197: ax.plot(t[m] / period, P[m] / P[m].max(), color='#ffb000', lw=1.4, label='attosecond bursts (H11–H21)')
  examples/12_high_harmonic_generation.py:198: F = np.array([laser.force(x) for x in t[m]])
  examples/12_high_harmonic_generation.py:199: ax.plot(t[m] / period, 0.5 * F / np.abs(F).max() - 0.6, color='#7fd4ff', lw=1.0, label='laser field (scaled)')
  examples/12_high_harmonic_generation.py:210: td = t[9::10][:len(dens)]
  examples/12_high_harmonic_generation.py:218: ax2.plot(t / period, [laser.force(x_) for x_ in t], color='#7fd4ff', lw=0.8)
  examples/13_two_component_bec.py:144: times.append(solver.t)
  examples/13_two_component_bec.py:153: title.set_text(f'Phase separation of a binary BEC   t = {solver.t:5.1f}')
  examples/13_two_component_bec.py:219: title.set_text(f'Two-component vortex lattices   t = {solver.t:5.1f}')
  examples/13_two_component_bec.py:224: print(f'    t = {solver.t:5.1f}: vortices {n1v} + {n2v}, '
  quantumlab/potentials/time_dependent.py:68: env = 1.0 if self.envelope is None else float(self.envelope(t))
  quantumlab/potentials/time_dependent.py:69: return self.F0 * env * np.sin(self.omega * t + self.phase)
  quantumlab/potentials/time_dependent.py:84: return V_base - self.force(t) * r_axis
  quantumlab/potentials/time_dependent.py:96: return np.broadcast_to(self.func(*coordinates(grid), t), grid.shape).astype(float)
  quantumlab/potentials/time_dependent.py:102: if t <= 0.0 or t >= duration:
  quantumlab/potentials/time_dependent.py:104: return float(np.sin(np.pi * t / duration) ** 2)
  quantumlab/potentials/time_dependent.py:118: if t <= 0.0 or t >= duration:
  quantumlab/potentials/time_dependent.py:120: if t < ramp:
  quantumlab/potentials/time_dependent.py:121: return float(np.sin(0.5 * np.pi * t / ramp) ** 2)
  quantumlab/potentials/time_dependent.py:122: if t > duration - ramp:
  quantumlab/potentials/time_dependent.py:123: return float(np.sin(0.5 * np.pi * (duration - t) / ramp) ** 2)
  quantumlab/solvers/multicomponent.py:143: callback(n, self.t, self._download(psis))
  quantumlab/strongfield.py:93: t = np.arange(len(s)) * dt
  quantumlab/strongfield.py:94: times = t[::max(1, len(s) // 400)] if times is None else np.asarray(times, dtype=float)
  quantumlab/strongfield.py:101: ts = t[lo:hi]
  quantumlab/visualization/plots_2d.py:105: for i, (wf, t) in enumerate(zip(wf_list, times)):
  quantumlab/visualization/plots_2d.py:118: ax.set_title(f't = {t:.2f}', fontsize=9, color=text_color)
  quantumlab/visualization/volume_3d.py:230: self._time.set_text('' if t is None else f't = {t:6.2f}')
  quantumlab/visualization/volume_3d.py:235: fig = self.draw(psi, t=t, elev=elev, azim=azim, title=title, note=note, overlays=overlays)
  quantumlab/visualization/volume_3d.py:294: self.renderer.draw(psi, t=t, elev=elev, azim=azim, title=self.title, note=self.note,
  quantumlab/visualization/volume_3d.py:323: for i, (psi, t) in enumerate(zip(snapshots, times)):
  quantumlab/visualization/volume_3d.py:324: anim.add_frame(psi, t)
  quantumlab/visualization/volume_3d.py:361: frames = [go.Frame(data=[mesh_for(s)], name=f'{t:.2f}') for s, t in zip(snapshots, times)]
  tests/test_gross_pitaevskii.py:26: t = solver.t
  tests/test_gross_pitaevskii.py:27: exact = (kappa / np.cosh(kappa * (grid.x - x0 - v * t))) ** 2
  tests/test_multicomponent.py:73: assert _spin_amplitude(state, k) == pytest.approx(4e-6 * np.cos(omega * solver.t), abs=1e-12)
  tests/test_multicomponent.py:85: t, amp = [], []
  tests/test_multicomponent.py:88: t.append(solver.t)
  tests/test_multicomponent.py:90: t, amp = np.array(t), np.array(amp)
  tests/test_multicomponent.py:92: assert np.polyfit(t[m], np.log(amp[m]), 1)[0] == pytest.approx(gamma, rel=1e-3)
  tests/test_rotation.py:30: t = solver.t
  tests/test_rotation.py:31: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=tol)
  tests/test_rotation.py:32: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=tol)
  tests/test_rotation.py:42: t = solver.t
  tests/test_rotation.py:43: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=1e-7)
  tests/test_rotation.py:44: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=1e-7)
  tests/test_rotation.py:57: assert np.angle(C * np.exp(1j * (2.0 - Om) * solver.t)) == pytest.approx(0.0, abs=1e-7)
  tests/test_split_operator.py:60: assert solver.t == pytest.approx(3.0)
  tests/test_split_operator.py:99: t = solver.t
  tests/test_split_operator.py:100: x_cl = F0 / (omega ** 2 - Omega ** 2) * (np.sin(Omega * t) - (Omega / omega) * np.sin(omega * t))
  tests/test_split_operator.py:108: b = TimeDependentCustomPotential(lambda x, t: 0.5 * x ** 2 - 0.3 * np.sin(1.7 * t) * x)
  tests/test_split_operator.py:116: sigma0, k0, t = 1.0, 1.0, 5.0
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:119: sigma_t = sigma0 * np.sqrt(1.0 + (t / (2.0 * sigma0 ** 2)) ** 2)
  tests/test_split_operator.py:120: exact = np.exp(-(grid.x - k0 * t) ** 2 / (2.0 * sigma_t ** 2)) / np.sqrt(2.0 * np.pi * sigma_t ** 2)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
  tests/test_strongfield.py:52: assert [env(t) for t in (-1.0, 0.0, 10.0, 11.0)] == [0.0, 0.0, 0.0, 0.0]
  tests/test_strongfield.py:62: t = np.arange(0, 400 * 2 * np.pi / w0, dt)
  tests/test_strongfield.py:63: sig = np.sin(w0 * t) + 1e-3 * np.sin(5 * w0 * t)
  tests/test_strongfield.py:74: t = np.arange(0, 1000, dt)
  tests/test_strongfield.py:75: sig = np.exp(-((t - 600) / 20) ** 2) * np.cos(9 * w0 * t)
  tests/test_strongfield.py:86: t = np.arange(0, 20 * 2 * np.pi / w0, dt)
  tests/test_strongfield.py:87: sig = sum(np.cos(q * w0 * t) for q in range(11, 22, 2))
  tests/test_strongfield.py:90: mid = (t > 5 * period) & (t < 15 * period)
  tests/test_strongfield.py:91: peaks = t[mid][np.r_[False, (P[mid][1:-1] > P[mid][:-2]) & (P[mid][1:-1] > P[mid][2:]), False]
INT_CALLS (0): 
INT_OTHER (9): quantumlab/solvers/split_operator.py:191, quantumlab/solvers/split_operator.py:196, quantumlab/solvers/split_operator.py:204, quantumlab/solvers/split_operator.py:239, quantumlab/solvers/split_operator.py:241, quantumlab/solvers/split_operator.py:251, quantumlab/solvers/split_operator.py:253, quantumlab/solvers/split_operator.py:254, quantumlab/solvers/split_operator.py:283
IMPORTS (0): 

## SplitOperatorSolver.backend  [quantumlab/solvers/split_operator.py:184] (method)
SIG: def backend(self) -> str:
EXT_CALLS (0):
EXT_OTHER (36):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/perf_comparison.py:113: backend = "unavailable"
  benchmarks/perf_comparison.py:137: backend = solver_gpu.backend
  benchmarks/perf_comparison.py:138: if backend != "cupy":
  benchmarks/perf_comparison.py:144: "reason": f"solver_fell_back_to:{backend}",
  benchmarks/perf_comparison.py:149: backend = "unavailable"
  benchmarks/perf_comparison.py:155: run_status = "PASSED" if (status["state"] == "ok" and backend == "cupy") else "UNAVAILABLE"
  benchmarks/perf_comparison.py:168: 'backend': backend,
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/backends.py:69: if isinstance(backend, ArrayBackend):
  quantumlab/solvers/backends.py:70: return backend
  quantumlab/solvers/backends.py:71: if backend == 'numpy':
  quantumlab/solvers/backends.py:73: if backend == 'cupy':
  quantumlab/solvers/backends.py:77: if backend == 'auto':
  quantumlab/solvers/multicomponent.py:62: backend=backend, device_id=device_id, t0=t0)
  quantumlab/stationary/imaginary_time.py:94: check_interval, hbar, m, orthogonal_to, workers, rotation, backend)
  quantumlab/stationary/imaginary_time.py:102: rotation=rotation, backend=backend)
  quantumlab/stationary/imaginary_time.py:220: rotation=rotation, backend=backend, workers=workers)
  tests/test_3d_gpu_solver.py:44: assert solver.backend == "cupy"
  tests/test_3d_gpu_solver.py:130: assert solver.backend == "scipy-cpu"
  tests/test_3d_gpu_solver.py:153: assert solver.backend in ("cupy", "scipy-cpu")
  tests/test_backends.py:57: backend = ArrayBackend(
  tests/test_backends.py:65: return backend, calls
  tests/test_backends.py:99: backend, calls = _strict_backend()
  tests/test_backends.py:101: dev_solver = SplitOperatorSolver(grid, potential, 0.01, backend=backend, **kwargs)
  tests/test_backends.py:103: assert dev_solver.backend == 'emulated-device'
  tests/test_backends.py:113: backend, calls = _strict_backend()
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:126: backend, _ = _strict_backend()
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:138: backend, _ = _strict_backend()
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:164: assert gpu_solver.backend == 'cupy'
  tests/test_backends.py:175: backend, calls = _strict_backend()
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_benchmark_failure_handling.py:197: backend = "cupy"
INT_CALLS (0): 
INT_OTHER (1): quantumlab/solvers/split_operator.py:129
IMPORTS (0): 

## SplitOperatorSolver.potential_at  [quantumlab/solvers/split_operator.py:187] (method)
SIG: def potential_at(self, t: float) -> np.ndarray:
EXT_CALLS (1):
  quantumlab/stationary/imaginary_time.py:105: V = solver.potential_at(0.0)
EXT_OTHER (1):
  quantumlab/stationary/imaginary_time.py:105: V = solver.potential_at(0.0)
INT_CALLS (1): quantumlab/solvers/split_operator.py:196
INT_OTHER (1): quantumlab/solvers/split_operator.py:196
IMPORTS (0): 

## SplitOperatorSolver._potential_on_device  [quantumlab/solvers/split_operator.py:193] (method)
SIG: def _potential_on_device(self, t):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/solvers/split_operator.py:204
INT_OTHER (1): quantumlab/solvers/split_operator.py:204
IMPORTS (0): 

## SplitOperatorSolver._potential_half_step  [quantumlab/solvers/split_operator.py:198] (method)
SIG: def _potential_half_step(self, psi, t, w):
EXT_CALLS (2):
  quantumlab/solvers/multicomponent.py:111: psis = self._potential_half_step(psis, w)
  quantumlab/solvers/multicomponent.py:113: psis = self._potential_half_step(psis, w)
EXT_OTHER (2):
  quantumlab/solvers/multicomponent.py:111: psis = self._potential_half_step(psis, w)
  quantumlab/solvers/multicomponent.py:113: psis = self._potential_half_step(psis, w)
INT_CALLS (2): quantumlab/solvers/split_operator.py:239, quantumlab/solvers/split_operator.py:241
INT_OTHER (2): quantumlab/solvers/split_operator.py:239, quantumlab/solvers/split_operator.py:241
IMPORTS (0): 

## SplitOperatorSolver._kinetic_step  [quantumlab/solvers/split_operator.py:225] (method)
SIG: def _kinetic_step(self, psi, w):
EXT_CALLS (1):
  quantumlab/solvers/multicomponent.py:112: psis = [self._engine._kinetic_step(p, w) for p in psis]
EXT_OTHER (1):
  quantumlab/solvers/multicomponent.py:112: psis = [self._engine._kinetic_step(p, w) for p in psis]
INT_CALLS (1): quantumlab/solvers/split_operator.py:240
INT_OTHER (1): quantumlab/solvers/split_operator.py:240
IMPORTS (0): 

## SplitOperatorSolver._strang  [quantumlab/solvers/split_operator.py:238] (method)
SIG: def _strang(self, psi, t, w):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/solvers/split_operator.py:253
INT_OTHER (1): quantumlab/solvers/split_operator.py:253
IMPORTS (0): 

## SplitOperatorSolver._norm  [quantumlab/solvers/split_operator.py:243] (method)
SIG: def _norm(self, psi) -> float:
EXT_CALLS (2):
  quantumlab/solvers/multicomponent.py:109: self._targets = [self._norm(p) for p in psis]
  quantumlab/solvers/multicomponent.py:117: norm = self._norm(p)
EXT_OTHER (2):
  quantumlab/solvers/multicomponent.py:109: self._targets = [self._norm(p) for p in psis]
  quantumlab/solvers/multicomponent.py:117: norm = self._norm(p)
INT_CALLS (2): quantumlab/solvers/split_operator.py:250, quantumlab/solvers/split_operator.py:256
INT_OTHER (2): quantumlab/solvers/split_operator.py:250, quantumlab/solvers/split_operator.py:256
IMPORTS (0): 

## SplitOperatorSolver._advance  [quantumlab/solvers/split_operator.py:246] (method)
SIG: def _advance(self, psi):
EXT_CALLS (2):
  quantumlab/solvers/multicomponent.py:132: return self._download(self._advance(self._upload(states)))
  quantumlab/solvers/multicomponent.py:141: psis = self._advance(psis)
EXT_OTHER (2):
  quantumlab/solvers/multicomponent.py:132: return self._download(self._advance(self._upload(states)))
  quantumlab/solvers/multicomponent.py:141: psis = self._advance(psis)
INT_CALLS (2): quantumlab/solvers/split_operator.py:271, quantumlab/solvers/split_operator.py:281
INT_OTHER (2): quantumlab/solvers/split_operator.py:271, quantumlab/solvers/split_operator.py:281
IMPORTS (0): 

## SplitOperatorSolver._upload  [quantumlab/solvers/split_operator.py:264] (method)
SIG: def _upload(self, wavefunction):
EXT_CALLS (2):
  quantumlab/solvers/multicomponent.py:132: return self._download(self._advance(self._upload(states)))
  quantumlab/solvers/multicomponent.py:139: psis = self._upload(states)
EXT_OTHER (2):
  quantumlab/solvers/multicomponent.py:132: return self._download(self._advance(self._upload(states)))
  quantumlab/solvers/multicomponent.py:139: psis = self._upload(states)
INT_CALLS (2): quantumlab/solvers/split_operator.py:271, quantumlab/solvers/split_operator.py:279
INT_OTHER (2): quantumlab/solvers/split_operator.py:271, quantumlab/solvers/split_operator.py:279
IMPORTS (0): 

## SplitOperatorSolver._download  [quantumlab/solvers/split_operator.py:267] (method)
SIG: def _download(self, psi):
EXT_CALLS (3):
  quantumlab/solvers/multicomponent.py:132: return self._download(self._advance(self._upload(states)))
  quantumlab/solvers/multicomponent.py:143: callback(n, self.t, self._download(psis))
  quantumlab/solvers/multicomponent.py:144: return self._download(psis)
EXT_OTHER (3):
  quantumlab/solvers/multicomponent.py:132: return self._download(self._advance(self._upload(states)))
  quantumlab/solvers/multicomponent.py:143: callback(n, self.t, self._download(psis))
  quantumlab/solvers/multicomponent.py:144: return self._download(psis)
INT_CALLS (3): quantumlab/solvers/split_operator.py:271, quantumlab/solvers/split_operator.py:283, quantumlab/solvers/split_operator.py:284
INT_OTHER (3): quantumlab/solvers/split_operator.py:271, quantumlab/solvers/split_operator.py:283, quantumlab/solvers/split_operator.py:284
IMPORTS (0): 

## SplitOperatorSolver.step  [quantumlab/solvers/split_operator.py:270] (method)
SIG: def step(self, wavefunction):
EXT_CALLS (39):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (91):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitOperatorSolver.evolve  [quantumlab/solvers/split_operator.py:273] (method)
SIG: def evolve(self, wavefunction, n_steps: int, callback=None, callback_interval: int = 1):
EXT_CALLS (55):
  benchmarks/gpu_split_operator.py:26: solver.evolve(wf0, 2)                        # warm-up (FFT plans, CUDA kernels)
  benchmarks/gpu_split_operator.py:28: wf = solver.evolve(wf0, steps)               # includes the final device → host copy
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:57: return SplitOperatorSolver(grid, pot, dt, order=order).evolve(wf0, int(round(2.0 / dt))).psi
  benchmarks/validation_suite.py:74: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:88: wf = SplitOperatorSolver(grid, pot, 0.01, order=4).evolve(wf, n_steps)
  benchmarks/validation_suite.py:163: wf = solver.evolve(WaveFunction1D(grid, psi), 4000)
  benchmarks/validation_suite.py:195: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:203: C = autocorrelation(wf0.psi, solver.evolve(wf0, 500).psi, grid)
  benchmarks/validation_suite.py:223: solver.evolve(states[0], int(round(20 * period / 0.05)),
  benchmarks/validation_suite.py:264: state = solver.evolve(state, 500)
  benchmarks/validation_suite.py:275: state = solver.evolve(state, 100)
  examples/09_soliton_collision.py:37: wf = solver.evolve(wf, record_every)
  examples/12_high_harmonic_generation.py:72: wf = solver.evolve(wf0, int(round(duration / DT)), callback=record)
  examples/13_two_component_bec.py:142: state = solver.evolve(state, 20)
  examples/13_two_component_bec.py:217: state = solver.evolve(state, 250)
  quantumlab/stationary/imaginary_time.py:130: wf = solver.evolve(wf, check_interval)
  quantumlab/stationary/imaginary_time.py:229: states = solver.evolve(states, check_interval)
  tests/test_backends.py:100: ref = SplitOperatorSolver(grid, potential, 0.01, backend='numpy', **kwargs).evolve(wf0, 30)
  tests/test_backends.py:102: out = dev_solver.evolve(wf0, 30)
  tests/test_backends.py:115: ref = SplitOperatorSolver(grid, None, 0.01, absorber=abl).evolve(wf0, 40)
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:163: gpu = gpu_solver.evolve(wf0, 50)
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_conjugate_gradient.py:54: lattice = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om).evolve(seed, 1500)
  tests/test_gross_pitaevskii.py:25: wf = solver.evolve(wf, 4000)
  tests/test_gross_pitaevskii.py:36: wf = SplitOperatorSolver(grid, None, 0.01, nonlinearity=0.0).evolve(wf, 1000)
  tests/test_gross_pitaevskii.py:48: wf = SplitOperatorSolver(grid, shaken, 0.005, nonlinearity=g, order=4).evolve(wf0, 400)
  tests/test_multicomponent.py:25: c = CoupledGPESolver(grid, (t1, t2), [[20.0, 0.0], [0.0, 35.0]], 0.01, order=4, rotation=0.3).evolve((a, b), 60)
  tests/test_multicomponent.py:26: r1 = SplitOperatorSolver(grid, t1, 0.01, order=4, nonlinearity=20.0, rotation=0.3).evolve(a, 60)
  tests/test_multicomponent.py:27: r2 = SplitOperatorSolver(grid, t2, 0.01, order=4, nonlinearity=35.0, rotation=0.3).evolve(b, 60)
  tests/test_multicomponent.py:72: state = solver.evolve(state, 500)
  tests/test_multicomponent.py:87: state = solver.evolve(state, 100)
  tests/test_multicomponent.py:101: out = CoupledGPESolver(grid, traps, G, 0.005, order=4).evolve(state, 300)
  tests/test_rotation.py:29: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:41: wf = solver.evolve(wf, 300)
  tests/test_rotation.py:54: wf = solver.evolve(wf0, 500)
  tests/test_rotation.py:71: wf = SplitOperatorSolver(grid, trap, 0.005, order=4, rotation=Om).evolve(wf, 600)
  tests/test_rotation.py:82: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:94: wf = solver.evolve(wf, 200)
  tests/test_rotation.py:105: lattice = solver.evolve(WaveFunction2D(grid, seed), 3000)
  tests/test_split_operator.py:56: wf = solver.evolve(wf, 300)
  tests/test_split_operator.py:72: return SplitOperatorSolver(grid, pot, dt, order=o).evolve(wf0, int(round(T / dt))).psi
  tests/test_split_operator.py:84: ref = SplitOperatorSolver(grid, pot, 0.0005, order=4).evolve(wf0, 4000).psi
  tests/test_split_operator.py:85: e2 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=2).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:86: e4 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=4).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:98: wf = solver.evolve(wf, 100)
  tests/test_split_operator.py:109: wa = SplitOperatorSolver(grid, a, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:110: wb = SplitOperatorSolver(grid, b, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:127: free = SplitOperatorSolver(grid, None, 0.01).evolve(wf, 1000)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
EXT_OTHER (55):
  benchmarks/gpu_split_operator.py:26: solver.evolve(wf0, 2)                        # warm-up (FFT plans, CUDA kernels)
  benchmarks/gpu_split_operator.py:28: wf = solver.evolve(wf0, steps)               # includes the final device → host copy
  benchmarks/validation_suite.py:44: wf = SplitOperatorSolver(grid, None, 0.05).evolve(WaveFunction1D.gaussian(grid, 0.0, k0, sigma0), 100)
  benchmarks/validation_suite.py:57: return SplitOperatorSolver(grid, pot, dt, order=order).evolve(wf0, int(round(2.0 / dt))).psi
  benchmarks/validation_suite.py:74: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:88: wf = SplitOperatorSolver(grid, pot, 0.01, order=4).evolve(wf, n_steps)
  benchmarks/validation_suite.py:163: wf = solver.evolve(WaveFunction1D(grid, psi), 4000)
  benchmarks/validation_suite.py:195: wf = solver.evolve(wf, 100)
  benchmarks/validation_suite.py:203: C = autocorrelation(wf0.psi, solver.evolve(wf0, 500).psi, grid)
  benchmarks/validation_suite.py:223: solver.evolve(states[0], int(round(20 * period / 0.05)),
  benchmarks/validation_suite.py:264: state = solver.evolve(state, 500)
  benchmarks/validation_suite.py:275: state = solver.evolve(state, 100)
  examples/09_soliton_collision.py:37: wf = solver.evolve(wf, record_every)
  examples/12_high_harmonic_generation.py:72: wf = solver.evolve(wf0, int(round(duration / DT)), callback=record)
  examples/13_two_component_bec.py:142: state = solver.evolve(state, 20)
  examples/13_two_component_bec.py:217: state = solver.evolve(state, 250)
  quantumlab/stationary/imaginary_time.py:130: wf = solver.evolve(wf, check_interval)
  quantumlab/stationary/imaginary_time.py:229: states = solver.evolve(states, check_interval)
  tests/test_backends.py:100: ref = SplitOperatorSolver(grid, potential, 0.01, backend='numpy', **kwargs).evolve(wf0, 30)
  tests/test_backends.py:102: out = dev_solver.evolve(wf0, 30)
  tests/test_backends.py:115: ref = SplitOperatorSolver(grid, None, 0.01, absorber=abl).evolve(wf0, 40)
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:161: cpu = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.01, **kwargs).evolve(wf0, 50)
  tests/test_backends.py:163: gpu = gpu_solver.evolve(wf0, 50)
  tests/test_backends.py:176: ref = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, **kwargs).evolve((a, b), 25)
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_conjugate_gradient.py:54: lattice = SplitOperatorSolver(grid, trap, 0.005, nonlinearity=g, imaginary_time=True, rotation=Om).evolve(seed, 1500)
  tests/test_gross_pitaevskii.py:25: wf = solver.evolve(wf, 4000)
  tests/test_gross_pitaevskii.py:36: wf = SplitOperatorSolver(grid, None, 0.01, nonlinearity=0.0).evolve(wf, 1000)
  tests/test_gross_pitaevskii.py:48: wf = SplitOperatorSolver(grid, shaken, 0.005, nonlinearity=g, order=4).evolve(wf0, 400)
  tests/test_multicomponent.py:25: c = CoupledGPESolver(grid, (t1, t2), [[20.0, 0.0], [0.0, 35.0]], 0.01, order=4, rotation=0.3).evolve((a, b), 60)
  tests/test_multicomponent.py:26: r1 = SplitOperatorSolver(grid, t1, 0.01, order=4, nonlinearity=20.0, rotation=0.3).evolve(a, 60)
  tests/test_multicomponent.py:27: r2 = SplitOperatorSolver(grid, t2, 0.01, order=4, nonlinearity=35.0, rotation=0.3).evolve(b, 60)
  tests/test_multicomponent.py:72: state = solver.evolve(state, 500)
  tests/test_multicomponent.py:87: state = solver.evolve(state, 100)
  tests/test_multicomponent.py:101: out = CoupledGPESolver(grid, traps, G, 0.005, order=4).evolve(state, 300)
  tests/test_rotation.py:29: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:41: wf = solver.evolve(wf, 300)
  tests/test_rotation.py:54: wf = solver.evolve(wf0, 500)
  tests/test_rotation.py:71: wf = SplitOperatorSolver(grid, trap, 0.005, order=4, rotation=Om).evolve(wf, 600)
  tests/test_rotation.py:82: wf = solver.evolve(wf, 100)
  tests/test_rotation.py:94: wf = solver.evolve(wf, 200)
  tests/test_rotation.py:105: lattice = solver.evolve(WaveFunction2D(grid, seed), 3000)
  tests/test_split_operator.py:56: wf = solver.evolve(wf, 300)
  tests/test_split_operator.py:72: return SplitOperatorSolver(grid, pot, dt, order=o).evolve(wf0, int(round(T / dt))).psi
  tests/test_split_operator.py:84: ref = SplitOperatorSolver(grid, pot, 0.0005, order=4).evolve(wf0, 4000).psi
  tests/test_split_operator.py:85: e2 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=2).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:86: e4 = _l2(SplitOperatorSolver(grid, pot, 0.02, order=4).evolve(wf0, 100).psi, ref, grid.dx)
  tests/test_split_operator.py:98: wf = solver.evolve(wf, 100)
  tests/test_split_operator.py:109: wa = SplitOperatorSolver(grid, a, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:110: wb = SplitOperatorSolver(grid, b, 0.01).evolve(wf0, 200)
  tests/test_split_operator.py:118: wf = SplitOperatorSolver(grid, None, 0.05).evolve(wf, int(round(t / 0.05)))
  tests/test_split_operator.py:127: free = SplitOperatorSolver(grid, None, 0.01).evolve(wf, 1000)
  tests/test_split_operator.py:128: absorbed = SplitOperatorSolver(grid, None, 0.01, absorber=AbsorbingBoundaryLayer(grid, 4.0)).evolve(wf, 1000)
  tests/test_split_operator.py:148: SplitOperatorSolver(grid, None, 0.1).evolve(wf, 10, callback=lambda n, t, w: calls.append((n, t)),
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitStep1DSolver  [quantumlab/solvers/split_step_1d.py:6] (class)
SIG: class SplitStep1DSolver(...):
EXT_CALLS (8):
  examples/01_gaussian_barrier.py:33: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  examples/02_harmonic_oscillator.py:31: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=m)
  examples/03_double_well.py:32: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  examples/04_multiple_barriers.py:34: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  quantumlab/runner.py:115: return SplitStep1DSolver(grid, potential, dt, hbar, m)
  testbench_interlock.py:100: solver = SplitStep1DSolver(grid, pot, dt=0.05)
  tests/test_solvers.py:13: solver = SplitStep1DSolver(grid, potential, dt=0.02)
  tests/test_solvers.py:24: solver = SplitStep1DSolver(grid, potential, dt=0.01)
EXT_OTHER (9):
  examples/01_gaussian_barrier.py:33: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  examples/02_harmonic_oscillator.py:31: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=m)
  examples/03_double_well.py:32: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  examples/04_multiple_barriers.py:34: solver = SplitStep1DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  quantumlab/runner.py:115: return SplitStep1DSolver(grid, potential, dt, hbar, m)
  testbench_interlock.py:100: solver = SplitStep1DSolver(grid, pot, dt=0.05)
  tests/test_solvers.py:13: solver = SplitStep1DSolver(grid, potential, dt=0.02)
  tests/test_solvers.py:24: solver = SplitStep1DSolver(grid, potential, dt=0.01)
  tests/test_split_operator.py:30: pot, legacy = GaussianBarrier(4.0, 1.0, 0.0), SplitStep1DSolver
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (9): quantumlab/runner.py:15(quantumlab.solvers), testbench_interlock.py:36(quantumlab.solvers), tests/test_split_operator.py:9(quantumlab.solvers), examples/01_gaussian_barrier.py:7(quantumlab.solvers.split_step_1d), examples/02_harmonic_oscillator.py:7(quantumlab.solvers.split_step_1d), examples/03_double_well.py:6(quantumlab.solvers.split_step_1d), examples/04_multiple_barriers.py:6(quantumlab.solvers.split_step_1d), quantumlab/solvers/__init__.py:2(quantumlab.solvers.split_step_1d), tests/test_solvers.py:6(quantumlab.solvers.split_step_1d)

## SplitStep1DSolver.__init__  [quantumlab/solvers/split_step_1d.py:8] (method)
SIG: def __init__(self, grid, potential, dt: float, hbar: float=1.0, m: float=1.0):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (1): quantumlab/solvers/split_step_1d.py:9
INT_OTHER (1): quantumlab/solvers/split_step_1d.py:9
IMPORTS (0): 

## SplitStep1DSolver.update_operators  [quantumlab/solvers/split_step_1d.py:16] (method)
SIG: def update_operators(self):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
INT_CALLS (1): quantumlab/solvers/split_step_1d.py:14
INT_OTHER (1): quantumlab/solvers/split_step_1d.py:14
IMPORTS (0): 

## SplitStep1DSolver.step  [quantumlab/solvers/split_step_1d.py:20] (method)
SIG: def step(self, wavefunction: WaveFunction1D) -> WaveFunction1D:
EXT_CALLS (39):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (91):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitStep2DSolver  [quantumlab/solvers/split_step_2d.py:6] (class)
SIG: class SplitStep2DSolver(...):
EXT_CALLS (4):
  examples/05_2d_gaussian_barrier.py:41: solver    = SplitStep2DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  quantumlab/runner.py:117: return SplitStep2DSolver(grid, potential, dt, hbar, m)
  tests/test_2d_solver.py:16: solver = SplitStep2DSolver(grid, potential, dt=0.02)
  tests/test_2d_solver.py:28: solver = SplitStep2DSolver(grid, potential, dt=0.01)
EXT_OTHER (5):
  examples/05_2d_gaussian_barrier.py:41: solver    = SplitStep2DSolver(grid, potential, dt, hbar=1.0, m=1.0)
  quantumlab/runner.py:117: return SplitStep2DSolver(grid, potential, dt, hbar, m)
  tests/test_2d_solver.py:16: solver = SplitStep2DSolver(grid, potential, dt=0.02)
  tests/test_2d_solver.py:28: solver = SplitStep2DSolver(grid, potential, dt=0.01)
  tests/test_split_operator.py:34: pot, legacy = Gaussian2DBarrier(3.0, 1.0), SplitStep2DSolver
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): quantumlab/runner.py:15(quantumlab.solvers), tests/test_split_operator.py:9(quantumlab.solvers), examples/05_2d_gaussian_barrier.py:6(quantumlab.solvers.split_step_2d), quantumlab/solvers/__init__.py:3(quantumlab.solvers.split_step_2d), tests/test_2d_solver.py:7(quantumlab.solvers.split_step_2d)

## SplitStep2DSolver.__init__  [quantumlab/solvers/split_step_2d.py:17] (method)
SIG: def __init__(self, grid, potential, dt: float, hbar: float = 1.0, m: float = 1.0):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (1): quantumlab/solvers/split_step_2d.py:18
INT_OTHER (1): quantumlab/solvers/split_step_2d.py:18
IMPORTS (0): 

## SplitStep2DSolver.update_operators  [quantumlab/solvers/split_step_2d.py:25] (method)
SIG: def update_operators(self):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
INT_CALLS (1): quantumlab/solvers/split_step_2d.py:23
INT_OTHER (1): quantumlab/solvers/split_step_2d.py:23
IMPORTS (0): 

## SplitStep2DSolver.step  [quantumlab/solvers/split_step_2d.py:30] (method)
SIG: def step(self, wavefunction: WaveFunction2D) -> WaveFunction2D:
EXT_CALLS (39):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (91):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitStep3DSolver  [quantumlab/solvers/split_step_3d.py:7] (class)
SIG: class SplitStep3DSolver(...):
EXT_CALLS (7):
  benchmarks/perf_comparison.py:94: solver_cpu = SplitStep3DSolver(grid, potential, dt=0.02)
  examples/06_3d_gaussian_barrier.py:42: solver    = SplitStep3DSolver(grid, potential, dt, hbar=1.0, m=1.0, workers=-1)
  quantumlab/runner.py:121: return SplitStep3DSolver(grid, potential, dt, hbar, m)
  tests/test_3d_gpu_solver.py:80: solver_cpu = SplitStep3DSolver(small_grid, barrier, dt=0.02)
  tests/test_3d_solver.py:77: solver = SplitStep3DSolver(grid, potential, dt=0.02)
  tests/test_3d_solver.py:95: solver = SplitStep3DSolver(grid, potential, dt=0.01)
  tests/test_benchmark_failure_handling.py:200: self._cpu = mod.SplitStep3DSolver(grid, potential, dt=dt)
EXT_OTHER (8):
  benchmarks/perf_comparison.py:94: solver_cpu = SplitStep3DSolver(grid, potential, dt=0.02)
  examples/06_3d_gaussian_barrier.py:42: solver    = SplitStep3DSolver(grid, potential, dt, hbar=1.0, m=1.0, workers=-1)
  quantumlab/runner.py:121: return SplitStep3DSolver(grid, potential, dt, hbar, m)
  tests/test_3d_gpu_solver.py:80: solver_cpu = SplitStep3DSolver(small_grid, barrier, dt=0.02)
  tests/test_3d_solver.py:77: solver = SplitStep3DSolver(grid, potential, dt=0.02)
  tests/test_3d_solver.py:95: solver = SplitStep3DSolver(grid, potential, dt=0.01)
  tests/test_benchmark_failure_handling.py:200: self._cpu = mod.SplitStep3DSolver(grid, potential, dt=dt)
  tests/test_split_operator.py:38: pot, legacy = Gaussian3DBarrier(3.0, 1.0), SplitStep3DSolver
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (7): quantumlab/runner.py:15(quantumlab.solvers), tests/test_split_operator.py:9(quantumlab.solvers), benchmarks/perf_comparison.py:38(quantumlab.solvers.split_step_3d), examples/06_3d_gaussian_barrier.py:6(quantumlab.solvers.split_step_3d), quantumlab/solvers/__init__.py:4(quantumlab.solvers.split_step_3d), tests/test_3d_gpu_solver.py:11(quantumlab.solvers.split_step_3d), tests/test_3d_solver.py:7(quantumlab.solvers.split_step_3d)

## SplitStep3DSolver.__init__  [quantumlab/solvers/split_step_3d.py:37] (method)
SIG: def __init__(self, grid, potential, dt: float, hbar: float = 1.0,
                 m: float = 1.0, workers: int = -1):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d_gpu.py:41: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (1): quantumlab/solvers/split_step_3d.py:39
INT_OTHER (1): quantumlab/solvers/split_step_3d.py:39
IMPORTS (0): 

## SplitStep3DSolver.update_operators  [quantumlab/solvers/split_step_3d.py:49] (method)
SIG: def update_operators(self):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d_gpu.py:76: self.update_operators()
INT_CALLS (1): quantumlab/solvers/split_step_3d.py:47
INT_OTHER (1): quantumlab/solvers/split_step_3d.py:47
IMPORTS (0): 

## SplitStep3DSolver.step  [quantumlab/solvers/split_step_3d.py:54] (method)
SIG: def step(self, wavefunction: WaveFunction3D) -> WaveFunction3D:
EXT_CALLS (39):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (91):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/split_step_3d_gpu.py:115: wf = self.step(wf)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitStep3DGPU  [quantumlab/solvers/split_step_3d_gpu.py:25] (class)
SIG: class SplitStep3DGPU(...):
EXT_CALLS (10):
  benchmarks/perf_comparison.py:117: solver_gpu = SplitStep3DGPU(grid, potential, dt=0.02)
  quantumlab/runner.py:120: return SplitStep3DGPU(grid, potential, dt, hbar, m)
  tests/test_3d_gpu_solver.py:43: solver = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:57: solver = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:79: solver_gpu = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:97: solver_seq = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:98: solver_ind = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:123: solver = SplitStep3DGPU(grid, potential, dt=0.02, device_id=999)
  tests/test_3d_gpu_solver.py:140: solver = SplitStep3DGPU(small_grid, potential, dt=0.02)
  tests/test_3d_gpu_solver.py:152: solver = SplitStep3DGPU(small_grid, barrier, dt=0.02)
EXT_OTHER (13):
  benchmarks/perf_comparison.py:117: solver_gpu = SplitStep3DGPU(grid, potential, dt=0.02)
  quantumlab/runner.py:120: return SplitStep3DGPU(grid, potential, dt, hbar, m)
  tests/test_3d_gpu_solver.py:43: solver = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:57: solver = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:79: solver_gpu = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:97: solver_seq = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:98: solver_ind = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_3d_gpu_solver.py:123: solver = SplitStep3DGPU(grid, potential, dt=0.02, device_id=999)
  tests/test_3d_gpu_solver.py:140: solver = SplitStep3DGPU(small_grid, potential, dt=0.02)
  tests/test_3d_gpu_solver.py:152: solver = SplitStep3DGPU(small_grid, barrier, dt=0.02)
  tests/test_benchmark_failure_handling.py:237: real_gpu = mod.SplitStep3DGPU
  tests/test_benchmark_failure_handling.py:268: real_gpu = mod.SplitStep3DGPU
  tests/test_benchmark_failure_handling.py:299: real_gpu = mod.SplitStep3DGPU
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (3): benchmarks/perf_comparison.py:39(quantumlab.solvers.split_step_3d_gpu), quantumlab/runner.py:16(quantumlab.solvers.split_step_3d_gpu), tests/test_3d_gpu_solver.py:10(quantumlab.solvers.split_step_3d_gpu)

## SplitStep3DGPU.__init__  [quantumlab/solvers/split_step_3d_gpu.py:31] (method)
SIG: def __init__(
        self,
        grid,
        potential,
        dt: float,
        hbar: float = 1.0,
        m: float = 1.0,
        device_id: int = 0,
        renormalize_interval: int = 0,
    ):
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:103: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_1d.py:9: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_2d.py:18: super().__init__(grid, potential, dt, hbar, m)
  quantumlab/solvers/split_step_3d.py:39: super().__init__(grid, potential, dt, hbar, m)
INT_CALLS (1): quantumlab/solvers/split_step_3d_gpu.py:41
INT_OTHER (1): quantumlab/solvers/split_step_3d_gpu.py:41
IMPORTS (0): 

## SplitStep3DGPU.update_operators  [quantumlab/solvers/split_step_3d_gpu.py:78] (method)
SIG: def update_operators(self) -> None:
EXT_CALLS (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
EXT_OTHER (4):
  quantumlab/solvers/split_operator.py:146: self.update_operators()
  quantumlab/solvers/split_step_1d.py:14: self.update_operators()
  quantumlab/solvers/split_step_2d.py:23: self.update_operators()
  quantumlab/solvers/split_step_3d.py:47: self.update_operators()
INT_CALLS (1): quantumlab/solvers/split_step_3d_gpu.py:76
INT_OTHER (1): quantumlab/solvers/split_step_3d_gpu.py:76
IMPORTS (0): 

## SplitStep3DGPU.step  [quantumlab/solvers/split_step_3d_gpu.py:87] (method)
SIG: def step(self, wavefunction: WaveFunction3D) -> WaveFunction3D:
EXT_CALLS (38):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
EXT_OTHER (90):
  benchmarks/perf_comparison.py:97: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:104: wf_cpu = solver_cpu.step(wf_cpu)
  benchmarks/perf_comparison.py:122: wf_gpu = solver_gpu.step(wf_gpu)
  benchmarks/validation_suite.py:143: wf = solver.step(wf)
  examples/01_gaussian_barrier.py:38: for step in range(1, num_steps + 1):
  examples/01_gaussian_barrier.py:39: wf_current = solver.step(wf_current)
  examples/01_gaussian_barrier.py:40: space_time[step, :] = wf_current.probability_density
  examples/01_gaussian_barrier.py:41: if step % 200 == 0:
  examples/01_gaussian_barrier.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}, Δx={dx:.3f}')
  examples/02_harmonic_oscillator.py:39: for step in range(1, num_steps + 1):
  examples/02_harmonic_oscillator.py:40: wf_current = solver.step(wf_current)
  examples/02_harmonic_oscillator.py:41: space_time[step, :] = wf_current.probability_density
  examples/02_harmonic_oscillator.py:42: t = step * dt
  examples/02_harmonic_oscillator.py:48: if step % 150 == 0:
  examples/02_harmonic_oscillator.py:49: print(f'  Step {step}/{num_steps}: Time={t:.2f}s, ⟨x⟩={x_mean:.4f}, ⟨E⟩={energy:.6f}')
  examples/03_double_well.py:39: for step in range(1, num_steps + 1):
  examples/03_double_well.py:40: wf_current = solver.step(wf_current)
  examples/03_double_well.py:41: space_time[step, :] = wf_current.probability_density
  examples/03_double_well.py:42: t = step * dt
  examples/03_double_well.py:46: if step % 300 == 0:
  examples/03_double_well.py:48: print(f'  Step {step}/{num_steps}: Time={t:.1f}s, ⟨x⟩={x_mean:.4f}, Energy={energy:.6f}')
  examples/04_multiple_barriers.py:39: for step in range(1, num_steps + 1):
  examples/04_multiple_barriers.py:40: wf_current = solver.step(wf_current)
  examples/04_multiple_barriers.py:41: space_time[step, :] = wf_current.probability_density
  examples/04_multiple_barriers.py:42: if step % 200 == 0:
  examples/04_multiple_barriers.py:45: print(f'  Step {step}/{num_steps}: Norm={norm:.6f}, ⟨x⟩={x_mean:.3f}')
  examples/05_2d_gaussian_barrier.py:53: for step in range(1, num_steps + 1):
  examples/05_2d_gaussian_barrier.py:54: wf_current = solver.step(wf_current)
  examples/05_2d_gaussian_barrier.py:57: if step in snapshot_steps:
  examples/05_2d_gaussian_barrier.py:59: snap_times.append(step * dt)
  examples/05_2d_gaussian_barrier.py:61: if step % 100 == 0:
  examples/05_2d_gaussian_barrier.py:67: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:47: for step in range(1, num_steps + 1):
  examples/06_3d_gaussian_barrier.py:48: wf_current = solver.step(wf_current)
  examples/06_3d_gaussian_barrier.py:51: if step % 50 == 0:
  examples/06_3d_gaussian_barrier.py:57: print(f'  Step {step:>4}/{num_steps}: Norm={norm:.6f}  '
  examples/06_3d_gaussian_barrier.py:60: if step in snapshot_steps:
  examples/06_3d_gaussian_barrier.py:64: title=f'3D Gaussian Barrier — Orthogonal Slices  (t = {step * dt:.2f})',
  examples/06_3d_gaussian_barrier.py:65: save_path=f'output/06_3d_slices_t{step:04d}.png',
  examples/06_3d_gaussian_barrier.py:69: print(f'  Snapshot saved: output/06_3d_slices_t{step:04d}.png')
  examples/07_3d_double_slit.py:82: for step in range(1, num_steps + 1):
  examples/07_3d_double_slit.py:83: wf = solver.step(wf)
  examples/07_3d_double_slit.py:84: if step % frame_every == 0:
  examples/07_3d_double_slit.py:89: if step == showcase_step:
  examples/07_3d_double_slit.py:91: if step % 50 == 0:
  examples/08_3d_bec_time_of_flight.py:109: for step in range(1, num_steps + 1):
  examples/08_3d_bec_time_of_flight.py:110: wf = solver.step(wf)
  examples/08_3d_bec_time_of_flight.py:111: if step % frame_every == 0:
  examples/08_3d_bec_time_of_flight.py:115: if step % (5 * frame_every) == 0:
  examples/10_quantum_chaos_stadium.py:76: ax.step(np.concatenate([[0], energies]), np.concatenate([[0], staircase]), where='post',
  examples/11_rotating_bec_vortex_lattice.py:97: for step in range(0, n_steps + 1):
  examples/11_rotating_bec_vortex_lattice.py:98: if step > 0:
  examples/11_rotating_bec_vortex_lattice.py:99: wf = solver.step(wf)
  examples/11_rotating_bec_vortex_lattice.py:100: if step % frame_every == 0:
  examples/11_rotating_bec_vortex_lattice.py:109: if step % 4000 == 0 and step > 0:
  examples/11_rotating_bec_vortex_lattice.py:183: for step in (1, -1):
  examples/11_rotating_bec_vortex_lattice.py:185: while abs(grid3.z[k + step]) <= 0.6 * Z:
  examples/11_rotating_bec_vortex_lattice.py:186: k += step
  examples/13_two_component_bec.py:140: for step in range(0, n_steps + 1, 20):
  examples/13_two_component_bec.py:141: if step:
  examples/13_two_component_bec.py:151: if step % 60 == 0:
  quantumlab/runner.py:160: for step in range(1, num_steps + 1):
  quantumlab/runner.py:161: wf_current = solver.step(wf_current)
  quantumlab/runner.py:165: if snapshot_interval > 0 and step % snapshot_interval == 0:
  quantumlab/runner.py:167: snap_times.append(step * float(cfg["dt"]))
  quantumlab/runner.py:169: if step % int(cfg.get("log_interval", 100)) == 0:
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/stationary/imaginary_time.py:126: wf = solver.step(wf)
  testbench_interlock.py:106: wf = solver.step(wf)
  tests/test_2d_solver.py:20: wf_current = solver.step(wf_current)
  tests/test_2d_solver.py:32: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:48: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:62: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:85: wf_gpu = solver_gpu.step(wf_gpu)
  tests/test_3d_gpu_solver.py:86: wf_cpu = solver_cpu.step(wf_cpu)
  tests/test_3d_gpu_solver.py:104: wf_ind = solver_ind.step(wf_ind)
  tests/test_3d_gpu_solver.py:127: wf_current = solver.step(wf_current)
  tests/test_3d_gpu_solver.py:144: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:82: wf_current = solver.step(wf_current)
  tests/test_3d_solver.py:100: wf_current = solver.step(wf_current)
  tests/test_backends.py:131: wa, wb = a.step(wa), b.step(wb)
  tests/test_benchmark_failure_handling.py:204: return self._cpu.step(wf)
  tests/test_benchmark_failure_handling.py:209: out = self._cpu.step(out)
  tests/test_benchmark_failure_handling.py:273: return super().step(wf)
  tests/test_multicomponent.py:140: solver.step((WaveFunction1D.gaussian(grid, 0.0, 0.0, 1.0),))
  tests/test_new_potentials_and_observables.py:118: wf = solver.step(wf)
  tests/test_solvers.py:17: wf_current = solver.step(wf_current)
  tests/test_solvers.py:28: wf_current = solver.step(wf_current)
  tests/test_split_operator.py:43: wa = a.step(wa)
  tests/test_split_operator.py:44: wb = b.step(wb)
INT_CALLS (1): quantumlab/solvers/split_step_3d_gpu.py:115
INT_OTHER (1): quantumlab/solvers/split_step_3d_gpu.py:115
IMPORTS (0): 

## SplitStep3DGPU.step_sequence  [quantumlab/solvers/split_step_3d_gpu.py:107] (method)
SIG: def step_sequence(self, initial_wf: WaveFunction3D, steps: int) -> WaveFunction3D:
EXT_CALLS (5):
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  tests/test_3d_gpu_solver.py:100: wf_seq = solver_seq.step_sequence(gaussian_wf, steps=20)
  tests/test_benchmark_failure_handling.py:277: return super().step_sequence(wf, steps)
  tests/test_benchmark_failure_handling.py:304: return super().step_sequence(wf, steps)
EXT_OTHER (5):
  benchmarks/perf_comparison.py:123: solver_gpu.step_sequence(wf.copy(), steps=warmup_steps)
  benchmarks/perf_comparison.py:128: wf_gpu = solver_gpu.step_sequence(wf.copy(), steps=steps)
  tests/test_3d_gpu_solver.py:100: wf_seq = solver_seq.step_sequence(gaussian_wf, steps=20)
  tests/test_benchmark_failure_handling.py:277: return super().step_sequence(wf, steps)
  tests/test_benchmark_failure_handling.py:304: return super().step_sequence(wf, steps)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## SplitStep3DGPU._step_gpu_internal  [quantumlab/solvers/split_step_3d_gpu.py:125] (method)
SIG: def _step_gpu_internal(self, psi_gpu):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/solvers/split_step_3d_gpu.py:92, quantumlab/solvers/split_step_3d_gpu.py:121
INT_OTHER (2): quantumlab/solvers/split_step_3d_gpu.py:92, quantumlab/solvers/split_step_3d_gpu.py:121
IMPORTS (0): 

## SplitStep3DGPU.backend  [quantumlab/solvers/split_step_3d_gpu.py:140] (method)
SIG: def backend(self) -> str:
EXT_CALLS (0):
EXT_OTHER (37):
  benchmarks/gpu_split_operator.py:25: solver = SplitOperatorSolver(grid, HarmonicTrap((1.0, 1.0, 0.8)), 0.005, backend=backend, **CONFIG)
  benchmarks/perf_comparison.py:113: backend = "unavailable"
  benchmarks/perf_comparison.py:137: backend = solver_gpu.backend
  benchmarks/perf_comparison.py:138: if backend != "cupy":
  benchmarks/perf_comparison.py:144: "reason": f"solver_fell_back_to:{backend}",
  benchmarks/perf_comparison.py:149: backend = "unavailable"
  benchmarks/perf_comparison.py:155: run_status = "PASSED" if (status["state"] == "ok" and backend == "cupy") else "UNAVAILABLE"
  benchmarks/perf_comparison.py:168: 'backend': backend,
  quantumlab/runner.py:172: logger.info("  Step %5d/%d  E=%.6f  <x>=%+.3f  [%s]", step, num_steps, E, x, solver.backend)
  quantumlab/solvers/backends.py:69: if isinstance(backend, ArrayBackend):
  quantumlab/solvers/backends.py:70: return backend
  quantumlab/solvers/backends.py:71: if backend == 'numpy':
  quantumlab/solvers/backends.py:73: if backend == 'cupy':
  quantumlab/solvers/backends.py:77: if backend == 'auto':
  quantumlab/solvers/multicomponent.py:62: backend=backend, device_id=device_id, t0=t0)
  quantumlab/solvers/split_operator.py:129: self._be = get_backend(backend, workers=workers, device_id=device_id)
  quantumlab/stationary/imaginary_time.py:94: check_interval, hbar, m, orthogonal_to, workers, rotation, backend)
  quantumlab/stationary/imaginary_time.py:102: rotation=rotation, backend=backend)
  quantumlab/stationary/imaginary_time.py:220: rotation=rotation, backend=backend, workers=workers)
  tests/test_3d_gpu_solver.py:44: assert solver.backend == "cupy"
  tests/test_3d_gpu_solver.py:130: assert solver.backend == "scipy-cpu"
  tests/test_3d_gpu_solver.py:153: assert solver.backend in ("cupy", "scipy-cpu")
  tests/test_backends.py:57: backend = ArrayBackend(
  tests/test_backends.py:65: return backend, calls
  tests/test_backends.py:99: backend, calls = _strict_backend()
  tests/test_backends.py:101: dev_solver = SplitOperatorSolver(grid, potential, 0.01, backend=backend, **kwargs)
  tests/test_backends.py:103: assert dev_solver.backend == 'emulated-device'
  tests/test_backends.py:113: backend, calls = _strict_backend()
  tests/test_backends.py:116: out = SplitOperatorSolver(grid, None, 0.01, absorber=abl, backend=backend).evolve(
  tests/test_backends.py:126: backend, _ = _strict_backend()
  tests/test_backends.py:127: a = SplitOperatorSolver(grid, HarmonicTrap(1.0), 0.02, backend=backend, rotation=0.3)
  tests/test_backends.py:138: backend, _ = _strict_backend()
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:164: assert gpu_solver.backend == 'cupy'
  tests/test_backends.py:175: backend, calls = _strict_backend()
  tests/test_backends.py:177: dev = CoupledGPESolver(grid, (HarmonicTrap(1.0), HarmonicTrap(1.2)), G, 0.01, backend=backend,
  tests/test_benchmark_failure_handling.py:197: backend = "cupy"
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (0): 

## ground_state_pcg  [quantumlab/stationary/conjugate_gradient.py:24] (function)
SIG: def ground_state_pcg(grid, potential, initial=None, nonlinearity: float = 0.0, rotation: float = 0.0,
                     tol: float = 1e-8, max_iter: int = 10000, hbar: float = 1.0, m: float = 1.0,
                     callback=None, callback_interval: int = 100, workers: int = -1):
EXT_CALLS (9):
  benchmarks/validation_suite.py:312: _, info = ground_state_pcg(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), tol=1e-10)
  benchmarks/validation_suite.py:317: wf, info = ground_state_pcg(grid, trap, nonlinearity=g, tol=1e-9)
  examples/11_rotating_bec_vortex_lattice.py:169: wf3, info3 = ground_state_pcg(grid3, trap3, initial=wf3, nonlinearity=g3, rotation=Om, tol=1e-6,
  tests/test_conjugate_gradient.py:20: wf, info = ground_state_pcg(grid, potential, tol=1e-10, max_iter=3000, **kwargs)
  tests/test_conjugate_gradient.py:32: wf, info = ground_state_pcg(grid, trap, nonlinearity=g, tol=1e-9)
  tests/test_conjugate_gradient.py:44: wf, info = ground_state_pcg(grid, HarmonicTrap(1.0), initial=guess, nonlinearity=5.0, tol=1e-9)
  tests/test_conjugate_gradient.py:56: wf, info = ground_state_pcg(grid, trap, initial=lattice, nonlinearity=g, rotation=Om, tol=1e-7, max_iter=3000)
  tests/test_conjugate_gradient.py:64: ground_state_pcg(Grid1D(64, -6.0, 6.0), HarmonicTrap(1.0), tol=1e-8,
  tests/test_conjugate_gradient.py:68: ground_state_pcg(Grid1D(32, -4.0, 4.0), DipoleDrive(None, 1.0, 1.0))
EXT_OTHER (9):
  benchmarks/validation_suite.py:312: _, info = ground_state_pcg(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), tol=1e-10)
  benchmarks/validation_suite.py:317: wf, info = ground_state_pcg(grid, trap, nonlinearity=g, tol=1e-9)
  examples/11_rotating_bec_vortex_lattice.py:169: wf3, info3 = ground_state_pcg(grid3, trap3, initial=wf3, nonlinearity=g3, rotation=Om, tol=1e-6,
  tests/test_conjugate_gradient.py:20: wf, info = ground_state_pcg(grid, potential, tol=1e-10, max_iter=3000, **kwargs)
  tests/test_conjugate_gradient.py:32: wf, info = ground_state_pcg(grid, trap, nonlinearity=g, tol=1e-9)
  tests/test_conjugate_gradient.py:44: wf, info = ground_state_pcg(grid, HarmonicTrap(1.0), initial=guess, nonlinearity=5.0, tol=1e-9)
  tests/test_conjugate_gradient.py:56: wf, info = ground_state_pcg(grid, trap, initial=lattice, nonlinearity=g, rotation=Om, tol=1e-7, max_iter=3000)
  tests/test_conjugate_gradient.py:64: ground_state_pcg(Grid1D(64, -6.0, 6.0), HarmonicTrap(1.0), tol=1e-8,
  tests/test_conjugate_gradient.py:68: ground_state_pcg(Grid1D(32, -4.0, 4.0), DipoleDrive(None, 1.0, 1.0))
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): benchmarks/validation_suite.py:311(quantumlab.stationary), examples/11_rotating_bec_vortex_lattice.py:45(quantumlab.stationary), tests/test_conjugate_gradient.py:7(quantumlab.stationary), quantumlab/stationary/__init__.py:5(quantumlab.stationary.conjugate_gradient)

## eigenstates  [quantumlab/stationary/eigensolver.py:17] (function)
SIG: def eigenstates(grid, potential, n_states: int = 6, hbar: float = 1.0, m: float = 1.0,
                tol: float = None, max_iter: int = 1000, seed: int = 0,
                method: str = 'auto', workers: int = -1) -> Tuple[np.ndarray, List]:
EXT_CALLS (11):
  benchmarks/validation_suite.py:119: E, _ = eigenstates(grid, HarmonicTrap(1.0), n_states=10, method='lanczos')
  benchmarks/validation_suite.py:124: E, _ = eigenstates(grid, HarmonicTrap(w), n_states=6, method='lobpcg')
  benchmarks/validation_suite.py:211: E, states = eigenstates(grid, atom, n_states=1)
  examples/10_quantum_chaos_stadium.py:41: energies, states = eigenstates(grid, stadium, n_states=n_states, method='lobpcg', tol=1e-6)
  examples/12_high_harmonic_generation.py:94: energies, states = eigenstates(GRID, atom, n_states=1)
  tests/test_stationary.py:16: energies, states = eigenstates(grid, HarmonicTrap(1.3), n_states=8, method='lanczos')
  tests/test_stationary.py:24: energies, _ = eigenstates(grid, HarmonicTrap((wx, wy)), n_states=6, method='lobpcg')
  tests/test_stationary.py:31: energies, states = eigenstates(grid, HarmonicTrap(1.0), n_states=4)
  tests/test_stationary.py:41: e_l, _ = eigenstates(grid, pot, n_states=5, method='lanczos')
  tests/test_stationary.py:42: e_b, _ = eigenstates(grid, pot, n_states=5, method='lobpcg', tol=1e-7)
  tests/test_strongfield.py:34: energies, _ = eigenstates(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), n_states=2)
EXT_OTHER (11):
  benchmarks/validation_suite.py:119: E, _ = eigenstates(grid, HarmonicTrap(1.0), n_states=10, method='lanczos')
  benchmarks/validation_suite.py:124: E, _ = eigenstates(grid, HarmonicTrap(w), n_states=6, method='lobpcg')
  benchmarks/validation_suite.py:211: E, states = eigenstates(grid, atom, n_states=1)
  examples/10_quantum_chaos_stadium.py:41: energies, states = eigenstates(grid, stadium, n_states=n_states, method='lobpcg', tol=1e-6)
  examples/12_high_harmonic_generation.py:94: energies, states = eigenstates(GRID, atom, n_states=1)
  tests/test_stationary.py:16: energies, states = eigenstates(grid, HarmonicTrap(1.3), n_states=8, method='lanczos')
  tests/test_stationary.py:24: energies, _ = eigenstates(grid, HarmonicTrap((wx, wy)), n_states=6, method='lobpcg')
  tests/test_stationary.py:31: energies, states = eigenstates(grid, HarmonicTrap(1.0), n_states=4)
  tests/test_stationary.py:41: e_l, _ = eigenstates(grid, pot, n_states=5, method='lanczos')
  tests/test_stationary.py:42: e_b, _ = eigenstates(grid, pot, n_states=5, method='lobpcg', tol=1e-7)
  tests/test_strongfield.py:34: energies, _ = eigenstates(Grid1D(2048, -100.0, 100.0), SoftCoulomb(), n_states=2)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (6): benchmarks/validation_suite.py:21(quantumlab.stationary), examples/10_quantum_chaos_stadium.py:26(quantumlab.stationary), examples/12_high_harmonic_generation.py:44(quantumlab.stationary), tests/test_stationary.py:5(quantumlab.stationary), tests/test_strongfield.py:6(quantumlab.stationary), quantumlab/stationary/__init__.py:1(quantumlab.stationary.eigensolver)

## apply_hamiltonian  [quantumlab/stationary/hamiltonian.py:6] (function)
SIG: def apply_hamiltonian(psi: np.ndarray, grid, V: np.ndarray, hbar: float = 1.0, m: float = 1.0,
                      nonlinearity: float = 0.0, workers: int = -1, rotation: float = 0.0) -> np.ndarray:
EXT_CALLS (5):
  quantumlab/stationary/conjugate_gradient.py:63: return apply_hamiltonian(p, grid, V, hbar, m, nonlinearity=g, workers=workers, rotation=rotation)
  quantumlab/stationary/imaginary_time.py:31: H_lin = apply_hamiltonian(psi, grid, V, hbar, m, rotation=rotation)
  quantumlab/stationary/imaginary_time.py:184: H_lin = apply_hamiltonian(p, grid, Vs[i], hbar, m, rotation=rotation)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
EXT_OTHER (5):
  quantumlab/stationary/conjugate_gradient.py:63: return apply_hamiltonian(p, grid, V, hbar, m, nonlinearity=g, workers=workers, rotation=rotation)
  quantumlab/stationary/imaginary_time.py:31: H_lin = apply_hamiltonian(psi, grid, V, hbar, m, rotation=rotation)
  quantumlab/stationary/imaginary_time.py:184: H_lin = apply_hamiltonian(p, grid, Vs[i], hbar, m, rotation=rotation)
  tests/test_rotation.py:131: H_psi = apply_hamiltonian(psi, grid, HarmonicTrap(1.0).evaluate(grid), rotation=0.6)
  tests/test_stationary.py:34: H_psi = apply_hamiltonian(wf.psi, grid, HarmonicTrap(1.0).evaluate(grid))
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): tests/test_rotation.py:128(quantumlab.stationary), tests/test_stationary.py:5(quantumlab.stationary), quantumlab/stationary/__init__.py:4(quantumlab.stationary.hamiltonian), quantumlab/stationary/conjugate_gradient.py:20(quantumlab.stationary.hamiltonian), quantumlab/stationary/imaginary_time.py:13(quantumlab.stationary.hamiltonian)

## ConvergenceInfo  [quantumlab/stationary/imaginary_time.py:18] (class)
SIG: class ConvergenceInfo(...):
EXT_CALLS (1):
  quantumlab/stationary/conjugate_gradient.py:132: return wavefunction_class(grid)(grid, psi), ConvergenceInfo(converged, it, E0, mu, residual)
EXT_OTHER (1):
  quantumlab/stationary/conjugate_gradient.py:132: return wavefunction_class(grid)(grid, psi), ConvergenceInfo(converged, it, E0, mu, residual)
INT_CALLS (1): quantumlab/stationary/imaginary_time.py:139
INT_OTHER (1): quantumlab/stationary/imaginary_time.py:139
IMPORTS (2): quantumlab/stationary/__init__.py:2(quantumlab.stationary.imaginary_time), quantumlab/stationary/conjugate_gradient.py:21(quantumlab.stationary.imaginary_time)

## _inner  [quantumlab/stationary/imaginary_time.py:26] (function)
SIG: def _inner(a, b, dV):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (6): quantumlab/stationary/imaginary_time.py:32, quantumlab/stationary/imaginary_time.py:35, quantumlab/stationary/imaginary_time.py:115, quantumlab/stationary/imaginary_time.py:116, quantumlab/stationary/imaginary_time.py:185, quantumlab/stationary/imaginary_time.py:187
INT_OTHER (6): quantumlab/stationary/imaginary_time.py:32, quantumlab/stationary/imaginary_time.py:35, quantumlab/stationary/imaginary_time.py:115, quantumlab/stationary/imaginary_time.py:116, quantumlab/stationary/imaginary_time.py:185, quantumlab/stationary/imaginary_time.py:187
IMPORTS (0): 

## _energy_and_mu  [quantumlab/stationary/imaginary_time.py:30] (function)
SIG: def _energy_and_mu(psi, grid, V, hbar, m, g, dV, rotation=0.0):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/stationary/imaginary_time.py:132, quantumlab/stationary/imaginary_time.py:138
INT_OTHER (2): quantumlab/stationary/imaginary_time.py:132, quantumlab/stationary/imaginary_time.py:138
IMPORTS (0): 

## _default_guess  [quantumlab/stationary/imaginary_time.py:40] (function)
SIG: def _default_guess(grid):
EXT_CALLS (1):
  quantumlab/stationary/conjugate_gradient.py:54: psi = _default_guess(grid) if initial is None else np.array(getattr(initial, 'psi', initial), dtype=complex)
EXT_OTHER (1):
  quantumlab/stationary/conjugate_gradient.py:54: psi = _default_guess(grid) if initial is None else np.array(getattr(initial, 'psi', initial), dtype=complex)
INT_CALLS (2): quantumlab/stationary/imaginary_time.py:109, quantumlab/stationary/imaginary_time.py:157
INT_OTHER (2): quantumlab/stationary/imaginary_time.py:109, quantumlab/stationary/imaginary_time.py:157
IMPORTS (1): quantumlab/stationary/conjugate_gradient.py:21(quantumlab.stationary.imaginary_time)

## ground_state  [quantumlab/stationary/imaginary_time.py:47] (function)
SIG: def ground_state(grid, potential, dtau: float = 0.01, nonlinearity: float = 0.0,
                 initial=None, tol: float = 1e-11, max_steps: int = 50000,
                 check_interval: int = 20, hbar: float = 1.0, m: float = 1.0,
                 orthogonal_to: Optional[List] = None, workers: int = -1,
                 rotation: float = 0.0, backend='numpy'):
EXT_CALLS (25):
  benchmarks/validation_suite.py:129: _, info = ground_state(grid, HarmonicTrap(w), dtau=0.01)
  benchmarks/validation_suite.py:172: wf, info = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  benchmarks/validation_suite.py:181: _, a = ground_state(grid, trap, dtau=0.02, nonlinearity=50.0, tol=1e-13)
  benchmarks/validation_suite.py:182: _, b = ground_state(grid, trap, dtau=0.01, nonlinearity=50.0, tol=1e-13)
  benchmarks/validation_suite.py:290: single, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=G)
  examples/08_3d_bec_time_of_flight.py:83: wf0, info = ground_state(grid, trap, dtau=0.005, nonlinearity=g, initial=psi_tf, tol=1e-10)
  examples/11_rotating_bec_vortex_lattice.py:71: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, nonlinearity=g2)
  examples/11_rotating_bec_vortex_lattice.py:162: wf3, info_it = ground_state(grid3, trap3, dtau=0.02, nonlinearity=g3, rotation=Om, initial=wf3,
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:140: wf_n, info_n = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0)
  tests/test_conjugate_gradient.py:36: _, it = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_conjugate_gradient.py:52: no_vortex, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_conjugate_gradient.py:55: _, it = ground_state(grid, trap, dtau=0.005, nonlinearity=g, rotation=Om, initial=lattice, max_steps=2000)
  tests/test_gross_pitaevskii.py:44: wf0, _ = ground_state(grid, trap, dtau=0.01, nonlinearity=g)
  tests/test_gross_pitaevskii.py:63: wf, info = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_gross_pitaevskii.py:75: wf0, _ = ground_state(grid, trap, dtau=0.01, nonlinearity=0.0)
  tests/test_gross_pitaevskii.py:76: wf1, _ = ground_state(grid, trap, dtau=0.01, nonlinearity=100.0)
  tests/test_multicomponent.py:39: single, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_rotation.py:102: no_vortex, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_rotation.py:138: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, rotation=0.6)
  tests/test_stationary.py:48: wf, info = ground_state(grid, HarmonicTrap((1.0, 1.2, 1.4)), dtau=0.01)
  tests/test_stationary.py:66: _, i1 = ground_state(grid, pot, dtau=0.02, tol=1e-14)
  tests/test_stationary.py:67: _, i2 = ground_state(grid, pot, dtau=0.01, tol=1e-14)
  tests/test_stationary.py:76: _, single = ground_state(grid, trap, dtau=0.0025, nonlinearity=g, tol=1e-12, max_steps=200000)
  tests/test_stationary.py:77: _, staged = ground_state(grid, trap, dtau=[0.04, 0.01, 0.0025], nonlinearity=g, tol=1e-12, max_steps=200000)
EXT_OTHER (25):
  benchmarks/validation_suite.py:129: _, info = ground_state(grid, HarmonicTrap(w), dtau=0.01)
  benchmarks/validation_suite.py:172: wf, info = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  benchmarks/validation_suite.py:181: _, a = ground_state(grid, trap, dtau=0.02, nonlinearity=50.0, tol=1e-13)
  benchmarks/validation_suite.py:182: _, b = ground_state(grid, trap, dtau=0.01, nonlinearity=50.0, tol=1e-13)
  benchmarks/validation_suite.py:290: single, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=G)
  examples/08_3d_bec_time_of_flight.py:83: wf0, info = ground_state(grid, trap, dtau=0.005, nonlinearity=g, initial=psi_tf, tol=1e-10)
  examples/11_rotating_bec_vortex_lattice.py:71: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, nonlinearity=g2)
  examples/11_rotating_bec_vortex_lattice.py:162: wf3, info_it = ground_state(grid3, trap3, dtau=0.02, nonlinearity=g3, rotation=Om, initial=wf3,
  tests/test_backends.py:139: wf_d, info_d = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0, backend=backend)
  tests/test_backends.py:140: wf_n, info_n = ground_state(grid, HarmonicTrap(1.0), dtau=0.01, nonlinearity=10.0)
  tests/test_conjugate_gradient.py:36: _, it = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_conjugate_gradient.py:52: no_vortex, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_conjugate_gradient.py:55: _, it = ground_state(grid, trap, dtau=0.005, nonlinearity=g, rotation=Om, initial=lattice, max_steps=2000)
  tests/test_gross_pitaevskii.py:44: wf0, _ = ground_state(grid, trap, dtau=0.01, nonlinearity=g)
  tests/test_gross_pitaevskii.py:63: wf, info = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_gross_pitaevskii.py:75: wf0, _ = ground_state(grid, trap, dtau=0.01, nonlinearity=0.0)
  tests/test_gross_pitaevskii.py:76: wf1, _ = ground_state(grid, trap, dtau=0.01, nonlinearity=100.0)
  tests/test_multicomponent.py:39: single, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_rotation.py:102: no_vortex, _ = ground_state(grid, trap, dtau=0.005, nonlinearity=g)
  tests/test_rotation.py:138: wf, info = ground_state(grid, HarmonicTrap(1.0), dtau=0.005, rotation=0.6)
  tests/test_stationary.py:48: wf, info = ground_state(grid, HarmonicTrap((1.0, 1.2, 1.4)), dtau=0.01)
  tests/test_stationary.py:66: _, i1 = ground_state(grid, pot, dtau=0.02, tol=1e-14)
  tests/test_stationary.py:67: _, i2 = ground_state(grid, pot, dtau=0.01, tol=1e-14)
  tests/test_stationary.py:76: _, single = ground_state(grid, trap, dtau=0.0025, nonlinearity=g, tol=1e-12, max_steps=200000)
  tests/test_stationary.py:77: _, staged = ground_state(grid, trap, dtau=[0.04, 0.01, 0.0025], nonlinearity=g, tol=1e-12, max_steps=200000)
INT_CALLS (2): quantumlab/stationary/imaginary_time.py:93, quantumlab/stationary/imaginary_time.py:161
INT_OTHER (2): quantumlab/stationary/imaginary_time.py:93, quantumlab/stationary/imaginary_time.py:161
IMPORTS (10): benchmarks/validation_suite.py:21(quantumlab.stationary), examples/08_3d_bec_time_of_flight.py:34(quantumlab.stationary), examples/11_rotating_bec_vortex_lattice.py:45(quantumlab.stationary), tests/test_backends.py:20(quantumlab.stationary), tests/test_conjugate_gradient.py:7(quantumlab.stationary), tests/test_gross_pitaevskii.py:7(quantumlab.stationary), tests/test_multicomponent.py:8(quantumlab.stationary), tests/test_rotation.py:7(quantumlab.stationary), tests/test_stationary.py:5(quantumlab.stationary), quantumlab/stationary/__init__.py:2(quantumlab.stationary.imaginary_time)

## excited_states  [quantumlab/stationary/imaginary_time.py:142] (function)
SIG: def excited_states(grid, potential, n_states: int, dtau: float = 0.01, tol: float = 1e-11,
                   max_steps: int = 50000, seed: int = 0, hbar: float = 1.0, m: float = 1.0,
                   workers: int = -1):
EXT_CALLS (2):
  examples/10_quantum_chaos_stadium.py:44: e_it, _, infos = excited_states(grid, stadium, n_states=3, dtau=0.002)
  tests/test_stationary.py:57: e_it, states, infos = excited_states(grid, pot, n_states=4, dtau=0.005)
EXT_OTHER (2):
  examples/10_quantum_chaos_stadium.py:44: e_it, _, infos = excited_states(grid, stadium, n_states=3, dtau=0.002)
  tests/test_stationary.py:57: e_it, states, infos = excited_states(grid, pot, n_states=4, dtau=0.005)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (3): examples/10_quantum_chaos_stadium.py:26(quantumlab.stationary), tests/test_stationary.py:5(quantumlab.stationary), quantumlab/stationary/__init__.py:2(quantumlab.stationary.imaginary_time)

## CoupledConvergenceInfo  [quantumlab/stationary/imaginary_time.py:171] (class)
SIG: class CoupledConvergenceInfo(...):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/stationary/imaginary_time.py:237
INT_OTHER (1): quantumlab/stationary/imaginary_time.py:237
IMPORTS (1): quantumlab/stationary/__init__.py:2(quantumlab.stationary.imaginary_time)

## _coupled_energy_mu  [quantumlab/stationary/imaginary_time.py:179] (function)
SIG: def _coupled_energy_mu(psis, grid, Vs, g, hbar, m, rotation, dV):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (2): quantumlab/stationary/imaginary_time.py:231, quantumlab/stationary/imaginary_time.py:236
INT_OTHER (2): quantumlab/stationary/imaginary_time.py:231, quantumlab/stationary/imaginary_time.py:236
IMPORTS (0): 

## coupled_ground_state  [quantumlab/stationary/imaginary_time.py:195] (function)
SIG: def coupled_ground_state(grid, potentials, couplings, initial, dtau: float = 0.005, tol: float = 1e-11,
                         max_steps: int = 50000, check_interval: int = 20, hbar: float = 1.0,
                         m: float = 1.0, rotation: float = 0.0, backend='numpy', workers: int = -1):
EXT_CALLS (6):
  benchmarks/validation_suite.py:289: (s1, s2), _ = coupled_ground_state(grid, (trap, trap), [[G, G], [G, G]], (a, b), dtau=0.005)
  benchmarks/validation_suite.py:301: states, _ = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G2, (a, b), dtau=0.005)
  examples/13_two_component_bec.py:73: states, info = coupled_ground_state(grid, (trap, trap), [[g, r * g], [r * g, g]],
  examples/13_two_component_bec.py:198: (s1, s2), info = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G,
  tests/test_multicomponent.py:36: (s1, s2), info = coupled_ground_state(grid, (trap, trap), [[g, g], [g, g]],
  tests/test_multicomponent.py:112: states, info = coupled_ground_state(grid, (trap, trap), G, (_gauss2d(grid, 1.5, norm=0.5), _gauss2d(grid, -1.5, norm=0.5)),
EXT_OTHER (6):
  benchmarks/validation_suite.py:289: (s1, s2), _ = coupled_ground_state(grid, (trap, trap), [[G, G], [G, G]], (a, b), dtau=0.005)
  benchmarks/validation_suite.py:301: states, _ = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G2, (a, b), dtau=0.005)
  examples/13_two_component_bec.py:73: states, info = coupled_ground_state(grid, (trap, trap), [[g, r * g], [r * g, g]],
  examples/13_two_component_bec.py:198: (s1, s2), info = coupled_ground_state(grid, (HarmonicTrap(1.0), HarmonicTrap(1.0)), G,
  tests/test_multicomponent.py:36: (s1, s2), info = coupled_ground_state(grid, (trap, trap), [[g, g], [g, g]],
  tests/test_multicomponent.py:112: states, info = coupled_ground_state(grid, (trap, trap), G, (_gauss2d(grid, 1.5, norm=0.5), _gauss2d(grid, -1.5, norm=0.5)),
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): benchmarks/validation_suite.py:247(quantumlab.stationary), examples/13_two_component_bec.py:43(quantumlab.stationary), tests/test_multicomponent.py:8(quantumlab.stationary), quantumlab/stationary/__init__.py:2(quantumlab.stationary.imaginary_time)

## transmission_coefficient  [quantumlab/observables/coefficients.py:4] (function)
SIG: def transmission_coefficient(wf, barrier_position: float=0.0) -> float:
EXT_CALLS (3):
  examples/01_gaussian_barrier.py:48: T = transmission_coefficient(wf_current, barrier_center)
  examples/04_multiple_barriers.py:49: T = transmission_coefficient(wf_current, boundary)
  tests/test_3d_observables.py:65: T = transmission_coefficient(wf, barrier_position=p['x0'])
EXT_OTHER (3):
  examples/01_gaussian_barrier.py:48: T = transmission_coefficient(wf_current, barrier_center)
  examples/04_multiple_barriers.py:49: T = transmission_coefficient(wf_current, boundary)
  tests/test_3d_observables.py:65: T = transmission_coefficient(wf, barrier_position=p['x0'])
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): examples/01_gaussian_barrier.py:9(quantumlab.observables.coefficients), examples/04_multiple_barriers.py:8(quantumlab.observables.coefficients), quantumlab/observables/__init__.py:2(quantumlab.observables.coefficients), tests/test_3d_observables.py:11(quantumlab.observables.coefficients)

## reflection_coefficient  [quantumlab/observables/coefficients.py:18] (function)
SIG: def reflection_coefficient(wf, barrier_position: float=0.0) -> float:
EXT_CALLS (3):
  examples/01_gaussian_barrier.py:47: R = reflection_coefficient(wf_current, barrier_center)
  examples/04_multiple_barriers.py:48: R = reflection_coefficient(wf_current, boundary)
  tests/test_3d_observables.py:66: R = reflection_coefficient(wf, barrier_position=p['x0'])
EXT_OTHER (3):
  examples/01_gaussian_barrier.py:47: R = reflection_coefficient(wf_current, barrier_center)
  examples/04_multiple_barriers.py:48: R = reflection_coefficient(wf_current, boundary)
  tests/test_3d_observables.py:66: R = reflection_coefficient(wf, barrier_position=p['x0'])
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): examples/01_gaussian_barrier.py:9(quantumlab.observables.coefficients), examples/04_multiple_barriers.py:8(quantumlab.observables.coefficients), quantumlab/observables/__init__.py:2(quantumlab.observables.coefficients), tests/test_3d_observables.py:11(quantumlab.observables.coefficients)

## gradient  [quantumlab/observables/current.py:11] (function)
SIG: def gradient(psi: np.ndarray, grid):
EXT_CALLS (3):
  quantumlab/strongfield.py:127: dV = base_potential.gradient(grid)[0]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  tests/test_strongfield.py:45: gx, gy = pot.gradient(grid)
EXT_OTHER (3):
  quantumlab/strongfield.py:127: dV = base_potential.gradient(grid)[0]
  quantumlab/strongfield.py:130: dV = np.real(gradient(base_potential.evaluate(grid).astype(complex), grid)[0])
  tests/test_strongfield.py:45: gx, gy = pot.gradient(grid)
INT_CALLS (2): quantumlab/observables/current.py:23, quantumlab/observables/current.py:30
INT_OTHER (2): quantumlab/observables/current.py:23, quantumlab/observables/current.py:30
IMPORTS (2): quantumlab/observables/__init__.py:6(quantumlab.observables.current), quantumlab/strongfield.py:129(quantumlab.observables.current)

## probability_current  [quantumlab/observables/current.py:17] (function)
SIG: def probability_current(wf, hbar: float = 1.0, m: float = 1.0):
EXT_CALLS (2):
  tests/test_new_potentials_and_observables.py:87: (j,) = probability_current(wf)
  tests/test_new_potentials_and_observables.py:95: for j, axis in zip(probability_current(wf), 'xyz'):
EXT_OTHER (2):
  tests/test_new_potentials_and_observables.py:87: (j,) = probability_current(wf)
  tests/test_new_potentials_and_observables.py:95: for j, axis in zip(probability_current(wf), 'xyz'):
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): tests/test_new_potentials_and_observables.py:10(quantumlab.observables), quantumlab/observables/__init__.py:6(quantumlab.observables.current)

## angular_momentum_z_expectation  [quantumlab/observables/current.py:26] (function)
SIG: def angular_momentum_z_expectation(wf, hbar: float = 1.0) -> float:
EXT_CALLS (10):
  benchmarks/validation_suite.py:114: '|⟨L_z⟩ − 1|', abs(angular_momentum_z_expectation(wf) - 1.0), 1e-10)
  examples/11_rotating_bec_vortex_lattice.py:104: Lz.append(angular_momentum_z_expectation(wf))
  examples/13_two_component_bec.py:225: f'⟨L_z⟩ = {angular_momentum_z_expectation(state[0]):.2f} + {angular_momentum_z_expectation(state[1]):.2f}')
  tests/test_conjugate_gradient.py:59: assert angular_momentum_z_expectation(wf) > 2.0
  tests/test_new_potentials_and_observables.py:104: assert angular_momentum_z_expectation(wf) == pytest.approx(float(ell), abs=1e-10)
  tests/test_rotation.py:58: assert angular_momentum_z_expectation(wf) == pytest.approx(1.0, abs=1e-10)
  tests/test_rotation.py:68: return total_energy_expectation(w, trap) - Om * angular_momentum_z_expectation(w)
  tests/test_rotation.py:108: return gross_pitaevskii_energy(w, trap, g) - Om * angular_momentum_z_expectation(w)
  tests/test_rotation.py:110: assert angular_momentum_z_expectation(lattice) > 2.0
  tests/test_rotation.py:140: assert angular_momentum_z_expectation(wf) == pytest.approx(0.0, abs=1e-8)
EXT_OTHER (10):
  benchmarks/validation_suite.py:114: '|⟨L_z⟩ − 1|', abs(angular_momentum_z_expectation(wf) - 1.0), 1e-10)
  examples/11_rotating_bec_vortex_lattice.py:104: Lz.append(angular_momentum_z_expectation(wf))
  examples/13_two_component_bec.py:225: f'⟨L_z⟩ = {angular_momentum_z_expectation(state[0]):.2f} + {angular_momentum_z_expectation(state[1]):.2f}')
  tests/test_conjugate_gradient.py:59: assert angular_momentum_z_expectation(wf) > 2.0
  tests/test_new_potentials_and_observables.py:104: assert angular_momentum_z_expectation(wf) == pytest.approx(float(ell), abs=1e-10)
  tests/test_rotation.py:58: assert angular_momentum_z_expectation(wf) == pytest.approx(1.0, abs=1e-10)
  tests/test_rotation.py:68: return total_energy_expectation(w, trap) - Om * angular_momentum_z_expectation(w)
  tests/test_rotation.py:108: return gross_pitaevskii_energy(w, trap, g) - Om * angular_momentum_z_expectation(w)
  tests/test_rotation.py:110: assert angular_momentum_z_expectation(lattice) > 2.0
  tests/test_rotation.py:140: assert angular_momentum_z_expectation(wf) == pytest.approx(0.0, abs=1e-8)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (7): benchmarks/validation_suite.py:22(quantumlab.observables), examples/11_rotating_bec_vortex_lattice.py:47(quantumlab.observables), examples/13_two_component_bec.py:44(quantumlab.observables), tests/test_conjugate_gradient.py:8(quantumlab.observables), tests/test_new_potentials_and_observables.py:10(quantumlab.observables), tests/test_rotation.py:8(quantumlab.observables), quantumlab/observables/__init__.py:6(quantumlab.observables.current)

## autocorrelation  [quantumlab/observables/current.py:35] (function)
SIG: def autocorrelation(psi0, psi_t, grid) -> complex:
EXT_CALLS (4):
  benchmarks/validation_suite.py:142: C[i] = autocorrelation(wf0.psi, wf.psi, grid)
  benchmarks/validation_suite.py:203: C = autocorrelation(wf0.psi, solver.evolve(wf0, 500).psi, grid)
  tests/test_new_potentials_and_observables.py:117: C[n] = autocorrelation(wf0.psi, wf.psi, grid)
  tests/test_rotation.py:55: C = autocorrelation(wf0.psi, wf.psi, grid)
EXT_OTHER (4):
  benchmarks/validation_suite.py:142: C[i] = autocorrelation(wf0.psi, wf.psi, grid)
  benchmarks/validation_suite.py:203: C = autocorrelation(wf0.psi, solver.evolve(wf0, 500).psi, grid)
  tests/test_new_potentials_and_observables.py:117: C[n] = autocorrelation(wf0.psi, wf.psi, grid)
  tests/test_rotation.py:55: C = autocorrelation(wf0.psi, wf.psi, grid)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): benchmarks/validation_suite.py:22(quantumlab.observables), tests/test_new_potentials_and_observables.py:10(quantumlab.observables), tests/test_rotation.py:8(quantumlab.observables), quantumlab/observables/__init__.py:6(quantumlab.observables.current)

## vortex_positions  [quantumlab/observables/current.py:40] (function)
SIG: def vortex_positions(wf, min_density: float = 0.2, smoothing: float = 1.0):
EXT_CALLS (9):
  examples/11_rotating_bec_vortex_lattice.py:101: pos, q = vortex_positions(wf)
  examples/11_rotating_bec_vortex_lattice.py:114: pos, q = vortex_positions(wf)
  examples/11_rotating_bec_vortex_lattice.py:175: pos3, q3 = vortex_positions(mid)
  examples/11_rotating_bec_vortex_lattice.py:187: p, _ = vortex_positions(WaveFunction2D(mid.grid, wf3.psi[:, :, k]))
  examples/13_two_component_bec.py:222: n1v = len(vortex_positions(state[0])[0])
  examples/13_two_component_bec.py:223: n2v = len(vortex_positions(state[1])[0])
  examples/13_two_component_bec.py:229: p1, q1 = vortex_positions(s1)
  examples/13_two_component_bec.py:230: p2, q2 = vortex_positions(s2)
  tests/test_new_potentials_and_observables.py:135: pos, charge = vortex_positions(WaveFunction2D(grid, psi))
EXT_OTHER (9):
  examples/11_rotating_bec_vortex_lattice.py:101: pos, q = vortex_positions(wf)
  examples/11_rotating_bec_vortex_lattice.py:114: pos, q = vortex_positions(wf)
  examples/11_rotating_bec_vortex_lattice.py:175: pos3, q3 = vortex_positions(mid)
  examples/11_rotating_bec_vortex_lattice.py:187: p, _ = vortex_positions(WaveFunction2D(mid.grid, wf3.psi[:, :, k]))
  examples/13_two_component_bec.py:222: n1v = len(vortex_positions(state[0])[0])
  examples/13_two_component_bec.py:223: n2v = len(vortex_positions(state[1])[0])
  examples/13_two_component_bec.py:229: p1, q1 = vortex_positions(s1)
  examples/13_two_component_bec.py:230: p2, q2 = vortex_positions(s2)
  tests/test_new_potentials_and_observables.py:135: pos, charge = vortex_positions(WaveFunction2D(grid, psi))
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): examples/11_rotating_bec_vortex_lattice.py:47(quantumlab.observables), examples/13_two_component_bec.py:44(quantumlab.observables), tests/test_new_potentials_and_observables.py:128(quantumlab.observables), quantumlab/observables/__init__.py:6(quantumlab.observables.current)

## position_expectation  [quantumlab/observables/expectation.py:4] (function)
SIG: def position_expectation(wf) -> float:
EXT_CALLS (17):
  benchmarks/validation_suite.py:77: err = max(err, abs(position_expectation(wf) - x_cl))
  benchmarks/validation_suite.py:197: err = max(err, abs(position_expectation(wf) - x0 * np.cos(t) * np.cos(Om * t)),
  examples/01_gaussian_barrier.py:43: x_mean = position_expectation(wf_current)
  examples/02_harmonic_oscillator.py:35: positions = [position_expectation(wf)]
  examples/02_harmonic_oscillator.py:43: x_mean = position_expectation(wf_current)
  examples/03_double_well.py:36: positions = [position_expectation(wf)]
  examples/03_double_well.py:43: x_mean = position_expectation(wf_current)
  examples/04_multiple_barriers.py:44: x_mean = position_expectation(wf_current)
  examples/05_2d_gaussian_barrier.py:63: x_exp = position_expectation(wf_current)
  quantumlab/runner.py:171: x = position_expectation(wf_current)
  testbench_interlock.py:110: x_exp = position_expectation(wf)
  tests/test_3d_observables.py:26: assert position_expectation(wf) == pytest.approx(p['x0'], abs=1e-6)
  tests/test_observables.py:14: assert position_expectation(wf) == pytest.approx(x0, abs=1e-05)
  tests/test_rotation.py:31: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=tol)
  tests/test_rotation.py:43: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=1e-7)
  tests/test_split_operator.py:101: assert position_expectation(wf) == pytest.approx(x_cl, abs=1e-7)
  tests/test_strongfield.py:101: assert a == pytest.approx(-position_expectation(wf) + 0.25, abs=1e-10)
EXT_OTHER (17):
  benchmarks/validation_suite.py:77: err = max(err, abs(position_expectation(wf) - x_cl))
  benchmarks/validation_suite.py:197: err = max(err, abs(position_expectation(wf) - x0 * np.cos(t) * np.cos(Om * t)),
  examples/01_gaussian_barrier.py:43: x_mean = position_expectation(wf_current)
  examples/02_harmonic_oscillator.py:35: positions = [position_expectation(wf)]
  examples/02_harmonic_oscillator.py:43: x_mean = position_expectation(wf_current)
  examples/03_double_well.py:36: positions = [position_expectation(wf)]
  examples/03_double_well.py:43: x_mean = position_expectation(wf_current)
  examples/04_multiple_barriers.py:44: x_mean = position_expectation(wf_current)
  examples/05_2d_gaussian_barrier.py:63: x_exp = position_expectation(wf_current)
  quantumlab/runner.py:171: x = position_expectation(wf_current)
  testbench_interlock.py:110: x_exp = position_expectation(wf)
  tests/test_3d_observables.py:26: assert position_expectation(wf) == pytest.approx(p['x0'], abs=1e-6)
  tests/test_observables.py:14: assert position_expectation(wf) == pytest.approx(x0, abs=1e-05)
  tests/test_rotation.py:31: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=tol)
  tests/test_rotation.py:43: assert position_expectation(wf) == pytest.approx(x0 * np.cos(t) * np.cos(Om * t), abs=1e-7)
  tests/test_split_operator.py:101: assert position_expectation(wf) == pytest.approx(x_cl, abs=1e-7)
  tests/test_strongfield.py:101: assert a == pytest.approx(-position_expectation(wf) + 0.25, abs=1e-10)
INT_CALLS (1): quantumlab/observables/expectation.py:27
INT_OTHER (1): quantumlab/observables/expectation.py:27
IMPORTS (14): benchmarks/validation_suite.py:22(quantumlab.observables), testbench_interlock.py:38(quantumlab.observables), tests/test_rotation.py:8(quantumlab.observables), tests/test_split_operator.py:12(quantumlab.observables), tests/test_strongfield.py:7(quantumlab.observables), examples/01_gaussian_barrier.py:8(quantumlab.observables.expectation), examples/02_harmonic_oscillator.py:8(quantumlab.observables.expectation), examples/03_double_well.py:7(quantumlab.observables.expectation), examples/04_multiple_barriers.py:7(quantumlab.observables.expectation), examples/05_2d_gaussian_barrier.py:8(quantumlab.observables.expectation), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), quantumlab/runner.py:18(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation), tests/test_observables.py:5(quantumlab.observables.expectation)

## position_squared_expectation  [quantumlab/observables/expectation.py:15] (function)
SIG: def position_squared_expectation(wf) -> float:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/observables/expectation.py:28
INT_OTHER (1): quantumlab/observables/expectation.py:28
IMPORTS (1): quantumlab/observables/__init__.py:1(quantumlab.observables.expectation)

## position_uncertainty  [quantumlab/observables/expectation.py:26] (function)
SIG: def position_uncertainty(wf) -> float:
EXT_CALLS (8):
  benchmarks/validation_suite.py:103: err = max(abs(position_uncertainty(wf) * momentum_uncertainty(wf, 'x') - 0.5),
  examples/01_gaussian_barrier.py:44: dx = position_uncertainty(wf_current)
  examples/05_2d_gaussian_barrier.py:65: dx    = position_uncertainty(wf_current)
  examples/08_3d_bec_time_of_flight.py:61: return np.array([position_uncertainty(wf), y_uncertainty(wf), z_uncertainty(wf)])
  tests/test_3d_observables.py:29: assert position_uncertainty(wf) == pytest.approx(p['sigma_x'], abs=1e-6)
  tests/test_3d_observables.py:38: ('x', p['k0_x'], p['sigma_x'], position_uncertainty(wf)),
  tests/test_observables.py:15: assert position_uncertainty(wf) == pytest.approx(sigma, abs=1e-05)
  tests/test_observables.py:19: dx = position_uncertainty(wf)
EXT_OTHER (9):
  benchmarks/validation_suite.py:103: err = max(abs(position_uncertainty(wf) * momentum_uncertainty(wf, 'x') - 0.5),
  examples/01_gaussian_barrier.py:44: dx = position_uncertainty(wf_current)
  examples/05_2d_gaussian_barrier.py:65: dx    = position_uncertainty(wf_current)
  examples/08_3d_bec_time_of_flight.py:61: return np.array([position_uncertainty(wf), y_uncertainty(wf), z_uncertainty(wf)])
  tests/test_3d_observables.py:29: assert position_uncertainty(wf) == pytest.approx(p['sigma_x'], abs=1e-6)
  tests/test_3d_observables.py:38: ('x', p['k0_x'], p['sigma_x'], position_uncertainty(wf)),
  tests/test_gross_pitaevskii.py:77: for f in (position_uncertainty, y_uncertainty, z_uncertainty):
  tests/test_observables.py:15: assert position_uncertainty(wf) == pytest.approx(sigma, abs=1e-05)
  tests/test_observables.py:19: dx = position_uncertainty(wf)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (8): benchmarks/validation_suite.py:22(quantumlab.observables), examples/08_3d_bec_time_of_flight.py:36(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), examples/01_gaussian_barrier.py:8(quantumlab.observables.expectation), examples/05_2d_gaussian_barrier.py:8(quantumlab.observables.expectation), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation), tests/test_observables.py:5(quantumlab.observables.expectation)

## y_expectation  [quantumlab/observables/expectation.py:32] (function)
SIG: def y_expectation(wf) -> float:
EXT_CALLS (5):
  benchmarks/validation_suite.py:198: abs(y_expectation(wf) + x0 * np.cos(t) * np.sin(Om * t)))
  examples/05_2d_gaussian_barrier.py:64: y_exp = y_expectation(wf_current)
  tests/test_3d_observables.py:27: assert y_expectation(wf) == pytest.approx(p['y0'], abs=1e-6)
  tests/test_rotation.py:32: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=tol)
  tests/test_rotation.py:44: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=1e-7)
EXT_OTHER (5):
  benchmarks/validation_suite.py:198: abs(y_expectation(wf) + x0 * np.cos(t) * np.sin(Om * t)))
  examples/05_2d_gaussian_barrier.py:64: y_exp = y_expectation(wf_current)
  tests/test_3d_observables.py:27: assert y_expectation(wf) == pytest.approx(p['y0'], abs=1e-6)
  tests/test_rotation.py:32: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=tol)
  tests/test_rotation.py:44: assert y_expectation(wf) == pytest.approx(-x0 * np.cos(t) * np.sin(Om * t), abs=1e-7)
INT_CALLS (1): quantumlab/observables/expectation.py:51
INT_OTHER (1): quantumlab/observables/expectation.py:51
IMPORTS (5): benchmarks/validation_suite.py:22(quantumlab.observables), tests/test_rotation.py:8(quantumlab.observables), examples/05_2d_gaussian_barrier.py:8(quantumlab.observables.expectation), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation)

## y_squared_expectation  [quantumlab/observables/expectation.py:41] (function)
SIG: def y_squared_expectation(wf) -> float:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/observables/expectation.py:52
INT_OTHER (1): quantumlab/observables/expectation.py:52
IMPORTS (1): quantumlab/observables/__init__.py:1(quantumlab.observables.expectation)

## y_uncertainty  [quantumlab/observables/expectation.py:50] (function)
SIG: def y_uncertainty(wf) -> float:
EXT_CALLS (5):
  benchmarks/validation_suite.py:104: abs(y_uncertainty(wf) * momentum_uncertainty(wf, 'y') - 0.5),
  examples/05_2d_gaussian_barrier.py:66: dy    = y_uncertainty(wf_current)
  examples/08_3d_bec_time_of_flight.py:61: return np.array([position_uncertainty(wf), y_uncertainty(wf), z_uncertainty(wf)])
  tests/test_3d_observables.py:30: assert y_uncertainty(wf) == pytest.approx(p['sigma_y'], abs=1e-6)
  tests/test_3d_observables.py:39: ('y', p['k0_y'], p['sigma_y'], y_uncertainty(wf)),
EXT_OTHER (6):
  benchmarks/validation_suite.py:104: abs(y_uncertainty(wf) * momentum_uncertainty(wf, 'y') - 0.5),
  examples/05_2d_gaussian_barrier.py:66: dy    = y_uncertainty(wf_current)
  examples/08_3d_bec_time_of_flight.py:61: return np.array([position_uncertainty(wf), y_uncertainty(wf), z_uncertainty(wf)])
  tests/test_3d_observables.py:30: assert y_uncertainty(wf) == pytest.approx(p['sigma_y'], abs=1e-6)
  tests/test_3d_observables.py:39: ('y', p['k0_y'], p['sigma_y'], y_uncertainty(wf)),
  tests/test_gross_pitaevskii.py:77: for f in (position_uncertainty, y_uncertainty, z_uncertainty):
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (6): benchmarks/validation_suite.py:22(quantumlab.observables), examples/08_3d_bec_time_of_flight.py:36(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), examples/05_2d_gaussian_barrier.py:8(quantumlab.observables.expectation), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation)

## z_expectation  [quantumlab/observables/expectation.py:56] (function)
SIG: def z_expectation(wf) -> float:
EXT_CALLS (3):
  tests/test_3d_observables.py:28: assert z_expectation(wf) == pytest.approx(p['z0'], abs=1e-6)
  tests/test_3d_observables.py:60: z_expectation(wf)
  tests/test_rotation.py:45: assert z_expectation(wf) == pytest.approx(0.0, abs=1e-10)
EXT_OTHER (3):
  tests/test_3d_observables.py:28: assert z_expectation(wf) == pytest.approx(p['z0'], abs=1e-6)
  tests/test_3d_observables.py:60: z_expectation(wf)
  tests/test_rotation.py:45: assert z_expectation(wf) == pytest.approx(0.0, abs=1e-10)
INT_CALLS (1): quantumlab/observables/expectation.py:71
INT_OTHER (1): quantumlab/observables/expectation.py:71
IMPORTS (3): tests/test_rotation.py:8(quantumlab.observables), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation)

## z_squared_expectation  [quantumlab/observables/expectation.py:63] (function)
SIG: def z_squared_expectation(wf) -> float:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (1): quantumlab/observables/expectation.py:72
INT_OTHER (1): quantumlab/observables/expectation.py:72
IMPORTS (1): quantumlab/observables/__init__.py:1(quantumlab.observables.expectation)

## z_uncertainty  [quantumlab/observables/expectation.py:70] (function)
SIG: def z_uncertainty(wf) -> float:
EXT_CALLS (4):
  benchmarks/validation_suite.py:105: abs(z_uncertainty(wf) * momentum_uncertainty(wf, 'z') - 0.5))
  examples/08_3d_bec_time_of_flight.py:61: return np.array([position_uncertainty(wf), y_uncertainty(wf), z_uncertainty(wf)])
  tests/test_3d_observables.py:31: assert z_uncertainty(wf) == pytest.approx(p['sigma_z'], abs=1e-6)
  tests/test_3d_observables.py:40: ('z', p['k0_z'], p['sigma_z'], z_uncertainty(wf)),
EXT_OTHER (5):
  benchmarks/validation_suite.py:105: abs(z_uncertainty(wf) * momentum_uncertainty(wf, 'z') - 0.5))
  examples/08_3d_bec_time_of_flight.py:61: return np.array([position_uncertainty(wf), y_uncertainty(wf), z_uncertainty(wf)])
  tests/test_3d_observables.py:31: assert z_uncertainty(wf) == pytest.approx(p['sigma_z'], abs=1e-6)
  tests/test_3d_observables.py:40: ('z', p['k0_z'], p['sigma_z'], z_uncertainty(wf)),
  tests/test_gross_pitaevskii.py:77: for f in (position_uncertainty, y_uncertainty, z_uncertainty):
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (5): benchmarks/validation_suite.py:22(quantumlab.observables), examples/08_3d_bec_time_of_flight.py:36(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation)

## momentum_expectation  [quantumlab/observables/expectation.py:76] (function)
SIG: def momentum_expectation(wf, direction: str='x', hbar: float=1.0) -> float:
EXT_CALLS (5):
  testbench_interlock.py:111: p_exp = momentum_expectation(wf)
  tests/test_3d_observables.py:42: assert momentum_expectation(wf, axis, hbar) == pytest.approx(hbar * k0, abs=1e-6)
  tests/test_3d_observables.py:51: momentum_expectation(wf, 'w')
  tests/test_new_potentials_and_observables.py:96: assert np.sum(j) * dV == pytest.approx(momentum_expectation(wf, axis), abs=1e-10)
  tests/test_observables.py:16: assert momentum_expectation(wf, hbar=hbar) == pytest.approx(hbar * k0, abs=1e-05)
EXT_OTHER (5):
  testbench_interlock.py:111: p_exp = momentum_expectation(wf)
  tests/test_3d_observables.py:42: assert momentum_expectation(wf, axis, hbar) == pytest.approx(hbar * k0, abs=1e-6)
  tests/test_3d_observables.py:51: momentum_expectation(wf, 'w')
  tests/test_new_potentials_and_observables.py:96: assert np.sum(j) * dV == pytest.approx(momentum_expectation(wf, axis), abs=1e-10)
  tests/test_observables.py:16: assert momentum_expectation(wf, hbar=hbar) == pytest.approx(hbar * k0, abs=1e-05)
INT_CALLS (1): quantumlab/observables/expectation.py:135
INT_OTHER (1): quantumlab/observables/expectation.py:135
IMPORTS (6): benchmarks/validation_suite.py:22(quantumlab.observables), testbench_interlock.py:38(quantumlab.observables), tests/test_new_potentials_and_observables.py:10(quantumlab.observables), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation), tests/test_observables.py:5(quantumlab.observables.expectation)

## momentum_squared_expectation  [quantumlab/observables/expectation.py:105] (function)
SIG: def momentum_squared_expectation(wf, direction: str='x', hbar: float=1.0) -> float:
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (7): quantumlab/observables/expectation.py:136, quantumlab/observables/expectation.py:156, quantumlab/observables/expectation.py:159, quantumlab/observables/expectation.py:160, quantumlab/observables/expectation.py:163, quantumlab/observables/expectation.py:164, quantumlab/observables/expectation.py:165
INT_OTHER (7): quantumlab/observables/expectation.py:136, quantumlab/observables/expectation.py:156, quantumlab/observables/expectation.py:159, quantumlab/observables/expectation.py:160, quantumlab/observables/expectation.py:163, quantumlab/observables/expectation.py:164, quantumlab/observables/expectation.py:165
IMPORTS (1): quantumlab/observables/__init__.py:1(quantumlab.observables.expectation)

## momentum_uncertainty  [quantumlab/observables/expectation.py:134] (function)
SIG: def momentum_uncertainty(wf, direction: str='x', hbar: float=1.0) -> float:
EXT_CALLS (6):
  benchmarks/validation_suite.py:103: err = max(abs(position_uncertainty(wf) * momentum_uncertainty(wf, 'x') - 0.5),
  benchmarks/validation_suite.py:104: abs(y_uncertainty(wf) * momentum_uncertainty(wf, 'y') - 0.5),
  benchmarks/validation_suite.py:105: abs(z_uncertainty(wf) * momentum_uncertainty(wf, 'z') - 0.5))
  tests/test_3d_observables.py:43: dp = momentum_uncertainty(wf, axis, hbar)
  tests/test_observables.py:18: assert momentum_uncertainty(wf, hbar=hbar) == pytest.approx(expected_dp, abs=1e-05)
  tests/test_observables.py:20: dp = momentum_uncertainty(wf, hbar=hbar)
EXT_OTHER (6):
  benchmarks/validation_suite.py:103: err = max(abs(position_uncertainty(wf) * momentum_uncertainty(wf, 'x') - 0.5),
  benchmarks/validation_suite.py:104: abs(y_uncertainty(wf) * momentum_uncertainty(wf, 'y') - 0.5),
  benchmarks/validation_suite.py:105: abs(z_uncertainty(wf) * momentum_uncertainty(wf, 'z') - 0.5))
  tests/test_3d_observables.py:43: dp = momentum_uncertainty(wf, axis, hbar)
  tests/test_observables.py:18: assert momentum_uncertainty(wf, hbar=hbar) == pytest.approx(expected_dp, abs=1e-05)
  tests/test_observables.py:20: dp = momentum_uncertainty(wf, hbar=hbar)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): benchmarks/validation_suite.py:22(quantumlab.observables), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), tests/test_3d_observables.py:5(quantumlab.observables.expectation), tests/test_observables.py:5(quantumlab.observables.expectation)

## potential_energy_expectation  [quantumlab/observables/expectation.py:140] (function)
SIG: def potential_energy_expectation(wf, potential) -> float:
EXT_CALLS (10):
  benchmarks/validation_suite.py:173: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  benchmarks/validation_suite.py:303: V = sum(potential_energy_expectation(s, HarmonicTrap(1.0)) for s in states)
  benchmarks/validation_suite.py:318: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  examples/08_3d_bec_time_of_flight.py:85: V = potential_energy_expectation(wf0, trap)
  quantumlab/observables/nonlinear.py:13: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:19: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:30: E = sum(kinetic_energy_expectation(s, hbar, m) + potential_energy_expectation(s, p)
  tests/test_conjugate_gradient.py:33: T, V, E_int = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  tests/test_gross_pitaevskii.py:65: V = potential_energy_expectation(wf, trap)
  tests/test_multicomponent.py:115: V = sum(potential_energy_expectation(s, trap) for s in states)
EXT_OTHER (10):
  benchmarks/validation_suite.py:173: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  benchmarks/validation_suite.py:303: V = sum(potential_energy_expectation(s, HarmonicTrap(1.0)) for s in states)
  benchmarks/validation_suite.py:318: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  examples/08_3d_bec_time_of_flight.py:85: V = potential_energy_expectation(wf0, trap)
  quantumlab/observables/nonlinear.py:13: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:19: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:30: E = sum(kinetic_energy_expectation(s, hbar, m) + potential_energy_expectation(s, p)
  tests/test_conjugate_gradient.py:33: T, V, E_int = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  tests/test_gross_pitaevskii.py:65: V = potential_energy_expectation(wf, trap)
  tests/test_multicomponent.py:115: V = sum(potential_energy_expectation(s, trap) for s in states)
INT_CALLS (1): quantumlab/observables/expectation.py:172
INT_OTHER (1): quantumlab/observables/expectation.py:172
IMPORTS (7): benchmarks/validation_suite.py:22(quantumlab.observables), examples/08_3d_bec_time_of_flight.py:36(quantumlab.observables), tests/test_conjugate_gradient.py:8(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), tests/test_multicomponent.py:9(quantumlab.observables), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), quantumlab/observables/nonlinear.py:2(quantumlab.observables.expectation)

## kinetic_energy_expectation  [quantumlab/observables/expectation.py:154] (function)
SIG: def kinetic_energy_expectation(wf, hbar: float=1.0, m: float=1.0) -> float:
EXT_CALLS (10):
  benchmarks/validation_suite.py:173: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  benchmarks/validation_suite.py:302: T = sum(kinetic_energy_expectation(s) for s in states)
  benchmarks/validation_suite.py:318: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  examples/08_3d_bec_time_of_flight.py:84: T = kinetic_energy_expectation(wf0)
  quantumlab/observables/nonlinear.py:13: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:19: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:30: E = sum(kinetic_energy_expectation(s, hbar, m) + potential_energy_expectation(s, p)
  tests/test_conjugate_gradient.py:33: T, V, E_int = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  tests/test_gross_pitaevskii.py:64: T = kinetic_energy_expectation(wf)
  tests/test_multicomponent.py:114: T = sum(kinetic_energy_expectation(s) for s in states)
EXT_OTHER (10):
  benchmarks/validation_suite.py:173: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  benchmarks/validation_suite.py:302: T = sum(kinetic_energy_expectation(s) for s in states)
  benchmarks/validation_suite.py:318: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  examples/08_3d_bec_time_of_flight.py:84: T = kinetic_energy_expectation(wf0)
  quantumlab/observables/nonlinear.py:13: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:19: return float(kinetic_energy_expectation(wf, hbar, m) + potential_energy_expectation(wf, potential)
  quantumlab/observables/nonlinear.py:30: E = sum(kinetic_energy_expectation(s, hbar, m) + potential_energy_expectation(s, p)
  tests/test_conjugate_gradient.py:33: T, V, E_int = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  tests/test_gross_pitaevskii.py:64: T = kinetic_energy_expectation(wf)
  tests/test_multicomponent.py:114: T = sum(kinetic_energy_expectation(s) for s in states)
INT_CALLS (1): quantumlab/observables/expectation.py:171
INT_OTHER (1): quantumlab/observables/expectation.py:171
IMPORTS (7): benchmarks/validation_suite.py:22(quantumlab.observables), examples/08_3d_bec_time_of_flight.py:36(quantumlab.observables), tests/test_conjugate_gradient.py:8(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), tests/test_multicomponent.py:9(quantumlab.observables), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), quantumlab/observables/nonlinear.py:2(quantumlab.observables.expectation)

## total_energy_expectation  [quantumlab/observables/expectation.py:170] (function)
SIG: def total_energy_expectation(wf, potential, hbar: float=1.0, m: float=1.0) -> float:
EXT_CALLS (20):
  benchmarks/validation_suite.py:86: E0 = total_energy_expectation(wf, pot)
  benchmarks/validation_suite.py:97: '|ΔE/E|', abs(total_energy_expectation(wf, pot) - E0) / E0, 1e-8)
  examples/02_harmonic_oscillator.py:36: energies = [total_energy_expectation(wf, potential, hbar=1.0, m=m)]
  examples/02_harmonic_oscillator.py:44: energy = total_energy_expectation(wf_current, potential, hbar=1.0, m=m)
  examples/03_double_well.py:47: energy = total_energy_expectation(wf_current, potential, hbar=1.0, m=1.0)
  quantumlab/runner.py:170: E = total_energy_expectation(wf_current, potential)
  testbench_interlock.py:103: E0 = total_energy_expectation(wf, pot)
  testbench_interlock.py:109: E1 = total_energy_expectation(wf, pot)
  tests/test_2d_solver.py:29: initial_energy = total_energy_expectation(wf, potential)
  tests/test_2d_solver.py:33: final_energy = total_energy_expectation(wf_current, potential)
  tests/test_3d_gpu_solver.py:58: E_initial = total_energy_expectation(gaussian_wf, barrier)
  tests/test_3d_gpu_solver.py:64: E_final = total_energy_expectation(wf_current, barrier)
  tests/test_3d_solver.py:97: E0 = total_energy_expectation(wf, potential)
  tests/test_3d_solver.py:101: E1 = total_energy_expectation(wf_current, potential)
  tests/test_rotation.py:68: return total_energy_expectation(w, trap) - Om * angular_momentum_z_expectation(w)
  tests/test_rotation.py:83: energies.append(total_energy_expectation(wf, trap))
  tests/test_solvers.py:25: initial_energy = total_energy_expectation(wf, potential)
  tests/test_solvers.py:29: final_energy = total_energy_expectation(wf_current, potential)
  tests/test_split_operator.py:55: E0 = total_energy_expectation(wf, pot)
  tests/test_split_operator.py:59: assert total_energy_expectation(wf, pot) == pytest.approx(E0, rel=energy_rtol)
EXT_OTHER (20):
  benchmarks/validation_suite.py:86: E0 = total_energy_expectation(wf, pot)
  benchmarks/validation_suite.py:97: '|ΔE/E|', abs(total_energy_expectation(wf, pot) - E0) / E0, 1e-8)
  examples/02_harmonic_oscillator.py:36: energies = [total_energy_expectation(wf, potential, hbar=1.0, m=m)]
  examples/02_harmonic_oscillator.py:44: energy = total_energy_expectation(wf_current, potential, hbar=1.0, m=m)
  examples/03_double_well.py:47: energy = total_energy_expectation(wf_current, potential, hbar=1.0, m=1.0)
  quantumlab/runner.py:170: E = total_energy_expectation(wf_current, potential)
  testbench_interlock.py:103: E0 = total_energy_expectation(wf, pot)
  testbench_interlock.py:109: E1 = total_energy_expectation(wf, pot)
  tests/test_2d_solver.py:29: initial_energy = total_energy_expectation(wf, potential)
  tests/test_2d_solver.py:33: final_energy = total_energy_expectation(wf_current, potential)
  tests/test_3d_gpu_solver.py:58: E_initial = total_energy_expectation(gaussian_wf, barrier)
  tests/test_3d_gpu_solver.py:64: E_final = total_energy_expectation(wf_current, barrier)
  tests/test_3d_solver.py:97: E0 = total_energy_expectation(wf, potential)
  tests/test_3d_solver.py:101: E1 = total_energy_expectation(wf_current, potential)
  tests/test_rotation.py:68: return total_energy_expectation(w, trap) - Om * angular_momentum_z_expectation(w)
  tests/test_rotation.py:83: energies.append(total_energy_expectation(wf, trap))
  tests/test_solvers.py:25: initial_energy = total_energy_expectation(wf, potential)
  tests/test_solvers.py:29: final_energy = total_energy_expectation(wf_current, potential)
  tests/test_split_operator.py:55: E0 = total_energy_expectation(wf, pot)
  tests/test_split_operator.py:59: assert total_energy_expectation(wf, pot) == pytest.approx(E0, rel=energy_rtol)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (12): benchmarks/validation_suite.py:22(quantumlab.observables), testbench_interlock.py:38(quantumlab.observables), tests/test_rotation.py:8(quantumlab.observables), tests/test_split_operator.py:12(quantumlab.observables), examples/02_harmonic_oscillator.py:8(quantumlab.observables.expectation), examples/03_double_well.py:7(quantumlab.observables.expectation), quantumlab/observables/__init__.py:1(quantumlab.observables.expectation), quantumlab/runner.py:18(quantumlab.observables.expectation), tests/test_2d_solver.py:9(quantumlab.observables.expectation), tests/test_3d_gpu_solver.py:12(quantumlab.observables.expectation), tests/test_3d_solver.py:9(quantumlab.observables.expectation), tests/test_solvers.py:7(quantumlab.observables.expectation)

## get_momentum_wavefunction  [quantumlab/observables/momentum.py:4] (function)
SIG: def get_momentum_wavefunction(wf):
EXT_CALLS (0):
EXT_OTHER (0):
INT_CALLS (3): quantumlab/observables/momentum.py:24, quantumlab/observables/momentum.py:27, quantumlab/observables/momentum.py:30
INT_OTHER (3): quantumlab/observables/momentum.py:24, quantumlab/observables/momentum.py:27, quantumlab/observables/momentum.py:30
IMPORTS (1): quantumlab/observables/__init__.py:3(quantumlab.observables.momentum)

## get_momentum_probability_density  [quantumlab/observables/momentum.py:22] (function)
SIG: def get_momentum_probability_density(wf):
EXT_CALLS (2):
  quantumlab/visualization/plots_1d.py:52: k, prob_k = get_momentum_probability_density(wf)
  tests/test_3d_observables.py:74: (kx, ky, kz), prob_k = get_momentum_probability_density(wf)
EXT_OTHER (2):
  quantumlab/visualization/plots_1d.py:52: k, prob_k = get_momentum_probability_density(wf)
  tests/test_3d_observables.py:74: (kx, ky, kz), prob_k = get_momentum_probability_density(wf)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (3): quantumlab/observables/__init__.py:3(quantumlab.observables.momentum), quantumlab/visualization/plots_1d.py:5(quantumlab.observables.momentum), tests/test_3d_observables.py:12(quantumlab.observables.momentum)

## interaction_energy  [quantumlab/observables/nonlinear.py:6] (function)
SIG: def interaction_energy(wf, nonlinearity: float) -> float:
EXT_CALLS (5):
  benchmarks/validation_suite.py:173: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  benchmarks/validation_suite.py:318: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  examples/08_3d_bec_time_of_flight.py:86: E_int = interaction_energy(wf0, g)
  tests/test_conjugate_gradient.py:33: T, V, E_int = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  tests/test_gross_pitaevskii.py:66: E_int = interaction_energy(wf, g)
EXT_OTHER (5):
  benchmarks/validation_suite.py:173: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  benchmarks/validation_suite.py:318: T, V, Ei = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  examples/08_3d_bec_time_of_flight.py:86: E_int = interaction_energy(wf0, g)
  tests/test_conjugate_gradient.py:33: T, V, E_int = kinetic_energy_expectation(wf), potential_energy_expectation(wf, trap), interaction_energy(wf, g)
  tests/test_gross_pitaevskii.py:66: E_int = interaction_energy(wf, g)
INT_CALLS (2): quantumlab/observables/nonlinear.py:14, quantumlab/observables/nonlinear.py:20
INT_OTHER (2): quantumlab/observables/nonlinear.py:14, quantumlab/observables/nonlinear.py:20
IMPORTS (5): benchmarks/validation_suite.py:22(quantumlab.observables), examples/08_3d_bec_time_of_flight.py:36(quantumlab.observables), tests/test_conjugate_gradient.py:8(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), quantumlab/observables/__init__.py:4(quantumlab.observables.nonlinear)

## gross_pitaevskii_energy  [quantumlab/observables/nonlinear.py:11] (function)
SIG: def gross_pitaevskii_energy(wf, potential, nonlinearity: float, hbar: float = 1.0, m: float = 1.0) -> float:
EXT_CALLS (5):
  examples/09_soliton_collision.py:55: E0 = gross_pitaevskii_energy(wf0, None, g)
  examples/09_soliton_collision.py:57: E1 = gross_pitaevskii_energy(wf, None, g)
  tests/test_gross_pitaevskii.py:47: E0 = gross_pitaevskii_energy(wf0, shaken, g)
  tests/test_gross_pitaevskii.py:49: assert gross_pitaevskii_energy(wf, shaken, g) == pytest.approx(E0, rel=1e-6)
  tests/test_rotation.py:108: return gross_pitaevskii_energy(w, trap, g) - Om * angular_momentum_z_expectation(w)
EXT_OTHER (5):
  examples/09_soliton_collision.py:55: E0 = gross_pitaevskii_energy(wf0, None, g)
  examples/09_soliton_collision.py:57: E1 = gross_pitaevskii_energy(wf, None, g)
  tests/test_gross_pitaevskii.py:47: E0 = gross_pitaevskii_energy(wf0, shaken, g)
  tests/test_gross_pitaevskii.py:49: assert gross_pitaevskii_energy(wf, shaken, g) == pytest.approx(E0, rel=1e-6)
  tests/test_rotation.py:108: return gross_pitaevskii_energy(w, trap, g) - Om * angular_momentum_z_expectation(w)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (4): examples/09_soliton_collision.py:22(quantumlab.observables), tests/test_gross_pitaevskii.py:8(quantumlab.observables), tests/test_rotation.py:8(quantumlab.observables), quantumlab/observables/__init__.py:4(quantumlab.observables.nonlinear)

## chemical_potential  [quantumlab/observables/nonlinear.py:17] (function)
SIG: def chemical_potential(wf, potential, nonlinearity: float, hbar: float = 1.0, m: float = 1.0) -> float:
EXT_CALLS (1):
  tests/test_gross_pitaevskii.py:69: assert chemical_potential(wf, trap, g) == pytest.approx(info.chemical_potential, rel=1e-10)
EXT_OTHER (6):
  examples/08_3d_bec_time_of_flight.py:88: print(f'  E/N = {info.energy:.6f}   μ = {info.chemical_potential:.6f}   residual ‖Hψ−μψ‖ = {info.residual:.1e}')
  examples/11_rotating_bec_vortex_lattice.py:72: print(f'\n[1] Non-rotating ground state: μ = {info.chemical_potential:.3f}, '
  examples/11_rotating_bec_vortex_lattice.py:73: f'Thomas–Fermi radius ≈ {np.sqrt(2 * info.chemical_potential):.2f}')
  examples/11_rotating_bec_vortex_lattice.py:172: f'μ = {info3.chemical_potential:.10f}, residual ‖(H−ΩL_z)ψ − μψ‖ = {info3.residual:.2e}')
  quantumlab/stationary/imaginary_time.py:22: chemical_potential: float
  tests/test_gross_pitaevskii.py:69: assert chemical_potential(wf, trap, g) == pytest.approx(info.chemical_potential, rel=1e-10)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): tests/test_gross_pitaevskii.py:8(quantumlab.observables), quantumlab/observables/__init__.py:4(quantumlab.observables.nonlinear)

## coupled_gp_energy  [quantumlab/observables/nonlinear.py:23] (function)
SIG: def coupled_gp_energy(states, potentials, couplings, hbar: float = 1.0, m: float = 1.0) -> float:
EXT_CALLS (2):
  tests/test_multicomponent.py:100: E0 = coupled_gp_energy(state, traps, G)
  tests/test_multicomponent.py:102: assert coupled_gp_energy(out, traps, G) == pytest.approx(E0, rel=1e-9)
EXT_OTHER (2):
  tests/test_multicomponent.py:100: E0 = coupled_gp_energy(state, traps, G)
  tests/test_multicomponent.py:102: assert coupled_gp_energy(out, traps, G) == pytest.approx(E0, rel=1e-9)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): tests/test_multicomponent.py:9(quantumlab.observables), quantumlab/observables/__init__.py:4(quantumlab.observables.nonlinear)

## miscibility_overlap  [quantumlab/observables/nonlinear.py:38] (function)
SIG: def miscibility_overlap(wf_a, wf_b) -> float:
EXT_CALLS (4):
  examples/13_two_component_bec.py:76: overlaps.append(miscibility_overlap(*states))
  examples/13_two_component_bec.py:200: print(f'    non-rotating ground state: overlap Λ = {miscibility_overlap(s1, s2):.4f} (miscible, g12 < g)')
  tests/test_multicomponent.py:125: assert miscibility_overlap(a, a) == pytest.approx(1.0)
  tests/test_multicomponent.py:127: assert miscibility_overlap(_gauss2d(grid, -5.0), far) < 1e-6
EXT_OTHER (4):
  examples/13_two_component_bec.py:76: overlaps.append(miscibility_overlap(*states))
  examples/13_two_component_bec.py:200: print(f'    non-rotating ground state: overlap Λ = {miscibility_overlap(s1, s2):.4f} (miscible, g12 < g)')
  tests/test_multicomponent.py:125: assert miscibility_overlap(a, a) == pytest.approx(1.0)
  tests/test_multicomponent.py:127: assert miscibility_overlap(_gauss2d(grid, -5.0), far) < 1e-6
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (3): examples/13_two_component_bec.py:44(quantumlab.observables), tests/test_multicomponent.py:9(quantumlab.observables), quantumlab/observables/__init__.py:4(quantumlab.observables.nonlinear)

## wavelength_to_omega  [quantumlab/strongfield.py:17] (function)
SIG: def wavelength_to_omega(wavelength_nm: float) -> float:
EXT_CALLS (5):
  benchmarks/validation_suite.py:217: w = sf.wavelength_to_omega(800.0)
  examples/12_high_harmonic_generation.py:59: omega = wavelength_to_omega(WAVELENGTH_NM)
  examples/12_high_harmonic_generation.py:87: omega = wavelength_to_omega(WAVELENGTH_NM)
  tests/test_strongfield.py:15: assert wavelength_to_omega(800.0) == pytest.approx(0.0569542, rel=1e-6)    # 1.55 eV photon
  tests/test_strongfield.py:16: assert wavelength_to_omega(800.0) * HARTREE_EV == pytest.approx(1.5498, abs=1e-4)
EXT_OTHER (5):
  benchmarks/validation_suite.py:217: w = sf.wavelength_to_omega(800.0)
  examples/12_high_harmonic_generation.py:59: omega = wavelength_to_omega(WAVELENGTH_NM)
  examples/12_high_harmonic_generation.py:87: omega = wavelength_to_omega(WAVELENGTH_NM)
  tests/test_strongfield.py:15: assert wavelength_to_omega(800.0) == pytest.approx(0.0569542, rel=1e-6)    # 1.55 eV photon
  tests/test_strongfield.py:16: assert wavelength_to_omega(800.0) * HARTREE_EV == pytest.approx(1.5498, abs=1e-4)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## intensity_to_field  [quantumlab/strongfield.py:22] (function)
SIG: def intensity_to_field(intensity_w_cm2: float) -> float:
EXT_CALLS (6):
  benchmarks/validation_suite.py:219: laser = DipoleDrive(atom, F0=sf.intensity_to_field(1e14), omega=w,
  examples/12_high_harmonic_generation.py:61: field = intensity_to_field(intensity)
  examples/12_high_harmonic_generation.py:90: field = intensity_to_field(intensity)
  examples/12_high_harmonic_generation.py:260: up = ponderomotive_energy(intensity_to_field(I), omega)
  tests/test_strongfield.py:17: assert intensity_to_field(3.50944758e16) == pytest.approx(1.0)
  tests/test_strongfield.py:18: assert intensity_to_field(1e14) == pytest.approx(0.05338, abs=1e-5)
EXT_OTHER (6):
  benchmarks/validation_suite.py:219: laser = DipoleDrive(atom, F0=sf.intensity_to_field(1e14), omega=w,
  examples/12_high_harmonic_generation.py:61: field = intensity_to_field(intensity)
  examples/12_high_harmonic_generation.py:90: field = intensity_to_field(intensity)
  examples/12_high_harmonic_generation.py:260: up = ponderomotive_energy(intensity_to_field(I), omega)
  tests/test_strongfield.py:17: assert intensity_to_field(3.50944758e16) == pytest.approx(1.0)
  tests/test_strongfield.py:18: assert intensity_to_field(1e14) == pytest.approx(0.05338, abs=1e-5)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## ponderomotive_energy  [quantumlab/strongfield.py:27] (function)
SIG: def ponderomotive_energy(field: float, omega: float) -> float:
EXT_CALLS (3):
  examples/12_high_harmonic_generation.py:91: Up = ponderomotive_energy(field, omega)
  examples/12_high_harmonic_generation.py:260: up = ponderomotive_energy(intensity_to_field(I), omega)
  tests/test_strongfield.py:19: assert ponderomotive_energy(0.05338, 0.05695) == pytest.approx(0.2196, abs=1e-4)
EXT_OTHER (3):
  examples/12_high_harmonic_generation.py:91: Up = ponderomotive_energy(field, omega)
  examples/12_high_harmonic_generation.py:260: up = ponderomotive_energy(intensity_to_field(I), omega)
  tests/test_strongfield.py:19: assert ponderomotive_energy(0.05338, 0.05695) == pytest.approx(0.2196, abs=1e-4)
INT_CALLS (1): quantumlab/strongfield.py:67
INT_OTHER (1): quantumlab/strongfield.py:67
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## classical_returns  [quantumlab/strongfield.py:32] (function)
SIG: def classical_returns(n_phases: int = 2000):
EXT_CALLS (3):
  benchmarks/validation_suite.py:214: _, _, ke = sf.classical_returns(4000)
  examples/12_high_harmonic_generation.py:137: births, returns, ke = classical_returns(4000)
  tests/test_strongfield.py:24: births, returns, energy = classical_returns(4000)
EXT_OTHER (3):
  benchmarks/validation_suite.py:214: _, _, ke = sf.classical_returns(4000)
  examples/12_high_harmonic_generation.py:137: births, returns, ke = classical_returns(4000)
  tests/test_strongfield.py:24: births, returns, energy = classical_returns(4000)
INT_CALLS (1): quantumlab/strongfield.py:67
INT_OTHER (1): quantumlab/strongfield.py:67
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## classical_cutoff  [quantumlab/strongfield.py:65] (function)
SIG: def classical_cutoff(ionisation_potential: float, field: float, omega: float) -> float:
EXT_CALLS (1):
  tests/test_strongfield.py:30: assert classical_cutoff(0.5, 0.05338, 0.05695) == pytest.approx(0.5 + 3.1731 * 0.2196, abs=1e-3)
EXT_OTHER (1):
  tests/test_strongfield.py:30: assert classical_cutoff(0.5, 0.05338, 0.05695) == pytest.approx(0.5 + 3.1731 * 0.2196, abs=1e-3)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (1): tests/test_strongfield.py:8(quantumlab.strongfield)

## harmonic_spectrum  [quantumlab/strongfield.py:70] (function)
SIG: def harmonic_spectrum(signal: np.ndarray, dt: float, omega0: float, window: bool = True):
EXT_CALLS (4):
  benchmarks/validation_suite.py:226: H, S = sf.harmonic_spectrum(acc, 0.05, w)
  examples/12_high_harmonic_generation.py:77: H, S = harmonic_spectrum(acc, DT, omega)
  examples/12_high_harmonic_generation.py:106: H, S = harmonic_spectrum(acc, DT, omega)
  tests/test_strongfield.py:64: H, S = harmonic_spectrum(sig, dt, w0)
EXT_OTHER (4):
  benchmarks/validation_suite.py:226: H, S = sf.harmonic_spectrum(acc, 0.05, w)
  examples/12_high_harmonic_generation.py:77: H, S = harmonic_spectrum(acc, DT, omega)
  examples/12_high_harmonic_generation.py:106: H, S = harmonic_spectrum(acc, DT, omega)
  tests/test_strongfield.py:64: H, S = harmonic_spectrum(sig, dt, w0)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## gabor_transform  [quantumlab/strongfield.py:83] (function)
SIG: def gabor_transform(signal: np.ndarray, dt: float, omega0: float, orders, width: float,
                    times=None):
EXT_CALLS (3):
  examples/12_high_harmonic_generation.py:136: tt, oo, G = gabor_transform(acc, DT, omega, np.linspace(1, 35, 241), width=sigma, times=times)
  examples/12_high_harmonic_generation.py:170: _, _, g = gabor_transform(acc, DT, omega, [q], width=sigma, times=fine)
  tests/test_strongfield.py:76: tt, oo, G = gabor_transform(sig, dt, w0, np.linspace(1, 15, 141), width=1 / (3 * w0),
EXT_OTHER (3):
  examples/12_high_harmonic_generation.py:136: tt, oo, G = gabor_transform(acc, DT, omega, np.linspace(1, 35, 241), width=sigma, times=times)
  examples/12_high_harmonic_generation.py:170: _, _, g = gabor_transform(acc, DT, omega, [q], width=sigma, times=fine)
  tests/test_strongfield.py:76: tt, oo, G = gabor_transform(sig, dt, w0, np.linspace(1, 15, 141), width=1 / (3 * w0),
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## attosecond_pulses  [quantumlab/strongfield.py:107] (function)
SIG: def attosecond_pulses(signal: np.ndarray, dt: float, omega0: float, order_min: float, order_max: float):
EXT_CALLS (3):
  benchmarks/validation_suite.py:235: P = sf.attosecond_pulses(acc, 0.05, w, 11, 21)
  examples/12_high_harmonic_generation.py:188: P = attosecond_pulses(acc, DT, omega, 11, 21)
  tests/test_strongfield.py:88: P = attosecond_pulses(sig, dt, w0, 10, 22)
EXT_OTHER (3):
  benchmarks/validation_suite.py:235: P = sf.attosecond_pulses(acc, 0.05, w, 11, 21)
  examples/12_high_harmonic_generation.py:188: P = attosecond_pulses(acc, DT, omega, 11, 21)
  tests/test_strongfield.py:88: P = attosecond_pulses(sig, dt, w0, 10, 22)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)

## dipole_acceleration  [quantumlab/strongfield.py:119] (function)
SIG: def dipole_acceleration(wf, base_potential, force: float) -> float:
EXT_CALLS (3):
  benchmarks/validation_suite.py:224: callback=lambda n, t, wf: acc.append(sf.dipole_acceleration(wf, atom, laser.force(t))))
  examples/12_high_harmonic_generation.py:68: acc.append(dipole_acceleration(wf, atom, laser.force(t)))
  tests/test_strongfield.py:100: a = dipole_acceleration(wf, HarmonicTrap(1.0), force=0.25)
EXT_OTHER (3):
  benchmarks/validation_suite.py:224: callback=lambda n, t, wf: acc.append(sf.dipole_acceleration(wf, atom, laser.force(t))))
  examples/12_high_harmonic_generation.py:68: acc.append(dipole_acceleration(wf, atom, laser.force(t)))
  tests/test_strongfield.py:100: a = dipole_acceleration(wf, HarmonicTrap(1.0), force=0.25)
INT_CALLS (0): 
INT_OTHER (0): 
IMPORTS (2): examples/12_high_harmonic_generation.py:45(quantumlab.strongfield), tests/test_strongfield.py:8(quantumlab.strongfield)
