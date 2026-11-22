import io
p = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20/_gen.py"
s = open(p, encoding="utf-8").read()
pairs = [
    # registry-only -> NONE
    ('"registry potentials/__init__.py:25 only (no call site)"',
     '"NONE (registry-only: potentials/__init__.py:25)"'),
    ('"registry potentials/__init__.py:27 only (no call site)"',
     '"NONE (registry-only: potentials/__init__.py:27)"'),
    ('"registry potentials/__init__.py:28 only (no call site)"',
     '"NONE (registry-only: potentials/__init__.py:28)"'),
    ('"registry potentials/__init__.py:33 only; imported unused at tests/test_potentials.py:8"',
     '"NONE (registry-only: potentials/__init__.py:33; imported unused at tests/test_potentials.py:8)"'),
    ('"registry potentials/__init__.py:32 only; imported unused at tests/test_potentials.py:7"',
     '"NONE (registry-only: potentials/__init__.py:32; imported unused at tests/test_potentials.py:7)"'),
    # generic-dispatch-only evaluate methods -> NONE
    ('"solvers (dynamic, generic .evaluate only)", "NONE", "NONE")',
     '"NONE (no call site; only generic Potential.evaluate dispatch could reach it)", "NONE", "NONE")'),
    ('"solvers (dynamic, generic .evaluate only)",\n  "NONE", "NONE")',
     '"NONE (no call site; only generic Potential.evaluate dispatch could reach it)",\n  "NONE", "NONE")'),
    # test-only -> TEST-ONLY
    ('"NONE (no production caller); tests/test_3d_solver.py:63"',
     '"TEST-ONLY: tests/test_3d_solver.py:63"'),
    ('"NONE (no production caller); tests/test_3d_solver.py:64"',
     '"TEST-ONLY: tests/test_3d_solver.py:64"'),
    ('"NONE (no production caller); tests/test_3d_solver.py:65"',
     '"TEST-ONLY: tests/test_3d_solver.py:65"'),
    ('"NONE (no production caller); tests",\n  "tests/test_new_potentials_and_observables.py::test_probability_current_of_moving_gaussian:84',
     '"TEST-ONLY: tests/test_new_potentials_and_observables.py:87,95",\n  "tests/test_new_potentials_and_observables.py::test_probability_current_of_moving_gaussian:84'),
    ('"NONE (no production caller); tests",\n  "tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24',
     '"TEST-ONLY: tests/test_3d_observables.py:28,60; test_rotation.py:45",\n  "tests/test_3d_observables.py::test_3d_position_expectation_and_uncertainty:24'),
    ('"NONE (no production caller); tests",\n  "tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54',
     '"TEST-ONLY: tests/test_gross_pitaevskii.py:69",\n  "tests/test_gross_pitaevskii.py::test_virial_theorem_for_gp_ground_state:54'),
    ('"NONE (no production caller); tests",\n  "tests/test_multicomponent.py::test_energy_and_populations_conserved_in_real_time:95',
     '"TEST-ONLY: tests/test_multicomponent.py:100,102",\n  "tests/test_multicomponent.py::test_energy_and_populations_conserved_in_real_time:95'),
    ('"NONE (no production caller); tests",\n  "tests/test_strongfield.py::test_classical_three_step_maximum:22',
     '"TEST-ONLY: tests/test_strongfield.py:30",\n  "tests/test_strongfield.py::test_classical_three_step_maximum:22'),
]
n = 0
for a, b in pairs:
    if a in s:
        s = s.replace(a, b, 1)
        n += 1
    else:
        print("NOT FOUND:", a[:70])
open(p, "w", encoding="utf-8").write(s)
print("replaced", n, "of", len(pairs))
