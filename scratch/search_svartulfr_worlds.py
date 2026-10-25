import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/worlds/public?limit=100", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    worlds = data.get('worlds', [])
    for w in worlds:
        name = w.get('name', '')
        if any(term in name.lower() for term in ['svart', 'blackwood', 'solarton', 'douglas']):
            print(f"MATCH: ID: {w.get('id')} | Name: {name} | Vis: {w.get('visibility')} | Status: {w.get('status')}")
