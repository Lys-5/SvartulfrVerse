import urllib.request
import json
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def test_put_rpg():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    alyssa_id = '_MXcEC8Y6B3BNm3b1ttHj6'
    url = f'https://app.wyvern.chat/api/worlds/characters/{alyssa_id}'
    
    payload = {
        'level': 19,
        'rpg_stats': {
            'enabled': True,
            'level': 19,
            'experience': 0,
            'species_id': None,
            'occupation_id': None,
            'base_stats': {
                'stat_1': 2,
                'stat_2': 4,
                'stat_3': 4,
                'stat_4': 7,
                'stat_5': 8,
                'stat_6': 6,
                'strength': 2,
                'endurance': 4,
                'agility': 4,
                'intelligence': 7,
                'charisma': 8,
                'luck': 6,
                'perception': 6
            }
        }
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={**headers, 'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(req) as resp:
        print(f"PUT response status: {resp.status}")
        
    # Verify with GET
    get_req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(get_req) as resp:
        verified = json.loads(resp.read().decode('utf-8'))
        
    print("VERIFIED level:", verified.get('level'))
    print("VERIFIED rpg_stats:", json.dumps(verified.get('rpg_stats'), indent=2))

if __name__ == '__main__':
    test_put_rpg()
