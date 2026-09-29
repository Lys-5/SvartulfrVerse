import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])

batch2_names = [
    'Roger', 'Harlow MacGregor', 'Arthur Grey', 'Jake Thompson', 
    'Dryden', 'Vargus', 'Sawyer Shephard'
]

for name in batch2_names:
    matches = [c for c in chars if name.lower() in (c.get('display_name') or '').lower()]
    for c in matches:
        dn = c.get('display_name')
        cid = c.get('id')
        ls = c.get('long_summary', '')
        s = c.get('summary', '')
        print('='*50)
        print(f"{dn} (ID: {cid})")
        print('Header:', ls.split('\n')[0] if ls else 'NO LS')
        text = ls if ls else s
        lines = [l for l in text.split('\n') if l.strip()]
        for l in lines[1:4]:
            print('  ', l[:100])
