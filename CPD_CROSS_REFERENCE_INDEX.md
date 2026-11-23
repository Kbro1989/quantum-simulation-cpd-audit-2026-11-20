# CPD Cross-Reference Index

**Created:** 2026-11-23
**Purpose:** connect the repository's documents without duplicating their content, so a
reader can navigate the evidence graph and tell which vortex report is current.

This index is a map, not an evidence source. Every row points at a file that exists on
disk; the *content* claims live in the referenced documents.

Fields: Document ID · Relative path · Evidence population · Parent refs · Supporting ·
Version/commit · Class (R1-R6 / NOT_APPLICABLE) · Type · Supersedes · Superseded by.

### Evidence class hierarchy (producer-authenticity legend, canonical)
- **R1** — Actual solver execution - Potentially valid measurement
- **R2** — Independent analytical or numerical reference - Independent validation
- **R3** — Synthetic input - generated test conditions, not physical measurements
- **R4** — Derived visualization or transformation - Depends on source evidence
- **R5** — Mock/stub/fabricated output - Invalid as execution evidence
- **R6** — Historical report without reproducible execution artifacts - Unverified historical claim
- **NOT_APPLICABLE** — Administrative, specification, bibliographic, provenance, inventory,
  or planning artifacts for which R1-R6 do not apply. Such documents are not assigned an R
  class; the individual evidence *inside* a report is classified separately.

Field notes: a map documents what a file is, not whether it is correct. The same evidence must
not change scientific meaning depending on which document a reader opens.

---

## A. Repository identity and governing rules

|| Document ID | Path | Population | Parent refs | Supporting | Version/commit | Class (R1-R6/NOT_APPLICABLE) | Type | Supersedes | Superseded by |
||---|---|---|---|---|---|---|---|---|---|
|| REPO-README | `README.md` | production_audit | — | all | `dcbdf21` | NOT_APPLICABLE | DOCUMENTATION | — | — |
|| REPO-CUSTOM-INSTR | `CUSTOM-INSTRUCTIONS.md` | production_audit | — | — | reconstructed | NOT_APPLICABLE | SPECIFICATION | RECONSTRUCTED-PROVISIONAL | — |
|| REPO-FINAL-AUDIT | `cpd_final_audit.md` | production_audit | REPO-CUSTOM-INSTR | `cpd_certification_manifest.json` | `44f30e3` / baseline `7cb98a7` | NOT_APPLICABLE | Mixed evidence; classify individual claims | — | later addenda in README §3 |

## B. Code architecture and reachability

|| Document ID | Path | Population | Parent refs | Supporting | Version/commit | Class (R1-R6/NOT_APPLICABLE) | Type | Supersedes | Superseded by |
||---|---|---|---|---|---|---|---|---|---|
|| INV-PRODUCER | `cpd_producer_inventory.md` | production_audit | REPO-FINAL-AUDIT | `cpd_relationship_graph.json` | `44f30e3` | R2 | STATIC_ANALYSIS | — | — |
|| INV-CONSUMER | `cpd_consumer_inventory.md` | production_audit | INV-PRODUCER | `cpd_relationship_graph.json` | `44f30e3` | R2 | STATIC_ANALYSIS | — | — |
|| INV-DETACHED | `cpd_detached_inventory.md` | production_audit | INV-PRODUCER | — | `44f30e3` | R2 | STATIC_ANALYSIS | — | — |
|| SOLVER-API | `cpd_solver_api_contract.md` | production_audit | INV-PRODUCER | — | `remediation/2026-11-20` | NOT_APPLICABLE | SPECIFICATION | — | — |
|| SOLVER-USAGE | `cpd_solver_usage_audit.md` | production_audit | SOLVER-API | — | `44f30e3` | R1 | Mixed source analysis and execution evidence | — | — |
|| SOLVER-LIFECYCLE | `cpd_solver_lifecycle_audit.md` | production_audit | SOLVER-USAGE | — | `44f30e3` | R1 | Mixed source analysis and execution evidence | — | — |
|| SOLVER-FIX-EVID | `cpd_solver_fix_evidence.md` | production_audit | SOLVER-LIFECYCLE | — | `44f30e3` | R1 | Separate patch evidence from execution evidence | — | — |
|| RELATIONSHIP-GRAPH | `cpd_relationship_graph.json` | production_audit | INV-PRODUCER | `evidence/build_relationship_graph.py` | `44f30e3` | R4 | Derived graph | — | — |

## C. Mathematical and physical verification

