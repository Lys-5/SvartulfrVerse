import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars_with_empty = []
for c in d['world_characters']:
    empty = [o for o in c.get('outfits', []) if len(o.get('description', '')) == 0]
    if empty:
        chars_with_empty.append((c['display_name'], c['id'], [o['name'] for o in empty]))

print(f'Total chars with empty outfits: {len(chars_with_empty)}')
print(f'Total empty outfit slots: {sum(len(e[2]) for e in chars_with_empty)}')
print()
for name, cid, slots in chars_with_empty:
    print(f'{name} ({cid}):')
    for s in slots:
        print(f'  - {s}')
