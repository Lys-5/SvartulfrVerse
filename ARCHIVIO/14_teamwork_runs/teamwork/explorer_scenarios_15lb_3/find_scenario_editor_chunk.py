import glob
import re

for p in glob.glob(r'e:\repository\SvartulfrVerse\scratch\*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
        if 'Character Scenario' in t or 'character-scenario' in t or 'scenario_id' in t:
            for m in re.finditer(r'character-scenario', t, re.IGNORECASE):
                pos = m.start()
                print(f"=== {p} at {pos} ===")
                print(t[max(0, pos-150):min(len(t), pos+300)])
                print()
