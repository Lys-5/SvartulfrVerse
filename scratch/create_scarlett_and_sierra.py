import urllib.request
import urllib.error
import json
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
SYNCED_FILE = ROOT / 'scratch' / 'synced_wyvern_ids.json'
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
            print("Token rinfrescato con successo.")
    except Exception as e:
        print("Warning: Errore rinfresco token:", e)
        token = TOKEN_FILE.read_text(encoding='utf-8').strip()
else:
    token = TOKEN_FILE.read_text(encoding='utf-8').strip()

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

def api_req(method: str, path: str, payload=None):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload).encode('utf-8') if payload is not None else None
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
        print(f"HTTP {e.code} on {method} {path}: {err_body[:300]}")
        return e.code, {'error': err_body}

synced_data = json.loads(SYNCED_FILE.read_text(encoding='utf-8')) if SYNCED_FILE.exists() else {}
synced_data.setdefault('characters_created', {})

TARGETS = [
    ('scarlett', 'Scarlett_Rose_card.json'),
    ('sierra', 'Sierra_Cruz_card.json')
]

for key, fname in TARGETS:
    fpath = FINAL_DIR / fname
    card = json.loads(fpath.read_text(encoding='utf-8'))
    
    # Check if existing in synced_data
    existing_id = synced_data['characters_created'].get(key, {}).get('id') or card.get('id')
    
    payload = {k: card[k] for k in EDITABLE_FIELDS if k in card}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    
    print(f"\n--- Deploying {card.get('name')} ({fname}) ---")
    if existing_id:
        print(f"Updating existing character {existing_id} via PUT...")
        st, res = api_req('PUT', f'/characters/{existing_id}', payload)
        new_id = existing_id
    else:
        print(f"Creating new character via POST /characters...")
        st, res = api_req('POST', '/characters', payload)
        new_id = res.get('id') or res.get('_id')
    
    print(f"Status: {st} | Assigned ID: {new_id}")
    if st in (200, 201) and new_id:
        card['id'] = new_id
        card['_id'] = new_id
        fpath.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
        synced_data['characters_created'][key] = {
            'id': new_id,
            'file': fname,
            'name': card.get('name')
        }
        print(f"Successfully saved {card.get('name')} with ID {new_id} to {fname}")
        
        # Verify via GET
        v_st, v_res = api_req('GET', f'/characters/{new_id}')
        print(f"GET Verification -> status={v_st} | name={v_res.get('name')} | outfits={len(v_res.get('outfits', []))}")
    else:
        print(f"FAILED to deploy {fname}: {res}")

SYNCED_FILE.write_text(json.dumps(synced_data, indent=2, ensure_ascii=False), encoding='utf-8')
print("\nsynced_wyvern_ids.json successfully updated!")
