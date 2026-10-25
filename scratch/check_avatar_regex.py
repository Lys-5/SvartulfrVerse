import json
import re

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for idx, e in enumerate(d["lexicon"]):
    name = e.get("name")
    assert e.get("custom_avatar_regex") is True, f"[{idx}] {name} custom_avatar_regex is not True"
    assert e.get("lines_parsed") == 1, f"[{idx}] {name} lines_parsed != 1"
    reg = e.get("avatar_activation_regex")
    assert isinstance(reg, str) and reg.strip(), f"[{idx}] {name} invalid avatar_activation_regex"
    assert "(?:^|\\n)" in reg or "(?<=^|\\n)" in reg, f"[{idx}] {name} regex missing multiline anchor: {reg}"
    # Verify regex compilation
    try:
        re.compile(reg, re.MULTILINE)
    except re.error as err:
        assert False, f"[{idx}] {name} regex compile error: {err} in pattern: {reg}"

print("All 99 entries have custom_avatar_regex=True, lines_parsed=1, and valid multiline regex patterns!")
