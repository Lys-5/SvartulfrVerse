import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx, e in enumerate(data.get('entries', [])):
    t = json.dumps(e, ensure_ascii=False)
    hits = []
    if 'Ironwood' in t: hits.append('Ironwood')
    if 'Moonflower' in t: hits.append('Moonflower')
    if 'Rylan' in t: hits.append('Rylan')
    if hits:
        print(f"NPC idx {idx}: {e.get('comment')} -> {hits}")
