# -*- coding: utf-8 -*-
"""Generate cpd_producer_inventory.md from the AST scan + curated annotations.
Reads only the repo; writes only into the audit directory.
"""
import json
import os

AUD = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20"
REPO = r"C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main"
defs = json.load(open(os.path.join(AUD, "_scan.json"), encoding="utf-8"))["defs"]

R = []
def E(qn, kind, i, o, m, p, c, t, v):
    R.append(dict(qn=qn, kind=kind, inp=i, out=o, math=m, pre=p, callers=c, tests=t, val=v))

# =====================================================================
# quantumlab/core/grid.py
# =====================================================================
E("Grid1D", "class",
  "N:int, x_min:float, x_max:float",
  "object; N,x_min,x_max,L,dx:float; x,k:float64 (N,); dk:float; shape:(N,)",
  "L=x_max-x_min; dx=L/N; x=linspace(x_min,x_max,N,endpoint=False); k=2*pi*fftfreq(N,dx); dk=2*pi/L",
  "NONE enforced (no validation of N>0, x_max>x_min, types). Post: dx>0 iff L>0; k[0]=0.",
  "runner.py:54; examples/01_gaussian_barrier.py:29; 02:27; 03:28; 04:30; 09:46; 12:51; benchmarks/validation_suite.py:42,52,69,118,135,160,209,248,312; testbench_interlock.py:97",
  "tests/test_potentials.py::test_gaussian_barrier:12; test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_free_particle_matches_analytic_gaussian_spreading:114; test_absorbing_boundary_validation.py::test_valid_arguments_build_a_clean_mask:70",
  "VERIFIED - underpins validation_suite free-spreading/convergence checks (report 1.37e-15, order 2.001/3.997)")
E("Grid1D.__init__", "method",
  "N:int, x_min:float, x_max:float",
  "sets N,x_min,x_max,L,dx,x,k,dk",
  "same as class",
  "NONE enforced",
  "all Grid1D(...) sites (see Grid1D)",
  "same as Grid1D",
  "VERIFIED - probe: N=8,-4,4 -> dx=1.0, dk=0.7853981634, x/k float64 (8,)")
E("Grid1D.shape", "property",
  "none",
  "tuple (N,)",
  "(N,)",
  "NONE",
  "quantumlab/core/wavefunction.py:11,48,88; potentials/*.py; tests (many)",
  "tests/test_3d_solver.py::test_grid3d_shape:34; test_potentials.py::test_gaussian_barrier:12",
  "PARTIALLY - exercised by every shape assertion; no independent check of the tuple itself")
E("Grid2D", "class",
  "N_x,N_y:int; x_min,x_max,y_min,y_max:float",
  "X,Y,K_x,K_y:float64 (N_x,N_y); x,y:float64; dx,dy,L_x,L_y,dk_x,dk_y:float; shape:(N_x,N_y)",
  "dx=L_x/N_x; dy=L_y/N_y; meshgrid(indexing='ij'); k_x=2pi ffreq(N_x,dx); K_x,K_y=meshgrid",
  "NONE enforced",
  "runner.py:56; examples/05:36,10:34,11:65,174,13:67,108,193; benchmarks/validation_suite.py:111,179,189,283,296",
  "tests/test_2d_solver.py::test_2d_norm_conservation:11; test_new_potentials_and_observables.py::test_harmonic_trap_anisotropic_and_centered:20; test_stationary.py::test_2d_anisotropic_spectrum_lobpcg:21",
  "VERIFIED - 2D/3D validation checks (rotating frame, GP virial) depend on it")
E("Grid2D.__init__", "method", "see Grid2D", "see Grid2D", "see Grid2D", "NONE enforced",
  "all Grid2D(...) sites (see Grid2D)", "same as Grid2D",
  "VERIFIED - probe: 4x6 grid -> X (4,6) float64, dk_x=1.5707963, dk_y=1.0471976")
E("Grid2D.shape", "property", "none", "tuple (N_x,N_y)", "(N_x,N_y)", "NONE",
  "wavefunction.py:48,88; potentials; tests", "tests/test_2d_solver.py::test_2d_norm_conservation:11",
  "PARTIALLY")
E("Grid3D", "class",
  "N_x,N_y,N_z:int; x_min..z_max:float",
  "X,Y,Z,K_x,K_y,K_z:float64 (N_x,N_y,N_z); dx,dy,dz,dk_x,dk_y,dk_z:float; shape:(N_x,N_y,N_z)",
  "dx=L_x/N_x etc; meshgrid('ij'); k_j=2pi ffreq(N_j,dj)",
  "NONE enforced",
  "runner.py:60; examples/06:32,07:43,08:70,11:154; benchmarks/validation_suite.py:83,101,122,170,315; benchmarks/perf_comparison.py:85; benchmarks/gpu_split_operator.py:45; visualization/volume_3d.py:343",
  "tests/test_3d_solver.py::test_grid3d_shape:34; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_stationary.py::test_3d_isotropic_degeneracy:29",
  "VERIFIED - 3D norm/energy conservation check (validation_report 2.55e-15, 2.18e-10)")
E("Grid3D.__init__", "method", "see Grid3D", "see Grid3D", "see Grid3D", "NONE enforced",
  "all Grid3D(...) sites (see Grid3D)", "same as Grid3D",
  "VERIFIED - probe: 4^3 grid -> X (4,4,4) float64, dk_z=1.5707963")
E("Grid3D.shape", "property", "none", "tuple (N_x,N_y,N_z)", "(N_x,N_y,N_z)", "NONE",
  "wavefunction.py:88; potentials; volume_3d.py; tests", "tests/test_3d_solver.py::test_grid3d_shape:34",
  "PARTIALLY")

# =====================================================================
# quantumlab/core/wavefunction.py
# =====================================================================
E("WaveFunction1D", "class", "grid:Grid1D, psi:ndarray=None",
  "object; psi complex128 (N,); grid",
  "container for psi on Grid1D",
  "psi None -> zeros(complex); else shape must equal grid.shape (ValueError)",
  "runner.py:70,74,84; solvers/split_step_1d.py:27; examples/09:30; benchmarks/validation_suite.py:163,252,253",
  "tests/test_gross_pitaevskii.py::test_bright_soliton_propagates_without_dispersion:20; test_multicomponent.py::test_invalid_coupled_configurations:130",
  "VERIFIED - norm/energy conservation and soliton checks")
E("WaveFunction1D.__init__", "method", "grid:Grid1D, psi:np.ndarray=None",
  "psi complex128 (N,)", "zeros if None else np.array(psi,dtype=complex)",
  "ENFORCED: psi.shape==grid.shape else ValueError",
  "all WaveFunction1D(...) sites; solvers/split_step_1d.py:27",
  "tests/test_solvers.py::test_norm_conservation:9; test_gross_pitaevskii.py:23",
  "VERIFIED")
E("WaveFunction1D.probability_density", "property", "none",
  "float64 (N,), rho=|psi|^2", "|psi|^2", "NONE",
  "observables/expectation.py:5; observables/coefficients.py:5; observables/nonlinear.py:8; strongfield.py:132; visualization; tests",
  "tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_gross_pitaevskii.py::test_bright_soliton_propagates_without_dispersion:20",
  "VERIFIED - soliton/free-spreading exact-density checks")
E("WaveFunction1D.norm", "method", "none", "float", "sum(|psi|^2)*dx", "NONE",
  "runner.py; examples; benchmarks/validation_suite.py:95; testbench_interlock.py:102,108",
  "tests/test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_norm_and_energy_conservation:50; test_2d_solver.py::test_2d_norm_conservation:11",
  "VERIFIED - norm conservation check 2.55e-15; probe 0.9999999999999999")
E("WaveFunction1D.normalize", "method", "none", "self (WaveFunction1D)", "psi /= sqrt(norm) if norm>0",
  "ENFORCED: no-op if norm==0 (silent)",
  "benchmarks/validation_suite.py:112,201; examples/11:158; tests",
  "tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99; test_rotation.py::test_vortex_is_stationary_with_rotating_frame_energy:48",
  "VERIFIED - normalised states used in validation")
E("WaveFunction1D.fourier_transform", "method", "none", "complex128 (N,)",
  "fft(psi)*dx/sqrt(2pi)", "NONE",
  "observables/expectation.py:77,106; observables/momentum.py:5",
  "indirect: tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_momentum_expectation_and_heisenberg:34",
  "VERIFIED - Parseval probe 0.9999999999999997 vs 0.9999999999999999; Heisenberg checks")
E("WaveFunction1D.copy", "method", "none", "WaveFunction1D (deep copy of psi)",
  "WaveFunction1D(grid, psi.copy())", "NONE",
  "runner.py:156,166; benchmarks/perf_comparison.py:101,123,128; tests/test_3d_gpu_solver.py:82,83",
  "tests/test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73",
  "PARTIALLY - used as test fixture/copy semantics; no independent check")
E("WaveFunction1D.gaussian", "classmethod", "grid:Grid1D, x0,k0,sigma:float",
  "WaveFunction1D, normalised",
  "exp(-(x-x0)^2/(4 sigma^2))*exp(i k0 x), then normalize",
  "ENFORCED: sigma==0 -> division by zero (not guarded)",
  "runner.py:70,74,84; examples; benchmarks/validation_suite.py:44,54,71,85,102,136,191,285,286,297,298; benchmarks/perf_comparison.py:86; benchmarks/gpu_split_operator.py:24; testbench_interlock.py:98",
  "tests/test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_free_particle_matches_analytic_gaussian_spreading:114; test_observables.py::test_gaussian_observables_and_uncertainty:7",
  "VERIFIED - free-spreading exact solution 1.37e-15; minimum-uncertainty 4.6e-12")
E("WaveFunction2D", "class", "grid:Grid2D, psi=None", "psi complex128 (N_x,N_y)", "container",
  "shape check (ValueError)",
  "runner.py; solvers/split_step_2d.py:41; examples/11:174,187; 13:117,118; benchmarks/validation_suite.py:112,201",
  "tests/test_rotation.py::test_coherent_state_in_rotating_frame:19; test_new_potentials_and_observables.py::test_vortex_positions_finds_imprinted_vortices:127",
  "VERIFIED")
E("WaveFunction2D.__init__", "method", "grid:Grid2D, psi=None", "psi complex128 (N_x,N_y)",
  "zeros or np.array(psi,complex)", "ENFORCED shape==grid.shape else ValueError",
  "all WaveFunction2D(...) sites", "tests/test_2d_solver.py::test_2d_norm_conservation:11",
  "VERIFIED")
E("WaveFunction2D.probability_density", "property", "none", "float64 (N_x,N_y)", "|psi|^2", "NONE",
  "observables; visualization; tests", "tests/test_rotation.py::test_rotating_frame_energy_conserved_in_anisotropic_trap:61",
  "VERIFIED")
E("WaveFunction2D.norm", "method", "none", "float", "sum(|psi|^2)*dx*dy", "NONE",
  "runner.py; examples; benchmarks/validation_suite.py:95",
  "tests/test_2d_solver.py::test_2d_norm_conservation:11; test_rotation.py::test_coherent_state_in_rotating_frame:19",
  "VERIFIED")
E("WaveFunction2D.normalize", "method", "none", "self", "psi/=sqrt(norm) if norm>0", "silent if norm==0",
  "benchmarks/validation_suite.py:112,201; examples/11:158",
  "tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99",
  "VERIFIED")
E("WaveFunction2D.fourier_transform", "method", "none", "complex128 (N_x,N_y)",
  "fft2(psi)*dx*dy/(2pi)", "NONE",
  "observables/expectation.py:77,106; observables/momentum.py:5",
  "indirect: tests/test_3d_observables.py::test_3d_momentum_probability_density:72",
  "VERIFIED - Parseval test (test_3d_observables.py:79)")
E("WaveFunction2D.copy", "method", "none", "WaveFunction2D", "WaveFunction2D(grid, psi.copy())", "NONE",
  "runner.py:156,166; benchmarks/perf_comparison.py",
  "tests/test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73",
  "PARTIALLY")
E("WaveFunction2D.gaussian", "classmethod", "grid:Grid2D, x0,y0,k0_x,k0_y,sigma_x,sigma_y",
  "WaveFunction2D normalised",
  "product of 1D Gaussians in X and Y, then normalize",
  "sigma==0 not guarded",
  "runner.py; examples/05:37,13:60; benchmarks/validation_suite.py:102,136,191,285,297",
  "tests/test_2d_solver.py::test_2d_norm_conservation:11; test_rotation.py::test_coherent_state_in_rotating_frame:19",
  "VERIFIED - rotating-frame coherent-state check 1.89e-08")
E("WaveFunction3D", "class", "grid:Grid3D, psi=None", "psi complex128 (N_x,N_y,N_z)", "container",
  "shape check (ValueError)",
  "solvers/split_step_3d.py:65; split_step_3d_gpu.py:93,105,123; examples/11:157",
  "tests/test_3d_solver.py::test_3d_gaussian_norm:53; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42",
  "VERIFIED")
