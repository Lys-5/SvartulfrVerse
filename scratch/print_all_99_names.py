import json
import re

primary_data = json.load(open("FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
entries = primary_data["lexicon"]

for idx, e in enumerate(entries):
    name = e.get("name", "")
    content = e.get("content", "")
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_str = bracket_m.group(1) if bracket_m else ""
    # extract NAME: ...;
    name_m = re.search(r"NAME:\s*([^;]+)", bracket_str)
    jed_name = name_m.group(1).strip() if name_m else name
    role_m = re.search(r"ROLE:\s*([^;]+)", bracket_str)
    jed_role = role_m.group(1).strip() if role_m else ""
    species_m = re.search(r"SPECIES:\s*([^;]+)", bracket_str)
    jed_species = species_m.group(1).strip() if species_m else ""
    
    print(f"[{idx:02d}] Name: '{name}' | JED_NAME: '{jed_name}' | Role: '{jed_role}'")
