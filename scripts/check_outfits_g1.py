import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))

targets = {
    'Nixara Bloodmoon': '_fmzBDjDn3Gnq2hXKy7tY6',
    'Marcus Thornfield': '_PCC1PLfcGrdw2VfMnhVcL',
    'Magnus Douglas III': '_jeJTbxLcrYWXNWYPDx4ph',
    'Lord Cornelius Douglas': '_rJKYcCt61hQa8XRamHEdM',
    'Elizabeth Duskwood': '_EwPN1te7qtUKYEx4NLgag',
    'Wulfnic Bloodmoon': '_W9PLYt9ERTBJBXqKQL2en',
    'Zefir Hvitskog': '_FJhtBq4xUM4aUWpaJAPYF',
    'Ut Berg': '_NYtBzeKNkm3pedHMnYaka',
    'Kaladin Nargathon': '_b7QqV43D8pU1tewx4qenY',
}

for name, cid in targets.items():
    c = next((x for x in d['world_characters'] if x['id'] == cid), None)
    if not c:
        print(f'{name}: NOT FOUND')
        continue
    outfits = c.get('outfits', [])
    print(f'\n=== {name} ({len(outfits)} outfits) ===')
    for o in outfits:
        desc = o.get('description', '')
        name_o = o.get('name', '')
        if len(desc) < 80:
            print(f'  [SHORT] [{name_o}] len={len(desc)}: {desc}')
        else:
            print(f'  [OK]    [{name_o}] len={len(desc)}: {desc[:80]}...')
