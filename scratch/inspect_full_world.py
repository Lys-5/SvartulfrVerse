import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/worlds/_YpX47fNraQFw2dD7TdycJ", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    # remove long fields
    clean = {}
    for k, v in data.items():
        if k in ('system_prompt_override', 'simulation_engine_rules'):
            clean[k] = f"<{len(str(v))} chars>"
        else:
            clean[k] = v
    print(json.dumps(clean, indent=2))
