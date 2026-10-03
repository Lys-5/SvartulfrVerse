import json

data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
for e in data['world_lexicon_entries']:
    if e.get('type') == 'memory':
        attached = e.get('attached_world_character_id')
        safe_name = e['name'].encode('ascii', 'replace').decode('ascii')
        print(f"{e['id']} | {safe_name:45} | attached: {attached}")
