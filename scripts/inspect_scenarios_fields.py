import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    w = json.load(f)

scenarios = w.get('world_scenarios', [])
print(f"Found {len(scenarios)} scenarios:")
for s in scenarios:
    print(f"Scenario ID: {s.get('id')}, Name: {s.get('name')}")
    print("Keys:", [k for k in s.keys() if 'field' in k or 'intro' in k])
    if 'fields' in s:
        print("   fields:", s.get('fields'))
    else:
        print("   'fields' key does not exist yet on scenario object")
