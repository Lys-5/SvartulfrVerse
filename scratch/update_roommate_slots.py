import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# 1. Fetch live scenario to get current revision
req_get = urllib.request.Request(f"{API_BASE}/character-scenarios/{SCENARIO_ID}", headers=headers)
with urllib.request.urlopen(req_get) as resp:
    live = json.load(resp)
current_rev = live.get('revision', 14)
print(f"Current live scenario revision: {current_rev}")

# 2. Load local scenario
scen_path = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.loads(scen_path.read_text(encoding='utf-8'))

# 3. Update slot 11 (female_roommate) and slot 13 (male_roommate)
for s in scen.get('slots', []):
    if s.get('key') == 'roommate':
        s['key'] = 'female_roommate'
        s['label'] = 'Female Roommate'
    elif s.get('key') == 'dorm_roommate':
        s['key'] = 'male_roommate'
        s['label'] = 'Male Roommate'

# 4. Update scenario text tags
scen_text = scen.get('scenario', '')
scen_text = scen_text.replace('{{scenarioChar "roommate"}}', '{{scenarioChar "female_roommate"}}')
scen_text = scen_text.replace('{{scenarioChar "dorm_roommate"}}', '{{scenarioChar "male_roommate"}}')
scen['scenario'] = scen_text

# 5. Save locally
scen_path.write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
print("Saved updated FINAL/Svartulfr_Master_Scenario.json")

# 6. Deploy via PUT /api/character-scenarios/{SCENARIO_ID}
put_payload = {
    'name': scen.get('name'),
    'display_description': scen.get('display_description', ''),
    'avatar': scen.get('avatar', ''),
    'tags': scen.get('tags', []),
    'visibility': scen.get('visibility', 'private'),
    'rating': scen.get('rating', 'explicit'),
    'revision': current_rev,
    'linked_world_id': scen.get('linked_world_id', ''),
    'scenario': scen.get('scenario', ''),
    'startup_script': scen.get('startup_script', ''),
    'slots': scen.get('slots', []),
    'greetings': scen.get('greetings', []),
    'lorebook_ids': scen.get('lorebook_ids', []),
    'gallery': scen.get('gallery', [])
}

req_put = urllib.request.Request(
    f"{API_BASE}/character-scenarios/{SCENARIO_ID}",
    data=json.dumps(put_payload, ensure_ascii=False).encode('utf-8'),
    headers=headers,
    method='PUT'
)

try:
    with urllib.request.urlopen(req_put, timeout=60) as resp:
        res = json.load(resp)
        print(f"Master Scenario PUT SUCCESS! Status: {resp.status} | New revision: {res.get('revision')} | Slots count: {len(res.get('slots', []))}")
        print("\nUpdated live slots:")
        for idx, s in enumerate(res.get('slots', []), 1):
            p_chars = [p.get('character_id') for p in s.get('pool', [])]
            print(f"  {idx:02d}. Key: '{s.get('key')}' | Label: '{s.get('label')}' | Pool: {p_chars}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8', errors='ignore')
    print(f"Master Scenario PUT HTTPError {e.code}: {err_body}")
