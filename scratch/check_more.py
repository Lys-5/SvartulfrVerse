import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    s = json.load(f)

for name in ['Jerry Thompson', 'Jeremy Thompson', 'Jason Thompson', 'Eira Elloway', 'Vespera Thorne']:
    for e in s['lexicon']:
        if e.get('name') == name:
            print('***', e.get('name'), '***')
            print(e.get('content')[:300])
            print('-------------------')
