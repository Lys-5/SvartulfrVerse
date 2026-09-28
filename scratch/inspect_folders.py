import json

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
real_chars = [c for c in chars if len(c.get('long_summary') or '') > 100]

# Check folders or metadata
char_dict = {c['id']: c for c in real_chars}

# Let's see what content_folders exist
folders = data.get('content_folders', {}).get('world_characters', [])
folder_map = {}
for f in folders:
    fname = f.get('name')
    for cid in f.get('character_ids', []):
        folder_map[cid] = fname

for c in real_chars:
    c['folder'] = folder_map.get(c['id'], 'Unassigned')

# Print count by folder
from collections import Counter
counts = Counter([c['folder'] for c in real_chars])
print("Folder counts among real characters:")
for k, v in counts.items():
    print(f"  {k}: {v}")
