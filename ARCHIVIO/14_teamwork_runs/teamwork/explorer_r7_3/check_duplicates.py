import json
from collections import Counter

for name, path in [('Primary', 'FINAL/Svartulfr_NPC_Primary.json'), ('Secondary', 'FINAL/Svartulfr_NPC_Secondary.json')]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {name} ({path}) ===")
    entries = data.get('entries', [])
    for e in entries:
        avatar = e.get('avatar')
        if avatar == 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public':
            print(f"  [Shared c8bdfad3] {e.get('name') or (e.get('keys') and e.get('keys')[0])}: {avatar}")
        if avatar == 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/650ea6f4.jpg?v=2881d07e':
            print(f"  [Shared 650ea6f4] {e.get('name') or (e.get('keys') and e.get('keys')[0])}: {avatar}")
