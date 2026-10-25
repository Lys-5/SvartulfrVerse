import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'

# 1. Backup entry #97 ({{user}} Hvit Douglas Bloodmoon) from Svartulfr_NPC_Primary.json
p1 = json.loads((FINAL / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
for idx, e in enumerate(p1.get('entries', [])):
    if 'Hvit Douglas Bloodmoon' in e.get('name', '') and '{{user}}' in e.get('name', ''):
        (ROOT / 'scratch' / 'archived_npc_primary_97_user_hvit.json').write_text(
            json.dumps(e, indent=2, ensure_ascii=False), encoding='utf-8'
        )
        print(f"Archived entry #{idx}: {e.get('name')}")

# 2. Check Wulfnic 12th outfit encoding in live_wulfnic.json
w_live = json.loads((ROOT / 'scratch' / 'live_wulfnic.json').read_text(encoding='utf-8'))
o12 = w_live['outfits'][-1]
print("Wulfnic 12th outfit repr:", repr(o12['description']))
