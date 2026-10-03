import sys
import json
import urllib.request
import re

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'

def main():
    token = get_auth_token()
    
    # 1. Get gallery items
    url = f'https://app.wyvern.chat/api/worlds/{WORLD_ID}/gallery'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        gallery = json.loads(resp.read().decode('utf-8'))
        
    # 2. Get all characters
    with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
        export_data = json.load(f)
    chars = export_data['world_characters']
    
    # Map chars by lowercase tokens
    print(f"Total characters: {len(chars)}")
    print(f"Total gallery items: {len(gallery)}\n")
    
    avatar_items = [item for item in gallery if item.get('type') == 'avatar']
    print(f"Total avatar items in gallery: {len(avatar_items)}\n")
    
    for item in avatar_items:
        t = item.get('title', '').strip()
        img_url = item.get('imageURL', '')
        gid = item.get('id', '')
        print(f"Gallery title: {t:20s} | url: {img_url}")

if __name__ == '__main__':
    main()
