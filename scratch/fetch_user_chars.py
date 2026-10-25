import urllib.request
import pathlib
import json

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_json(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("=== FETCHING COLLECTION CHARACTERS ===")
try:
    data = fetch_json('https://app.wyvern.chat/api/inventory/collection/characters?limit=100')
    items = data.get('items', [])
    print(f"Total in collection: {len(items)}")
    for item in items:
        cid = item.get('id') or item.get('character_id')
        cname = item.get('name') or (item.get('character') and item['character'].get('name'))
        print(f"  COLLECTION: {cid} -> {cname}")
except Exception as e:
    print(f"Error fetching collection: {e}")

print("\n=== FETCHING MINE CHARACTERS ===")
try:
    data = fetch_json('https://app.wyvern.chat/api/characters/mine')
    chars = data.get('characters', [])
    print(f"Total in mine: {len(chars)}")
    for c in chars:
        print(f"  MINE: {c.get('id')} -> {c.get('name')}")
except Exception as e:
    print(f"Error fetching mine: {e}")
