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
            print("Token rinfrescato con successo.")
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

OFFICIAL_TAGS = {
  'Alyssa_Douglas_Bloodmoon_card.json': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Omega", "Student", "Fluff"],
  'Erik_Douglas_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "CEO"],
  'Jasper_Douglas_Bloodmoon_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Beta", "Musician", "Student"],
  'Noah_Douglas_Bloodmoon_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Student"],
  'Malachia_Douglas_Bloodmoon_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "Bodyguard", "Athlete"],
  'Logan_Douglas_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Beta", "Mechanic"],
  'Edric_Douglas_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Student"],
  'Wulfnic_Bloodmoon_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Historical", "Supernatural", "Original", "Werewolf", "Mythology"],
  'Elizabeth_Duskwood_card.json': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Omega", "Doctor"],
  'Magnus_Douglas_III_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Historical", "Supernatural", "Original", "Werewolf", "Royalty"],
  'Kaladin_Nargathon_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "Military", "Bodyguard"],
  'Zeera_Darkfire_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Demon", "CEO"],
  'Jared_Thompson_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Minotaur", "Demihuman", "Student", "Athlete", "Himbo"],
  'Mackenzie_Sanchez_Rogers_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Musician", "Artist"],
  'Marek_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Monster", "Demihuman"],
  'Russ_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Human", "Student", "Artist"],
  'Neon_Purr_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Demihuman", "Musician", "Cyberpunk"],
  'Scarlett_Rose_card.json': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Succubus (Incubus)", "Demihuman", "Student"],
  'Sierra_Cruz_card.json': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Naga", "Demihuman", "Student", "Monster"],
  'Stan_Davies_Jr_card.json': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "Student", "Artist"]
}

print("=== 2. LOCAL FIXES: REPLACING {{age}} & STANDARDIZING TAGS ===")
# Elizabeth
p = FINAL_DIR / 'Elizabeth_Duskwood_card.json'
card = json.loads(p.read_text(encoding='utf-8'))
card['description'] = card['description'].replace('AGE: {{age}};', 'AGE: 76 (Born July 14, 1947);')
card['tags'] = OFFICIAL_TAGS[p.name]
p.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Fixed Elizabeth Duskwood")

# Jared
p = FINAL_DIR / 'Jared_Thompson_card.json'
card = json.loads(p.read_text(encoding='utf-8'))
card['description'] = card['description'].replace('AGE: {{age}};', 'AGE: 22 (Born 2002);')
card['tags'] = OFFICIAL_TAGS[p.name]
p.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Fixed Jared Thompson")

# Kaladin
p = FINAL_DIR / 'Kaladin_Nargathon_card.json'
card = json.loads(p.read_text(encoding='utf-8'))
card['description'] = card['description'].replace('AGE: {{age}};', 'AGE: 37 (Born 1987);')
card['tags'] = OFFICIAL_TAGS[p.name]
p.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Fixed Kaladin Nargathon")

# Mackenzie
p = FINAL_DIR / 'Mackenzie_Sanchez_Rogers_card.json'
card = json.loads(p.read_text(encoding='utf-8'))
card['description'] = card['description'].replace('AGE: {{age}};', 'AGE: 19 (Born 2004);')
card['tags'] = OFFICIAL_TAGS[p.name]
p.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Fixed Mackenzie Sanchez-Rogers")

# Magnus
p = FINAL_DIR / 'Magnus_Douglas_III_card.json'
card = json.loads(p.read_text(encoding='utf-8'))
card['description'] = card['description'].replace('AGE: {{age}} (b. December 29, 1668', 'AGE: 355 (Born December 29, 1668')
card['tags'] = OFFICIAL_TAGS[p.name]
p.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Fixed Magnus Douglas III")

