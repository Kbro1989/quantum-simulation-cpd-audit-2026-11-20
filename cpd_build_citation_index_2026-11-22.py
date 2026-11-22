#!/usr/bin/env python3
"""
cpd_build_citation_index_2026-11-22.py

Builds a citation index for the six PDFs in schauberger_sources_2026-11-22/.

Bibliographic fields are taken from the sources themselves (arXiv abs pages and the
PDF text layers, extracted 2026-11-22); hashes, byte sizes and page counts are derived
from disk. Nothing is hand-typed from the research narrative.

Evidence populations are kept separate on purpose:
  gpe_bec            - mean-field Gross-Pitaevskii / trapped BEC
  two_fluid_helium   - coupled normal-fluid + superfluid models
  classical_cfd      - classical fluid / CFD methodology
  classical_geometry - classical vortex geometry and coordinate systems
"""
import hashlib
import json
from pathlib import Path

import pymupdf

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
S = AUD / "schauberger_sources_2026-11-22"
OUT_JSON = AUD / "pks_research_index" / "pks_citation_index.json"
OUT_MD = AUD / "pks_research_index" / "pks_citation_index.md"

ENTRIES = [
    {
        "id": "fetter_svidzinsky_2001_jopcm",
        "file": "fetter_vortices_yale.pdf",
        "title": "Vortices in a trapped dilute Bose-Einstein condensate",
        "authors": ["Alexander L. Fetter", "Anatoly A. Svidzinsky"],
        "year": 2001,
        "venue": "Journal of Physics: Condensed Matter 13 (2001) R135-R194",
        "doi": "10.1088/0953-8984/13/12/201",
        "pii": "S0953-8984(01)08644-1",
        "arxiv_id": "cond-mat/0102003",
        "version": "published",
        "population": "gpe_bec",
        "topic": "GPE vortex structure, energy, dynamics, normal modes, stability, vortex arrays",
        "relevance": "Primary GPE reference for the QuantumLab 1D/2D/3D solver and BEC vortex physics.",
    },
    {
        "id": "fetter_svidzinsky_2001_arxiv",
        "file": "arxiv_cond-mat_0102003_fetter.pdf",
        "title": "Vortices in a trapped dilute Bose-Einstein condensate",
        "authors": ["Alexander Fetter", "Anatoly Svidzinsky"],
        "year": 2001,
        "venue": "arXiv preprint",
        "doi": None,
        "arxiv_id": "cond-mat/0102003",
        "version": "preprint",
        "population": "gpe_bec",
        "topic": "Same work as the J. Phys.: Condens. Matter review; preprint form.",
        "relevance": "Same as the published version; useful for cross-checking pagination and equations.",
    },
    {
        "id": "tang_2022_vortex_rings",
        "file": "arxiv_2211.01560_vortex_rings.pdf",
        "title": "Imaging the decay of quantized vortex rings to decipher quantum dissipation",
        "authors": ["Yuan Tang", "Wei Guo", "Hiromichi Kobayashi", "Satoshi Yui",
                    "Makoto Tsubota", "Toshiaki Kanai"],
        "year": 2022,
        "venue": "arXiv preprint",
        "doi": None,
        "arxiv_id": "2211.01560",
        "version": "preprint",
        "population": "two_fluid_helium",
        "topic": "Quantized vortex rings in He II; Schwarz / two-way / self-consistent two-way models; mutual friction",
        "relevance": "Bridge into 3D vortex-ring dynamics and dissipation; NOT a single-component GPE validation.",
    },
    {
        "id": "bradley_2026_turbulence",
        "file": "arxiv_2607.22244_turbulence.pdf",
        "title": "Turbulence in Quantum Gases: Vortices, Waves, and Cascades",
        "authors": ["Ashton S. Bradley", "Tyler W. Neely", "Xiaoquan Yu", "Brian P. Anderson"],
        "year": 2026,
        "venue": "arXiv preprint",
        "doi": None,
        "arxiv_id": "2607.22244",
        "version": "preprint",
        "population": "gpe_bec",
        "topic": "Review: quantum turbulence, vortex dynamics, waves, cascades in ultracold gases",
        "relevance": "Literature map for later numerical and experimental vortex work in the GPE setting.",
    },
    {
        "id": "lyra_2021_elliptic",
        "file": "arxiv_2108.04013_lyra.pdf",
        "title": "Vortex solution in elliptic coordinates",
        "authors": ["Wladimir Lyra"],
        "year": 2021,
        "venue": "arXiv preprint",
        "doi": None,
        "arxiv_id": "2108.04013",
        "version": "preprint",
        "population": "classical_geometry",
        "topic": "Exact elliptical vortex solution of the Euler equations; elliptic-coordinate transformations",
        "relevance": "Geometric / mathematical reference (metric factors, differential geometry), not a quantum-vortex solution.",
    },
    {
        "id": "donepudi_2024_pof",
        "file": "donepudi_2024_physics_of_fluids.pdf",
        "title": "Numerical analysis of vortex dynamics in hyperbolic funnels using computational fluid dynamics",
        "authors": ["Teja Donepudi", "Maarten van de Griend", "Luewton L. F. Agostinho",
                    "Esther J. de Kroon", "Roman Klymenko", "Rene Pecnik",
                    "Jakob Woisetschlager", "Elmar C. Fuchs"],
        "year": 2024,
        "venue": "Physics of Fluids 36, 095171 (2024)",
        "doi": "10.1063/5.0222216",
        "arxiv_id": None,
        "version": "published",
        "population": "classical_cfd",
        "topic": "3D structured meshes, volume-of-fluid multiphase modelling, Euler-Euler, SST turbulence with curvature correction",
        "relevance": "Classical vortex geometry and CFD methodology; separate from quantum-simulation validation.",
    },
]


