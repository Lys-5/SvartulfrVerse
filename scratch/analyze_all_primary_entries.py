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

print(f"Loaded {len(entries)} entries from {primary_path}")

# Let's inspect each entry in detail
detailed_records = []

for idx, e in enumerate(entries):
    name = e.get("name", "").strip()
    content = e.get("content", "")
    avatar = e.get("avatar", "")
    regex = e.get("avatar_activation_regex", "")
    keys = e.get("keys", [])
    secondary_keys = e.get("secondary_keys", [])
    selective = e.get("selective", False)
    ignored_chars = e.get("ignored_characters", [])
    ignored_personas = e.get("ignored_personas", [])
    existing_npc_info = e.get("npc_info", {})

    # Extract JED+ bracket block
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_str = bracket_m.group(1) if bracket_m else ""
    
    attrs = {}
    if bracket_str:
        parts = re.split(r";\s*", bracket_str)
        for p in parts:
            if ":" in p:
                k, v = p.split(":", 1)
                attrs[k.strip().upper()] = v.strip()
    
    jed_name_raw = attrs.get("NAME", name)
    
    # Analyze regex for duplicate surnames
    dupes = detect_duplicate_surnames(regex)
    
    # Check broad umbrella keys in keys, secondary_keys, nicknames
    broad_keys = [k for k in keys if k.strip().lower() in CANONICAL_BROAD_KEYS]
    broad_sec = [k for k in secondary_keys if k.strip().lower() in CANONICAL_BROAD_KEYS]
    
    # Existing nicknames
    existing_nicks = existing_npc_info.get("nicknames", []) if isinstance(existing_npc_info, dict) else []
    broad_nicks = [n for n in existing_nicks if n.strip().lower() in CANONICAL_BROAD_KEYS]

    detailed_records.append({
        "index": idx,
        "entry_name": name,
        "jed_name_raw": jed_name_raw,
        "species": attrs.get("SPECIES", ""),
        "role": attrs.get("ROLE", ""),
        "age": attrs.get("AGE", ""),
        "avatar": avatar,
        "regex": regex,
        "dupes": dupes,
        "keys": keys,
        "secondary_keys": secondary_keys,
        "selective": selective,
        "ignored_characters": ignored_chars,
        "ignored_personas": ignored_personas,
        "existing_npc_info": existing_npc_info,
        "broad_keys": broad_keys,
        "broad_sec": broad_sec,
        "broad_nicks": broad_nicks
    })

with open("scratch/detailed_records.json", "w", encoding="utf-8") as f:
    json.dump(detailed_records, f, indent=2, ensure_ascii=False)

print("Saved scratch/detailed_records.json")
