import os
import shutil

ROOT = os.getcwd()

def move_if_exists(src, dst_folder):
    if os.path.exists(src):
        os.makedirs(dst_folder, exist_ok=True)
        dst = os.path.join(dst_folder, os.path.basename(src))
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

def main():
    print("START UNIFY")

    # cleanup junk folders if exist
    junk = ["STR_CLEAN", "analysis_results", "outputs/intermediate", "outputs/logs"]
    for j in junk:
        if os.path.exists(j):
            shutil.rmtree(j)
            print("removed:", j)

    # ensure structure
    for d in ["scripts", "data", "results", "figures", "tables", "manuscript"]:
        os.makedirs(d, exist_ok=True)

    print("STRUCTURE OK")

    with open("REPO_STATUS.txt", "w") as f:
        f.write("UNIFIED REPO READY")

    print("DONE")

if __name__ == "__main__":
    main()