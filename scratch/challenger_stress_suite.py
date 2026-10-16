"""
Adversarial Stress Test Suite for Svartulfr Verse Lorebooks
Author: Challenger 1 (critic, specialist)
Milestones: R1 & R2
"""
import os
import json
import re
import time
import hashlib
import copy

ROOT = r"e:\repository\SvartulfrVerse"
FINAL_DIR = os.path.join(ROOT, "FINAL")
OPT_DIR = os.path.join(ROOT, "lorebooks", "optimized")
BACKUP_DIR = os.path.join(ROOT, "scratch", "backup_pre_audit_lorebooks")
SCRATCH_DIR = os.path.join(ROOT, "scratch")

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

LOREBOOKS = [
    ("Svartulfr_Lorebook_I.json", "_gwwCxCfQ6PQaLEjAQVpJL", 219, "non_npc"),
    ("Svartulfr_Lorebook_II.json", "_HfG7TeV6MJyj6bxMwxkpt", 143, "non_npc"),
    ("Svartulfr_Lorebook_III.json", "_9zWTGqYJNJ4BCDMj8gfcD", 35, "non_npc"),
    ("Svartulfr_Location.json", "_EjXxkmPVhpCXg8xABpFkK", 196, "non_npc"),
    ("Svartulfr_NPC_Primary.json", "_zwEqgEEzh12X6gHVmMKKC", 106, "npc"),
    ("Svartulfr_NPC_Secondary.json", "_Uht3Ckz44JBDrPnUHq7LV", 310, "npc"),
]

CANONICAL_BROAD_KEYS = {
    "solarton", "succ", "blackwood", "vampire", "werewolf",
    "college", "student", "alpha", "omega"
}

BANNED_NPC_PHRASES = {
    "succ student",
    "pack leader",
    "blackwood council",
    "alligator demihuman",
    "demon representative",
    "human representative"
}

