import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'

EDITABLE_FIELDS = [
    'name', 'avatar', 'description', 'personality', 'mes_example', 'creator_notes',
    'post_history_instructions', 'pre_history_instructions', 'visual_description',
    'first_mes', 'alternate_greetings', 'scenario', 'model_url', 'soundcloud_url',
    'character_note', 'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating',
    'chat_name', 'pronouns', 'outfits', 'default_outfit', 'shared_info',
    'secretFields', 'secrets', 'fields', 'commands', 'lexicon', 'can_fork',
    'linked_world', 'metadata', 'prompt_assembly', 'first_message_name',
    'enable_advanced_greetings', 'greetings', 'gallery', 'lorebooks', 'personas',
    'sprite_sets', 'regex_scripts'
]

SVARTULFR_CREST_AVATAR = 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public'

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
        print(f"HTTP {e.code} on {method} {path}: {err_body[:300]}")
        return e.code, {'error': err_body}

# Load existing synced_wyvern_ids.json
synced_file = ROOT / 'scratch' / 'synced_wyvern_ids.json'
synced_ids = json.loads(synced_file.read_text(encoding='utf-8')) if synced_file.exists() else {}
synced_ids.setdefault('characters_updated', {})
synced_ids.setdefault('characters_created', {})

# 1. Update 7 Existing Cards
EXISTING_CARDS = [
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json'),
    ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json'),
    ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json'),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json'),
    ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json'),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json'),
    ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json'),
]

print("=== 1. UPDATING 7 EXISTING /MINE CARDS ===")
for cid, fname in EXISTING_CARDS:
    fpath = FINAL_DIR / fname
    card = json.loads(fpath.read_text(encoding='utf-8'))
    payload = {k: card[k] for k in EDITABLE_FIELDS if k in card}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    
    st, res = api_req('PUT', f'/characters/{cid}', payload)
    outfits_count = len(res.get('outfits', [])) if isinstance(res, dict) else len(payload.get('outfits', []))
    print(f"PUT /characters/{cid} ({fname}) -> status={st} | outfits={outfits_count} | name={res.get('name') if isinstance(res, dict) else card.get('name')}")
    synced_ids['characters_updated'][cid] = {'file': fname, 'status': st, 'name': card.get('name')}

# 2. Create / Sync 8 New Cards
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

# Marek was created earlier in test
MAREK_PREV_ID = '_cL86CRDAYABmaBWgdLQNw'

print("\n=== 2. CREATING / SYNCING 8 NEW /MINE CARDS ===")
for slot_key, fname in NEW_CARDS:
    fpath = FINAL_DIR / fname
    card = json.loads(fpath.read_text(encoding='utf-8'))
    
    # Check if already created
    existing_entry = synced_ids['characters_created'].get(slot_key)
    existing_id = existing_entry.get('id') if existing_entry else None
    if slot_key == 'marek' and not existing_id:
        existing_id = MAREK_PREV_ID
    
    payload = {k: card[k] for k in EDITABLE_FIELDS if k in card}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    
    # Fallback avatar if missing
    if not payload.get('avatar') or not str(payload['avatar']).startswith('http'):
        payload['avatar'] = SVARTULFR_CREST_AVATAR
    
    if existing_id:
        st, res = api_req('PUT', f'/characters/{existing_id}', payload)
        print(f"PUT /characters/{existing_id} ({fname}) -> status={st}")
        new_id = existing_id
    else:
        st, res = api_req('POST', '/characters', payload)
        new_id = res.get('id') or res.get('_id')
        print(f"POST /characters ({fname}) -> status={st} | assigned_id={new_id}")
    
    if new_id:
        card['id'] = new_id
        card['_id'] = new_id
        card['avatar'] = payload['avatar']
        card['pronouns'] = payload['pronouns']
        fpath.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
        synced_ids['characters_created'][slot_key] = {'id': new_id, 'file': fname, 'name': card.get('name')}

synced_file.write_text(json.dumps(synced_ids, indent=2, ensure_ascii=False), encoding='utf-8')
print("\nSynced Wyvern IDs successfully updated and saved to scratch/synced_wyvern_ids.json!")
