import pandas as pd

df = pd.read_csv(
    "results/FINAL_evolutionary_forbidden_integration.tsv",
    sep="\t"
)

print(df.columns.tolist())
print(df.shape)
print(df["significance_level"].value_counts())