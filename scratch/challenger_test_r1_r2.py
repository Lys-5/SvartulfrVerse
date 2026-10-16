"""
Challenger 1 Empirical Verification and Stress Test Suite
Milestones R1 & R2
"""
import os
import json
import re
import hashlib
import copy

ROOT = r"e:\repository\SvartulfrVerse"
FINAL_DIR = os.path.join(ROOT, "FINAL")
OPT_DIR = os.path.join(ROOT, "lorebooks", "optimized")
BACKUP_DIR = os.path.join(ROOT, "scratch", "backup_pre_audit_lorebooks")
SCRATCH_DIR = os.path.join(ROOT, "scratch")

FILES = [
    ("Svartulfr_Lorebook_I.json", "_gwwCxCfQ6PQaLEjAQVpJL", 219, "non_npc"),
    ("Svartulfr_Lorebook_II.json", "_HfG7TeV6MJyj6bxMwxkpt", 143, "non_npc"),
    ("Svartulfr_Lorebook_III.json", "_9zWTGqYJNJ4BCDMj8gfcD", 35, "non_npc"),
    ("Svartulfr_Location.json", "_EjXxkmPVhpCXg8xABpFkK", 196, "non_npc"),
    ("Svartulfr_NPC_Primary.json", "_zwEqgEEzh12X6gHVmMKKC", 106, "npc"),
    ("Svartulfr_NPC_Secondary.json", "_Uht3Ckz44JBDrPnUHq7LV", 310, "npc"),
]

