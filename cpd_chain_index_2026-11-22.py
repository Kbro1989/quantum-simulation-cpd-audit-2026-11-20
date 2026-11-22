#!/usr/bin/env python3
"""
cpd_chain_index_2026-11-22.py

Rebuild the verification-chain index from disk instead of trusting the
certification manifest, and state the Domain-27 producer/consumer contract
with its violations.

Findings this encodes (all reproduced from disk, 2026-11-22):
  * cpd_certification_manifest.json marks 32 files "absent": true. Every one
    of them exists. Two path-convention faults:
      - domains 19-24 and their run logs were listed without the
        `nvidia_validation/` prefix;
      - the probe execution records were looked for under `probes/` but they
        live under `evidence/`.
  * Domain 27 is the only domain listed with correct full paths, so it is the
    only domain that the manifest's own lookup could find.
  * The manifest claims coverage of "72 files, 1,051,846 bytes"; the audit
    directory actually holds ~174 files.
  * Domain 27's producer (physics_integration.py) writes scalar fields while
    its consumer (generate_validation_artifacts.py) reads array fields, and
    that consumer has zero quantumlab imports -- it is outside the usage chain.

Writes only inside the audit workspace.
"""
import hashlib
import json
import re
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
ROOTS = ["probes", "evidence", "validation_artifacts",
         "validation_artifacts_ext", "nvidia_validation"]
SKIP_DIRS = {"__pycache__", ".git"}


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def domain_of(rel: str) -> str:
    m = re.search(r"domain(\d+)", rel)
    if m:
        return f"D{m.group(1)}"
    if re.search(r"probe_E", rel):
        return "D-probe-E"
    if re.search(r"probe_L5", rel):
        return "D-probe-L5"
    return "D-?"


def kind_of(name: str) -> str:
    if name.endswith(".py"):
        return "script"
    if name.endswith((".txt", ".log")):
        return "execution_record"
    if name.endswith((".png", ".gif", ".mp4")):
        return "visual_artifact"
    if name.endswith(".json"):
        return "json_record"
    if name.endswith(".md"):
        return "report"
    if name.endswith(".html"):
        return "viewer"
    return "other"


def build_index() -> dict:
    files = []
    for root in ROOTS:
        base = AUD / root
        if not base.is_dir():
            continue
        for dp, dn, fn in __import__("os").walk(base):
            dn[:] = [d for d in dn if d not in SKIP_DIRS]
            for f in sorted(fn):
                p = Path(dp) / f
                rel = p.relative_to(AUD).as_posix()
                files.append({
                    "path": rel,
                    "domain": domain_of(rel),
                    "kind": kind_of(f),
                    "bytes": p.stat().st_size,
                    "sha256": sha256(p),
                })
    # top-level audit reports/registers are part of the chain too
    for f in sorted(AUD.iterdir()):
        if f.is_file() and f.suffix.lower() in {".md", ".json", ".py", ".txt", ".html"}:
            files.append({
                "path": f.name,
                "domain": domain_of(f.name),
                "kind": kind_of(f.name),
                "bytes": f.stat().st_size,
                "sha256": sha256(f),
            })
    files.sort(key=lambda r: (r["domain"], r["path"]))
    return {"files": files}


def compare_manifest(index: dict) -> list:
    man = json.load(open(AUD / "cpd_certification_manifest.json", encoding="utf-8"))
    by_path = {r["path"]: r for r in index["files"]}
    # also index by leaf name so a wrong-prefix entry can still be resolved
    by_leaf = {}
    for r in index["files"]:
        by_leaf.setdefault(Path(r["path"]).name, []).append(r)

    findings = []
    for e in man["entries"]:
        p = e["path"]
        if e.get("absent"):
            hit = by_path.get(p) or (by_leaf.get(Path(p).name) or [None])[0]
            if hit:
                findings.append({
                    "manifest_path": p,
                    "manifest_claim": "absent",
                    "actual_path": hit["path"],
                    "actual_bytes": hit["bytes"],
                    "fault": ("wrong prefix (nvidia_validation/ missing)"
                              if p.startswith("domain") else
                              "wrong directory (probe records live in evidence/)"),
                })
        else:
            hit = by_path.get(p)
            if hit is None:
                findings.append({"manifest_path": p, "manifest_claim": "present",
                                 "actual_path": None, "fault": "listed present but not on disk"})
            elif hit["sha256"] != e.get("sha256"):
                findings.append({"manifest_path": p, "manifest_claim": "present",
                                 "actual_path": hit["path"], "fault": "sha256 mismatch"})
    return findings


