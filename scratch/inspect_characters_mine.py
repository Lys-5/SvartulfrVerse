import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/characters/mine", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("Keys in /characters/mine:", list(data.keys()))
    print("Total characters in /characters/mine:", len(data.get('characters', [])))
    for c in data.get('characters', []):
        print("Char:", c.get('id'), c.get('name'))
