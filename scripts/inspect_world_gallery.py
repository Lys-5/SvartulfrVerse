import sys
import json
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'

def main():
    token = get_auth_token()
    url = f'https://app.wyvern.chat/api/worlds/{WORLD_ID}/gallery'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        items = json.loads(resp.read().decode('utf-8'))
    
    print(f"Total items in gallery: {len(items)}\n")
    for i, it in enumerate(items):
        t = it.get('title')
        typ = it.get('type')
        gid = it.get('id')
        url = it.get('imageURL')
        print(f"{i:2d} | type: {typ:12s} | title: {t} | id: {gid}")

if __name__ == '__main__':
    main()
