#!/usr/bin/env python3
"""Query the CPD relationship graph for the scientifically consequential chains."""
import json
from collections import defaultdict
from pathlib import Path

G = json.loads(Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20\cpd_relationship_graph.json").read_text(encoding="utf-8"))

resolved = [e for e in G["edges"] if e["kind"] == "CALL" and e["resolution"] in ("exact", "name")]

# key scientific names
KEY = ("potential", "evaluate", "step", "step_sequence", "evolve", "solve", "ground_state",
       "vortex", "energy", "norm", "hamiltonian", "grid", "gaussian", "wavefunction",
       "expectation", "current", "momentum", "absorb", "create_potential", "runner",
       "build_grid", "build_solver", "backend", "to_device", "to_host", "total_energy")


def relevant(e):
    blob = (e["from"] + " " + e["to"]).lower()
    return any(k in blob for k in KEY)


sub = [e for e in resolved if relevant(e)]

by_module = defaultdict(list)
for e in sub:
    by_module[e["from"].split(".")[1] if e["from"].count(".") > 1 else e["from"]].append(e)

print("=" * 78)
print("RESOLVED CALL EDGES ON THE SCIENTIFIC CHAIN")
print("=" * 78)
for mod in sorted(by_module):
    print(f"\n### {mod}")
    seen = set()
    for e in by_module[mod]:
        k = (e["from"], e["to"], e["resolution"])
        if k in seen:
            continue
        seen.add(k)
        sites = "; ".join(f"{s['file']}:{s['line']}" for s in e["sites"][:4])
        print(f"  {e['from']:<46} -> {e['to']:<46} [{e['resolution']}] {sites}")

print()
print("=" * 78)
print("NODES WITH NO INCOMING RESOLVED CALL EDGE (nothing calls them, statically)")
print("=" * 78)
incoming = {e["to"] for e in resolved}
outgoing = {e["from"] for e in resolved}
isolated = sorted(n["id"] for n in G["nodes"]
                  if n["id"] not in incoming and n["id"] not in outgoing)
for i in isolated:
    print("  " + i)
print(f"\n  -> {len(isolated)} of {len(G['nodes'])} nodes have no resolved call in or out")
