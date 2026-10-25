import json

d = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
entries = d.get('entries', [])
print(f"Total entries in NPC Primary: {len(entries)}")
target_ids = {
    '4NzXF4_0hYxmN7Idltzpw': 'Scarlett Rose',
    'ijy8vrlphNv19-p-gbYuY': 'Sierra Cruz',
    'YCxAqNoShpefVvk0_Pc7i': 'Russell Sinclair',
    'ekdQjq63xP7HtNuaPQJQE': 'Stanley Davies Jr.',
    'RM6rcwv8MlY1XWaCTQp0M': 'Jared Thompson',
    'alyssa_world_dossier_2b54a223': 'Alyssa World Dossier'
}
found = {}
for e in entries:
    eid = e.get('entry_id') or e.get('id')
    if eid in target_ids:
        content = e.get('content', '') or e.get('description', '')
        found[eid] = e
        print(f"{target_ids[eid]} ({eid}):")
        print(f"  name: {e.get('name')}")
        print(f"  type: {e.get('type')}")
        print(f"  selective: {e.get('selective')}")
        print(f"  content_len: {len(content)}")
        print(f"  keys: {e.get('keys')}")
        print(f"  secondary_keys: {e.get('secondary_keys')}")
        print(f"  avatar: {e.get('avatar')}")
        print(f"  custom_avatar_regex: {e.get('custom_avatar_regex')}")
        print(f"  avatar_activation_regex: {e.get('avatar_activation_regex')}")

missing = set(target_ids.keys()) - set(found.keys())
if missing:
    print(f"MISSING IDs: {missing}")