E("WaveFunction3D.__init__", "method", "grid:Grid3D, psi=None", "psi complex128 (N_x,N_y,N_z)",
  "zeros or np.array(psi,complex)", "ENFORCED shape==grid.shape else ValueError",
  "all WaveFunction3D(...) sites", "tests/test_3d_solver.py::test_3d_gaussian_norm:53",
  "VERIFIED")
E("WaveFunction3D.probability_density", "property", "none", "float64 (N_x,N_y,N_z)", "|psi|^2", "NONE",
  "observables; visualization; tests", "tests/test_3d_solver.py::test_3d_gaussian_norm:53",
  "VERIFIED")
E("WaveFunction3D.norm", "method", "none", "float", "sum(|psi|^2)*dx*dy*dz", "NONE",
  "runner.py; examples; benchmarks/validation_suite.py:95",
  "tests/test_3d_solver.py::test_3d_norm_conservation:72; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42",
  "VERIFIED - 3D norm conservation 2.55e-15")
E("WaveFunction3D.normalize", "method", "none", "self", "psi/=sqrt(norm) if norm>0", "silent if norm==0",
  "benchmarks/validation_suite.py:112,201; examples/11:158",
  "tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99",
  "VERIFIED")
E("WaveFunction3D.fourier_transform", "method", "none", "complex128 (N_x,N_y,N_z)",
  "fftn(psi)*dx*dy*dz/(2pi)^1.5", "NONE",
  "observables/expectation.py:77,106; observables/momentum.py:5",
  "indirect: tests/test_3d_observables.py::test_3d_momentum_probability_density:72",
  "VERIFIED - Parseval test")
E("WaveFunction3D.copy", "method", "none", "WaveFunction3D", "WaveFunction3D(grid, psi.copy())", "NONE",
  "runner.py:156,166; benchmarks/perf_comparison.py",
  "tests/test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73",
  "PARTIALLY")
E("WaveFunction3D.slice_xy", "method", "z_idx:int=None", "float64 (N_x,N_y)",
  "probability_density[:,:,z_idx] (default N_z//2)",
  "ENFORCED: z_idx out of range -> IndexError (not guarded)",
  "TEST-ONLY: tests/test_3d_solver.py:63",
  "tests/test_3d_solver.py::test_3d_wavefunction_slices_shape:60",
  "PARTIALLY - shape only")
E("WaveFunction3D.slice_xz", "method", "y_idx:int=None", "float64 (N_x,N_z)",
  "probability_density[:,y_idx,:] (default N_y//2)", "not guarded",
  "TEST-ONLY: tests/test_3d_solver.py:64",
  "tests/test_3d_solver.py::test_3d_wavefunction_slices_shape:60",
  "PARTIALLY")
E("WaveFunction3D.slice_yz", "method", "x_idx:int=None", "float64 (N_y,N_z)",
  "probability_density[x_idx,:,:] (default N_x//2)", "not guarded",
  "TEST-ONLY: tests/test_3d_solver.py:65",
  "tests/test_3d_solver.py::test_3d_wavefunction_slices_shape:60",
  "PARTIALLY")
E("WaveFunction3D.gaussian", "classmethod",
  "grid:Grid3D, x0,y0,z0,k0_x,k0_y,k0_z,sigma_x,sigma_y,sigma_z",
  "WaveFunction3D normalised", "product of 3 1D Gaussians, then normalize",
  "sigma==0 not guarded",
  "runner.py; examples/06:33,07:59; benchmarks/validation_suite.py:85,102,136,191,285,297",
  "tests/test_3d_solver.py::test_3d_gaussian_norm:53; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24",
  "VERIFIED - minimum-uncertainty 3D check 4.6e-12")

# =====================================================================
# quantumlab/core/absorbing_boundary.py
# =====================================================================
E("AbsorbingBoundaryLayer", "class", "grid:Grid1D/2D/3D, boundary_width:float, order:int=3",
  "object; mask float64 grid.shape; boundary_width,order",
  "separable polynomial mask, 1 interior -> 0 at edges",
  "ENFORCED: boundary_width real finite >0 (TypeError/ValueError); order Integral >=1; grid type else TypeError",
  "runner.py:148; examples/05:42,06:43,07:60,12:64; benchmarks/validation_suite.py:221",
  "tests/test_absorbing_boundary_validation.py (all); test_2d_solver.py::test_absorbing_boundary_1d:36; test_3d_solver.py::test_abl_3d_shape:109; test_split_operator.py::test_absorber_removes_outgoing_flux:124",
  "VERIFIED - mask finiteness/monotonicity tests; HHG check uses absorber")
E("AbsorbingBoundaryLayer.__init__", "method", "grid, boundary_width:float, order:int=3",
  "sets grid,boundary_width,order,mask", "validates then _build_mask()",
  "ENFORCED (see class)",
  "all AbsorbingBoundaryLayer(...) sites", "tests/test_absorbing_boundary_validation.py::test_valid_arguments_build_a_clean_mask:70",
  "VERIFIED - probe: orders 1..6 all finite, min 0.0 max 1.0")
E("AbsorbingBoundaryLayer._polynomial_profile", "method", "d:ndarray",
  "float64 same shape, in [0,1]",
  "clip(d,0,1); order<=3: d^2(3-2d); order==4: 6d^5-15d^4+10d^3; else Bernstein sum",
  "ENFORCED: clips d to [0,1]",
  "internal: _build_mask_1d:98,102; _2d:117,118,121,122; _3d:137,138,141,142,145,146",
  "indirect: tests/test_absorbing_boundary_validation.py::test_mask_is_monotone_from_edge_to_interior:89 (order 3); test_valid_arguments_build_a_clean_mask:70 (orders 1,3,4,6)",
  "PARTIALLY - orders 1..6 probed finite; general Bernstein branch only order 6 exercised")
E("AbsorbingBoundaryLayer._binomial", "method", "n,k:int", "int", "math.comb(n,k)", "NONE",
  "internal: _polynomial_profile:69,70",
  "indirect: order>4 mask tests",
  "PARTIALLY")
E("AbsorbingBoundaryLayer._build_mask", "method", "none", "float64 grid.shape",
  "dispatch on grid type", "ENFORCED: TypeError for unsupported grid",
  "internal: __init__:51",
  "indirect: all ABL tests",
  "PARTIALLY")
E("AbsorbingBoundaryLayer._build_mask_1d", "method", "none", "float64 (N,)",
  "prod of left/right polynomial profiles; right_edge=x.max()+dx", "NONE",
  "internal: _build_mask:82",
  "indirect: tests/test_absorbing_boundary_validation.py::test_interior_is_unity_and_edges_are_absorbed:78",
  "VERIFIED - edge/interior/monotonicity tests")
E("AbsorbingBoundaryLayer._build_mask_2d", "method", "none", "float64 (N_x,N_y)",
  "outer product mask_x[:,None]*mask_y[None,:]", "NONE",
  "internal: _build_mask:84",
  "indirect: tests/test_2d_solver.py::test_absorbing_boundary_2d:46",
  "VERIFIED - 2D shape/edge test")
E("AbsorbingBoundaryLayer._build_mask_3d", "method", "none", "float64 (N_x,N_y,N_z)",
  "separable outer product over x,y,z", "NONE",
  "internal: _build_mask:86",
  "indirect: tests/test_3d_solver.py::test_abl_3d_corners_absorbed:123",
  "VERIFIED - 3D corner/interior tests")
E("AbsorbingBoundaryLayer.apply", "method", "wavefunction",
  "wavefunction (in-place; psi *= mask)", "psi *= mask",
  "ENFORCED: shape mismatch would broadcast-error (not explicit)",
  "runner.py:163; examples/05:55,06:49",
  "tests/test_2d_solver.py::test_abl_norm_decay:55; test_3d_solver.py::test_abl_3d_norm_decay:134; test_absorbing_boundary_validation.py::test_absorber_still_removes_probability:96",
  "VERIFIED - norm-decay tests; HHG flux absorption")

# =====================================================================
# quantumlab/core/spectral.py
# =====================================================================
E("ndim", "function", "grid:Grid1D/2D/3D", "int 1/2/3",
  "isinstance dispatch", "ENFORCED: TypeError for unsupported grid",
  "solvers/split_operator.py:115,173",
  "indirect: every solver/stationary test",
  "PARTIALLY")
E("wavefunction_class", "function", "grid", "WaveFunction1D/2D/3D class",
  "{1:WF1D,2:WF2D,3:WF3D}[ndim(grid)]", "Propagates ndim TypeError",
  "solvers/split_operator.py:132; multicomponent.py:69; stationary/conjugate_gradient.py:132; eigensolver.py:99; imaginary_time.py:104,222",
  "indirect: all solver/stationary tests",
  "PARTIALLY")
E("volume_element", "function", "grid", "float dV", "dx | dx*dy | dx*dy*dz", "NONE",
  "observables/current.py:32,37; observables/nonlinear.py:8,29; solvers/multicomponent.py:68; split_operator.py:133; stationary/conjugate_gradient.py:50; eigensolver.py:98; imaginary_time.py:103,221; strongfield.py:132",
  "tests/test_stationary.py:10 (direct)",
  "VERIFIED - probe: 1.0,1.0,1.0 for unit cells")
E("coordinates", "function", "grid", "tuple of meshes",
  "(x,) | (X,Y) | (X,Y,Z)", "Propagates ndim TypeError",
  "potentials/coulomb.py:24; time_dependent.py:73,96; traps.py:28; stationary/imaginary_time.py:41",
  "indirect: potential tests",
  "PARTIALLY")
E("wavevectors", "function", "grid", "tuple of k-meshes",
  "(k,) | (K_x,K_y) | (K_x,K_y,K_z) in FFT order", "Propagates ndim TypeError",
  "observables/current.py:14; spectral.k_squared:56",
  "indirect: probability_current tests",
  "PARTIALLY")
E("k_squared", "function", "grid", "float64 grid.shape", "sum K_j^2", "NONE",
  "solvers/split_operator.py:137; stationary/conjugate_gradient.py:52; eigensolver.py:48; hamiltonian.py:13",
  "indirect: all spectral checks",
  "VERIFIED - spectra/energies checks")
E("k_volume_element", "function", "grid", "float dk | dk_x*dk_y | dk_x*dk_y*dk_z",
  "product of grid dk's", "NONE",
  "NONE - zero references anywhere in repo",
  "NONE",
  "NONE - dead code (probe confirms it computes, but nothing consumes it)")

# =====================================================================
# quantumlab/potentials/base.py
# =====================================================================
E("Potential", "class", "abstract", "abstract base",
  "interface: evaluate(grid)->ndarray", "abstractmethod evaluate",
  "subclassed at potentials/barriers.py:5,20,35,47,68,96,133; wells.py:5,20,35; oscillator.py:5; periodic.py:5; disorder.py:5; custom.py:5; traps.py:6; coulomb.py:6; apertures.py:11,79; time_dependent.py:16",
  "NONE (abstract; exercised through subclasses)",
  "PARTIALLY - contract enforced by subclass tests")
E("Potential.evaluate", "method", "grid", "ndarray", "abstract", "abstractmethod",
  "called dynamically at solvers/split_operator.py:143; split_step_1d.py:10; 2d:19; 3d:41; 3d_gpu:60,68; multicomponent.py:71; stationary/*; observables/expectation.py:143; visualization/*",
  "tests/test_potentials.py (all); test_new_potentials_and_observables.py (all)",
  "VERIFIED - through concrete potential tests")

# =====================================================================
# quantumlab/potentials/apertures.py
# =====================================================================
E("_smooth_step", "function", "u:ndarray", "float64 same shape in (0,1)",
  "0.5*(1+tanh(u))", "NONE",
  "internal: ApertureScreen.evaluate:65,74; StadiumBilliard.evaluate:102",
  "indirect: aperture/stadium tests",
  "PARTIALLY")
E("ApertureScreen", "class",
  "V0, wall_position=0, wall_thickness=1, separation=4, aperture_width=1, n_apertures=2, aperture='slit', smoothing=0.25",
  "object; V array", "opaque screen with n smoothed openings",
  "ENFORCED: aperture in {'slit','pinhole'} else ValueError",
  "examples/07_3d_double_slit.py:50; registry potentials/__init__.py:35,36",
  "tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26; test_aperture_screen_slits_are_translation_invariant_in_z:41; test_volume_3d.py::test_renderer_writes_png:43",
  "PARTIALLY - geometry tests, no analytic reference")
E("ApertureScreen.__init__", "method", "see class", "sets fields", "validation of aperture string",
  "ENFORCED aperture string",
  "all ApertureScreen(...) sites", "tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26",
  "PARTIALLY")
