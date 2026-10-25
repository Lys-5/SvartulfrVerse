import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

d = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))
for i, e in enumerate(d['lexicon']):
    c = e['content']
    if 'CAMP MYSTIC BACKGROUND & ROLE:' in c:
        continue
    has_b = 'BACKSTORY:' in c
    has_f = ('FAMILY & PACK:' in c) or ('CLAN AND COMPANY:' in c)
    has_v = 'VOICE & BEHAVIOR:' in c
    if not (has_b and has_f and has_v):
        headers = re.findall(r'^([A-Z][A-Z0-9\s&\'\-\(\)/]+):', c, flags=re.M)
        print(f"[{i:3d}] {e['entry_id']} | {e['name']} | B={has_b} F={has_f} V={has_v} | {headers}")
