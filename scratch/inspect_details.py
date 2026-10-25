import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

# 1. Inspect scenario field of live_scenario_latest.json
scen = json.loads((ROOT / 'scratch' / 'live_scenario_latest.json').read_text(encoding='utf-8'))
out.append("=== SCENARIO FIELD ===")
out.append(scen.get('scenario', ''))
out.append("======================")

# 2. Inspect entry #24, #55, #97, #99 in Svartulfr_NPC_Primary.json
p1 = json.loads((FINAL / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
for idx, e in enumerate(p1.get('entries', [])):
    name = e.get('name', '')
    if any(k in name.lower() for k in ['russ', 'mackenzie', 'hvit', 'alyssa']):
        out.append(f"\n--- NPC Primary #{idx} ({e.get('id')}): {name} (type={e.get('type')}, keys={e.get('keys')}) ---")
        out.append(e.get('content', ''))

# 3. Inspect Scarlett, Sierra, Stan, Mac, Jasper cards RPG blocks
for fn in ['Scarlett_Rose_card.json', 'Sierra_Cruz_card.json', 'Stan_Davies_Jr_card.json', 'Mackenzie_Sanchez_Rogers_card.json', 'Jasper_Douglas_Bloodmoon_card.json', 'Erik_Douglas_card.json']:
    c = json.loads((FINAL / fn).read_text(encoding='utf-8'))
    desc = c.get('description', '')
    m = re.search(r'(RPG STATS.*)', desc, re.S)
    out.append(f"\n--- {fn} RPG Block ---")
    if m:
        out.append(m.group(1))
    else:
        out.append("NO RPG BLOCK FOUND")

(ROOT / 'scratch' / 'inspect_details_utf8.txt').write_text('\n'.join(out), encoding='utf-8')
print("Done")
