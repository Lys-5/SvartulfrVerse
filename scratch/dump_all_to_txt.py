import json
import re

primary_data = json.load(open("FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
entries = primary_data["lexicon"]

with open("scratch/all_primary_entries_summary.txt", "w", encoding="utf-8") as out:
    for idx, e in enumerate(entries):
        name = e.get("name", "")
        content = e.get("content", "")
        bracket_m = re.search(r"\[([^\]]+)\]", content)
        bracket_str = bracket_m.group(1) if bracket_m else ""
        name_m = re.search(r"NAME:\s*([^;]+)", bracket_str)
        jed_name = name_m.group(1).strip() if name_m else name
        role_m = re.search(r"ROLE:\s*([^;]+)", bracket_str)
        jed_role = role_m.group(1).strip() if role_m else ""
        species_m = re.search(r"SPECIES:\s*([^;]+)", bracket_str)
        jed_species = species_m.group(1).strip() if species_m else ""
        keys = e.get("keys", [])
        regex = e.get("avatar_activation_regex", "")
        existing_info = e.get("npc_info", {})
        
        out.write(f"[{idx:02d}] entry_name: '{name}'\n")
        out.write(f"     JED NAME: '{jed_name}'\n")
        out.write(f"     SPECIES: '{jed_species}'\n")
        out.write(f"     ROLE: '{jed_role}'\n")
        out.write(f"     KEYS: {keys}\n")
        out.write(f"     REGEX: {regex}\n")
        out.write(f"     EXISTING NPC_INFO: {existing_info}\n\n")

print("Wrote scratch/all_primary_entries_summary.txt")
