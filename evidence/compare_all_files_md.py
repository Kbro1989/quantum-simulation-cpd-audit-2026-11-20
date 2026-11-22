#!/usr/bin/env python3
"""Compare the ALL-FILES.md (regenerated) against the previous HEAD version.

Usage: python compare_all_files_md.py [REPO]
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")


def git(*args):
    return subprocess.run(
        ["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True
    ).stdout


def entries(text: str) -> set[str]:
    return {ln[2:] for ln in text.splitlines() if ln.startswith("./")}


def main() -> int:
    old_text = git("show", "HEAD:ALL-FILES.md")
    new_text = (REPO / "ALL-FILES.md").read_text(encoding="utf-8")
    old, new = entries(old_text), entries(new_text)
    added = sorted(new - old)
    removed = sorted(old - new)

    print(f"old (HEAD 44f30e3): {len(old)} entries")
    print(f"new (regenerated) : {len(new)} entries")
    print(f"delta             : {len(new) - len(old)}  (new - old)")
    print(f"added             : {len(added)}")
    print(f"removed           : {len(removed)}")
    if added:
        print("\n-- added (first 60) --")
        for p in added[:60]:
            print(" +", p)
        if len(added) > 60:
            print(f"    ... {len(added) - 60} more")
    if removed:
        print("\n-- removed --")
        for p in removed:
            print(" -", p)
    if not added and not removed:
        print("\nno difference")
    return 0


if __name__ == "__main__":
    sys.exit(main())
