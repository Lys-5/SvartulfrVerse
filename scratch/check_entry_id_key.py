import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
e = d['lexicon'][0]
print("Keys of entry in Primary:", list(e.keys()))
for i, entry in enumerate(d['lexicon']):
    name = entry.get('name')
    if any(n in name for n in ['Erik', 'Malachia', 'Noah', 'Logan', 'Wulfnic', 'Mackenzie']):
        print(f"[{i}] id={entry.get('id')} entry_id={entry.get('entry_id')} name={name}")
