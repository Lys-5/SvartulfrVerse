import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

req_get = urllib.request.Request(
    'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4',
    headers=headers
)
with urllib.request.urlopen(req_get) as resp:
    live = json.loads(resp.read().decode('utf-8'))

p = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.load(p.open(encoding='utf-8'))

# Let's test removing slot 'marek' vs keeping slot 'marek'
# Or testing each slot one by one!
slots_to_test = [s for s in scen['slots'] if s['key'] != 'marek']
print(f"Testing with {len(slots_to_test)} slots (without marek)...")

payload = {
    'name': scen['name'],
    'display_description': scen.get('display_description', ''),
    'avatar': scen.get('avatar', ''),
    'tags': scen.get('tags', []),
    'visibility': scen['visibility'],
    'rating': scen['rating'],
    'revision': live['revision'],
    'scenario': scen['scenario'],
    'startup_script': scen.get('startup_script', ''),
    'slots': slots_to_test,
    'greetings': [g for g in scen['greetings'] if g.get('speaker_slot') != 'marek'],
    'lorebook_ids': scen.get('lorebook_ids', [])
}

# If any message in greetings has speaker_slot == 'marek', change to 'twin' or remove
for g in payload['greetings']:
    if 'messages' in g:
        g['messages'] = [m for m in g['messages'] if m.get('speaker_slot') != 'marek']

body = json.dumps(payload).encode('utf-8')
req_put = urllib.request.Request(
    'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4',
    data=body,
    headers=headers,
    method='PUT'
)

try:
    with urllib.request.urlopen(req_put) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"PUT without marek SUCCESS! Status: {resp.status}, New revision: {res.get('revision')}")
except urllib.error.HTTPError as e:
    err = e.read().decode('utf-8')
    print(f"PUT without marek failed: {e.code} - {err}")
except Exception as e:
    print(f"Error: {e}")
