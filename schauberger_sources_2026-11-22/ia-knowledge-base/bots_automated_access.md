---
name: Bots, LLMs & Automated Access — User-Agent, rate limits, best practices
description: This guide covers best practices for bots, AI agents, LLMs, and other automated tools interacting with Internet Archive services and APIs.
type: reference
metadata:
  source: scrape
  group: getting_started
  endpoint: https://archive.org/developers/bots.html
---

# Bots, LLMs & Automated Access — User-Agent, rate limits, best practices

> Source: https://archive.org/developers/bots.html · Internet Archive developer docs · fetched 2026-07-03 · format-converted from HTML. Hub: [[HOME]]

# Bots, LLMs, and Automated Access

This guide covers best practices for bots, AI agents, LLMs, and other automated tools interacting with Internet Archive services and APIs.

## AI Coding Assistants

For AI coding assistants like Claude Code, Cursor, Windsurf, and similar tools, we provide ready-to-use skills and documentation:

**[internetarchive/internet-archive-skills](https://github.com/internetarchive/internet-archive-skills)**

This repository contains skills that enable AI assistants to properly interact with archive.org APIs, including uploading, downloading, searching, and metadata operations.

## User-Agent Requirements

**All automated requests to archive.org must include a descriptive User-Agent header** that identifies:

* The tool or bot name
* Version number
* For AI agents: the model being used (e.g., `claude-sonnet-4-20250514`)

This helps the Internet Archive track usage patterns, troubleshoot issues, and maintain service quality.

### ia CLI (v5.7.2+)

Use the `--user-agent-suffix` option:

```
ia --user-agent-suffix "MyBot/1.0.0 (claude-sonnet-4-20250514)" download my-item

```

Or set it permanently in `~/.config/internetarchive/ia.ini`:

```
[general]
user_agent_suffix = MyBot/1.0.0 (claude-sonnet-4-20250514)

```

### Python Library

Pass the suffix when creating a session:

```
from internetarchive import get_session

session = get_session(config={
    'general': {'user_agent_suffix': 'MyBot/1.0.0 (claude-sonnet-4-20250514)'}
})

# Use session for all operations
item = session.get_item('example-item')

```

Or configure it in your `ia.ini` file as shown above.

### Direct HTTP Requests

When making direct API calls with curl, requests, or other HTTP clients:

```
curl -H "User-Agent: MyBot/1.0.0 (claude-sonnet-4-20250514)" \
  https://archive.org/metadata/example-item

```

```
import requests

headers = {
    'User-Agent': 'MyBot/1.0.0 (claude-sonnet-4-20250514)'
}
response = requests.get('https://archive.org/metadata/example-item', headers=headers)

```

### Resulting User-Agent

When using the `ia` CLI or Python library, your suffix is appended to the default User-Agent:

```
internetarchive/5.7.2 (Linux x86_64; N; en; ACCESS_KEY) Python/3.11.0 MyBot/1.0.0 (claude-sonnet-4-20250514)

```

## Rate Limiting

Automated tools should respect rate limits:

* Add delays between requests for bulk operations
* Honor `429 Too Many Requests` responses and `Retry-After` headers
* Use `--checksum` flags to avoid re-downloading/re-uploading unchanged files
* Consider using GNU Parallel with `-j` to limit concurrent requests

```
# Limit to 4 concurrent downloads with 1 second delay
cat items.txt | parallel -j4 --delay 1 'ia download {}'

```

## Best Practices

1. **Identify your bot clearly** - Use descriptive User-Agent strings
2. **Authenticate when possible** - Configure `ia` with your credentials
3. **Cache responses** - Avoid repeated requests for the same data
4. **Use bulk endpoints** - Prefer batch operations over many individual requests
5. **Choose the right collection** - For content you intend to keep on archive.org, contact [info@archive.org](mailto:info%40archive.org) to request a permanent collection. Otherwise, upload to the Community collection matched to the item’s media type: `opensource` (Community Texts), `opensource_movies` (Community Video), `opensource_audio` (Community Audio), `opensource_image` (Community Images), `opensource_media` (Community Data), or `open_source_software` (Community Software). Use `test_collection` only as a sandbox for validating uploads end-to-end — items there are automatically removed after approximately 30 days
6. **Handle errors gracefully** - Implement retries with exponential backoff
