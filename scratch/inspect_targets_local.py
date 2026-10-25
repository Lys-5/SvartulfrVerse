import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
primary_path = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'

with open(primary_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('lexicon', data.get('entries', []))
print(f"Total entries in local Svartulfr_NPC_Primary.json: {len(entries)}")

target_ids = {
    '4NzXF4_0hYxmN7Idltzpw': 'Scarlett Rose',
    'ijy8vrlphNv19-p-gbYuY': 'Sierra Cruz',
    'YCxAqNoShpefVvk0_Pc7i': "Russell 'Russ' Sinclair",
    'ekdQjq63xP7HtNuaPQJQE': 'Stanley Davies Jr.',
    'RM6rcwv8MlY1XWaCTQp0M': 'Jared Thompson',
    'alyssa_world_dossier_2b54a223': 'Alyssa Hvit Douglas Bloodmoon',
    'Vcj4h2TL4Usola2A4OOl6': 'Jasper (Reference)'
}

found = {}
for idx, entry in enumerate(entries):
    eid = entry.get('id')
    keys = entry.get('keys', [])
    sec_keys = entry.get('secondary_keys', [])
    content = entry.get('content', '')
    for tid, tname in target_ids.items():
        # Match by ID or check keys/name
        if eid == tid:
            found[tid] = (idx, entry)
        elif not eid and any(k.lower() == tname.lower() for k in keys):
            found[tid] = (idx, entry)

print("\n--- FOUND TARGETS IN LOCAL FILE ---")
for tid, tname in target_ids.items():
    if tid in found:
        idx, entry = found[tid]
        print(f"\n[TARGET: {tname}] (ID: {tid}) at index {idx}")
        print(f"  id: {entry.get('id')}")
        print(f"  type: {entry.get('type')}")
        print(f"  keys: {entry.get('keys')}")
        print(f"  secondary_keys: {entry.get('secondary_keys')}")
        print(f"  selective: {entry.get('selective')}")
        print(f"  key_logic: {entry.get('key_logic')}")
        print(f"  constant: {entry.get('constant')}")
        print(f"  avatar: {entry.get('avatar')}")
        print(f"  custom_avatar_regex: {entry.get('custom_avatar_regex')}")
        print(f"  avatar_activation_regex: {repr(entry.get('avatar_activation_regex'))}")
        print(f"  lines_parsed: {entry.get('lines_parsed')}")
        print(f"  npc_info: {entry.get('npc_info')}")
        content = entry.get('content', '')
        print(f"  content length: {len(content)} chars")
        print(f"  content preview: {repr(content[:150])}")
    else:
        print(f"\n[TARGET: {tname}] (ID: {tid}) -> NOT FOUND BY ID! Searching by name...")
        matches = [e for e in entries if any(tname.lower() in k.lower() for k in e.get('keys', []))]
        print(f"  Name matches: {len(matches)}")
        for m in matches:
            print(f"    found entry id={m.get('id')}, keys={m.get('keys')[:5]}")
