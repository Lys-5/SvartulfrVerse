import sys
import json
import requests
import re
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
    # Wyvern saves characters using PUT /api/worlds/{world_id}/characters/{char_id}
    # (Or sometimes /api/worlds/characters/{char_id}, let's try the one that worked for the subagent)
    url = f"{API_BASE}/worlds/characters/{char_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    # In some platforms PUT requires partial payload
    resp = requests.put(url, headers=headers, json=payload)
    if resp.status_code == 404:
        # Fallback to the other endpoint format
        url2 = f"{API_BASE}/worlds/{WORLD_ID}/characters/{char_id}"
        resp = requests.put(url2, headers=headers, json=payload)
    return resp.status_code, resp.text

def parse_jed_proposal():
    with open(r'd:\SvartulfrVerse\docs\Douglas_Family_JED_Proposal.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    chars_data = {}
    
    # Split by '## ' which indicates a character section
    sections = content.split('## ')
    for sec in sections:
        if not sec.strip():
            continue
        lines = sec.split('\n')
        name = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        
        # basic cleanup of the extra trailing ']'
        body = re.sub(r'\]\n\n\]$', ']', body)
        
        # Only add valid cast
        if name in ["Erik", "Malachia", "Jasper", "Noah", "Wulfnic", "Logan"]:
            chars_data[name] = body
            
    return chars_data

def main():
    token = get_auth_token()
    chars = get_all_characters(token)
    jed_data = parse_jed_proposal()
    
    for name, jed_text in jed_data.items():
        # Find character in wyvern
        target = None
        for c in chars:
            display = c.get('display_name', '') or ''
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
