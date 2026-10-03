import sys, requests, json
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
token = get_auth_token()
resp = requests.get(f'https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}', headers={'Authorization': f'Bearer {token}'})
for c in resp.json():
    name = c.get('display_name', '')
    if 'zeera' in name.lower():
        print(f"{name} -> ID: {c.get('id')}")
