import urllib.request
import json
import sys
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def scan():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    url = f'https://app.wyvern.chat/api/worlds/characters/world/{world_id}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chars = json.loads(resp.read().decode('utf-8'))
    print(f'Total live characters: {len(chars)}')

    sample_names = ['Harlan Beaumont', 'Zeera', 'Bailey Rogers', 'Harrison Black', 'Malachia Douglas Bloodmoon', 'Jasper Douglas Bloodmoon', 'Alyssa Douglas Bloodmoon']
    for c in chars:
        name = c.get('display_name')
        if any(sn in name for sn in sample_names):
            cid = c.get('id')
            cur_url = f'https://app.wyvern.chat/api/worlds/characters/{cid}'
            r = urllib.request.Request(cur_url, headers=headers)
            with urllib.request.urlopen(r) as cr:
                detail = json.loads(cr.read().decode('utf-8'))
            rs = detail.get('rpg_stats')
            print(f"- {name} ({cid}): rpg_stats={rs is not None}")
            if rs:
                print(f"    detail: level={rs.get('level')}, species={rs.get('species_id')}, occ={rs.get('occupation_id')}, stats={rs.get('base_stats')}")

if __name__ == '__main__':
    scan()
