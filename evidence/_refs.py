"""Aggregate scanner output into a per-producer reference report (read-only on repo)."""
import json
from collections import defaultdict

AUD = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20"
data = json.load(open(AUD + "/_scan.json", encoding="utf-8"))
defs = data["defs"]
refs = data["refs"]
imports = data["imports"]

# index refs by name
by_name = defaultdict(list)
for name, f, ln, is_call, text in refs:
    by_name[name].append((f, ln, is_call, text))

# index imports by imported name
imp_by_name = defaultdict(list)
for mod, name, f, ln, is_from in imports:
    imp_by_name[name].append((mod, f, ln, is_from))

out = []
for d in defs:
    qn = d["qualname"]
    short = qn.split(".")[-1]
    mod = d["module"]
    ext_calls, ext_other = [], []
    int_calls, int_other = [], []
    for f, ln, is_call, text in by_name.get(short, []):
        if f == mod and ln == d["lineno"]:
            continue  # the def line itself
        entry = (f, ln, text)
        if f == mod:
            (int_calls if is_call else int_other).append(entry)
        else:
            (ext_calls if is_call else ext_other).append(entry)
    imps = imp_by_name.get(short, [])
    out.append(dict(qualname=qn, module=mod, lineno=d["lineno"], kind=d["kind"],
                    signature=d["signature"], decorators=d["decorators"],
                    ext_calls=sorted(set(ext_calls)), ext_other=sorted(set(ext_other)),
                    int_calls=sorted(set(int_calls)), int_other=sorted(set(int_other)),
                    imports=sorted(set((m, f, ln) for m, f, ln, _ in imps))))

with open(AUD + "/_refs.md", "w", encoding="utf-8") as fh:
    for o in out:
        fh.write(f"\n## {o['qualname']}  [{o['module']}:{o['lineno']}] ({o['kind']})\n")
        fh.write(f"SIG: {o['signature']}\n")
        fh.write(f"EXT_CALLS ({len(o['ext_calls'])}):\n")
        for f, ln, t in o["ext_calls"]:
            fh.write(f"  {f}:{ln}: {t}\n")
        fh.write(f"EXT_OTHER ({len(o['ext_other'])}):\n")
        for f, ln, t in o["ext_other"]:
            fh.write(f"  {f}:{ln}: {t}\n")
        fh.write(f"INT_CALLS ({len(o['int_calls'])}): " +
                 ", ".join(f"{f}:{ln}" for f, ln, _ in o["int_calls"]) + "\n")
        fh.write(f"INT_OTHER ({len(o['int_other'])}): " +
                 ", ".join(f"{f}:{ln}" for f, ln, _ in o["int_other"]) + "\n")
        fh.write(f"IMPORTS ({len(o['imports'])}): " +
                 ", ".join(f"{f}:{ln}({m})" for m, f, ln in o["imports"]) + "\n")

json.dump(out, open(AUD + "/_refs.json", "w", encoding="utf-8"), indent=1)
print("wrote", len(out), "producer records")