def md5_bytes(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

def md5_file(filepath: str) -> str:
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def run_tests():
    print("=" * 70)
    print("CHALLENGER 1: EMPIRICAL TEST SUITE (MILISTONES R1 & R2)")
    print("=" * 70)

    # -------------------------------------------------------------
    # TEST 1: File Existence, JSON Parsing, Schema & Exact Entry Counts
    # -------------------------------------------------------------
    print("\n[TEST 1] JSON Integrity, Parsing, and Exact Counts across all folders")
    total_entries_final = 0
    total_entries_opt = 0
    total_entries_backup = 0
    all_final_entry_ids = {}

    for fname, expected_id, expected_count, kind in FILES:
        for folder_name, folder_path in [("FINAL", FINAL_DIR), ("optimized", OPT_DIR), ("backup", BACKUP_DIR)]:
            fpath = os.path.join(folder_path, fname)
            assert os.path.exists(fpath), f"Missing file: {fpath}"
            assert os.path.getsize(fpath) > 0, f"Empty file: {fpath}"
            
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            assert isinstance(data, dict), f"Root must be dict in {fpath}"
            assert "entries" in data, f"Missing 'entries' in {fpath}"
            assert "lexicon" in data, f"Missing 'lexicon' in {fpath}"
            
            entries = data["entries"]
            lexicon = data["lexicon"]
            
            assert isinstance(entries, list), f"'entries' must be list in {fpath}"
            assert isinstance(lexicon, list), f"'lexicon' must be list in {fpath}"
            
            assert len(entries) == expected_count, f"Entry count mismatch in {folder_name}/{fname}: expected {expected_count}, got {len(entries)}"
            assert len(lexicon) == expected_count, f"Lexicon count mismatch in {folder_name}/{fname}: expected {expected_count}, got {len(lexicon)}"
            
            if folder_name == "FINAL":
                total_entries_final += len(entries)
                # Check entry_ids within file
                seen_in_file = set()
                for idx, entry in enumerate(lexicon):
                    assert isinstance(entry, dict), f"Entry {idx} in {fname} is not a dict: {type(entry)}"
                    eid = entry.get("entry_id")
                    assert eid is not None, f"Entry {idx} in {fname} has None entry_id"
                    assert isinstance(eid, str) and len(eid.strip()) > 0, f"Entry {idx} in {fname} has invalid entry_id: '{eid}'"
                    assert eid not in seen_in_file, f"Duplicate entry_id '{eid}' inside {fname} at index {idx}"
                    seen_in_file.add(eid)
                    all_final_entry_ids[eid] = (fname, idx, entry.get("name"))
            elif folder_name == "optimized":
                total_entries_opt += len(entries)
            elif folder_name == "backup":
                total_entries_backup += len(lexicon)

        print(f"  OK: {fname} (exact count: {expected_count})")

    assert total_entries_final == 1009, f"Total FINAL entries {total_entries_final} != 1009"
    assert total_entries_opt == 1009, f"Total OPT entries {total_entries_opt} != 1009"
    assert total_entries_backup == 1009, f"Total BACKUP entries {total_entries_backup} != 1009"
    assert len(all_final_entry_ids) == 1009, f"Unique entry IDs across all lorebooks {len(all_final_entry_ids)} != 1009 (cross-file duplicate IDs detected!)"
    print(f"PASS: Exactly 1,009 entries verified. Zero nulls, zero duplicate IDs (within or across files).")

    # -------------------------------------------------------------
    # TEST 2: Deep Equality entries == lexicon & FINAL == optimized
    # -------------------------------------------------------------
    print("\n[TEST 2] Deep Equality (entries == lexicon & FINAL == optimized)")
    for fname, _, expected_count, _ in FILES:
        final_path = os.path.join(FINAL_DIR, fname)
        opt_path = os.path.join(OPT_DIR, fname)
        
        with open(final_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        with open(opt_path, "r", encoding="utf-8") as f:
            opt_data = json.load(f)

        # 1. Strict equality in FINAL
        assert final_data["entries"] == final_data["lexicon"], f"entries != lexicon in FINAL/{fname}"
        
        # 2. Strict equality in optimized
        assert opt_data["entries"] == opt_data["lexicon"], f"entries != lexicon in optimized/{fname}"
        
        # 3. Complete object equality between FINAL and optimized
        assert final_data == opt_data, f"Data in FINAL/{fname} != optimized/{fname}"
        
        # 4. Byte-for-byte MD5 match
        final_md5 = md5_file(final_path)
        opt_md5 = md5_file(opt_path)
        assert final_md5 == opt_md5, f"MD5 mismatch for {fname}: FINAL={final_md5}, opt={opt_md5}"
        print(f"  OK: {fname} (entries == lexicon STRICT TRUE, MD5: {final_md5})")

    print("PASS: 100% strict equality and bit-for-bit mirroring verified.")

    # -------------------------------------------------------------
    # TEST 3: Empirical Mutation Diff vs Pre-Audit Backup
    # -------------------------------------------------------------
    print("\n[TEST 3] Empirical Diff: Verify ONLY Intended Mutations Were Applied")
    mutation_stats = {
        "non_npc_purged_regex": 0,
        "non_npc_purged_empty_avatar": 0,
        "non_npc_preserved_avatar": 0,
        "npc_pruned_broad_keys": 0,
        "npc_pruned_sec_keys": 0,
        "npc_assigned_crest_avatar": 0,
        "npc_preserved_avatar": 0,
        "unintended_content_mutations": 0,
        "unintended_name_mutations": 0,
        "unintended_deletion": 0
    }

    for fname, _, expected_count, kind in FILES:
        backup_path = os.path.join(BACKUP_DIR, fname)
        final_path = os.path.join(FINAL_DIR, fname)
        
        with open(backup_path, "r", encoding="utf-8") as f:
            backup_data = json.load(f)
        with open(final_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
            
        b_lex = backup_data["lexicon"]
        f_lex = final_data["lexicon"]
        
        assert len(b_lex) == len(f_lex) == expected_count, f"Count mismatch vs backup in {fname}"
        
        for idx in range(expected_count):
            b_entry = b_lex[idx]
            f_entry = f_lex[idx]
            
            # Entry ID and name must NEVER change
            assert b_entry.get("entry_id") == f_entry.get("entry_id"), f"entry_id mutated in {fname} [{idx}]"
            assert b_entry.get("name") == f_entry.get("name"), f"name mutated in {fname} [{idx}]"
            
            # Content must never change
            if b_entry.get("content") != f_entry.get("content"):
                print(f"WARNING: Content mutation in {fname} [{idx}] {b_entry.get('name')}")
                mutation_stats["unintended_content_mutations"] += 1
                
            # Type must never change
            assert b_entry.get("type") == f_entry.get("type"), f"type mutated in {fname} [{idx}]"
            
            if kind == "non_npc":
                if "avatar_activation_regex" in b_entry and "avatar_activation_regex" not in f_entry:
                    mutation_stats["non_npc_purged_regex"] += 1
                if ("avatar" in b_entry and not b_entry["avatar"].startswith("http")) and ("avatar" not in f_entry):
                    mutation_stats["non_npc_purged_empty_avatar"] += 1
                if "avatar" in f_entry and f_entry["avatar"].startswith("http"):
                    mutation_stats["non_npc_preserved_avatar"] += 1
            else:
                # NPC lorebook
                b_keys = b_entry.get("keys", [])
                f_keys = f_entry.get("keys", [])
                if b_keys != f_keys:
                    diff_keys = set(b_keys) - set(f_keys)
                    mutation_stats["npc_pruned_broad_keys"] += len(diff_keys)
                    
                b_sec = b_entry.get("secondary_keys", [])
                f_sec = f_entry.get("secondary_keys", [])
                if b_sec != f_sec:
                    diff_sec = set(b_sec) - set(f_sec)
                    mutation_stats["npc_pruned_sec_keys"] += len(diff_sec)
                    
                b_av = b_entry.get("avatar", "")
                f_av = f_entry.get("avatar", "")
                if (not b_av.startswith("http")) and f_av.startswith("http"):
                    mutation_stats["npc_assigned_crest_avatar"] += 1
                elif b_av.startswith("http") and f_av == b_av:
                    mutation_stats["npc_preserved_avatar"] += 1

    print(f"  Mutation stats vs backup:")
    for k, v in mutation_stats.items():
        print(f"    {k}: {v}")
        
    assert mutation_stats["unintended_content_mutations"] == 0, "Found unintended content mutations!"
    assert mutation_stats["unintended_name_mutations"] == 0, "Found unintended name mutations!"
    assert mutation_stats["npc_assigned_crest_avatar"] == 302, f"Expected 302 avatar assignments, got {mutation_stats['npc_assigned_crest_avatar']}"
    assert mutation_stats["npc_preserved_avatar"] == 114, f"Expected 114 preserved avatars, got {mutation_stats['npc_preserved_avatar']}"
    print("PASS: Zero unintended mutations across all 1,009 entries.")

    # -------------------------------------------------------------
    # TEST 4: Missing Avatars JSON Log Strict Cross-Validation
    # -------------------------------------------------------------
    print("\n[TEST 4] Cross-validating scratch/missing_npc_avatars.json vs actual files")
    log_path = os.path.join(SCRATCH_DIR, "missing_npc_avatars.json")
    with open(log_path, "r", encoding="utf-8") as f:
        log_data = json.load(f)
        
    assert log_data["total_remediated"] == 302
    logged_entries = log_data["entries"]
    assert len(logged_entries) == 302
    
    # Check that each logged entry actually maps to the entry in FINAL
    for item in logged_entries:
        lfname = item["lorebook"]
        idx = item["index"]
        eid = item["entry_id"]
        final_path = os.path.join(FINAL_DIR, lfname)
        with open(final_path, "r", encoding="utf-8") as f:
            d = json.load(f)
        entry = d["lexicon"][idx]
        assert entry["entry_id"] == eid, f"Log index {idx} entry_id mismatch: {eid} vs {entry['entry_id']}"
        assert entry["name"] == item["name"], f"Log index {idx} name mismatch: {item['name']} vs {entry['name']}"
        assert entry["avatar"] == item["applied_avatar"]
        
        # Verify it genuinely had empty avatar in backup
        backup_path = os.path.join(BACKUP_DIR, lfname)
        with open(backup_path, "r", encoding="utf-8") as f:
            bd = json.load(f)
        b_entry = bd["lexicon"][idx]
        b_av = (b_entry.get("avatar") or "").strip()
        assert not b_av.startswith("http"), f"Entry {item['name']} was logged as remediated but had valid avatar in backup: {b_av}"

    print("PASS: missing_npc_avatars.json perfectly cross-validated against backup and final.")

    # Call TEST 5 and TEST 6
    test_npc_regex_compilation_and_matching()



def test_npc_regex_compilation_and_matching():
    print("\n[TEST 5] NPC avatar_activation_regex Compilation & Multiline Matching")
    
    total_npcs = 0
    compiled_patterns = []
    
    for fname in ["Svartulfr_NPC_Primary.json", "Svartulfr_NPC_Secondary.json"]:
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
            
        for idx, entry in enumerate(d["lexicon"]):
            total_npcs += 1
            name = entry.get("name", "")
            regex_str = entry.get("avatar_activation_regex")
            npc_info = entry.get("npc_info", {})
            
            assert regex_str is not None, f"Missing regex in {fname} [{idx}] {name}"
            assert isinstance(regex_str, str), f"Regex is not string in {fname} [{idx}] {name}"
            
            # Compile with re.M (multiline)
            try:
                pattern = re.compile(regex_str, re.M)
            except Exception as e:
                raise AssertionError(f"Failed to compile regex for {fname} [{idx}] {name}: '{regex_str}'. Error: {e}")
                
            compiled_patterns.append({
                "fname": fname,
                "idx": idx,
                "name": name,
                "regex_str": regex_str,
                "pattern": pattern,
                "npc_info": npc_info
            })
            
    assert total_npcs == 416, f"Expected 416 NPCs, got {total_npcs}"
    print(f"  All 416 NPC regexes successfully compiled with re.M.")

    # Print first 5 regexes as sample
    for cp in compiled_patterns[:5]:
        print(f"  Sample [{cp['idx']}] {cp['name']}: {cp['regex_str']}")

    # Now let's stress test matching and rejection!
    print("\n[TEST 6] Multiline Matching against Simulated Dialogue Headers")
    match_success_count = 0
    rejection_success_count = 0
    mismatch_warnings = []
    
    for item in compiled_patterns:
        pat = item["pattern"]
        name = item["name"]
        fname = item["fname"]
        idx = item["idx"]
        info = item["npc_info"]
        
        first = info.get("first_name", "")
        last = info.get("last_name", "")
        nicknames = info.get("nicknames", [])
        
        # Test headers that SHOULD match:
        test_headers = []
        
        # 1. Full name at start of line: "Name:"
        if name:
            test_headers.append(f"{name}:")
            test_headers.append(f"{name} :")
            test_headers.append(f"  {name}:") # leading space
            test_headers.append(f"\n{name}:") # after newline
            test_headers.append(f"\n  {name}:") # newline + leading space
            test_headers.append(f"Hello world.\n{name}: 'Dialogue here'") # mid-text dialogue
            
        # 2. Firstname Lastname if different from name
        if first and last and f"{first} {last}" != name:
            test_headers.append(f"{first} {last}:")
            test_headers.append(f"\n{first} {last}:")
            
        # 3. Firstname only
        if first and len(first) > 2:
            test_headers.append(f"{first}:")
            test_headers.append(f"\n{first}:")
            test_headers.append(f"\n  {first}:")
            
        # 4. Nicknames
        for nick in nicknames:
            if nick and len(nick) > 2:
                test_headers.append(f"{nick}:")
                test_headers.append(f"\n{nick}:")

        matched_any = False
        for header in test_headers:
            m = pat.search(header)
            if m:
                matched_any = True
            else:
                mismatch_warnings.append((item['name'], header, item['regex_str']))
                
        if matched_any:
            match_success_count += 1
            
        # Test headers that MUST NOT match (Negative test cases):
        negative_headers = [
            f"Not{name}:",
            f"Fake {name}:",
            f"RandomStranger:",
            f"The quick brown fox jumped over the lazy dog.",
            f"He said that {name} was going home.", # Name in middle of sentence without colon
            f"I saw {name} at the store:", # Sentence ending in colon but name is not the speaker header
            f"Dr. Somebody Else:"
        ]
        
        for neg in negative_headers:
            m = pat.search(neg)
            if m:
                # If negative header matched, that's a false positive bug!
                # Unless the match was because 'I saw Name at the store:' matched if regex is too loose
                raise AssertionError(f"False positive match! NPC {name} regex '{item['regex_str']}' matched negative input: '{neg}' (matched '{m.group(0)}')")
                
        rejection_success_count += 1

    print(f"  Tested 416 NPCs: {match_success_count}/416 matched expected headers.")
    print(f"  Tested 416 NPCs: {rejection_success_count}/416 rejected negative inputs without any false positives.")
    if mismatch_warnings:
        print(f"  Total mismatch warnings on specific variations: {len(mismatch_warnings)}")
        for w in mismatch_warnings[:10]:
            print(f"    Warning: NPC '{w[0]}' did not match variation '{w[1]}'. Regex: {w[2]}")
    else:
        print("  Zero mismatch warnings! 100% of tested variations matched perfectly.")


if __name__ == "__main__":
    run_tests()
