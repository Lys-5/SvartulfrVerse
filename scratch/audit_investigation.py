import json

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

print('=== PRIMARY ENTRIES WITH IGNORED FIELDS ===')
for e in prim['lexicon']:
    ic = e.get('ignored_characters')
    ip = e.get('ignored_personas')
    if ic or ip:
        print(f"{e.get('name')} ({e.get('entry_id')}): chars={ic}, personas={ip}")

print('\n=== SECONDARY ENTRIES WITH IGNORED FIELDS ===')
for e in sec['lexicon']:
    ic = e.get('ignored_characters')
    ip = e.get('ignored_personas')
    if ic or ip:
        print(f"{e.get('name')} ({e.get('entry_id')}): chars={ic}, personas={ip}")
