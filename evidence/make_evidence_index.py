#!/usr/bin/env python3
"""Build cpd_evidence_index.json — machine-readable index of every deliverable
in the CPD audit directory, with SHA-256 and size.

Usage: python evidence/make_evidence_index.py >/dev/null && echo OK
"""
import hashlib
import json
import os
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")

EXCLUDE = {
    "evidence/_l5_launcher.py",                       # probe launcher (build artifact)
    "evidence/probe_E_consumer_correctness_run.txt",  # derived from probe file
    "evidence/probe_L5_runtime.py",                   # derived probe script
    "evidence/compare_all_files_md.py",               # derived comparison helper
    "evidence/graph_query_out.txt",                   # derived from graph
    "evidence/*.py",                                  # helper scripts
    "evidence/*.log",                                 # subagent transcripts
}

SKIP_DIRS = {"evidence", "probes"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    records = []
    for root, dirs, files in os.walk(AUD):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            p = Path(root) / name
            rel = p.relative_to(AUD)
            if rel.as_posix() in EXCLUDE:
                continue
            records.append({
                "path": rel.as_posix(),
                "size_bytes": p.stat().st_size,
                "sha256": sha256(p),
                "format": p.suffix.lower() or "dir",
            })
    records.sort(key=lambda r: r["path"])
    out = AUD / "cpd_evidence_index.json"
    out.write_text(json.dumps({"audit": "quantum-simulation CPD", "date": "2026-11-20",
                               "entries": records}, indent=2), encoding="utf-8")
    print(f"entries: {len(records)}")
    print(f"written: {out}")
    return 0


if __name__ == "__main__":
    main()
