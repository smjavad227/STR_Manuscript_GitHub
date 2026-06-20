import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# =========================
# Paths
# =========================
DATA_PATH = "data/processed/Complete_Multi_Species_Conservation_Data.csv"

OUT_PNG = "figures/main_figures/Figure3_Conservation_Heatmap.png"
OUT_TIFF = "figures/submission_tiff/Figure3_Conservation_Heatmap.tiff"

os.makedirs("figures/main_figures", exist_ok=True)
os.makedirs("figures/submission_tiff", exist_ok=True)

# =========================
# Load data
# =========================
df = pd.read_csv(DATA_PATH)

species_cols = ["Human", "Chimpanzee", "Gorilla", "Orangutan", "Macaque"]

for col in species_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================
# Top 50 motifs
# =========================
df_top = df.sort_values("avg_conservation", ascending=False).head(50)

heatmap_data = df_top.set_index("kmer")[species_cols]

# =========================
# Plot
# =========================
plt.figure(figsize=(10, 14))

sns.heatmap(
    heatmap_data,
    cmap="coolwarm",
    linewidths=0.3,
    linecolor="white"
)

plt.title("Figure 3. STR Motif Conservation Across Primate Species", fontsize=12)
plt.xlabel("Species")
plt.ylabel("Motifs")

plt.tight_layout()

# =========================
# Save
# =========================
plt.savefig(OUT_PNG, dpi=300)
plt.savefig(OUT_TIFF, dpi=300)
plt.close()

print("Figure 3 completed successfully")
print("PNG:", OUT_PNG)
print("TIFF:", OUT_TIFF)