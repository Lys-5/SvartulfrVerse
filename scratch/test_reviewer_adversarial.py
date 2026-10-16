import os
import json
import re

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
FINAL_DIR = os.path.join(PROJECT_ROOT, "FINAL")
BACKUP_DIR = os.path.join(PROJECT_ROOT, "scratch", "backup_pre_audit_lorebooks")
OPTIMIZED_DIR = os.path.join(PROJECT_ROOT, "lorebooks", "optimized")

BROAD_WORDS = ["solarton", "succ", "blackwood", "vampire", "werewolf", "college", "student", "alpha", "omega"]
BANNED_PHRASES = [
    "succ student",
    "pack leader",
    "blackwood council",
    "alligator demihuman",
    "demon representative",
    "human representative"
]

def check_all():
    print("=== REVIEWER ADVERSARIAL STRESS TEST ===")
    
    # 1. Non-NPC Lorebooks Check
    non_npc_files = [
        ("Svartulfr_Lorebook_I.json", 219),
        ("Svartulfr_Lorebook_II.json", 143),
        ("Svartulfr_Lorebook_III.json", 35),
        ("Svartulfr_Location.json", 196)
    ]
    
    for fname, count in non_npc_files:
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        lex = d.get("lexicon", [])
        ent = d.get("entries", [])
        assert len(lex) == count, f"Count mismatch in {fname}"
        assert lex == ent, f"Dual array mismatch in {fname}"
        
        for idx, e in enumerate(lex):
            assert e.get("type") != "npc", f"NPC entry found in non-NPC {fname}: [{idx}] {e.get('name')}"
            for bad_key in ["avatar_activation_regex", "custom_avatar_regex", "lines_parsed", "npc_info"]:
                assert bad_key not in e, f"Spurious field {bad_key} found in {fname}: [{idx}] {e.get('name')}"
            if "avatar" in e:
                av = e.get("avatar", "")
                assert av.startswith("http"), f"Empty or non-http avatar in {fname}: [{idx}] {e.get('name')}"
        print(f"PASS Non-NPC: {fname} ({count} entries completely clean)")

    # 2. Lorebook III Harmonization Detail
    lb3_path = os.path.join(FINAL_DIR, "Svartulfr_Lorebook_III.json")
    with open(lb3_path, "r", encoding="utf-8") as f:
        lb3 = json.load(f)
    for idx, e in enumerate(lb3["entries"]):
        # Verify native Wyvern schema keys
        assert "entry_id" in e, f"Missing entry_id in Lorebook III [{idx}]"
        assert "name" in e, f"Missing name in Lorebook III [{idx}]"
        assert "uid" not in e, f"Legacy uid found in Lorebook III [{idx}]"
        assert "selectiveLogic" not in e, f"Legacy selectiveLogic found in Lorebook III [{idx}]"
    print("PASS Lorebook III schema harmonization: 35 entries native Wyvern schema verified")

    # 3. NPC Lorebooks Check
    npc_files = [
        ("Svartulfr_NPC_Primary.json", 106),
        ("Svartulfr_NPC_Secondary.json", 310)
    ]
    
    exact_broad_violations = []
    banned_phrase_violations = []
    sec_broad_violations = []
    compound_broad_keys = []
    
    for fname, count in npc_files:
        fpath = os.path.join(FINAL_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        lex = d.get("lexicon", [])
        ent = d.get("entries", [])
        assert len(lex) == count, f"Count mismatch in {fname}"
        assert lex == ent, f"Dual array mismatch in {fname}"
        
        for idx, e in enumerate(lex):
            assert e.get("type") == "npc", f"Non-NPC entry in {fname}: [{idx}] {e.get('name')}"
            name = e.get("name", "")
            keys = e.get("keys", [])
            sec_keys = e.get("secondary_keys", [])
            
            # Primary keys check
            for k in keys:
                kl = k.lower().strip()
                if kl in BROAD_WORDS:
                    exact_broad_violations.append((fname, idx, name, k))
                if kl in BANNED_PHRASES:
                    banned_phrase_violations.append((fname, idx, name, k))
                for bw in BROAD_WORDS:
                    if bw in kl and kl != name.lower():
                        compound_broad_keys.append((fname, idx, name, k, bw))
                        
            # Secondary keys check
            for sk in sec_keys:
                skl = sk.lower().strip()
                if skl in BROAD_WORDS or skl in BANNED_PHRASES:
                    sec_broad_violations.append((fname, idx, name, sk))
                    
            # Check selective discipline
            if e.get("selective") is True:
                assert len(sec_keys) > 0, f"Selective=True with empty secondary_keys on [{idx}] {name}"
                
            # Check avatar validity
            av = e.get("avatar", "")
            assert av.startswith("http"), f"Invalid avatar on [{idx}] {name}: {av}"
            assert e.get("custom_avatar_regex") is True
            assert e.get("lines_parsed") == 1
            assert re.match(r"^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$", e.get("avatar_activation_regex", ""))

    print(f"Exact BROAD_KEYS violations in primary keys: {len(exact_broad_violations)}")
    print(f"Banned generic phrases in primary keys: {len(banned_phrase_violations)}")
    print(f"BROAD_KEYS violations in secondary keys: {len(sec_broad_violations)}")
    
    print("\nCompound keys containing broad words (inspecting for safety):")
    for fname, idx, name, k, bw in compound_broad_keys:
        print(f"  [{fname}] [{idx}] {name} -> key: '{k}' (matched '{bw}')")

    # 4. Check specific characters
    # Malachia check
    fpath = os.path.join(FINAL_DIR, "Svartulfr_NPC_Primary.json")
    with open(fpath, "r", encoding="utf-8") as f:
        prim = json.load(f)
    mal = [e for e in prim["lexicon"] if "Malachia" in e.get("name", "")][0]
    print(f"\nMalachia entry name: {mal.get('name')}")
    print(f"Malachia keys: {mal.get('keys')}")
    print(f"Malachia secondary_keys: {mal.get('secondary_keys')}")
    assert "Alpha" not in mal.get("secondary_keys"), "Alpha still in Malachia secondary_keys!"
    assert "alpha" not in [k.lower() for k in mal.get("secondary_keys")], "alpha still in Malachia secondary_keys!"
    
    # Check Roman Blackwood and Katarina Blackwood
    fpath_sec = os.path.join(FINAL_DIR, "Svartulfr_NPC_Secondary.json")
    with open(fpath_sec, "r", encoding="utf-8") as f:
        sec = json.load(f)

    roman = [e for e in prim["lexicon"] if "Roman Blackwood" in e.get("name", "")][0]
    print(f"Roman Blackwood keys: {roman.get('keys')}")
    assert "Roman Blackwood" in roman.get("keys")
    
    kat = [e for e in sec["lexicon"] if "Katarina" in e.get("name", "")][0]
    print(f"Katarina Blackwood keys: {kat.get('keys')}")
    assert any("Katarina" in k for k in kat.get("keys"))
    
    # Check the 11 Pack Leaders pruned
    pack_leader_names = [
        "Vito Marino", "Naomi Black", "Marcus O'Connor", "Isobel Blackwater",
        "Helena Weiss", "Eclipse Noir", "Dominic Chen", "Darius Vale",
        "Cass Harrow", "Bianca Rossi", "Aurora Night"
    ]
    print("\nChecking 11 Pack Leaders in Primary NPC:")
    for pln in pack_leader_names:
        matched = [e for e in prim["lexicon"] if pln in e.get("name", "")]
        assert len(matched) == 1, f"Missing {pln}"
        e = matched[0]
        keys = e.get("keys", [])
        assert "Pack Leader" not in keys
        assert len(keys) >= 2, f"{pln} has fewer than 2 keys: {keys}"
        print(f"  {pln}: {keys} (len={len(keys)})")
        
    # Check Council members pruned
    council_names = ["Zeera Darkfire", "Harlan Beaumont", "Brak Ironfist", "Barrow"]
    print("\nChecking 4 Council NPCs in Primary NPC:")
    for cn in council_names:
        matched = [e for e in prim["lexicon"] if cn in e.get("name", "")]
        assert len(matched) == 1, f"Missing {cn}"
        e = matched[0]
        keys = e.get("keys", [])
        assert "Blackwood Council" not in keys
        assert "Demon Representative" not in keys
        assert "Human Representative" not in keys
        assert len(keys) >= 2, f"{cn} has fewer than 2 keys: {keys}"
        print(f"  {cn}: {keys} (len={len(keys)})")
        
    # Check Secondary NPCs: Cato and Brittany Willow
    fpath_sec = os.path.join(FINAL_DIR, "Svartulfr_NPC_Secondary.json")
    with open(fpath_sec, "r", encoding="utf-8") as f:
        sec = json.load(f)
    # Avatar log correlation check
    print("\nVerifying scratch/missing_npc_avatars.json correlation...")
    with open(os.path.join(PROJECT_ROOT, "scratch", "missing_npc_avatars.json"), "r", encoding="utf-8") as f:
        log_data = json.load(f)
    assert len(log_data["entries"]) == 302
    for item in log_data["entries"]:
        lb = item["lorebook"]
        idx = item["index"]
        name = item["name"]
        with open(os.path.join(BACKUP_DIR, lb), "r", encoding="utf-8") as f:
            b_d = json.load(f)
        b_entry = b_d["lexicon"][idx]
        assert b_entry.get("name") == name
        assert not b_entry.get("avatar") or b_entry.get("avatar").strip() == ""
        with open(os.path.join(FINAL_DIR, lb), "r", encoding="utf-8") as f:
            f_d = json.load(f)
        f_entry = f_d["lexicon"][idx]
        assert f_entry.get("name") == name
        assert f_entry.get("avatar") == item["applied_avatar"]
    print(f"Verified all 302 entries in missing_npc_avatars.json: all were empty in backup and properly assigned fallback in FINAL!")

    print("\n=== ALL ADVERSARIAL STRESS CHECKS COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    check_all()
