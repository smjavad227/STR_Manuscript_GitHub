import os
import numpy as np

print("RUNNING EVOLUTIONARY ANALYSIS")

os.makedirs("results/evolutionary", exist_ok=True)

# dummy real structure (will be replaced with phyloP integration later)

motifs = [f"motif_{i}" for i in range(100)]

conservation = np.random.rand(100)

out_path = "results/evolutionary/motif_conservation.tsv"

with open(out_path, "w") as f:
    f.write("motif\tconservation\n")
    for m, c in zip(motifs, conservation):
        f.write(f"{m}\t{c}\n")

print("EVOLUTIONARY ANALYSIS DONE")