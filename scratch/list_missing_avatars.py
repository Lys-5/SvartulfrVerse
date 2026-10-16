import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    prim = json.load(f)

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec = json.load(f)

missing_prim = []
for idx, e in enumerate(prim['entries']):
    av = e.get('avatar')
    if not (av and isinstance(av, str) and av.strip().startswith('http')):
        missing_prim.append({
            'index': idx,
            'entry_id': e.get('entry_id'),
            'name': e.get('name'),
            'comment': e.get('comment'),
            'type': e.get('type'),
            'keys': e.get('keys'),
            'avatar': av,
            'activation_regex': e.get('avatar_activation_regex')
        })

missing_sec = []
for idx, e in enumerate(sec['entries']):
    av = e.get('avatar')
    if not (av and isinstance(av, str) and av.strip().startswith('http')):
        missing_sec.append({
            'index': idx,
            'entry_id': e.get('entry_id'),
            'name': e.get('name'),
            'comment': e.get('comment'),
            'type': e.get('type'),
            'keys': e.get('keys'),
            'avatar': av,
            'activation_regex': e.get('avatar_activation_regex')
        })

print(f"Missing Primary count: {len(missing_prim)}")
print(f"Missing Secondary count: {len(missing_sec)}")
print("\nAll 44 Missing in Primary:")
for m in missing_prim:
    print(f"  [{m['index']}] entry_id={m['entry_id']} | name='{m['name']}' | keys={m['keys'][:2]}")

print("\nSample 15 Missing in Secondary:")
for m in missing_sec[:15]:
    print(f"  [{m['index']}] entry_id={m['entry_id']} | name='{m['name']}' | keys={m['keys'][:2]}")
