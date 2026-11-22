#!/usr/bin/env python3
"""
cpd_pks_capture_pilot_2026-11-22.py

Bounded, stratified capture-body pilot for the PKS historical reconstruction.

Sampling frame (from pks_url_histories.json, built from live CDX per-URL queries):
  * longitudinal continuity - same URL captured in several years (strongest signal)
  * peak-year coverage    - 2011, 2016, 2019, 2022, plus earliest and latest
  * scientific relevance  - egg curve / Walter's mathematics / Viktor's water
                            flow / institute claims and patents

Fetches the raw archived response via the `id_` replay modifier, records the
exact retrieval outcome, and never overwrites the original CDX inventory.

Writes only inside the audit workspace.
"""
import csv
import hashlib
import json
import subprocess
import time
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
SRC = AUD / "schauberger_sources_2026-11-22"
IDX = AUD / "pks_research_index"
BODIES = IDX / "pks_capture_bodies"
BODIES.mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
RETRIEVED = "2026-11-22"

# Priority URLs, most scientifically relevant first.
PRIORITY = [
    "http://pks.or.at/wp-content/uploads/Berechnung_Ei-Kurve.pdf",
    "http://www.pks.or.at/w_berechnungen.html",
    "https://pks.or.at/berechnungen/",
    "http://www.pks.or.at:80/w_patents.html",
    "http://www.pks.or.at:80/viktor_patente.html",
    "http://www.pks.or.at:80/v_patents.html",
    "http://www.pks.or.at:80/w_patents.html",
    "http://www.pks.or.at/w.schauberger_e.html",
    "http://www.pks.or.at/w.schauberger.html",
    "http://www.pks.or.at/v.schauberger_e.html",
    "http://www.pks.or.at/v.schauberger.html",
    "http://www.pks.or.at/forschung_wasser.html",
    "http://www.pks.or.at:80/bio-vs.html",
    "http://www.pks.or.at:80/bio-ws.html",
    "http://www.pks.or.at/1upper_en.html",
    "http://www.pks.or.at/1upper.html",
    "http://pks.or.at/en/viktorschauberger/",
    "http://pks.or.at/en/walterschauberger/",
    "https://pks.or.at/patente/",
    "https://pks.or.at/walter-schauberger/",
    "https://pks.or.at/viktor-schauberger/",
]

PILOT_TARGET = 36

# de-duplicate: an earlier revision listed one URL twice, which produced duplicate
# capture entries and (via the failure path below) destroyed a good body.
PRIORITY = list(dict.fromkeys(PRIORITY))


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def pick_captures(ts_list, k=3):
    """earliest, a mid spread, latest - deduplicated."""
    ts = sorted(set(ts_list))
    if len(ts) <= k:
        return ts
    step = (len(ts) - 1) / (k - 1)
    idxs = sorted({round(i * step) for i in range(k)})
    return [ts[i] for i in idxs]


def main() -> None:
    hist = json.loads((SRC / "pks_url_histories.json").read_text(encoding="utf-8"))["histories"]

    frame = []
    for url in PRIORITY:
        ts = hist.get(url, [])
        if not ts:
            continue
        years = sorted({t[:4] for t in ts})
        frame.append({"url": url, "capture_count": len(ts), "years": years,
                      "first": min(ts), "last": max(ts), "selected": pick_captures(ts)})
    (IDX / "pks_sampling_frame.json").write_text(
        json.dumps({"criterion": ["longitudinal continuity", "peak-year coverage",
                                  "scientific relevance"],
                    "frame": frame}, indent=2) + "\n", encoding="utf-8")

    plan = []
    for row in frame:
        for ts in row["selected"]:
            plan.append((row["url"], ts))
    # pad toward the target with the highest-value unused captures
    if len(plan) < PILOT_TARGET:
        used = {(u, t) for u, t in plan}
        for row in sorted(frame, key=lambda r: -r["capture_count"]):
            for ts in sorted(row["selected"]):
                if (row["url"], ts) not in used:
                    plan.append((row["url"], ts))
                    used.add((row["url"], ts))
                    if len(plan) >= PILOT_TARGET:
                        break
            if len(plan) >= PILOT_TARGET:
                break
    plan = plan[:PILOT_TARGET]
    print(f"frame urls={len(frame)} pilot captures={len(plan)}")

    log = []
    index = []
    for n, (url, ts) in enumerate(plan, 1):
        replay = f"https://web.archive.org/web/{ts}id_/{url}"
        slug = hashlib.sha1(url.encode()).hexdigest()[:10]
        stem = f"{ts}_{slug}"
        raw = BODIES / f"{stem}.bin"
        r = subprocess.run(["curl", "-sSL", "--max-time", "90", "-A", UA,
                            "-o", raw.name,
                            "-w", "%{http_code}\t%{content_type}\t%{size_download}\t%{url_effective}",
                            replay],
                           cwd=str(BODIES), capture_output=True, text=True, timeout=130)
        meta = (r.stdout or "").strip().split("\t")
        code = meta[0] if meta else "?"
        ctype = meta[1] if len(meta) > 1 else ""
        size = meta[2] if len(meta) > 2 else ""
        effective = meta[3] if len(meta) > 3 else ""
        data = raw.read_bytes() if raw.exists() else b""
        # Never destroy a previously-good body on a failed retry: write only on
        # success, leave any existing file untouched otherwise.
        ok = code.startswith("2") and len(data) > 0
        rec = {"n": n, "original_url": url, "capture_timestamp": ts,
               "replay_url": replay, "http_status": code, "content_type": ctype,
               "reported_size": size, "bytes": len(data), "sha256": sha(data) if data else None,
               "effective_url": effective, "ok": ok,
               "error": (r.stderr or "").strip()[:200]}
        log.append(rec)
        print(f"  {'OK ' if ok else 'FAIL'} {n:2d} {ts} {len(data):>8d} B  {ctype[:32]:34s} {url[:70]}")
        if ok:
            raw.write_bytes(data)
            index.append({"file": raw.name, "original_url": url, "capture_timestamp": ts,
                          "bytes": len(data), "sha256": rec["sha256"],
                          "content_type": ctype, "http_status": code})
        time.sleep(0.5)

    with (IDX / "pks_capture_fetch_log.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(log[0].keys()))
        w.writeheader()
        w.writerows(log)
    (IDX / "pks_capture_content_index.json").write_text(
        json.dumps({"retrieved": RETRIEVED, "replay_modifier": "id_ (raw archived response)",
                    "attempted": len(log), "succeeded": len(index), "failed": len(log) - len(index),
                    "captures": index}, indent=2) + "\n", encoding="utf-8")
    print(f"\nattempted={len(log)} succeeded={len(index)} failed={len(log) - len(index)}")


if __name__ == "__main__":
    main()