def domain27_contract() -> dict:
    d27 = AUD / "nvidia_validation/domain27_zero_floor"
    phys = json.load(open(d27 / "domain27_zero_floor_physics.json", encoding="utf-8"))
    gen = (d27 / "generate_validation_artifacts.py").read_text(encoding="utf-8", errors="replace")

    def scalar_type(v):
        if isinstance(v, bool): return "bool"
        if isinstance(v, (int, float)): return "scalar"
        if isinstance(v, list): return "array"
        if isinstance(v, dict): return "object"
        return type(v).__name__

    tests = phys.get("tests", {})
    rows = []
    # (test, field, how the generator reads it)
    reads = [
        ("gaussian_tail_decay", "tail_analysis", 'tail.get("tail_analysis", {})'),
        ("vortex_core_density_floor", "core_density.cpu", 'vor.get("core_density", {}).get("cpu")'),
        ("fft_numerical_zeros", "fft_normalization", 'fft.get("fft_normalization", [])'),
        ("fft_numerical_zeros", "relative_l2_error", 'fft.get("relative_l2_error", [])'),
        ("gaussian_current_evolution", "cpu_center_variance", 'gauss.get("cpu_center_variance", [])'),
        ("gaussian_current_evolution", "gpu_center_variance", 'gauss.get("gpu_center_variance", [])'),
        ("gaussian_current_evolution", "cpu_center", 'gauss.get("cpu_center", [])'),
        ("gaussian_current_evolution", "gpu_center", 'gauss.get("gpu_center", [])'),
        ("energy_threshold_with_zero_floor", "cpu_energy", 'energy.get("cpu_energy", [])'),
        ("energy_threshold_with_zero_floor", "gpu_energy", 'energy.get("gpu_energy", [])'),
        ("energy_threshold_with_zero_floor", "classification_counts", 'energy.get("classification_counts", {})'),
    ]
    for test, field, how in reads:
        node = tests.get(test)
        if node is None:
            rows.append({"test": test, "field": field, "present_in_json": False,
                         "actual_type": None, "consumer_read": how,
                         "violation": "test block absent from producer output"})
            continue
        cur = node
        for part in field.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                cur = None
                break
        actual = scalar_type(cur) if cur is not None else None
        expects_array = "[]" in how
        violation = ""
        if cur is None:
            violation = "field absent from producer output"
        elif expects_array and actual != "array":
            violation = f"consumer defaults to array, producer wrote {actual}"
        elif (not expects_array) and actual == "array":
            violation = f"consumer expects scalar, producer wrote {actual}"
        rows.append({"test": test, "field": field, "present_in_json": True,
                     "actual_type": actual, "consumer_read": how, "violation": violation})

    gen_imports = sorted(set(re.findall(r'(?:from|import)\s+(quantumlab[\w\.]*)', gen)))
    return {
        "producer": "nvidia_validation/domain27_zero_floor/physics_integration.py",
        "consumer": "nvidia_validation/domain27_zero_floor/generate_validation_artifacts.py",
        "consumer_quantumlab_imports": gen_imports,
        "consumer_in_usage_chain": bool(gen_imports),
        "field_contract": rows,
        "violation_count": sum(1 for r in rows if r["violation"]),
    }


def main() -> None:
    index = build_index()
    findings = compare_manifest(index)
    contract = domain27_contract()

    out = {
        "index": "cpd_verification_chain_index_2026-11-22",
        "generated": "2026-11-22",
        "audit_dir": str(AUD),
        "roots": ROOTS,
        "file_count": len(index["files"]),
        "total_bytes": sum(r["bytes"] for r in index["files"]),
        "domains_present": sorted({r["domain"] for r in index["files"]}),
        "files": index["files"],
        "manifest_comparison": {
            "manifest_coverage_claim": "72 files, 1,051,846 bytes",
            "actual_file_count": len(index["files"]),
            "actual_total_bytes": sum(r["bytes"] for r in index["files"]),
            "false_absent_count": len(findings),
            "findings": findings,
        },
        "domain27_contract": contract,
    }
    p = AUD / "cpd_verification_chain_index_2026-11-22.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    print(f"files indexed: {len(index['files'])}  bytes: {out['total_bytes']}")
    print(f"domains: {out['domains_present']}")
    print(f"false-absent findings: {len(findings)}")
    for f in findings[:6]:
        print(f"   {f['manifest_path']}  ->  {f['actual_path']}  [{f['fault']}]")
    print(f"domain27 contract violations: {contract['violation_count']} / {len(contract['field_contract'])}")
    for r in contract["field_contract"]:
        if r["violation"]:
            print(f"   {r['test']}.{r['field']}: {r['violation']}")
    print("written:", p)


if __name__ == "__main__":
    main()
