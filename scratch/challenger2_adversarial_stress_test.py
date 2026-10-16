"""
Adversarial Stress Test Suite for Milestones R1 & R2
Role: Empirical Challenger 2 (Trigger Collision & Fallback Rigor)
"""

import os
import json
import re
import sys
from collections import defaultdict

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
FINAL_DIR = os.path.join(PROJECT_ROOT, "FINAL")
BACKUP_DIR = os.path.join(PROJECT_ROOT, "scratch", "backup_pre_audit_lorebooks")
OPTIMIZED_DIR = os.path.join(PROJECT_ROOT, "lorebooks", "optimized")
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch")

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

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

LOREBOOKS = [
    ("Svartulfr_Lorebook_I.json", "_gwwCxCfQ6PQaLEjAQVpJL", "non_npc", 219),
    ("Svartulfr_Lorebook_II.json", "_HfG7TeV6MJyj6bxMwxkpt", "non_npc", 143),
    ("Svartulfr_Lorebook_III.json", "_9zWTGqYJNJ4BCDMj8gfcD", "non_npc", 35),
    ("Svartulfr_Location.json", "_EjXxkmPVhpCXg8xABpFkK", "non_npc", 196),
    ("Svartulfr_NPC_Primary.json", "_zwEqgEEzh12X6gHVmMKKC", "npc", 106),
    ("Svartulfr_NPC_Secondary.json", "_Uht3Ckz44JBDrPnUHq7LV", "npc", 310),
]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_adversarial_tests():
    print("=" * 70)
    print("EMPIRICAL CHALLENGER 2: ADVERSARIAL STRESS TEST SUITE (R1 & R2)")
    print("=" * 70)
    
    findings = []
    warnings = []
    
    # -------------------------------------------------------------------------
    # TEST SUITE 1: Backup vs FINAL Deep Diff Across All 416 NPCs
    # -------------------------------------------------------------------------
    print("\n>>> SUITE 1: Deep Diff Analysis between Pre-Audit Backup and FINAL")
    
    total_npc_entries = 0
    all_npc_final = []
    all_npc_backup = {}
    
    for fname, l_id, kind, count in LOREBOOKS:
        if kind != "npc":
            continue
        backup_path = os.path.join(BACKUP_DIR, fname)
        final_path = os.path.join(FINAL_DIR, fname)
        
        b_data = load_json(backup_path)
        f_data = load_json(final_path)
        
        b_lex = b_data.get("lexicon", [])
        f_lex = f_data.get("lexicon", [])
        
        assert len(b_lex) == count, f"Backup {fname} count {len(b_lex)} != {count}"
        assert len(f_lex) == count, f"Final {fname} count {len(f_lex)} != {count}"
        
        for idx in range(count):
            total_npc_entries += 1
            b_entry = b_lex[idx]
            f_entry = f_lex[idx]
            
            entry_id = f_entry.get("entry_id")
            name = f_entry.get("name", "")
            
            # Map by entry_id
            all_npc_backup[entry_id] = (fname, idx, b_entry)
            all_npc_final.append((fname, idx, f_entry))
            
            # Check what fields mutated between backup and final
            mutated_fields = []
            for k in set(b_entry.keys()).union(set(f_entry.keys())):
                if b_entry.get(k) != f_entry.get(k):
                    mutated_fields.append(k)
                    
            # We expect mutations only in keys, secondary_keys, avatar, or selective (if secondary_keys was empty)
            unexpected_mutations = [k for k in mutated_fields if k not in ["keys", "secondary_keys", "avatar", "selective"]]
            if unexpected_mutations:
                findings.append(f"CRITICAL: Unexpected field mutation in {fname} [{idx}] '{name}' (ID: {entry_id}): {unexpected_mutations}")
                
    print(f"Loaded {total_npc_entries} total NPC entries across Primary and Secondary.")
    
    # -------------------------------------------------------------------------
    # TEST SUITE 2: Pruned Trigger Keys and Proper Name Preservation
    # -------------------------------------------------------------------------
    print("\n>>> SUITE 2: Pruned Trigger Keys & Proper Name Preservation")
    
    removed_keys_map = {}
    removed_sec_keys_map = {}
    
    for fname, idx, f_entry in all_npc_final:
        entry_id = f_entry.get("entry_id")
        name = f_entry.get("name", "")
        _, _, b_entry = all_npc_backup[entry_id]
        
        b_keys = b_entry.get("keys", [])
        f_keys = f_entry.get("keys", [])
        
        b_sec = b_entry.get("secondary_keys", [])
        f_sec = f_entry.get("secondary_keys", [])
        
        rem_keys = [k for k in b_keys if k not in f_keys]
        if rem_keys:
            removed_keys_map[f"{fname}:{name} (id:{entry_id})"] = rem_keys
            
        rem_sec = [k for k in b_sec if k not in f_sec]
        if rem_sec:
            removed_sec_keys_map[f"{fname}:{name} (id:{entry_id})"] = rem_sec
            
        # Check that NPC still has >= 1 valid, non-empty primary key
        if len(f_keys) < 1:
            findings.append(f"CRITICAL: NPC {fname} [{idx}] '{name}' has NO primary keys!")
        for k in f_keys:
            if not k or not k.strip():
                findings.append(f"CRITICAL: NPC {fname} [{idx}] '{name}' has empty key in keys: {f_keys}")
                
    print(f"Total NPCs with pruned primary keys: {len(removed_keys_map)}")
    for who, klist in removed_keys_map.items():
        print(f"  {who} -> Removed keys: {klist}")
        
    print(f"Total NPCs with pruned secondary keys: {len(removed_sec_keys_map)}")
    for who, klist in removed_sec_keys_map.items():
        print(f"  {who} -> Removed secondary keys: {klist}")
        
    # Check that removed keys match ONLY expected banned phrases / broad keys
    for who, klist in removed_keys_map.items():
        for k in klist:
            kl = k.strip().lower()
            if kl not in BANNED_NPC_PHRASES and kl not in CANONICAL_BROAD_KEYS:
                findings.append(f"CRITICAL: Key '{k}' removed from {who} was NOT in BANNED_NPC_PHRASES or CANONICAL_BROAD_KEYS!")
                
    for who, klist in removed_sec_keys_map.items():
        for k in klist:
            kl = k.strip().lower()
            if kl not in BANNED_NPC_PHRASES and kl not in CANONICAL_BROAD_KEYS:
                findings.append(f"CRITICAL: Secondary key '{k}' removed from {who} was NOT in BANNED_NPC_PHRASES or CANONICAL_BROAD_KEYS!")
                
    # Check proper names preservation specifically
    print("\n--- Checking Proper Names Preservation ---")
    roman_found = False
    kat_found = False
    for fname, idx, f_entry in all_npc_final:
        name = f_entry.get("name", "")
        keys = f_entry.get("keys", [])
        if name == "Roman Blackwood":
            roman_found = True
            assert "Roman Blackwood" in keys, f"Roman Blackwood key missing: {keys}"
            print(f"  Verified Roman Blackwood keys: {keys}")
        if "Katarina" in name and "Blackwood" in name:
            kat_found = True
            assert any("Katarina" in k for k in keys), f"Katarina Blackwood key missing: {keys}"
            print(f"  Verified Katarina 'Kat' Blackwood keys: {keys}")
    assert roman_found and kat_found, "Did not find Roman or Katarina Blackwood in NPC set!"

    # -------------------------------------------------------------------------
    # TEST SUITE 3: Adversarial Search for Residual Broad Keys and Collisions
    # -------------------------------------------------------------------------
    print("\n>>> SUITE 3: Adversarial Residual Broad Keys & Trigger Collision Mining")
    
    # 3.1 Check every single key and secondary_key across all 416 NPCs for exact broad keys or banned phrases
    exact_broad_key_hits = []
    banned_phrase_hits = []
    
    # Also search for substrings of canonical broad keys to audit whether they are proper names or suspect
    substring_hits = defaultdict(list)
    
    for fname, idx, f_entry in all_npc_final:
        name = f_entry.get("name", "")
        keys = f_entry.get("keys", [])
        sec = f_entry.get("secondary_keys", [])
        
        for k in keys:
            kl = k.strip().lower()
            if kl in CANONICAL_BROAD_KEYS:
                exact_broad_key_hits.append((fname, idx, name, "primary", k))
            if kl in BANNED_NPC_PHRASES:
                banned_phrase_hits.append((fname, idx, name, "primary", k))
            for bk in CANONICAL_BROAD_KEYS:
                if re.search(r'\b' + re.escape(bk) + r'\b', kl):
                    substring_hits[bk].append((fname, idx, name, "primary", k))
                    
        for k in sec:
            kl = k.strip().lower()
            if kl in CANONICAL_BROAD_KEYS:
                exact_broad_key_hits.append((fname, idx, name, "secondary", k))
            if kl in BANNED_NPC_PHRASES:
                banned_phrase_hits.append((fname, idx, name, "secondary", k))
            for bk in CANONICAL_BROAD_KEYS:
                if re.search(r'\b' + re.escape(bk) + r'\b', kl):
                    substring_hits[bk].append((fname, idx, name, "secondary", k))
                    
    if exact_broad_key_hits:
        for hit in exact_broad_key_hits:
            findings.append(f"CRITICAL: Exact canonical broad key in {hit[0]} [{hit[1]}] '{hit[2]}' ({hit[3]}): '{hit[4]}'")
    else:
        print("  PASS: Exactly 0 exact CANONICAL_BROAD_KEYS found across all 416 NPCs.")
        
    if banned_phrase_hits:
        for hit in banned_phrase_hits:
            findings.append(f"CRITICAL: Banned umbrella phrase in {hit[0]} [{hit[1]}] '{hit[2]}' ({hit[3]}): '{hit[4]}'")
    else:
        print("  PASS: Exactly 0 BANNED_NPC_PHRASES found across all 416 NPCs.")
        
    print("\n--- Substring / Word-Boundary Audit of BROAD_KEYS in NPC Keys ---")
    for bk, occurrences in substring_hits.items():
        print(f"  Occurrences of word '{bk}' in NPC keys ({len(occurrences)}):")
        for fname, idx, name, ktype, k in occurrences:
            print(f"    [{fname}][{ktype}] NPC: '{name}' -> Key: '{k}'")
            # Verify if this is a legitimate proper name or an umbrella term!
            kl = k.lower()
            if bk == "blackwood":
                # Check that it's a person name (e.g. Roman Blackwood, Katarina Blackwood)
                if not any(pn in kl for pn in ["roman", "katarina", "kat", "cynthia", "edric", "magnus", "erik", "logan", "alyssa", "jasper", "malachia", "noah", "marcus"]):
                    warnings.append(f"Potentially broad Blackwood key: '{k}' on NPC '{name}' in {fname}")
            elif bk in ["alpha", "omega", "werewolf", "vampire", "student", "college", "solarton", "succ"]:
                warnings.append(f"Broad key '{bk}' found inside key '{k}' on NPC '{name}' in {fname} ({ktype})")

    # 3.2 Check for Primary Key Collisions (Exact Duplicate Keys between DIFFERENT NPCs)
    print("\n--- Key Collision Matrix across all 416 NPCs ---")
    key_to_npcs = defaultdict(list)
    for fname, idx, f_entry in all_npc_final:
        name = f_entry.get("name", "")
        keys = f_entry.get("keys", [])
        for k in keys:
            key_clean = k.strip().lower()
            key_to_npcs[key_clean].append((fname, idx, name, k))
            
    collisions = {k: npcs for k, npcs in key_to_npcs.items() if len(npcs) > 1}
    print(f"Total collision keys shared by multiple NPCs: {len(collisions)}")
    for k, npcs in collisions.items():
        print(f"  Collision on key '{k}' ({len(npcs)} NPCs):")
        for fname, idx, name, orig_k in npcs:
            print(f"    - {name} ({fname} [{idx}]) [orig: '{orig_k}']")
            
    # 3.3 Check for Extremely Short Keys (length <= 3)
    print("\n--- Extremely Short Primary Keys (len <= 3) ---")
    short_keys = []
    for fname, idx, f_entry in all_npc_final:
        name = f_entry.get("name", "")
        keys = f_entry.get("keys", [])
        for k in keys:
            if len(k.strip()) <= 3:
                short_keys.append((fname, idx, name, k))
    print(f"Total short keys (len <= 3): {len(short_keys)}")
    for fname, idx, name, k in short_keys:
        print(f"  Short key: '{k}' on NPC '{name}' in {fname}")

    # -------------------------------------------------------------------------
    # TEST SUITE 4: Fallback Avatars & Missing Avatars Log Rigorous Verification
    # -------------------------------------------------------------------------
    print("\n>>> SUITE 4: Avatar Integrity & scratch/missing_npc_avatars.json Verification")
    
    missing_log_path = os.path.join(SCRATCH_DIR, "missing_npc_avatars.json")
    assert os.path.exists(missing_log_path), "missing_npc_avatars.json does NOT exist!"
    log_data = load_json(missing_log_path)
    
    log_entries = log_data.get("entries", [])
    assert len(log_entries) == 302, f"Expected 302 entries in log, got {len(log_entries)}"
    assert log_data.get("total_remediated") == 302, f"total_remediated in log header is {log_data.get('total_remediated')}"
    assert log_data.get("canonical_fallback_url") == FALLBACK_AVATAR
    
    # Create mapping of logged entry IDs
    logged_entry_ids = set()
    for item in log_entries:
        logged_entry_ids.add(item["entry_id"])
    assert len(logged_entry_ids) == 302, f"Duplicate entry IDs in missing_npc_avatars.json! Unique={len(logged_entry_ids)}"
    
    # Audit all 416 NPCs for avatar transitions:
    pre_empty_or_invalid_count = 0
    pre_valid_count = 0
    
    fallback_assigned_count = 0
    valid_untouched_count = 0
    
    for fname, idx, f_entry in all_npc_final:
        entry_id = f_entry.get("entry_id")
        name = f_entry.get("name", "")
        _, _, b_entry = all_npc_backup[entry_id]
        
        b_av = (b_entry.get("avatar") or "").strip()
        f_av = (f_entry.get("avatar") or "").strip()
        
        # Check pre-audit avatar state
        if not b_av.startswith("http"):
            pre_empty_or_invalid_count += 1
            # MUST be in logged_entry_ids
            if entry_id not in logged_entry_ids:
                findings.append(f"CRITICAL: NPC {fname} [{idx}] '{name}' had empty/invalid avatar in backup but was NOT logged in missing_npc_avatars.json!")
            # MUST now have FALLBACK_AVATAR
            if f_av != FALLBACK_AVATAR:
                findings.append(f"CRITICAL: NPC {fname} [{idx}] '{name}' had empty avatar in backup but does NOT have canonical fallback in FINAL! Got: '{f_av}'")
            else:
                fallback_assigned_count += 1
        else:
            pre_valid_count += 1
            # MUST NOT be in logged_entry_ids
            if entry_id in logged_entry_ids:
                findings.append(f"CRITICAL: NPC {fname} [{idx}] '{name}' had valid avatar '{b_av}' in backup but was erroneously logged in missing_npc_avatars.json!")
            # MUST NOT have been changed in FINAL!
            if f_av != b_av:
                findings.append(f"CRITICAL: Valid avatar for NPC {fname} [{idx}] '{name}' was MUTATED! Pre: '{b_av}' -> Post: '{f_av}'")
            else:
                valid_untouched_count += 1
                
    print(f"Pre-audit valid avatars: {pre_valid_count} (Expected 114)")
    print(f"Pre-audit empty/invalid avatars: {pre_empty_or_invalid_count} (Expected 302)")
    print(f"Post-remediation valid avatars untouched: {valid_untouched_count} (Expected 114)")
    print(f"Post-remediation fallback avatars assigned: {fallback_assigned_count} (Expected 302)")
    
    assert pre_valid_count == 114, f"Pre-valid count mismatch: {pre_valid_count} != 114"
    assert pre_empty_or_invalid_count == 302, f"Pre-empty count mismatch: {pre_empty_or_invalid_count} != 302"
    assert valid_untouched_count == 114, f"Valid untouched mismatch: {valid_untouched_count} != 114"
    assert fallback_assigned_count == 302, f"Fallback assigned mismatch: {fallback_assigned_count} != 302"

    # Cross-reference every single entry in missing_npc_avatars.json with FINAL/
    for logged in log_entries:
        lid = logged["entry_id"]
        lfname = logged["lorebook"]
        lidx = logged["index"]
        lname = logged["name"]
        
        # Check against backup
        assert lid in all_npc_backup, f"Logged entry {lid} not in backup!"
        bfname, bidx, bentry = all_npc_backup[lid]
        assert bfname == lfname, f"Lorebook mismatch for {lid}: log={lfname}, backup={bfname}"
        assert bidx == lidx, f"Index mismatch for {lid}: log={lidx}, backup={bidx}"
        assert bentry.get("name") == lname, f"Name mismatch for {lid}: log={lname}, backup={bentry.get('name')}"
        assert not (bentry.get("avatar") or "").strip().startswith("http"), f"Entry {lid} logged as missing avatar actually had: '{bentry.get('avatar')}'"
        
        # Check against FINAL
        final_file_path = os.path.join(FINAL_DIR, lfname)
        f_data = load_json(final_file_path)
        f_entry = f_data["lexicon"][lidx]
        assert f_entry["entry_id"] == lid
        assert f_entry["name"] == lname
        assert f_entry["avatar"] == FALLBACK_AVATAR
        assert f_entry.get("custom_avatar_regex") is True
        assert f_entry.get("lines_parsed") == 1
        assert f_entry.get("avatar_activation_regex", "").startswith("(?:^|\\n)")
        
    print("  PASS: 100% of 302 logged entries match exact entries in FINAL/ and were previously empty.")
    print("  PASS: 100% of 114 previously valid avatars were preserved byte-for-byte.")

    # -------------------------------------------------------------------------
    # TEST SUITE 5: Non-NPC Cleanliness and Array Synchronization
    # -------------------------------------------------------------------------
    print("\n>>> SUITE 5: Non-NPC Metadata & Dual Array Synchronization")
    for fname, _, kind, expected_count in LOREBOOKS:
        for folder_name, folder_path in [("FINAL", FINAL_DIR), ("lorebooks/optimized", OPTIMIZED_DIR)]:
            fpath = os.path.join(folder_path, fname)
            d = load_json(fpath)
            lex = d.get("lexicon", [])
            ent = d.get("entries", [])
            assert len(lex) == expected_count, f"{folder_name}/{fname} lexicon count {len(lex)} != {expected_count}"
            assert len(ent) == expected_count, f"{folder_name}/{fname} entries count {len(ent)} != {expected_count}"
            assert ent == lex, f"{folder_name}/{fname} entries != lexicon"
            
            if kind == "non_npc":
                for idx, item in enumerate(lex):
                    for spurious in ["avatar_activation_regex", "custom_avatar_regex", "lines_parsed", "npc_info"]:
                        if spurious in item:
                            findings.append(f"CRITICAL: Non-NPC entry in {folder_name}/{fname} [{idx}] contains '{spurious}'!")
                    if "avatar" in item:
                        av = item["avatar"]
                        if not av.startswith("http"):
                            findings.append(f"CRITICAL: Non-NPC entry in {folder_name}/{fname} [{idx}] contains non-http avatar: '{av}'")
                            
    print("  PASS: All 6 lorebooks synchronized and non-NPC entries verified clean.")
    
    # -------------------------------------------------------------------------
    # SUMMARY OF ADVERSARIAL FINDINGS
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY OF ADVERSARIAL CHALLENGE FINDINGS")
    print("=" * 70)
    print(f"CRITICAL FINDINGS (Bugs / Failures): {len(findings)}")
    for f in findings:
        print(f"  [X] {f}")
        
    print(f"\nWARNINGS / ADVERSARIAL OBSERVATIONS: {len(warnings)}")
    for w in warnings:
        print(f"  [!] {w}")
        
    if findings:
        print("\nADVERSARIAL VERDICT: REQUEST_CHANGES")
        sys.exit(1)
    else:
        print("\nADVERSARIAL VERDICT: ALL PASS")
        sys.exit(0)

if __name__ == "__main__":
    run_adversarial_tests()
