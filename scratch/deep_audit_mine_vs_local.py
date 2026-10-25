import urllib.request
import json
import os
import difflib

ROOT = r'e:\repository\SvartulfrVerse'
token = open(os.path.join(ROOT, 'scratch', 'wyvern_token.txt'), encoding='utf-8').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0'}

def api_get(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("=" * 80)
print("AUDIT GLOBALE APPROFONDITO: WYVERN MINE vs REPOSITORY LOCALE")
print("=" * 80)

# 1. PERSONAS (3)
print("\n--- 1. AUDIT USER PERSONAS (3) ---")
live_personas = api_get('https://app.wyvern.chat/api/user-personas')
print(f"Live Personas trovate: {len(live_personas)}")

local_personas_map = {
    'persona_1786335754946': 'Alyssa_Persona.json',
    'user_persona_VnRF2xGeG1C4xByDF9h9R': 'Alyssa_Persona.json',
    '1792155173728': 'Jasper_Persona.json',
    'user_persona_bGDFCEtKDzVmgbCmHJWEW': 'Jasper_Persona.json',
    '1791389790053': 'Echo_Persona.json',
    'user_persona_Chhp2NRN1kkVVPXCGQb8C': 'Echo_Persona.json',
}

persona_diffs = 0
for lp in live_personas:
    pid = lp.get('id') or lp.get('persona_id')
    pname = lp.get('name')
    matched_file = local_personas_map.get(lp.get('id')) or local_personas_map.get(lp.get('persona_id'))
    if not matched_file:
        print(f"  [ANOMALIA] Persona live non mappata in locale: {pname} ({lp.get('id')} / {lp.get('persona_id')})")
        persona_diffs += 1
        continue
    loc_path = os.path.join(ROOT, 'FINAL', 'personas', matched_file)
    loc_p = json.load(open(loc_path, encoding='utf-8'))
    
    # Check fields
    name_ok = (loc_p.get('name') == lp.get('name'))
    desc_ok = (loc_p.get('description') == lp.get('description'))
    outfits_loc = len(loc_p.get('outfits', []))
    outfits_live = len(lp.get('outfits', []))
    pron_ok = (loc_p.get('pronoun_subjective') == lp.get('pronoun_subjective'))
    can_fork_ok = (loc_p.get('can_fork') == lp.get('can_fork') and lp.get('can_fork') is True)
    
    print(f"  Persona '{pname}' ({matched_file}):")
    print(f"    Name: {'OK' if name_ok else 'DIFF'} | Desc len: {len(loc_p.get('description', ''))} vs {len(lp.get('description', ''))} ({'OK' if desc_ok else 'DIFF'})")
    print(f"    Outfits: loc={outfits_loc} vs live={outfits_live} ({'OK' if outfits_loc == outfits_live else 'DIFF'}) | can_fork={lp.get('can_fork')} ({'OK' if can_fork_ok else 'DIFF'})")
    
    if not (name_ok and desc_ok and outfits_loc == outfits_live and pron_ok and can_fork_ok):
        persona_diffs += 1

print(f"Esito Personas: {len(live_personas)} verificate, {persona_diffs} discrepanze.")

# 2. STANDALONE CHARACTER CARDS (14)
print("\n--- 2. AUDIT STANDALONE CHARACTERS (14) ---")
live_mine = api_get('https://app.wyvern.chat/api/characters/mine')
live_chars = live_mine.get('characters', [])
print(f"Live Characters in /characters/mine: {len(live_chars)}")

cards_map = {
    '_t4J9aQNJM36cUKAP4wB4U': 'Jasper_Douglas_Bloodmoon_card.json',
    '_QPea6g4Q1QfeYCVHCLMPR': 'Erik_Douglas_card.json',
    '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan_Douglas_card.json',
    '_RDfz7XzTpM23LpPALVXHM': 'Malachia_Douglas_Bloodmoon_card.json',
    '_zFLUjV8aVxQRAfQxGcAcY': 'Noah_Douglas_Bloodmoon_card.json',
    '_TbRM3EdxDjHFgqztTbCpL': 'Edric_Douglas_card.json',
    '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic_Bloodmoon_card.json',
    '_6exg3yPfe2eCDK4hTftkh': 'Alyssa_Douglas_Bloodmoon_card.json',
    '_xJVPtBLL3dxy69RLKL9X9': 'Jared_Thompson_card.json',
    '_zn24784jfcchQ7EwCyAnm': 'Mackenzie_Sanchez_Rogers_card.json',
    '_qXgBMbFYJfc84hbLHhe92': 'Scarlett_Rose_card.json',
    '_pnrXbkWqcgmFAf3meRWFY': 'Sierra_Cruz_card.json',
    '_Xd3NhKnRJByMTtdb6PjxJ': 'Stan_Davies_Jr_card.json',
    '_wn6DkCcg3Xqa2Xpx9ttnT': 'Russ_card.json',
}

card_diffs = 0
for lc in live_chars:
    cid = lc.get('id')
    cname = lc.get('name')
    matched_file = cards_map.get(cid)
    if not matched_file:
        print(f"  [ANOMALIA] Card live non mappata nei 14 slot: {cname} ({cid})")
        card_diffs += 1
        continue
    loc_path = os.path.join(ROOT, 'FINAL', matched_file)
    loc_c = json.load(open(loc_path, encoding='utf-8'))
    
    desc_ok = (loc_c.get('description') == lc.get('description'))
    outfits_loc = len(loc_c.get('outfits', []))
    outfits_live = len(lc.get('outfits', []))
    rating_ok = (loc_c.get('rating') == lc.get('rating'))
    vis_ok = (lc.get('visibility') == 'private')
    phi_ok = (loc_c.get('post_history_instructions') == lc.get('post_history_instructions'))
    
    print(f"  Card '{cname}' ({matched_file}):")
    print(f"    Desc len: {len(loc_c.get('description', ''))} vs {len(lc.get('description', ''))} ({'OK' if desc_ok else 'DIFF'}) | Rating: {lc.get('rating')} ({'OK' if rating_ok else 'DIFF'})")
    print(f"    Outfits: loc={outfits_loc} vs live={outfits_live} ({'OK' if outfits_loc == outfits_live else 'DIFF'}) | Phi: {'OK' if phi_ok else 'DIFF'}")
    
    if not (desc_ok and outfits_loc == outfits_live and rating_ok and vis_ok and phi_ok):
        card_diffs += 1
        if not desc_ok:
            print(f"      Desc len diff: loc={len(loc_c.get('description', ''))} vs live={len(lc.get('description', ''))}")
        if outfits_loc != outfits_live:
            print(f"      Outfits diff: loc={outfits_loc} vs live={outfits_live}")
        if not rating_ok:
            print(f"      Rating diff: loc={loc_c.get('rating')} vs live={lc.get('rating')}")

print(f"Esito Cards: {len(live_chars)} verificate, {card_diffs} discrepanze.")

# 3. LOREBOOKS STANDALONE (6)
print("\n--- 3. AUDIT LOREBOOKS STANDALONE (6) ---")
lorebooks_map = [
    ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 'Lorebook I', 221),
    ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 'Lorebook II', 139),
    ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartulfr_Lorebook_III.json', 'Lorebook III', 35),
    ('_EjXxkmPVhpCXg8xABpFkK', 'Svartulfr_Location.json', 'Location', 188),
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary', 99),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary', 111),
]