E("ApertureScreen.aperture_centers", "property", "none", "float64 (n_apertures,)",
  "(i-(n-1)/2)*separation", "NONE",
  "internal: evaluate:69; tests/test_new_potentials_and_observables.py:38",
  "tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26",
  "PARTIALLY")
E("ApertureScreen.evaluate", "method", "grid:Grid2D/Grid3D", "float64 grid.shape",
  "V0*wall*(1-opening); wall=smoothstep pair; opening=sum of smoothstep slits/pinholes clipped",
  "ENFORCED: TypeError if not Grid2D/Grid3D",
  "solvers (dynamic); tests/test_new_potentials_and_observables.py:30,43",
  "tests/test_new_potentials_and_observables.py::test_aperture_screen_geometry_3d_pinholes:26; test_aperture_screen_slits_are_translation_invariant_in_z:41",
  "PARTIALLY")
E("StadiumBilliard", "class", "V0, radius, length, smoothing=0.2", "object",
  "soft-walled stadium potential", "NONE",
  "examples/10_quantum_chaos_stadium.py:35; registry potentials/__init__.py:37",
  "tests/test_new_potentials_and_observables.py::test_stadium_is_open_inside_and_closed_outside:47; test_stationary.py::test_lanczos_and_lobpcg_agree_on_chaotic_billiard:38",
  "PARTIALLY - geometry + cross-solver agreement, no analytic energies")
E("StadiumBilliard.__init__", "method", "see class", "sets fields", "none", "NONE",
  "all StadiumBilliard(...) sites", "tests/test_new_potentials_and_observables.py::test_stadium_is_open_inside_and_closed_outside:47",
  "PARTIALLY")
E("StadiumBilliard.evaluate", "method", "grid:Grid2D", "float64 (N_x,N_y)",
  "V0*smoothstep((dist-R)/s), dist=distance to segment [-L/2,L/2] on x",
  "ENFORCED: TypeError if not Grid2D",
  "solvers (dynamic); tests/test_new_potentials_and_observables.py:49; test_stationary.py:40",
  "tests/test_new_potentials_and_observables.py::test_stadium_is_open_inside_and_closed_outside:47; test_stationary.py::test_lanczos_and_lobpcg_agree_on_chaotic_billiard:38",
  "PARTIALLY")

# =====================================================================
# quantumlab/potentials/barriers.py
# =====================================================================
E("GaussianBarrier", "class", "V0, width, position=0", "object",
  "V0*exp(-((x-position)/width)^2)", "NONE",
  "examples/01_gaussian_barrier.py:32; testbench_interlock.py:99; registry potentials/__init__.py:20,21",
  "tests/test_potentials.py::test_gaussian_barrier:12; test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_norm_and_energy_conservation:50",
  "PARTIALLY - peak/edge assertions only")
E("GaussianBarrier.__init__", "method", "see class", "sets fields", "none", "NONE",
  "all GaussianBarrier(...) sites", "tests/test_potentials.py::test_gaussian_barrier:12",
  "PARTIALLY")
E("GaussianBarrier.evaluate", "method", "grid:Grid1D/2D/3D", "float64 grid.shape",
  "V0*exp(-((X-position)/width)^2)", "NONE (accepts any grid type; no validation)",
  "solvers (dynamic); tests/test_potentials.py:18; test_solvers.py:12,23",
  "tests/test_potentials.py::test_gaussian_barrier:12; test_solvers.py::test_energy_conservation:20",
  "PARTIALLY")
E("RectangularBarrier", "class", "V0, width, position=0", "object", "rectangular barrier",
  "NONE", "registry potentials/__init__.py:24",
  "tests/test_potentials.py::test_rectangular_barrier:25",
  "PARTIALLY")
E("RectangularBarrier.__init__", "method", "see class", "sets fields", "none", "NONE",
  "tests/test_potentials.py:30", "tests/test_potentials.py::test_rectangular_barrier:25", "PARTIALLY")
E("RectangularBarrier.evaluate", "method", "grid:Grid1D/2D/3D", "float64 grid.shape",
  "where(|x-position|<=width/2, V0, 0)", "NONE",
  "solvers (dynamic); tests/test_potentials.py:31",
  "tests/test_potentials.py::test_rectangular_barrier:25",
  "PARTIALLY")
E("PotentialStep", "class", "V0, position=0", "object", "step potential", "NONE",
  "NONE (registry-only: potentials/__init__.py:25)",
  "NONE (imported unused at tests/test_potentials.py:4)",
  "NONE")
E("PotentialStep.__init__", "method", "see class", "sets fields", "none", "NONE",
  "NONE", "NONE", "NONE")
E("PotentialStep.evaluate", "method", "grid", "float64 grid.shape",
  "where(x>=position, V0, 0)", "NONE",
  "NONE (no call site; only generic Potential.evaluate dispatch could reach it)",
  "NONE", "NONE")
E("MultipleBarriers", "class", "V0, width, positions:list", "object", "sum of rectangles",
  "NONE", "examples/04_multiple_barriers.py:33; registry potentials/__init__.py:26",
  "NONE", "NONE")
E("MultipleBarriers.__init__", "method", "see class", "sets fields", "none", "NONE",
  "examples/04_multiple_barriers.py:33", "NONE", "NONE")
E("MultipleBarriers.evaluate", "method", "grid", "float64 grid.shape",
  "V[pos-width/2<=x<=pos+width/2]=V0 for each pos", "NONE",
  "solvers (dynamic); examples/04:40",
  "NONE", "NONE")
E("ResonantTunnelingDiode", "class", "V0, barrier_width, well_width, position=0", "object",
  "double barrier", "NONE",
  "NONE (registry-only: potentials/__init__.py:27)",
  "NONE", "NONE")
E("ResonantTunnelingDiode.__init__", "method", "see class", "sets fields", "none", "NONE",
  "NONE", "NONE", "NONE")
E("ResonantTunnelingDiode.evaluate", "method", "grid", "float64 grid.shape",
  "two barriers at pos_left/pos_right", "NONE",
  "NONE (no call site; only generic Potential.evaluate dispatch could reach it)", "NONE", "NONE")
E("Gaussian2DBarrier", "class", "V0, width, x0=0, y0=0", "object",
  "isotropic 2D Gaussian", "NONE",
  "examples/05_2d_gaussian_barrier.py:40; registry potentials/__init__.py:22",
  "tests/test_split_operator.py::test_order2_matches_legacy_solvers:26",
  "PARTIALLY")
E("Gaussian2DBarrier.__init__", "method", "see class", "sets fields", "none", "NONE",
  "tests/test_split_operator.py:34", "tests/test_split_operator.py::test_order2_matches_legacy_solvers:26", "PARTIALLY")
E("Gaussian2DBarrier.evaluate", "method", "grid:Grid2D/3D", "float64 grid.shape",
  "V0*exp(-((X-x0)^2+(Y-y0)^2)/width^2)", "ENFORCED: TypeError if not 2D/3D",
  "solvers (dynamic); tests/test_split_operator.py:34",
  "tests/test_split_operator.py::test_order2_matches_legacy_solvers:26",
  "PARTIALLY")
E("Gaussian3DBarrier", "class", "V0, width, x0=0,y0=0,z0=0", "object",
  "isotropic 3D Gaussian", "NONE",
  "examples/06_3d_gaussian_barrier.py:41; benchmarks/perf_comparison.py:91; registry potentials/__init__.py:23",
  "tests/test_3d_solver.py::test_gaussian3d_barrier_peak:152; test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_split_operator.py::test_order2_matches_legacy_solvers:26",
  "PARTIALLY")
E("Gaussian3DBarrier.__init__", "method", "see class", "sets fields", "none", "NONE",
  "tests/test_3d_solver.py:155,166", "tests/test_3d_solver.py::test_gaussian3d_barrier_symmetry:163", "PARTIALLY")
E("Gaussian3DBarrier.evaluate", "method", "grid:Grid3D", "float64 (N_x,N_y,N_z)",
  "V0*exp(-r^2/width^2)", "ENFORCED: TypeError if not Grid3D",
  "solvers (dynamic); tests/test_3d_solver.py:156,167",
  "tests/test_3d_solver.py::test_gaussian3d_barrier_peak:152; test_gaussian3d_barrier_symmetry:163",
  "PARTIALLY")

# =====================================================================
# quantumlab/potentials/coulomb.py
# =====================================================================
E("SoftCoulomb", "class", "Z=1.0, softening=sqrt(2), center=None", "object",
  "soft-core Coulomb potential", "NONE",
  "benchmarks/validation_suite.py:210,312; examples/12:86; registry potentials/__init__.py:38",
  "tests/test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33; test_soft_coulomb_gradient_matches_finite_difference:40; test_conjugate_gradient.py::test_linear_ground_states_to_machine_precision:19",
  "VERIFIED - hydrogen E0=-0.5 to 1.94e-14; gradient vs finite difference")
E("SoftCoulomb.__init__", "method", "see class", "sets fields", "none", "NONE",
  "all SoftCoulomb(...) sites", "tests/test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33",
  "VERIFIED")
E("SoftCoulomb._displacements", "method", "grid", "tuple of arrays",
  "coords - center (broadcast)", "NONE",
  "internal: evaluate:30; gradient:35",
  "indirect: SoftCoulomb tests",
  "PARTIALLY")
E("SoftCoulomb.evaluate", "method", "grid", "float64 grid.shape",
  "-Z/sqrt(r^2+a^2)", "NONE",
  "solvers (dynamic); tests/test_strongfield.py:44",
  "tests/test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33; test_soft_coulomb_gradient_matches_finite_difference:40",
  "VERIFIED - hydrogen ground state 1.94e-14; probe V(0)=-0.7071 for a=sqrt2")
E("SoftCoulomb.gradient", "method", "grid", "tuple of float64 arrays",
  "Z*d_i/(r^2+a^2)^1.5", "NONE",
  "strongfield.py:127; tests/test_strongfield.py:45",
  "tests/test_strongfield.py::test_soft_coulomb_gradient_matches_finite_difference:40",
  "VERIFIED - finite-difference comparison atol 1e-3")

# =====================================================================
# quantumlab/potentials/custom.py
# =====================================================================
E("CustomPotential", "class", "func:callable", "object", "user potential", "ENFORCED callable",
  "benchmarks/validation_suite.py:53; tests/test_split_operator.py:67,82",
  "tests/test_potentials.py::test_custom_potential:45; test_new_potentials_and_observables.py::test_custom_potential_3d:57; test_split_operator.py::test_convergence_order:64",
  "VERIFIED - convergence-order check uses CustomPotential")
E("CustomPotential.__init__", "method", "func", "sets func", "stores func; no evaluation",
  "ENFORCED TypeError if not callable",
  "all CustomPotential(...) sites", "tests/test_potentials.py::test_custom_potential:45",
  "PARTIALLY")
E("CustomPotential.evaluate", "method", "grid:Grid1D/2D/3D", "ndarray",
  "func(x) | func(X,Y) | func(X,Y,Z)", "NONE (return type/shape not validated)",
  "solvers (dynamic); tests/test_potentials.py:49; test_new_potentials_and_observables.py:59",
  "tests/test_potentials.py::test_custom_potential:45; test_new_potentials_and_observables.py::test_custom_potential_3d:57",
  "PARTIALLY")

# =====================================================================
# quantumlab/potentials/disorder.py
# =====================================================================
E("RandomDisorder", "class", "W, cell_width, seed=None", "object",
  "piecewise-constant random disorder", "NONE",
  "NONE (registry-only: potentials/__init__.py:33; imported unused at tests/test_potentials.py:8)",
  "NONE", "NONE")
E("RandomDisorder.__init__", "method", "see class", "sets fields", "none", "NONE",
  "NONE", "NONE", "NONE")
E("RandomDisorder.evaluate", "method", "grid:Grid1D/2D", "float64 grid.shape",
  "rng.uniform(-W/2,W/2,num_cells)[cell index]", "NONE (seed=None -> nondeterministic)",
  "NONE (no call site; only generic Potential.evaluate dispatch could reach it)", "NONE", "NONE")

# =====================================================================
# quantumlab/potentials/oscillator.py
# =====================================================================
E("HarmonicOscillator", "class", "omega, m=1, position=0", "object", "harmonic potential",
  "NONE", "examples/02_harmonic_oscillator.py:30; registry potentials/__init__.py:31",
  "tests/test_potentials.py::test_harmonic_oscillator:36; test_2d_solver.py::test_2d_energy_conservation:23; test_3d_solver.py::test_3d_energy_conservation_harmonic:86",
  "PARTIALLY - analytic 1D formula asserted")
E("HarmonicOscillator.__init__", "method", "see class", "sets fields", "none", "NONE",
  "all HarmonicOscillator(...) sites", "tests/test_potentials.py::test_harmonic_oscillator:36",
  "PARTIALLY")
