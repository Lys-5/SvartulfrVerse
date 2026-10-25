import urllib.request
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request("https://app.wyvern.chat/api/worlds/public?limit=100", headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    worlds = data.get('worlds', [])
    print(f"Total public worlds: {len(worlds)}")
    for idx, w in enumerate(worlds):
        creator = w.get('creator') or {}
        creator_name = creator.get('displayName') if isinstance(creator, dict) else str(creator)
        creator_id = creator.get('uid') if isinstance(creator, dict) else ''
        print(f"[{idx+1}] ID: {w.get('id')} | Name: '{w.get('name')}' | Creator: {creator_name} ({creator_id}) | Vis: {w.get('visibility')} | Status: {w.get('status')}")
