import json
import re

cards = [
    "FINAL/Erik_Douglas_card.json",
    "FINAL/Malachia_Douglas_Bloodmoon_card.json",
    "FINAL/Noah_Douglas_Bloodmoon_card.json",
    "FINAL/Logan_Douglas_card.json",
    "FINAL/Wulfnic_Bloodmoon_card.json",
    "FINAL/Mackenzie_Sanchez_Rogers_card.json",
    "FINAL/Edric_Douglas_card.json"
]

print("=== 7 CORE CARDS SURVEY ===")
for path in cards:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    cid = data.get("id")
    name = data.get("name")
    avatar = data.get("avatar")
    desc = data.get("description", "")
    print(f"\nFile: {path}")
    print(f"ID: {cid}")
    print(f"Name: {name}")
    print(f"Avatar: {avatar}")
    print(f"Desc Length: {len(desc)} characters")
    
    # Headings
    headings = re.findall(r"^[A-Z0-9 &/_\[\]\(\)\-\']{3,}:", desc, flags=re.MULTILINE)
    print(f"Headings: {headings}")
    
    # Check if Vehicles, Intimacy Profile, RPG Stats/Traits exist
    has_veh = "VEHICLE" in desc.upper()
    has_int = "INTIMACY" in desc.upper()
    has_rpg = "RPG" in desc.upper() or "MGT" in desc or "S.P.E.C.I.A.L." in desc or "STAT" in desc
    print(f"Contains Vehicles: {has_veh}, Intimacy: {has_int}, RPG: {has_rpg}")
    
    # Check for card regex / npc_info
    print(f"Card has custom_avatar_regex: {data.get('custom_avatar_regex')}")
    print(f"Card has avatar_activation_regex: {data.get('avatar_activation_regex')}")
    print(f"Card has npc_info: {data.get('npc_info')}")
