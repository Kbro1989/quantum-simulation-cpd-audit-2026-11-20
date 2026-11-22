---
name: Wayback Availability API — is a URL archived / closest snapshot
description: Wayback Availability API — the simplest Wayback endpoint: GET archive.org/wayback/available?url=&timestamp= returns the closest snapshot. Public read, no auth.
type: reference
metadata:
  source: curated
  group: wayback
  endpoint: https://archive.org/help/wayback_api.php
---

# Wayback Availability API — is a URL archived / closest snapshot

> Source: https://archive.org/help/wayback_api.php · CURATED reference (upstream not cleanly scrapeable) · compiled 2026-07-03. Hub: [[HOME]]

The **Availability API** is the simplest way to look up whether a URL is in the Wayback
Machine and to get the snapshot closest to a given time. It is a public read endpoint — **no
authentication**.

## Request

```
GET https://archive.org/wayback/available?url=<URL>[&timestamp=<YYYYMMDDhhmmss>][&callback=<jsonp_fn>]
```

- **`url`** (required) — the target URL, without a scheme is fine (e.g. `example.com/page`).
- **`timestamp`** (optional) — desired point in time, `YYYYMMDDhhmmss` (any left-truncation
  works: `2013`, `201301`, `20130101`). The API returns the **closest** capture to it. Omit to
  get the most recent.

## Response (JSON)

```json
{
  "url": "example.com",
  "archived_snapshots": {
    "closest": {
      "available": true,
      "url": "http://web.archive.org/web/20130119213259/http://example.com",
      "timestamp": "20130119213259",
      "status": "200"
    }
  }
}
```

- `archived_snapshots` is **`{}` (empty)** when there is no capture for the URL.
- `closest.url` is the dated Wayback replay URL; `timestamp` is the actual capture time (may
  differ from the one you requested); `status` is the HTTP status recorded at capture.

## When to use which Wayback API

- **Availability** (this page) — one closest snapshot, yes/no + link. Cheapest.
- **[[wayback_cdx|CDX Server API]]** — the full list of captures (every timestamp), with
  filtering/collapsing/pagination. Use for enumeration & change detection.
- **[[save_page_now|Save Page Now 2]]** — create a *new* capture (write; needs IA S3 keys).
