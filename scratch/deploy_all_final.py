import json
import pathlib
import urllib.request
import urllib.error
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
PERSONAS_DIR = FINAL_DIR / 'personas'
TOKEN_FILE = ROOT / 'scratch' / 'wyvern_token.txt'
API_BASE = 'https://app.wyvern.chat/api'

# 1. Refresh Token
ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
rt_path = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\74bb3384-9979-419b-80ab-c29e070cbffe\scratch\refresh_token.txt')
if rt_path.exists():
    rt = rt_path.read_text(encoding='utf-8').strip()
    body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
    req = urllib.request.Request(f'https://securetoken.googleapis.com/v1/token?key={ak}', data=body, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            token = data['id_token']
            TOKEN_FILE.write_text(token, encoding='utf-8')
            print("Token refreshed successfully.")
    except Exception as e:
        print("Warning refreshing token:", e)
        token = TOKEN_FILE.read_text(encoding='utf-8').strip()
else:
    token = TOKEN_FILE.read_text(encoding='utf-8').strip()

def api_req(method: str, path: str, payload=None):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8') if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode('utf-8')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTP {e.code} on {method} {path}: {err_body[:400]}")
        return e.code, {'error': err_body}

# 2. Deploy Master Scenario
print("\n=== 1. DEPLOYING MASTER SCENARIO ===")
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'
st_get, live_scen = api_req('GET', f'/character-scenarios/{SCENARIO_ID}')
current_rev = live_scen.get('revision', 16)
print(f"Fetched live scenario {SCENARIO_ID}: status={st_get}, current_rev={current_rev}")
time.sleep(2.5)

scen_path = FINAL_DIR / 'Svartulfr_Master_Scenario.json'
scen = json.loads(scen_path.read_text(encoding='utf-8'))
scen['revision'] = current_rev

scen_payload = {
    'name': scen['name'],
    'display_description': scen.get('display_description', ''),
    'avatar': scen.get('avatar', ''),
    'tags': scen.get('tags', []),
    'visibility': scen.get('visibility', 'private'),
    'rating': scen.get('rating', 'explicit'),
    'revision': current_rev,
    'scenario': scen['scenario'],
    'startup_script': scen.get('startup_script', ''),
    'slots': scen['slots'],
    'greetings': scen['greetings'],
    'lorebook_ids': scen.get('lorebook_ids', [])
}

st_put, res_scen = api_req('PUT', f'/character-scenarios/{SCENARIO_ID}', scen_payload)
new_rev = res_scen.get('revision', current_rev + 1)
print(f"PUT /character-scenarios/{SCENARIO_ID} -> status={st_put}, new_rev={new_rev}, greetings={len(res_scen.get('greetings', []))}")
if st_put in (200, 201):
    scen['revision'] = new_rev
    scen_path.write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
time.sleep(2.5)

# 3. Deploy 6 Lorebooks
print("\n=== 2. DEPLOYING 6 LOREBOOKS ===")
LOREBOOKS_SYNC = [
    ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 'Lorebook I'),
    ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 'Lorebook II'),
    ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartulfr_Lorebook_III.json', 'Lorebook III'),
    ('_EjXxkmPVhpCXg8xABpFkK', 'Svartulfr_Location.json', 'Location'),
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary'),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary'),
]

for lid, fname, label in LOREBOOKS_SYNC:
    fpath = FINAL_DIR / fname
    d = json.loads(fpath.read_text(encoding='utf-8'))
    entries = d.get('lexicon') or d.get('entries') or []
    payload = {
        'name': d.get('name'),
        'description': d.get('description'),
        'visibility': 'private',
        'rating': 'explicit',
        'scan_depth': d.get('scan_depth', 5),
        'token_budget': d.get('token_budget', 5000),
        'recursive_scanning': d.get('recursive_scanning', True),
        'lexicon': entries
    }
    st, res = api_req('PUT', f'/lorebooks/{lid}', payload)
    saved_cnt = len(res.get('lexicon', res.get('entries', []))) if isinstance(res, dict) else -1
    print(f"PUT /lorebooks/{lid} ({label}) -> status={st} | sent={len(entries)} | saved={saved_cnt}")
    assert st in (200, 201) and saved_cnt == len(entries), f"Failed Lorebook {label}: {st}"
    time.sleep(2.5)