E("HarmonicOscillator.evaluate", "method", "grid:Grid1D/2D/3D", "float64 grid.shape",
  "0.5*m*omega^2*(x-position)^2 (sum over axes)", "NONE",
  "solvers (dynamic); tests/test_potentials.py:41",
  "tests/test_potentials.py::test_harmonic_oscillator:36; test_2d_solver.py::test_2d_energy_conservation:23",
  "VERIFIED - analytic 1D formula allclose; 2D/3D energy conservation")

# =====================================================================
# quantumlab/potentials/periodic.py
# =====================================================================
E("CrystalPotential", "class", "V0, lattice_spacing, position=0", "object",
  "sin^2 lattice", "NONE",
  "NONE (registry-only: potentials/__init__.py:32; imported unused at tests/test_potentials.py:7)",
  "NONE", "NONE")
E("CrystalPotential.__init__", "method", "see class", "sets fields", "none", "NONE",
  "NONE", "NONE", "NONE")
E("CrystalPotential.evaluate", "method", "grid:Grid1D/2D", "float64 grid.shape",
  "V0*sin(pi*(x-position)/lattice_spacing)^2", "NONE",
  "NONE (no call site; only generic Potential.evaluate dispatch could reach it)", "NONE", "NONE")

# =====================================================================
# quantumlab/potentials/time_dependent.py
# =====================================================================
E("TimeDependentPotential", "class", "abstract", "abstract base; time_dependent=True",
  "interface evaluate_at(grid,t)", "abstractmethod evaluate_at; evaluate(grid)=evaluate_at(grid,0)",
  "subclassed at time_dependent.py:27,87",
  "NONE (abstract; exercised through DipoleDrive/TimeDependentCustomPotential)",
  "PARTIALLY")
E("TimeDependentPotential.evaluate_at", "method", "grid, t:float", "ndarray", "abstract",
  "abstractmethod",
  "solvers/split_operator.py:191 (dynamic dispatch)",
  "tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69; test_dipole_drive_rejects_missing_axis:79",
  "VERIFIED - driven-oscillator Ehrenfest check 5.60e-09")
E("TimeDependentPotential.evaluate", "method", "grid", "ndarray",
  "evaluate_at(grid, 0.0)", "NONE",
  "NONE established (subclasses override evaluate_at; generic .evaluate sites target static potentials)",
  "NONE", "NONE")
E("DipoleDrive", "class",
  "base:Potential|None, F0, omega, axis='x', phase=0, envelope=None",
  "object; time_dependent=True",
  "V(r,t)=V_base(r)-F(t)*r_axis; F(t)=F0*env(t)*sin(omega t+phase)",
  "ENFORCED axis in {x,y,z} else ValueError; axis availability checked at evaluate time",
  "benchmarks/validation_suite.py:70,219; examples/12:63; tests/test_split_operator.py:93,107,141",
  "tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69; test_split_operator.py::test_driven_oscillator_follows_classical_trajectory:90",
  "VERIFIED - Ehrenfest driven oscillator 5.60e-09; HHG odd-harmonic check")
E("DipoleDrive.__init__", "method", "see class", "sets fields + cache",
  "stores base/F0/omega/axis/phase/envelope; initialises cache",
  "ENFORCED axis",
  "all DipoleDrive(...) sites", "tests/test_new_potentials_and_observables.py::test_dipole_drive_rejects_missing_axis:79",
  "PARTIALLY")
E("DipoleDrive.force", "method", "t:float", "float",
  "F0*env(t)*sin(omega*t+phase)", "ENFORCED: envelope must be callable if given (not validated)",
  "strongfield callbacks; examples/12:68,198,218,233,245; benchmarks/validation_suite.py:224",
  "tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69",
  "VERIFIED - driven oscillator + HHG")
E("DipoleDrive._static_parts", "method", "grid", "tuple (V_base, r_axis)",
  "cached base potential and axis coordinate", "ENFORCED: ValueError if axis unavailable on grid",
  "internal: evaluate_at:83",
  "indirect: DipoleDrive tests",
  "PARTIALLY")
E("DipoleDrive.evaluate_at", "method", "grid, t:float", "float64 grid.shape",
  "V_base - force(t)*r_axis", "ENFORCED axis (via _static_parts)",
  "solvers/split_operator.py:191 (dynamic); tests/test_new_potentials_and_observables.py:76,81",
  "tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69; test_dipole_drive_rejects_missing_axis:79",
  "VERIFIED - driven oscillator Ehrenfest")
E("TimeDependentCustomPotential", "class", "func:callable", "object",
  "user V(r,t)", "ENFORCED callable",
  "tests/test_split_operator.py:108; registry via potentials/__init__.py:15 export",
  "tests/test_split_operator.py::test_time_dependent_custom_potential_matches_dipole_drive:104",
  "PARTIALLY - cross-check vs DipoleDrive")
E("TimeDependentCustomPotential.__init__", "method", "func", "sets func",
  "stores func; evaluate_at broadcasts func(*coords,t)",
  "ENFORCED TypeError",
  "tests/test_split_operator.py:108", "tests/test_split_operator.py::test_time_dependent_custom_potential_matches_dipole_drive:104",
  "PARTIALLY")
E("TimeDependentCustomPotential.evaluate_at", "method", "grid, t:float", "float64 grid.shape",
  "broadcast_to(func(*coordinates,t), grid.shape).astype(float)", "ENFORCED: broadcast error if shape mismatch",
  "solvers/split_operator.py:191 (dynamic)",
  "tests/test_split_operator.py::test_time_dependent_custom_potential_matches_dipole_drive:104",
  "PARTIALLY")
E("sin2_envelope", "function", "duration:float",
  "callable t->float in [0,1]", "sin^2(pi t/duration) on (0,duration), else 0",
  "ENFORRED: duration<=0 -> division issues (not guarded)",
  "tests/test_new_potentials_and_observables.py:70",
  "tests/test_new_potentials_and_observables.py::test_sin2_envelope_and_dipole_force:69",
  "PARTIALLY")
E("flat_top_envelope", "function", "duration:float, ramp:float",
  "callable t->float in [0,1]", "sin^2 ramps of length ramp, flat 1 between, 0 outside",
  "ENFORCED: ValueError unless 0 < 2*ramp <= duration",
  "benchmarks/validation_suite.py:220; examples/12:63",
  "tests/test_strongfield.py::test_flat_top_envelope:50",
  "VERIFIED - used in HHG validation (odd harmonics, attosecond train)")

# =====================================================================
# quantumlab/potentials/traps.py
# =====================================================================
E("HarmonicTrap", "class", "omegas:float|seq, m=1.0, center=None", "object",
  "anisotropic harmonic trap", "NONE",
  "benchmarks/validation_suite.py (many); examples/08:48,74,11:68,71,155,13:68,197,198; benchmarks/gpu_split_operator.py:25",
  "tests/test_new_potentials_and_observables.py::test_harmonic_trap_isotropic_matches_oscillator:15; test_harmonic_trap_anisotropic_and_centered:20; test_stationary.py::test_1d_harmonic_spectrum_lanczos:14",
  "VERIFIED - harmonic spectra exact to 7.28e-14; GP virial")
E("HarmonicTrap.__init__", "method", "see class", "sets fields", "none", "NONE",
  "all HarmonicTrap(...) sites", "tests/test_new_potentials_and_observables.py::test_harmonic_trap_anisotropic_and_centered:20",
  "PARTIALLY")
E("HarmonicTrap.evaluate", "method", "grid:Grid1D/2D/3D", "float64 grid.shape",
  "0.5*m*sum_j omega_j^2 (r_j-c_j)^2", "NONE",
  "solvers (dynamic); tests/test_new_potentials_and_observables.py:17,22",
  "tests/test_new_potentials_and_observables.py::test_harmonic_trap_isotropic_matches_oscillator:15; test_stationary.py::test_1d_harmonic_spectrum_lanczos:14",
  "VERIFIED - exact spectra, virial, rotating frame")

# =====================================================================
# quantumlab/potentials/wells.py
# =====================================================================
E("InfiniteSquareWell", "class", "width, position=0, V_inf=1e9", "object",
  "infinite well", "NONE",
  "NONE (registry-only: potentials/__init__.py:28)",
  "NONE", "NONE")
E("InfiniteSquareWell.__init__", "method", "see class", "sets fields", "none", "NONE",
  "NONE", "NONE", "NONE")
E("InfiniteSquareWell.evaluate", "method", "grid:Grid1D/2D", "float64 grid.shape",
  "0 inside |x-position|<=width/2 else V_inf", "NONE",
  "NONE (no call site; only generic Potential.evaluate dispatch could reach it)", "NONE", "NONE")
E("FiniteSquareWell", "class", "V0, width, position=0", "object", "finite well", "NONE",
  "registry potentials/__init__.py:29",
  "tests/test_potentials.py::test_potential_factory:52",
  "PARTIALLY - factory/attrs only")
E("FiniteSquareWell.__init__", "method", "see class", "sets fields", "none", "NONE",
  "tests/test_potentials.py:53", "tests/test_potentials.py::test_potential_factory:52", "PARTIALLY")
E("FiniteSquareWell.evaluate", "method", "grid:Grid1D/2D", "float64 grid.shape",
  "0 inside well else V0", "NONE",
  "solvers (dynamic, generic .evaluate only)",
  "tests/test_potentials.py::test_potential_factory:52 (indirect)",
  "PARTIALLY")
E("DoubleWell", "class", "V0, barrier_distance, position=0", "object", "quartic double well",
  "NONE", "examples/03_double_well.py:31; registry potentials/__init__.py:30",
  "NONE", "NONE")
E("DoubleWell.__init__", "method", "see class", "sets fields", "none", "NONE",
  "examples/03_double_well.py:31", "NONE", "NONE")
E("DoubleWell.evaluate", "method", "grid:Grid1D/2D", "float64 grid.shape",
  "V0*((x-position)/barrier_distance)^2-1)^2", "NONE",
  "solvers (dynamic); examples/03:40", "NONE", "NONE")

# =====================================================================
# quantumlab/potentials/__init__.py
# =====================================================================
E("create_potential", "function", "name:str, **kwargs", "Potential instance",
  "POTENTIAL_REGISTRY[name.lower()](**kwargs)",
  "ENFORCED: ValueError if name unknown",
  "runner.py:141",
  "tests/test_potentials.py::test_potential_factory:52; test_new_potentials_and_observables.py::test_registry_has_new_potentials:63; test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33",
  "PARTIALLY - registry dispatch tested; physics of each entry tested separately")

# =====================================================================
# quantumlab/solvers/base.py
# =====================================================================
E("Solver", "class", "grid, potential, dt, hbar=1, m=1", "abstract base",
  "interface step(wavefunction); backend property",
  "abstractmethod step",
  "subclassed at split_operator.py:42; split_step_1d.py:6; 2d:6; 3d:7; 3d_gpu:25",
  "NONE (abstract; exercised through subclasses)",
  "PARTIALLY")
E("Solver.__init__", "method", "grid, potential, dt, hbar=1, m=1",
  "sets grid,potential,dt,hbar,m", "plain assignment", "NONE",
  "super().__init__ at split_operator.py:103; split_step_1d.py:9; 2d:18; 3d:39; 3d_gpu:41",
  "indirect: all solver tests",
  "PARTIALLY")
E("Solver.step", "method", "wavefunction", "wavefunction", "abstract", "abstractmethod",
  "called dynamically: runner.py:161; stationary/imaginary_time.py:126; examples/01:39,02:40,03:40,04:40,05:54,06:48,07:83,08:110,11:99; benchmarks/validation_suite.py:143; benchmarks/perf_comparison.py:97,104,122; testbench_interlock.py:106",
  "tests/test_solvers.py::test_norm_conservation:9; test_split_operator.py::test_order2_matches_legacy_solvers:26",
  "VERIFIED - through subclass checks")
E("Solver.backend", "property", "none", "str", "returns 'scipy-cpu'", "NONE",
  "NONE (overridden by SplitOperatorSolver.backend:184, SplitStep3DGPU.backend:140, CoupledGPESolver.backend:78)",
  "NONE", "NONE")

# =====================================================================
# quantumlab/solvers/backends.py
# =====================================================================
E("ArrayBackend", "class", "name, xp, fftn, ifftn, to_device, to_host",
  "frozen dataclass", "backend bundle", "NONE",
  "constructed in numpy_backend:33; cupy_backend:50; tests/test_backends.py:57",
  "tests/test_backends.py::test_emulated_device_array_rejects_host_mixing:68",
  "VERIFIED - emulated-device strictness test")
E("cupy_available", "function", "none", "bool",
  "import cupy and getDeviceCount()>0, else False", "NONE",
  "benchmarks/gpu_split_operator.py:40; get_backend:74,78",
  "tests/test_backends.py::test_backend_selection:145",
  "PARTIALLY")
E("numpy_backend", "function", "workers=-1", "ArrayBackend(name='scipy-cpu')",
  "scipy.fft.fftn/ifftn with workers, overwrite_x=True", "NONE",
  "internal: get_backend:72,78",
  "indirect: tests/test_backends.py::test_device_code_path_matches_numpy:97",
  "VERIFIED - CPU reference path")
