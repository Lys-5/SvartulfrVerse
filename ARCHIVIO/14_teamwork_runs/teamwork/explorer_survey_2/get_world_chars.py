import urllib.request
import json
import pathlib

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
req = urllib.request.Request(
    'https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ',
    headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
)
try:
    resp = urllib.request.urlopen(req)
    chars = json.loads(resp.read().decode('utf-8'))
    print(f"Total world characters in _YpX47fNraQFw2dD7TdycJ: {len(chars)}")
    for c in chars:
        print(f"  id={c.get('id')} name={c.get('name')!r} first_name={c.get('first_name')!r} display_name={c.get('display_name')!r} nicknames={c.get('nicknames')}")
except Exception as e:
    print("Error:", e)