|| Document ID | Path | Population | Parent refs | Supporting | Version/commit | Class (R1-R6/NOT_APPLICABLE) | Type | Supersedes | Superseded by |
||---|---|---|---|---|---|---|---|---|---|
|| MATH-VALIDATION | `cpd_mathematical_validation_report.md` | quantum_physics | REPO-FINAL-AUDIT | — | `44f30e3` | R1 | R1 measurements plus R2 references | — | — |
|| PHYSICS-MATRIX | `cpd_physics_validation_matrix.md` | quantum_physics | MATH-VALIDATION | — | `44f30e3` | R2 | Evidence register containing mixed classes | — | — |
|| BACKEND-INDEP | `cpd_backend_independence_audit.md` | quantum_physics | PHYSICS-MATRIX | — | `44f30e3` | R2 | R1 measurements unless an independent reference is used | — | — |
|| IND-PHYSICS | `cpd_independent_physics_validation.md` | quantum_physics | PHYSICS-MATRIX | — | — | NOT_APPLICABLE | Scaffold, not a result | — | — |
|| TRACE-27PLUS | `cpd_traceability_27plus.json` | quantum_physics | DOMAIN-VAR-MATRIX | — | `44f30e3` | R2 | Traceability register | — | — |
|| DOMAIN-VERDICTS | `cpd_domain_verdict_register.json` | quantum_physics | PHYSICS-MATRIX | — | `44f30e3` | R2 | Verdict register | — | — |
|| GPE-BENCH-SPEC | `literature_gpe_benchmarks/BENCHMARK_SPEC.md` | quantum_physics | SOLVER-API | `literature_gpe_benchmarks/b1_results_2026-11-22.json` | live | NOT_APPLICABLE | SPECIFICATION; generated test inputs are R3 | — | — |
|| GPE-BENCH-B1 | `literature_gpe_benchmarks/b1_results_2026-11-22.json` | quantum_physics | GPE-BENCH-SPEC | `B1_tf_profile/benchmark_01_tf_profile.py` | live | R1 | Measured benchmark | — | — |

## D. Evidence integrity

|| Document ID | Path | Population | Parent refs | Supporting | Version/commit | Class (R1-R6/NOT_APPLICABLE) | Type | Supersedes | Superseded by |
||---|---|---|---|---|---|---|---|---|---|
|| MOCK-FORENSICS | `cpd_mock_fixture_forensics.md` | production_audit | REPO-FINAL-AUDIT | `cpd_mock_and_fixture_register.json` | `44f30e3` | R2 | AUDIT_REPORT | — | — |
|| PRODUCER-AUTH | `cpd_producer_authenticity_audit.md` | production_audit | INV-PRODUCER | — | `44f30e3` | R2 | AUDIT_REPORT | — | — |
|| MANIFEST-V7 | `cpd_certification_manifest_v7.json` | production_audit | REPO-README | — | `8598439` (tree) / `c708ff8` (recon target) | NOT_APPLICABLE | PROVENANCE / INVENTORY | v1-v6 | — |
|| DEFECT-REGISTER | `cpd_defect_register.json` | production_audit | REPO-FINAL-AUDIT | — | `44f30e3` | R4 | Derived register, with linked underlying evidence | — | — |
|| REMEDIATION-PLAN | `cpd_remediation_plan.md` | production_audit | DEFECT-REGISTER | — | `44f30e3` | R4 | PLANNING_ARTIFACT | — | — |

## E. Historical PKS / Schauberger research branch

|| Document ID | Path | Population | Parent refs | Supporting | Version/commit | Class (R1-R6/NOT_APPLICABLE) | Type | Supersedes | Superseded by |
||---|---|---|---|---|---|---|---|---|---|
|| PKS-RECON | `pks_research_index/pks_reconstruction_report.md` | historical_pks | — | — | 2026-11-22 | R4 | Historical reconstruction from primary sources | — | — |
|| PKS-PRINTED-MATH | `pks_research_index/pks_printed_math_recovery_2026-11-22.md` | historical_pks | PKS-RECON | `pks_eikurve_pages/` | 2026-11-22 | R1/R2 | Separate source transcription from independent derivation | — | — |
|| PKS-EQ-AUDIT | `pks_research_index/pks_equation_audit.json` | historical_pks | PKS-PRINTED-MATH | `pks_equation_inventory.json` | 2026-11-22 | R2 | Equation audit reference | — | — |
|| PKS-GEOMETRY | `pks_research_index/pks_geometry_inventory.json` | historical_pks | PKS-EQ-AUDIT | — | 2026-11-22 | R2 | Geometry inventory | — | — |
|| SCHAUBERGER-ATLAS | `cpd_schauberger_research_atlas_2026-11-22.md` | historical_pks | PKS-GEOMETRY | `schauberger_sources_2026-11-22/` | 2026-11-22 | R6 | RESEARCH_SYNTHESIS / SEED | — | — |
|| VORTEX-PROVENANCE | `cpd_vortex_provenance_2026-11-22.md` | historical_pks | SCHAUBERGER-ATLAS | — | 2026-11-22 | R2 | TERMINOLOGY_PROVENANCE | — | — |
|| PKS-CITATION | `pks_research_index/pks_citation_index.json` | historical_pks | PKS-RECON | `pks_citation_index.md` | 2026-11-22 | NOT_APPLICABLE | BIBLIOGRAPHIC_METADATA | — | — |
|| RASIDI-LINEAGE | `cpd_rasidi_kingwen_lineage_2026-11-22.md` | historical_pks | REPO-README | — | 2026-11-22 | NOT_APPLICABLE | GIT_PROVENANCE | — | — |
|| PKS-RETRIEVED | `pks_research_index/pks_retrieved_references_2026-11-22.json` | historical_pks | PKS-CITATION | 4 PDFs in `schauberger_sources_2026-11-22/` | 2026-11-22 | R3 | HISTORICAL_PRIMARY_SOURCE | — | — |

