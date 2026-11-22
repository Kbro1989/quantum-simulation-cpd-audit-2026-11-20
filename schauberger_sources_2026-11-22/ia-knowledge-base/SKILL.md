---
name: archiveorg
description: "Internet Archive (archive.org) developer API usage guide for AI agents — the item model, the read-vs-write auth split (public reads vs IA-S3 `Authorization: LOW access:secret` for writes), reading item metadata (archive.org/metadata/<id>), Advanced Search + the cursor Scrape API, creating/modifying items (IA S3 upload + Metadata Write), derive Tasks, Changes/Views/Reviews, the Wayback Machine (Availability, CDX Server, Save Page Now 2), and the internetarchive Python library + ia CLI. Pairs with the queryable docs base in this repo. Triggers: 'archive.org', 'internet archive', 'internetarchive', 'ia cli', 'wayback', 'wayback machine', 'cdx', 'save page now', 'availability api', 'ias3', 's3.us.archive.org', 'archive.org metadata', 'advancedsearch', 'scrape api'."
---

# archive.org (Internet Archive) developer API — agent guide

Build correct Internet Archive calls without guessing. When the docs base is attached, query it
(`archiveorg_search "<intent>"`) for the exact page (params + response) instead of recalling.

## The item model

The Archive is organised around **items** — a bucket of files plus a metadata record, addressed by
a globally-unique `identifier` (ASCII, ≤100 chars, first char alphanumeric). Files live under the
item; metadata lives in `<identifier>_meta.xml` + `<identifier>_files.xml` (exposed as JSON via the
Metadata API).

## Auth — reads are public, writes need IA-S3 keys

- **Reads (no auth):** `GET https://archive.org/metadata/<identifier>`, Advanced Search / Scrape,
  Wayback Availability / CDX, Views, Changes.
- **Writes / uploads:** get an IA-S3 `access:secret` pair from <https://archive.org/account/s3.php>
  and send **`Authorization: LOW <access>:<secret>`**. Used by the IA S3 upload API, Metadata Write,
  Tasks, and Save Page Now 2. Keep the pair in env vars (`$IA_ACCESS_KEY`, `$IA_SECRET_KEY`); never
  hard-code. Liveness probe: `GET https://web.archive.org/save/status/user` (200 valid / 401 bad).
- **Host split:** item APIs on `archive.org` / `s3.us.archive.org`; Wayback on `web.archive.org`.

## Endpoint map

| Area                 | What / where                                                                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read metadata**    | `GET archive.org/metadata/<id>` — the whole item record (meta + files) as JSON                                                                              |
| **Find items**       | `advancedsearch.php` (Lucene query, paged, ~10k cap) · `services/search/v1/scrape` (cursor, full bulk export)                                               |
| **Upload / create**  | IA S3-like API — `PUT` files to `s3.us.archive.org` (item ↔ bucket, file ↔ key)                                                                             |
| **Write metadata**   | Metadata Write API — JSON Patch, transactions, targets                                                                                                      |
| **Derive jobs**      | Tasks API — submit / track derive & rebuild; also OCR & PDF derive modules                                                                                  |
| **Feeds / services** | Changes (item change feed), Views (engagement counts), Reviews, Simple Lists (relationships)                                                                |
| **Wayback — read**   | Availability (`archive.org/wayback/available` — closest snapshot) · CDX Server (`web.archive.org/cdx/search/cdx` — every capture, filter/collapse/paginate) |
| **Wayback — write**  | Save Page Now 2 — `POST web.archive.org/save` (needs IA-S3 keys), poll `/save/status/<job_id>`                                                              |
| **Client library**   | `internetarchive` Python package + `ia` CLI — wraps upload/download/search/metadata/tasks                                                                   |

## Search vs Scrape

- **advancedsearch.php** — quick lookups / first page / a UI; Lucene `q`, `fl[]=` fields, `sort[]=`,
  `rows`+`page`, `output=json`. Deep paging capped (`page*rows` ≲ 10k).
- **scrape** (`services/search/v1/scrape`) — complete enumeration past the cap: `q`, `fields=`,
  `count` (≤10000), and a `cursor` you resend until it's absent. Use for whole collections.

## Wayback quick reference

- **Is a URL archived?** → Availability: `GET archive.org/wayback/available?url=…&timestamp=…` →
  `archived_snapshots.closest` (empty `{}` if none).
- **Every capture of a URL/host?** → CDX: `GET web.archive.org/cdx/search/cdx?url=…&output=json`
  with `matchType`, `from`/`to`, `filter=statuscode:200`, `collapse=digest`, pagination.
- **Archive a live URL now?** → Save Page Now 2: `POST web.archive.org/save` (form `url=…`, `LOW`
  auth header), then poll `/save/status/<job_id>`.

## Tips

- Set a descriptive `User-Agent` and honour rate limits — back off on `429`. The Archive publishes
  an automated-access / bot policy; respect it.
- To fetch one item by identifier use the Metadata API, not search.
- The `docs/` base in this repo has one page per API/topic (and the metadata field schema chunked
  per field) — query it for exact parameters and response fields.
