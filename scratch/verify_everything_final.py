import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
OPT = ROOT / 'lorebooks' / 'optimized'
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

def get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8'))

print("=== 1. VERIFYING LOCAL LOREBOOKS & OPTIMIZED MIRRORS ===")
EXPECTED_LB = [
    ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 221),
    ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 139),
    ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartulfr_Lorebook_III.json', 35),
    ('_EjXxkmPVhpCXg8xABpFkK', 'Svartulfr_Location.json', 188),
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 99),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 111),
]

for lid, fname, exp_cnt in EXPECTED_LB:
    f_data = json.loads((FINAL / fname).read_text(encoding='utf-8'))
    o_data = json.loads((OPT / fname).read_text(encoding='utf-8'))
    entries = f_data.get('entries', [])
    assert len(entries) == exp_cnt, f"{fname}: expected {exp_cnt}, got {len(entries)}"
    assert len(o_data.get('entries', [])) == exp_cnt, f"optimized/{fname}: mismatch"
    for e in entries:
        c = e.get('content', '')
        assert '{{user}}' not in c.lower(), f"{{{{user}}}} found in {fname} -> {e.get('name')}"
        assert '{{pronoun' not in c.lower(), f"{{{{pronoun found in {fname} -> {e.get('name')}"
        assert '[INSTRUCTIONS:' not in c, f"[INSTRUCTIONS: found in {fname} -> {e.get('name')}"
        if '[STATS:' in c:
            assert '[STATS: STR' in c and 'LCK' in c, f"Non-7-stat block in {fname} -> {e.get('name')}"
            assert 'MGT:' not in c and 'MGT ' not in c, f"Legacy MGT stat in {fname} -> {e.get('name')}"
    st, live_lb = get_json(f'https://app.wyvern.chat/api/lorebooks/{lid}')
    live_cnt = len(live_lb.get('lexicon', live_lb.get('entries', [])))
    assert st == 200 and live_cnt == exp_cnt, f"Live {fname} count mismatch: {live_cnt} != {exp_cnt}"
    print(f"OK {fname}: local={len(entries)}, optimized={len(o_data.get('entries', []))}, live={live_cnt}, 0 {{{{user}}}}, 0 legacy stats")

print("\n=== 2. VERIFYING 14 CHARACTER CARDS & 3 USER PERSONAS (LOCAL & LIVE) ===")
CARDS = [
    ('_wn6DkCcg3Xqa2Xpx9ttnT', 'Russ_card.json', 9, 21),
    ('_6exg3yPfe2eCDK4hTftkh', 'Alyssa_Douglas_Bloodmoon_card.json', 19, 19),
    ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json', 9, 13),
    ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json', 10, 55),
    ('_xJVPtBLL3dxy69RLKL9X9', 'Jared_Thompson_card.json', 11, 22),
    ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json', 11, 19),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json', 10, 49),
    ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie_Sanchez_Rogers_card.json', 11, 19),
    ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json', 11, 28),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json', 9, 25),
    ('_qXgBMbFYJfc84hbLHhe92', 'Scarlett_Rose_card.json', 9, 20),
    ('_pnrXbkWqcgmFAf3meRWFY', 'Sierra_Cruz_card.json', 9, 18),
    ('_Xd3NhKnRJByMTtdb6PjxJ', 'Stan_Davies_Jr_card.json', 9, 21),
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json', 12, 99),
]

for cid, fname, exp_outfits, exp_lvl in CARDS:
    c = json.loads((FINAL / fname).read_text(encoding='utf-8'))
    desc = c['description']
    assert '[LEVEL: ' in desc and f'[LEVEL: {exp_lvl};' in desc, f"{fname}: missing [LEVEL: {exp_lvl};"
    assert '[STATS: STR' in desc and 'LCK' in desc and 'MGT' not in desc, f"{fname}: bad stats format"
    assert len(c.get('outfits', [])) == exp_outfits, f"{fname}: outfits {len(c.get('outfits', []))} != {exp_outfits}"
    for o in c.get('outfits', []):
        assert 'id' in o and 'name' in o and 'description' in o and 'outfit' not in o, f"{fname}: bad outfit schema {o.keys()}"
    if fname == 'Jasper_Douglas_Bloodmoon_card.json':
        assert 'Ascended Alpha' not in json.dumps(c), "Jasper still has Ascended Alpha"
    if fname == 'Mackenzie_Sanchez_Rogers_card.json':
        assert 'Dominant Alpha' not in desc and 'Alpha Command' not in desc, "Mac still has Alpha traits"
    if fname == 'Edric_Douglas_card.json':
        assert c.get('rating') == 'mature', "Edric rating not mature"
    if fname == 'Russ_card.json':
        assert 'Demihuman Tiger' in desc and 'AGE: 21' in desc and c.get('post_history_instructions'), "Russ check failed"
    st, live_c = get_json(f'https://app.wyvern.chat/api/characters/{cid}')
    assert st == 200 and len(live_c.get('outfits', [])) == exp_outfits, f"Live {fname} outfits mismatch"
    print(f"OK {fname} ({cid}): local & live outfits={exp_outfits}, LEVEL={exp_lvl}, rating={live_c.get('rating')}")

for pid, pfile, exp_outfits in [
    ('persona_1786335754946', 'Alyssa_Persona.json', 19),
    ('1792155173728', 'Jasper_Persona.json', 11),
    ('1791389790053', 'Echo_Persona.json', 4),
]:
    p = json.loads((FINAL / 'personas' / pfile).read_text(encoding='utf-8'))
    assert len(p.get('outfits', [])) == exp_outfits, f"{pfile} outfits mismatch"
    if pfile == 'Jasper_Persona.json':
        assert 'Ascended Alpha' not in json.dumps(p), "Jasper Persona has Ascended Alpha"
        assert '{{user}}' not in p['description'], "Jasper Persona has {{user}}"
    st, live_p = get_json(f'https://app.wyvern.chat/api/user-personas/{pid}')
    assert st == 200 and len(live_p.get('outfits', [])) == exp_outfits, f"Live {pfile} mismatch"
    print(f"OK {pfile} ({pid}): local & live outfits={exp_outfits}")

print("\n=== 3. VERIFYING MASTER SCENARIO (LOCAL & LIVE) ===")
st, live_s = get_json('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4')
local_s = json.loads((FINAL / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8'))
assert st == 200
assert len(live_s['greetings']) == 29 and len(local_s['greetings']) == 29
for i, (lg, rg) in enumerate(zip(local_s['greetings'], live_s['greetings'])):
    assert lg['name'].startswith(f"{i+1:02d}. ")
    assert rg['name'] == lg['name']
    assert len(lg['messages']) == len(rg['messages']) and len(lg['messages']) >= 1
    assert lg['content'] == lg['messages'][0]['content']
    assert lg['speaker_slot'] == lg['messages'][0]['speaker_slot']
    for m in lg['messages']:
        assert m['speaker_slot'] is not None
        assert '—' not in m['content'] and '*' not in m['content']
print(f"OK Master Scenario (rev {live_s.get('revision')}): 29 chronological greetings verified locally and live!")
