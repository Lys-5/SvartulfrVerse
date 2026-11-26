import json
import requests

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

lorebooks = [
    ('Svartulfr - Lorebook I', '_gwwCxCfQ6PQaLEjAQVpJL', 'FINAL/Svartulfr_Lorebook_I.json'),
    ('Svartulfr - Lorebook II', '_HfG7TeV6MJyj6bxMwxkpt', 'FINAL/Svartulfr_Lorebook_II.json'),
    ('Svartulfr - Lorebook III', '_9zWTGqYJNJ4BCDMj8gfcD', 'FINAL/Svartulfr_Lorebook_III.json'),
    ('Svartulfr - Location', '_EjXxkmPVhpCXg8xABpFkK', 'FINAL/Svartulfr_Location.json'),
    ('Svartulfr - NPC Primary', '_zwEqgEEzh12X6gHVmMKKC', 'FINAL/Svartulfr_NPC_Primary.json'),
    ('Svartulfr - NPC Secondary', '_Uht3Ckz44JBDrPnUHq7LV', 'FINAL/Svartulfr_NPC_Secondary.json'),
]

print("="*80)
print("COMPARING LIVE LOREBOOKS vs LOCAL FILES")
print("="*80)

for title, lid, local_path in lorebooks:
    r = requests.get(f'https://app.wyvern.chat/api/lorebooks/{lid}', headers=headers)
    if r.status_code != 200:
        print(f"[FAIL] {title} ({lid}): HTTP {r.status_code}")
        continue
    live_lb = r.json()
    live_lexicon = live_lb.get('lexicon', [])
    
    with open(local_path, 'r', encoding='utf-8') as f:
        loc_data = json.load(f)
    loc_entries = loc_data.get('entries', [])
    
    print(f"{title:25} | HTTP {r.status_code} | Live: {len(live_lexicon)} | Local: {len(loc_entries)}")
    if len(live_lexicon) != len(loc_entries):
        print(f"  WARNING: Count mismatch! Live: {len(live_lexicon)} vs Local: {len(loc_entries)}")
    else:
        print(f"  [OK] Counts match exactly ({len(live_lexicon)} entries)")
