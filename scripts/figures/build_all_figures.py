import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("BUILDING FIGURES")

os.makedirs("outputs/figures", exist_ok=True)

# =========================
# FIGURE 1 (dummy distribution)
# =========================

fig1 = np.random.lognormal(mean=0, sigma=1, size=1000)

plt.figure()
plt.hist(fig1, bins=50)
plt.title("Figure 1 - STR O/E Distribution (Placeholder)")
plt.savefig("outputs/figures/figure1.png")
plt.close()

# =========================
# FIGURE 2 (scatter)
# =========================

x = np.random.rand(162)
y = np.random.rand(162)

plt.figure()
plt.scatter(x, y)
plt.title("Figure 2 - Depletion vs Conservation (Placeholder)")
plt.savefig("outputs/figures/figure2.png")
plt.close()

# =========================
# FIGURE 3–6 placeholders
# =========================

for i in range(3, 7):
    plt.figure()
    plt.plot(np.random.rand(10))
    plt.title(f"Figure {i} - Placeholder")
    plt.savefig(f"outputs/figures/figure{i}.png")
    plt.close()

print("FIGURES DONE")