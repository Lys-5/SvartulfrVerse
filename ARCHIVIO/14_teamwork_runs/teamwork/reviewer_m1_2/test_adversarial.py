import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from scripts.verify_npc_schema_contract import (
    compile_wyvern_avatar_regex,
    detect_duplicate_surnames,
    escape_wyvern,
    validate_anti_collision_contract,
    validate_avatar_gallery_contract,
    validate_entries_lexicon_parity,
    validate_npc_info_schema,
)

print("=== ADVERSARIAL STRESS TEST SUITE ===")

# Test 1: Duplicate surnames with escaped quotes or hyphens
print("\n--- Test 1: Escaped characters in duplicate surname detection ---")
raw_p = "(?:^|\\n)\\s*(?:Mark O'Connor O'Connor)\\s*:"
res_raw = detect_duplicate_surnames(raw_p, "O'Connor")
print("Raw apostrophe:", res_raw)
assert len(res_raw) > 0, "Failed to detect raw O'Connor O'Connor"

escaped_p = "(?:^|\\n)\\s*(?:Mark O['‘’ʼ‛′]Connor O['‘’ʼ‛′]Connor)\\s*:"
res_escaped = detect_duplicate_surnames(escaped_p, "O'Connor")
print("Escaped character class apostrophe:", res_escaped)

# Test 2: Multi-word last names (e.g. Douglas Bloodmoon, Sanchez Rogers)
print("\n--- Test 2: Multi-word last names ---")
multi_p = "(?:^|\\n)\\s*(?:Malachia Douglas Bloodmoon Douglas Bloodmoon)\\s*:"
res_multi = detect_duplicate_surnames(multi_p, "Douglas Bloodmoon")
print("Multi-word surname dupe:", res_multi)
assert len(res_multi) > 0, "Failed to detect multi-word duplicate surname"

# Test 3: What if someone has a legitimate repeated word in name?
# e.g., Boutros Boutros-Ghali or Sirhan Sirhan
print("\n--- Test 3: Legitimate repetition false positive check ---")
legit_p = "(?:^|\\n)\\s*(?:Boutros Boutros-Ghali)\\s*:"
res_legit = detect_duplicate_surnames(legit_p, "Boutros-Ghali")
print("Legitimate name repeated word:", res_legit)

# Test 4: Unicode normalization and special characters in escape_wyvern
print("\n--- Test 4: Unicode normalization edge cases in escape_wyvern ---")
composed = "e\u0301" # e + acute accent decomposed (NFD)
escaped_comp = escape_wyvern(composed)
print(f"Decomposed 'e + acute' normalized: {repr(escaped_comp)}")
assert escaped_comp == "\u00e9", "NFC normalization failed"

# Test 5: Regex special characters in names
print("\n--- Test 5: Regex characters in names ---")
tricky_npc = {
    "first_name": "Test (Special)",
    "middle_names": ["*Star*"],
    "last_name": "Doe [Agent]",
    "nicknames": ["$Money$", "^Up^"],
    "titles": ["Dr. (PhD)"]
}
compiled_tricky = compile_wyvern_avatar_regex(tricky_npc)
print("Compiled tricky regex length:", len(compiled_tricky))
assert r"\(" in compiled_tricky
assert r"\[" in compiled_tricky
assert r"\*" in compiled_tricky
assert r"\$" in compiled_tricky
assert r"\^" in compiled_tricky

# Test 6: Empty, None, or Malformed inputs across all validators
print("\n--- Test 6: Extreme boundary conditions across validators ---")
# npc_info
assert not validate_npc_info_schema(None)[0]
assert not validate_npc_info_schema([])[0]
assert not validate_npc_info_schema({"first_name": None})[0]
assert not validate_npc_info_schema({"first_name": ""})[0]
assert not validate_npc_info_schema({"first_name": "   "})[0]
assert not validate_npc_info_schema({"first_name": "Valid", "middle_names": None})[0] == False  # middle_names None is ok or error?
val, errs = validate_npc_info_schema({"first_name": "Valid", "middle_names": None})
print("middle_names None result:", val, errs)

# Test 7: Parity with deep structures
print("\n--- Test 7: Parity validator with key ordering differences ---")
# JSON keys in different order should still pass because json.dumps(sort_keys=True) is used!
lb1 = {
    "entries": [{"a": 1, "b": 2}],
    "lexicon": [{"b": 2, "a": 1}]
}
val, errs = validate_entries_lexicon_parity(lb1)
print("Different key order in entries vs lexicon passes parity:", val)
assert val, "Parity check failed despite identical semantic JSON object"

print("\n=== ALL ADVERSARIAL TESTS COMPLETED ===")