lb_diffs = 0
for lid, fname, label, exp_cnt in lorebooks_map:
    loc_path = os.path.join(ROOT, 'FINAL', fname)
    loc_lb = json.load(open(loc_path, encoding='utf-8'))
    loc_cnt = len(loc_lb.get('lexicon') or loc_lb.get('entries') or [])
    
    live_lb = api_get(f'https://app.wyvern.chat/api/lorebooks/{lid}')
    live_lex = live_lb.get('lexicon', [])
    live_cnt = len(live_lex)
    
    meta_name_ok = (live_lb.get('name') == loc_lb.get('name'))
    scan_ok = (live_lb.get('scan_depth') == loc_lb.get('scan_depth', 5))
    budget_ok = (live_lb.get('token_budget') == loc_lb.get('token_budget', 5000))
    cnt_ok = (live_cnt == loc_cnt == exp_cnt)
    
    print(f"  Lorebook '{label}' ({lid}):")
    print(f"    Entries: loc={loc_cnt} | live={live_cnt} | expected={exp_cnt} ({'OK' if cnt_ok else 'DIFF'})")
    print(f"    Metadata: Name={'OK' if meta_name_ok else 'DIFF'} | scan_depth={live_lb.get('scan_depth')} | budget={live_lb.get('token_budget')}")
    
    if not (meta_name_ok and cnt_ok and scan_ok and budget_ok):
        lb_diffs += 1
        # Check entry diffs
        for i, (le, re) in enumerate(zip(loc_lb.get('lexicon', []), live_lex)):
            if le.get('name') != re.get('name') or len(le.get('content', '')) != len(re.get('content', '')):
                print(f"      Entry {i} mismatch: loc='{le.get('name')}' (len {len(le.get('content', ''))}) vs live='{re.get('name')}' (len {len(re.get('content', ''))})")
                break

