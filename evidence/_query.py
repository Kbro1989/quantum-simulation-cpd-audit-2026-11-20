import json, sys
AUD = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20"
d = json.load(open(AUD + "/_refs.json", encoding="utf-8"))
want = sys.argv[1:]
for o in d:
    if o["qualname"] in want or o["qualname"].split(".")[-1] in want:
        print(f"\n=== {o['qualname']} ({o['module']}:{o['lineno']}) kind={o['kind']}")
        print("  EXT_CALLS:")
        for f, ln, t in o["ext_calls"]:
            print(f"    {f}:{ln}: {t}")
        print("  EXT_OTHER:")
        for f, ln, t in o["ext_other"]:
            print(f"    {f}:{ln}: {t}")
        print("  INT_CALLS:", ", ".join(f"{f}:{ln}" for f, ln, _ in o["int_calls"]))
        print("  INT_OTHER:", ", ".join(f"{f}:{ln}" for f, ln, _ in o["int_other"]))
        print("  IMPORTS:", ", ".join(f"{f}:{ln}({m})" for m, f, ln in o["imports"]))
