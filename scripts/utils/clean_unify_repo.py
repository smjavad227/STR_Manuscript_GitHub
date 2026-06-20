from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[2]

TO_DELETE = [
    ROOT / "figures",
    ROOT / "figure5_results",
    ROOT / "Figure3_Paper_Submission",
]

for path in TO_DELETE:
    if path.exists():
        shutil.rmtree(path)

str_clean = ROOT / "STR_CLEAN"

if str_clean.exists():
    shutil.rmtree(str_clean)

print("DONE")