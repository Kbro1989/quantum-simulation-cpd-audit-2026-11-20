import json
AUD = r"C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20"
d = json.load(open(AUD + "/_refs.json", encoding="utf-8"))
for o in d:
    prod = sorted({f"{f}:{ln}" for f, ln, _ in o["ext_calls"] if not f.startswith("tests/")})
    tests = sorted({f"{f}:{ln}" for f, ln, _ in o["ext_calls"] if f.startswith("tests/")})
    print(f"\n{o['qualname']} [{o['module']}:{o['lineno']}]")
    print("  PROD:", ", ".join(prod) if prod else "-")
    print("  TEST:", ", ".join(tests) if tests else "-")
