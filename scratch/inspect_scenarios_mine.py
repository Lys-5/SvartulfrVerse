import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/scenarios/mine", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("Keys in /scenarios/mine:", list(data.keys()))
    print("Total scenarios in /scenarios/mine:", len(data.get('scenarios', [])))
    for s in data.get('scenarios', []):
        print("Scenario:", s.get('id'), s.get('title'))
