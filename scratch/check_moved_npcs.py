import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec = json.load(f)

test_names = ['Alicia Virtuoso', 'Allegra Lumsden', 'Rick Howell', 'Adrian Locke', 'Aiden Anderson']
for e in sec['entries']:
    name = e.get('name')
    if name in test_names:
        print(f"\n--- {name} in FINAL/Svartulfr_NPC_Secondary.json ---")
        content = e.get('content', '')
        for line in content.split('\n'):
            if 'AGE:' in line:
                print(f"  {line.strip()[:100]}")
