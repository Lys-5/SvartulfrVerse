import json
import pathlib
import urllib.request
import urllib.error
import time

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
            print("Token rinfrescato.")
    except Exception as e:
        print("Warning rinfresco token:", e)
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

# 1. Fix Mac linked_world
mac_path = FINAL_DIR / 'Mackenzie_Sanchez_Rogers_card.json'
mac_card = json.loads(mac_path.read_text(encoding='utf-8'))
mac_card['linked_world'] = None
mac_path.write_text(json.dumps(mac_card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Removed linked_world from Mackenzie")

# 2. Deploy Marek
print("\n=== DEPLOYING MAREK TO WYVERN ===")
marek_path = FINAL_DIR / 'Marek_card.json'
marek_card = json.loads(marek_path.read_text(encoding='utf-8'))
marek_payload = {k: marek_card[k] for k in EDITABLE_FIELDS if k in marek_card}
marek_payload['pronouns'] = normalize_pronouns(marek_payload.get('pronouns'))
marek_payload['visibility'] = 'private'
marek_payload['linked_world'] = None

st, res = api_req('POST', '/characters', marek_payload)
print(f"Marek POST status: {st} | res: {res}")
if st in (200, 201):
    marek_id = res.get('id') or res.get('_id')
    marek_card['id'] = marek_id
    marek_card['_id'] = marek_id
    marek_path.write_text(json.dumps(marek_card, indent=2, ensure_ascii=False), encoding='utf-8')
    synced_data['characters_created']['marek'] = {
        'id': marek_id,
        'file': 'Marek_card.json',
        'name': 'Marek'
    }
    SYNCED_FILE.write_text(json.dumps(synced_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Marek successfully created with ID {marek_id}!")

# 3. Update remaining cards (Mac, Zeera, Russ, Sierra)
RETRY_CARDS = [
    ('Mac', mac_card['id'], 'Mackenzie_Sanchez_Rogers_card.json'),
    ('Zeera', synced_data['characters_created']['zeera']['id'], 'Zeera_Darkfire_card.json'),
    ('Russ', synced_data['characters_created']['russ']['id'], 'Russ_card.json'),
    ('Sierra', synced_data['characters_created']['sierra']['id'], 'Sierra_Cruz_card.json'),
]

print("\n=== UPDATING REMAINING CARDS WITH DELAY ===")
for name, cid, fname in RETRY_CARDS:
    print(f"Waiting 2 seconds before {name} ({cid})...")
    time.sleep(2)
    fpath = FINAL_DIR / fname
    c = json.loads(fpath.read_text(encoding='utf-8'))
    payload = {k: c[k] for k in EDITABLE_FIELDS if k in c}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    payload['visibility'] = 'private'
    payload['linked_world'] = None
    
    st, res = api_req('PUT', f'/characters/{cid}', payload)
    print(f"PUT /characters/{cid} ({name} - {fname}) -> status={st} | tags={len(res.get('tags', [])) if isinstance(res, dict) else len(payload.get('tags', []))}")

print("\nAll remaining cards updated!")