import sys
if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def md5_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def test_suite():
    results = {
        "passed": 0,
        "failed": 0,
        "errors": []
    }

    def check(name, condition, msg=""):
        if condition:
            results["passed"] += 1
        else:
            print(f"  [FAIL] {name}: {msg}")
            results["failed"] += 1
            results["errors"].append(f"{name}: {msg}")


    print("=====================================================================")
    print("RUNNING ADVERSARIAL CHALLENGER SUITE (EMPIRICAL VERIFICATION)")
    print("=====================================================================")

    # -------------------------------------------------------------
    # SUITE 1: FILE SYSTEM & JSON INTEGRITY
    # -------------------------------------------------------------
    print("\n--- Suite 1: File Existence, JSON Parsing, and Counts ---")
    total_entries_count = 0
    all_global_entry_ids = {}

    for fname, exp_id, exp_count, kind in LOREBOOKS:
        for folder, path in [("FINAL", FINAL_DIR), ("optimized", OPT_DIR), ("backup", BACKUP_DIR)]:
            fpath = os.path.join(path, fname)
            check(f"File exists {folder}/{fname}", os.path.exists(fpath), f"File not found: {fpath}")
            if not os.path.exists(fpath):
                continue
            sz = os.path.getsize(fpath)
            check(f"File non-empty {folder}/{fname}", sz > 0, f"Size is 0")
            
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                check(f"JSON parsed {folder}/{fname}", isinstance(data, dict), "Not a dict")
            except Exception as e:
                check(f"JSON parsed {folder}/{fname}", False, f"JSON parse error: {e}")
                continue
                
            entries = data.get("entries", [])
            lexicon = data.get("lexicon", [])
            check(f"Entries count {folder}/{fname} == {exp_count}", len(entries) == exp_count, f"Got {len(entries)}")
            check(f"Lexicon count {folder}/{fname} == {exp_count}", len(lexicon) == exp_count, f"Got {len(lexicon)}")

            if folder == "FINAL":
                total_entries_count += len(entries)
                for idx, entry in enumerate(lexicon):
                    eid = entry.get("entry_id")
                    check(f"Entry ID present [{fname} #{idx}]", eid is not None and len(str(eid).strip()) > 0, f"Invalid ID: {eid}")
                    if eid in all_global_entry_ids:
                        prev_file, prev_idx, prev_name = all_global_entry_ids[eid]
                        check(f"Global Entry ID Unique [{eid}]", False, f"Duplicate ID! In {fname} #{idx} ('{entry.get('name')}') and {prev_file} #{prev_idx} ('{prev_name}')")
                    else:
                        all_global_entry_ids[eid] = (fname, idx, entry.get("name"))

    check("Total universe entry count exactly 1,009", total_entries_count == 1009, f"Got {total_entries_count}")
    check("Global unique entry IDs count exactly 1,009", len(all_global_entry_ids) == 1009, f"Got {len(all_global_entry_ids)}")

    # -------------------------------------------------------------
    # SUITE 2: DEEP EQUALITY ENTRIES == LEXICON ACROSS REPOSITORIES
    # -------------------------------------------------------------
    print("\n--- Suite 2: Deep Equality (entries == lexicon & FINAL == optimized) ---")
    for fname, _, exp_count, _ in LOREBOOKS:
        final_path = os.path.join(FINAL_DIR, fname)
        opt_path = os.path.join(OPT_DIR, fname)
        
        with open(final_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        with open(opt_path, "r", encoding="utf-8") as f:
            opt_data = json.load(f)

        check(f"FINAL/{fname} entries == lexicon", final_data["entries"] == final_data["lexicon"], "Mismatch between entries and lexicon")
        check(f"optimized/{fname} entries == lexicon", opt_data["entries"] == opt_data["lexicon"], "Mismatch between entries and lexicon in optimized")
        check(f"FINAL/{fname} == optimized/{fname}", final_data == opt_data, "FINAL and optimized data objects differ")
        check(f"MD5 hash match {fname}", md5_file(final_path) == md5_file(opt_path), f"Hash mismatch: FINAL={md5_file(final_path)} vs opt={md5_file(opt_path)}")

    # -------------------------------------------------------------
    # SUITE 3: HISTORICAL AUDIT & REPLACEMENT IN LOREBOOK III
    # -------------------------------------------------------------
    print("\n--- Suite 3: Lorebook III SillyTavern to Native Schema Replacement Audit ---")
    b3_path = os.path.join(BACKUP_DIR, "Svartulfr_Lorebook_III.json")
    f3_path = os.path.join(FINAL_DIR, "Svartulfr_Lorebook_III.json")
    with open(b3_path, "r", encoding="utf-8") as f:
        b3_data = json.load(f)
    with open(f3_path, "r", encoding="utf-8") as f:
        f3_data = json.load(f)

    b3_entries = b3_data.get("entries", [])
    b3_lexicon = b3_data.get("lexicon", [])
    f3_entries = f3_data.get("entries", [])
    f3_lexicon = f3_data.get("lexicon", [])

    check("Lorebook III backup lexicon has 35 entries", len(b3_lexicon) == 35, f"Got {len(b3_lexicon)}")
    check("Lorebook III FINAL entries equals lexicon", f3_entries == f3_lexicon, "Entries != lexicon in Lorebook III")
    check("Lorebook III FINAL lexicon identical to backup lexicon", f3_lexicon == b3_lexicon, "FINAL lexicon mutated vs backup lexicon!")
    
    # Verify that each entry in backup entries corresponded to backup lexicon
    for idx in range(35):
        st_entry = b3_entries[idx]
        wy_entry = b3_lexicon[idx]
        name_match = (st_entry.get("comment") == wy_entry.get("name"))
        check(f"Lorebook III entry #{idx} name match ('{wy_entry.get('name')}')", name_match, f"{st_entry.get('comment')} != {wy_entry.get('name')}")
        content_match = (st_entry.get("content") == wy_entry.get("content"))
        check(f"Lorebook III entry #{idx} content match", content_match, "Content differed between legacy ST entry and Wyvern entry")

    # -------------------------------------------------------------
    # SUITE 4: ZERO RESIDUAL {{age}} MACROS
    # -------------------------------------------------------------
    print("\n--- Suite 4: Complete Macro Scan (Zero {{age}} Macros) ---")
    age_macro_regex = re.compile(r"\{\{\s*age\s*\}\}", re.IGNORECASE)
    any_macro_regex = re.compile(r"\{\{[^}]+\}\}")
    for fname, _, _, _ in LOREBOOKS:
        for folder, path in [("FINAL", FINAL_DIR), ("optimized", OPT_DIR)]:
            fpath = os.path.join(path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            age_matches = age_macro_regex.findall(content)
            check(f"0 {{{{age}}}} in {folder}/{fname}", len(age_matches) == 0, f"Found {len(age_matches)} matches: {age_matches}")
            
            # Check for any unexpected unexpanded macros
            all_macros = any_macro_regex.findall(content)
            # Permitted macros in Wyvern character cards might be {{user}} or {{char}}, but lorebooks shouldn't have rogue ones
            suspicious = [m for m in all_macros if m.lower() not in ["{{user}}", "{{char}}"]]
            check(f"No suspicious macros in {folder}/{fname}", len(suspicious) == 0, f"Suspicious macros found: {suspicious}")

    # -------------------------------------------------------------
    # SUITE 5: UMBRELLA KEYS & BROAD KEYS PRUNING ON NPCS
    # -------------------------------------------------------------
    print("\n--- Suite 5: Umbrella Keywords & Generic Triggers on NPCs ---")
    for fname, _, exp_count, kind in LOREBOOKS:
        if kind != "npc":
            continue
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            name = entry.get("name", "")
            keys = [k.strip().lower() for k in entry.get("keys", [])]
            sec_keys = [k.strip().lower() for k in entry.get("secondary_keys", [])]

            # 1. Broad keys in primary
            for bk in CANONICAL_BROAD_KEYS:
                check(f"NPC [{name}] does not have broad key '{bk}'", bk not in keys, f"Found '{bk}' in keys")

            # 2. Banned phrases in primary
            for bp in BANNED_NPC_PHRASES:
                check(f"NPC [{name}] does not have banned phrase '{bp}'", bp not in keys, f"Found '{bp}' in keys")

            # 3. Malachia's secondary_keys
            if "Malachia" in name and "Bloodmoon" in name:
                check("Malachia does not have 'alpha' in secondary_keys", "alpha" not in sec_keys, f"Found 'alpha' in {sec_keys}")

            # 4. Selective discipline: selective=True must have secondary_keys
            if entry.get("selective") is True:
                check(f"NPC [{name}] selective=True has non-empty secondary_keys", len(entry.get("secondary_keys", [])) > 0, "Empty secondary_keys with selective=True")

            # 5. Protected proper names
            if name == "Roman Blackwood":
                check("Roman Blackwood has 'Roman Blackwood' key", "Roman Blackwood" in entry.get("keys", []), "Missing 'Roman Blackwood'")
            if "Katarina" in name and "Blackwood" in name:
                check("Katarina Blackwood retains key containing 'Katarina'", any("Katarina" in k for k in entry.get("keys", [])), "Missing Katarina key")

    # -------------------------------------------------------------
    # SUITE 6: NON-NPC METADATA CLEANLINESS
    # -------------------------------------------------------------
    print("\n--- Suite 6: Non-NPC Metadata Cleanliness ---")
    for fname, _, exp_count, kind in LOREBOOKS:
        if kind != "non_npc":
            continue
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            name = entry.get("name", "")
            check(f"No avatar_activation_regex in {fname} [{name}]", "avatar_activation_regex" not in entry, "Found avatar_activation_regex")
            check(f"No custom_avatar_regex in {fname} [{name}]", "custom_avatar_regex" not in entry, "Found custom_avatar_regex")
            check(f"No lines_parsed in {fname} [{name}]", "lines_parsed" not in entry, "Found lines_parsed")
            check(f"No npc_info in {fname} [{name}]", "npc_info" not in entry, "Found npc_info")
            if "avatar" in entry:
                av = entry["avatar"]
                check(f"Avatar is valid HTTP in {fname} [{name}]", av.startswith("http"), f"Invalid avatar: {av}")

    # -------------------------------------------------------------
    # SUITE 7: ADVERSARIAL MULTILINE REGEX & DIALOGUE STRESS TESTING
    # -------------------------------------------------------------
    print("\n--- Suite 7: Multiline Regex Stress Testing for All 416 NPCs ---")
    total_npc_tested = 0
    regex_format_pattern = re.compile(r"^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$")

    for fname in ["Svartulfr_NPC_Primary.json", "Svartulfr_NPC_Secondary.json"]:
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            total_npc_tested += 1
            name = entry.get("name", "")
            av = entry.get("avatar", "")
            rg = entry.get("avatar_activation_regex", "")
            custom = entry.get("custom_avatar_regex")
            lines = entry.get("lines_parsed")
            info = entry.get("npc_info", {})

            # Structural checks
            check(f"NPC [{name}] has HTTP avatar", av.startswith("http"), f"Avatar: {av}")
            check(f"NPC [{name}] custom_avatar_regex is True", custom is True, f"custom: {custom}")
            check(f"NPC [{name}] lines_parsed == 1", lines == 1, f"lines: {lines}")
            check(f"NPC [{name}] regex structure valid", bool(regex_format_pattern.match(rg)), f"Invalid regex structure: {rg}")

            # Compilation test
            try:
                t0 = time.perf_counter()
                pat = re.compile(rg, re.M)
                compile_time_ms = (time.perf_counter() - t0) * 1000
                check(f"NPC [{name}] regex compiled", True, "")
                check(f"NPC [{name}] compile time < 5ms", compile_time_ms < 5.0, f"Took {compile_time_ms:.2f}ms")
            except Exception as e:
                check(f"NPC [{name}] regex compiled", False, f"Compile error: {e}")
                continue

            # Performance / ReDoS stress test with long inputs
            long_padding = " " * 5000 + "\n" + " " * 5000
            t0 = time.perf_counter()
            m = pat.search(long_padding)
            exec_time_ms = (time.perf_counter() - t0) * 1000
            check(f"NPC [{name}] ReDoS immune (< 10ms on large whitespace)", exec_time_ms < 10.0, f"Took {exec_time_ms:.2f}ms")
            check(f"NPC [{name}] no match on pure whitespace", m is None, "Matched whitespace!")

            # Positive Matching Scenarios:
            # 1. Exactly "Name:"
            m1 = pat.search(f"{name}:")
            check(f"NPC [{name}] matches 'Name:'", m1 is not None, f"Failed on '{name}:'")

            # 2. Leading whitespace "  Name:"
            m2 = pat.search(f"  {name}:")
            check(f"NPC [{name}] matches '  Name:'", m2 is not None, f"Failed on '  {name}:'")

            # 3. Newline "\nName:"
            m3 = pat.search(f"\n{name}:")
            check(f"NPC [{name}] matches '\\nName:'", m3 is not None, f"Failed on '\\n{name}:'")

            # 4. Multi-turn dialogue with newline "\n  Name: 'Hello'"
            m4 = pat.search(f"Narrator speaks.\n  {name}: \"I am speaking.\"")
            check(f"NPC [{name}] matches mid-turn dialogue", m4 is not None, f"Failed on mid-turn dialogue")

            # 5. Space before colon "Name :"
            m5 = pat.search(f"{name} :")
            check(f"NPC [{name}] matches 'Name :'", m5 is not None, f"Failed on '{name} :'")

            # Firstname match if first_name present
            first = info.get("first_name")
            if first and len(first) > 2 and first != name:
                mf = pat.search(f"{first}:")
                check(f"NPC [{name}] matches 'Firstname:' ('{first}:')", mf is not None, f"Failed on '{first}:'")
                mf_nl = pat.search(f"\n{first}:")
                check(f"NPC [{name}] matches '\\nFirstname:' ('\\n{first}:')", mf_nl is not None, f"Failed on '\\n{first}:'")

            # Negative Matching Scenarios (Adversarial False Positive Rejection):
            # 1. Prefix: "NotName:"
            n1 = pat.search(f"Not{name}:")
            check(f"NPC [{name}] rejects 'NotName:'", n1 is None, f"False match on 'Not{name}:'")

            # 2. Fake name: "Fake Name:"
            n2 = pat.search(f"Fake {name}:")
            check(f"NPC [{name}] rejects 'Fake Name:'", n2 is None, f"False match on 'Fake {name}:'")

            # 3. Mentioned in sentence without colon: "I saw Name yesterday."
            n3 = pat.search(f"I saw {name} yesterday.")
            check(f"NPC [{name}] rejects in-sentence mention", n3 is None, f"False match on sentence")

            # 4. Sentence ending in colon where Name is in the middle: "I told Name to leave:"
            n4 = pat.search(f"I told {name} to leave:")
            check(f"NPC [{name}] rejects name embedded in sentence ending in colon", n4 is None, f"False match on embedded sentence: {n4.group(0) if n4 else ''}")

            # 5. Completely different speaker: "RandomStranger:"
            n5 = pat.search("RandomStranger:")
            check(f"NPC [{name}] rejects 'RandomStranger:'", n5 is None, f"False match on RandomStranger")

    check("Total NPCs tested in Suite 7 == 416", total_npc_tested == 416, f"Got {total_npc_tested}")

    # -------------------------------------------------------------
    # SUITE 8: NPC SPECIAL CHARACTERS ESCAPING AUDIT
    # -------------------------------------------------------------
    print("\n--- Suite 8: NPC Names with Special Characters (Regex Escaping Audit) ---")
    special_char_npcs = []
    for fname in ["Svartulfr_NPC_Primary.json", "Svartulfr_NPC_Secondary.json"]:
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            name = entry.get("name", "")
            if any(c in name for c in [".", "'", "-", "/", "(", ")", "&", "\"", ","]):
                special_char_npcs.append((fname, idx, name, entry.get("avatar_activation_regex")))

    print(f"  Found {len(special_char_npcs)} NPCs with special characters in their name.")
    for fname, idx, name, rg in special_char_npcs:
        pat = re.compile(rg, re.M)
        m = pat.search(f"{name}:")
        check(f"Special Char NPC [{name}] matches verbatim header", m is not None, f"Failed on '{name}:'. Regex: {rg}")

    # -------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------
    print("\n" + "=" * 70)
    print(f"ADVERSARIAL SUITE SUMMARY: {results['passed']} PASSED, {results['failed']} FAILED")
    print("=" * 70)
    if results["failed"] > 0:
        print("\nFAILURES:")
        for err in results["errors"][:20]:
            print(f"  - {err}")
    else:
        print("\nALL ADVERSARIAL STRESS TESTS PASSED WITH 100% EMPIRICAL SUCCESS!")

    return results

if __name__ == "__main__":
    res = test_suite()
    if res["failed"] > 0:
        exit(1)
    else:
        exit(0)
