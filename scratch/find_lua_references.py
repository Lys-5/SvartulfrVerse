import json
import glob
import os
import re

print("Searching for startup_script or lua in json files...")
for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for f in files:
        if f.endswith(".json"):
            path = os.path.join(root, f)
            try:
                txt = open(path, encoding="utf-8", errors="ignore").read()
                if "startup_script" in txt or "_scenario" in txt or "assignments" in txt:
                    print("Match in:", path)
            except:
                pass
