import yaml
import os
import logging
import subprocess
from datetime import datetime

CONFIG_PATH = "pipeline/config.yaml"

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

os.makedirs("logs", exist_ok=True)

log_file = f"logs/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run_script(script_path):
    logging.info(f"Running {script_path}")
    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )
    logging.info(result.stdout)
    if result.stderr:
        logging.error(result.stderr)
    print(result.stdout)

# =========================
# REAL PIPELINE STEPS
# =========================

def step1_str_detection():
    run_script("scripts/str_detection/run_trf_scan.py")

def step2_evolutionary_analysis():
    run_script("scripts/evolutionary_analysis/motif_conservation.py")

def step3_expression_analysis():
    run_script("scripts/expression_analysis/cellxgene_analysis.py")

def step4_figures():
    run_script("scripts/figures/build_all_figures.py")

def step5_tables():
    run_script("scripts/statistics/build_tables.py")

# =========================
# RUN ALL
# =========================

if __name__ == "__main__":

    print("PIPELINE STARTED")

    step1_str_detection()
    step2_evolutionary_analysis()
    step3_expression_analysis()
    step4_figures()
    step5_tables()

    print("PIPELINE FINISHED")
    logging.info("Pipeline completed")
import subprocess
subprocess.run(["python", "pipeline/make_submission.py"])