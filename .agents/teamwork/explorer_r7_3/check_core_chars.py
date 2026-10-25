import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary = json.load(f)

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    secondary = json.load(f)

core_keys_primary = [
    'Erik Ulfr Douglas',
    'Malachia Björn Douglas Bloodmoon',
    'Noah Loki Douglas Bloodmoon',
    'Logan Járn Douglas',
    'Wulfnic Báleygr Bloodmoon',
    'Mackenzie Sanchez-Rogers'
]

print("=== Core Characters in Primary ===")
for e in primary.get('entries', []):
    name = e.get('name')
    for k in core_keys_primary:
        if k in name or (e.get('keys') and any(k.lower() in x.lower() for x in e.get('keys'))):
            print(f"Name: {name}")
            print(f"  id: {e.get('id')}")
            print(f"  type: {e.get('type')}")
            print(f"  avatar: {e.get('avatar')}")
            print(f"  ignored_characters: {e.get('ignored_characters')}")
            print(f"  desc length: {len(e.get('description', ''))}")
            break

print("\n=== Edric in Secondary ===")
for e in secondary.get('entries', []):
    name = e.get('name', '')
    if 'edric' in name.lower() or (e.get('keys') and any('edric' in x.lower() for x in e.get('keys'))):
        print(f"Name: {name}")
        print(f"  id: {e.get('id')}")
        print(f"  type: {e.get('type')}")
        print(f"  avatar: {e.get('avatar')}")
        print(f"  ignored_characters: {e.get('ignored_characters')}")
        print(f"  desc length: {len(e.get('description', ''))}")
