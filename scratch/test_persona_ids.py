import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}

for pid in ['persona_1786335754946', 'user_persona_VnRF2xGeG1C4xByDF9h9R', '1792155173728', 'user_persona_bGDFCEtKDzVmgbCmHJWEW']:
    try:
        req = urllib.request.Request(f'https://app.wyvern.chat/api/user-personas/{pid}', headers=headers)
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            print(f"{pid} -> OK! name={d.get('name')}, id={d.get('id')}, can_fork={d.get('can_fork')}")
    except Exception as e:
        print(f"{pid} -> ERROR: {e}")
