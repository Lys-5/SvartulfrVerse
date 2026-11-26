import json
import re

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary = json.load(f)

target_ids = {
    'Scarlett Rose': '4NzXF4_0hYxmN7Idltzpw',
    'Sierra Cruz': 'ijy8vrlphNv19-p-gbYuY',
    'Russell Russ Sinclair': 'YCxAqNoShpefVvk0_Pc7i',
    'Stanley Davies Jr': 'ekdQjq63xP7HtNuaPQJQE',
    'Jared Thompson': 'RM6rcwv8MlY1XWaCTQp0M',
    'Alyssa Hvit Douglas Bloodmoon': 'alyssa_world_dossier_2b54a223',
    'Jasper Svartr Douglas Bloodmoon': 'Vcj4h2TL4Usola2A4OOl6'
}

entries_by_id = {e.get('entry_id') or e.get('id'): e for e in primary['entries']}

print("Total entries in Primary:", len(primary['entries']))
print("Total lexicon in Primary:", len(primary['lexicon']))

for name, eid in target_ids.items():
    e = entries_by_id.get(eid)
    if not e:
        print(f"\nMISSING ENTRY: {name} ({eid})")
        # Try finding by name
        for entry in primary['entries']:
            if name.split()[0].lower() in (entry.get('name') or '').lower():
                print(f"  Found potential match by name: name={entry.get('name')}, entry_id={entry.get('entry_id')}")
        continue
    content = e.get('content', '')
    desc_len = len(content)
    is_jed = ('[NAME:' in content or '[NAME :' in content) and 'BACKSTORY:' in content
    ext = e.get('extensions', {})
    ignored_chars = e.get('ignored_characters') or ext.get('ignored_characters')
    ignored_personas = e.get('ignored_personas') or ext.get('ignored_personas')
    print(f"\n=== {name} (entry_id: {eid}) ===")
    print(f"  name field: {e.get('name')}")
    print(f"  type: {e.get('type')}")
    print(f"  selective: {e.get('selective')}")
    print(f"  keys: {e.get('keys')}")
    print(f"  secondary_keys: {e.get('secondary_keys')}")
    print(f"  key_logic: {e.get('key_logic')}")
    print(f"  desc_len: {desc_len}")
    print(f"  is_jed: {is_jed}")
    print(f"  avatar: {e.get('avatar')}")
    print(f"  custom_avatar_regex: {e.get('custom_avatar_regex')}")
    print(f"  avatar_activation_regex: {e.get('avatar_activation_regex')}")
    print(f"  lines_parsed: {e.get('lines_parsed')}")
    print(f"  npc_info: {e.get('npc_info')}")
    print(f"  ignored_characters: {e.get('ignored_characters')}")
    print(f"  ignored_personas: {e.get('ignored_personas')}")
    print(f"  extensions: {e.get('extensions')}")
    print(f"  em_dash_in_content: {'—' in content}")
    print(f"  age_macro_in_content: {'{{age}}' in content}")
