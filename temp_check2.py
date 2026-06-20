import pandas as pd

df = pd.read_csv(
    "results/FINAL_evolutionary_forbidden_integration.tsv",
    sep="\t"
)

print("Total:", len(df))

print("\nSpecies count:")
print(df["species_count"].value_counts(dropna=False).sort_index())

print("\nConservation non-null:")
print(df["conservation_score"].notna().sum())

print("\nSpecies >=4:")
print((df["species_count"] >= 4).sum())

print("\nSpecies >=3:")
print((df["species_count"] >= 3).sum())

print("\nStrong+VeryStrong+Extreme:")
print(df[df["significance_level"] != "Moderate"].shape[0])