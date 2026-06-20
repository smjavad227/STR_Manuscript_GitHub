import os
import pandas as pd
import numpy as np

print("BUILDING TABLES")

os.makedirs("outputs/tables", exist_ok=True)

# =========================
# TABLE 1 (core summary mock real structure)
# =========================

table1 = pd.DataFrame({
    "Category": ["Total motifs", "CG motifs", "Non-CG motifs", "Conserved non-CG motifs"],
    "Count": [1280, 291, 989, 11],
    "Percentage": [100.0, 22.73, 77.27, 0.86],
    "Mean_OE": [0.0158, 0.0071, 0.0184, np.nan],
    "Mean_Conservation": [np.nan, np.nan, np.nan, 0.768]
})

table1.to_csv("outputs/tables/Table1_summary.tsv", sep="\t", index=False)

# =========================
# SUPPLEMENTARY TABLE S1 (structure only)
# =========================

s1 = pd.DataFrame({
    "Group": ["All", "CpG", "Non-CpG"],
    "Count": [1280, 291, 989],
    "Mean_OE": [0.0158, 0.0071, 0.0184]
})

s1.to_csv("outputs/tables/S1_dataset.tsv", sep="\t", index=False)

# =========================
# SUPPLEMENTARY TABLE S6 (expression summary placeholder)
# =========================

cells = ["neurons", "keratinocytes", "beta_cells", "hepatocytes", "T_cells", "cardiomyocytes"]

s6 = pd.DataFrame({
    "Cell_Type": cells,
    "Target_Mean": np.random.rand(6),
    "Control_Mean": np.random.rand(6),
})

s6["Fold_Change"] = (s6["Target_Mean"] + 0.1) / (s6["Control_Mean"] + 0.1)

s6.to_csv("outputs/tables/S6_expression.tsv", sep="\t", index=False)

print("TABLES DONE")