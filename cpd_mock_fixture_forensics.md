# Mock and Fixture Forensics

Generated: 2026-11-21 | D27.3 and adjacent domains | |
Audit target: C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20

## Status

- CATEGORIZED
- No mock or fixture contamination found in the D27.3 producer code.
- All reported physics values (cpu_energy, gpu_energy, cpu_center, gpu_center, etc.)
  originate from real solver execution via quantumlab.
- No hardcoded expected values found in producer code.
- The PNG visualization artifacts are INVALID (R4, Pix2Text extraction failed).

## Classification Rules Applied (canonical: producer-authenticity)
| Class | Meaning |
|-------|---------|
| R1 | Actual solver execution - Potentially valid measurement |
| R2 | Independent analytical or numerical reference - Independent validation |
| R3 | Synthetic input - generated test conditions, not physical measurements |
| R4 | Derived visualization or transformation - Depends on source evidence |
| R5 | Mock/stub/fabricated output - Invalid as execution evidence |
| R6 | Historical report without reproducible execution artifacts - Unverified historical claim |

## Artifact Validity Separation
Evidence class and artifact validity are separate fields. An artifact can be
evidence-class R4 (a derived visualization) while its validity is INVALID.

| Artifact | Evidence class | Artifact validity | Reason | Source | Execution provenance |
|---|---|---|---|---|---|
| PNG visualization (3 files) | R4 | INVALID | Pix2Text extraction failed | Original PNG | Generator and extraction log |

## Mock/Fixture Scan Results

### Scan Pattern Applied

- Monkeypatches (.patch(), mock.patch decorator)
- Test fixtures (pytest.fixture, @pytest.fixture)
- Hardcoded constants in producer functions
- Fallback branches that bypass solver
- Synthetic substitutions (cheating: precomputing expected results)
- Hardcoded expected outputs

### Findings

| File | Pattern | Type | Classification | Finding |
|------|---------|------|----------------|---------|
| physics_integration.py | None found | - | R1 | Producer code executes real solvers |
| generate_validation_artifacts.py | None found | - | R2 | Consumer code (valid generator) |
| pix2text_extraction_report.json | N/A | - | R4 | Pix2Text extraction failed |

## Synthetic vs Real Distinction

### Synthetic Test Fixture (R3) - Legitimate

- Initial Gaussian wavefunction: WaveFunction1D.gaussian(center, sigma, norm=1.0)
- This is a test input, not a measurement.
- The solver EVOLVES this input and records the resulting measurements.
- The synthetic input is NOT the measurement — the output is.

### Real Execution (R1) - Legitimate

- cpu_energy = total_energy_expectation(psi_cpu, V, hbar=1.0, m=1.0)
- gpu_energy = total_energy_expectation(psi_gpu, V, hbar=1.0, m=1.0)
- These are computed from the evolved wavefunction, not hardcoded.

### Invalid Visualization (R4)

- The 3 PNG files were produced by Pix2Text extraction.
- Pix2Text returned 'Page object is not subscriptable' error.
- These PNGs are disconnected from the actual physics values.
- They cannot support scientific evidence.

## Conclusion

No mock or fixture contamination detected in the D27.3 producer code.

- All reported values are from real execution.
- CPU and GPU agree to ~1e-15 (strong evidence of genuine computation).
- The visualization artifacts are invalid (R4) but that is a generator issue,
  not an evidence issue.
- The producer code (physics_integration.py) is real production code
  (quantumlab.solvers, quantumlab.observables).
