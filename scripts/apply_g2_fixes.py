import os
import sys
import json
import re
import shutil
import time
from datetime import datetime, timezone

sys.path.append(os.getcwd())
from scratch.resolve_g2_all import known_dates
from scratch.g2_fix_helpers import (
    d_to_h, STANDARD_INSTRUCTIONS, ALYSSA_ID, JASPER_ID,
    generate_contextual_outfits, generate_contextual_speech, clean_em_dashes
)

EXPORT_PATH = "exports/Svartulfr_Export.json"
BACKUP_PATH = "exports/Svartulfr_Export_pre_g2_fix.json"

# 1. Create backup
if not os.path.exists(BACKUP_PATH):
    shutil.copy2(EXPORT_PATH, BACKUP_PATH)
    print(f"Created backup snapshot at {BACKUP_PATH}")
else:
    print(f"Backup already exists at {BACKUP_PATH}")

# 2. Load data
with open(EXPORT_PATH, "r", encoding="utf-8") as f:
    world_data = json.load(f)

with open("scratch/g2_canonical_list.json", "r", encoding="utf-8") as f:
    g2_list = json.load(f)

g2_ids = {item["id"]: item["name"] for item in g2_list}

characters = world_data.get("world_characters", [])
chars_by_id = {c["id"]: c for c in characters}

# Canonical relationship overrides for specific characters
CANONICAL_ATTITUDES = {
    "Vincent Campbell": [
        {"target_id": ALYSSA_ID, "tier": "acquaintance", "intensity": 30, "reasoning": "Sees her around SUCC as Erik Douglas's daughter. Keeps a respectful, polite distance acknowledging family pedigree."},
        {"target_id": JASPER_ID, "tier": "acquaintance", "intensity": 25, "reasoning": "Recognizes Jasper's tech presence and fraternity neutrality. Occasional cool nods across campus."}
    ],
    "Andrew Campbell": [
        {"target_id": ALYSSA_ID, "tier": "stranger", "intensity": 15, "reasoning": "Unknown scent. Has seen her on campus but moves in entirely different academic circles."},
        {"target_id": JASPER_ID, "tier": "stranger", "intensity": 15, "reasoning": "Unknown scent. Quietly aware of him as the Douglas twin who avoids hockey rinks."}
    ],
    "Scarlett Rose": [
        {"target_id": ALYSSA_ID, "tier": "close_friend", "intensity": 60, "reasoning": "Fiercely loyal campus wingwoman, shares genuine camaraderie and zero predatory tension."},
        {"target_id": JASPER_ID, "tier": "acquaintance", "intensity": 40, "reasoning": "Mutual casual understanding, unhurried acquaintance on campus."}
    ],
    "Russ Sinclair": [
        {"target_id": ALYSSA_ID, "tier": "acquaintance", "intensity": 30, "reasoning": "Known through campus interactions and shared peer groups."},
        {"target_id": JASPER_ID, "tier": "close_friend", "intensity": 65, "reasoning": "Close bond, dorm neighbor, and trusted campus friend."}
    ],
    "Tomas Matthews": [
        {"target_id": ALYSSA_ID, "tier": "stranger", "intensity": 15, "reasoning": "Unknown scent. Knows she is high-pedigree supernatural royalty, keeping his distance."},
        {"target_id": JASPER_ID, "tier": "disliked", "intensity": 35, "reasoning": "Friction over tech, privilege, and fraternity posturing."}
    ]
}

