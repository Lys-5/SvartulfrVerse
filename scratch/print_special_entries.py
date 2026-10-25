import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    prim = json.load(f)['entries']

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec = json.load(f)['entries']

print("=== PRIMARY SPECIAL ===")
for idx in [5, 24, 25]:
    print(f"--- [{idx}] {prim[idx]['name']} ---")
    print(prim[idx]['content'])

print("=== SECONDARY SPECIAL ===")
for idx in [19, 29, 30, 31, 32, 33, 34, 35, 36, 37, 69, 90]:
    print(f"--- [{idx}] {sec[idx]['name']} ---")
    print(sec[idx]['content'])
