# PKS research index

**Built:** 2026-11-22
**Builder:** `cpd_pks_research_index_builder_2026-11-22.py`
**Source material:** `../schauberger_sources_2026-11-22/`

**Original five artifacts** (built 2026-11-22), each generated from files already on disk.
Nothing here is hand-typed from the research narrative.

| artifact | content |
|---|---|
| `pks_temporal_change_map.csv` | 1513 index rows — capture timestamp, year, month, original URL, Wayback URL, urlkey, content hash flag |
| `pks_source_provenance.json` | retrieval method, source URL, sha256 and transcription confidence for each of the 4 recovered PKS documents |
| `pks_equation_inventory.json` | 12 equations (10 from the Harthun/Rennert PDF, 2 external), each with verification flag and transcription confidence |
| `pks_geometry_inventory.json` | 3 geometries (Walter egg curve, Donepudi funnel, Lyra elliptic vortex) + the open `xy=1` vs `z=0.079/r²` discrepancy |
| `pks_claim_evidence_matrix.csv` | 12 claims classified: historical assertion / attribution, mathematical claim, experimentally supported, established methodological or mathematical result |

**Subsequent expansions** (same directory, later additions — not part of the original five):
`pks_citation_index.{json,md}` (10 records, four evidence populations),
`pks_retrieved_references_2026-11-22.json` (4 hash-verified PDFs + 1 blocked),
`pks_reconstruction_report.md`, `pks_printed_math_recovery_2026-11-22.md`,
`pks_temporal_content_diffs{,.json}`, `pks_capture_*`, and the `pks_vortex_*` /
`quantum_vortex_*` detector-generation reports (see `CPD_CROSS_REFERENCE_INDEX.md` §F).

## What this index does NOT claim

- **The temporal change map is an index, not a content comparison.** The CDX index
  supplies timestamps and URLs, not page bodies. `content_hash` is `NOT_CAPTURED` and
  `content_compared` is `no` on every row of `pks_temporal_change_map.csv`. Any
  statement about *what changed* between two captures would be fabricated until the
  capture bodies are fetched. Capture bodies **have** since been fetched for a pilot
  set (32 unique bodies from 36 attempts); the per-URL comparisons live in
  `pks_temporal_content_diffs/`.
- **Equation confidence is marked, not assumed.** The PDF text layer fragments
  fractions, radicals and subscripts. EQ-04 and EQ-07…EQ-10 are `partial`/`low` and
  are leads to confirm against the printed PDF. **EQ-05 and EQ-10 were subsequently
  recovered from the rendered pages** (see below) and are no longer text-layer
  transcriptions.
- **A mathematical identity is not a physical mechanism.** The recovered egg-curve
  geometry is a mathematical object with an unresolved volume calculation.

## Equation recovery status (2026-11-22)

The Harthun/Rennert PDF (`Berechnung_Ei-Kurve.pdf`, SHA-256 `ec4358df…`, 157,656 B)
is **byte-identical across the 2020-10-29, 2024-04-15 and 2026-07-11 captures** — a
fixed reference. Pages 6, 7 and 9 were rendered at 200 DPI and read visually
(`pks_eikurve_pages/`); page 8 (two-point and point-slope forms) was rate-limited and
remains on the text-layer transcription.

| equation | status | artifact |
|---|---|---|
| EQ-03 | `ALGEBRAICALLY_VERIFIED` | `pks_equation_audit.json` |
| EQ-07, EQ-08 | `ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS` | `pks_equation_audit.json` |
| EQ-09 | `SIGN_CONVENTION_UNRESOLVED` | needs the page-8 diagram |
| EQ-05 | `CLOSURE_PROVEN` | `pks_printed_math_recovery_2026-11-22.md` |
| EQ-10 | `DISCREPANCY_PRESERVED` | `pks_printed_math_recovery_2026-11-22.md` |

EQ-05 closure is analytic, not merely numerical: both parameter-domain endpoints
coincide at `(0, 1.6018862051)`; the removable singularities at `cos φ = 0` give
`r → 1/z₀ = 7/6`; the radicand is non-negative over the full domain (min 0.163265306,
zero negative samples).

EQ-10's three values are retained, not reconciled: printed equation **5.986907**,
closed-curve integral **7.736654**, source-stated **0.4045**.

## Separation of concerns

`archive-org-api-knowledge-base` remains a **separate reference repository**
(archival retrieval methodology). Its documents are copied into
`../schauberger_sources_2026-11-22/ia-knowledge-base/` for traceability only;
the scientific evidence lives here and in `../schauberger_sources_2026-11-22/`.

Cross-reference: `../cpd_schauberger_research_atlas_2026-11-22.md` (research
seed) and `../cpd_vortex_provenance_2026-11-22.md` (the two vortex referents).
