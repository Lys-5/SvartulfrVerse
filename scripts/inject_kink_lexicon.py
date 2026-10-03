import sys
import json
import requests
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def inject_lexicon(token, filepath):
    url = f"{API_BASE}/worlds/lexicon"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        entries = json.load(f)
        
    for entry in entries:
        entry['world_id'] = WORLD_ID
        if 'is_global' in entry and isinstance(entry['is_global'], str):
            entry['is_global'] = entry['is_global'].lower() == 'true'
            
        resp = requests.post(url, headers=headers, json=entry)
        if resp.status_code in [200, 201]:
            print(f"Created Lexicon: {entry['name']}")
        else:
            print(f"Failed {entry['name']}: {resp.status_code} {resp.text}")
        time.sleep(1)

if __name__ == '__main__':
    inject_lexicon(get_auth_token(), r'd:\SvartulfrVerse\docs\Kinks_Lexicon.json')
