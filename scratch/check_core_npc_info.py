import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

target_names = ['Erik', 'Logan', 'Jasper', 'Alyssa', 'Malachia', 'Noah', 'Wulfnic', 'Kaladin', 'Marcus', 'Nixara']
for e in data['lexicon']:
    if any(tn in e['name'] for tn in target_names):
        print(f"{e['name']}:")
        print('  keys:', e.get('keys'))
        print('  npc_info:', e.get('npc_info'))
        print('  ignored_characters:', e.get('ignored_characters'))
        print('  ignored_personas:', e.get('ignored_personas'))
        print('  avatar:', e.get('avatar'))
        print()
