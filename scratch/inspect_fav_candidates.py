import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ARCHIVIO/janitor_sources/janitor_favorites_candidates.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('characters', [])
print(f"Total favorite characters in Janitor export: {len(chars)}")

with open('scratch/all_57_favorites.txt', 'w', encoding='utf-8') as out:
    for idx, c in enumerate(chars):
        name = c.get('name', 'Unknown')
        creator = c.get('creator_name', 'Unknown')
        cid = c.get('id', '')
        line = f"[{idx+1:02d}] {name} (by {creator}) | ID: {cid}"
        print(line)
        out.write(line + '\n')
