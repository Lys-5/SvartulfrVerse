import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
for l in data['world_locations']:
    name = l.get('name')
    parent = l.get('parent_location')
    if 'villa douglas:' in name.lower() or 'jasper\'s cavern' in name.lower():
        p_id = parent.get('id') if isinstance(parent, dict) else parent
        print(f"{l['id']} | {name:45} | parent: {p_id}")
