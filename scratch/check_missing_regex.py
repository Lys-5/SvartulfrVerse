import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    prim = json.load(f)

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec = json.load(f)

print("Sample regex patterns for NPCs with missing avatars in Primary:")
prim_missing = [e for e in prim['entries'] if not e.get('avatar')]
for e in prim_missing[:5]:
    print(f"  Name: {e.get('name')}")
    print(f"    Regex: {e.get('avatar_activation_regex')}")
    print(f"    npc_info: {e.get('npc_info')}")

print("\nSample regex patterns for NPCs with missing avatars in Secondary:")
sec_missing = [e for e in sec['entries'] if not e.get('avatar')]
for e in sec_missing[:5]:
    print(f"  Name: {e.get('name')}")
    print(f"    Regex: {e.get('avatar_activation_regex')}")
    print(f"    npc_info: {e.get('npc_info')}")
