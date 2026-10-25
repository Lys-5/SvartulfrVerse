import requests, json, os, difflib

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

print("=== 1. FETCHING PERSONAS & CHARACTERS (MINE) ===")
r_personas = requests.get('https://app.wyvern.chat/api/user-personas', headers=headers)
r_chars = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)

personas = r_personas.json() if r_personas.status_code == 200 else []
chars_data = r_chars.json() if r_chars.status_code == 200 else {}
chars = chars_data.get('characters', []) if isinstance(chars_data, dict) else []

print(f"Personas: {len(personas)} | Characters: {len(chars)}")

# Check Alyssa & Jasper in Personas
for p in personas:
    pname = p.get('name')
    if pname in ['Alyssa', 'Jasper']:
        local_p_path = f'FINAL/personas/{pname}_Persona.json'
        if os.path.exists(local_p_path):
            local_p = json.load(open(local_p_path, encoding='utf-8'))
            print(f"\n--- PERSONA: {pname} ---")
            live_desc = p.get('description', '')
            local_desc = local_p.get('description', '')
            if live_desc != local_desc:
                print(f"Description DIFFERENCE: live len={len(live_desc)} vs local len={len(local_desc)}")
                diff = list(difflib.unified_diff(local_desc.splitlines(), live_desc.splitlines(), lineterm='', n=2))
                for line in diff[:30]:
                    print(line)
            else:
                print("Description: IDENTICAL")
            # check other fields
            for k in ['personality', 'first_mes', 'mes_example', 'scenario', 'post_history_instructions', 'outfits']:
                live_v = p.get(k)
                local_v = local_p.get(k)
                if live_v != local_v:
                    print(f"Field '{k}' differs: live={type(live_v)} len={len(str(live_v))} vs local={type(local_v)} len={len(str(local_v))}")
                    if k == 'outfits':
                        print(f"Live outfits count: {len(live_v or [])} vs Local outfits count: {len(local_v or [])}")

# Check Alyssa & Jasper in Characters
for c in chars:
    cname = c.get('name')
    if any(k in cname for k in ['Jasper', 'Alyssa']):
        print(f"\n--- CHARACTER CARD: {cname} (ID: {c.get('id')}) ---")
        card_file = 'FINAL/Jasper_Douglas_Bloodmoon_card.json' if 'Jasper' in cname else 'FINAL/Alyssa_Douglas_Bloodmoon_card.json'
        local_c = json.load(open(card_file, encoding='utf-8'))
        live_desc = c.get('description', '')
        local_desc = local_c.get('description', '')
        if live_desc != local_desc:
            print(f"Description DIFFERENCE: live len={len(live_desc)} vs local len={len(local_desc)}")
            diff = list(difflib.unified_diff(local_desc.splitlines(), live_desc.splitlines(), lineterm='', n=2))
            for line in diff[:30]:
                print(line)
        else:
            print("Description: IDENTICAL")
        for k in ['personality', 'first_mes', 'mes_example', 'scenario', 'post_history_instructions', 'outfits', 'system_prompt']:
            live_v = c.get(k)
            local_v = local_c.get(k)
            if live_v != local_v:
                print(f"Field '{k}' differs: live len={len(str(live_v))} vs local len={len(str(local_v))}")
                if k == 'outfits':
                    print(f"Live outfits: {len(live_v or [])} vs Local outfits: {len(local_v or [])}")

print("\n=== 2. FETCHING LOREBOOKS (NPC Secondary & Location) ===")
# Svartúlfr - NPC Secondary: _Uht3Ckz44JBDrPnUHq7LV
r_npc_sec = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
# Svartúlfr - Location: _EjXxkmPVhpCXg8xABpFkK
r_loc = requests.get('https://app.wyvern.chat/api/lorebooks/_EjXxkmPVhpCXg8xABpFkK', headers=headers)

if r_npc_sec.status_code == 200:
    lb_npc = r_npc_sec.json()
    live_lex_npc = lb_npc.get('lexicon', [])
    local_lex_npc = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8')).get('lexicon', [])
    print(f"NPC Secondary: Live lexicon count = {len(live_lex_npc)} | Local count = {len(local_lex_npc)}")
    
    local_ids = {e.get('id') for e in local_lex_npc}
    new_npc_entries = [e for e in live_lex_npc if e.get('id') not in local_ids]
    print(f"New NPC entries found in live: {len(new_npc_entries)}")
    for e in new_npc_entries:
        print(f"  - New NPC: '{e.get('name')}' (id: {e.get('id')}, type: {e.get('type')}, keys: {e.get('keys')})")

    # Also check if any existing entry was modified
    live_map = {e.get('id'): e for e in live_lex_npc}
    modified_npc = []
    for le in local_lex_npc:
        eid = le.get('id')
        if eid in live_map:
            if json.dumps(le, sort_keys=True) != json.dumps(live_map[eid], sort_keys=True):
                modified_npc.append(le.get('name'))
    if modified_npc:
        print(f"Existing NPC entries modified: {modified_npc}")

if r_loc.status_code == 200:
    lb_loc = r_loc.json()
    live_lex_loc = lb_loc.get('lexicon', [])
    local_lex_loc = json.load(open('FINAL/Svartulfr_Location.json', encoding='utf-8')).get('lexicon', [])
    print(f"\nLocation: Live lexicon count = {len(live_lex_loc)} | Local count = {len(local_lex_loc)}")
    
    local_ids_loc = {e.get('id') for e in local_lex_loc}
    new_loc_entries = [e for e in live_lex_loc if e.get('id') not in local_ids_loc]
    print(f"New Location entries found in live: {len(new_loc_entries)}")
    for e in new_loc_entries:
        print(f"  - New Location: '{e.get('name')}' (id: {e.get('id')}, type: {e.get('type')}, keys: {e.get('keys')})")

    live_map_loc = {e.get('id'): e for e in live_lex_loc}
    modified_loc = []
    for le in local_lex_loc:
        eid = le.get('id')
        if eid in live_map_loc:
            if json.dumps(le, sort_keys=True) != json.dumps(live_map_loc[eid], sort_keys=True):
                modified_loc.append(le.get('name'))
    if modified_loc:
        print(f"Existing Location entries modified: {modified_loc}")
