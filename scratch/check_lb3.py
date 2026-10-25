import json

with open('FINAL/Svartulfr_Lorebook_III.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])
print(f"Lorebook III total entries: {len(entries)}")
for idx, e in enumerate(entries):
    keys = e.get('keys', '')
    if isinstance(keys, list):
        keys = ', '.join(keys)
    print(f"{idx+1}. {e.get('name', 'Unnamed')} (keys: {keys[:40]})")
