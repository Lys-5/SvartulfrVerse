import json

with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    card = json.load(f)

for k, v in card.items():
    if isinstance(v, (dict, list)):
        print(f"Key {k} (type {type(v)}): {str(v)[:150]}")
    elif isinstance(v, str) and (len(v) == 22 or len(v) == 24 or v.startswith('_')):
        print(f"Key {k} = {v}")
