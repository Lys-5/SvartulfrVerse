import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
lexicon = d.get('world_lexicon_entries', [])

print("=== ALL 20 ORGANIZATION/FACTION ENTRIES ===")
for item in lexicon:
    if item.get('type') == 'organization/faction':
        print(f"  * {item.get('name')} ({item.get('id')})")

print("\n=== ALL 36 ITEM ENTRIES ===")
for item in lexicon:
    if item.get('type') == 'item':
        print(f"  * {item.get('name')} ({item.get('id')})")

print("\n=== ALL 32 MEMORY ENTRIES ===")
for item in lexicon:
    if item.get('type') == 'memory':
        att = item.get('attached_world_character_id')
        print(f"  * {item.get('name')} ({item.get('id')}) -> attached: {att}")

print("\n=== CREATURE ENTRIES ===")
for item in lexicon:
    if item.get('type') == 'creature':
        print(f"  * {item.get('name')} ({item.get('id')})")
