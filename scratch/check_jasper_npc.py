import json

primary = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8')).get('entries', [])
secondary = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8')).get('entries', [])

for e in primary + secondary:
    name = e.get('name', '')
    if 'jasper' in name.lower():
        print(f"Jasper entry: {e.get('entry_id')} | {name} | type: {e.get('type')} | keys: {e.get('keys')} | sec_keys: {e.get('secondary_keys')} | sel: {e.get('selective')}")
