import json
import urllib.request
from pathlib import Path

ROOT = Path('e:/repository/SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = TOKEN_PATH.read_text(encoding='utf-8').strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
world_id = "_YpX47fNraQFw2dD7TdycJ"
url = f"https://app.wyvern.chat/api/worlds/characters/world/{world_id}"

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    chars = json.loads(resp.read().decode('utf-8'))

print(f"Total World Characters in World {world_id}: {len(chars)}")
for c in chars:
    print(f"  - {c.get('name')} | Display: {c.get('display_name')} | ID: {c.get('id')}")

tags_0 = ['Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Jasper', 'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett']
print("\nMapping Scene 0 tags:")
for tag in set(tags_0):
    if tag == 'Narrator':
        print(f"  Tag '{tag}' -> Built-in VN System Narrator")
    else:
        matches = [c for c in chars if tag.lower() in c.get('name', '').lower() or tag.lower() in (c.get('display_name') or '').lower()]
        if matches:
            m = matches[0]
            print(f"  Tag '{tag}' -> World Character: {m.get('name')} (ID: {m.get('id')})")
        else:
            print(f"  Tag '{tag}' -> UNMATCHED!")
