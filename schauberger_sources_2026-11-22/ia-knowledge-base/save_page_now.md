---
name: Save Page Now 2 (SPN2) API — archive a live URL on demand
description: Save Page Now 2 (SPN2) API — POST web.archive.org/save to capture a live URL into the Wayback Machine, poll /save/status/{job_id}, check quota via /save/status/user. Auth = your IA S3 keys (Authorization: LOW access:secret).
type: reference
metadata:
  source: curated
  group: wayback
  endpoint: https://docs.google.com/document/d/1Nsv52MvSjbLb2PCpHlat0gkzw0EvtSgpKHu4mk0MnrA/edit
---

# Save Page Now 2 (SPN2) API — archive a live URL on demand

> Source: https://docs.google.com/document/d/1Nsv52MvSjbLb2PCpHlat0gkzw0EvtSgpKHu4mk0MnrA/edit · CURATED reference (upstream not cleanly scrapeable) · compiled 2026-07-03. Hub: [[HOME]]

**Save Page Now 2 (SPN2)** captures a *live* URL into the Wayback Machine on demand. Unlike
the read APIs, capturing is a **write** operation and requires your **IA S3 keys** (the same
`access:secret` pair used by the [[ias3|IA S3 API]] — get them at
<https://archive.org/account/s3.php>).

## Authentication

Send your S3 keys in the `Authorization` header on every SPN2 call:

```
Authorization: LOW <ACCESS_KEY>:<SECRET_KEY>
Accept: application/json
```

## 1 · Submit a capture

```
POST https://web.archive.org/save
Content-Type: application/x-www-form-urlencoded

url=https://example.com/page&capture_outlinks=0
```

Response: `{"url": "https://example.com/page", "job_id": "spn2-abc123..."}`.

**Useful form parameters** (all optional, `1`/`0`):

| Param | Effect |
| --- | --- |
| `capture_all` | Also capture pages that return an error status (4xx/5xx). |
| `capture_outlinks` | Also capture the page's outlinks. |
| `capture_screenshot` | Save a screenshot of the page as a separate capture. |
| `skip_first_archive` | Skip the check for the first-ever archive of the URL (faster). |
| `if_not_archived_within` | Only capture if no snapshot exists within the given period (e.g. `3600` seconds or `1d`). |
| `outlinks_availability` | Return availability of the page's outlinks in the status. |
| `email_result` | Email a report when the capture completes. |

## 2 · Poll capture status

```
GET https://web.archive.org/save/status/<job_id>
```

Returns `status: pending | success | error`. On success it includes `original_url`,
`timestamp`, `duration_sec`, and (when requested) `outlinks` / `screenshot`. On error it
includes an `exception`/`status_ext` describing the failure.

## 3 · Check your account quota / session limits

```
GET https://web.archive.org/save/status/user
```

Returns your available vs. used capture slots (SPN2 enforces per-account **concurrency** and
**daily** capture limits). This is also the cheapest **key-liveness probe** — a valid key pair
returns `200`; bad credentials return `401`.

## Notes

- Rate/limits: SPN2 throttles concurrent + daily captures per account; back off on `429` and
  consult `/save/status/user`.
- The `internetarchive` Python library and `ia` CLI do **not** wrap SPN2 — call it directly
  (e.g. `requests.post`) with the `LOW access:secret` header.
- To only *read* existing captures, use the [[wayback_availability|Availability API]] or the
  [[wayback_cdx|CDX Server API]] — no keys required.
