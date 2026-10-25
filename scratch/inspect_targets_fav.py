import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ARCHIVIO/janitor_sources/janitor_favorites_candidates.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('characters', [])

targets = ['Thrakgor', 'Crowe', 'Morgeth', 'Thorvald', 'Harald']

for c in chars:
    name = c.get('name', '')
    for t in targets:
        if t.lower() in name.lower():
            print(f"=== {name} (by {c.get('creator_name')}) ===")
            desc = c.get('description', '')
            print(f"Description len: {len(desc)}")
            print(desc[:500])
            print("...\n")
