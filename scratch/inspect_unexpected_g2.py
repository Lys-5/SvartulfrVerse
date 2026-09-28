"""
Inspect the 14 unexpected G2 characters to determine their correct group.
"""
import json

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
char_map = {c['id']: c for c in chars}

# The 14 unexpected IDs
unexpected = {
    '_kP1gWeyLw9jKbz3Xf73GH': 'Marek',
    '_a6KYGdN3BWTgbYEbT4mx8': 'Zeera',
    '_LMBDb78CUFJ2wMPpXQgYy': 'Professor Kiwetin',
    '_xDFyKfnKEfKWA9NdVhVV7': 'Naomi Black',
    '_9J8jRp16w6NbjTWfeqTXy': 'Marlowe Voss',
    '_ejE6Xp83PhtJrDKCqbjhH': 'Harrison Black',
    '_ErE1aA4ychtDkNqGYtzpc': 'Harlow MacGregor',
    '_AjMH4N66RxKj2Pr84wqgz': 'Harlan Beaumont',
    '_CzjGd8k87dKNdFUgLNV8z': 'Emil',
    '_R6XD6qLdQTrm7F3nd2j1V': 'Darius Vale',
    '_FjnaULjNgMhbct6pFXqPN': 'Charles "Charlie" DeVille',
    '_GBPCNEWLL2NmdaWAhg6Cn': 'Cassian Aralas',
    '_AycV4d9dJRBakCmdH4q4J': 'Brak Ironfist',
    '_LEeEzdCCyGjQ8kfVkcra8': 'Barrow',
}

# Content folders
folders = data.get('content_folders', [])
folder_map = {}
for f_entry in folders:
    fid = f_entry.get('id', '')
    fname = f_entry.get('name', '')
    for cid in f_entry.get('character_ids', []):
        folder_map[cid] = fname

for uid, uname in unexpected.items():
    c = char_map.get(uid)
    if not c:
        print(f"\n{uname}: NOT FOUND in world_characters")
        continue
    
    name = c.get('display_name') or c.get('name') or ''
    ls = (c.get('long_summary') or '')[:300]
    s = (c.get('summary') or '')[:200]
    folder = folder_map.get(uid, 'NONE')
    
    print(f"\n{'='*60}")
    print(f"NAME: {name}")
    print(f"ID: {uid}")
    print(f"FOLDER: {folder}")
    print(f"LONG_SUMMARY ({len(c.get('long_summary') or '')} chars):")
    print(f"  {ls}...")
    print(f"SUMMARY ({len(c.get('summary') or '')} chars):")
    print(f"  {s}...")
