import json
import os
import requests

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

# 1. Fetch live data
print("Fetching live data...")
res_mine = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
assert res_mine.status_code == 200
live_mine = res_mine.json().get('characters', [])
live_mine_by_id = {c['id']: c for c in live_mine}

res_lb1 = requests.get('https://app.wyvern.chat/api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL', headers=headers)
assert res_lb1.status_code == 200
live_lb1 = res_lb1.json()

res_lb2 = requests.get('https://app.wyvern.chat/api/lorebooks/_HfG7TeV6MJyj6bxMwxkpt', headers=headers)
assert res_lb2.status_code == 200
live_lb2 = res_lb2.json()

res_lb_prim = requests.get('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
assert res_lb_prim.status_code == 200
live_lb_prim = res_lb_prim.json()

res_lb_sec = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
assert res_lb_sec.status_code == 200
live_lb_sec = res_lb_sec.json()

# 2. Local files
cards_config = [
    {
        'name': 'Edric Douglas',
        'cid': '_TbRM3EdxDjHFgqztTbCpL',
        'card_file': 'FINAL/Edric_Douglas_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Secondary.json',
        'lb_live': live_lb_sec,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public'
    },
    {
        'name': 'Erik Ulfr Douglas',
        'cid': '_QPea6g4Q1QfeYCVHCLMPR',
        'card_file': 'FINAL/Erik_Douglas_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public'
    },
    {
        'name': 'Jasper Svartr Douglas Bloodmoon',
        'cid': '_t4J9aQNJM36cUKAP4wB4U',
        'card_file': 'FINAL/Jasper_Douglas_Bloodmoon_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public'
    },
    {
        'name': 'Logan Járn Douglas',
        'cid': '_T8Ywcr9FEqNf9JxbK6eHP',
        'card_file': 'FINAL/Logan_Douglas_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public'
    },
    {
        'name': 'Mackenzie Sanchez-Rogers',
        'cid': '_zn24784jfcchQ7EwCyAnm',
        'card_file': 'FINAL/Mackenzie_Sanchez_Rogers_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public'
    },
    {
        'name': 'Malachia Björn Douglas Bloodmoon',
        'cid': '_RDfz7XzTpM23LpPALVXHM',
        'card_file': 'FINAL/Malachia_Douglas_Bloodmoon_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public'
    },
    {
        'name': 'Noah Loki Douglas Bloodmoon',
        'cid': '_zFLUjV8aVxQRAfQxGcAcY',
        'card_file': 'FINAL/Noah_Douglas_Bloodmoon_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public'
    },
    {
        'name': 'Wulfnic Bóleygr Bloodmoon',
        'cid': '_HEQQbbRFwKdG8QE2Fh1z1',
        'card_file': 'FINAL/Wulfnic_Bloodmoon_card.json',
        'lb_file': 'FINAL/Svartulfr_NPC_Primary.json',
        'lb_live': live_lb_prim,
        'expected_avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public'
    }
]

print("\n--- CHECKING LOCAL AND LIVE PARITY ACROSS ALL 8 CARDS ---")
errors = []

for cfg in cards_config:
    cname = cfg['name']
    cid = cfg['cid']
    print(f"\nChecking: {cname} ({cid})")

    # Local card
    with open(cfg['card_file'], 'r', encoding='utf-8') as f:
        loc_card = json.load(f)
    loc_card_desc = loc_card.get('description', '')
    loc_card_avatar = loc_card.get('avatar', '')

    # Live card
    live_card = live_mine_by_id.get(cid)
    if not live_card:
        errors.append(f"Live card {cid} ({cname}) not found in /characters/mine")
        continue
    live_card_desc = live_card.get('description', '')
    live_card_avatar = live_card.get('avatar', '')

    # Local lorebook entry
    with open(cfg['lb_file'], 'r', encoding='utf-8') as f:
        loc_lb = json.load(f)
    loc_lb_entry = None
    for e in loc_lb.get('entries', []):
        if cid in e.get('ignored_characters', []) or e.get('name') == cname:
            loc_lb_entry = e
            break
    if not loc_lb_entry:
        errors.append(f"Local entry for {cname} not found in {cfg['lb_file']}")
        continue

    loc_lb_desc = loc_lb_entry.get('content', '')
    loc_lb_avatar = loc_lb_entry.get('avatar', '')
    loc_lb_ignored = loc_lb_entry.get('ignored_characters', [])

    # Live lorebook entry
    live_lb_entry = None
    for e in cfg['lb_live'].get('lexicon', []):
        if cid in e.get('ignored_characters', []) or e.get('name') == cname:
            live_lb_entry = e
            break
    if not live_lb_entry:
        errors.append(f"Live entry for {cname} not found in live lorebook")
        continue

    live_lb_desc = live_lb_entry.get('content', '')
    live_lb_avatar = live_lb_entry.get('avatar', '')
    live_lb_ignored = live_lb_entry.get('ignored_characters', [])

    # Check 1: Avatar matches expected gallery asset
    exp_avatar = cfg['expected_avatar']
    if loc_card_avatar != exp_avatar:
        errors.append(f"[{cname}] local card avatar mismatch: {loc_card_avatar} != {exp_avatar}")
    if live_card_avatar != exp_avatar:
        errors.append(f"[{cname}] live card avatar mismatch: {live_card_avatar} != {exp_avatar}")
    if loc_lb_avatar != exp_avatar:
        errors.append(f"[{cname}] local lorebook avatar mismatch: {loc_lb_avatar} != {exp_avatar}")
    if live_lb_avatar != exp_avatar:
        errors.append(f"[{cname}] live lorebook avatar mismatch: {live_lb_avatar} != {exp_avatar}")

    # Check 2: Byte-for-byte textual parity across all 4 representations:
    # loc_card_desc == live_card_desc == loc_lb_desc == live_lb_desc
    if loc_card_desc != loc_lb_desc:
        errors.append(f"[{cname}] Local card desc != local lb desc (len diff: {len(loc_card_desc) - len(loc_lb_desc)})")
    if live_card_desc != live_lb_desc:
        errors.append(f"[{cname}] Live card desc != live lb desc (len diff: {len(live_card_desc) - len(live_lb_desc)})")
    if loc_card_desc != live_card_desc:
        errors.append(f"[{cname}] Local card desc != live card desc (len diff: {len(loc_card_desc) - len(live_card_desc)})")

    # Check 3: ignored_characters contains exactly the card ID
    if loc_lb_ignored != [cid]:
        errors.append(f"[{cname}] Local lb ignored_characters is not exactly [{cid}]: {loc_lb_ignored}")
    if live_lb_ignored != [cid]:
        errors.append(f"[{cname}] Live lb ignored_characters is not exactly [{cid}]: {live_lb_ignored}")

    print(f"  Local Card Avatar:    {loc_card_avatar == exp_avatar}")
    print(f"  Live Card Avatar:     {live_card_avatar == exp_avatar}")
    print(f"  Local LB Avatar:      {loc_lb_avatar == exp_avatar}")
    print(f"  Live LB Avatar:       {live_lb_avatar == exp_avatar}")
    print(f"  Desc Parity (4-way):  {loc_card_desc == loc_lb_desc == live_card_desc == live_lb_desc} (Len: {len(loc_card_desc)})")
    print(f"  Ignored chars exact:  {loc_lb_ignored == [cid] and live_lb_ignored == [cid]}")

print("\n--- CHECKING MEMORY ENTRIES IN LOREBOOK I & II ---")
# Lorebook I
mem_lb1_loc = [e for e in json.load(open('FINAL/Svartulfr_Lorebook_I.json', encoding='utf-8'))['entries'] if e.get('type') == 'memory']
mem_lb1_live = [e for e in live_lb1.get('lexicon', []) if e.get('type') == 'memory']
print(f"Lorebook I Memory count: local={len(mem_lb1_loc)}, live={len(mem_lb1_live)}")
for e in mem_lb1_loc:
    ign = e.get('ignored_characters', [])
    if ign:
        errors.append(f"[LB1 Local Memory] {e.get('name')} has ignored_characters: {ign}")
for e in mem_lb1_live:
    ign = e.get('ignored_characters', [])
    if ign:
        errors.append(f"[LB1 Live Memory] {e.get('name')} has ignored_characters: {ign}")

# Lorebook II
mem_lb2_loc = [e for e in json.load(open('FINAL/Svartulfr_Lorebook_II.json', encoding='utf-8'))['entries'] if e.get('type') == 'memory']
mem_lb2_live = [e for e in live_lb2.get('lexicon', []) if e.get('type') == 'memory']
print(f"Lorebook II Memory count: local={len(mem_lb2_loc)}, live={len(mem_lb2_live)}")
for e in mem_lb2_loc:
    ign = e.get('ignored_characters', [])
    if ign:
        errors.append(f"[LB2 Local Memory] {e.get('name')} has ignored_characters: {ign}")
for e in mem_lb2_live:
    ign = e.get('ignored_characters', [])
    if ign:
        errors.append(f"[LB2 Live Memory] {e.get('name')} has ignored_characters: {ign}")

print("\n--- PARITY BETWEEN FINAL/ AND lorebooks/optimized/ ---")
for lb_name in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    p_final = f"FINAL/{lb_name}"
    p_opt = f"lorebooks/optimized/{lb_name}"
    with open(p_final, 'r', encoding='utf-8') as f:
        d_final = f.read()
    with open(p_opt, 'r', encoding='utf-8') as f:
        d_opt = f.read()
    if d_final != d_opt:
        errors.append(f"Parity mismatch between {p_final} and {p_opt} (bytes: {len(d_final)} vs {len(d_opt)})")
    else:
        print(f"  {lb_name}: 100% byte-for-byte identical between FINAL/ and lorebooks/optimized/")

print("\n--- RESULTS SUMMARY ---")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
else:
    print("ALL TESTS PASSED! ZERO ERRORS.")
