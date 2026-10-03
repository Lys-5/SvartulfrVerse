import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
for l in data['world_locations']:
    parent = l.get('parent_location')
    if parent:
        p_id = parent.get('id') if isinstance(parent, dict) else parent
        safe_name = l['name'].encode('ascii', 'replace').decode('ascii')
        print(f"{safe_name:45} -> parent: {p_id}")