modified_count = 0
for cid, name in g2_ids.items():
    if cid not in chars_by_id:
        print(f"WARNING: G2 Character {name} ({cid}) not found in world_characters!")
        continue
    
    c = chars_by_id[cid]
    modified_count += 1
    
    # 1. is_global = True
    c["is_global"] = True
    
    # 2. final_instructions
    c["final_instructions"] = STANDARD_INSTRUCTIONS
    
    # 3. birthdate & start_timeline_position
    if name in known_dates:
        y, m, d = known_dates[name]
        hours = d_to_h(y, m, d)
        c["birthdate"] = hours
        c["start_timeline_position"] = hours
    else:
        print(f"ERROR: No date found for {name}!")
        
    # 4. Clean em-dashes
    if c.get("summary"):
        c["summary"] = clean_em_dashes(c["summary"])
    if c.get("display_description"):
        c["display_description"] = clean_em_dashes(c["display_description"])
    if c.get("long_summary"):
        c["long_summary"] = clean_em_dashes(c["long_summary"])
        
    # 5. Outfits (ensure at least 5)
    existing_outfits = c.get("outfits") or []
    if len(existing_outfits) < 5:
        role_text = (c.get("summary") or "") + " " + (c.get("display_description") or "")
        species_text = ""
        # Try to find species
        sp_m = re.search(r'SPECIES:\s*([^;\]\n]+)', c.get("long_summary") or "", re.I)
        if sp_m:
            species_text = sp_m.group(1).strip()
        new_outfits = generate_contextual_outfits(name, species_text, role_text)
        c["outfits"] = new_outfits
        c["default_outfit_id"] = new_outfits[0]["id"]
        
    # 6. Speech Examples (ensure at least 5)
    existing_speech = c.get("speech_examples") or []
    if len(existing_speech) < 5:
        role_text = (c.get("summary") or "") + " " + (c.get("display_description") or "")
        species_text = ""
        sp_m = re.search(r'SPECIES:\s*([^;\]\n]+)', c.get("long_summary") or "", re.I)
        if sp_m:
            species_text = sp_m.group(1).strip()
        c["speech_examples"] = generate_contextual_speech(name, species_text, role_text)
        
    # 7. Attitudes (ensure attitudes exist, especially towards Alyssa & Jasper)
    existing_attitudes = c.get("attitudes") or []
    target_ids = {a.get("target_id") for a in existing_attitudes}
    
    ts = int(time.time() * 1000)
    
    # Check if Alyssa is covered
    if ALYSSA_ID not in target_ids:
        # Check custom override or default
        if name in CANONICAL_ATTITUDES and any(ca["target_id"] == ALYSSA_ID for ca in CANONICAL_ATTITUDES[name]):
            ca = next(x for x in CANONICAL_ATTITUDES[name] if x["target_id"] == ALYSSA_ID)
            existing_attitudes.append({
                "id": f"attitude-{ts}-1",
                "target_type": "world_character",
                "target": "",
                "tier": ca["tier"],
                "intensity": ca["intensity"],
                "reasoning": ca["reasoning"],
                "target_id": ALYSSA_ID
            })
        else:
            existing_attitudes.append({
                "id": f"attitude-{ts}-1",
                "target_type": "world_character",
                "target": "",
                "tier": "stranger",
                "intensity": 15,
                "reasoning": "Unknown scent. Has never personally crossed paths with the Douglas daughter.",
                "target_id": ALYSSA_ID
            })
            
    # Check if Jasper is covered
    if JASPER_ID not in target_ids:
        if name in CANONICAL_ATTITUDES and any(ca["target_id"] == JASPER_ID for ca in CANONICAL_ATTITUDES[name]):
            ca = next(x for x in CANONICAL_ATTITUDES[name] if x["target_id"] == JASPER_ID)
            existing_attitudes.append({
                "id": f"attitude-{ts}-2",
                "target_type": "world_character",
                "target": "",
                "tier": ca["tier"],
                "intensity": ca["intensity"],
                "reasoning": ca["reasoning"],
                "target_id": JASPER_ID
            })
        else:
            existing_attitudes.append({
                "id": f"attitude-{ts}-2",
                "target_type": "world_character",
                "target": "",
                "tier": "stranger",
                "intensity": 15,
                "reasoning": "Unknown scent. Has never personally crossed paths with the Douglas son.",
                "target_id": JASPER_ID
            })
            
    c["attitudes"] = existing_attitudes

# Save updated export
with open(EXPORT_PATH, "w", encoding="utf-8") as f:
    json.dump(world_data, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {modified_count} G2 characters in {EXPORT_PATH}!")
