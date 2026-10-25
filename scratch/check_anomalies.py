import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    s = json.load(f)

for eid in ['NQd7n3QacMcK-TzowQ2LE', 'oov5UWuVhZ3RGgoxMkaTS', 'Og7V6v67guXXAaP0_PsTM']:
    for e in s['lexicon']:
        if e.get('entry_id') == eid:
            print('***', e.get('name'), '***')
            print(e.get('content'))
            print('-------------------')
