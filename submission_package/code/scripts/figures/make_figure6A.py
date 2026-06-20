#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reproduce Figure 6A exactly as in the original PNG (no error bars, values on bars).
Data source: analysis_results/x_vs_autosomes_comparison.csv
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "analysis_results" / "x_vs_autosomes_comparison.csv"
OUTPUT_DIR = PROJECT_ROOT / "figures" / "submission_tiff"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)

# Define order and display labels
metrics_order = ["length", "period", "copies", "score", "entropy"]
display_names = {
    "length": "Length (bp)",
    "period": "Period (bp)",
    "copies": "Copy Number",
    "score": "TRF Score",
    "entropy": "Entropy (bits)"
}

# Extract means only (ignore std)
x_means = []
auto_means = []
labels = []

for metric in metrics_order:
    row = df[df["metric"] == metric].iloc[0]
    x_means.append(row["x_mean"])
    auto_means.append(row["auto_mean"])
    labels.append(display_names[metric])

# Plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
fig, ax = plt.subplots(figsize=(8, 5))

x = np.arange(len(labels))
width = 0.35

bars1 = ax.bar(x - width/2, x_means, width, label='Chromosome X', color='#4C72B0', edgecolor='black')
bars2 = ax.bar(x + width/2, auto_means, width, label='Autosomes (chr1,8,19,21)', color='#DD8452', edgecolor='black')

# Add value labels on top of bars
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{height:.1f}', ha='center', va='bottom', fontsize=8)
for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{height:.1f}', ha='center', va='bottom', fontsize=8)

ax.set_ylabel('Value', fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)
ax.legend(fontsize=9)
ax.set_title('A', loc='left', fontweight='bold', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

out_tiff = OUTPUT_DIR / "Figure6A.tiff"
out_png = OUTPUT_DIR / "Figure6A.png"
plt.savefig(out_tiff, dpi=300, format='tiff', bbox_inches='tight')
plt.savefig(out_png, dpi=300, bbox_inches='tight')
print(f"Saved: {out_tiff}")
print(f"Saved: {out_png}")
plt.show()