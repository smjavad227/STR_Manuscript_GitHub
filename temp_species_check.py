import pandas as pd

df = pd.read_csv(
r"D:\My_Projects_Restored\home\javad\projects\Genome_Wide_Laws_Consolidated\Forbidden_STR_Motifs_Paper\02_DATA\INTERMEDIATE\phase4_evolutionary_analysis\results\evolutionary_conservation_analysis\tables\conserved_motifs.csv"
)

print(df.head(20))

print("\nUNIQUE SPECIES VALUES:\n")
print(df["species"].head(20))