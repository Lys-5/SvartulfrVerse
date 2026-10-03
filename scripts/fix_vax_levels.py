import sys, json, requests
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'
token = get_auth_token()

def get_level(age):
    if age <= 13:
        return 1
    lvl = 1 + ((age - 13) // 5)
    return min(lvl, 99)

targets = {
    "Zeera Darkfire": get_level(29), # 4
    "Aras Darkfire": get_level(32), # 4
    "Karshin Darkfire": get_level(30), # 4
    "Boros Darkfire": get_level(35), # 5
    "Varg Darkfire": get_level(800) # 99
}

print(targets)

# Fetch all characters to find their IDs
resp = requests.get(f'{API_BASE}/worlds/characters/world/{WORLD_ID}', headers={'Authorization': f'Bearer {token}'})
chars = resp.json()

headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

for c in chars:
    name = c.get('display_name', '')
    if name in targets:
        char_id = c.get('id')
        
        # We must fetch the full character to retain other stats
        char_resp = requests.get(f'{API_BASE}/worlds/characters/{char_id}', headers=headers)
        char_data = char_resp.json()
        
        rpg_stats = char_data.get('rpg_stats', {})
        rpg_stats['level'] = targets[name]
        
        payload = {'rpg_stats': rpg_stats}
        put_resp = requests.put(f'{API_BASE}/worlds/characters/{char_id}', headers=headers, json=payload)
        print(f'Updated {name} to level {targets[name]}: {put_resp.status_code}')
