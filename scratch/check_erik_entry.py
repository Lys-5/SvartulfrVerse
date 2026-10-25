import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for e in d['lexicon']:
    if e.get('entry_id') == 'C-JisFj8qA1tsFEqZKevk':
        for k, v in e.items():
            if k != 'content':
                print(f"{k}: {v}")
        print("content (first 100 chars):", e.get('content')[:100])
