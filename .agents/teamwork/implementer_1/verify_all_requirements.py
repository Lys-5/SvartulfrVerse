import json
import requests
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

print("======================================================================")
print("COMPREHENSIVE AUDIT OF REQUIREMENTS R1, R2, R3")
print("======================================================================")

# 1. Check Memory Entries in Lorebook I and II
print("\n--- R1.3: Checking Memory Entries in Lorebook I & II ---")
for lb_fname in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json']:
    lb_path = ROOT / 'FINAL' / lb_fname
    if not lb_path.exists():
        print(f"ERROR: {lb_path} not found!")
        continue
    with open(lb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('lexicon', [])
    memories = [e for e in entries if e.get('type') == 'memory']
    bad_memories = [e for e in memories if e.get('ignored_characters')]
    print(f"{lb_fname}: Total entries={len(entries)}, Memory entries={len(memories)}, Bad with ignored_characters={len(bad_memories)}")
    for bm in bad_memories:
        print(f"  [BAD] {bm.get('name')}: {bm.get('ignored_characters')}")

# Also check live Lorebook I & II
print("\n--- Live Lorebook I & II Memory Check ---")
for lb_id, name in [('_gwwCxCfQ6PQaLEjAQVpJL', 'Lorebook I'), ('_HfG7TeV6MJyj6bxMwxkpt', 'Lorebook II')]:
    r = requests.get(f'https://app.wyvern.chat/api/lorebooks/{lb_id}', headers=headers)
    if r.status_code == 200:
        data = r.json()
        entries = data.get('lexicon', [])
        memories = [e for e in entries if e.get('type') == 'memory']
        bad = [e for e in memories if e.get('ignored_characters')]
        print(f"Live {name} ({lb_id}): Total={len(entries)}, Memories={len(memories)}, Bad with ignored_chars={len(bad)}")
    else:
        print(f"Live {name} fetch failed: {r.status_code}")

# 2. Check 8 Cards Descriptions vs Lorebook Content (Local & Live)
print("\n--- R1.1 & R1.2: Check 8 Cards Descriptions & ignored_characters ---")
TARGET_CARDS = {
    'Edric': {
        'name': 'Edric Douglas',
        'cid': '_TbRM3EdxDjHFgqztTbCpL',
        'file': 'FINAL/Edric_Douglas_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Secondary.json',
        'lb_id': '_Uht3Ckz44JBDrPnUHq7LV',
        'lb_type': 'Secondary'
    },
    'Erik': {
        'name': 'Erik Ulfr Douglas',
        'cid': '_QPea6g4Q1QfeYCVHCLMPR',
        'file': 'FINAL/Erik_Douglas_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    },
    'Jasper': {
        'name': 'Jasper Svartr Douglas Bloodmoon',
        'cid': '_t4J9aQNJM36cUKAP4wB4U',
        'file': 'FINAL/Jasper_Douglas_Bloodmoon_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    },
    'Logan': {
        'name': 'Logan Járn Douglas',
        'cid': '_T8Ywcr9FEqNf9JxbK6eHP',
        'file': 'FINAL/Logan_Douglas_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    },
    'Mackenzie': {
        'name': 'Mackenzie Sanchez-Rogers',
        'cid': '_zn24784jfcchQ7EwCyAnm',
        'file': 'FINAL/Mackenzie_Sanchez_Rogers_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    },
    'Malachia': {
        'name': 'Malachia Björn Douglas Bloodmoon',
        'cid': '_RDfz7XzTpM23LpPALVXHM',
        'file': 'FINAL/Malachia_Douglas_Bloodmoon_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    },
    'Noah': {
        'name': 'Noah Loki Douglas Bloodmoon',
        'cid': '_zFLUjV8aVxQRAfQxGcAcY',
        'file': 'FINAL/Noah_Douglas_Bloodmoon_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    },
    'Wulfnic': {
        'name': 'Wulfnic Bóleygr Bloodmoon',
        'cid': '_HEQQbbRFwKdG8QE2Fh1z1',
        'file': 'FINAL/Wulfnic_Bloodmoon_card.json',
        'lb': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_id': '_zwEqgEEzh12X6gHVmMKKC',
        'lb_type': 'Primary'
    }
}

for key, info in TARGET_CARDS.items():
    cpath = ROOT / info['file']
    with open(cpath, 'r', encoding='utf-8') as f:
        cdata = json.load(f)
    card_desc = cdata.get('description', '')
    
    lbpath = ROOT / info['lb']
    with open(lbpath, 'r', encoding='utf-8') as f:
        lbdata = json.load(f)
        
    found_entry = None
    for e in lbdata.get('lexicon', []):
        if info['cid'] in e.get('ignored_characters', []):
            found_entry = e
            break
        if e.get('name') == info['name']:
            found_entry = e
            break
            
    if not found_entry:
        print(f"[FAIL] Local Lorebook entry not found for {key}")
        continue
        
    entry_desc = found_entry.get('content', '')
    desc_match = (card_desc == entry_desc)
    ignored_ok = (info['cid'] in found_entry.get('ignored_characters', []))
    print(f"LOCAL {key:10}: Desc match={desc_match} (Card:{len(card_desc)} / Entry:{len(entry_desc)}), ignored_chars OK={ignored_ok} ({found_entry.get('ignored_characters')})")

print("\n--- Live 8 Cards vs Live Lorebooks Check ---")
r_mine = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
live_chars = {c['id']: c for c in r_mine.json().get('characters', [])} if r_mine.status_code == 200 else {}

r_prim = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
live_prim_lex = r_prim.json().get('lexicon', []) if r_prim.status_code == 200 else []

r_sec = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
live_sec_lex = r_sec.json().get('lexicon', []) if r_sec.status_code == 200 else []

for key, info in TARGET_CARDS.items():
    lc = live_chars.get(info['cid'])
    live_desc = lc.get('description', '') if lc else ''
    
    lex = live_prim_lex if info['lb_type'] == 'Primary' else live_sec_lex
    found = None
    for e in lex:
        if info['cid'] in e.get('ignored_characters', []):
            found = e
            break
        if e.get('name') == info['name']:
            found = e
            break
            
    if not found:
        print(f"[FAIL] Live Lorebook entry not found for {key}")
        continue
        
    ldesc = found.get('content', '')
    d_match = (live_desc == ldesc)
    ign_ok = (info['cid'] in found.get('ignored_characters', []))
    print(f"LIVE  {key:10}: Live Desc match={d_match} (LiveCard:{len(live_desc)} / LiveEntry:{len(ldesc)}), ignored_chars OK={ign_ok} ({found.get('ignored_characters')})")
