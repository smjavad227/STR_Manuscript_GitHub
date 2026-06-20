import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path.cwd()

if not (PROJECT_ROOT / "figure5_results").exists():
    print("Please run this script from the STR_Manuscript_GitHub directory.")
    exit(1)

candidates = {
    "figure5_raw.csv": PROJECT_ROOT / "figure5_results" / "figure5_raw_data.csv",
    "figure5_length_stats.csv": PROJECT_ROOT / "figure5_results" / "figure5_length_statistics.csv",
    "x_vs_autosomes.csv": PROJECT_ROOT / "analysis_results" / "x_vs_autosomes_comparison.csv",
    "supp_table_S2.csv": PROJECT_ROOT / "tables" / "supplementary_tables" / "Supplementary_Table_S2_Top_50_Motifs.csv",
    "complete_conservation.csv": PROJECT_ROOT / "data" / "processed" / "Complete_Multi_Species_Conservation_Data.csv",
    "figure5_length_stats_alt.csv": PROJECT_ROOT / "figure5_results" / "figure5_length_stats.csv",
}

print("Scanning for data files relevant to Figure 5...\n")
for name, path in candidates.items():
    if path.exists():
        print(f"=== Found: {name} ===")
        print(f"Path: {path}")
        df = pd.read_csv(path)
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("First 3 rows:")
        print(df.head(3).to_string())
        print("\n--- Basic statistics for numeric columns ---")
        print(df.describe())
        print("\n" + "="*80 + "\n")
    else:
        print(f"Not found: {name}")

fig5_dir = PROJECT_ROOT / "figure5_results"
if fig5_dir.exists():
    other_csv = list(fig5_dir.glob("*.csv"))
    if other_csv:
        print("Additional CSV files in figure5_results:")
        for f in other_csv:
            if f.name not in candidates.values():
                print(f"  {f.name}")
                df = pd.read_csv(f)
                print(f"    Columns: {list(df.columns)}")
                print(f"    First row: {df.iloc[0].to_dict()}")
    else:
        print("No other CSV files in figure5_results.")
else:
    print("figure5_results directory not found.")