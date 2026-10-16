import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'

CLEAN_POST_FIELDS = [
    'name', 'avatar', 'description', 'personality', 'mes_example', 'creator_notes',
    'post_history_instructions', 'pre_history_instructions', 'visual_description',
    'first_mes', 'alternate_greetings', 'scenario', 'model_url', 'soundcloud_url',
    'character_note', 'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating',
    'chat_name', 'pronouns', 'outfits', 'default_outfit', 'shared_info', 'visibility'
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
synced_ids.setdefault('characters_created', {})

# We already have:
# Alyssa: _6exg3yPfe2eCDK4hTftkh
# Marek: _cL86CRDAYABmaBWgdLQNw
# Kaladin: _EnRGd1jfbjTTGmz4EFJdd
# Elizabeth: _zBD6rWUkJBAjLfXnja4xh
# Magnus: _dJ7nRMQEbcUgdWG96MqLz
# Zeera: _3tMk6cRAFewRnKMkdJ4XU

NEW_CARDS = [
    ('zeera', 'Zeera_Darkfire_card.json', '_3tMk6cRAFewRnKMkdJ4XU'),
    ('jared', 'Jared_Thompson_card.json', None),
    ('mac', 'Mackenzie_Sanchez_Rogers_card.json', None),
]

for slot_key, fname, known_id in NEW_CARDS:
    fpath = FINAL_DIR / fname
    card = json.loads(fpath.read_text(encoding='utf-8'))
    
    payload = {k: card[k] for k in CLEAN_POST_FIELDS if k in card}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    payload['visibility'] = 'unlisted'
    
    if not payload.get('avatar') or not str(payload['avatar']).startswith('http'):
        payload['avatar'] = SVARTULFR_CREST_AVATAR
        
    if known_id:
        new_id = known_id
        st = 200
        print(f"Using known ID for {fname}: {new_id}")
    else:
        st, res = api_req('POST', '/characters', payload)
        new_id = res.get('id') or res.get('_id')
        print(f"POST /characters ({fname}) -> status={st} | assigned_id={new_id}")
    
    if new_id:
        card['id'] = new_id
        card['_id'] = new_id
        card['avatar'] = payload['avatar']
        card['pronouns'] = payload['pronouns']
        card['visibility'] = 'unlisted'
        fpath.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
        synced_ids['characters_created'][slot_key] = {'id': new_id, 'file': fname, 'name': card.get('name')}

synced_file.write_text(json.dumps(synced_ids, indent=2, ensure_ascii=False), encoding='utf-8')
print("\nSynced Wyvern IDs successfully updated and saved to scratch/synced_wyvern_ids.json!")
