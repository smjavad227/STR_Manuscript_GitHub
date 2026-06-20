import pandas as pd

cons = pd.read_csv(
r"D:\My_Projects_Restored\home\javad\projects\Genome_Wide_Laws_Consolidated\Forbidden_STR_Motifs_Paper\02_DATA\INTERMEDIATE\phase4_evolutionary_analysis\results\evolutionary_conservation_analysis\tables\conserved_motifs.csv"
)

forb = pd.read_csv(
r"D:\My_Projects_Restored\home\javad\projects\Genome_Wide_Laws_Consolidated\Forbidden_STR_Motifs_Paper\02_DATA\INTERMEDIATE\phase4_evolutionary_analysis\results\evolutionary_conservation_analysis\tables\forbidden_motifs_candidates.csv"
)

print("\nCONSERVED")
print(cons.shape)
print(cons.columns.tolist())

print("\nFORBIDDEN")
print(forb.shape)
print(forb.columns.tolist())