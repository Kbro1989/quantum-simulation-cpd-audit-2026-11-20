# Internet Archive knowledge base — local usage note

**Checked:** 2026-11-22
**Question:** which local git repos use `Kbro1989/archive-org-api-knowledge-base`,
and is it needed for the Wayback work in this atlas?

## 1. Repository

| field | value |
|---|---|
| local clone | `C:\Users\krist\Desktop\archive-org-api-knowledge-base` |
| remote 1 | `git@github.com:Kbro1989/archive-org-api-knowledge-base.git` |
| remote 2 | `git@github.com:LARIkoz/archive-org-api-knowledge-base.git` (upstream — it is a fork) |
| GitHub | <https://github.com/Kbro1989/archive-org-api-knowledge-base> — public, fork, created 2026-07-31 |
| purpose | queryable knowledge base over the Internet Archive developer API: items/metadata, IA-S3 upload, Advanced Search & Scrape, Tasks/Changes/Views/Reviews, Wayback (Availability, CDX, Save Page Now), and the `internetarchive` Python library / `ia` CLI |
| layout | `docs/<group>/<page>.md` (one page per API/topic), `skill/SKILL.md`, `.eidetic-base.json` (attach-ready manifest) |

## 2. Local usage check

| location | result |
|---|---|
| Desktop top-level clone | **present** |
| `.git/config` references from other repos | **none** — no other repo lists it as a remote or submodule |
| Hermes skills | one reference: `skills/.archive/github-org-repo-mining/references/github-unauthenticated-discovery.md` (archived skill) |
| `web.archive.org/cdx` callers | **none** in any sovereign repo. Only this knowledge base documents it. |
| `web.archive.org/web/...` occurrences | King Wen `kingwen_train_data/wiki_math_research_batch_2026-07-11{,-layer2}.json` (URLs stored as data, not calls); `zotero/upstream/Internet Archive Wayback Machine.js` (a downloaded Zotero translator) |
| `archive.org/developers` | only inside this knowledge base itself |

**Conclusion:** the knowledge base is the **only local CDX reference** and nothing
else in the stack calls the CDX API. It was needed, and it is used here.

## 3. Correct CDX invocation (per `docs/wayback/wayback_cdx.md`)

Endpoint: `GET https://web.archive.org/cdx/search/cdx`

Parameters used in this session:

```
url=pks.or.at/*          wildcard → prefix match
matchType=prefix         implicit in the trailing /*
filter=statuscode:200    keep only successful captures
collapse=urlkey          one row per distinct URL
fl=timestamp,original    restrict returned fields
output=json              JSON array; first element is the field header
```

### Why the first attempt returned HTTP 503

The first query returned `503` with an 11.8 KB HTML body. The reference explains
the likely cause: the CDX server **caps a single query at 150,000 records by
default**, and a `/*` prefix query over a whole domain is exactly the case the
documentation says to move to the **Pagination API**. A plain retry (no change of
shape) succeeded and returned 1513 rows — so the 503 was transient load, not a
bad query. Do not treat a single 503 as a negative result; retry once and, if it
persists, paginate.

### Pagination parameters (for large queries)

| param | meaning |
|---|---|
| `showNumPages=true` | returns the page count only |
| `page=i` | zero-based page index |
| `pageSize=P` | blocks scanned per page, `1 <= P <= default` (archive.org default 50) |
| `showResumeKey=true` / `resumeKey=` | resume without recomputing from the start |
| `limit=N` / `limit=-N` | first N / last N |
| `showDupeCount=true`, `showSkipCount=true`, `lastSkipTimestamp=true` | counters |
| `gzip=false` | CDX returns gzip by default |
| `fastLatest=true` | faster latest-match path for exact matches |

### Access control

CDX results can be restricted per-URL and per-field; access is granted by an
**API key passed as a cookie**:

```
curl -H "Cookie: <api-key>"
```

Relevant here: `pks.or.at` serves a **JavaScript challenge interstitial** to
plain `curl` (all four PKS fetches returned the same ~12 KB challenge document).
The CDX API is the correct route to that site's history — it reads the archive
index rather than the origin server.

## 4. Result obtained

`wayback_pks_cdx.json` — **1513 captures**, 1513 distinct URLs,
`19981201062636` → `20260914134417`.
Indexed in `wayback_pks_captures_index.json` (per-year counts, top originals).

| year | captures |
|---|---|
| 1998 | 10 |
| 2000 | 28 |
| 2007 | 97 |
| 2011 | 179 |
| 2016 | 186 |
| 2019 | 236 |
| 2021 | 109 |
| 2022 | 198 |
| 2024 | 148 |
| 2026 | 41 |

Capture dates are **not** publication dates — the atlas (§8) already flags this.

## 5. Files copied from the knowledge base

| file | bytes |
|---|---|
| `wayback_cdx.md` | 19,384 |
| `wayback_availability.md` | 2,186 |
| `save_page_now.md` | 3,276 |
| `bots_automated_access.md` | 4,441 |
| `SKILL.md` | 5,537 |
| `README.md` | 4,257 |
| `.eidetic-base.json` | 104 |
