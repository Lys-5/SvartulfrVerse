import json

files = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Location.json'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    avatars = [e.get('avatar') for e in d.get('entries', []) if 'avatar' in e]
    print(f"{f}: has {len(avatars)} entries with 'avatar' key. Samples: {set(avatars[:10])}")
