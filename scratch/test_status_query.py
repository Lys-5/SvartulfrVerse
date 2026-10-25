import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

user_id = '2r4fVpvImte5dbljedLkZJxre2d2'

statuses = [
    'pending',
    'approved',
    'all',
    'draft',
    'private',
    'unlisted',
    'rejected',
    'any'
]

for s in statuses:
    url = f"https://app.wyvern.chat/api/worlds/user/{user_id}?status={s}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            worlds = data.get('worlds', [])
            print(f"Status '{s}' -> count: {len(worlds)}, total: {data.get('total')}")
            for w in worlds:
                print(f"  ID: {w.get('id')} | Name: '{w.get('name')}' | Status: {w.get('status')} | Vis: {w.get('visibility')}")
    except Exception as e:
        print(f"Status '{s}' -> Error: {e}")
