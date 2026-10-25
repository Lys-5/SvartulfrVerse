import urllib.request
import urllib.parse
import json
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

names = ['Rory Ballantine', 'Ruaraidh', 'Sully Jones', 'Jean-Luc Virtuoso', 'Arthur Sinclair', 'Alicia Virtuoso', 'Ilya Volkov', 'Vasile Ionescu', 'Barrow', 'Marek', 'Radek']

for name in names:
    q = urllib.parse.quote(name)
    url = f'https://app.wyvern.chat/api/characters?search={q}&limit=5'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data if isinstance(data, list) else data.get('items', []) or data.get('characters', [])
            print(f"Search '{name}': {len(items)} results")
            for item in items[:3]:
                print(f"  -> {item.get('id')} | {item.get('name')} | Creator: {item.get('creator', {}).get('displayName')}")
    except Exception as e:
        print(f"Search '{name}' ERROR: {e}")
