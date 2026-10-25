import json

with open('scratch/inbox/mine_inventory.json', 'r', encoding='utf-8') as f:
    inv = json.load(f)

for item in inv:
    name = item.get('name') or item.get('display_name') or ''
    if 'Edric' in name:
        print(f"Mine item: ID={item.get('id')} NAME={name} TYPE={item.get('type')}")

with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    card = json.load(f)

print("=== FINAL/Edric_Douglas_card.json ===")
print("Keys:", list(card.keys()))
for field in ['name', 'display_name', 'long_summary', 'description', 'personality', 'first_mes', 'rpg_stats']:
    if field in card:
        val = str(card[field])
        print(f"--- {field} ---")
        print(val[:500])
