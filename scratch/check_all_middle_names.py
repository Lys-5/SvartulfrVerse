import json
import re

primary_data = json.load(open("FINAL/Svartulfr_NPC_Primary.json", encoding="utf-8"))
entries = primary_data["lexicon"]

for idx, e in enumerate(entries):
    name = e.get("name", "")
    content = e.get("content", "")
    bracket_m = re.search(r"\[([^\]]+)\]", content)
    bracket_str = bracket_m.group(1) if bracket_m else ""
    
    # Check if MIDDLE_NAME appears in bracket_str
    mid_m = re.search(r"MIDDLE_NAME[S]?:\s*([^;]+)", bracket_str)
    if mid_m:
        print(f"[{idx:02d}] Explicit MIDDLE_NAME in JED: {name} -> {mid_m.group(1)}")
    
    # Check name for 3+ words
    words = name.split()
    if len(words) > 2:
        print(f"[{idx:02d}] Entry name has > 2 words: {name}")
