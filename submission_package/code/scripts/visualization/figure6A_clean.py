import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Data
# -----------------------------

features = [
    "Length\n(bp)",
    "Period\n(bp)",
    "Copy\nNumber",
    "TRF\nScore",
    "Entropy\n(bits)"
]

chrX = [189, 15.8, 10.4, 130.6, 34.7]
autosomes = [316, 28.4, 11.8, 239.6, 33.2]

# -----------------------------
# Plot
# -----------------------------

x = np.arange(len(features))
width = 0.36

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width/2,
    chrX,
    width,
    label='Chromosome X',
    alpha=0.85
)

bars2 = ax.bar(
    x + width/2,
    autosomes,
    width,
    label='Autosomes\n(chr1,8,19,21)',
    alpha=0.85
)

# -----------------------------
# Labels
# -----------------------------

ax.set_title(
    "A. Comparison of STR Characteristics: Chromosome X vs Autosomes",
    fontsize=16,
    weight='bold',
    pad=15
)

ax.set_ylabel("Mean Value", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(features, fontsize=12)

ax.legend(fontsize=12)

# Grid
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Remove top/right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# -----------------------------
# Value labels
# -----------------------------

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f'{height:.1f}',
            ha='center',
            va='bottom',
            fontsize=10
        )

plt.tight_layout()

# Save
plt.savefig(
    "Figure6A_clean.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()