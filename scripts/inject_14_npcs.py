import sys
import json
import requests
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def get_all_characters(token):
    url = f"{API_BASE}/worlds/characters/world/{WORLD_ID}"
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get(url, headers=headers)
    return resp.json()

def update_character(token, char_id, payload):
    url = f"{API_BASE}/worlds/characters/{char_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.put(url, headers=headers, json=payload)
    if resp.status_code == 404:
        url2 = f"{API_BASE}/worlds/{WORLD_ID}/characters/{char_id}"
        resp = requests.put(url2, headers=headers, json=payload)
    return resp.status_code, resp.text

def main():
    token = get_auth_token()
    chars = get_all_characters(token)
    
    try:
        with open(r'd:\SvartulfrVerse\docs\14_NPCs_JED.json', 'r', encoding='utf-8') as f:
            jed_data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return
    
    for name, jed_text in jed_data.items():
        # Match with wyvern
        target = None
        for c in chars:
            display = c.get('display_name', '') or ''
            # Simple substring match (e.g. "Fade" in "Fade Greymoor")
            if name.lower() in display.lower():
                target = c
                break
        
        if not target:
            print(f"Could not find {name} in Wyvern.")
            continue
            
        char_id = target.get('id') or target.get('_id')
        print(f"Updating {name} ({char_id})...")
        
        payload = {
            "world_id": WORLD_ID,
            "description": jed_text
        }
        
        status, text = update_character(token, char_id, payload)
        if status in [200, 204]:
            print(f"Successfully updated {name}!")
        else:
            print(f"Failed to update {name}: {status} {text}")
            
        time.sleep(1)

if __name__ == '__main__':
    main()
