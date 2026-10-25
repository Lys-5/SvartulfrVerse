import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

resources = [
    'characters',
    'lorebooks',
    'scenarios',
    'worlds',
    'parties',
    'user-personas',
    'personas',
    'prompts',
    'prompt-assemblies'
]

for r in resources:
    url = f"https://app.wyvern.chat/api/{r}/mine"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"SUCCESS {r}/mine -> count: {len(data) if isinstance(data, list) else 'dict'}")
    except urllib.error.HTTPError as e:
        print(f"FAILED {r}/mine -> {e.code}")