E("cupy_backend", "function", "device_id=0", "ArrayBackend(name='cupy')",
  "cupyx.scipy.fft with device selection", "ENFORCED: ValueError if device_id out of range",
  "internal: get_backend:76,78",
  "indirect: tests/test_backends.py::test_real_cupy_matches_cpu:158 (skipif no CUDA)",
  "VERIFIED - GPU benchmark relative_error ~1.1e-14..1.8e-14 on RTX A1000")
E("get_backend", "function", "backend='numpy', workers=-1, device_id=0", "ArrayBackend",
  "dispatch numpy/cupy/auto/ArrayBackend", "ENFORCED: ValueError for unknown; RuntimeError if cupy unavailable",
  "solvers/split_operator.py:129",
  "tests/test_backends.py::test_backend_selection:145",
  "PARTIALLY")

# =====================================================================
# quantumlab/solvers/multicomponent.py
# =====================================================================
E("CoupledGPESolver", "class",
  "grid, potentials:Sequence, couplings, dt, hbar=1,m=1,order=2,imaginary_time=False,rotation=0,damping=0,workers=-1,backend='numpy',device_id=0,t0=0",
  "object; n_components,couplings,engine", "coupled GPE propagator",
  "ENFORCED: couplings shape (n,n), symmetric, static potentials only",
  "benchmarks/validation_suite.py:261,272; examples/13:120,201; stationary/imaginary_time.py:219",
  "tests/test_multicomponent.py (all); test_backends.py::test_coupled_solver_device_path_matches_numpy:168",
  "VERIFIED - Bogoliubov/phase-separation/Manakov/virial checks")
E("CoupledGPESolver.__init__", "method", "see class", "sets fields + engine",
  "validates couplings; builds SplitOperatorSolver(grid,None,...)",
  "ENFORCED (see class)",
  "all CoupledGPESolver(...) sites", "tests/test_multicomponent.py::test_invalid_coupled_configurations:130",
  "PARTIALLY")
E("CoupledGPESolver.t", "property", "none", "float", "t0+steps_taken*dt", "NONE",
  "tests/test_multicomponent.py:73,88",
  "tests/test_multicomponent.py::test_bogoliubov_spin_mode_frequency:63",
  "PARTIALLY")
E("CoupledGPESolver.backend", "property", "none", "str", "engine backend name", "NONE",
  "NONE (no call site)", "NONE", "NONE")
E("CoupledGPESolver._densities", "method", "psis, rescale:bool", "list of arrays",
  "|psi_j|^2, optionally rescaled to target norms", "NONE",
  "internal: _potential_half_step:97,99,101",
  "indirect: coupled tests",
  "PARTIALLY")
E("CoupledGPESolver._effective_potentials", "method", "rhos", "list of arrays",
  "V_i + sum_j g_ij rho_j", "NONE",
  "internal: _potential_half_step:97,99,101",
  "indirect: coupled tests",
  "PARTIALLY")
E("CoupledGPESolver._potential_half_step", "method", "psis, w", "list of arrays",
  "exp(-i c V_eff h/2hbar) psi (frozen density real-time; midpoint rescaled imaginary/damped)",
  "NONE",
  "internal: _advance:111,113",
  "indirect: coupled tests",
  "VERIFIED - Manakov/virial/Bogoliubov")
E("CoupledGPESolver._norm", "method", "psi", "float", "sum|psi|^2*dV", "NONE",
  "internal: _advance:109,117",
  "indirect: coupled tests",
  "PARTIALLY")
E("CoupledGPESolver._advance", "method", "psis", "list of arrays",
  "Strang/Yoshida over components with renormalisation", "NONE",
  "internal: step:132; evolve:141",
  "indirect: coupled tests",
  "VERIFIED")
E("CoupledGPESolver._upload", "method", "states", "list of device arrays",
  "to_device(psi) per component", "ENFORCED: ValueError if len(states)!=n_components",
  "internal: step:132; evolve:139",
  "tests/test_multicomponent.py::test_invalid_coupled_configurations:130",
  "PARTIALLY")
E("CoupledGPESolver._download", "method", "psis", "tuple of WaveFunction",
  "wf_class(grid, to_host(p))", "NONE",
  "internal: step:132; evolve:143,144",
  "indirect: coupled tests",
  "PARTIALLY")
E("CoupledGPESolver.step", "method", "states", "tuple of WaveFunction",
  "one coupled step", "ENFORCED via _upload",
  "tests/test_multicomponent.py:140",
  "tests/test_multicomponent.py::test_invalid_coupled_configurations:130",
  "VERIFIED")
E("CoupledGPESolver.evolve", "method", "states, n_steps, callback=None, callback_interval=1",
  "tuple of WaveFunction", "n_steps coupled steps with callbacks", "NONE",
  "examples/13:142,217; benchmarks/validation_suite.py:264,275; stationary/imaginary_time.py:229",
  "tests/test_multicomponent.py::test_bogoliubov_spin_mode_frequency:63; test_energy_and_populations_conserved_in_real_time:95",
  "VERIFIED")

# =====================================================================
# quantumlab/solvers/split_operator.py
# =====================================================================
E("SplitOperatorSolver", "class",
  "grid, potential, dt, hbar=1,m=1,order=2,nonlinearity=0,imaginary_time=False,absorber=None,workers=-1,t0=0,rotation=0,damping=0,backend='numpy',device_id=0",
  "object; propagators", "generic split-operator propagator",
  "ENFORCED: order in {2,4}; order=4+imaginary_time ValueError; imaginary_time+time_dependent ValueError; damping>=0; damping requires order=2 real; rotation requires 2D/3D",
  "runner.py:106; multicomponent.py:60; stationary/imaginary_time.py:100; benchmarks/validation_suite.py (many); examples/07:60,08:99,09:34,11:76,12:64",
  "tests/test_split_operator.py (all); test_rotation.py (all); test_gross_pitaevskii.py (all); test_backends.py (all)",
  "VERIFIED - 27/27 validation checks; convergence orders 2.001/3.997")
E("SplitOperatorSolver.__init__", "method", "see class", "sets fields, builds operators",
  "validates; evaluates static V; builds _U_T/_U_V_half; sets _c",
  "ENFORCED (see class)",
  "all SplitOperatorSolver(...) sites", "tests/test_split_operator.py::test_invalid_configurations_raise:134",
  "PARTIALLY")
E("SplitOperatorSolver.update_operators", "method", "none", "sets _U_T,_U_x_half,_U_yz,_U_V_half",
  "exp(c*T_k*h/hbar) etc per substep weight w",
  "NONE",
  "internal: __init__:146",
  "indirect: all solver tests",
  "VERIFIED - convergence/norm/energy checks")
E("SplitOperatorSolver._rotating_kinetic_parts", "method", "none", "(H_x,H_yz)",
  "H_x=hbar^2 k_x^2/2m+Omega hbar y k_x; H_yz=hbar^2 k_y^2/2m-O hbar x k_y (+z term in 3D)",
  "NONE",
  "internal: update_operators:160",
  "indirect: test_rotation.py (all)",
  "VERIFIED - rotating-frame exact trajectory 1.89e-08; vortex eigenstate 1.15e-08")
E("SplitOperatorSolver.t", "property", "none", "float", "t0+steps_taken*dt", "NONE",
  "benchmarks/validation_suite.py:75,164,196,205,265,276; examples/07:81,85,88,90,93; 08:112,113,117,126; 09:39; 11:102,107,110,127; tests/test_split_operator.py:60,99; test_rotation.py:30,42",
  "tests/test_split_operator.py::test_norm_and_energy_conservation:50; test_evolve_callback_schedule:144",
  "PARTIALLY")
E("SplitOperatorSolver.backend", "property", "none", "str", "backend name", "NONE",
  "runner.py:172; tests/test_3d_gpu_solver.py:44,130,153; test_backends.py:103,164",
  "tests/test_backends.py::test_device_code_path_matches_numpy:97",
  "PARTIALLY")
E("SplitOperatorSolver.potential_at", "method", "t:float", "float64 grid.shape (host)",
  "static V or potential.evaluate_at(grid,t)", "NONE",
  "stationary/imaginary_time.py:105; internal _potential_on_device:196",
  "indirect: imaginary-time tests",
  "PARTIALLY")
E("SplitOperatorSolver._potential_on_device", "method", "t", "device array",
  "static device V or to_device(potential_at(t))", "NONE",
  "internal: _potential_half_step:204",
  "indirect: solver tests",
  "PARTIALLY")
E("SplitOperatorSolver._potential_half_step", "method", "psi, t, w", "psi (in place)",
  "exp(-i c (V+g|psi|^2) h/2hbar) psi; midpoint density variant when renormalising",
  "NONE",
  "internal: _strang:239,241",
  "indirect: all dynamics tests",
  "VERIFIED - soliton, GP, driven, HHG")
E("SplitOperatorSolver._kinetic_step", "method", "psi, w", "psi",
  "FFT -> multiply U_T (or rotated 3-factor) -> IFFT", "NONE",
  "internal: _strang:240; multicomponent.py:112",
  "indirect: all dynamics tests",
  "VERIFIED - convergence order + exact solutions")
E("SplitOperatorSolver._strang", "method", "psi, t, w", "psi",
  "V(h/2) T(h) V(h/2) at t and t+w*dt", "NONE",
  "internal: _advance:253",
  "indirect: all dynamics tests",
  "VERIFIED")
E("SplitOperatorSolver._norm", "method", "psi", "float", "sum|psi|^2*dV", "NONE",
  "internal: _advance:250,256",
  "indirect: norm tests",
  "PARTIALLY")
E("SplitOperatorSolver._advance", "method", "psi", "psi",
  "Yoshida/Strang composition + renormalisation + absorber", "NONE",
  "internal: step:271; evolve:281",
  "indirect: all dynamics tests",
  "VERIFIED")
E("SplitOperatorSolver._upload", "method", "wavefunction", "device complex array",
  "to_device(np.array(psi,complex))", "NONE",
  "internal: step:271; evolve:279",
  "indirect: backend tests",
  "PARTIALLY")
E("SplitOperatorSolver._download", "method", "psi", "WaveFunction",
  "wf_class(grid, to_host(psi))", "NONE",
  "internal: step:271; evolve:283,284",
  "indirect: backend tests",
  "PARTIALLY")
E("SplitOperatorSolver.step", "method", "wavefunction", "WaveFunction",
  "one full step (upload/advance/download)", "NONE",
  "runner.py:161; stationary/imaginary_time.py:126; examples/07:83,08:110,11:99; benchmarks/validation_suite.py:143; testbench_interlock.py:106",
  "tests/test_split_operator.py::test_order2_matches_legacy_solvers:26; test_norm_and_energy_conservation:50",
  "VERIFIED")
E("SplitOperatorSolver.evolve", "method", "wavefunction, n_steps, callback=None, callback_interval=1",
  "WaveFunction", "n_steps with callbacks; keeps psi on device", "NONE",
  "runner? no; stationary/imaginary_time.py:130,229; examples/09:37,12:72,13:142,217; benchmarks/validation_suite.py (many)",
  "tests/test_split_operator.py::test_free_particle_matches_analytic_gaussian_spreading:114; test_absorber_removes_outgoing_flux:124; test_backends.py::test_device_absorber_and_callbacks:109",
  "VERIFIED")

# =====================================================================
# quantumlab/solvers/split_step_1d.py
# =====================================================================
E("SplitStep1DSolver", "class", "grid, potential, dt, hbar=1, m=1", "object",
  "legacy 1D Strang SSFM", "NONE",
  "runner.py:115; examples/01:33,02:31,03:32,04:34; testbench_interlock.py:100",
  "tests/test_solvers.py::test_norm_conservation:9; test_energy_conservation:20",
  "VERIFIED - matches SplitOperatorSolver order 2 to 1e-12")
E("SplitStep1DSolver.__init__", "method", "see class", "sets V,T_k,U_V,U_T",
  "evaluates potential; builds propagators", "NONE",
  "all SplitStep1DSolver(...) sites", "tests/test_solvers.py::test_norm_conservation:9",
  "PARTIALLY")
E("SplitStep1DSolver.update_operators", "method", "none", "sets U_V,U_T",
  "exp(-i V dt/2hbar), exp(-i T_k dt/hbar)", "NONE",
  "internal: __init__:14",
  "indirect: test_solvers",
  "PARTIALLY")
E("SplitStep1DSolver.step", "method", "wavefunction:WaveFunction1D", "WaveFunction1D",
  "U_V FFT U_T IFFT U_V", "NONE",
  "runner.py:161; examples/01:39,02:40,03:40,04:40; tests",
  "tests/test_solvers.py::test_norm_conservation:9; test_energy_conservation:20",
  "VERIFIED")

