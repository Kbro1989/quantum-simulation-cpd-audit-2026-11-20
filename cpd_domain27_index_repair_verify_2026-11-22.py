#!/usr/bin/env python3
"""
cpd_domain27_index_repair_verify_2026-11-22.py

Regenerates nvidia_validation/domain27_zero_floor/validation_index.html using the
fixed create_validation_index() (href and src now carry the parent directory), then
verifies every referenced path resolves to a real file on disk.

Read-only apart from rewriting validation_index.html.
"""
import importlib.util
import os
import re
import sys
from pathlib import Path

AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
D27 = AUD / "nvidia_validation" / "domain27_zero_floor"
GEN = D27 / "generate_validation_artifacts.py"
HTML = D27 / "validation_index.html"

sys.path.insert(0, str(D27))
spec = importlib.util.spec_from_file_location("gen_d27", GEN)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

before = HTML.read_text(encoding="utf-8") if HTML.exists() else ""
before_refs = re.findall(r'(?:href|src)="([^"]+)"', before)

out = mod.create_validation_index()
print("regenerated:", out)

html = HTML.read_text(encoding="utf-8")
refs = re.findall(r'(?:href|src)="([^"]+)"', html)
print(f"references in index: {len(refs)} (was {len(before_refs)})")

broken_before = [r for r in before_refs if not (D27 / r).exists()]
broken_after = [r for r in refs if not (D27 / r).exists()]

print(f"\nbroken BEFORE: {len(broken_before)}")
for r in broken_before:
    print("   ", r)
print(f"broken AFTER:  {len(broken_after)}")
for r in broken_after:
    print("   ", r)

# structural check: every ref must be test_dir/filename
bad_shape = [r for r in refs if "/" not in r]
print(f"\nrefs missing parent dir: {len(bad_shape)}")
for r in bad_shape:
    print("   ", r)

ok = not broken_after and not bad_shape
print("\nVERDICT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
