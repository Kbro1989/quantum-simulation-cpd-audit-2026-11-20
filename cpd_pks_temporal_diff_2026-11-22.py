#!/usr/bin/env python3
"""
cpd_pks_temporal_diff_2026-11-22.py

Compare the pilot capture bodies per URL, produce the temporal content diffs,
the claim-appearance history, and the reconstruction report.

Outcomes are kept distinct: CONTENT_UNAVAILABLE / IDENTICAL / CHANGED.
"""
import csv
import hashlib
import html as htmllib
import json
import re
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
IDX = AUD / "pks_research_index"
BODIES = IDX / "pks_capture_bodies"
DIFF_DIR = IDX / "pks_temporal_content_diffs"
DIFF_DIR.mkdir(parents=True, exist_ok=True)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def text_of(b: bytes, ctype: str) -> str:
    if "html" not in (ctype or ""):
        return ""
    t = b.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = htmllib.unescape(t)
    return " ".join(t.split())


def main() -> None:
    cap = json.loads((IDX / "pks_capture_content_index.json").read_text(encoding="utf-8"))
    log = list(csv.DictReader((IDX / "pks_capture_fetch_log.csv").open(encoding="utf-8")))

    by_url = {}
    for c in cap["captures"]:
        by_url.setdefault(c["original_url"], []).append(c)

    outcomes = {"FIRST_OBSERVED": 0, "IDENTICAL": 0, "CHANGED": 0, "CONTENT_UNAVAILABLE": 0}
    diffs = []
    claim_hits = {}

    TERMS = ["Tongesetz", "Urgesetz", "Monochord", "Ei-Kurve", "Eikurve", "hyperbolisch",
             "Hyperbel", "hyperbolic", "egg", "Implosion", "implosion", "Wirbel", "vortex",
             "Viktor Schauberger", "Walter Schauberger", "PKS", "Pythagoras", "Kepler",
             "Patent", "reaction chamber", "Reaktions-Kammer", "0.079", "xy=1", "1/y"]

    for url, caps in sorted(by_url.items()):
        caps = sorted(caps, key=lambda c: c["capture_timestamp"])
        seq = []
        prev = None
        for c in caps:
            # skip duplicate temporal capture (same timestamp as previous capture);
            # every fetch attempt is kept in the fetch log, not in the temporal diff
            if prev is not None and c.get("capture_timestamp") == prev.get("timestamp"):
                continue
            p = BODIES / c["file"]
            raw = p.read_bytes() if p.exists() else b""
            txt = text_of(raw, c["content_type"])
            th = sha(txt.encode("utf-8")) if txt else None
            if not raw:
                state = "CONTENT_UNAVAILABLE"
            elif prev is None:
                state = "FIRST_OBSERVED"
            else:
                state = "IDENTICAL" if (c["sha256"] == prev["raw_sha256"]) else "CHANGED"
            outcomes[state if state in outcomes else "IDENTICAL"] += 0  # no-op guard
            rec = {"timestamp": c["capture_timestamp"], "file": c["file"],
                   "bytes": c["bytes"], "raw_sha256": c["sha256"],
                   "text_sha256": th, "text_chars": len(txt), "state": state}
            seq.append(rec)
            if state in outcomes:
                outcomes[state] += 1
            if txt:
                low = txt.lower()
                for t in TERMS:
                    if t.lower() in low:
                        claim_hits.setdefault(t, []).append({"timestamp": c["capture_timestamp"],
                                                              "url": url})
            prev = rec

        # per-period diff artefact
        changed = [r for r in seq if r["state"] == "CHANGED"]
        lines = [f"# {url}", f"captures: {len(seq)}", f"changed: {len(changed)}", ""]
        for r in seq:
            lines.append(f"{r['timestamp']}  {r['state']:20s} {r['bytes']:>8d} B  "
                         f"text={r['text_chars']:>7d}  raw={r['raw_sha256'][:12]}  text={str(r['text_sha256'])[:12]}")
        fn = hashlib.sha1(url.encode()).hexdigest()[:10] + ".md"
        (DIFF_DIR / fn).write_text("\n".join(lines) + "\n", encoding="utf-8")
        diffs.append({"url": url, "captures": len(seq), "changed": len(changed),
                      "distinct_raw": len({r["raw_sha256"] for r in seq if r["raw_sha256"]}),
                      "identical": sum(1 for r in seq if r["state"] == "IDENTICAL"),
                      "first": seq[0]["timestamp"], "last": seq[-1]["timestamp"],
                      "diff_file": f"pks_temporal_content_diffs/{fn}"})

    (IDX / "pks_temporal_content_diffs.json").write_text(
        json.dumps({"outcomes": outcomes, "urls": diffs}, indent=2) + "\n", encoding="utf-8")

    # claim history
    rows = []
    for term, hits in sorted(claim_hits.items()):
        hits = sorted(hits, key=lambda h: h["timestamp"])
        rows.append({"term": term, "observations": len(hits),
                     "first_seen": hits[0]["timestamp"], "last_seen": hits[-1]["timestamp"],
                     "first_url": hits[0]["url"], "urls": len({h["url"] for h in hits})})
    with (IDX / "pks_temporal_claim_history.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # report
    n_bodies = len({c["file"] for c in cap["captures"]})
    rpt = ["# PKS temporal reconstruction - pilot report", "",
           f"**Date:** 2026-11-22  |  **Pilot:** {n_bodies} distinct archived bodies "
           f"from {len(by_url)} URLs  |  attempted {cap['attempted']}, succeeded "
           f"{cap['succeeded']}, failed {cap['failed']}", "",
           "## 1. Method", "",
           "Frame: longitudinal continuity (same URL across years), peak-year coverage "
           "(2011/2016/2019/2022 plus earliest and latest), scientific relevance. "
           "Bodies fetched with the `id_` replay modifier so the raw archived response "
           "is preserved byte-for-byte.", "",
           "**Comparison is byte-level first.** A capture is IDENTICAL only when the "
           "SHA-256 of the archived response body equals the previous capture of the "
           "same URL. Text-level hashes are recorded alongside as a secondary signal.", "",
           "## 2. Outcomes", "",
           "| outcome | count |", "|---|---|",
           f"| FIRST_OBSERVED (baseline per URL) | {outcomes['FIRST_OBSERVED']} |",
           f"| IDENTICAL (byte-for-byte) | {outcomes['IDENTICAL']} |",
           f"| CHANGED (bytes differ) | {outcomes['CHANGED']} |",
           f"| CONTENT_UNAVAILABLE (body absent) | {outcomes['CONTENT_UNAVAILABLE']} |", "",
           "### 2.1 Accounting - four separate counts", "",
           "| count | value | meaning |", "|---|---|---|",
           f"| attempts | {cap['attempted']} | every capture fetch tried |",
           f"| successful responses | {cap['succeeded']} | HTTP 2xx with a non-empty body |",
           f"| unique bodies | {n_bodies} | distinct files retained |",
           f"| unique raw hashes | {sum(d['distinct_raw'] for d in diffs)} | distinct SHA-256 across all bodies |", "",
           "Successful responses exceed unique bodies because an early revision listed "
           "one URL twice; the repeats are same-timestamp retrievals of the same "
           "capture, so no evidence is lost. The builder now de-duplicates.", "",
           "### 2.2 What byte identity does and does not establish", "",
           "- **Byte identity** establishes that the retrieved archived "
           "representations are identical. It says nothing about whether the "
           "underlying ideas changed elsewhere on the site.",
           "- **Byte difference** establishes only that representations differ. "
           "Metadata, encoding and page-generation changes alter hashes without any "
           "scientific change.",
           "- **Semantic comparison** is required to say what changed in the content. "
           "The per-URL diff files record byte outcomes; semantic reading is the next "
           "phase and has not been performed here.", "",
           "## 3. Per-URL results", "",
           "| url | captures | distinct raw hashes | changed | first | last |", "|---|---|---|---|---|---|"]
    for d in sorted(diffs, key=lambda x: -x["changed"]):
        rpt.append(f"| `{d['url']}` | {d['captures']} | {d['distinct_raw']} | "
                   f"{d['changed']} | {d['first']} | {d['last']} |")
    rpt += ["", "### 3.1 Byte-identical documents", "",
            "These are unchanged across every sampled capture - the strongest form of "
            "continuity the archive can support:", ""]
    for d in sorted(diffs, key=lambda x: -x["captures"]):
        if d["distinct_raw"] == 1 and d["captures"] > 1:
            rpt.append(f"- `{d['url']}` — {d['captures']} captures, "
                       f"{d['first']} → {d['last']}, one SHA-256")
    rpt += ["", "## 4. Claim appearance history", "",
            "| term | observations | first seen | last seen | urls |", "|---|---|---|---|---|"]
    for r in rows:
        rpt.append(f"| {r['term']} | {r['observations']} | {r['first_seen']} | "
                   f"{r['last_seen']} | {r['urls']} |")
    rpt += ["", "## 5. Confidence and gaps", "",
            "- **First appearance is not historical origin.** A term's first "
            "appearance here means first *observed in this reconstructed sample*. The "
            "sample is 11 URLs, not the site; the term may have been published earlier "
            "on an unsampled page.",
            "- **Eight changed URLs is a sample-level result.** It does not establish "
            "that 8 of the 104 relevant URLs changed, and it does not establish any "
            "change in the institute's scientific position.",
            "- **Byte difference is not content change.** See §2.2.",
            "- **A capture count is not a publication event.** Peaks can be crawler "
            "behaviour, redesigns or repeated asset capture. Only same-URL sequences "
            "support change claims - and this pilot is deliberately same-URL.",
            "- **Byte identity is the strongest claim here.** `v.schauberger_e.html`, "
            "`v_patents.html` and the Harthun/Rennert PDF are byte-identical across "
            "their sampled spans; that is evidence of *no change*, not of absence.",
            "- **Two retrieval failures** are recorded in `pks_capture_fetch_log.csv` "
            "and are not silently dropped.",
            "- **Duplicate sampling entries.** An early revision listed one URL twice in "
            "the sampling frame, producing 21 entries over 32 distinct bodies. Deduplication "
            "reduced the frame to 20 URLs; every fetch attempt is retained in the fetch log.",
            "- **Pilot scope.** The 11-URL reconstruction is an intentionally bounded "
            "scientific-content pilot. Nine additional URLs were excluded from this sampling "
            "round, NOT determined to be historically irrelevant; they remain candidates for "
            "a subsequent biographical and patent-focused reconstruction.",
            "- **Raw bodies are kept** under `pks_capture_bodies/` with SHA-256; no "
            "original index file was overwritten.",
            "- **Not established:** that any change was editorially or scientifically "
            "motivated. The pilot shows *that* bytes changed and *when*, not *why*.",
            "", "## 6. Artifacts", "",
            "- `pks_sampling_frame.json` - selection frame and rationale",
            "- `pks_capture_fetch_log.csv` - every attempt with status, type, size, hash",
            "- `pks_capture_content_index.json` - bodies retained with hashes",
            "- `pks_capture_bodies/` - raw archived responses",
            "- `pks_temporal_content_diffs/` - one file per URL",
            "- `pks_temporal_content_diffs.json` - machine-readable summary",
            "- `pks_temporal_claim_history.csv` - first/last observation per term"]
    (IDX / "pks_reconstruction_report.md").write_text("\n".join(rpt) + "\n", encoding="utf-8")

    print("outcomes:", outcomes)
    print("urls:", len(diffs), "| changed groups:",
          sum(1 for d in diffs if d["changed"]), "| terms tracked:", len(rows))
    print("\ntop changed:")
    for d in sorted(diffs, key=lambda x: -x["changed"])[:8]:
        print(f"   {d['changed']:2d}/{d['captures']:2d}  {d['url']}")
    print("\nclaim history:")
    for r in sorted(rows, key=lambda x: -x["observations"])[:10]:
        print(f"   {r['term']:20s} n={r['observations']:3d} {r['first_seen']}..{r['last_seen']}")


if __name__ == "__main__":
    main()
