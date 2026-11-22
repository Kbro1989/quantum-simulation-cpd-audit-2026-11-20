# PKS research index

**Built:** 2026-11-22
**Builder:** `cpd_pks_research_index_builder_2026-11-22.py`
**Source material:** `../schauberger_sources_2026-11-22/`

Five artifacts, each generated from files already on disk. Nothing here is
hand-typed from the research narrative.

| artifact | content |
|---|---|
| `pks_temporal_change_map.csv` | 1513 index rows — capture timestamp, year, month, original URL, Wayback URL, urlkey, content hash flag |
| `pks_source_provenance.json` | retrieval method, source URL, sha256 and transcription confidence for each of the 4 recovered PKS documents |
| `pks_equation_inventory.json` | 12 equations (10 from the Harthun/Rennert PDF, 2 external), each with verification flag and transcription confidence |
| `pks_geometry_inventory.json` | 3 geometries (Walter egg curve, Donepudi funnel, Lyra elliptic vortex) + the open `xy=1` vs `z=0.079/r²` discrepancy |
| `pks_claim_evidence_matrix.csv` | 12 claims classified: historical assertion / attribution, mathematical claim, experimentally supported, established methodological or mathematical result |

## What this index does NOT claim

- **No content comparison between captures.** The CDX index supplies timestamps
  and URLs, not page bodies. `content_hash` is `NOT_CAPTURED` and
  `content_compared` is `no` on every row. Any statement about *what changed*
  between two captures would be fabricated until capture bodies are fetched.
- **No archived capture body has been fetched.** `archived_captures_fetched: 0`.
  The four PKS documents were read from the live URLs via a reader because the
  origin serves a JavaScript challenge interstitial to `curl`; the interstitials
  are kept as `*_BLOCKED_js_challenge.html`.
- **Equation confidence is marked, not assumed.** The PDF text layer fragments
  fractions, radicals and subscripts. Entries PKS-EQ-04…EQ-10 are
  `partial`/`low` and are leads to confirm against the printed PDF, not
  established forms. PKS-EQ-01…EQ-03 and EQ-06 are `high`.

## Separation of concerns

`archive-org-api-knowledge-base` remains a **separate reference repository**
(archival retrieval methodology). Its documents are copied into
`../schauberger_sources_2026-11-22/ia-knowledge-base/` for traceability only;
the scientific evidence lives here and in `../schauberger_sources_2026-11-22/`.

Cross-reference: `../cpd_schauberger_research_atlas_2026-11-22.md` (research
seed) and `../cpd_vortex_provenance_2026-11-22.md` (the two vortex referents).
