import json

with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    card = json.load(f)

print("=== FINAL/Edric_Douglas_card.json ===")
for k in ['id', 'name', 'display_name']:
    print(k, ':', card.get(k))

for field in ['long_summary', 'description', 'personality', 'first_mes', 'rpg_stats']:
    if field in card:
        print(f"--- {field} ---")
        print(str(card[field])[:800])
