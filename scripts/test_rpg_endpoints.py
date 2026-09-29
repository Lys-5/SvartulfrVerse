import urllib.request
import json
import sys
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def test_endpoints():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    
    candidates = [
        f'https://app.wyvern.chat/api/worlds/blueprints',
        f'https://app.wyvern.chat/api/worlds/{world_id}/blueprints',
        f'https://app.wyvern.chat/api/rpg/species',
        f'https://app.wyvern.chat/api/rpg/occupations',
        f'https://app.wyvern.chat/api/worlds/rpg',
        f'https://app.wyvern.chat/api/worlds/{world_id}/rpg-stats',
        f'https://app.wyvern.chat/api/worlds/rpg-stats',
        f'https://app.wyvern.chat/api/rpg/classes',
        f'https://app.wyvern.chat/api/rpg',
        f'https://app.wyvern.chat/api/species',
        f'https://app.wyvern.chat/api/traits',
        f'https://app.wyvern.chat/api/worlds/traits',
        f'https://app.wyvern.chat/api/worlds/{world_id}/traits',
        f'https://app.wyvern.chat/api/items',
        f'https://app.wyvern.chat/api/worlds/items',
        f'https://app.wyvern.chat/api/worlds/{world_id}/items'
    ]
    
    for url in candidates:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                print(f"200 OK: {url} -> {type(data)} {list(data.keys()) if isinstance(data, dict) else len(data)}")
        except urllib.error.HTTPError as e:
            if e.code != 404:
                print(f"{e.code}: {url}")
        except Exception as e:
            pass

if __name__ == '__main__':
    test_endpoints()
