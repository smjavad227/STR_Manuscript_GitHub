"""
MASTER FIGURE RUNNER (Q1 CLEAN VERSION)
Runs all figures with unified output structure.
"""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
FIG_DIR = BASE / "outputs" / "figures"

FIG_DIR.mkdir(parents=True, exist_ok=True)

FIG_SCRIPTS = [
    "scripts/figures/make_figure1.py",
    "scripts/figures/make_figure2.py",
    "scripts/figures/make_figure3.py",
    "scripts/figures/make_figure4.py",
    "scripts/figures/make_figure5.py",
    "scripts/figures/make_figure6A.py",
    "scripts/figures/make_figure6B.py",
]

print("\n==============================")
print("RUNNING ALL FIGURES (CLEAN MODE)")
print("==============================\n")

for script in FIG_SCRIPTS:
    path = BASE / script
    if not path.exists():
        print(f"SKIP (missing): {script}")
        continue

    print(f"RUNNING: {script}")
    result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)

print("\n==============================")
print("ALL FIGURES DONE")
print("==============================")