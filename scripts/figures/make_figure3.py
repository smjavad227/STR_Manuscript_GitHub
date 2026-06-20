#!/usr/bin/env python3

import sys
import subprocess
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PROJECT ROOT
# =========================
BASE = Path(__file__).resolve().parents[2]

# Ensure project root is importable (fixes config module errors)
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))

# =========================
# INPUT FILES (ROBUST)
# =========================
PRIMARY_INPUT = BASE / "data" / "submission" / "Figure3_FullData.csv"
FALLBACK_INPUT = BASE / "data" / "submission" / "Figure3_Data.csv"

INPUT_FILE = PRIMARY_INPUT if PRIMARY_INPUT.exists() else FALLBACK_INPUT

# fallback script
FALLBACK_SCRIPT = BASE / "scripts" / "figures" / "make_figure3_conservation_heatmap.py"

# =========================
# OUTPUT DIRECTORIES
# =========================
OUT_MAIN = BASE / "figures" / "main_figures"
OUT_SUB = BASE / "figures" / "submission_tiff"

OUT_MAIN.mkdir(parents=True, exist_ok=True)
OUT_SUB.mkdir(parents=True, exist_ok=True)

# =========================
# FALLBACK MODE
# =========================
if not INPUT_FILE.exists():
    print("Figure3 fallback mode activated")

    if FALLBACK_SCRIPT.exists():
        subprocess.run([sys.executable, str(FALLBACK_SCRIPT)], check=True)
    else:
        print("ERROR: fallback script not found")
    sys.exit(0)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv(INPUT_FILE)

required_cols = {"avg_conservation", "kmer"}
if not required_cols.issubset(df.columns):
    missing = required_cols - set(df.columns)
    print(f"ERROR: missing columns: {missing}")
    sys.exit(1)

species = ["Human", "Chimpanzee", "Gorilla", "Orangutan", "Macaque"]
valid_species = [s for s in species if s in df.columns]

# =========================
# PROCESS
# =========================
df = df.dropna(subset=["avg_conservation"])
top50 = df.nlargest(50, "avg_conservation").reset_index(drop=True)

# =========================
# PLOT
# =========================
fig, ax = plt.subplots(figsize=(3.6, 4.2))

im = ax.imshow(
    top50[valid_species].values,
    cmap="RdYlBu_r",
    aspect="auto"
)

cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label("Conservation Score")

ax.set_xticks(range(len(valid_species)))
ax.set_xticklabels(valid_species, rotation=45, ha="right")

ax.set_yticks(range(len(top50)))
ax.set_yticklabels(top50["kmer"].astype(str), fontsize=6)

ax.set_xlabel("Species")
ax.set_ylabel("Motif")
ax.set_title("Conservation of Depleted Motifs Across Primate Species")

plt.tight_layout()

# =========================
# SAVE OUTPUT
# =========================
png_path = OUT_MAIN / "Figure3_Conservation_Heatmap.png"
tiff_path = OUT_SUB / "Figure3_Conservation_Heatmap.tiff"

plt.savefig(png_path, dpi=600, bbox_inches="tight")
plt.savefig(tiff_path, dpi=600, format="tiff", bbox_inches="tight")

plt.close()

print(f"Saved PNG: {png_path}")
print(f"Saved TIFF: {tiff_path}")