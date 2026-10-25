import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

user_id = '2r4fVpvImte5dbljedLkZJxre2d2'

queries = [
    f'?search=Svartulfr',
    f'?search=Blackwood',
    f'?search=test',
    f'?creator={user_id}',
    f'?userId={user_id}',
    f'?creatorId={user_id}',
    f'?author={user_id}',
    f'?user={user_id}',
    f'?filter=mine',
    f'?mine=true',
    f'?visibility=all',
    f'?visibility=private'
]

for q in queries:
    url = f"https://app.wyvern.chat/api/worlds/public{q}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            worlds = data.get('worlds', [])
            print(f"Query '{q}' -> count: {len(worlds)}, total: {data.get('total')}")
            for w in worlds:
                creator = w.get('creator') or {}
                c_uid = creator.get('uid') if isinstance(creator, dict) else ''
                print(f"  ID: {w.get('id')} | Name: '{w.get('name')}' | Creator: {c_uid} | Vis: {w.get('visibility')}")
    except Exception as e:
        print(f"Query '{q}' -> Error: {e}")
