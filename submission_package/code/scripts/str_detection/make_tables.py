from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "analysis_results"
TABLE_DIR = BASE_DIR / "tables" / "final"
TABLE_DIR.mkdir(parents=True, exist_ok=True)

basic_stats = pd.read_csv(DATA_DIR / "basic_statistics.csv")
xvsauto = pd.read_csv(DATA_DIR / "x_vs_autosomes_comparison.csv")

basic_stats.columns = basic_stats.columns.str.strip()

# =========================
# TABLE 1 (FIXED)
# =========================
table1 = pd.DataFrame({
    "Chromosome": basic_stats["chromosome"],
    "Count": basic_stats["length_count"],
    "Mean_Length": basic_stats["length_mean"],
    "Mean_Period": basic_stats["period_mean"],
    "Mean_Copies": basic_stats["copies_mean"]
})

table1.to_csv(TABLE_DIR / "Table1_basic_statistics.csv", index=False)

# =========================
# SUPPLEMENTARY TABLE S1
# =========================
xvsauto.to_csv(TABLE_DIR / "Supplementary_Table_S1_x_vs_autosomes.csv", index=False)

print("Tables generated successfully ? tables/final/")