# =====================================================================
# quantumlab/solvers/split_step_2d.py
# =====================================================================
E("SplitStep2DSolver", "class", "grid, potential, dt, hbar=1, m=1", "object",
  "legacy 2D Strang SSFM", "NONE",
  "runner.py:117; examples/05:41",
  "tests/test_2d_solver.py::test_2d_norm_conservation:11; test_2d_energy_conservation:23",
  "VERIFIED - matches SplitOperatorSolver order 2")
E("SplitStep2DSolver.__init__", "method", "see class", "sets V,T_k,U_V,U_T", "none", "NONE",
  "all SplitStep2DSolver(...) sites", "tests/test_2d_solver.py::test_2d_norm_conservation:11",
  "PARTIALLY")
E("SplitStep2DSolver.update_operators", "method", "none", "sets U_V,U_T",
  "exp(-i V dt/2hbar), exp(-i T_k dt/hbar)", "NONE",
  "internal: __init__:23", "indirect: test_2d_solver", "PARTIALLY")
E("SplitStep2DSolver.step", "method", "wavefunction:WaveFunction2D", "WaveFunction2D",
  "U_V FFT2 U_T IFFT2 U_V", "NONE",
  "runner.py:161; examples/05:54; tests",
  "tests/test_2d_solver.py::test_2d_norm_conservation:11; test_2d_energy_conservation:23",
  "VERIFIED")

# =====================================================================
# quantumlab/solvers/split_step_3d.py
# =====================================================================
E("SplitStep3DSolver", "class", "grid, potential, dt, hbar=1, m=1, workers=-1", "object",
  "legacy 3D Strang SSFM", "NONE",
  "runner.py:121; examples/06:42; benchmarks/perf_comparison.py:94",
  "tests/test_3d_solver.py::test_3d_norm_conservation:72; test_3d_energy_conservation_harmonic:86; test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73",
  "VERIFIED - CPU/GPU parity 1e-5; energy conservation")
E("SplitStep3DSolver.__init__", "method", "see class", "sets V,T_k,U_V,U_T", "none", "NONE",
  "all SplitStep3DSolver(...) sites", "tests/test_3d_solver.py::test_3d_norm_conservation:72",
  "PARTIALLY")
E("SplitStep3DSolver.update_operators", "method", "none", "sets U_V,U_T",
  "exp(-i V dt/2hbar), exp(-i T_k dt/hbar)", "NONE",
  "internal: __init__:47", "indirect: test_3d_solver", "PARTIALLY")
E("SplitStep3DSolver.step", "method", "wavefunction:WaveFunction3D", "WaveFunction3D",
  "U_V FFTN U_T IFFTN U_V", "NONE",
  "runner.py:161; examples/06:48; benchmarks; tests",
  "tests/test_3d_solver.py::test_3d_norm_conservation:72; test_3d_gpu_solver.py::test_3d_gpu_matches_cpu:73",
  "VERIFIED")

# =====================================================================
# quantumlab/solvers/split_step_3d_gpu.py
# =====================================================================
E("SplitStep3DGPU", "class",
  "grid, potential, dt, hbar=1,m=1,device_id=0,renormalize_interval=0",
  "object; cupy or cpu fallback",
  "GPU 3D SSFM with CPU fallback",
  "ENFORCED: device_id validated when CuPy present; invalid -> warn + CPU fallback",
  "runner.py:120; benchmarks/perf_comparison.py:117",
  "tests/test_3d_gpu_solver.py (all); test_benchmark_failure_handling.py (monkeypatched)",
  "VERIFIED - GPU benchmark relative_error 1.1e-14..1.8e-14 on RTX A1000; CPU/GPU parity test")
E("SplitStep3DGPU.__init__", "method", "see class", "sets V,T_k on device, operators",
  "evaluates potential; builds propagators", "ENFORCED device_id (conditional)",
  "all SplitStep3DGPU(...) sites", "tests/test_3d_gpu_solver.py::test_cpu_fallback_produces_valid_result:112",
  "PARTIALLY")
E("SplitStep3DGPU.update_operators", "method", "none", "sets U_V,U_T",
  "exp(-i V dt/2hbar), exp(-i T_k dt/hbar) on device", "NONE",
  "internal: __init__:76", "indirect: GPU tests",
  "PARTIALLY")
E("SplitStep3DGPU.step", "method", "wavefunction:WaveFunction3D", "WaveFunction3D",
  "one GPU step; optional renormalisation every interval", "NONE",
  "benchmarks/perf_comparison.py:97,104,122; tests",
  "tests/test_3d_gpu_solver.py::test_3d_gpu_norm_conservation:42; test_3d_gpu_matches_cpu:73",
  "VERIFIED")
E("SplitStep3DGPU.step_sequence", "method", "initial_wf:WaveFunction3D, steps:int",
  "WaveFunction3D", "in-VRAM multi-step", "NONE",
  "benchmarks/perf_comparison.py:123,128",
  "tests/test_3d_gpu_solver.py::test_step_sequence_matches_individual_steps:95",
  "VERIFIED - matches individual steps to 1e-12")
E("SplitStep3DGPU._step_gpu_internal", "method", "psi_gpu", "device array",
  "U_V FFT U_T IFFT U_V + optional renormalisation", "NONE",
  "internal: step:92; step_sequence:121",
  "indirect: GPU tests",
  "PARTIALLY")
E("SplitStep3DGPU.backend", "property", "none", "str 'cupy'|'scipy-cpu'",
  "gpu flag", "NONE",
  "tests/test_3d_gpu_solver.py:44,130,153",
  "tests/test_3d_gpu_solver.py::test_backend_property:151",
  "PARTIALLY")

# =====================================================================
# quantumlab/stationary/conjugate_gradient.py
# =====================================================================
E("ground_state_pcg", "function",
  "grid, potential, initial=None, nonlinearity=0, rotation=0, tol=1e-8, max_iter=10000, hbar=1,m=1, callback=None, callback_interval=100, workers=-1",
  "(WaveFunction, ConvergenceInfo)",
  "preconditioned nonlinear CG on the sphere; E=<psi|H|psi>-(g/2)int|psi|^4",
  "ENFORCED: ValueError if potential.time_dependent",
  "benchmarks/validation_suite.py:312,317; examples/11:169",
  "tests/test_conjugate_gradient.py (all)",
  "VERIFIED - hydrogen E0=-0.5 to 7.77e-16; GP virial 5.79e-10")

# =====================================================================
# quantumlab/stationary/eigensolver.py
# =====================================================================
E("eigenstates", "function",
  "grid, potential, n_states=6, hbar=1,m=1,tol=None,max_iter=1000,seed=0,method='auto',workers=-1",
  "(energies ndarray (n_states,), states list[WaveFunction])",
  "matrix-free H via FFT; LOBPCG (k-space preconditioned) or Lanczos (ARPACK)",
  "ENFORCED: ValueError for unknown method; LOBPCG non-convergence RuntimeWarning",
  "benchmarks/validation_suite.py:119,124,211; examples/10:41,12:94",
  "tests/test_stationary.py (all); test_strongfield.py::test_soft_coulomb_hydrogen_ground_state:33",
  "VERIFIED - exact harmonic spectra 7.28e-14/1.42e-13; hydrogen -0.5 to 1.94e-14")

# =====================================================================
# quantumlab/stationary/hamiltonian.py
# =====================================================================
E("apply_hamiltonian", "function",
  "psi:ndarray, grid, V:ndarray, hbar=1,m=1,nonlinearity=0,workers=-1,rotation=0",
  "ndarray grid.shape",
  "H psi = -hbar^2/2m nabla^2 psi + (V+g|psi|^2) psi - Omega L_z psi (spectral derivatives)",
  "NONE (V shape not validated)",
  "stationary/conjugate_gradient.py:63; imaginary_time.py:31,184",
  "tests/test_stationary.py::test_3d_isotropic_degeneracy:29; test_rotation.py::test_rotating_hamiltonian_has_vortex_eigenstate:126",
  "VERIFIED - vortex eigenstate H psi=(2-Omega)psi to 1e-12; residual checks")

# =====================================================================
# quantumlab/stationary/imaginary_time.py
# =====================================================================
E("ConvergenceInfo", "class", "converged,steps,energy,chemical_potential,residual",
  "dataclass", "container", "NONE",
  "constructed in ground_state:139; excited_states (via ground_state)",
  "indirect: test_stationary.py (all)",
  "PARTIALLY")
E("_inner", "function", "a,b,dV", "complex", "sum(conj(a)*b)*dV", "NONE",
  "internal: _energy_and_mu:32,35,36; ground_state:115,116; _coupled_energy_mu:185,187,189",
  "indirect: stationary tests",
  "PARTIALLY")
E("_energy_and_mu", "function", "psi,grid,V,hbar,m,g,dV,rotation=0",
  "(energy,mu,residual)",
  "E=<T>+<V>+(g/2)int|psi|^4; mu=<H_GP>; residual=||H_GP psi-mu psi||",
  "NONE",
  "internal: ground_state:132,138",
  "indirect: test_stationary.py::test_ground_state_error_is_second_order_in_dtau:63",
  "VERIFIED - dtau^2 residual ratio 3.99")
E("_default_guess", "function", "grid", "complex128 grid.shape",
  "exp(-r^2/(2 width^2)), width=min(ptp(coords))/8",
  "ENFORCED: none (min ptp could be 0 -> division by zero)",
  "stationary/conjugate_gradient.py:54; internal ground_state:109; excited_states:157",
  "indirect: stationary tests",
  "PARTIALLY")
E("ground_state", "function",
  "grid, potential, dtau=0.01, nonlinearity=0, initial=None, tol=1e-11, max_steps=50000, check_interval=20, hbar=1,m=1, orthogonal_to=None, workers=-1, rotation=0, backend='numpy'",
  "(WaveFunction, ConvergenceInfo)",
  "imaginary-time relaxation via SplitOperatorSolver(order=2,imaginary_time=True); optional Gram-Schmidt; dtau sequence continuation",
  "ENFORCED: orthogonal_to only for linear (ValueError); propagates solver validations",
  "benchmarks/validation_suite.py:129,172,181,182,290; examples/08:83,11:71,162",
  "tests/test_stationary.py (all); test_gross_pitaevskii.py (all); test_rotation.py (all); test_backends.py::test_ground_state_on_device_backend:136",
  "VERIFIED - exact 3D ground state 6.95e-10; GP virial; dtau^2")
E("excited_states", "function",
  "grid, potential, n_states, dtau=0.01, tol=1e-11, max_steps=50000, seed=0, hbar=1,m=1, workers=-1",
  "(energies ndarray, states list, infos list)",
  "imaginary time + Gram-Schmidt against converged states",
  "NONE",
  "examples/10:44",
  "tests/test_stationary.py::test_imaginary_time_excited_states_match_lanczos:54",
  "VERIFIED - matches Lanczos to 1e-8")
E("CoupledConvergenceInfo", "class",
  "converged,steps,energy,chemical_potentials,residuals", "dataclass", "container", "NONE",
  "constructed in coupled_ground_state:237",
  "indirect: test_multicomponent.py (all)",
  "PARTIALLY")
E("_coupled_energy_mu", "function", "psis,grid,Vs,g,hbar,m,rotation,dV",
  "(energy,mus,residuals)",
  "E=sum_i(<T>_i+<V_i>)+0.5 sum_ij g_ij int n_i n_j; per-component mu and residual",
  "NONE",
  "internal: coupled_ground_state:231,236",
  "indirect: coupled tests",
  "VERIFIED - Manakov/virial")
E("coupled_ground_state", "function",
  "grid, potentials, couplings, initial, dtau=0.005, tol=1e-11, max_steps=50000, check_interval=20, hbar=1,m=1, rotation=0, backend='numpy', workers=-1",
  "(states tuple, CoupledConvergenceInfo)",
  "imaginary-time coupled GPE at fixed populations",
  "NONE",
  "benchmarks/validation_suite.py:289,301; examples/13:73,198",
  "tests/test_multicomponent.py::test_manakov_point_total_density_equals_single_component:32; test_coupled_virial_theorem:107",
  "VERIFIED - Manakov point 1.76e-07; virial 2.27e-06")

# =====================================================================
# quantumlab/observables/coefficients.py
# =====================================================================
E("transmission_coefficient", "function", "wf, barrier_position=0.0", "float",
  "int_{x>=barrier_position} |psi|^2 dx", "ENFORCED: TypeError for unsupported wf type",
  "examples/01:48,04:49",
  "tests/test_3d_observables.py::test_3d_transmission_reflection_sum_to_norm:63",
  "PARTIALLY - T+R=norm and half-splitting only")
E("reflection_coefficient", "function", "wf, barrier_position=0.0", "float",
  "int_{x<barrier_position} |psi|^2 dx", "ENFORCED: TypeError for unsupported wf type",
  "examples/01:47,04:48",
  "tests/test_3d_observables.py::test_3d_transmission_reflection_sum_to_norm:63",
  "PARTIALLY")

