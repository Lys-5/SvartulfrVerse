import json
import re

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cabin_map = {}
for e in data.get('entries', []):
    content = e.get('content', '')
    name = e.get('name')
    # Search for Cabin X or Cabina X
    m = re.search(r'(Cabin\s+[A-Za-z0-9\-]+|Moonflower|Ironwood)', content, re.IGNORECASE)
    if m:
        cab = m.group(1)
        cabin_map.setdefault(cab, []).append(name)

for cab, members in cabin_map.items():
    print(f"{cab}: {len(members)} campers -> {members[:3]}...")
