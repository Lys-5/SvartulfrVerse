import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios/char_scenario_nLC84wrHdrbB6P3DEhwKb', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print("Camp Mystic Startup Script:")
print(data.get('startup_script'))
