from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
FIG_DIR = BASE / "scripts" / "figures"

print("===================================")
print("RUNNING ALL FIGURES")
print("===================================")

figures = [
    "make_figure1.py",
    "make_figure2.py",
    "make_figure3.py",
    "make_figure4.py",
    "make_figure5.py",
    "make_figure6A.py",
    "make_figure6B.py",
]

for f in figures:
    path = FIG_DIR / f
    print(f"RUNNING:", f)
    exec(open(path, encoding="utf-8").read())

print("===================================")
print("FIGURES COMPLETE")
print("===================================")