import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
no_parent = [l for l in data['world_locations'] if not l.get('parent_location')]
print(f"Locations without parent: {len(no_parent)}")
for l in no_parent:
    safe_name = l['name'].encode('ascii', 'replace').decode('ascii')
    print(f"{l['id']} | {safe_name}")
