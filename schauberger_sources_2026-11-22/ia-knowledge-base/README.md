# archive.org (Internet Archive) developer API — knowledge base for AI agents

A **queryable knowledge base** over the **[Internet Archive developer API](https://archive.org/developers/)**
— items & metadata, IA-S3 upload, Advanced Search & the cursor Scrape API, Tasks / Changes / Views /
Reviews, the **Wayback Machine** (Availability, CDX Server, Save Page Now 2), and the
`internetarchive` Python library + `ia` CLI — one clean Markdown page per API/topic, with the
request shape, parameters, response fields, and the read-vs-write auth model.

Built as an [**eidetic**](https://github.com/LARIkoz/eidetic) _topic base_: attach it to your project
over MCP and ask, in plain language, **“how do I upload an item, is this URL archived, how do I
bulk-export a collection?”** — instead of scrolling the docs or guessing request shapes.

> Useful for Claude Code / Cursor / any MCP or RAG agent that needs to build correct Internet Archive
> calls: read item metadata (`archive.org/metadata/<id>`), search & scrape the item index,
> create / modify items (IA S3), submit derive tasks, and archive or look up URLs in the Wayback
> Machine (Availability / CDX / Save Page Now).

## Layout

```
docs/
  HOME.md                    # hub: the API surface, the auth model, and every page grouped
  <group>/<page>.md          # one page per API/topic — request, params, response, notes
                             # groups: getting_started, metadata, upload_s3, search,
                             #         services, derive, wayback, python_library
.eidetic-base.json           # manifest (attach-ready)
skill/SKILL.md               # agent usage guide (auth model, item model, endpoint map)
```

Four APIs the official Sphinx portal doesn't expose cleanly are included as **curated** pages
(each cites its public upstream): Wayback **Availability**, Wayback **CDX Server** (mirrored from
the canonical GitHub README), **Save Page Now 2**, and **Advanced Search + Scrape**.

## Use it as an eidetic base

```bash
git clone https://github.com/LARIkoz/archive-org-api-knowledge-base.git ~/eidetic-bases/archiveorg-base
# point eidetic at it, then:
python3 ~/.claude/memory-system/bin/base.py index  archiveorg
python3 ~/.claude/memory-system/bin/base.py attach archiveorg --scope project --run
# now ask:  archiveorg_search "is this URL archived in the wayback machine"
```

Don't use eidetic? The `docs/` tree is plain Markdown — drop it into any RAG / vector store.

## Auth & execution model (TL;DR — full detail per page)

The Internet Archive is organised around **items** (a bucket of files + a metadata record,
addressed by a unique `identifier`). **Reads are public; writes need IA-S3 keys.**

- **Read** (no auth): `GET https://archive.org/metadata/<identifier>`, Advanced Search / Scrape,
  Wayback Availability / CDX, Views, Changes.
- **Write / upload** (IA-S3 keys from <https://archive.org/account/s3.php>): sent as
  **`Authorization: LOW <access>:<secret>`** — used by the IA S3 upload API, Metadata Write, Tasks,
  and Save Page Now 2. Keep the pair in environment variables; never hard-code it.
- **Host split:** item APIs on `archive.org` / `s3.us.archive.org`; Wayback on `web.archive.org`.
- **Easiest client:** the `internetarchive` Python library / `ia` CLI (Save Page Now is the one
  thing they don't wrap — call it directly with the `LOW` header).

## Agent skill

`skill/SKILL.md` is a drop-in Claude Code skill that teaches an agent the Internet Archive
essentials — the item model, the read-vs-write auth split, and the endpoint map. Install it:

```bash
mkdir -p ~/.claude/skills/archiveorg && cp -R skill/* ~/.claude/skills/archiveorg/
```

## Attribution & license

Documentation content is mirrored from the **public** Internet Archive developer docs
(<https://archive.org/developers/>) and is **© Internet Archive** — see [`NOTICE`](NOTICE). This is
an **unofficial**, community convenience mirror for AI tooling; not affiliated with or endorsed by
the Internet Archive. To request removal, open an issue.

The repository structure, the `skill/` guide, and the `HOME.md` hub are original work, released
under the MIT License.
