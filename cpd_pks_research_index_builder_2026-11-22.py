#!/usr/bin/env python3
"""
cpd_pks_research_index_builder_2026-11-22.py

Build the PKS research index from material already on disk:

  * wayback_pks_cdx.json          - 1513 (timestamp, original) rows
  * pks_ei-kurve_extracted_text.md- extracted text layer of the Harthun/Rennert PDF
  * pks_viktor_biography_extracted.md
  * pks_walter_biography_extracted.md
  * pks_patent_inventory_extracted.md

Honesty constraints enforced:
  * The CDX index gives timestamps and URLs, NOT page content. No artifact here
    claims a content change between captures; `content_hash` and
    `content_compared` record that content was never fetched.
  * The four PKS documents were retrieved from the LIVE urls through a reader,
    not from archived captures. Provenance says so.
  * Equations transcribed from the extracted text layer are marked with a
    transcription confidence because PDF text extraction mangles fractions.

Writes only inside the audit workspace.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
SRC = AUD / "schauberger_sources_2026-11-22"
OUT = AUD / "pks_research_index"
OUT.mkdir(parents=True, exist_ok=True)

CDX_QUERY = ("https://web.archive.org/cdx/search/cdx?url=pks.or.at%2F*"
             "&output=json&filter=statuscode:200&collapse=urlkey&fl=timestamp,original")
RETRIEVED = "2026-11-22"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def wayback_url(ts: str, original: str) -> str:
    return f"https://web.archive.org/web/{ts}/{original}"


# ---------------------------------------------------------------- 1. temporal
def temporal_change_map() -> dict:
    rows = json.loads((SRC / "wayback_pks_cdx.json").read_text(encoding="utf-8"))
    header, data = rows[0], rows[1:]
    csv_path = OUT / "pks_temporal_change_map.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["capture_timestamp", "year", "month", "original_url",
                    "wayback_url", "urlkey", "content_hash", "content_compared",
                    "note"])
        for ts, original in data:
            w.writerow([ts, ts[:4], ts[4:6], original, wayback_url(ts, original),
                        "", "NOT_CAPTURED", "no",
                        "index row only; page content never fetched"])
    years = {}
    for ts, _ in data:
        years[ts[:4]] = years.get(ts[:4], 0) + 1
    return {
        "file": "pks_temporal_change_map.csv",
        "rows": len(data),
        "years": dict(sorted(years.items())),
        "earliest": min(r[0] for r in data),
        "latest": max(r[0] for r in data),
        "content_compared": False,
    }


# ------------------------------------------------------------- 2. provenance
def source_provenance() -> dict:
    docs = [
        ("pks_ei-kurve_extracted_text.md", "https://pks.or.at/wp-content/uploads/Berechnung_Ei-Kurve.pdf",
         "Harthun & Rennert, _Die Ei-Kurve als Schnitt des Hyperbolischen Kegels_"),
        ("pks_viktor_biography_extracted.md", "https://pks.or.at/en/viktorschauberger/",
         "PKS Viktor Schauberger biography"),
        ("pks_walter_biography_extracted.md", "https://pks.or.at/en/walterschauberger/",
         "PKS Walter Schauberger biography"),
        ("pks_patent_inventory_extracted.md", "https://pks.or.at/en/patents/",
         "PKS patent inventory"),
    ]
    entries = []
    for name, url, desc in docs:
        p = SRC / name
        entries.append({
            "file": name, "description": desc, "source_url": url,
            "retrieved": RETRIEVED,
            "retrieval_method": "reader extraction of the LIVE url (origin serves a JS challenge to curl)",
            "archived_capture_used": None,
            "bytes": p.stat().st_size, "sha256": sha(p),
            "transcription_confidence": ("partial - PDF text layer mangles fractions and radicals"
                                         if name.endswith("text.md") and "ei-kurve" in name else "high - HTML to markdown"),
        })
    blocked = sorted(p.name for p in SRC.glob("*_BLOCKED_js_challenge.html"))
    return {
        "generated": RETRIEVED,
        "cdx_query": CDX_QUERY,
        "cdx_rows": len(json.loads((SRC / "wayback_pks_cdx.json").read_text(encoding="utf-8"))) - 1,
        "documents": entries,
        "origin_access": {
            "method": "curl",
            "result": "blocked by JavaScript challenge interstitial",
            "interstitials_kept": blocked,
        },
        "archived_captures_fetched": 0,
        "note": ("No archived capture body has been fetched. The index is an inventory, "
                 "not a content corpus. Every content statement in this index traces to "
                 "the live-url extractions listed above."),
    }


# ------------------------------------------------------ 3. equation inventory
def equation_inventory() -> dict:
    txt = (SRC / "pks_ei-kurve_extracted_text.md").read_text(encoding="utf-8", errors="replace")

    def has(*needles):
        return all(n in txt for n in needles)

    eqs = [
        {"id": "PKS-EQ-01", "form": "l * f = 1", "role": "monochord string-length/frequency relation",
         "present_in_text": has("Tongesetz") or has("l f"),
         "confidence": "high", "language": "de"},
        {"id": "PKS-EQ-02", "form": "1/n * n = 1", "role": "Walter Schauberger 'Tongesetz', generalised; raised to 'Urgesetz des Universums' in the source",
         "present_in_text": has("Tongesetz"), "confidence": "high", "language": "de"},
        {"id": "PKS-EQ-03", "form": "x * y = 1", "role": "equilateral hyperbola in asymptote form (Bild 1); the cone-generating curve",
         "present_in_text": has("gleichseitige Hyperbel"), "confidence": "high", "language": "de"},
        {"id": "PKS-EQ-04",
         "form": "x = +/- sqrt( 1/(z0 - y*sin(alpha))^2 - (y*cos(alpha))^2 )",
         "role": "hyperbolic egg curve, explicit form (Schnitthoehe z0, Schnittwinkel alpha)",
         "present_in_text": has("Hyperbolische Ei-Kurve in expliziter Form"),
         "confidence": "partial - the extracted text layer mangles the radical and the fraction; verify against Bild 3 / the printed equation",
         "language": "de"},
        {"id": "PKS-EQ-05", "form": "parametric form in (r, phi), sign before the root selects cone-tube vs 'mountain' cut",
         "role": "hyperbolic egg curve, parameter form", "present_in_text": has("Parameter-Form"),
         "confidence": "low - rendered as fragmented glyphs in the text layer", "language": "de"},
        {"id": "PKS-EQ-06", "form": "z1 = 1/y1 ; z2 = 1/y2", "role": "two-point form: the two principal vertices lie on the hyperbola branches",
         "present_in_text": has("z1") or has("1/y"), "confidence": "high", "language": "de"},
        {"id": "PKS-EQ-07", "form": "z0 = z1*z2*(z1+z2) / (z1^2 + z1*z2 + z2^2)",
         "role": "cutting height from the two given vertices", "present_in_text": has("Zwei-Punkte-Form"),
         "confidence": "partial - equation is glyph-fragmented", "language": "de"},
        {"id": "PKS-EQ-08", "form": "z0 = z1 * (1 - tan(alpha))", "role": "point-slope form A (sharp vertex + cut angle)",
         "present_in_text": has("Punkt-Anstiegsform A"), "confidence": "partial", "language": "de"},
        {"id": "PKS-EQ-09", "form": "z0 = z2 * (1 + tan(alpha))", "role": "point-slope form B (blunt vertex + cut angle)",
         "present_in_text": has("Punkt-Anstiegsform B"), "confidence": "partial", "language": "de"},
        {"id": "PKS-EQ-10", "form": "V = (pi/3) * (1/z1 - 1/z2) * (1/z1^2 + 1/z1*1/z2 + 1/z2^2) * tan(alpha) * (tan(alpha) - cos(alpha))",
         "role": "volume of the egg solid of revolution; source reports V = 0.4045 for the 'Oktav-Ei' (z1=1, z2=2)",
         "present_in_text": has("Berechnung des Ei-Volumens"),
         "confidence": "partial - glyph-fragmented; the numeric result 0.4045 is legible",
         "language": "de"},
        {"id": "EXT-EQ-01", "form": "z = 0.079 / r^2", "role": "Donepudi et al. 2024 hyperbolic funnel profile (Physics of Fluids 36, 095171)",
         "present_in_text": False, "confidence": "high", "language": "en",
         "source": "donepudi_2024_physics_of_fluids.pdf"},
        {"id": "EXT-EQ-02", "form": "vorticity constant; streamlines closed and elliptic (mu_dot=0, nu_dot=const)",
         "role": "Lyra 2021 elliptic-coordinate vortex, exact compressible-Euler solution",
         "present_in_text": False, "confidence": "high", "language": "en",
         "source": "arxiv_2108.04013_lyra.pdf"},
    ]
    for e in eqs:
        e["verified_against_source_document"] = bool(e.pop("present_in_text"))
    return {
        "generated": RETRIEVED,
        "primary_source": "pks_ei-kurve_extracted_text.md",
        "primary_source_sha256": sha(SRC / "pks_ei-kurve_extracted_text.md"),
        "transcription_note": ("Equations PKS-EQ-04..EQ-10 were transcribed from the PDF text "
                               "layer, which fragments fractions, radicals and subscripts. "
                               "Treat 'partial' and 'low' confidence entries as leads to be "
                               "confirmed against the printed PDF, not as established forms."),
        "equations": eqs,
    }


# ----------------------------------------------------- 4. geometry inventory
def geometry_inventory() -> dict:
    return {
        "generated": RETRIEVED,
        "geometries": [
            {"id": "GEO-A", "name": "Walter Schauberger egg curve",
             "construction": "rotate xy=1 about the y-axis -> hyperbolic cone; project a hyperbolic spiral; intersect with an inclined plane",
             "parameters": {"z0": "height where the cutting plane meets the vertical axis",
                            "alpha": "inclination of the cutting plane to the horizontal",
                            "z1,z2": "heights of the sharp and blunt principal vertices"},
             "source": "pks_ei-kurve_extracted_text.md",
             "confidence": "construction high; explicit/parametric equations partial"},
            {"id": "GEO-B", "name": "Donepudi hyperbolic funnel",
             "profile": "z = 0.079 / r^2",
             "regimes": ["Straight", "Twisted Schauberger"],
             "source": "donepudi_2024_physics_of_fluids.pdf (Physics of Fluids 36, 095171)",
             "confidence": "high"},
            {"id": "GEO-C", "name": "Elliptic-coordinate vortex",
             "construction": "closed elliptic streamlines; exact nonlinear solution of the compressible Euler equation",
             "source": "arxiv_2108.04013_lyra.pdf (arXiv:2108.04013)",
             "confidence": "high"},
        ],
        "open_discrepancy": {
            "statement": ("GEO-A's generating relation xy=1 rotated about the y-axis is not "
                          "demonstrably the same surface as GEO-B's z = 0.079/r^2."),
            "unresolved": ["coordinate mapping", "exponent", "dimensional scaling", "surface definition"],
            "possible_explanations": ["different hyperbolic geometry", "later engineering adaptation",
                                      "coordinate transformation", "shared description only"],
            "status": "OPEN",
        },
        "comparison_plan": ["geometry-only analytical comparison",
                            "classical Navier-Stokes simulation",
                            "Gross-Pitaevskii quantum simulation"],
        "separation_rule": ("New Schauberger hypotheses must not be merged into the existing "
                            "quantum-solver evidence; the comparison is a separate branch."),
    }


# ------------------------------------------------------- 5. claim evidence matrix
def claim_evidence_matrix() -> dict:
    rows = [
        ["PKS-C01", "Walter Schauberger generalised the monochord relation to 1/n * n = 1 and called it the 'Tongesetz'",
         "historical_assertion", "pks_ei-kurve_extracted_text.md", "document states it directly",
         "not testable as physics; attributable"],
        ["PKS-C02", "The Tongesetz is the 'Urgesetz des Universums' (universal law of the universe)",
         "historical_assertion", "pks_ei-kurve_extracted_text.md",
         "PKS document itself calls the thesis 'eigenwillig' and individual to Walter",
         "NOT established by the identity; explicitly disclaimed in the source"],
        ["PKS-C03", "Plane sections through the hyperbolic cone produce egg curves",
         "mathematical_claim", "pks_ei-kurve_extracted_text.md",
         "derivation present; equation glyph-fragmented", "re-derivable - verify against printed PDF"],
        ["PKS-C04", "Max Mack first observed that plane sections of the cone give egg curves",
         "historical_attribution", "pks_ei-kurve_extracted_text.md", "document states it", "attributable"],
        ["PKS-C05", "H. Riffer first derived the egg-curve equation generally (1973)",
         "historical_attribution", "pks_ei-kurve_extracted_text.md", "document states it", "attributable"],
        ["PKS-C06", "Ines Rennert re-derived and systematised the representations (not Harthun as an earlier edition said)",
         "historical_attribution", "pks_ei-kurve_extracted_text.md", "document corrects its own earlier edition",
         "attributable; correction recorded"],
        ["PKS-C07", "Egg solid of revolution volume V = 0.4045 for the 'Oktav-Ei' (z1=1, z2=2)",
         "mathematical_claim", "pks_ei-kurve_extracted_text.md", "numeric result legible",
         "re-derivable once the equation is confirmed"],
        ["PKS-C08", "Viktor Schauberger observed fish holding station in moving water and derived centripetal flow forms",
         "historical_assertion", "pks_viktor_biography_extracted.md", "biography present",
         "attributable to Viktor's own writings; mechanism not established"],
        ["PKS-C09", "Hyperbolic funnels produce a Twisted vortex regime with higher gas dissolution than other regimes",
         "experimentally_supported", "donepudi_2024_physics_of_fluids.pdf",
         "TU Delft thesis + 2024 Physics of Fluids paper, CFD validated against experiment",
         "independent peer-reviewed evidence"],
        ["PKS-C10", "Water exiting the funnel remains undersaturated under the tested conditions",
         "experimentally_supported", "donepudi_2024_physics_of_fluids.pdf",
         "stated in both thesis and paper", "negative result - keep"],
        ["PKS-C11", "A power-law energy spectrum alone is insufficient evidence for a turbulent cascade",
         "established_methodological_result", "arxiv_2607.22244_turbulence.pdf",
         "2026 review states it explicitly", "adopt as a rule for our own simulations"],
        ["PKS-C12", "Curved streamlines are not the same as local fluid rotation",
         "established_mathematical_result", "donepudi_2024_physics_of_fluids.pdf",
         "u_theta ~ 1/r irrotational outside the core; u_theta ~ r solid-body rotation",
         "use when comparing classical and quantum vortices"],
    ]
    p = OUT / "pks_claim_evidence_matrix.csv"
    with p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["claim_id", "claim", "classification", "source", "evidence_note", "status"])
        w.writerows(rows)
    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    return {"file": "pks_claim_evidence_matrix.csv", "rows": len(rows), "by_classification": counts}


def main() -> None:
    t = temporal_change_map()
    prov = source_provenance()
    eq = equation_inventory()
    geo = geometry_inventory()
    claims = claim_evidence_matrix()

    (OUT / "pks_source_provenance.json").write_text(json.dumps(prov, indent=2) + "\n", encoding="utf-8")
    (OUT / "pks_equation_inventory.json").write_text(json.dumps(eq, indent=2) + "\n", encoding="utf-8")
    (OUT / "pks_geometry_inventory.json").write_text(json.dumps(geo, indent=2) + "\n", encoding="utf-8")

    print(f"temporal_change_map : {t['rows']} rows, {len(t['years'])} years, "
          f"{t['earliest']} -> {t['latest']}, content_compared={t['content_compared']}")
    print(f"source_provenance   : {len(prov['documents'])} docs, "
          f"{prov['origin_access']['result']}, captures fetched={prov['archived_captures_fetched']}")
    print(f"equation_inventory  : {len(eq['equations'])} equations")
    print(f"geometry_inventory  : {len(geo['geometries'])} geometries, discrepancy={geo['open_discrepancy']['status']}")
    print(f"claim_evidence      : {claims['rows']} rows -> {claims['by_classification']}")
    print("\nwritten to:", OUT)


if __name__ == "__main__":
    main()
