import json

data = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
entries = data.get('lexicon', data.get('entries', []))

npc_entries = [e for e in entries if e.get('type') == 'npc']
print(f"Total npc entries in Primary: {len(npc_entries)}")

for i, e in enumerate(npc_entries[:5]):
    print(f"\n--- NPC Example {i+1}: {e.get('name')} (entry_id: {e.get('entry_id')}) ---")
    print(f"type: {e.get('type')}")
    print(f"keys: {e.get('keys')}")
    print(f"secondary_keys: {e.get('secondary_keys')}")
    print(f"selective: {e.get('selective')}")
    print(f"key_logic: {e.get('key_logic')}")
    print(f"avatar: {e.get('avatar')}")
    print(f"custom_avatar_regex: {e.get('custom_avatar_regex')}")
    print(f"avatar_activation_regex: {repr(e.get('avatar_activation_regex'))}")
    print(f"lines_parsed: {e.get('lines_parsed')}")
    print(f"npc_info: {json.dumps(e.get('npc_info'), indent=2)}")
    print(f"content len: {len(e.get('content', ''))}")
