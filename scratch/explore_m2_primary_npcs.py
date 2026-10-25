import json
import re
from pathlib import Path
import sys
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
lexicon = data["lexicon"]

print(f"Total entries in Primary: {len(lexicon)}")

# 1. Inspect root gallery
print(f"Root keys present: {list(data.keys())}")
print(f"Has gallery: {'gallery' in data}, Has gallery_count: {'gallery_count' in data}")

# 2. Inspect anti-collision
ic_entries = []
ip_entries = []
sel_entries = []

for idx, e in enumerate(lexicon):
    if e.get("ignored_characters"):
        ic_entries.append((idx, e.get("name"), e.get("ignored_characters")))
    if e.get("ignored_personas"):
        ip_entries.append((idx, e.get("name"), e.get("ignored_personas")))
    if e.get("selective"):
        sel_entries.append((idx, e.get("name"), e.get("secondary_keys")))

print(f"\nEntries with ignored_characters ({len(ic_entries)}):")
for item in ic_entries:
    print(f"  [{item[0]}] {item[1]}: {item[2]}")

print(f"\nEntries with ignored_personas ({len(ip_entries)}):")
for item in ip_entries:
    print(f"  [{item[0]}] {item[1]}: {item[2]}")

print(f"\nEntries with selective=True ({len(sel_entries)}):")
for item in sel_entries:
    print(f"  [{item[0]}] {item[1]}: {item[2]}")

# 3. Duplicate surname entries
print("\nEntries with duplicate surnames:")
dupe_entries = []
for idx, e in enumerate(lexicon):
    name = e.get("name", "")
    reg = e.get("avatar_activation_regex", "")
    dupes = detect_duplicate_surnames(reg)
    if dupes:
        dupe_entries.append((idx, name, dupes, reg))
        print(f"  [{idx}] {name}: {dupes}")

print(f"Total duplicate surname entries found: {len(dupe_entries)}")

# 4. Detailed dump of each of the 99 entries
results = []
for idx, e in enumerate(lexicon):
    entry_name = e.get("name", "").strip()
    content = e.get("content", "")
    
    # Extract JED+ bracket block
    bracket_match = re.search(r"\[([^\]]+)\]", content)
    bracket_text = bracket_match.group(1) if bracket_match else ""
    
    # Parse attributes inside bracket
    attrs = {}
    if bracket_text:
        # Split by semicolons not inside parens
        parts = re.split(r";\s*", bracket_text)
        for p in parts:
            if ":" in p:
                k, v = p.split(":", 1)
                attrs[k.strip().upper()] = v.strip()
    
    jed_name = attrs.get("NAME", "")
    species = attrs.get("SPECIES", "")
    role = attrs.get("ROLE", "")
    age = attrs.get("AGE", "")
    
    existing_npc_info = e.get("npc_info")
    keys = e.get("keys", [])
    sec_keys = e.get("secondary_keys", [])
    
    # Check for broad umbrella keys
    broad_in_keys = [k for k in keys if k.lower().strip() in CANONICAL_BROAD_KEYS]
    broad_in_sec = [k for k in sec_keys if k.lower().strip() in CANONICAL_BROAD_KEYS]
    
    results.append({
        "index": idx,
        "entry_name": entry_name,
        "jed_name": jed_name,
        "species": species,
        "role": role,
        "age": age,
        "keys": keys,
        "broad_keys": broad_in_keys + broad_in_sec,
        "existing_npc_info": existing_npc_info,
        "avatar": e.get("avatar", ""),
        "avatar_activation_regex": e.get("avatar_activation_regex", "")
    })

with open("scratch/primary_npc_analysis.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\nWrote detailed analysis to scratch/primary_npc_analysis.json")
