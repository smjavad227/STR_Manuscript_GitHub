#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

# ----------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_FILE = PROJECT_ROOT / "analysis_results" / "x_vs_autosomes_comparison.csv"
OUTPUT_DIR = PROJECT_ROOT / "figures" / "submission_tiff"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PNG = OUTPUT_DIR / "Figure6B.png"
OUTPUT_TIFF = OUTPUT_DIR / "Figure6B.tiff"

# ----------------------------------------------------------------------
# Load Data (SAFE)
# ----------------------------------------------------------------------
if not DATA_FILE.exists():
    raise FileNotFoundError(f"Missing input file: {DATA_FILE}")

df = pd.read_csv(DATA_FILE)

required_cols = {"metric", "x_mean", "auto_mean"}
if not required_cols.issubset(df.columns):
    raise ValueError(f"Missing required columns. Found: {df.columns}")

# ----------------------------------------------------------------------
# Define expected metrics
# ----------------------------------------------------------------------
metrics = ["length", "period", "copies", "score", "entropy"]
labels = ["Length", "Period", "Copies", "Score", "Entropy"]
markers = ['o', 's', '^', 'D', 'v']
colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#9378B2']

# ----------------------------------------------------------------------
# Filter + Align data safely
# ----------------------------------------------------------------------
df = df[df["metric"].isin(metrics)].copy()
df = df.set_index("metric").reindex(metrics)

x_vals = pd.to_numeric(df["x_mean"], errors="coerce").values
y_vals = pd.to_numeric(df["auto_mean"], errors="coerce").values

# Remove NaNs
mask = ~np.isnan(x_vals) & ~np.isnan(y_vals)
x_vals = x_vals[mask]
y_vals = y_vals[mask]

if len(x_vals) < 2:
    raise ValueError(f"Not enough valid data points for Figure6B: {len(x_vals)}")

# ----------------------------------------------------------------------
# Regression + Stats
# ----------------------------------------------------------------------
x_vals_2d = x_vals.reshape(-1, 1)

reg = LinearRegression().fit(x_vals_2d, y_vals)
r2 = reg.score(x_vals_2d, y_vals)

r_val, p_val = pearsonr(x_vals, y_vals)

x_line = np.linspace(min(x_vals), max(x_vals), 100)
y_line = reg.predict(x_line.reshape(-1, 1))

# ----------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 8))

for i in range(len(x_vals)):
    ax.scatter(
        x_vals[i],
        y_vals[i],
        color=colors[i % len(colors)],
        marker=markers[i % len(markers)],
        s=250,
        label=labels[i] if i < len(labels) else f"Metric {i+1}",
        zorder=3
    )

ax.plot(
    x_line, y_line,
    color='#F79646',
    linewidth=3,
    label=f'Regression (R² = {r2:.3f})',
    zorder=2
)

ax.plot(
    x_line, x_line,
    color='#85A5C4',
    linestyle='--',
    linewidth=3,
    label='y = x',
    zorder=1
)

# ----------------------------------------------------------------------
# Formatting
# ----------------------------------------------------------------------
ax.set_title(
    'B. Correlation between Chromosome X and Autosomes',
    fontsize=18,
    fontweight='bold',
    pad=15
)

ax.set_xlabel('Chromosome X (mean value)', fontsize=14)
ax.set_ylabel('Autosomes (mean value)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Annotation
text_str = f"Pearson r = {r_val:.3f}\np = {p_val:.4g}"
ax.text(
    0.05, 0.95,
    text_str,
    transform=ax.transAxes,
    fontsize=13,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='white', edgecolor='black')
)

ax.legend(loc='lower right', fontsize=11)

plt.tight_layout()

# ----------------------------------------------------------------------
# Save (SAFE + LOG)
# ----------------------------------------------------------------------
plt.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight")
plt.savefig(OUTPUT_TIFF, dpi=300, format='tiff', bbox_inches="tight")

print("Figure6B saved successfully:")
print("  PNG :", OUTPUT_PNG)
print("  TIFF:", OUTPUT_TIFF)

plt.close()