import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
for s in data['world_scenarios']:
    loc = s.get('location')
    loc_id = loc.get('id') if isinstance(loc, dict) else loc
    loc_name = loc.get('name') if isinstance(loc, dict) else 'None'
    safe_name = s['name'].encode('ascii', 'replace').decode('ascii')
    safe_loc_name = loc_name.encode('ascii', 'replace').decode('ascii')
    print(f"{s['id']} | {safe_name[:40]:40} | loc: {safe_loc_name} ({loc_id})")
