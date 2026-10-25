import json

with open('FINAL/Svartulfr_Lorebook_III.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for e in data['entries']:
    if 'Ballantine' in e.get('name', ''):
        print(f"Name: {e.get('name')}")
        print(f"Content: {e.get('content')}")
