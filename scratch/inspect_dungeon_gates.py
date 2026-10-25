import json

with open('FINAL/Svartulfr_Lorebook_II.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for e in d['entries']:
    if 'Dungeon Gates' in e.get('name', ''):
        print(f"Name: {e.get('name')}")
        print(f"Keys: {e.get('keys')}")
        print(f"Content:\n{e.get('content')}\n")
