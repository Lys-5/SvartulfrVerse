"""
Comprehensive Verification Test Suite for Milestones R1 & R2
Svartúlfr Verse — Standalone Lorebooks
"""

import os
import json
import re
import hashlib

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
FINAL_DIR = os.path.join(PROJECT_ROOT, "FINAL")
OPTIMIZED_DIR = os.path.join(PROJECT_ROOT, "lorebooks", "optimized")
BACKUP_DIR = os.path.join(PROJECT_ROOT, "scratch", "backup_pre_audit_lorebooks")
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch")

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

LOREBOOKS = [
    ("Svartulfr_Lorebook_I.json", "_gwwCxCfQ6PQaLEjAQVpJL", "non_npc", 219),
    ("Svartulfr_Lorebook_II.json", "_HfG7TeV6MJyj6bxMwxkpt", "non_npc", 143),
    ("Svartulfr_Lorebook_III.json", "_9zWTGqYJNJ4BCDMj8gfcD", "non_npc", 35),
    ("Svartulfr_Location.json", "_EjXxkmPVhpCXg8xABpFkK", "non_npc", 196),
    ("Svartulfr_NPC_Primary.json", "_zwEqgEEzh12X6gHVmMKKC", "npc", 106),
    ("Svartulfr_NPC_Secondary.json", "_Uht3Ckz44JBDrPnUHq7LV", "npc", 310),
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

def md5_file(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def test_safety_backup():
    print("\n--- Test 1: Safety Backup Verification ---")
    assert os.path.exists(BACKUP_DIR), f"Backup directory {BACKUP_DIR} does not exist!"
    for fname, _, _, count in LOREBOOKS:
        bpath = os.path.join(BACKUP_DIR, fname)
        assert os.path.exists(bpath), f"Backup file {bpath} does not exist!"
        sz = os.path.getsize(bpath)
        assert sz > 0, f"Backup file {bpath} is empty!"
        with open(bpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        assert len(d.get("lexicon", [])) == count, f"Backup {fname} lexicon count mismatch: expected {count}, got {len(d.get('lexicon', []))}"
        print(f"  Backup Verified: {fname} ({count} entries, {sz} bytes)")
    print("Test 1 PASS: All 6 backup files intact and verified.")

def test_pillar_1_non_npc_clean():
    print("\n--- Test 2: Pillar 1 (Non-NPC Metadata Cleanliness) ---")
    for fname, _, kind, count in LOREBOOKS:
        if kind != "non_npc":
            continue
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            assert "avatar_activation_regex" not in entry, f"Found avatar_activation_regex in {fname} [{idx}]"
            assert "custom_avatar_regex" not in entry, f"Found custom_avatar_regex in {fname} [{idx}]"
            assert "lines_parsed" not in entry, f"Found lines_parsed in {fname} [{idx}]"
            assert "npc_info" not in entry, f"Found npc_info in {fname} [{idx}]"
            if "avatar" in entry:
                av = entry["avatar"]
                assert av.startswith("http"), f"Invalid non-http avatar in {fname} [{idx}]: {av}"
        print(f"  Pillar 1 Verified: {fname} (0 spurious fields across {count} entries)")
    print("Test 2 PASS: Pillar 1 compliant on all non-NPC lorebooks.")

def test_pillar_2_npc_keys():
    print("\n--- Test 3: Pillar 2 (NPC Umbrella Keys & Generic Triggers) ---")
    for fname, _, kind, count in LOREBOOKS:
        if kind != "npc":
            continue
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            name = entry.get("name", "")
            keys = [k.strip().lower() for k in entry.get("keys", [])]
            sec_keys = [k.strip().lower() for k in entry.get("secondary_keys", [])]
            
            # Check canonical broad keys in primary keys
            for bk in CANONICAL_BROAD_KEYS:
                assert bk not in keys, f"Found exact broad key '{bk}' in {fname} [{idx}] {name}"
                
            # Check banned phrases in primary keys
            for bp in BANNED_NPC_PHRASES:
                assert bp not in keys, f"Found banned phrase '{bp}' in {fname} [{idx}] {name}"
                
            # Check Malachia's secondary_keys
            if "Malachia" in name and "Bloodmoon" in name:
                assert "alpha" not in sec_keys, f"Found 'alpha' in Malachia's secondary_keys in {fname} [{idx}]"
                print(f"    Verified Malachia secondary_keys without 'Alpha': {entry.get('secondary_keys')}")
                
            # Check selective discipline
            if entry.get("selective") is True:
                assert len(entry.get("secondary_keys", [])) > 0, f"Selective=True with empty secondary_keys on [{idx}] {name}"
                
            # Proper names check
            if name == "Roman Blackwood":
                assert "Roman Blackwood" in entry.get("keys", []), f"Roman Blackwood key missing!"
            if "Katarina" in name and "Blackwood" in name:
                assert any("Katarina" in k for k in entry.get("keys", [])), f"Katarina Blackwood key missing!"
                
        print(f"  Pillar 2 Verified: {fname} ({count} entries cleanly pruned)")
    print("Test 3 PASS: Pillar 2 compliant on all NPC lorebooks.")

def test_pillar_3_zero_age_macros():
    print("\n--- Test 4: Pillar 3 (Zero Residual {{age}} Macros) ---")
    for fname, _, _, _ in LOREBOOKS:
        for folder_name, folder_path in [("FINAL", FINAL_DIR), ("lorebooks/optimized", OPTIMIZED_DIR)]:
            fpath = os.path.join(folder_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            matches = re.findall(r"\{\{\s*age\s*\}\}", content, re.IGNORECASE)
            assert len(matches) == 0, f"Found {len(matches)} residual {{{{age}}}} macros in {folder_name}/{fname}!"
            print(f"  Pillar 3 Verified: {folder_name}/{fname} (0 {{{{age}}}} macros)")
    print("Test 4 PASS: Pillar 3 zero {{age}} macros verified across FINAL/ and lorebooks/optimized/.")

def test_pillar_4_npc_avatars_and_regex():
    print("\n--- Test 5: Pillar 4 (NPC Avatars & Regex Splitting) ---")
    reg_pat = re.compile(r"^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$")
    total_npcs = 0
    total_fallback = 0
    total_custom = 0
    
    for fname, _, kind, count in LOREBOOKS:
        if kind != "npc":
            continue
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        for idx, entry in enumerate(d["lexicon"]):
            total_npcs += 1
            name = entry.get("name", "")
            av = entry.get("avatar", "")
            assert av.startswith("http"), f"NPC [{idx}] {name} in {fname} has non-http avatar: '{av}'"
            if av == FALLBACK_AVATAR:
                total_fallback += 1
            else:
                total_custom += 1
                
            assert entry.get("custom_avatar_regex") is True, f"NPC [{idx}] {name} in {fname} lacks custom_avatar_regex: true"
            assert entry.get("lines_parsed") == 1, f"NPC [{idx}] {name} in {fname} has lines_parsed != 1"
            rg = entry.get("avatar_activation_regex", "")
            assert reg_pat.match(rg), f"NPC [{idx}] {name} in {fname} has invalid regex: '{rg}'"
        print(f"  Pillar 4 Verified: {fname} ({count} NPCs with valid avatar & multiline regex)")
        
    assert total_npcs == 416, f"Expected 416 NPCs, got {total_npcs}"
    assert total_fallback == 302, f"Expected 302 fallback avatars, got {total_fallback}"
    assert total_custom == 114, f"Expected 114 custom avatars, got {total_custom}"
    print(f"Test 5 PASS: All 416 NPCs verified (114 original valid URLs, 302 Svartúlfr Crest fallbacks).")

def test_missing_avatars_log():
    print("\n--- Test 6: Missing Avatars JSON Log Verification ---")
    log_path = os.path.join(SCRATCH_DIR, "missing_npc_avatars.json")
    assert os.path.exists(log_path), f"Log file {log_path} does not exist!"
    with open(log_path, "r", encoding="utf-8") as f:
        log_data = json.load(f)
    assert log_data["total_remediated"] == 302, f"Expected total_remediated=302, got {log_data['total_remediated']}"
    assert log_data["canonical_fallback_url"] == FALLBACK_AVATAR
    assert log_data["summary"]["Svartulfr_NPC_Primary"] == 44
    assert log_data["summary"]["Svartulfr_NPC_Secondary"] == 258
    assert len(log_data["entries"]) == 302
    print(f"Test 6 PASS: missing_npc_avatars.json verified ({len(log_data['entries'])} logged entries).")

def test_dual_array_synchronization():
    print("\n--- Test 7: Dual Array Synchronization (entries == lexicon) ---")
    total_count = 0
    for fname, _, _, expected_cnt in LOREBOOKS:
        for folder_name, folder_path in [("FINAL", FINAL_DIR), ("lorebooks/optimized", OPTIMIZED_DIR)]:
            fpath = os.path.join(folder_path, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                d = json.load(f)
            entries = d.get("entries", [])
            lexicon = d.get("lexicon", [])
            assert len(entries) == expected_cnt, f"{folder_name}/{fname}: entries count {len(entries)} != {expected_cnt}"
            assert len(lexicon) == expected_cnt, f"{folder_name}/{fname}: lexicon count {len(lexicon)} != {expected_cnt}"
            assert entries == lexicon, f"{folder_name}/{fname}: entries and lexicon arrays are NOT identical!"
        total_count += expected_cnt
        print(f"  Synchronized: {fname} (entries == lexicon, count={expected_cnt})")
    assert total_count == 1009, f"Expected 1,009 total entries, got {total_count}"
    print(f"Test 7 PASS: Dual array synchronization verified across all 6 files in both FINAL/ and lorebooks/optimized/ (Total: 1,009).")

def test_mirror_checksums():
    print("\n--- Test 8: Repository Mirror Checksums ---")
    for fname, _, _, _ in LOREBOOKS:
        f_path = os.path.join(FINAL_DIR, fname)
        o_path = os.path.join(OPTIMIZED_DIR, fname)
        f_h = md5_file(f_path)
        o_h = md5_file(o_path)
        assert f_h == o_h, f"Checksum mismatch for {fname}: FINAL={f_h}, optimized={o_h}"
        assert os.path.getsize(f_path) == os.path.getsize(o_path), f"Size mismatch for {fname}"
        print(f"  Mirror Identical: {fname} (md5: {f_h})")
    print("Test 8 PASS: lorebooks/optimized/ is 100% byte-for-byte identical to FINAL/.")

def main():
    print("=================================================================")
    print("RUNNING COMPREHENSIVE VERIFICATION SUITE (R1 & R2)")
    print("=================================================================")
    test_safety_backup()
    test_pillar_1_non_npc_clean()
    test_pillar_2_npc_keys()
    test_pillar_3_zero_age_macros()
    test_pillar_4_npc_avatars_and_regex()
    test_missing_avatars_log()
    test_dual_array_synchronization()
    test_mirror_checksums()
    print("\n=================================================================")
    print("ALL 8 VERIFICATION TESTS PASSED WITH 100% SUCCESS!")
    print("=================================================================")

if __name__ == "__main__":
    main()
