#!/usr/bin/env python3
"""
cpd_retrieve_primary_references_2026-11-22.py

Retrieves the missing primary references identified by the 2026-11-22 reference audit,
into schauberger_sources_2026-11-22/. Every download is verified: HTTP status, PDF magic,
page count, byte size and SHA-256. A failed download is recorded, never silently skipped.

Sources (resolved 2026-11-22):
  arXiv:cond-mat/9806038  Dalfovo, Giorgini, Pitaevskii, Stringari
  arXiv:cond-mat/9906144  Castin, Dum
  arXiv:2001.01616        Galantucci, Baggaley, Parker, Barenghi
  arXiv:1711.02814        Yui, Kobayashi, Tsubota (et al.)
  PNAS (PMC6369748)      Fonda, Sreenivasan, Lathrop
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pymupdf

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
S = AUD / "schauberger_sources_2026-11-22"
OUT = AUD / "pks_research_index" / "pks_retrieved_references_2026-11-22.json"

JOBS = [
    ("arxiv_cond-mat_9806038_dalfovo.pdf",
     "https://arxiv.org/pdf/cond-mat/9806038",
     "Dalfovo, Giorgini, Pitaevskii, Stringari — Theory of Bose-Einstein condensation in trapped gases",
     "cond-mat/9806038", "gpe_bec"),
    ("arxiv_cond-mat_9906144_castin_dum.pdf",
     "https://arxiv.org/pdf/cond-mat/9906144",
     "Castin, Dum — Bose-Einstein condensates with vortices in rotating traps",
     "cond-mat/9906144", "gpe_bec"),
    ("arxiv_2001.01616_galantucci.pdf",
     "https://arxiv.org/pdf/2001.01616",
     "Galantucci et al. — A new self-consistent approach of quantum turbulence in superfluid helium",
     "2001.01616", "two_fluid_helium"),
    ("arxiv_1711.02814_yui.pdf",
     "https://arxiv.org/pdf/1711.02814",
     "Yui et al. — Three-dimensional coupled dynamics of the two-fluid model in superfluid He-4",
     "1711.02814", "two_fluid_helium"),
]

# Retrieval attempted 2026-11-22 but blocked from this host; recorded, not silently dropped.
PENDING = [
    {"file": "fonda_2019_pnas_reconnection.pdf",
     "identifier": "10.1073/pnas.1816403116",
     "description": "Fonda, Sreenivasan, Lathrop — Reconnection scaling in quantum fluids (PNAS 116, 1924)",
     "population": "two_fluid_helium",
     "status": "RETRIEVAL_BLOCKED",
     "reason": ("PMC serves a JS-gated 'Preparing to download' page (no PDF); "
                "pnas.org/pdf and europepmc.org/pdf render both return HTTP 403 from "
                "this host. Not fabricated — left pending.")},
]


def fetch(url, dest):
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "180",
                        "-A", "Mozilla/5.0 (research-archive; contact kristain33rs@gmail.com)",
                        "-o", str(dest), "-w", "%{http_code}", url],
                       capture_output=True, text=True, timeout=240)
    return r.stdout.strip(), r.stderr.strip()


def main():
    records = []
    for name, url, desc, ident, pop in JOBS:
        dest = S / name
        code, err = fetch(url, dest)
        rec = {"file": name, "source_url": url, "identifier": ident,
               "description": desc, "population": pop, "http_status": code}
        ok = False
        if dest.exists() and dest.stat().st_size > 1000:
            b = dest.read_bytes()
            rec["bytes"] = len(b)
            rec["sha256"] = hashlib.sha256(b).hexdigest()
            rec["magic_ok"] = b[:5] == b"%PDF-"
            if rec["magic_ok"]:
                try:
                    d = pymupdf.open(str(dest))
                    rec["pages"] = d.page_count
                    ok = d.page_count > 0
                except Exception as e:
                    rec["open_error"] = str(e)
        rec["verified"] = bool(ok)
        records.append(rec)
        print(f"  {'OK ' if ok else 'FAIL'} {name:44s} http={code} "
              f"{rec.get('bytes','?'):>9} bytes  {rec.get('pages','?')} pages")

    out = {"retrieved": "2026-11-22", "count": len(records),
           "verified_count": sum(1 for r in records if r["verified"]),
           "records": records, "pending": PENDING}
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nverified {out['verified_count']}/{out['count']} -> {OUT}")
    return 0 if out["verified_count"] == out["count"] else 1


if __name__ == "__main__":
    sys.exit(main())