## F. Vortex detector generations (which is current)

| Document ID | Path | Population | Class (R1-R6/NOT_APPLICABLE) | Type | Superseded by |
|---|---|---|---|---|---|
|| VORTEX-DETECT-V2 | `pks_research_index/quantum_vortex_detector_v2.json` | quantum_physics | NOT_APPLICABLE | superseded detector | DETECT-V3 |
|| VORTEX-DETECT-V3 | `pks_research_index/pks_vortex_detector_v3_2026-11-22.md` | quantum_physics | NOT_APPLICABLE | CURRENT detector (D1 FAIL_INITIAL_CONDITION, D2 PASS_WITH_CAVEAT, D3 INITIAL_CONDITION_ONLY, D4 PASS_WITH_CAVEAT) | — |
|| VORTEX-REGULARIZED | `pks_research_index/pks_vortex_regularized_2026-11-22.md` | quantum_physics | NOT_APPLICABLE | CURRENT regularized state (D1 PASS, D2 PASS, D3 uncertified late, D4 independent 0.99-1.02) | — |
|| VORTEX-D3-REV1 | `pks_research_index/quantum_vortex_d3_remediation.json` | quantum_physics | NOT_APPLICABLE | superseded (clamped out-of-domain samples) | REV2 |
|| VORTEX-D3-REV2 | `pks_research_index/quantum_vortex_d3_remediation_v2.json` | quantum_physics | NOT_APPLICABLE | superseded (geometry corrected, still NOT VALIDATED) | REV3 |
|| VORTEX-D3-REV3 | `pks_research_index/quantum_vortex_d3_remediation_v3.json` | quantum_physics | NOT_APPLICABLE | superseded (root cause: domain_exit) | REV4 |
|| VORTEX-D3-REV4 | `pks_research_index/quantum_vortex_d3_remediation_v4.json` | quantum_physics | NOT_APPLICABLE | CURRENT D3 estimator (circle fit; C1/C2/C3 PASS, C5/C6 FAIL; coverage-gated) | — |
|| VORTEX-GATE1 | `pks_research_index/quantum_vortex_gate1_d3.json` | quantum_physics | NOT_APPLICABLE | Gate 1 FAILS acceptance (detector bias) | — |
|| VORTEX-GATE-DERIV | `pks_research_index/quantum_vortex_gate_derivation.json` | quantum_physics | NOT_APPLICABLE | CURRENT diagnostic gate (coverage ≥ 0.90, gap ≤ 40°, SE ≤ 0.25; 0 ungated) | — |
|| VORTEX-DOMAIN-EXP | `pks_research_index/quantum_vortex_domain_experiment.json` | quantum_physics | R1 | L=8 recovers coverage | — |

## G. Solver API to literature cross-reference

Connects `cpd_solver_api_contract.md` (and the solver modules it names) to the retrieved
GPE literature. Validation questions only - this table does not certify the implementation.

| QuantumLab component | Literature | Validation question | Benchmark |
|---|---|---|---|
|| `Grid3D` | Dalfovo et al. 1999 | spatial discretization / resolution | — |
|| `WaveFunction3D` | Fetter & Svidzinsky 2001 | complex order parameter, vortex structure | B1 |
|| `SplitOperatorSolver` | Castin & Dum 1999 | time evolution, analytical benchmarks | B2 (specified) |
|| nonlinear GPE potential | Gross / Pitaevskii | correct `g|ψ|²` interaction | B1 |
|| imaginary-time propagation | Dalfovo; Fetter | ground-state convergence | B1 - measured |
|| rotating-frame solver | Castin & Dum; Fetter | angular momentum, vortex stability | B3 (specified) |
|| vortex detection | Fetter; Tang et al. | phase topology, core tracking | detector v3 (D1-D4) |
|| 3D turbulence diagnostics | Bradley et al. | energy spectra, vortex correlations | — |

Tang and Galantucci/Yui remain **separate two-fluid / filament-model references** - they can
motivate comparative experiments but do **not** certify the single-component GPE.

## H. Open gates (from README §3.4, unchanged)

- Gate 27 assets need re-evaluation.
- EQ-09 awaits the page-8 diagram; EQ-10 volume discrepancy unresolved.
- Vortex-line evolution `NOT_CERTIFIED`; D3 `NOT VALIDATED`.
- **Gate 2 - GPE stationarity `NOT_TESTED`** (separate gate, not started).
