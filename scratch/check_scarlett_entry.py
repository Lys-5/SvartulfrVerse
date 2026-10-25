import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for e in d['lexicon']:
    if e.get('name') == 'Scarlett Rose':
        for k, v in e.items():
            if k != 'content':
                print(f"{k}: {v}")
        break
