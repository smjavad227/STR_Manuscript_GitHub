import os
import shutil

print("BUILDING SUBMISSION PACKAGE")

base = "submission_package"

def safe_copy_file(src, dst_dir):
    if os.path.isfile(src):
        try:
            shutil.copy2(src, dst_dir)
        except Exception as e:
            print(f"[SKIP FILE] {src} -> {e}")

def safe_copy_dir(src, dst):
    if os.path.exists(src):
        try:
            shutil.copytree(src, dst, dirs_exist_ok=True)
        except Exception as e:
            print(f"[SKIP DIR] {src} -> {e}")

folders = [
    f"{base}/figures",
    f"{base}/tables",
    f"{base}/code/pipeline",
    f"{base}/code/scripts",
    f"{base}/results",
    f"{base}/logs"
]

for f in folders:
    os.makedirs(f, exist_ok=True)

src_fig = "outputs/figures"
dst_fig = f"{base}/figures"

if os.path.exists(src_fig):
    for item in os.listdir(src_fig):
        src_path = os.path.join(src_fig, item)
        if os.path.isdir(src_path):
            safe_copy_dir(src_path, os.path.join(dst_fig, item))
        else:
            safe_copy_file(src_path, dst_fig)

src_tab = "outputs/tables"
dst_tab = f"{base}/tables"

if os.path.exists(src_tab):
    for item in os.listdir(src_tab):
        src_path = os.path.join(src_tab, item)
        if os.path.isdir(src_path):
            safe_copy_dir(src_path, os.path.join(dst_tab, item))
        else:
            safe_copy_file(src_path, dst_tab)

safe_copy_dir("results", f"{base}/results")
safe_copy_dir("pipeline", f"{base}/code/pipeline")
safe_copy_dir("scripts", f"{base}/code/scripts")

for rf in ["README.md", "requirements.txt", "pipeline/run_all.py"]:
    if os.path.exists(rf):
        safe_copy_file(rf, f"{base}/code")

print("SUBMISSION PACKAGE READY (CLEAN)")