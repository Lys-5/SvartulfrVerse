"""
Automated 4-Pillar Remediation & Harmonization Script for Standalone Lorebooks
Svartúlfr Verse — Wyvern Architecture
Worker 1 (Milestones R1 & R2)
"""

import os
import json
import copy
import re
import shutil
from datetime import datetime, timezone

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
FINAL_DIR = os.path.join(PROJECT_ROOT, "FINAL")
OPTIMIZED_DIR = os.path.join(PROJECT_ROOT, "lorebooks", "optimized")
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch")

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

LOREBOOKS_CONFIG = {
    "Svartulfr_Lorebook_I.json": {
        "id": "_gwwCxCfQ6PQaLEjAQVpJL",
        "kind": "non_npc",
        "expected_count": 219
    },
    "Svartulfr_Lorebook_II.json": {
        "id": "_HfG7TeV6MJyj6bxMwxkpt",
        "kind": "non_npc",
        "expected_count": 143
    },
    "Svartulfr_Lorebook_III.json": {
        "id": "_9zWTGqYJNJ4BCDMj8gfcD",
        "kind": "non_npc",
        "expected_count": 35
    },
    "Svartulfr_Location.json": {
        "id": "_EjXxkmPVhpCXg8xABpFkK",
        "kind": "non_npc",
        "expected_count": 196
    },
    "Svartulfr_NPC_Primary.json": {
        "id": "_zwEqgEEzh12X6gHVmMKKC",
        "kind": "npc_primary",
        "expected_count": 106
    },
    "Svartulfr_NPC_Secondary.json": {
        "id": "_Uht3Ckz44JBDrPnUHq7LV",
        "kind": "npc_secondary",
        "expected_count": 310
    }
}

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

