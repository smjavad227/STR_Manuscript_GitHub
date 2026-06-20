import os
import logging

print("RUNNING STR DETECTION")

os.makedirs("results", exist_ok=True)

with open("results/str_detection_dummy.txt", "w") as f:
    f.write("STR detection placeholder output\n")

print("STR DETECTION DONE")