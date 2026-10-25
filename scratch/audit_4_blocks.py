import json, re

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('===', path, '===')
    missing = 0
    for e in data['lexicon']:
        c = e['content']
        has_b = 'BACKSTORY:' in c
        has_f = ('FAMILY & PACK:' in c) or ('CLAN AND COMPANY:' in c)
        has_v = 'VOICE & BEHAVIOR:' in c
        if not (has_b and has_f and has_v):
            missing += 1
            headers = re.findall(r'^([A-Z][A-Z0-9\s&\'\-\(\)/]+):', c, flags=re.M)
            print(f"{e['entry_id']} | {e['name']} | B={has_b} F={has_f} V={has_v} | headers={headers}")
    print('Total non-strict:', missing)

check_file('FINAL/Svartulfr_NPC_Primary.json')
check_file('FINAL/Svartulfr_NPC_Secondary.json')
