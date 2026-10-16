import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
PERSONAS_DIR = FINAL_DIR / 'personas'
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'

def api_req(method: str, path: str, payload=None):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload).encode('utf-8') if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            'Authorization': f'Bearer {TOKEN}',
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

synced_ids = {
    'lorebooks': {},
    'characters_updated': {},
    'characters_created': {},
    'personas': {},
}

# 1. Sync the 6 Lorebooks
LOREBOOKS_MAP = [
    ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json'),
    ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json'),
    ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartulfr_Lorebook_III.json'),
    ('_EjXxkmPVhpCXg8xABpFkK', 'Svartulfr_Location.json'),
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json'),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json'),
]

print('=== 1. SYNCING 6 LOREBOOKS ===')
for lb_id, fname in LOREBOOKS_MAP:
    lb_data = json.loads((FINAL_DIR / fname).read_text(encoding='utf-8'))
    entries = lb_data.get('entries', lb_data.get('lexicon', []))
    payload = {
        'name': lb_data.get('name', fname.replace('.json', '')),
        'description': lb_data.get('description', ''),
        'scan_depth': lb_data.get('scan_depth', 5),
        'token_budget': lb_data.get('token_budget', 5000),
        'recursive_scanning': lb_data.get('recursive_scanning', True),
        'entries': entries,
    }
    st, res = api_req('PUT', f'/lorebooks/{lb_id}', payload)
    res_entries = len(res.get('entries', [])) if isinstance(res, dict) else -1
    print(f"PUT /lorebooks/{lb_id} ({fname}) -> status={st} | entries_sent={len(entries)} | entries_saved={res_entries}")
    synced_ids['lorebooks'][lb_id] = {'file': fname, 'status': st, 'entries': len(entries)}

# 2. Update the 7 Existing /mine Character Cards
EXISTING_CARDS = [
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json'),
    ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json'),
    ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json'),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json'),
    ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json'),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json'),
    ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json'),
]

print('\n=== 2. UPDATING 7 EXISTING /MINE CHARACTER CARDS ===')
for cid, fname in EXISTING_CARDS:
    card = json.loads((FINAL_DIR / fname).read_text(encoding='utf-8'))
    st, res = api_req('PUT', f'/characters/{cid}', card)
    print(f"PUT /characters/{cid} ({fname}) -> status={st} | outfits={len(card.get('outfits', []))}")
    synced_ids['characters_updated'][cid] = {'file': fname, 'status': st, 'name': card.get('name')}

# 3. Create (or update if already created) the 8 New /mine Character Cards
NEW_CARDS = [
    ('alyssa', 'Alyssa_Douglas_Bloodmoon_card.json'),
    ('zeera', 'Zeera_Darkfire_card.json'),
    ('jared', 'Jared_Thompson_card.json'),
    ('mac', 'Mackenzie_Sanchez_Rogers_card.json'),
    ('marek', 'Marek_card.json'),
    ('kaladin', 'Kaladin_Nargathon_card.json'),
    ('elizabeth', 'Elizabeth_Duskwood_card.json'),
    ('magnus', 'Magnus_Douglas_III_card.json'),
]

print('\n=== 3. CREATING 8 NEW /MINE CHARACTER CARDS ===')
# Strip read-only fields before POST /api/characters
STRIP_FIELDS = {
    'id', '_id', 'created_at', 'updated_at', 'creator', 'status',
    'statistics_record', 'entity_statistics', 'approval_date', 'visibility_submitted_at',
    'last_public_submitted_at', 'rejection_date', 'approval_comment', 'rejection_comment',
    'updated_at_by_user', 'moderation_hold', 'moderation_events', 'token_count',
    'likes', 'liked_by_me', 'boosted_by_me', 'vanity_slug', 'wyldfire_code'
}

for slot_key, fname in NEW_CARDS:
    fpath = FINAL_DIR / fname
    card = json.loads(fpath.read_text(encoding='utf-8'))
    post_payload = {k: v for k, v in card.items() if k not in STRIP_FIELDS}
    st, res = api_req('POST', '/characters', post_payload)
    new_id = res.get('_id') or res.get('id')
    print(f"POST /characters ({fname}) -> status={st} | new_id={new_id}")
    if new_id:
        card['id'] = new_id
        card['_id'] = new_id
        fpath.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
        synced_ids['characters_created'][slot_key] = {'id': new_id, 'file': fname, 'name': card.get('name')}

# 4. Update Alyssa & Echo User Personas and Create Jasper User Persona
print('\n=== 4. SYNCING USER PERSONAS ===')
for pid, fname in [
    ('persona_1786335754946', 'Alyssa_Persona.json'),
    ('1791389790053', 'Echo_Persona.json'),
]:
    p_data = json.loads((PERSONAS_DIR / fname).read_text(encoding='utf-8'))
    st, res = api_req('PUT', f'/user-personas/{pid}', p_data)
    print(f"PUT /user-personas/{pid} ({fname}) -> status={st}")
    synced_ids['personas'][pid] = {'file': fname, 'status': st, 'name': p_data.get('name')}

jasper_p_path = PERSONAS_DIR / 'Jasper_Persona.json'
jasper_p = json.loads(jasper_p_path.read_text(encoding='utf-8'))
st, res = api_req('POST', '/user-personas', jasper_p)
jasper_pid = res.get('persona_id') or res.get('id') or res.get('_id')
print(f"POST /user-personas (Jasper_Persona.json) -> status={st} | persona_id={jasper_pid}")
if jasper_pid:
    jasper_p['persona_id'] = jasper_pid
    if res.get('id'):
        jasper_p['id'] = res.get('id')
    jasper_p_path.write_text(json.dumps(jasper_p, indent=2, ensure_ascii=False), encoding='utf-8')
    synced_ids['personas']['jasper'] = {'persona_id': jasper_pid, 'id': res.get('id'), 'status': st, 'name': 'Jasper'}

(ROOT / 'scratch' / 'synced_wyvern_ids.json').write_text(json.dumps(synced_ids, indent=2, ensure_ascii=False), encoding='utf-8')
print('\nSaved scratch/synced_wyvern_ids.json!')
