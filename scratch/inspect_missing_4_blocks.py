import json
import re

for path, label in [('FINAL/Svartulfr_NPC_Primary.json', 'PRIMARY'), ('FINAL/Svartulfr_NPC_Secondary.json', 'SECONDARY')]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('entries', [])
    print(f'=== {label} ===')
    for idx, e in enumerate(entries):
        if label == 'SECONDARY' and idx >= 111:
            continue
        c = e.get('content', '')
        has_bs = 'BACKSTORY:' in c
        has_fp = ('FAMILY & PACK:' in c) or ('CLAN AND COMPANY:' in c)
        has_vb = 'VOICE & BEHAVIOR:' in c
        if not (has_bs and has_fp and has_vb):
            headers = re.findall(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', c, flags=re.M)
            print(f'[{idx}] {e.get("name")} (id={e.get("id")}) | bs={has_bs}, fp={has_fp}, vb={has_vb}')
            print('   Headers:', headers)
