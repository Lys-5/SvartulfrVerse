import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': 'Bearer ' + token,
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}

url = 'https://app.wyvern.chat/api/character-scenarios/mine?limit=50'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print(f"Total scenarios: {data.get('total')}")
for sc in data.get('items', []):
    sid = sc.get('id')
    req2 = urllib.request.Request(f"https://app.wyvern.chat/api/character-scenarios/{sid}", headers=headers)
    with urllib.request.urlopen(req2, timeout=15) as r2:
        d2 = json.loads(r2.read().decode('utf-8'))
        print(f"[{sid}] '{d2.get('name')}' | Vis: {d2.get('visibility')} | Slots: {len(d2.get('slots', []))} | Greetings: {len(d2.get('greetings', []))} | Lorebooks: {len(d2.get('lorebook_ids', []))}")
