import json
import re
import sys
from pathlib import Path

sys.path.insert(0, ".")
from scripts.verify_npc_schema_contract import (
    CANONICAL_BROAD_KEYS,
    compile_wyvern_avatar_regex,
    detect_duplicate_surnames,
    validate_npc_info_schema,
    validate_anti_collision_contract
)

primary_path = Path("FINAL/Svartulfr_NPC_Primary.json")
data = json.load(open(primary_path, "r", encoding="utf-8"))
entries = data["lexicon"]

print(f"Total entries: {len(entries)}")

# Build comprehensive mapping for all 99 entries
# We want:
# index, name, first_name, middle_names, last_name, nicknames, titles, npc_prefix

catalog = []

for idx, e in enumerate(entries):
    name = e.get("name", "").strip()
    content = e.get("content", "")
    existing_info = e.get("npc_info", {})
    keys = e.get("keys", [])
    regex = e.get("avatar_activation_regex", "")
    
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_str = bracket_m.group(1) if bracket_m else ""
    attrs = {}
    if bracket_str:
        for part in re.split(r";\s*", bracket_str):
            if ":" in part:
                k, v = part.split(":", 1)
                attrs[k.strip().upper()] = v.strip()
    
    jed_name = attrs.get("NAME", name).strip()
    
    # Defaults from existing_info if available
    fn = existing_info.get("first_name", "")
    ln = existing_info.get("last_name", "")
    nicks = list(existing_info.get("nicknames", []))
    titles = list(existing_info.get("titles", []))
    mid_names = []
    npc_prefix = ""

    # Specific refinements based on canonical JED+ analysis
    
    # Middle names check
    if "MIDDLE_NAME" in attrs:
        raw_mid = attrs["MIDDLE_NAME"]
        # e.g. "Loki (Wolf Name...)" or "Dominic (Civil Nobility), Járn (Wolf Name...)"
        # extract words before parentheses
        parts = raw_mid.split(",")
        for p in parts:
            clean_p = re.split(r"[\(\[]", p)[0].strip()
            if clean_p and clean_p not in mid_names:
                mid_names.append(clean_p)
    elif "MIDDLE_NAMES" in attrs:
        raw_mid = attrs["MIDDLE_NAMES"]
        parts = raw_mid.split(",")
        for p in parts:
            clean_p = re.split(r"[\(\[]", p)[0].strip()
            if clean_p and clean_p not in mid_names:
                mid_names.append(clean_p)

    # Manual inspection overrides for known characters:
    if idx == 0: # Hugh Rivers
        fn, ln = "Hugh", "Rivers"
        titles = ["Alpha"]
        nicks = ["The Mountain Sovereign"]
    elif idx == 1: # Liam O’Connor
        fn, ln = "Liam", "O'Connor"
    elif idx == 10: # Dominic Rogers
        fn, ln = "Dominic", "Rogers"
        mid_names = ["Wayne"]
        titles = ["Mr."]
        nicks = ["Dom", "Bailey's Dad"]
    elif idx == 24: # Russell 'Russ' Sinclair
        fn, ln = "Russell", "Sinclair"
        nicks = ["Russ"]
    elif idx == 25: # Daniel "Danny" Boone
        fn, ln = "Daniel", "Boone"
        nicks = ["Danny"]
    elif idx == 28: # Harrison Black
        fn, ln = "Harrison", "Black"
        titles = ["Councilman"]
        nicks = ["Harry"]
    elif idx == 32: # Wulfnic Báleygr Bloodmoon
        fn, ln = "Wulfnic", "Bloodmoon"
        mid_names = ["Báleygr"]
        titles = ["Jarl", "Alpha"]
        nicks = ["The First Tusk", "The Ancient", "Alpha of Alphas"]
    elif idx == 36: # Ut Berg
        fn, ln = "Ut", "Berg"
        nicks = ["The Mountain", "Út Fjallit"]
    elif idx == 39: # Sullivan "Sully" Jones
        fn, ln = "Sullivan", "Jones"
        nicks = ["Sully"]
    elif idx == 40: # Stanley Davies Sr.
        fn, ln = "Stanley", "Davies"
        titles = ["Mr."]
        nicks = ["Stanley Davies Sr."]
    elif idx == 41: # Stanley Davies Jr.
        fn, ln = "Stanley", "Davies"
        nicks = ["Stan", "Stanley Davies Jr."]
    elif idx == 43: # Ruaraidh "Rory" Ballantine
        fn, ln = "Ruaraidh", "Ballantine"
        nicks = ["Rory"]
    elif idx == 44: # Roland Vickers
        fn, ln = "Roland", "Vickers"
        mid_names = ["Mark"]
    elif idx == 45: # Professor Loewe
        fn, ln = "Richard", "Loewe"
        titles = ["Professor"]
        nicks = ["Loewe"]
    elif idx == 46: # Oskar
        fn, ln = "Oskar", ""
        nicks = ["Ozzie", "Squidface"]
    elif idx == 47: # Noah Loki Douglas Bloodmoon
        fn, ln = "Noah", "Douglas Bloodmoon"
        mid_names = ["Loki"]
        nicks = ["The Grey Eminence", "Golden Boy"]
    elif idx == 48: # Nixara Hvit Bloodmoon
        fn, ln = "Nixara", "Bloodmoon"
        mid_names = ["Hvit"]
        nicks = ["White Moon", "Pack Mom"]
    elif idx == 51: # Marcus Thornfield
        fn, ln = "Marcus", "Thornfield"
        mid_names = ["Iron"]
    elif idx == 52: # Marcus O'Connor
        fn, ln = "Marcus", "O'Connor"
        nicks = ["Mark", "Oldtown"]
    elif idx == 53: # Malachia Björn Douglas Bloodmoon
        fn, ln = "Malachia", "Douglas Bloodmoon"
        mid_names = ["Björn"]
        titles = ["Alpha"]
        nicks = ["The Berserker", "Ghost", "The King"]
    elif idx == 54: # Magnus Douglas III
        fn, ln = "Magnus", "Douglas"
        titles = ["III", "Sir"]
        nicks = ["Patriarch Magnus"]
    elif idx == 55: # Mackenzie Sanchez-Rogers
        fn, ln = "Mackenzie", "Sanchez-Rogers"
        nicks = ["Mac"]
    elif idx == 56: # Lord Cornelius Douglas
        fn, ln = "Cornelius", "Douglas"
        titles = ["Lord"]
    elif idx == 57: # Logan Járn Douglas
        fn, ln = "Logan", "Douglas"
        mid_names = ["Dominic", "Járn"]
        nicks = ["Uncle Logan", "The Peacemaker"]
    elif idx == 58: # Kaladin Nargathon
        fn, ln = "Kaladin", "Nargathon"
        mid_names = ["Blackwolf"]
        titles = ["Commander"]
        nicks = ["Kal", "Subject Zero"]
    elif idx == 60: # Jasper Svartr Douglas Bloodmoon
        fn, ln = "Jasper", "Douglas Bloodmoon"
        mid_names = ["Svartr"]
        nicks = ["DJ Frequency", "Shadow Wolf", "Jasp"]
    elif idx == 65: # Iordan R. Vess
        fn, ln = "Iordan", "Vess"
        mid_names = ["R."]
        titles = ["Alpha"]
        nicks = ["Io"]
    elif idx == 66: # Helena Weiss
        fn, ln = "Helena", "Weiss"
        titles = ["Professor"]
        nicks = ["Arcadia"]
    elif idx == 68: # Harlan Beaumont
        fn, ln = "Harlan", "Beaumont"
        nicks = ["Huck"]
    elif idx == 69: # Hank Thompson
        fn, ln = "Hank", "Thompson"
        titles = ["Coach"]
    elif idx == 70: # GREED - Roxie
        fn, ln = "Roxie", ""
        nicks = ["Greed", "Rox"]
    elif idx == 71: # GLUTTONY - Kevin
        fn, ln = "Kevin", ""
        nicks = ["Gluttony"]
    elif idx == 72: # Finnegan Novak
        fn, ln = "Finnegan", "Novak"
        nicks = ["Finn"]
    elif idx == 73: # Federico "Riki" Savini
        fn, ln = "Federico", "Savini"
        nicks = ["Riki"]
    elif idx == 74: # Fade Greymoor
        fn, ln = "Mihaela", "Greymoor"
        nicks = ["Fade"]
    elif idx == 75: # Eris Davies
        fn, ln = "Eris", "Davies"
        titles = ["Mrs.", "Ms."]
        nicks = ["Stan's Mom"]
    elif idx == 76: # Erik Ulfr Douglas
        fn, ln = "Erik", "Douglas"
        mid_names = ["Cornelius", "Ulfr"]
        titles = ["Alpha", "Lord"]
        nicks = ["The Prime Alpha", "The Patriarch"]
    elif idx == 77: # Elizabeth Duskwood
        fn, ln = "Elizabeth", "Duskwood"
        titles = ["Lady"]
        nicks = ["Nonna"]
    elif idx == 79: # ENVY - Siobhan
        fn, ln = "Siobhan", ""
        nicks = ["Envy"]
    elif idx == 80: # Dullahan
        fn, ln = "Dullahan", ""
        titles = ["Coach"]
        nicks = ["Coach D", "Dully"]
    elif idx == 81: # Dr. Arthur Sinclair
        fn, ln = "Arthur", "Sinclair"
        titles = ["Dr."]
        nicks = ["Sloth", "The Alchemist"]
    elif idx == 89: # Bianca Rossi
        fn, ln = "Bianca", "Rossi"
        nicks = ["Bia"]
    elif idx == 91: # Barkley Rover
        fn, ln = "Barkley", "Rover"
        titles = ["Coach"]
        nicks = ["Barks", "Coach B"]
    elif idx == 92: # Bailey Rogers
        fn, ln = "Bailey", "Rogers"
        nicks = ["Red"]
    elif idx == 94: # Archer Wolfwood
        fn, ln = "Archer", "Wolfwood"
        titles = ["Chancellor"]
    elif idx == 96: # Andrew Campbell
        fn, ln = "Andrew", "Campbell"
        nicks = ["Andy"]
    elif idx == 98: # Alyssa Hvit Douglas Bloodmoon
        fn, ln = "Alyssa", "Douglas Bloodmoon"
        mid_names = ["Hvit"]
        nicks = ["White Moon", "Lyssa", "The Anchor"]

    # Filter out empty or whitespace strings
    mid_names = [m.strip() for m in mid_names if m and m.strip()]
    nicks = [n.strip() for n in nicks if n and n.strip()]
    titles = [t.strip() for t in titles if t and t.strip()]

    # Clean out any accidental broad umbrella terms
    nicks = [n for n in nicks if n.lower() not in CANONICAL_BROAD_KEYS]
    titles = [t for t in titles if t.lower() not in CANONICAL_BROAD_KEYS]

    cand_npc_info = {
        "first_name": fn,
        "middle_names": mid_names,
        "last_name": ln if ln else None,
        "nicknames": nicks,
        "titles": titles,
        "npc_prefix": npc_prefix
    }

    # Validate against schema contract
    valid, errs = validate_npc_info_schema(cand_npc_info)
    if not valid:
        print(f"ERROR on [{idx}] {name}: {errs}")

    catalog.append({
        "index": idx,
        "entry_name": name,
        "npc_info": cand_npc_info,
        "valid": valid
    })

print(f"Total cataloged: {len(catalog)}")
valid_count = sum(1 for c in catalog if c["valid"])
print(f"Valid count: {valid_count}/{len(catalog)}")

with open("scratch/proposed_primary_npc_info.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)
