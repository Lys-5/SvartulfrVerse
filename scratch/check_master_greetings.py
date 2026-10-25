import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for i, g in enumerate(data.get('greetings', [])):
    pids = g.get('linked_persona_ids', [])
    name = g.get('name') or g.get('title') or f"Greeting #{i+1}"
    print(f"[{i}] {name} -> {pids}")
