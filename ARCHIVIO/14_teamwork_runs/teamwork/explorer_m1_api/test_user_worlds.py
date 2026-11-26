import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

url = "https://app.wyvern.chat/api/worlds/user/2r4fVpvImte5dbljedLkZJxre2d2"
req = urllib.request.Request(url, headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
})

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("User worlds response status:", resp.status)
    if isinstance(data, dict):
        print("Dict keys:", list(data.keys()))
        worlds = data.get('worlds', [])
        print(f"Total worlds found: {len(worlds)}")
        for w in worlds:
            print(f"  - ID: {w.get('id')} | Name: '{w.get('name')}' | Visibility: {w.get('visibility')} | Age: {w.get('world_age')}")
    elif isinstance(data, list):
        print(f"List of {len(data)} worlds:")
        for w in data:
            print(f"  - ID: {w.get('id')} | Name: '{w.get('name')}'")
