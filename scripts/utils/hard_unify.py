import os
import shutil

ROOT = os.getcwd()

KEEP = {
    "scripts",
    "data",
    "results",
    "figures",
    "tables",
    "manuscript",
    "pipeline",
    "docs"
}

DELETE = [
    "STR_CLEAN",
    "analysis_results",
]

def remove(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("removed:", path)

def main():

    print("HARD UNIFY START")

    # remove junk roots
    for d in DELETE:
        remove(d)

    # remove duplicated / non-standard dirs inside outputs
    bad_outputs = [
        "outputs/intermediate",
        "outputs/logs",
        "outputs/data",
    ]
    for d in bad_outputs:
        remove(d)

    # enforce structure
    for d in KEEP:
        os.makedirs(d, exist_ok=True)

    # create submission-ready anchors
    os.makedirs("figures/main_figures", exist_ok=True)
    os.makedirs("figures/supplementary_figures", exist_ok=True)
    os.makedirs("tables/main_tables", exist_ok=True)
    os.makedirs("tables/supplementary_tables", exist_ok=True)

    with open("REPO_STATUS_FINAL.txt", "w") as f:
        f.write("HARD UNIFIED FOR Q1 SUBMISSION")

    print("DONE")

if __name__ == "__main__":
    main()