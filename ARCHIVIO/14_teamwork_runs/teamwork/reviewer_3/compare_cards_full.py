import json
import requests

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
assert r.status_code == 200
live_chars = {c['id']: c for c in r.json().get('characters', [])}

cards = [
    ('Edric Douglas', '_TbRM3EdxDjHFgqztTbCpL', 'FINAL/Edric_Douglas_card.json'),
    ('Erik Ulfr Douglas', '_QPea6g4Q1QfeYCVHCLMPR', 'FINAL/Erik_Douglas_card.json'),
    ('Jasper Svartr Douglas Bloodmoon', '_t4J9aQNJM36cUKAP4wB4U', 'FINAL/Jasper_Douglas_Bloodmoon_card.json'),
    ('Logan Járn Douglas', '_T8Ywcr9FEqNf9JxbK6eHP', 'FINAL/Logan_Douglas_card.json'),
    ('Mackenzie Sanchez-Rogers', '_zn24784jfcchQ7EwCyAnm', 'FINAL/Mackenzie_Sanchez_Rogers_card.json'),
    ('Malachia Björn Douglas Bloodmoon', '_RDfz7XzTpM23LpPALVXHM', 'FINAL/Malachia_Douglas_Bloodmoon_card.json'),
    ('Noah Loki Douglas Bloodmoon', '_zFLUjV8aVxQRAfQxGcAcY', 'FINAL/Noah_Douglas_Bloodmoon_card.json'),
    ('Wulfnic Bóleygr Bloodmoon', '_HEQQbbRFwKdG8QE2Fh1z1', 'FINAL/Wulfnic_Bloodmoon_card.json'),
]

print("="*80)
print("DEEP FIELD-BY-FIELD COMPARISON: LOCAL CARD vs LIVE CARD")
print("="*80)

for name, cid, local_path in cards:
    print(f"\nComparing {name} ({cid})...")
    with open(local_path, 'r', encoding='utf-8') as f:
        loc = json.load(f)
    live = live_chars.get(cid)
    if not live:
        print(f"  CRITICAL: Live card {cid} not found!")
        continue

    # Fields to check
    checked_fields = ['name', 'avatar', 'description', 'personality', 'first_mes', 'mes_example', 'scenario', 'post_history_instructions', 'character_note']
    for k in checked_fields:
        loc_val = loc.get(k, '')
        live_val = live.get(k, '')
        if loc_val != live_val:
            print(f"  MISMATCH on field '{k}':")
            print(f"    Local (len {len(str(loc_val))}): {str(loc_val)[:100]}...")
            print(f"    Live  (len {len(str(live_val))}): {str(live_val)[:100]}...")
        else:
            print(f"  [OK] Field '{k}' is identical (len: {len(str(loc_val))})")
