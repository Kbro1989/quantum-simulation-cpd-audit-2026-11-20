"""Read-only AST scanner: enumerate producers in target modules and all repo references.
Writes JSON to the audit dir. Never writes inside the repo.
"""
import ast
import json
import os
import sys

REPO = r"C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main"
OUT = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20/_scan.json"

TARGET_FILES = [
    "quantumlab/core/grid.py",
    "quantumlab/core/wavefunction.py",
    "quantumlab/core/absorbing_boundary.py",
    "quantumlab/core/spectral.py",
    "quantumlab/potentials/base.py",
    "quantumlab/potentials/apertures.py",
    "quantumlab/potentials/barriers.py",
    "quantumlab/potentials/coulomb.py",
    "quantumlab/potentials/custom.py",
    "quantumlab/potentials/disorder.py",
    "quantumlab/potentials/oscillator.py",
    "quantumlab/potentials/periodic.py",
    "quantumlab/potentials/time_dependent.py",
    "quantumlab/potentials/traps.py",
    "quantumlab/potentials/wells.py",
    "quantumlab/potentials/__init__.py",
    "quantumlab/solvers/base.py",
    "quantumlab/solvers/backends.py",
    "quantumlab/solvers/multicomponent.py",
    "quantumlab/solvers/split_operator.py",
    "quantumlab/solvers/split_step_1d.py",
    "quantumlab/solvers/split_step_2d.py",
    "quantumlab/solvers/split_step_3d.py",
    "quantumlab/solvers/split_step_3d_gpu.py",
    "quantumlab/solvers/__init__.py",
    "quantumlab/stationary/conjugate_gradient.py",
    "quantumlab/stationary/eigensolver.py",
    "quantumlab/stationary/hamiltonian.py",
    "quantumlab/stationary/imaginary_time.py",
    "quantumlab/stationary/__init__.py",
    "quantumlab/observables/coefficients.py",
    "quantumlab/observables/current.py",
    "quantumlab/observables/expectation.py",
    "quantumlab/observables/momentum.py",
    "quantumlab/observables/nonlinear.py",
    "quantumlab/observables/__init__.py",
    "quantumlab/strongfield.py",
]


def sig_of(node, source_lines):
    """Verbatim def header from lineno up to the line before the body."""
    start = node.lineno - 1
    if getattr(node, "body", None):
        end = node.body[0].lineno - 1
    else:
        end = node.lineno
    lines = source_lines[start:end]
    # strip trailing blank/comment-only lines
    while lines and (lines[-1].strip() == "" or lines[-1].strip().startswith("#")):
        lines.pop()
    return "\n".join(l.rstrip() for l in lines).strip()


def collect(path, source_lines):
    tree = ast.parse("\n".join(source_lines), filename=path)
    defs = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defs.append(dict(module=path, qualname=node.name, kind="function",
                             lineno=node.lineno, signature=sig_of(node, source_lines),
                             decorators=[ast.unparse(d) for d in node.decorator_list]))
        elif isinstance(node, ast.ClassDef):
            defs.append(dict(module=path, qualname=node.name, kind="class",
                             lineno=node.lineno,
                             signature=f"class {node.name}(...):",
                             decorators=[ast.unparse(d) for d in node.decorator_list]))
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    defs.append(dict(module=path, qualname=f"{node.name}.{sub.name}",
                                     kind="method", lineno=sub.lineno,
                                     signature=sig_of(sub, source_lines),
                                     decorators=[ast.unparse(d) for d in sub.decorator_list],
                                     class_name=node.name))
    return defs


def collect_refs(root):
    refs = []  # (name, file, lineno, is_call, line_text)
    imports = []  # (module, name, file, lineno, is_from)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__", ".pytest_cache")]
        for fn in filenames:
            if not fn.endswith(".py"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace("\\", "/")
            try:
                src = open(full, encoding="utf-8").read()
            except Exception:
                continue
            lines = src.splitlines()
            try:
                tree = ast.parse(src, filename=rel)
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Name):
                    refs.append((node.id, rel, node.lineno, False,
                                 lines[node.lineno - 1].strip() if node.lineno - 1 < len(lines) else ""))
                elif isinstance(node, ast.Attribute):
                    refs.append((node.attr, rel, node.lineno, False,
                                 lines[node.lineno - 1].strip() if node.lineno - 1 < len(lines) else ""))
                elif isinstance(node, ast.Call):
                    f = node.func
                    if isinstance(f, ast.Name):
                        refs.append((f.id, rel, node.lineno, True,
                                     lines[node.lineno - 1].strip() if node.lineno - 1 < len(lines) else ""))
                    elif isinstance(f, ast.Attribute):
                        refs.append((f.attr, rel, node.lineno, True,
                                     lines[node.lineno - 1].strip() if node.lineno - 1 < len(lines) else ""))
                elif isinstance(node, ast.ImportFrom):
                    mod = node.module or ""
                    for a in node.names:
                        imports.append((mod, a.name, rel, node.lineno, True))
                elif isinstance(node, ast.Import):
                    for a in node.names:
                        imports.append((a.name, a.asname or a.name, rel, node.lineno, False))
    return refs, imports


def main():
    defs = []
    for rel in TARGET_FILES:
        full = os.path.join(REPO, rel)
        src = open(full, encoding="utf-8").read()
        lines = src.splitlines()
        defs.extend(collect(rel, lines))
    refs, imports = collect_refs(REPO)
    json.dump(dict(defs=defs, refs=refs, imports=imports), open(OUT, "w", encoding="utf-8"), indent=1)
    print("defs", len(defs), "refs", len(refs), "imports", len(imports))


if __name__ == "__main__":
    main()
