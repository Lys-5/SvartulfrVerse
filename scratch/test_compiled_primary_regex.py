import json
import sys
from pathlib import Path

sys.path.insert(0, ".")
from scripts.verify_npc_schema_contract import (
    compile_wyvern_avatar_regex,
    detect_duplicate_surnames
)

catalog = json.load(open("scratch/proposed_primary_npc_info.json", encoding="utf-8"))

total_dupes = 0
for item in catalog:
    idx = item["index"]
    name = item["entry_name"]
    info = item["npc_info"]
    compiled = compile_wyvern_avatar_regex(info)
    dupes = detect_duplicate_surnames(compiled, info.get("last_name"))
    if dupes:
        print(f"[{idx:02d}] {name} has compiled dupes: {dupes}")
        total_dupes += 1

print(f"Total compiled duplicate defects: {total_dupes}/99")
