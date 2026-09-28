import json

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])

council_targets = [
    'Erik Douglas',
    'Cass Harrow',
    'Naomi Black',
    'Darius Vale',
    'Bianca Rossi',
    'Dominic Chen',
    'Aurora Night',
    'Eclipse Noir',
    'Marcus O\'Connor',
    'Isobel Blackwater',
    'Helena Weiss',
    'Vito Marino',
    'Angelo Moreno',
    'Federico Savini',
    'Harlan Beaumont',
    'Zeera',
    'Brak Ironfist',
    'Barrow',
    'Harrison Black',
    'Abel Vilas',
    'Cassian Aralas',
    'Marlowe Voss'
]

print("--- Council Search in world_characters ---")
for ct in council_targets:
    found = [c for c in chars if ct.lower() in (c.get('display_name') or '').lower() or ct.lower() in (c.get('name') or '').lower()]
    if found:
        print(f"FOUND: {ct} -> id: {found[0]['id']}, display_name: {found[0].get('display_name')}")
    else:
        print(f"NOT FOUND: {ct}")
