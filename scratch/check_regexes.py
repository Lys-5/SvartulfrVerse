import json
import re

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for idx in [0, 10, 25, 28, 52, 66, 68, 73, 75, 77]:
    e = d["lexicon"][idx]
    reg = e.get("avatar_activation_regex")
    name = e.get("name")
    compiled = re.compile(reg, re.MULTILINE)
    
    # Test valid turns
    test_turn_full = f"\n{name}: \"Hello world.\""
    m = compiled.search(test_turn_full)
    assert m is not None, f"Failed to match full name for {name}: {reg}"
    
    # Check duplicate surname is absent
    info = e.get("npc_info", {})
    ln = info.get("last_name")
    if ln:
        assert f"{ln} {ln}".lower() not in reg.lower(), f"Duplicate surname found in regex: {reg}"
        
print("All 10 fixed regexes tested and match proper speaker turns with 0 duplicate surnames!")
