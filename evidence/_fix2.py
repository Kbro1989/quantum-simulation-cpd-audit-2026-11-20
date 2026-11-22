import io
p = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20/_gen.py"
s = open(p, encoding="utf-8").read()

def rep(old, new, count=-1):
    global s
    n = s.count(old)
    if n == 0:
        print("NOT FOUND:", old[:80])
    else:
        s = s.replace(old, new) if count < 0 else s.replace(old, new, count)
    print("replaced", n, ":", old[:50])

# 1D norm
rep('"runner.py; examples; benchmarks/validation_suite.py:95; visualization/volume_3d.py:50,106; stationary/eigensolver.py:88; testbench_interlock.py:102,108"',
    '"runner.py; examples; benchmarks/validation_suite.py:95; testbench_interlock.py:102,108"')
# 2D/3D norm (2 occurrences)
rep('"benchmarks/perf_comparison.py:134,135; benchmarks/validation_suite.py:95; examples/01_gaussian_barrier.py:42; examples/04_multiple_barriers.py:43; examples/05_2d_gaussian_barrier.py:62; examples/06_3d_gaussian_barrier.py:52; examples/07_3d_double_slit.py:93; examples/08_3d_bec_time_of_flight.py:119; examples/09_soliton_collision.py:61; examples/12_high_harmonic_generation.py:102; examples/13_two_component_bec.py:119,165,166; quantumlab/stationary/eigensolver.py:88; quantumlab/visualization/volume_3d.py:106,50; testbench_interlock.py:102,108"',
    '"benchmarks/validation_suite.py:95; examples/01_gaussian_barrier.py:42; examples/04_multiple_barriers.py:43; examples/05_2d_gaussian_barrier.py:62; examples/06_3d_gaussian_barrier.py:52; examples/07_3d_double_slit.py:93; examples/08_3d_bec_time_of_flight.py:119; examples/09_soliton_collision.py:61; examples/12_high_harmonic_generation.py:102; examples/13_two_component_bec.py:119,165,166; testbench_interlock.py:102,108"')
# copy 1D
rep('"runner.py:156,166; solvers/split_step_1d.py:21; benchmarks/perf_comparison.py:101,123,128; examples/07:88,90; config.py:9"',
    '"runner.py:156,166; benchmarks/perf_comparison.py:101,123,128; tests/test_3d_gpu_solver.py:82,83"')
rep('"runner.py:156,166; solvers/split_step_2d.py:32; benchmarks/perf_comparison.py"',
    '"runner.py:156,166; benchmarks/perf_comparison.py"')
rep('"runner.py:156,166; solvers/split_step_3d.py:56; split_step_3d_gpu.py:95; benchmarks/perf_comparison.py"',
    '"runner.py:156,166; benchmarks/perf_comparison.py"')
# probability_density line
rep('observables/nonlinear.py:8; strongfield.py:127;', 'observables/nonlinear.py:8; strongfield.py:132;')
# SoftCoulomb.gradient
rep('"strongfield.py:127; observables/current.py:23,30 (via hasattr); tests/test_strongfield.py:45"',
    '"strongfield.py:127; tests/test_strongfield.py:45"')
# observables.gradient
rep('"strongfield.py:127,130; internal probability_current:23; angular_momentum_z_expectation:30"',
    '"strongfield.py:130; internal probability_current:23; angular_momentum_z_expectation:30"')
# ABL apply
rep('"runner.py:163; examples/05:55,06:49; solvers/split_operator.py:260 (via _mask_dev)"',
    '"runner.py:163; examples/05:55,06:49"')
# ndim
rep('"solvers/split_operator.py:115,173; stationary/imaginary_time.py:90; potentials? no"',
    '"solvers/split_operator.py:115,173"')
# Solver.step
rep('"called dynamically: runner.py:161; examples; benchmarks; stationary/imaginary_time.py:126; tests"',
    '"called dynamically: runner.py:161; stationary/imaginary_time.py:126; examples/01:39,02:40,03:40,04:40,05:54,06:48,07:83,08:110,11:99; benchmarks/validation_suite.py:143; benchmarks/perf_comparison.py:97,104,122; testbench_interlock.py:106"')
# SplitOperatorSolver.t
rep('"runner.py:172; examples; tests/test_split_operator.py:60,99; test_rotation.py:30,42"',
    '"benchmarks/validation_suite.py:75,164,196,205,265,276; examples/07:81,85,88,90,93; 08:112,113,117,126; 09:39; 11:102,107,110,127; tests/test_split_operator.py:60,99; test_rotation.py:30,42"')
# SplitOperatorSolver.step
rep('"runner.py:161; stationary/imaginary_time.py:126; examples; benchmarks; tests"',
    '"runner.py:161; stationary/imaginary_time.py:126; examples/07:83,08:110,11:99; benchmarks/validation_suite.py:143; testbench_interlock.py:106"')
# SplitStep1D.step
rep('"runner.py:161; examples; tests"', '"runner.py:161; examples/01:39,02:40,03:40,04:40; tests"')
# SplitStep3DGPU.step
rep('"runner? no; benchmarks/perf_comparison.py:104,122; examples; tests"',
    '"benchmarks/perf_comparison.py:97,104,122; tests"')
open(p, "w", encoding="utf-8").write(s)
print("done")
