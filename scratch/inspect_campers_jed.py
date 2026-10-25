import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx in [111, 112, 113, 114, 115, 151, 152, 153, 154, 155]:
    e = data['entries'][idx]
    first_line = e.get('content', '').split('\n')[0]
    print(f"IDX {idx}: {first_line}")
