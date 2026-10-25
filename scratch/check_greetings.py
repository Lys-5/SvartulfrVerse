import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for i, g in enumerate(data.get('greetings', [])):
    print(f"Greeting {i}: title='{g.get('title')}'")
    print('  Keys:', list(g.keys()))
    for k in g:
        if 'persona' in k.lower():
            print(f'  {k}:', g[k])
    if i >= 3:
        break
