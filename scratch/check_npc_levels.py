import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

for lb_file in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    for idx, e in enumerate(lb.get('entries', [])):
        c = e.get('content', '')
        age_m = re.search(r'AGE:\s*(\d+)', c)
        lvl_m = re.search(r'\[LEVEL:\s*(\d+)|Level:\s*(\d+)', c, re.I)
        if lvl_m:
            lvl = lvl_m.group(1) or lvl_m.group(2)
            age = age_m.group(1) if age_m else 'N/A'
            if age != 'N/A':
                expected = min(99, int(age))
                if int(lvl) != expected:
                    out.append(f"{lb_file} #{idx} ({e.get('name')}): AGE={age}, LEVEL={lvl} (expected {expected})")
            else:
                out.append(f"{lb_file} #{idx} ({e.get('name')}): AGE=N/A, LEVEL={lvl}")

(ROOT / 'scratch' / 'npc_level_mismatches.txt').write_text('\n'.join(out), encoding='utf-8')
print(f"Found {len(out)} NPC level mismatches")
print('\n'.join(out[:30]))
