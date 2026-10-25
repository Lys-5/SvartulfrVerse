import json

with open('FINAL/Svartulfr_Location.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

e = data['entries'][209]
for k, v in e.items():
    if k != 'content':
        print(f"{k}: {v}")
