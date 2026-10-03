import sys
import json
import requests
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def create_character(token, name, description):
    url = f"{API_BASE}/worlds/characters"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'world_id': WORLD_ID,
        'display_name': name,
        'name': name,
        'description': description,
        'is_global': True
    }
    resp = requests.post(url, headers=headers, json=payload)
    return resp.status_code, resp.json() if resp.status_code == 200 else resp.text

def main():
    token = get_auth_token()
    
    try:
        with open(r'd:\SvartulfrVerse\docs\GroupA_JED.json', 'r', encoding='utf-8') as f:
            group_a_data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return
    
    for name, jed_text in group_a_data.items():
        print(f"Creating {name}...")
        
        status, data = create_character(token, name, jed_text)
        if status in [200, 201]:
            char_id = data.get('id') or data.get('_id')
            print(f"Successfully created {name}! (ID: {char_id})")
        else:
            print(f"Failed to create {name}: {status} {data}")
            
        time.sleep(1)

if __name__ == '__main__':
    main()
