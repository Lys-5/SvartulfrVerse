import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    w = json.load(f)

chars = w.get('world_characters', [])
with_bd = [c for c in chars if c.get('birthdate') is not None]
print(f"Total chars: {len(chars)}")
print(f"Chars with birthdate: {len(with_bd)}")
for c in with_bd:
    print(f"{c.get('display_name'):35s} | bd: {c.get('birthdate')} | st: {c.get('start_timeline_position')}")
