import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(ROOT / 'scratch'))
import refresh_token

TOKEN = refresh_token.refresh()

API_APP = 'https://app.wyvern.chat/api'
API_LORE = 'https://app.wyvern.chat/api' # or 'https://api.wyvern.chat'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

def api_call(method: str, url: str, payload=None, timeout=60):
    data = json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8') if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode('utf-8')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTP {e.code} on {method} {url}: {err_body[:300]}")
        return e.code, {'error': err_body}
    except Exception as e:
        print(f"Exception on {method} {url}: {e}")
        return 0, {'error': str(e)}

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

# 1. DEPLOY 8 CHARACTER CARDS
print("\n" + "=" * 60)
print("1. DEPLOYING 8 CHARACTER CARDS")
print("=" * 60)

final_cards = [
    ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json'),
    ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json'),
    ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json'),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json'),
    ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie_Sanchez_Rogers_card.json'),
    ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json'),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json'),
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json')
]

for cid, fname in final_cards:
    fpath = ROOT / 'FINAL' / fname
    c = json.loads(fpath.read_text(encoding='utf-8'))
    payload = {k: c[k] for k in EDITABLE_FIELDS if k in c}
    if 'pronouns' in payload:
        payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    payload['visibility'] = 'private'
    
    st, res = api_call('PUT', f'{API_APP}/characters/{cid}', payload)
    print(f"PUT /characters/{cid} ({fname}) -> status={st}")
    assert st in (200, 201), f"Failed deploying card {fname}: {st} {res}"
    time.sleep(2)

# 2. DEPLOY 3 USER PERSONAS
print("\n" + "=" * 60)
print("2. DEPLOYING 3 USER PERSONAS")
print("=" * 60)

personas_sync = [
    ('persona_1786335754946', 'Alyssa_Persona.json'),
    ('1792155173728', 'Jasper_Persona.json'),
    ('1791389790053', 'Echo_Persona.json'),
]

for pid, fname in personas_sync:
    p_data = json.loads((ROOT / 'FINAL' / 'personas' / fname).read_text(encoding='utf-8'))
    # Remove top level id / _id if needed, or send as is
    payload = {k: v for k, v in p_data.items() if k not in ['_id', 'id']}
    st, res = api_call('PUT', f'{API_APP}/user-personas/{pid}', payload)
    print(f"PUT /user-personas/{pid} ({fname}) -> status={st}")
    assert st in (200, 201), f"Failed deploying persona {fname}: {st} {res}"
    time.sleep(2)

# 3. DEPLOY 2 NPC LOREBOOKS
print("\n" + "=" * 60)
print("3. DEPLOYING 2 NPC LOREBOOKS")
print("=" * 60)

lorebooks_sync = [
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary'),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary'),
]

for lid, fname, label in lorebooks_sync:
    fpath = ROOT / 'FINAL' / fname
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
    st, res = api_call('PUT', f'{API_LORE}/lorebooks/{lid}', payload, timeout=120)
    saved_cnt = len(res.get('lexicon', res.get('entries', []))) if isinstance(res, dict) else -1
    print(f"PUT /lorebooks/{lid} ({label}) -> status={st} | sent={len(entries)} | saved={saved_cnt}")
    assert st in (200, 201), f"Failed deploying lorebook {label}: {st} {res}"
    time.sleep(2)

print("\n" + "=" * 60)
print("ALL LIVE DEPLOYMENTS FINISHED SUCCESSFULLY!")
print("=" * 60)