# =====================================================================
# quantumlab/observables/current.py
# =====================================================================
E("gradient", "function", "psi:ndarray, grid", "tuple of arrays",
  "spectral gradient (ifftn(1j K psi_k)) per axis", "Propagates ndim TypeError",
  "strongfield.py:130; internal probability_current:23; angular_momentum_z_expectation:30",
  "indirect: test_new_potentials_and_observables.py::test_probability_current_of_moving_gaussian:84; test_strongfield.py::test_soft_coulomb_gradient_matches_finite_difference:40",
  "VERIFIED - current integrates to momentum; Lz exact")
E("probability_current", "function", "wf, hbar=1,m=1", "tuple of arrays",
  "j=(hbar/m) Im(psi* grad psi)", "NONE",
  "TEST-ONLY: tests/test_new_potentials_and_observables.py:87,95",
  "tests/test_new_potentials_and_observables.py::test_probability_current_of_moving_gaussian:84; test_probability_current_integrates_to_momentum_3d:91",
  "VERIFIED - j=2*rho for moving Gaussian; integrates to <p>")
E("angular_momentum_z_expectation", "function", "wf, hbar=1", "float",
  "<psi|-i hbar (x d_y - y d_x)|psi>",
  "ENFORCED: TypeError unless Grid2D/Grid3D",
  "benchmarks/validation_suite.py:114; examples/11:104,13:225",
  "tests/test_new_potentials_and_observables.py::test_vortex_angular_momentum:99; test_rotation.py (all)",
  "VERIFIED - <Lz>=1 to 2.22e-16; vortex lattice")
E("autocorrelation", "function", "psi0, psi_t, grid", "complex",
  "C(t)=<psi0|psi_t>=int conj(psi0) psi_t dV", "NONE",
  "benchmarks/validation_suite.py:142,203",
  "tests/test_new_potentials_and_observables.py::test_autocorrelation_spectrum_peaks_at_eigenenergies:107; test_rotation.py::test_vortex_is_stationary_with_rotating_frame_energy:48",
  "VERIFIED - Feit-Fleck peaks; vortex phase 1.15e-08")
E("vortex_positions", "function", "wf, min_density=0.2, smoothing=1.0",
  "(positions (n,2), charges (n,))",
  "phase winding per plaquette, 2pi q; density-masked",
  "ENFORCED: TypeError unless Grid2D",
  "examples/11:101,114,175,187; 13:222,223,229,230",
  "tests/test_new_potentials_and_observables.py::test_vortex_positions_finds_imprinted_vortices:127",
  "PARTIALLY - imprinted-vortex positions/charges; no independent analytic field")

# =====================================================================
# quantumlab/observables/expectation.py
# =====================================================================
E("position_expectation", "function", "wf", "float", "int x |psi|^2 dx",
  "ENFORCED: TypeError for unsupported wf type",
  "benchmarks/validation_suite.py:77,197; runner.py:171; examples; testbench_interlock.py:110",
  "tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_rotation.py::test_coherent_state_in_rotating_frame:19",
  "VERIFIED - Ehrenfest driven oscillator 5.60e-09; rotating frame 1.89e-08")
E("position_squared_expectation", "function", "wf", "float", "int x^2 |psi|^2 dx",
  "ENFORCED: TypeError for unsupported wf type",
  "internal: position_uncertainty:28",
  "indirect: test_observables.py::test_gaussian_observables_and_uncertainty:7",
  "VERIFIED - uncertainty product 4.6e-12")
E("position_uncertainty", "function", "wf", "float", "sqrt(max(<x^2>-<x>^2,0))",
  "ENFORCED: TypeError for unsupported wf type",
  "benchmarks/validation_suite.py:103; examples/01:44,05:65,08:61",
  "tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24",
  "VERIFIED - Heisenberg 4.6e-12")
E("y_expectation", "function", "wf", "float", "int Y |psi|^2 dV",
  "ENFORCED: ValueError unless 2D/3D",
  "benchmarks/validation_suite.py:198; examples/05:64",
  "tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24; test_rotation.py::test_coherent_state_in_rotating_frame:19",
  "VERIFIED - rotating frame 1.89e-08")
E("y_squared_expectation", "function", "wf", "float", "int Y^2 |psi|^2 dV",
  "ENFORCED: ValueError unless 2D/3D",
  "internal: y_uncertainty:52",
  "indirect: test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24",
  "VERIFIED")
E("y_uncertainty", "function", "wf", "float", "sqrt(max(<y^2>-<y>^2,0))",
  "ENFORCED: ValueError unless 2D/3D",
  "benchmarks/validation_suite.py:104; examples/05:66,08:61",
  "tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24",
  "VERIFIED")
E("z_expectation", "function", "wf", "float", "int Z |psi|^2 dV",
  "ENFORCED: ValueError unless 3D",
  "TEST-ONLY: tests/test_3d_observables.py:28,60; test_rotation.py:45",
  "tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24; test_3d_z_expectation_rejects_lower_dimensions:54; test_rotation.py::test_coherent_state_in_rotating_frame_3d:36",
  "PARTIALLY")
E("z_squared_expectation", "function", "wf", "float", "int Z^2 |psi|^2 dV",
  "ENFORCED: ValueError unless 3D",
  "internal: z_uncertainty:72",
  "indirect: test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24",
  "VERIFIED")
E("z_uncertainty", "function", "wf", "float", "sqrt(max(<z^2>-<z>^2,0))",
  "ENFORCED: ValueError unless 3D",
  "benchmarks/validation_suite.py:105; examples/08:61",
  "tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24",
  "VERIFIED")
E("momentum_expectation", "function", "wf, direction='x', hbar=1", "float",
  "int hbar k |phi|^2 dk (phi=fourier_transform)",
  "ENFORCED: ValueError for invalid direction per dimension; TypeError for unsupported wf",
  "testbench_interlock.py:111",
  "tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_momentum_expectation_and_heisenberg:34",
  "VERIFIED - Heisenberg 4.6e-12")
E("momentum_squared_expectation", "function", "wf, direction='x', hbar=1", "float",
  "int (hbar k)^2 |phi|^2 dk",
  "ENFORCED: ValueError/TypeError as above",
  "internal: kinetic_energy_expectation:156,159,160,163,164,165; momentum_uncertainty:136",
  "indirect: Heisenberg tests",
  "VERIFIED")
E("momentum_uncertainty", "function", "wf, direction='x', hbar=1", "float",
  "sqrt(max(<p^2>-<p>^2,0))",
  "ENFORCED: ValueError/TypeError as above",
  "benchmarks/validation_suite.py:103,104,105",
  "tests/test_observables.py::test_gaussian_observables_and_uncertainty:7; test_3d_observables.py::test_3d_momentum_expectation_and_heisenberg:34",
  "VERIFIED - Heisenberg 4.6e-12")
E("potential_energy_expectation", "function", "wf, potential", "float",
  "int V |psi|^2 dV (0 if potential None)",
  "ENFORCED: TypeError for unsupported wf type",
  "benchmarks/validation_suite.py:173,303,318; examples/08:85; observables/nonlinear.py:13,19,30",
  "tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54; test_multicomponent.py::test_coupled_virial_theorem:107",
  "VERIFIED - GP/coupled virial")
E("kinetic_energy_expectation", "function", "wf, hbar=1,m=1", "float",
  "sum_axis <p_axis^2>/(2m)",
  "ENFORCED: TypeError for unsupported wf type",
  "benchmarks/validation_suite.py:173,302,318; examples/08:84; observables/nonlinear.py:13,19,30",
  "tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54; test_multicomponent.py::test_coupled_virial_theorem:107",
  "VERIFIED - GP/coupled virial")
E("total_energy_expectation", "function", "wf, potential, hbar=1,m=1", "float",
  "<T>+<V>",
  "Propagates TypeError",
  "benchmarks/validation_suite.py:86,97; runner.py:170; examples/02:36,44,03:47; testbench_interlock.py:103,109",
  "tests/test_solvers.py::test_energy_conservation:20; test_2d_solver.py::test_2d_energy_conservation:23; test_split_operator.py::test_norm_and_energy_conservation:50",
  "VERIFIED - energy conservation 2.18e-10 (order 4, 500 steps)")

# =====================================================================
# quantumlab/observables/momentum.py
# =====================================================================
E("get_momentum_wavefunction", "function", "wf",
  "((k...), phi_shifted) fftshifted",
  "fftshift of fourier_transform and k axes",
  "ENFORCED: implicit (assumes WaveFunction type)",
  "internal: get_momentum_probability_density:24,27,30",
  "indirect: test_3d_observables.py::test_3d_momentum_probability_density:72",
  "PARTIALLY")
E("get_momentum_probability_density", "function", "wf",
  "((k...), |phi|^2) fftshifted",
  "|fftshift(phi)|^2",
  "ENFORCED: implicit",
  "visualization/plots_1d.py:52",
  "tests/test_3d_observables.py::test_3d_momentum_probability_density:72",
  "VERIFIED - Parseval norm equality 1e-10")

# =====================================================================
# quantumlab/observables/nonlinear.py
# =====================================================================
E("interaction_energy", "function", "wf, nonlinearity", "float",
  "(g/2) int |psi|^4 dV", "NONE",
  "benchmarks/validation_suite.py:173,318; examples/08:86",
  "tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54; test_conjugate_gradient.py::test_gp_ground_state_without_dtau_floor:27",
  "VERIFIED - GP virial 2.32e-06 / CG 5.79e-10")
E("gross_pitaevskii_energy", "function", "wf, potential, nonlinearity, hbar=1,m=1",
  "float", "<T>+<V>+(g/2)int|psi|^4", "Propagates TypeError",
  "examples/09:55,57",
  "tests/test_gross_pitaevskii.py::test_gp_energy_conserved_in_real_time:40; test_rotation.py::test_rotating_gp_ground_state_with_vortex_lattice_beats_vortex_free_state:98",
  "VERIFIED - energy conservation rel 1e-6")
E("chemical_potential", "function", "wf, potential, nonlinearity, hbar=1,m=1",
  "float", "<T>+<V>+g int|psi|^4", "Propagates TypeError",
  "TEST-ONLY: tests/test_gross_pitaevskii.py:69",
  "tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54",
  "PARTIALLY - cross-checked against ConvergenceInfo.chemical_potential")
E("coupled_gp_energy", "function", "states, potentials, couplings, hbar=1,m=1",
  "float", "sum_i(<T>_i+<V_i>)+0.5 sum_ij g_ij int n_i n_j", "Propagates TypeError",
  "TEST-ONLY: tests/test_multicomponent.py:100,102",
  "tests/test_multicomponent.py::test_energy_and_populations_conserved_in_real_time:95",
  "VERIFIED - conservation rel 1e-9")
E("miscibility_overlap", "function", "wf_a, wf_b", "float",
  "int n_a n_b / sqrt(int n_a^2 int n_b^2)", "NONE",
  "examples/13:76,200",
  "tests/test_multicomponent.py::test_miscibility_overlap:122",
  "PARTIALLY - identity/orthogonality limits only")

# =====================================================================
# quantumlab/strongfield.py
# =====================================================================
E("wavelength_to_omega", "function", "wavelength_nm:float", "float (a.u.)",
  "45.56335253/wavelength_nm", "NONE",
  "benchmarks/validation_suite.py:217; examples/12:59,87",
  "tests/test_strongfield.py::test_laser_unit_conversions:14",
  "VERIFIED - 800 nm -> 1.5498 eV (probe 0.05695419)")
E("intensity_to_field", "function", "intensity_w_cm2:float", "float (a.u.)",
  "sqrt(I/3.50944758e16)", "NONE",
  "benchmarks/validation_suite.py:219; examples/12:61,90,260",
  "tests/test_strongfield.py::test_laser_unit_conversions:14",
  "VERIFIED - probe 1e14 -> 0.05338025")
E("ponderomotive_energy", "function", "field, omega", "float (a.u.)",
  "E0^2/(4 omega^2)", "NONE",
  "examples/12:91,260",
  "tests/test_strongfield.py::test_laser_unit_conversions:14",
  "VERIFIED - probe 0.21960887")
E("classical_returns", "function", "n_phases=2000",
  "(birth_phase, return_phase, return_energy/U_p)",
  "three-step model; x=cos phi-cos phi0+(phi-phi0) sin phi0; brentq first crossing; E=2Up(sin phi_r-sin phi0)^2",
  "NONE",
  "benchmarks/validation_suite.py:214; examples/12:137",
  "tests/test_strongfield.py::test_classical_three_step_maximum:22",
  "VERIFIED - max 3.1731, birth 17 deg, return 252 deg; probe 3.1731359 at 17.97 deg")
E("classical_cutoff", "function", "ionisation_potential, field, omega", "float",
  "Ip + max(E_return)/Up * Up", "NONE",
  "TEST-ONLY: tests/test_strongfield.py:30",
  "tests/test_strongfield.py::test_classical_three_step_maximum:22",
  "PARTIALLY")
