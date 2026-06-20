from pathlib import Path

# =========================
# ROOT PROJECT
# =========================
ROOT = Path(__file__).resolve().parents[1]

# =========================
# OUTPUT STRUCTURE (Q1 STANDARD)
# =========================
FIG_DIR = ROOT / "outputs" / "figures"
TABLE_DIR = ROOT / "outputs" / "tables"
INTERMEDIATE_DIR = ROOT / "outputs" / "intermediate"
DATA_DIR = ROOT / "outputs" / "data"

# =========================
# FIGURE SUBFOLDERS
# =========================
FIG1_DIR = FIG_DIR / "figure1"
FIG2_DIR = FIG_DIR / "figure2"
FIG3_DIR = FIG_DIR / "figure3"
FIG4_DIR = FIG_DIR / "figure4"
FIG5_DIR = FIG_DIR / "figure5"
FIG6_DIR = FIG_DIR / "figure6"

# create all
for d in [FIG1_DIR, FIG2_DIR, FIG3_DIR, FIG4_DIR, FIG5_DIR, FIG6_DIR]:
    d.mkdir(parents=True, exist_ok=True)