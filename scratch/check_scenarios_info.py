import urllib.request
import json

token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

url = 'https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    wdata = json.loads(resp.read().decode('utf-8'))
    print('World keys:', list(wdata.keys()))
    scs = wdata.get('scenarios', [])
    print('World scenarios count:', len(scs))
    for i, s in enumerate(scs):
        print(f"  [{i}] ID: {s.get('_id')} | Name: {s.get('name') or s.get('title')}")

# Also check character scenarios
try:
    req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios', headers=headers)
    with urllib.request.urlopen(req) as resp:
        cs = json.loads(resp.read().decode('utf-8'))
        print('Character scenarios count:', len(cs))
        for i, s in enumerate(cs):
            print(f"  [{i}] ID: {s.get('_id')} | Name: {s.get('name')}")
except Exception as e:
    print('Error char scenarios:', e)
