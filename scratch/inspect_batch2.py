import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])

batch2 = [
    'Garrett Locke', 'Roger', 'Harlow MacGregor', 'Bram Beaumont',
    'Atlas Teague', 'Arthur Grey', 'Jake Thompson', 'Kîwêtin',
    'Vargus', 'Sawyer Shephard'
]

for name in batch2:
    matches = [c for c in chars if name.lower() in (c.get('display_name') or '').lower()]
    for c in matches:
        dn = c.get('display_name')
        ls = c.get('long_summary') or ''
        s = c.get('summary') or ''
        first_line = ls.split('\n')[0] if ls else s.split('\n')[0]
        print(f"{dn:30s} | ID: {c.get('id'):22s} | LS: {len(ls):4d} | Header: {first_line[:70]}")
