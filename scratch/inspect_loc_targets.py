import json

with open('FINAL/Svartulfr_Location.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total location entries: {len(d.get('entries', []))}")

loc_targets = ['Bricklane', 'Solarton Square', 'Sidewinder', 'Solarton']

for e in d['entries']:
    name = e.get('name', '')
    if any(t.lower() in name.lower() for t in loc_targets):
        print(f"=== LOC: {name} (id: {e.get('id')}) ===")
        print(f"Keys: {e.get('keys')}")
        print(f"Content:\n{e.get('content')}\n")
