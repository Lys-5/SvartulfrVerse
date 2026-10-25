import json

cards = [
    ("Erik Ulfr Douglas", "FINAL/Erik_Douglas_card.json"),
    ("Malachia Björn Douglas Bloodmoon", "FINAL/Malachia_Douglas_Bloodmoon_card.json"),
    ("Noah Loki Douglas Bloodmoon", "FINAL/Noah_Douglas_Bloodmoon_card.json"),
    ("Logan Járn Douglas", "FINAL/Logan_Douglas_card.json"),
    ("Wulfnic Báleygr Bloodmoon", "FINAL/Wulfnic_Bloodmoon_card.json"),
    ("Mackenzie Sanchez-Rogers", "FINAL/Mackenzie_Sanchez_Rogers_card.json"),
    ("Edric Douglas", "FINAL/Edric_Douglas_card.json")
]

for name, path in cards:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("=" * 60)
    print(f"NAME: {name}")
    print(f"FILE: {path}")
    print(f"CARD ID: {data.get('id')}")
    print(f"AVATAR: {data.get('avatar')}")
    desc = data.get("description", "")
    print(f"DESC TOTAL LENGTH: {len(desc)} characters")
    
    # Extract bracket block
    bracket_end = desc.find("]\n")
    if bracket_end != -1:
        print("\n--- INITIAL BRACKET BLOCK ---")
        print(desc[:bracket_end+1])
    
    # Extract sections
    sections = [
        "BACKSTORY:",
        "FAMILY & PACK:",
        "CLAN AND COMPANY:",
        "VOICE & BEHAVIOR:",
        "THE WEIGHT HE CARRIES:",
        "THE SECRET HE CARRIES:",
        "SEXUALITY & INTIMACY:",
        "GRIEF & INTIMACY:",
        "SIGNATURE VEHICLE & ASSETS:",
        "SIGNATURE VEHICLE & GEAR:",
        "SIGNATURE VEHICLE & TOOLS:",
        "SIGNATURE VEHICLE & RELICS:",
        "RPG STATS & TRAITS:"
    ]
    
    print("\n--- SECTIONS SUMMARY ---")
    for sec in sections:
        pos = desc.find(sec)
        if pos != -1:
            snippet = desc[pos:pos+len(sec)+120].replace("\n", " ")
            print(f"  {sec} (pos {pos}) -> {snippet}...")
            
    # Check RPG stats specifically
    rpg_pos = desc.find("RPG STATS & TRAITS:")
    if rpg_pos != -1:
        print("\n--- RPG BLOCK ---")
        print(desc[rpg_pos:])
