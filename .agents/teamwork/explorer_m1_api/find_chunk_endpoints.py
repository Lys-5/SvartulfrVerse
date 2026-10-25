import glob
import re

for p in glob.glob('scratch/*.js'):
    txt = open(p, encoding='utf-8', errors='ignore').read()
    matches = set(re.findall(r'/api/worlds[a-zA-Z0-9_\-\/]*', txt))
    if matches:
        print(f"=== {p} ===")
        for m in sorted(matches):
            print("  ", m)
