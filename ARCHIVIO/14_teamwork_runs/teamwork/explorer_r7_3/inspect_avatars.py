import json
from collections import Counter

files = [
    ('Primary', 'FINAL/Svartulfr_NPC_Primary.json'),
    ('Secondary', 'FINAL/Svartulfr_NPC_Secondary.json')
]

for name, path in files:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('entries', [])
    lexicon = data.get('lexicon', [])
    print(f"=== {name} ({path}) ===")
    print(f"id: {data.get('id')}")
    print(f"name: {data.get('name')}")
    print(f"photoURL: {data.get('photoURL')}")
    print(f"token_budget: {data.get('token_budget')}")
    print(f"entries count: {len(entries)}, lexicon count: {len(lexicon)}")
    
    # Check entries avatars
    avatars = [e.get('avatar') for e in entries]
    avatar_counts = Counter(avatars)
    print(f"Total entries: {len(entries)}")
    print(f"Unique avatar URLs: {len(avatar_counts)}")
    
    # Check empty, null, or placeholder
    old_placeholder = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"
    new_placeholder = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"
    
    old_ph_count = sum(1 for a in avatars if a == old_placeholder)
    new_ph_count = sum(1 for a in avatars if a == new_placeholder)
    none_or_empty = sum(1 for a in avatars if not a)
    custom_count = len(avatars) - old_ph_count - new_ph_count - none_or_empty
    
    print(f"Old crest placeholder ({old_placeholder}): {old_ph_count}")
    print(f"New DCC placeholder ({new_placeholder}): {new_ph_count}")
    print(f"None or empty avatars: {none_or_empty}")
    print(f"Custom / distinct avatars: {custom_count}")
    
    print("\nTop 10 avatar URLs:")
    for url, count in avatar_counts.most_common(10):
        print(f"  [{count}] {url}")
    print("-" * 50)
