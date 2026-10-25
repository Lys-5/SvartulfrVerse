import json

data = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
entries = data.get('lexicon', data.get('entries', []))

target_ids = [
    '4NzXF4_0hYxmN7Idltzpw',  # Scarlett Rose
    'ijy8vrlphNv19-p-gbYuY',  # Sierra Cruz
    'YCxAqNoShpefVvk0_Pc7i',  # Russell 'Russ' Sinclair
    'ekdQjq63xP7HtNuaPQJQE',  # Stanley Davies Jr.
    'RM6rcwv8MlY1XWaCTQp0M',  # Jared Thompson
    'alyssa_world_dossier_2b54a223', # Alyssa
    'Vcj4h2TL4Usola2A4OOl6'   # Jasper
]

found_map = {}
for idx, e in enumerate(entries):
    eid = e.get('entry_id')
    if eid in target_ids:
        found_map[eid] = (idx, e)

print(f"Found {len(found_map)} of {len(target_ids)} target entries in FINAL/Svartulfr_NPC_Primary.json:\n")

for tid in target_ids:
    if tid in found_map:
        idx, e = found_map[tid]
        print(f"=== [{idx}] {e.get('name')} (entry_id: {tid}) ===")
        print(f"type: {repr(e.get('type'))}")
        print(f"name: {repr(e.get('name'))}")
        print(f"keys: {e.get('keys')}")
        print(f"secondary_keys: {e.get('secondary_keys')}")
        print(f"selective: {e.get('selective')}")
        print(f"key_logic: {repr(e.get('key_logic'))}")
        print(f"constant: {e.get('constant')}")
        print(f"position: {repr(e.get('position'))}")
        print(f"insertion_order: {e.get('insertion_order')}")
        print(f"priority: {e.get('priority')}")
        print(f"avatar: {repr(e.get('avatar'))}")
        print(f"custom_avatar_regex: {e.get('custom_avatar_regex')}")
        print(f"avatar_activation_regex: {repr(e.get('avatar_activation_regex'))}")
        print(f"lines_parsed: {e.get('lines_parsed')}")
        print(f"npc_info: {e.get('npc_info')}")
        content = e.get('content', '')
        print(f"content length: {len(content)} characters")
        print(f"content first 120 chars: {repr(content[:120])}")
        print(f"content last 120 chars: {repr(content[-120:])}")
        print()