E("harmonic_spectrum", "function", "signal, dt, omega0, window=True",
  "(omega/omega0, |rfft|^2)",
  "Hann window then |FFT|^2 vs harmonic order", "NONE",
  "benchmarks/validation_suite.py:226; examples/12:77,106",
  "tests/test_strongfield.py::test_harmonic_spectrum_peaks_at_harmonic_orders:60",
  "VERIFIED - HHG odd-harmonic ratio 2.3e3")
E("gabor_transform", "function", "signal, dt, omega0, orders, width, times=None",
  "(times, orders, map[time,order])",
  "|int a(t') exp(-(t'-t)^2/2sigma^2) exp(-i omega t') dt'|^2",
  "NONE",
  "examples/12:136,170",
  "tests/test_strongfield.py::test_gabor_transform_locates_burst:72",
  "PARTIALLY - burst localization only")
E("attosecond_pulses", "function", "signal, dt, omega0, order_min, order_max",
  "float64 (len(signal),)",
  "|ifft(band-filtered spectrum)|^2 (analytic signal)", "NONE",
  "benchmarks/validation_suite.py:235; examples/12:188",
  "tests/test_strongfield.py::test_attosecond_pulses_from_harmonic_comb:83",
  "VERIFIED - half-cycle burst spacing 3.08e-03")
E("dipole_acceleration", "function", "wf, base_potential, force", "float",
  "a(t)=< -dV0/dx > + F(t) (Ehrenfest)",
  "ENFORCED: implicit (base_potential must have gradient or evaluate)",
  "benchmarks/validation_suite.py:224; examples/12:68",
  "tests/test_strongfield.py::test_dipole_acceleration_obeys_ehrenfest_in_harmonic_trap:96",
  "VERIFIED - a=-<x>+F to 1e-10; drives HHG spectrum")

# =====================================================================
# emit
# =====================================================================
by_qn = {d["qualname"]: d for d in defs}
missing = [d["qualname"] for d in defs if d["qualname"] not in {r["qn"] for r in R}]
extra = [r["qn"] for r in R if r["qn"] not in by_qn]
if missing or extra:
    raise SystemExit("annotation mismatch missing=%s extra=%s" % (missing, extra))

ANN = {r["qn"]: r for r in R}
srclines = {}
for _d in defs:
    if _d["module"] not in srclines:
        srclines[_d["module"]] = open(os.path.join(REPO, _d["module"]), encoding="utf-8").read().splitlines()
module_order = []
for d in defs:
    if d["module"] not in module_order:
        module_order.append(d["module"])

out = []
out.append("# QuantumLab Producer Inventory - CPD audit 2026-11-20")
out.append("")
out.append("- Repository: `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`")
out.append("- Branch `remediation/2026-11-20`, HEAD `44f30e30654c064b75f760833741ab55b392ff20` (clean tree).")
out.append("- Package: `quantumlab` 1.3.0 (split-step Fourier quantum wave-packet simulator).")
out.append("- Method: read-only `read_file`/`search_files` + an AST scan of every `*.py` in the repo (definitions, imports, call/attribute sites); cheap import/shape probes. No file in the repo was created, modified, moved or deleted; no git state-changing command was run; no packages installed; the full test suite was not run.")
out.append("")
out.append("## Scope and counting rule")
out.append("")
out.append("A **producer** is any class, function or method that creates scientifically meaningful information")
out.append("(numerical values, state, arrays or artifacts). Inventory granularity is **function-level**: every class")
out.append("and every function/method defined at module or class top level in the listed files is one producer, including")
out.append("`__init__`, properties and private helpers. Nested closures (e.g. `envelope` inside `sin2_envelope`) are")
out.append("not counted separately; they are named inside their enclosing row. Module-level constants (`YOSHIDA_W0`,")
out.append("`YOSHIDA_W1`, `HARTREE_EV`, `AU_TIME_FS`, `AU_INTENSITY_W_CM2`, `POTENTIAL_REGISTRY`, `_AXIS_INDEX`) and")
out.append("`__init__.py` re-export lists are not functions and are not counted.")
out.append("")
out.append("**Total producers: %d**" % len(defs))
out.append("")
out.append("Call-site notation: `path:line`. Tests are cited as `tests/file.py::test_name:line` (line = test function")
out.append("definition). 'NONE' means no such site exists anywhere in the repository.")
out.append("")
out.append("Independent-validation legend: **VERIFIED** = checked against an exact/analytic or independent numerical")
out.append("reference in `benchmarks/validation_suite.py` (report `benchmarks/validation_report.md`, 27/27 pass) or the GPU")
out.append("benchmark (`benchmarks/results_2026-11-20_cuda.json`); **PARTIALLY** = unit tests only, or indirect exercise")
out.append("through a caller; **NONE** = no test and no independent check.")
out.append("")
out.append("Evidence base for the probes (run on this host, Python 3.11.9 / numpy 2.4.3):")
out.append("`Grid1D(8,-4,4)` -> `dx=1.0`, `dk=0.7853981634`, `x/k` float64 `(8,)`; `Grid2D(4x6)` -> `X` `(4,6)` float64,")
out.append("`dk_x=1.5707963`, `dk_y=1.0471976`; `Grid3D(4^3)` -> `X` `(4,4,4)` float64; `WaveFunction*` `psi` complex128,")
out.append("`probability_density` float64; Gaussian norm `0.9999999999999999`; 1D Parseval `0.9999999999999997`;")
out.append("`AbsorbingBoundaryLayer` orders 1..6 all finite, min 0.0, max 1.0; `k_volume_element` computes but has no")
out.append("consumer; `classical_returns(2000)` max `3.1731359` at birth `17.97 deg`; `wavelength_to_omega(800)=0.05695419`;")
out.append("`intensity_to_field(1e14)=0.05338025`; `ponderomotive_energy=0.21960887`.")
out.append("")
out.append("---")
out.append("")
out.append("## Inventory")
out.append("")

idx = 0
for mod in module_order:
    out.append("### `%s`" % mod)
    out.append("")
    for d in defs:
        if d["module"] != mod:
            continue
        idx += 1
        a = ANN[d["qualname"]]
        kind = a["kind"]
        dec = [x.lstrip("@") for x in d.get("decorators", [])]
        extra = [x for x in dec if x != kind]
        if extra:
            kind += " (" + ", ".join(extra) + ")"
        sig = d["signature"]
        if d["kind"] == "class":
            sig = srclines[d["module"]][d["lineno"] - 1].strip()
        out.append("#### P%d. `%s` - %s" % (idx, d["qualname"], kind))
        out.append("")
        out.append("- **Definition:** `%s:%d`" % (d["module"], d["lineno"]))
        out.append("- **Signature (verbatim):** `%s`" % sig.replace("`", "'").replace("\n", "\\n"))
        out.append("- **Input domain:** %s" % a["inp"])
        out.append("- **Output domain:** %s" % a["out"])
        out.append("- **Mathematical definition:** %s" % a["math"])
        out.append("- **Preconditions / postconditions enforced:** %s" % a["pre"])
        out.append("- **Actual callers:** %s" % a["callers"])
        out.append("- **Test coverage:** %s" % a["tests"])
        out.append("- **Independent validation:** %s" % a["val"])
        out.append("")
    out.append("")

# ---- finish sections ----
from collections import OrderedDict
mod_counts = OrderedDict()
for d in defs:
    mod_counts[d["module"]] = mod_counts.get(d["module"], 0) + 1

no_caller = []
no_test = []
for d in defs:
    a = ANN[d["qualname"]]
    c = a["callers"].strip()
    t = a["tests"].strip()
    if c.startswith("NONE"):
        no_caller.append(d)
    if t.startswith("NONE"):
        no_test.append(d)

def qn_list(items):
    return sorted({d["module"] + "::" + d["qualname"] for d in items})

out.append("---")
out.append("")
out.append("## (a) Producer counts by module")
out.append("")
out.append("| Module | Producers |")
out.append("|---|---|")
for m, c in mod_counts.items():
    out.append("| `%s` | %d |" % (m, c))
out.append("| **Total** | **%d** |" % len(defs))
out.append("")
out.append("Grouped: core = %d; potentials = %d; solvers = %d; stationary = %d; observables = %d; strongfield = %d."
          % (sum(c for m, c in mod_counts.items() if "/core/" in m),
             sum(c for m, c in mod_counts.items() if "/potentials/" in m),
             sum(c for m, c in mod_counts.items() if "/solvers/" in m),
             sum(c for m, c in mod_counts.items() if "/stationary/" in m),
             sum(c for m, c in mod_counts.items() if "/observables/" in m),
             mod_counts.get("quantumlab/strongfield.py", 0)))
out.append("")
out.append("## (b) Producers with NO caller anywhere (unconsumed)")
out.append("")
out.append("These have no call/instantiation site in the repository. Abstract base classes are listed separately at the")
out.append("end because they are consumed through subclassing, not called.")
out.append("")
for d in no_caller:
    a = ANN[d["qualname"]]
    out.append("- `%s::%s` - %s" % (d["module"], d["qualname"], a["callers"]))
out.append("")
out.append("Abstract bases with no direct caller (consumed via `class X(Base)`): `quantumlab.potentials.base.Potential`,")
out.append("`quantumlab.potentials.time_dependent.TimeDependentPotential`, `quantumlab.solvers.base.Solver`.")
out.append("")
out.append("## (c) Producers with NO test coverage")
out.append("")
out.append("No direct test and no indirect exercise through a tested caller.")
out.append("")
for d in no_test:
    out.append("- `%s::%s`" % (d["module"], d["qualname"]))
out.append("")
out.append("## (d) Five producers whose mathematical contract is most safety-critical")
out.append("")
out.append("1. **`quantumlab.solvers.split_operator.SplitOperatorSolver._kinetic_step` (+ `_strang`/`_advance`)** - the")
out.append("   core propagator. A wrong kinetic phase or splitting weight breaks unitarity and every dynamics result; it")
out.append("   is the single most reused numerical contract in the package. Independent evidence: convergence orders")
out.append("   2.001/3.997, exact free-Gaussian spreading 1.37e-15, exact soliton 1.46e-09, 3D norm 2.55e-15, energy 2.18e-10.")
out.append("2. **`quantumlab.core.wavefunction.WaveFunction1D/2D/3D.fourier_transform`** - fixes the momentum-space measure")
out.append("   (`dx^d/(2 pi)^{d/2}`). An error propagates into `momentum_expectation`, `kinetic_energy_expectation` and")
out.append("   `total_energy_expectation`, i.e. into every reported energy. Independent evidence: Parseval probe")
out.append("   0.9999999999999997 and the 3D Parseval test; Heisenberg product 4.6e-12.")
out.append("3. **`quantumlab.stationary.eigensolver.eigenstates`** - produces the energies and eigenstates used as physical")
out.append("   predictions (e.g. the hydrogen ionisation potential). Independent evidence: exact harmonic spectra to")
out.append("   7.28e-14 (Lanczos) / 1.42e-13 (LOBPCG), soft-core hydrogen -0.5 to 1.94e-14, Lanczos/LOBPCG agreement 1e-9.")
out.append("4. **`quantumlab.core.absorbing_boundary.AbsorbingBoundaryLayer._polynomial_profile` (+ `apply`)** - the mask")
out.append("   is applied every step; a bad profile silently deletes the state or injects NaN (the documented defect")
out.append("   D-P2-2 fixed at HEAD). Independent evidence: finiteness/monotonicity/edge tests and the HHG flux-absorption")
out.append("   check; probe confirms finite [0,1] masks for orders 1..6.")
out.append("5. **`quantumlab.potentials.coulomb.SoftCoulomb.evaluate` (+ `gradient`)** - the strong-field model potential;")
out.append("   its analytic gradient enters `dipole_acceleration` and therefore the HHG/attosecond spectra. Independent")
out.append("   evidence: hydrogen ground state -0.5 to 1.94e-14, gradient vs central finite differences atol 1e-3, HHG")
out.append("   odd-harmonic ratio 2.3e3.")
out.append("")
out.append("Runners-up: `SplitOperatorSolver._potential_half_step` (nonlinear/imaginary-time midpoint),")
out.append("`CoupledGPESolver._potential_half_step` (coupled densities), `observables.current.probability_current`")
out.append("(continuity equation), `strongfield.harmonic_spectrum` (HHG readout).")
out.append("")

path = os.path.join(AUD, "cpd_producer_inventory.md")
open(path, "w", encoding="utf-8").write("\n".join(out))
json.dump(dict(total=len(defs),
               no_caller=qn_list(no_caller),
               no_test=qn_list(no_test)),
          open(os.path.join(AUD, "_lists.json"), "w", encoding="utf-8"), indent=1)
print("wrote", path, "rows", len(defs), "no_caller", len(no_caller), "no_test", len(no_test))
