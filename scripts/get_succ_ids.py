import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

for name in ['Jared Thompson', 'Bailey Rogers', 'Janice Thompson', 'Tomas Matthews', 'Dullahan', 'Fade Greymoor']:
    match = [c for c in world_data['world_characters'] if name.lower() in (c.get('name') or c.get('display_name') or '').lower()]
    for m in match:
        print(f"{name} -> ID: {m['id']} | Current Avatar: {bool(m.get('avatar'))}")
