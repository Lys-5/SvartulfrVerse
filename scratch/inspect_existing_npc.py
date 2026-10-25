import json

data = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))['lexicon']

# Look at entry 0: Jet Thompson
e0 = data[0]
print("=== ENTRY 0: JET THOMPSON ===")
print("Name:", e0.get('name'))
print("Type:", e0.get('type'))
print("Keys:", e0.get('keys'))
print("Avatar:", e0.get('avatar'))
print("Custom regex:", e0.get('custom_avatar_regex'))
print("Avatar regex:", repr(e0.get('avatar_activation_regex')))
print("Lines parsed:", e0.get('lines_parsed'))
print("NPC info:", e0.get('npc_info'))
print("Content snippet (first 400 chars):")
print(e0.get('content', '')[:400])

# Look at entry 106: Thrakgor Deathspine
e_thrak = data[106]
print("\n=== ENTRY 106: THRAKGOR ===")
print("Name:", e_thrak.get('name'))
print("Content snippet (first 400 chars):")
print(e_thrak.get('content', '')[:400])
