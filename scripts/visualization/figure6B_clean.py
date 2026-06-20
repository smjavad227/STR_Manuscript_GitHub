import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# -----------------------------
# Data
# -----------------------------

x_vals = np.array([189, 15.8, 10.4, 130.6, 34.7])
y_vals = np.array([316, 28.4, 11.8, 239.6, 33.2])

labels = ['Length', 'Period', 'Copies', 'Score', 'Entropy']
markers = ['o', 's', '^', 'D', 'v']

# -----------------------------
# Regression
# -----------------------------

slope, intercept, r_value, p_value, std_err = linregress(x_vals, y_vals)

x_line = np.linspace(0, 380, 100)
y_line = slope * x_line + intercept

# -----------------------------
# Plot
# -----------------------------

fig, ax = plt.subplots(figsize=(8, 7))

for i in range(len(x_vals)):
    ax.scatter(
        x_vals[i],
        y_vals[i],
        s=300,
        marker=markers[i],
        label=labels[i],
        alpha=0.85
    )

# Equality line
ax.plot(
    [0, 380],
    [0, 380],
    linestyle='--',
    linewidth=2,
    alpha=0.6,
    label='y = x'
)

# Regression line
ax.plot(
    x_line,
    y_line,
    linewidth=3,
    alpha=0.85,
    label=f'Regression (R² = {r_value**2:.3f})'
)

# -----------------------------
# Labels
# -----------------------------

ax.set_title(
    "B. Correlation between Chromosome X and Autosomes",
    fontsize=18,
    weight='bold',
    pad=15
)

ax.set_xlabel(
    "Chromosome X (mean value)",
    fontsize=14
)

ax.set_ylabel(
    "Autosomes (mean value)",
    fontsize=14
)

# Stats box
stats_text = (
    f"Pearson r = {r_value:.3f}\n"
    f"p = {p_value:.4f}"
)

ax.text(
    0.05,
    0.95,
    stats_text,
    transform=ax.transAxes,
    fontsize=13,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.9)
)

# Grid
ax.grid(True, linestyle='--', alpha=0.3)

# Legend
ax.legend(fontsize=11)

# Remove top/right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Save
plt.savefig(
    "Figure6B_clean.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()