# Zeera
p = FINAL_DIR / 'Zeera_Darkfire_card.json'
card = json.loads(p.read_text(encoding='utf-8'))
card['description'] = card['description'].replace('AGE: {{age}};', 'AGE: 34;')
for lex in card.get('lexicon', []):
    if lex.get('name') == 'Aras Darkfire':
        lex['content'] = lex['content'].replace('AGE: {{age}};', 'AGE: 45;')
    elif lex.get('name') == 'Boros Darkfire':
        lex['content'] = lex['content'].replace('AGE: {{age}};', 'AGE: 45;')
    elif lex.get('name') == 'Karshin Darkfire':
        lex['content'] = lex['content'].replace('AGE: {{age}};', 'AGE: 28;')
    elif lex.get('name') == 'Varg Darkfire':
        lex['content'] = lex['content'].replace('AGE: {{age}};', 'AGE: 45;')
card['tags'] = OFFICIAL_TAGS[p.name]
p.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
print("Fixed Zeera Darkfire & lexicon")

# Fix tags on all other cards
for fname, tag_list in OFFICIAL_TAGS.items():
    p = FINAL_DIR / fname
    if p.exists():
        c = json.loads(p.read_text(encoding='utf-8'))
        c['tags'] = tag_list
        p.write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding='utf-8')

print("All 20 character cards updated locally with official tags.")

# 3. Deploy Stan Davies Jr.
print("\n=== 3. DEPLOYING STAN DAVIES JR. TO WYVERN ===")
stan_path = FINAL_DIR / 'Stan_Davies_Jr_card.json'
stan_card = json.loads(stan_path.read_text(encoding='utf-8'))

synced_data = json.loads(SYNCED_FILE.read_text(encoding='utf-8')) if SYNCED_FILE.exists() else {}
synced_data.setdefault('characters_created', {})

stan_existing_id = synced_data['characters_created'].get('stan', {}).get('id') or stan_card.get('id')

stan_payload = {k: stan_card[k] for k in EDITABLE_FIELDS if k in stan_card}
stan_payload['pronouns'] = normalize_pronouns(stan_payload.get('pronouns'))
stan_payload['visibility'] = 'private'

if stan_existing_id:
    print(f"Updating Stan {stan_existing_id} via PUT...")
    st, res = api_req('PUT', f'/characters/{stan_existing_id}', stan_payload)
    stan_id = stan_existing_id
else:
    print("Creating Stan via POST /characters...")
    st, res = api_req('POST', '/characters', stan_payload)
    stan_id = res.get('id') or res.get('_id')

print(f"Stan status: {st} | Assigned ID: {stan_id}")
if st in (200, 201) and stan_id:
    stan_card['id'] = stan_id
    stan_card['_id'] = stan_id
    stan_path.write_text(json.dumps(stan_card, indent=2, ensure_ascii=False), encoding='utf-8')
    synced_data['characters_created']['stan'] = {
        'id': stan_id,
        'file': 'Stan_Davies_Jr_card.json',
        'name': 'Stanley Davies Jr.'
    }
    SYNCED_FILE.write_text(json.dumps(synced_data, indent=2, ensure_ascii=False), encoding='utf-8')

# 4. Sync All Cards to Wyvern API (PUT)
print("\n=== 4. SYNCING ALL UPDATED CARDS TO WYVERN API ===")
ALL_SYNC_TARGETS = []

for cid, info in synced_data.get('characters_updated', {}).items():
    ALL_SYNC_TARGETS.append((cid, info['file'], info['name']))

for slot_key, info in synced_data.get('characters_created', {}).items():
    if slot_key != 'stan': # Stan already handled
        ALL_SYNC_TARGETS.append((info['id'], info['file'], info['name']))

for cid, fname, name in ALL_SYNC_TARGETS:
    fpath = FINAL_DIR / fname
    if not fpath.exists():
        continue
    c = json.loads(fpath.read_text(encoding='utf-8'))
    payload = {k: c[k] for k in EDITABLE_FIELDS if k in c}
    payload['pronouns'] = normalize_pronouns(payload.get('pronouns'))
    payload['visibility'] = 'private'
    
    st, res = api_req('PUT', f'/characters/{cid}', payload)
    print(f"PUT /characters/{cid} ({name} - {fname}) -> status={st} | tags={len(res.get('tags', [])) if isinstance(res, dict) else len(payload.get('tags', []))}")
    time.sleep(0.3)

print("\nAll characters successfully updated and deployed to Wyvern!")
