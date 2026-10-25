import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

inventory_endpoints = [
    '/api/inventory',
    '/api/inventory/mine',
    '/api/inventories/mine',
    '/api/user/inventory',
    '/api/users/inventory',
    '/api/inventory/user',
    '/api/mine',
    '/api/user/mine',
    '/api/users/2r4fVpvImte5dbljedLkZJxre2d2/inventory',
]

for ep in inventory_endpoints:
    try:
        req = urllib.request.Request(f"https://app.wyvern.chat{ep}", headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"SUCCESS {ep} -> keys: {list(data.keys())[:8]}")
            if 'worlds' in data:
                print(f"  FOUND WORLDS IN {ep}: count = {len(data['worlds'])}")
                for w in data['worlds']:
                    print("   World:", w.get('id'), w.get('name'))
    except urllib.error.HTTPError as e:
        print(f"FAILED {ep} -> {e.code}")
    except Exception as e:
        print(f"ERROR {ep} -> {e}")
