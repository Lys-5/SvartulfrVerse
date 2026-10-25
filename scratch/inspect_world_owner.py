import urllib.request
import json

headers = {
    'Authorization': f'Bearer {open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()}',
    'User-Agent': 'Mozilla/5.0'
}

req = urllib.request.Request('https://app.wyvern.chat/api/worlds/_YpX47fNraQFw2dD7TdycJ', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
for k, v in data.items():
    if any(x in k.lower() for x in ['user', 'author', 'creator', 'owner', 'id']):
        print(f'{k}: {v}')
