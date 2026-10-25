import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx in [111, 112, 113, 114, 115, 151, 152, 153, 154, 155]:
    e = data['entries'][idx]
    print(f"=== NPC {idx}: {e.get('comment')} ===")
    for line in e.get('content', '').split('\n'):
        if any(w in line for w in ['AFFILIATION', 'Moonflower', 'Ironwood', 'Lake Wolf', 'Jasper', 'Alyssa', 'Edric', 'Rylan']):
            print("  ", line[:150])
