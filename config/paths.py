from pathlib import Path

# =========================
# ROOT PROJECT
# =========================
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# =========================
# INPUT DATA
# =========================
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
ANALYSIS_RESULTS = PROJECT_ROOT / "analysis_results"
TABLES_DIR = PROJECT_ROOT / "tables"

# =========================
# OUTPUT (NEW STANDARD)
# =========================
OUTPUT_DIR = PROJECT_ROOT / "outputs"

FIGURES_DIR = OUTPUT_DIR / "figures"
TABLES_OUT = OUTPUT_DIR / "tables"
INTERMEDIATE = OUTPUT_DIR / "intermediate"

# =========================
# FIGURE OUTPUTS
# =========================
FIG1 = FIGURES_DIR
FIG2 = FIGURES_DIR
FIG3 = FIGURES_DIR
FIG4 = FIGURES_DIR
FIG5 = FIGURES_DIR
FIG6 = FIGURES_DIR

# =========================
# AUTO CREATE FOLDERS
# =========================
for p in [OUTPUT_DIR, FIGURES_DIR, TABLES_OUT, INTERMEDIATE]:
    p.mkdir(parents=True, exist_ok=True)