def main():
    records = []
    for e in ENTRIES:
        p = S / e["file"]
        b = p.read_bytes()
        doc = pymupdf.open(str(p))
        rec = dict(e)
        rec.update({
            "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest(),
            "pages": doc.page_count,
            "on_disk": True,
        })
        rec["url"] = (f"https://arxiv.org/abs/{e['arxiv_id']}" if e["arxiv_id"]
                      else f"https://doi.org/{e['doi']}")
        records.append(rec)

    out = {
        "collection": "schauberger_sources_2026-11-22",
        "built": "2026-11-22",
        "source_pdf_count": len(records),
        "populations": {
            "gpe_bec": "mean-field Gross-Pitaevskii / trapped BEC",
            "two_fluid_helium": "coupled normal-fluid + superfluid helium models",
            "classical_cfd": "classical fluid / CFD methodology",
            "classical_geometry": "classical vortex geometry and coordinate systems",
        },
        "note": ("Bibliographic fields extracted from the arXiv abs pages and PDF text "
                 "layers; hashes, byte sizes and page counts derived from disk. The "
                 "populations overlap mathematically but do not validate the same "
                 "physical model."),
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = ["# Citation index — schauberger_sources_2026-11-22", "",
             "Built 2026-11-22. Bibliographic fields are extracted from the arXiv abs pages",
             "and PDF text layers; hashes, byte sizes and page counts are derived from disk.", "",
             "## Evidence populations (kept separate)", ""]
    for k, v in out["populations"].items():
        lines.append(f"- **{k}** — {v}")
    lines += ["", "## Records", "",
              "| id | year | population | version | title | venue | id/DOI | pages | sha256 |",
              "|---|---|---|---|---|---|---|---|---|"]
    for r in records:
        ident = r["arxiv_id"] or r["doi"]
        lines.append(f"| {r['id']} | {r['year']} | {r['population']} | {r['version']} | "
                     f"{r['title']} | {r['venue']} | {ident} | {r['pages']} | `{r['sha256'][:16]}` |")
    lines += ["", "## Relevance to the QuantumLab simulator", ""]
    for r in records:
        lines.append(f"- **{r['id']}** ({r['population']}): {r['relevance']}")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print("wrote:", OUT_JSON)
    print("wrote:", OUT_MD)
    for r in records:
        print(f"  {r['id']:34s} {r['pages']:3d}p  {r['bytes']:>9d}B  {r['population']}")


if __name__ == "__main__":
    main()
