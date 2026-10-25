import requests, json, os, difflib

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

out = []
def log(s=""):
    out.append(s)

log("=== 1. DETAILED INSPECTION: ALYSSA & JASPER ===")
r_personas = requests.get('https://app.wyvern.chat/api/user-personas', headers=headers)
r_chars = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)

personas = r_personas.json() if r_personas.status_code == 200 else []
chars_data = r_chars.json() if r_chars.status_code == 200 else {}
chars = chars_data.get('characters', []) if isinstance(chars_data, dict) else []

# Check Alyssa & Jasper in Personas
for p in personas:
    pname = p.get('name')
    if pname in ['Alyssa', 'Jasper']:
        local_p_path = f'FINAL/personas/{pname}_Persona.json'
        if os.path.exists(local_p_path):
            local_p = json.load(open(local_p_path, encoding='utf-8'))
            log(f"\n--- PERSONA: {pname} ---")
            live_desc = p.get('description', '')
            local_desc = local_p.get('description', '')
            if live_desc != local_desc:
                log(f"Description DIFFERENCE: live len={len(live_desc)} vs local len={len(local_desc)}")
                diff = list(difflib.unified_diff(local_desc.splitlines(), live_desc.splitlines(), lineterm='', n=2))
                for line in diff:
                    log(line)
            else:
                log("Description: IDENTICAL")
            for k in ['personality', 'first_mes', 'mes_example', 'scenario', 'post_history_instructions', 'outfits']:
                live_v = p.get(k)
                local_v = local_p.get(k)
                if live_v != local_v:
                    log(f"Field '{k}' differs")
                    if k == 'outfits':
                        log(f"  Live outfits: {len(live_v or [])} vs Local outfits: {len(local_v or [])}")
                        # list outfit names
                        live_names = [o.get('name') for o in (live_v or [])]
                        local_names = [o.get('name') for o in (local_v or [])]
                        log(f"  Live outfit names: {live_names}")
                        log(f"  Local outfit names: {local_names}")
                    elif isinstance(live_v, str) and isinstance(local_v, str):
                        diff = list(difflib.unified_diff(local_v.splitlines(), live_v.splitlines(), lineterm='', n=2))
                        for line in diff[:20]:
                            log(f"  {line}")

# Check Alyssa & Jasper in Characters
for c in chars:
    cname = c.get('name')
    if any(k in cname for k in ['Jasper', 'Alyssa']):
        log(f"\n--- CHARACTER CARD: {cname} (ID: {c.get('id')}) ---")
        card_file = 'FINAL/Jasper_Douglas_Bloodmoon_card.json' if 'Jasper' in cname else 'FINAL/Alyssa_Douglas_Bloodmoon_card.json'
        local_c = json.load(open(card_file, encoding='utf-8'))
        live_desc = c.get('description', '')
        local_desc = local_c.get('description', '')
        if live_desc != local_desc:
            log(f"Description DIFFERENCE: live len={len(live_desc)} vs local len={len(local_desc)}")
            diff = list(difflib.unified_diff(local_desc.splitlines(), live_desc.splitlines(), lineterm='', n=2))
            for line in diff:
                log(line)
        else:
            log("Description: IDENTICAL")
        for k in ['personality', 'first_mes', 'mes_example', 'scenario', 'post_history_instructions', 'outfits', 'system_prompt']:
            live_v = c.get(k)
            local_v = local_c.get(k)
            if live_v != local_v:
                log(f"Field '{k}' differs: live len={len(str(live_v))} vs local len={len(str(local_v))}")
                if k == 'outfits':
                    log(f"  Live outfits: {len(live_v or [])} vs Local outfits: {len(local_v or [])}")
                    live_names = [o.get('name') for o in (live_v or [])]
                    local_names = [o.get('name') for o in (local_v or [])]
                    log(f"  Live outfit names: {live_names}")
                    log(f"  Local outfit names: {local_names}")
                elif isinstance(live_v, str) and isinstance(local_v, str):
                    diff = list(difflib.unified_diff(local_v.splitlines(), live_v.splitlines(), lineterm='', n=2))
                    for line in diff[:20]:
                        log(f"  {line}")

log("\n=== 2. LOREBOOKS: NPC SECONDARY & LOCATION ===")
r_npc_sec = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
r_loc = requests.get('https://app.wyvern.chat/api/lorebooks/_EjXxkmPVhpCXg8xABpFkK', headers=headers)

if r_npc_sec.status_code == 200:
    lb_npc = r_npc_sec.json()
    live_lex_npc = lb_npc.get('lexicon', [])
    local_lex_npc = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8')).get('lexicon', [])
    log(f"NPC Secondary: Live count = {len(live_lex_npc)} | Local count = {len(local_lex_npc)}")
    
    # Save live NPC Secondary raw dump to scratch for analysis
    json.dump(lb_npc, open('scratch/live_raw_npc_secondary.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    
    local_ids = {e.get('id') for e in local_lex_npc}
    # find which entries are newly added
    new_npc_entries = [e for e in live_lex_npc if e.get('id') not in local_ids]
    log(f"New NPC entries count: {len(new_npc_entries)}")
    for idx, e in enumerate(new_npc_entries):
        log(f"  [{idx+1}] ID={e.get('id')} Name='{e.get('name')}' Keys={e.get('keys')} Type='{e.get('type')}' DescLen={len(e.get('description',''))}")

if r_loc.status_code == 200:
    lb_loc = r_loc.json()
    live_lex_loc = lb_loc.get('lexicon', [])
    local_lex_loc = json.load(open('FINAL/Svartulfr_Location.json', encoding='utf-8')).get('lexicon', [])
    log(f"\nLocation: Live count = {len(live_lex_loc)} | Local count = {len(local_lex_loc)}")
    
    # Save live Location raw dump to scratch
    json.dump(lb_loc, open('scratch/live_raw_location.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    
    local_ids_loc = {e.get('id') for e in local_lex_loc}
    new_loc_entries = [e for e in live_lex_loc if e.get('id') not in local_ids_loc]
    log(f"New Location entries count: {len(new_loc_entries)}")
    for idx, e in enumerate(new_loc_entries):
        log(f"  [{idx+1}] ID={e.get('id')} Name='{e.get('name')}' Keys={e.get('keys')} Type='{e.get('type')}' DescLen={len(e.get('description',''))}")

with open('scratch/user_changes_report.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Report written to scratch/user_changes_report.txt")