print(f"Esito Lorebooks: 6 verificati, {lb_diffs} discrepanze.")

# 4. MASTER CHARACTER SCENARIO (1)
print("\n--- 4. AUDIT MASTER CHARACTER SCENARIO (1) ---")
live_scen = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4')
loc_scen = json.load(open(os.path.join(ROOT, 'FINAL', 'Svartulfr_Master_Scenario.json'), encoding='utf-8'))

scen_diffs = 0
rev_live = live_scen.get('revision')
rev_loc = loc_scen.get('revision')
g_live_cnt = len(live_scen.get('greetings', []))
g_loc_cnt = len(loc_scen.get('greetings', []))
slots_live_cnt = len(live_scen.get('slots', []))
slots_loc_cnt = len(loc_scen.get('slots', []))
lb_ids_live = len(live_scen.get('lorebook_ids', []))
lb_ids_loc = len(loc_scen.get('lorebook_ids', []))
script_live_len = len(live_scen.get('startup_script', ''))
script_loc_len = len(loc_scen.get('startup_script', ''))
scen_prompt_ok = (live_scen.get('scenario') == loc_scen.get('scenario'))

print(f"  Master Scenario (char_scenario_1DC43ggb6mB8YLJDJKrU4):")
print(f"    Revision: loc={rev_loc} | live={rev_live} ({'OK' if rev_loc == rev_live else 'DIFF'})")
print(f"    Greetings: loc={g_loc_cnt} | live={g_live_cnt} ({'OK' if g_loc_cnt == g_live_cnt == 29 else 'DIFF'})")
print(f"    Slots: loc={slots_loc_cnt} | live={slots_live_cnt} ({'OK' if slots_loc_cnt == slots_live_cnt == 13 else 'DIFF'})")
print(f"    Lorebook IDs: loc={lb_ids_loc} | live={lb_ids_live} ({'OK' if lb_ids_loc == lb_ids_live == 14 else 'DIFF'})")
print(f"    Startup Script len: loc={script_loc_len} | live={script_live_len} ({'OK' if script_loc_len == script_live_len else 'DIFF'})")
print(f"    Scenario Prompt: {'OK' if scen_prompt_ok else 'DIFF'}")

if not (rev_loc == rev_live and g_live_cnt == 29 and slots_live_cnt == 13 and lb_ids_live == 14 and script_live_len == script_loc_len and scen_prompt_ok):
    scen_diffs += 1

# Check greetings 1-by-1
greeting_errors = 0
for idx, (lg, rg) in enumerate(zip(loc_scen.get('greetings', []), live_scen.get('greetings', []))):
    lg_name = lg.get('title') or lg.get('name')
    rg_name = rg.get('title') or rg.get('name')
    if lg_name != rg_name or len(lg.get('messages', [])) != len(rg.get('messages', [])):
        print(f"    Greeting {idx+1} mismatch: loc='{lg_name}' ({len(lg.get('messages', []))} msgs) vs live='{rg_name}' ({len(rg.get('messages', []))} msgs)")
        greeting_errors += 1

print(f"Esito Scenario: {'PERFETTAMENTE SINCRONIZZATO' if scen_diffs == 0 and greeting_errors == 0 else f'{scen_diffs} discrepanze'}")

print("\n" + "=" * 80)
total_diffs = persona_diffs + card_diffs + lb_diffs + scen_diffs + greeting_errors
print(f"RIASSUNTO FINALE AUDIT: {total_diffs} DISCREPANZE RILEVATE")
print("=" * 80)
