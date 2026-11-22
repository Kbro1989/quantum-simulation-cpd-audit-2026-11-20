# PKS temporal reconstruction - pilot report

**Date:** 2026-11-22  |  **Pilot:** 32 distinct archived bodies from 11 URLs  |  attempted 36, succeeded 34, failed 2

## 1. Method

Frame: longitudinal continuity (same URL across years), peak-year coverage (2011/2016/2019/2022 plus earliest and latest), scientific relevance. Bodies fetched with the `id_` replay modifier so the raw archived response is preserved byte-for-byte.

**Comparison is byte-level first.** A capture is IDENTICAL only when the SHA-256 of the archived response body equals the previous capture of the same URL. Text-level hashes are recorded alongside as a secondary signal.

## 2. Outcomes

| outcome | count |
|---|---|
| FIRST_OBSERVED (baseline per URL) | 11 |
| IDENTICAL (byte-for-byte) | 13 |
| CHANGED (bytes differ) | 10 |
| CONTENT_UNAVAILABLE (body absent) | 0 |

### 2.1 Accounting - four separate counts

| count | value | meaning |
|---|---|---|
| attempts | 36 | every capture fetch tried |
| successful responses | 34 | HTTP 2xx with a non-empty body |
| unique bodies | 32 | distinct files retained |
| unique raw hashes | 21 | distinct SHA-256 across all bodies |

Successful responses exceed unique bodies because an early revision listed one URL twice; the repeats are same-timestamp retrievals of the same capture, so no evidence is lost. The builder now de-duplicates.

### 2.2 What byte identity does and does not establish

- **Byte identity** establishes that the retrieved archived representations are identical. It says nothing about whether the underlying ideas changed elsewhere on the site.
- **Byte difference** establishes only that representations differ. Metadata, encoding and page-generation changes alter hashes without any scientific change.
- **Semantic comparison** is required to say what changed in the content. The per-URL diff files record byte outcomes; semantic reading is the next phase and has not been performed here.

## 3. Per-URL results

| url | captures | distinct raw hashes | changed | first | last |
|---|---|---|---|---|---|
| `http://www.pks.or.at/forschung_wasser.html` | 3 | 3 | 2 | 20070820181620 | 20171003054101 |
| `https://pks.or.at/berechnungen/` | 3 | 3 | 2 | 20190824093147 | 20260711231444 |
| `http://www.pks.or.at/v.schauberger.html` | 3 | 2 | 1 | 20070820181030 | 20141230035942 |
| `http://www.pks.or.at/w.schauberger.html` | 3 | 2 | 1 | 20070730235440 | 20120821183739 |
| `http://www.pks.or.at/w.schauberger_e.html` | 2 | 2 | 1 | 20100324235812 | 20130718095426 |
| `http://www.pks.or.at/w_berechnungen.html` | 3 | 2 | 1 | 20070820181455 | 20170521002120 |
| `http://www.pks.or.at:80/viktor_patente.html` | 3 | 2 | 1 | 20080417032553 | 20150120154226 |
| `http://www.pks.or.at:80/w_patents.html` | 5 | 2 | 1 | 20080915103925 | 20161001000105 |
| `http://pks.or.at/wp-content/uploads/Berechnung_Ei-Kurve.pdf` | 3 | 1 | 0 | 20201029223404 | 20260711234929 |
| `http://www.pks.or.at/v.schauberger_e.html` | 3 | 1 | 0 | 20070820181052 | 20110821031856 |
| `http://www.pks.or.at:80/v_patents.html` | 3 | 1 | 0 | 20091117122533 | 20110722220350 |

### 3.1 Byte-identical documents

These are unchanged across every sampled capture - the strongest form of continuity the archive can support:

- `http://pks.or.at/wp-content/uploads/Berechnung_Ei-Kurve.pdf` — 3 captures, 20201029223404 → 20260711234929, one SHA-256
- `http://www.pks.or.at/v.schauberger_e.html` — 3 captures, 20070820181052 → 20110821031856, one SHA-256
- `http://www.pks.or.at:80/v_patents.html` — 3 captures, 20091117122533 → 20110722220350, one SHA-256

## 4. Claim appearance history

| term | observations | first seen | last seen | urls |
|---|---|---|---|---|
| Ei-Kurve | 3 | 20190824093147 | 20260711231444 | 1 |
| Eikurve | 1 | 20170521002120 | 20170521002120 | 1 |
| Implosion | 4 | 20080417032553 | 20161001000105 | 2 |
| Kepler | 3 | 20190824093147 | 20260711231444 | 1 |
| PKS | 3 | 20190824093147 | 20260711231444 | 1 |
| Patent | 21 | 20070820181620 | 20260711231444 | 9 |
| Pythagoras | 3 | 20190824093147 | 20260711231444 | 1 |
| Reaktions-Kammer | 1 | 20161001000105 | 20161001000105 | 1 |
| Viktor Schauberger | 19 | 20070820181030 | 20260711231444 | 7 |
| Walter Schauberger | 19 | 20070730235440 | 20260711231444 | 6 |
| Wirbel | 3 | 20070820181620 | 20171003054101 | 1 |
| implosion | 4 | 20080417032553 | 20161001000105 | 2 |
| vortex | 2 | 20070820181620 | 20120826222319 | 1 |

## 5. Confidence and gaps

- **First appearance is not historical origin.** A term's first appearance here means first *observed in this reconstructed sample*. The sample is 11 URLs, not the site; the term may have been published earlier on an unsampled page.
- **Eight changed URLs is a sample-level result.** It does not establish that 8 of the 104 relevant URLs changed, and it does not establish any change in the institute's scientific position.
- **Byte difference is not content change.** See §2.2.
- **A capture count is not a publication event.** Peaks can be crawler behaviour, redesigns or repeated asset capture. Only same-URL sequences support change claims - and this pilot is deliberately same-URL.
- **Byte identity is the strongest claim here.** `v.schauberger_e.html`, `v_patents.html` and the Harthun/Rennert PDF are byte-identical across their sampled spans; that is evidence of *no change*, not of absence.
- **Two retrieval failures** are recorded in `pks_capture_fetch_log.csv` and are not silently dropped.
- **Duplicate sampling entries.** An early revision listed one URL twice, producing 34 index entries over 32 distinct bodies. The duplicates were same-timestamp repeats of the same capture, so no evidence is lost, but the counts differ and the builder now de-duplicates.
- **Raw bodies are kept** under `pks_capture_bodies/` with SHA-256; no original index file was overwritten.
- **Not established:** that any change was editorially or scientifically motivated. The pilot shows *that* bytes changed and *when*, not *why*.

## 6. Artifacts

- `pks_sampling_frame.json` - selection frame and rationale
- `pks_capture_fetch_log.csv` - every attempt with status, type, size, hash
- `pks_capture_content_index.json` - bodies retained with hashes
- `pks_capture_bodies/` - raw archived responses
- `pks_temporal_content_diffs/` - one file per URL
- `pks_temporal_content_diffs.json` - machine-readable summary
- `pks_temporal_claim_history.csv` - first/last observation per term