def remediate_non_npc_lorebook(filename, cfg):
    filepath = os.path.join(FINAL_DIR, filename)
    print(f"\n[Pillar 1] Remediating Non-NPC lorebook: {filename}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    lexicon = data.get("lexicon", [])
    assert len(lexicon) == cfg["expected_count"], f"Count mismatch in {filename}: expected {cfg['expected_count']}, got {len(lexicon)}"
    
    purged_regex_count = 0
    purged_empty_avatar_count = 0
    preserved_avatar_count = 0
    
    for idx, entry in enumerate(lexicon):
        assert entry.get("type") != "npc", f"Unexpected NPC in non-NPC file {filename} at index {idx}"
        
        # Purge avatar_activation_regex
        if "avatar_activation_regex" in entry:
            del entry["avatar_activation_regex"]
            purged_regex_count += 1
            
        # Purge spurious NPC metadata fields if present
        for spurious_field in ["custom_avatar_regex", "lines_parsed", "npc_info"]:
            if spurious_field in entry:
                del entry[spurious_field]
                
        # Handle avatar field: remove if empty/whitespace, preserve if valid http URL
        if "avatar" in entry:
            av = (entry.get("avatar") or "").strip()
            if not av.startswith("http"):
                del entry["avatar"]
                purged_empty_avatar_count += 1
            else:
                preserved_avatar_count += 1
                
        # Ensure selective: false if secondary_keys is empty
        if entry.get("selective") is True and not entry.get("secondary_keys"):
            entry["selective"] = False

    # Synchronize entries = lexicon (deep copy)
    data["lexicon"] = lexicon
    data["entries"] = copy.deepcopy(lexicon)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
        
    print(f"  Purged avatar_activation_regex: {purged_regex_count}")
    print(f"  Purged empty avatars: {purged_empty_avatar_count}")
    print(f"  Preserved valid avatars: {preserved_avatar_count}")
    print(f"  Dual array synchronized: len(entries)={len(data['entries'])}, len(lexicon)={len(data['lexicon'])}, equal={data['entries'] == data['lexicon']}")


def remediate_npc_lorebook(filename, cfg, missing_avatar_log):
    filepath = os.path.join(FINAL_DIR, filename)
    print(f"\n[Pillar 2 & 4] Remediating NPC lorebook: {filename}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    lexicon = data.get("lexicon", [])
    assert len(lexicon) == cfg["expected_count"], f"Count mismatch in {filename}: expected {cfg['expected_count']}, got {len(lexicon)}"
    
    pruned_keys_count = 0
    pruned_sec_keys_count = 0
    applied_avatar_count = 0
    preserved_avatar_count = 0
    
    for idx, entry in enumerate(lexicon):
        assert entry.get("type") == "npc", f"Non-NPC entry found in NPC file {filename} at index {idx}"
        name = entry.get("name", "")
        
        # 1. Prune secondary_keys for umbrella keywords (e.g. 'Alpha' on Malachia)
        sec_keys = entry.get("secondary_keys", [])
        new_sec_keys = []
        for sk in sec_keys:
            sk_clean = sk.strip()
            if sk_clean.lower() in CANONICAL_BROAD_KEYS or sk_clean.lower() in BANNED_NPC_PHRASES:
                print(f"  Pruning secondary_key '{sk}' from NPC [{idx}] {name}")
                pruned_sec_keys_count += 1
            else:
                new_sec_keys.append(sk_clean)
        entry["secondary_keys"] = new_sec_keys
        
        # 2. Prune primary keys for generic umbrella role triggers
        keys = entry.get("keys", [])
        new_keys = []
        for k in keys:
            k_clean = k.strip()
            # Safety safeguard: Never strip proper names
            if k_clean in ["Roman Blackwood", "Katarina 'Kat' Blackwood"]:
                new_keys.append(k_clean)
                continue
                
            if k_clean.lower() in BANNED_NPC_PHRASES or k_clean.lower() in CANONICAL_BROAD_KEYS:
                print(f"  Pruning primary key '{k}' from NPC [{idx}] {name}")
                pruned_keys_count += 1
            else:
                new_keys.append(k_clean)
                
        # Assert that if generic keys were pruned, the NPC retains >= 2 distinctive keys
        if len(keys) != len(new_keys):
            assert len(new_keys) >= 2, f"Affected NPC [{idx}] {name} has fewer than 2 keys after pruning: {new_keys}"
        entry["keys"] = new_keys
        
        # 3. Avatar validation & fallback assignment
        av = (entry.get("avatar") or "").strip()
        if not av.startswith("http"):
            # Missing avatar: assign canonical fallback
            missing_avatar_log.append({
                "lorebook": filename,
                "lorebook_id": cfg["id"],
                "entry_id": entry.get("entry_id"),
                "index": idx,
                "name": name,
                "previous_avatar": entry.get("avatar", ""),
                "applied_avatar": FALLBACK_AVATAR,
                "keys": new_keys
            })
            entry["avatar"] = FALLBACK_AVATAR
            applied_avatar_count += 1
        else:
            preserved_avatar_count += 1
            
        # 4. Enforce regex activation splitting standards
        entry["custom_avatar_regex"] = True
        entry["lines_parsed"] = 1
        reg = entry.get("avatar_activation_regex", "")
        assert reg.startswith("(?:^|\\n)"), f"Invalid regex pattern on NPC [{idx}] {name}: {reg}"
        
        # 5. Selective logic check
        if entry.get("selective") is True and not entry.get("secondary_keys"):
            entry["selective"] = False

    # Synchronize entries = lexicon (deep copy)
    data["lexicon"] = lexicon
    data["entries"] = copy.deepcopy(lexicon)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
        
    print(f"  Pruned primary trigger keys: {pruned_keys_count}")
    print(f"  Pruned secondary trigger keys: {pruned_sec_keys_count}")
    print(f"  Assigned fallback avatars: {applied_avatar_count}")
    print(f"  Preserved existing valid avatars: {preserved_avatar_count}")
    print(f"  Dual array synchronized: len(entries)={len(data['entries'])}, len(lexicon)={len(data['lexicon'])}, equal={data['entries'] == data['lexicon']}")


def main():
    print("=================================================================")
    print("STARTING 4-PILLAR AUTOMATED REMEDIATION (MILESTONES R1 & R2)")
    print("=================================================================")
    
    missing_avatar_log = []
    
    # Process all 6 files
    for filename, cfg in LOREBOOKS_CONFIG.items():
        if cfg["kind"] == "non_npc":
            remediate_non_npc_lorebook(filename, cfg)
        else:
            remediate_npc_lorebook(filename, cfg, missing_avatar_log)
            
    # Check total missing avatars logged
    print("\n-----------------------------------------------------------------")
    print("WRITING MISSING AVATAR AUDIT LOG")
    print("-----------------------------------------------------------------")
    print(f"Total NPCs remediated with fallback avatar: {len(missing_avatar_log)}")
    assert len(missing_avatar_log) == 302, f"Expected 302 remediated avatars, got {len(missing_avatar_log)}"
    
    prim_count = sum(1 for e in missing_avatar_log if e["lorebook"] == "Svartulfr_NPC_Primary.json")
    sec_count = sum(1 for e in missing_avatar_log if e["lorebook"] == "Svartulfr_NPC_Secondary.json")
    assert prim_count == 44, f"Expected 44 Primary NPCs, got {prim_count}"
    assert sec_count == 258, f"Expected 258 Secondary NPCs, got {sec_count}"
    
    log_payload = {
        "audit_timestamp": datetime.now(timezone.utc).isoformat(),
        "canonical_fallback_url": FALLBACK_AVATAR,
        "total_remediated": len(missing_avatar_log),
        "summary": {
            "Svartulfr_NPC_Primary": prim_count,
            "Svartulfr_NPC_Secondary": sec_count
        },
        "entries": missing_avatar_log
    }
    
    log_path = os.path.join(SCRATCH_DIR, "missing_npc_avatars.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_payload, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Successfully wrote audit log to {log_path} ({os.path.getsize(log_path)} bytes)")

    # Assert 0 residual {{age}} macros across all 6 files
    print("\n-----------------------------------------------------------------")
    print("VALIDATING ZERO {{age}} MACROS ACROSS ALL 6 LOREBOOKS (PILLAR 3)")
    print("-----------------------------------------------------------------")
    for filename in LOREBOOKS_CONFIG.keys():
        filepath = os.path.join(FINAL_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r"\{\{\s*age\s*\}\}", content, re.IGNORECASE)
        assert len(matches) == 0, f"Found {len(matches)} residual {{{{age}}}} macros in {filename}!"
        print(f"  {filename}: 0 {{{{age}}}} macros (PASS)")
        
    # Mirror all 6 remediated files to lorebooks/optimized/
    print("\n-----------------------------------------------------------------")
    print("MIRRORING REMEDIATED FILES TO lorebooks/optimized/")
    print("-----------------------------------------------------------------")
    os.makedirs(OPTIMIZED_DIR, exist_ok=True)
    for filename in LOREBOOKS_CONFIG.keys():
        src = os.path.join(FINAL_DIR, filename)
        dst = os.path.join(OPTIMIZED_DIR, filename)
        shutil.copy2(src, dst)
        src_sz = os.path.getsize(src)
        dst_sz = os.path.getsize(dst)
        assert src_sz == dst_sz, f"Size mismatch during mirroring of {filename}"
        print(f"  Mirrored {filename} -> lorebooks/optimized/ ({dst_sz} bytes)")
        
    print("\n=================================================================")
    print("AUTOMATED REMEDIATION & MIRRORING COMPLETED SUCCESSFULLY!")
    print("=================================================================")

if __name__ == "__main__":
    main()