# 4. Deploy 14 Character Cards
print("\n=== 3. DEPLOYING 14 CHARACTER CARDS ===")
EDITABLE_FIELDS = [
    'name', 'avatar', 'description', 'personality', 'mes_example', 'creator_notes',
    'post_history_instructions', 'pre_history_instructions', 'visual_description',
    'first_mes', 'alternate_greetings', 'scenario', 'model_url', 'soundcloud_url',
    'character_note', 'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating',
    'chat_name', 'pronouns', 'outfits', 'default_outfit', 'shared_info',
    'secretFields', 'secrets', 'fields', 'commands', 'lexicon', 'can_fork',
    'linked_world', 'metadata', 'prompt_assembly', 'first_message_name',
    'enable_advanced_greetings', 'greetings', 'gallery', 'lorebooks', 'personas',
    'sprite_sets', 'regex_scripts', 'visibility'
]

def normalize_pronouns(p):
    if isinstance(p, dict):
        return p
    if isinstance(p, str):
        if 'she' in p.lower():
            return {
                'pronoun_subjective': 'she',
                'pronoun_objective': 'her',
                'pronoun_possessive_determiner': 'her',
                'pronoun_possessive_pronoun': 'hers',
                'pronoun_reflexive': 'herself'
            }
        else:
            return {
                'pronoun_subjective': 'he',
                'pronoun_objective': 'him',
                'pronoun_possessive_determiner': 'his',
                'pronoun_possessive_pronoun': 'his',
                'pronoun_reflexive': 'himself'
            }
    return {
        'pronoun_subjective': 'they',
        'pronoun_objective': 'them',
        'pronoun_possessive_determiner': 'their',
        'pronoun_possessive_pronoun': 'theirs',
        'pronoun_reflexive': 'themselves'
    }

CARDS_SYNC = [
    ('_wn6DkCcg3Xqa2Xpx9ttnT', 'Russ_card.json'),
    ('_6exg3yPfe2eCDK4hTftkh', 'Alyssa_Douglas_Bloodmoon_card.json'),
    ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json'),
    ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json'),
    ('_xJVPtBLL3dxy69RLKL9X9', 'Jared_Thompson_card.json'),
    ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json'),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json'),
    ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie_Sanchez_Rogers_card.json'),
    ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json'),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json'),
    ('_qXgBMbFYJfc84hbLHhe92', 'Scarlett_Rose_card.json'),
    ('_pnrXbkWqcgmFAf3meRWFY', 'Sierra_Cruz_card.json'),
    ('_Xd3NhKnRJByMTtdb6PjxJ', 'Stan_Davies_Jr_card.json'),
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json'),
]

for cid, fname in CARDS_SYNC:
    fpath = FINAL_DIR / fname
    c = json.loads(fpath.read_text(encoding='utf-8'))
    payload = {k: c[k] for k in EDITABLE_FIELDS if k in c}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    payload['visibility'] = 'private'
    st, res = api_req('PUT', f'/characters/{cid}', payload)
    outfits_cnt = len(res.get('outfits', [])) if isinstance(res, dict) else -1
    rating_val = res.get('rating') if isinstance(res, dict) else '?'
    print(f"PUT /characters/{cid} ({fname}) -> status={st} | outfits={outfits_cnt} | rating={rating_val}")
    assert st in (200, 201), f"Failed card {fname}: {st}"
    time.sleep(2.5)

# 5. Deploy User Personas
print("\n=== 4. DEPLOYING USER PERSONAS ===")
PERSONAS_SYNC = [
    ('persona_1786335754946', 'Alyssa_Persona.json'),
    ('1792155173728', 'Jasper_Persona.json'),
    ('1791389790053', 'Echo_Persona.json'),
]

for pid, fname in PERSONAS_SYNC:
    p_data = json.loads((PERSONAS_DIR / fname).read_text(encoding='utf-8'))
    st, res = api_req('PUT', f'/user-personas/{pid}', p_data)
    outfits_cnt = len(res.get('outfits', [])) if isinstance(res, dict) else -1
    print(f"PUT /user-personas/{pid} ({fname}) -> status={st} | outfits={outfits_cnt}")
    assert st in (200, 201), f"Failed persona {fname}: {st}"
    time.sleep(2.5)

print("\n=== ALL WYVERN DEPLOYMENTS COMPLETED SUCCESSFULLY! ===")
