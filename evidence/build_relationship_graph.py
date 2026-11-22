#!/usr/bin/env python3
"""Build a function-level producer/consumer relationship graph for quantumlab.

Static AST analysis. Two edge kinds:
  CALL  - a syntactic call site (file:line) resolving to a known repo function/class
  IMPORT- an import relationship (weaker; does not prove runtime use)

Resolution is best-effort and each edge carries a `resolution` field:
  exact   - the callee was resolved to a unique repo definition
  name    - resolved by bare name (may be ambiguous)
  unknown - could not be resolved

Output: cpd_relationship_graph.json
"""
from __future__ import annotations

import ast
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
PKG = REPO / "quantumlab"
OUT = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20\cpd_relationship_graph.json")


def module_of(path: Path) -> str:
    rel = path.relative_to(REPO).with_suffix("")
    parts = list(rel.parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def walk_files(root: Path):
    for p in sorted(root.rglob("*.py")):
        if "__pycache__" in p.parts:
            continue
        yield p


class Visitor(ast.NodeVisitor):
    def __init__(self, path: Path, module: str, index: dict):
        self.path = path
        self.module = module
        self.index = index          # bare name -> list of (module, qualname, kind, line)
        self.nodes = []
        self.edges = []
        self.imports = []
        self.stack = []

    def visit_ClassDef(self, node):
        qual = ".".join(self.stack + [node.name])
        self.nodes.append({"id": f"{self.module}.{qual}", "module": self.module,
                           "name": node.name, "kind": "class",
                           "file": str(self.path.relative_to(REPO)), "line": node.lineno})
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def visit_FunctionDef(self, node):
        qual = ".".join(self.stack + [node.name])
        self.nodes.append({"id": f"{self.module}.{qual}", "module": self.module,
                           "name": node.name, "kind": "method" if self.stack else "function",
                           "file": str(self.path.relative_to(REPO)), "line": node.lineno})
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def visit_Import(self, node):
        for a in node.names:
            self.imports.append({"module": self.module, "target": a.name,
                                 "file": str(self.path.relative_to(REPO)), "line": node.lineno})

    def visit_ImportFrom(self, node):
        mod = node.module or ""
        for a in node.names:
            self.imports.append({"module": self.module, "target": f"{mod}.{a.name}",
                                 "file": str(self.path.relative_to(REPO)), "line": node.lineno})

    # -- calls -------------------------------------------------------------
    def _resolve(self, name: str):
        hits = self.index.get(name, [])
        if not hits:
            return None, "unknown"
        if len(hits) == 1:
            return hits[0], "exact"
        # prefer a hit from the same module
        same = [h for h in hits if h[0] == self.module]
        if len(same) == 1:
            return same[0], "exact"
        return hits[0], "name"

    def visit_Call(self, node):
        parts = []
        cur = node.func
        while isinstance(cur, ast.Attribute):
            parts.append(cur.attr)
            cur = cur.value
        if isinstance(cur, ast.Name):
            parts.append(cur.id)
        parts.reverse()
        if not parts:
            self.generic_visit(node)
            return
        bare = parts[-1]
        hit, conf = self._resolve(bare)
        caller = f"{self.module}." + ".".join(self.stack) if self.stack else self.module
        if hit:
            tgt_module, tgt_qual, kind, line = hit
            self.edges.append({
                "from": caller, "to": f"{tgt_module}.{tgt_qual}",
                "kind": "CALL", "resolution": conf,
                "file": str(self.path.relative_to(REPO)), "line": node.lineno,
                "text": ast.get_source_segment(SRC[self.path], node) or "",
            })
        else:
            self.edges.append({
                "from": caller, "to": bare, "kind": "CALL", "resolution": "unknown",
                "file": str(self.path.relative_to(REPO)), "line": node.lineno,
                "text": ast.get_source_segment(SRC[self.path], node) or "",
            })
        self.generic_visit(node)


SRC: dict = {}


def main() -> int:
    global SRC
    files = list(walk_files(PKG))
    SRC = {p: p.read_text(encoding="utf-8", errors="replace") for p in files}
    modules = {p: module_of(p) for p in files}

    # pass 1: definitions index (bare name -> definitions)
    index = defaultdict(list)
    trees = {}
    for p in files:
        try:
            tree = ast.parse(SRC[p])
        except SyntaxError as exc:
            print(f"  !! parse failure {p.relative_to(REPO)}: {exc}")
            continue
        trees[p] = tree
        mod = modules[p]
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                index[node.name].append((mod, node.name, "function", node.lineno))

    # pass 2: walk with qualification
    all_nodes, all_edges, all_imports = [], [], []
    for p in files:
        if p not in trees:
            continue
        v = Visitor(p, modules[p], index)
        v.visit(trees[p])
        all_nodes.extend(v.nodes)
        all_edges.extend(v.edges)
        all_imports.extend(v.imports)

    # collapse duplicate call edges
    collapsed = {}
    for e in all_edges:
        key = (e["from"], e["to"], e["kind"], e["resolution"])
        collapsed.setdefault(key, {"from": e["from"], "to": e["to"], "kind": e["kind"],
                                    "resolution": e["resolution"], "sites": []})
        collapsed[key]["sites"].append({"file": e["file"], "line": e["line"], "text": e["text"][:120]})
    edges = sorted(collapsed.values(), key=lambda x: (x["from"], x["to"]))

    node_ids = {n["id"] for n in all_nodes}
    calls_from_outside = [e for e in edges if e["from"] not in node_ids]

    graph = {
        "meta": {
            "repo": str(REPO),
            "branch": "remediation/2026-11-20",
            "head": "44f30e30654c064b75f760833741ab55b392ff20",
            "generated": "2026-11-20",
            "method": "static AST; CALL = syntactic call site, IMPORT = import relationship",
            "resolution_legend": {
                "exact": "resolved to a unique repo definition",
                "name": "resolved by bare name; possibly ambiguous",
                "unknown": "could not be resolved",
            },
            "caveat": "Import relationships do NOT prove runtime use. CALL edges are syntactic and "
                      "may include unreached branches. No runtime tracing was performed.",
        },
        "counts": {
            "modules": len(set(modules.values())),
            "nodes": len(all_nodes),
            "call_edges": len([e for e in edges if e["kind"] == "CALL"]),
            "import_edges": len(all_imports),
            "unresolved_calls": len([e for e in edges if e["resolution"] == "unknown"]),
        },
        "nodes": sorted(all_nodes, key=lambda n: n["id"]),
        "edges": edges,
        "imports": sorted(all_imports, key=lambda i: (i["module"], i["target"])),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(graph, indent=2), encoding="utf-8")

    print(f"modules      : {graph['counts']['modules']}")
    print(f"nodes        : {graph['counts']['nodes']}")
    print(f"call edges   : {graph['counts']['call_edges']}")
    print(f"import edges : {graph['counts']['import_edges']}")
    print(f"unresolved   : {graph['counts']['unresolved_calls']}")
    print(f"written      : {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
