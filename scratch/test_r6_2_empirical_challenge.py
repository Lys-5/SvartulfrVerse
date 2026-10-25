import json
import os
import re
import sys
import urllib.request
import urllib.error

def run_tests():
    print("======================================================================")
    print("CHALLENGER R6-2: EMPIRICAL STRESS TEST & INTEGRITY AUDIT")
    print("======================================================================")
    failures = []
    passes = []

    def assert_true(cond, msg):
        if cond:
            passes.append(msg)
            print(f"[PASS] {msg}")
        else:
            failures.append(msg)
            print(f"[FAIL] {msg}")

    # Helper to get entry identifier and text
    def get_id(e):
        return e.get("entry_id") or e.get("id")

    def get_text(e):
        return e.get("content") or e.get("description") or ""

    # ---------------------------------------------------------
    # 1. LOCAL LOREBOOK PRIMARY AUDIT
    # ---------------------------------------------------------
    primary_path = "FINAL/Svartulfr_NPC_Primary.json"
    assert_true(os.path.exists(primary_path), f"File {primary_path} exists")

    with open(primary_path, "r", encoding="utf-8") as f:
        primary_data = json.load(f)

    entries = primary_data.get("entries", [])
    lexicon = primary_data.get("lexicon", [])

    assert_true(len(entries) == 99, f"Local Primary entries count is 99 (actual: {len(entries)})")
    assert_true(len(lexicon) == 99, f"Local Primary lexicon count is 99 (actual: {len(lexicon)})")
    assert_true(entries == lexicon, "Local Primary entries and lexicon arrays are completely identical")

    # Map by entry_id / id
    entries_by_id = {get_id(e): e for e in entries if get_id(e)}
    
    target_specs = {
        "Scarlett Rose": {
            "id": "4NzXF4_0hYxmN7Idltzpw",
            "expected_card_id": "_qXgBMbFYJfc84hbLHhe92",
            "expected_personas": [],
            "names_for_regex": ["Scarlett Rose", "Scarlett"],
            "negative_test_sentences": [
                "I was looking at Scarlett Rose yesterday in class.",
                "Does Scarlett know about the lab assignment?"
            ]
        },
        "Sierra Cruz": {
            "id": "ijy8vrlphNv19-p-gbYuY",
            "expected_card_id": "_pnrXbkWqcgmFAf3meRWFY",
            "expected_personas": [],
            "names_for_regex": ["Sierra Cruz", "Sierra"],
            "negative_test_sentences": [
                "Sierra Cruz is not in the library right now.",
                "Why did Sierra leave early?"
            ]
        },
        "Russell 'Russ' Sinclair": {
            "id": "YCxAqNoShpefVvk0_Pc7i",
            "expected_card_id": "_wn6DkCcg3Xqa2Xpx9ttnT",
            "expected_personas": [],
            "names_for_regex": ["Russell Sinclair", "Russ Sinclair", "Russell 'Russ'", "Russell", "Russ"],
            "negative_test_sentences": [
                "I met Russ Sinclair at the quad.",
                "Russell was working on his laptop."
            ]
        },
        "Stanley Davies Jr.": {
            "id": "ekdQjq63xP7HtNuaPQJQE",
            "expected_card_id": "_Xd3NhKnRJByMTtdb6PjxJ",
            "expected_personas": [],
            "names_for_regex": ["Stanley Davies Jr.", "Stanley Davies", "Stan Davies", "Stan"],
            "negative_test_sentences": [
                "We saw Stanley Davies Jr. playing hockey.",
                "Stan Davies was sitting in the corner."
            ]
        },
        "Jared Thompson": {
            "id": "RM6rcwv8MlY1XWaCTQp0M",
            "expected_card_id": "_xJVPtBLL3dxy69RLKL9X9",
            "expected_personas": [],
            "names_for_regex": ["Jared Thompson", "J-Man", "Jared"],
            "negative_test_sentences": [
                "The quarterback Jared Thompson threw a touchdown.",
                "Hey Jared, pass the ball!"
            ]
        },
        "Alyssa Hvit Douglas Bloodmoon": {
            "id": "alyssa_world_dossier_2b54a223",
            "expected_card_id": "_6exg3yPfe2eCDK4hTftkh",
            "expected_personas": ["persona_1786335754946"],
            "names_for_regex": ["Alyssa Douglas", "Alyssa Hvit", "White Moon", "Alyssa"],
            "negative_test_sentences": [
                "Alyssa Douglas was seen near the medical sciences building.",
                "I asked Alyssa about the medicine."
            ]
        },
        "Jasper Svartr Douglas Bloodmoon": {
            "id": "Vcj4h2TL4Usola2A4OOl6",
            "expected_card_id": "_t4J9aQNJM36cUKAP4wB4U",
            "expected_personas": ["1792155173728"],
            "names_for_regex": ["Jasper Douglas", "Jasper Svartr", "Shadow Wolf", "Jasper"],
            "negative_test_sentences": [
                "Jasper Douglas is currently hacking the terminal.",
                "Tell Jasper to hurry up."
            ]
        }
    }

    umbrella_keywords = {"solarton", "succ", "blackwood", "vampire", "werewolf", "college", "student", "alpha", "omega"}

    print("\n--- Testing Target Entries in Local Lorebook Primary ---")
    for name, spec in target_specs.items():
        entry_id = spec["id"]
        assert_true(entry_id in entries_by_id, f"Entry {name} (id: {entry_id}) found in Primary entries")
        entry = entries_by_id.get(entry_id, {})
        
        # 1. Description/Content Length > 2000
        desc = get_text(entry)
        desc_len = len(desc)
        assert_true(desc_len > 2000, f"{name}: description length > 2,000 chars (actual: {desc_len} chars)")

        # 2. Schema fields
        assert_true(entry.get("type") == "npc", f"{name}: type is 'npc' (actual: {entry.get('type')})")
        assert_true(entry.get("selective") is False, f"{name}: selective is False (actual: {entry.get('selective')})")
        assert_true(entry.get("custom_avatar_regex") is True, f"{name}: custom_avatar_regex is True")
        assert_true(entry.get("lines_parsed") == 1, f"{name}: lines_parsed == 1")
        
        # 3. Avatar
        avatar = entry.get("avatar", "")
        assert_true(avatar.startswith("https://"), f"{name}: valid HTTPS avatar URL ({avatar})")

        # 4. Suppression arrays
        ignored_chars = entry.get("ignored_characters", [])
        expected_char = spec["expected_card_id"]
        assert_true(expected_char in ignored_chars, f"{name}: ignored_characters contains {expected_char} (actual: {ignored_chars})")

        ignored_pers = entry.get("ignored_personas", [])
        expected_pers = spec["expected_personas"]
        assert_true(set(ignored_pers) == set(expected_pers), f"{name}: ignored_personas matches {expected_pers} (actual: {ignored_pers})")

        # 5. Regex Stress Testing
        pattern_str = entry.get("avatar_activation_regex", "")
        assert_true(bool(pattern_str), f"{name}: avatar_activation_regex is populated ({pattern_str})")
        
        try:
            # Compiled with re.MULTILINE to match standard Wyvern engine behavior
            regex = re.compile(pattern_str, re.MULTILINE)
            
            # Positive test: start of string
            for speaker in spec["names_for_regex"]:
                test_msg1 = f'{speaker}: "Hello world."'
                m1 = regex.search(test_msg1)
                assert_true(m1 is not None, f"{name}: Regex matches start-of-line '{speaker}: \"...\"'")

                test_msg2 = f'\n{speaker}: "Dialogue on new line."'
                m2 = regex.search(test_msg2)
                assert_true(m2 is not None, f"{name}: Regex matches newline '{speaker}: \"...\"'")

                test_msg3 = f'\n  {speaker} : "Indented dialogue."'
                m3 = regex.search(test_msg3)
                assert_true(m3 is not None, f"{name}: Regex matches indented newline '  {speaker} : \"...\"'")

            # Negative test: in-sentence mention should NOT trigger avatar regex
            for neg_sentence in spec["negative_test_sentences"]:
                m_neg = regex.search(neg_sentence)
                assert_true(m_neg is None, f"{name}: Regex does NOT false-positive on sentence: '{neg_sentence}'")

        except Exception as e:
            assert_true(False, f"{name}: Regex compilation or evaluation failed with error {e}")

        # 6. Anti-umbrella keywords
        keys = set(k.lower() for k in entry.get("keys", []))
        overlap = keys.intersection(umbrella_keywords)
        assert_true(len(overlap) == 0, f"{name}: Zero umbrella keywords in keys (overlap: {overlap})")

        # 7. No raw {{age}} macros in description
        assert_true("{{age}}" not in desc, f"{name}: Zero raw '{{{{age}}}}' macros in description")

        # 8. Formatting discipline: No em-dashes in description
        assert_true("—" not in desc, f"{name}: Zero em-dashes in description")

    # ---------------------------------------------------------
    # 2. LOCAL OPTIMIZED MIRROR AUDIT
    # ---------------------------------------------------------
    mirror_path = "lorebooks/optimized/Svartulfr_NPC_Primary.json"
    assert_true(os.path.exists(mirror_path), f"Optimized mirror {mirror_path} exists")
    with open(mirror_path, "r", encoding="utf-8") as f:
        mirror_data = json.load(f)
    assert_true(mirror_data == primary_data, "FINAL and lorebooks/optimized Primary files are 100% identical")

    # ---------------------------------------------------------
    # 3. LIVE WYVERN API LOREBOOK PRIMARY AUDIT
    # ---------------------------------------------------------
    print("\n--- Testing Live Wyvern API Lorebook Primary (_zwEqgEEzh12X6gHVmMKKC) ---")
    token_path = "scratch/wyvern_token.txt"
    token = open(token_path, "r", encoding="utf-8").read().strip()
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "ChallengerBot/1.0"
    }

    lorebook_id = "_zwEqgEEzh12X6gHVmMKKC"
    api_url = f"https://app.wyvern.chat/api/lorebooks/{lorebook_id}"
    req = urllib.request.Request(api_url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            assert_true(resp.status == 200, f"GET {api_url} returned HTTP {resp.status}")
            live_lorebook = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        assert_true(False, f"Live API GET for lorebook {lorebook_id} failed: {e}")
        live_lorebook = {}

    live_lorebook_obj = live_lorebook.get("lorebook", live_lorebook)
    live_entries = live_lorebook_obj.get("lexicon", live_lorebook_obj.get("entries", []))
    assert_true(len(live_entries) == 99, f"Live Lorebook lexicon count is 99 (actual: {len(live_entries)})")
    
    live_entries_by_id = {get_id(e): e for e in live_entries if get_id(e)}
    for name, spec in target_specs.items():
        entry_id = spec["id"]
        assert_true(entry_id in live_entries_by_id, f"Live API contains {name} (id: {entry_id})")
        live_entry = live_entries_by_id.get(entry_id, {})
        local_entry = entries_by_id.get(entry_id, {})

        live_desc = get_text(live_entry)
        assert_true(len(live_desc) > 2000, f"Live {name}: description length > 2000 (actual: {len(live_desc)})")
        assert_true(live_desc == get_text(local_entry), f"Live {name}: description exactly matches local description")
        assert_true(live_entry.get("avatar_activation_regex") == local_entry.get("avatar_activation_regex"), f"Live {name}: avatar_activation_regex matches local")
        assert_true(live_entry.get("ignored_characters") == local_entry.get("ignored_characters"), f"Live {name}: ignored_characters matches local")
        assert_true(live_entry.get("ignored_personas") == local_entry.get("ignored_personas"), f"Live {name}: ignored_personas matches local")

    # ---------------------------------------------------------
    # 4. CHARACTER CARDS PARITY (LOCAL VS LIVE API)
    # ---------------------------------------------------------
    print("\n--- Testing Character Cards Parity (Wyvern /characters/mine vs Local) ---")
    cards_url = "https://app.wyvern.chat/api/characters/mine"
    req_cards = urllib.request.Request(cards_url, headers=headers)
    try:
        with urllib.request.urlopen(req_cards, timeout=15) as resp:
            assert_true(resp.status == 200, f"GET {cards_url} returned HTTP {resp.status}")
            mine_data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        assert_true(False, f"GET {cards_url} failed: {e}")
        mine_data = {}

    live_chars = mine_data.get("characters", [])
    assert_true(len(live_chars) == 8, f"Wyvern /characters/mine returns exactly 8 characters (actual: {len(live_chars)})")

    approved_card_ids = {
        "_t4J9aQNJM36cUKAP4wB4U": "Jasper Svartr Douglas Bloodmoon",
        "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
        "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Dominic Járn Douglas",
        "_RDfz7XzTpM23LpPALVXHM": "Malachia Björn Douglas Bloodmoon",
        "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
        "_TbRM3EdxDjHFgqztTbCpL": "Edric Douglas",
        "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Báleygr Bloodmoon",
        "_zn24784jfcchQ7EwCyAnm": "Mackenzie Sanchez-Rogers"
    }

    live_char_ids = {c.get("id"): c.get("name") for c in live_chars}
    assert_true(set(live_char_ids.keys()) == set(approved_card_ids.keys()), f"Live card IDs match exactly approved 8 card IDs (actual: {list(live_char_ids.keys())})")

    # Check Jared Thompson deleted (HTTP 404)
    jared_card_id = "_xJVPtBLL3dxy69RLKL9X9"
    jared_url = f"https://app.wyvern.chat/api/characters/{jared_card_id}"
    req_jared = urllib.request.Request(jared_url, headers=headers)
    try:
        with urllib.request.urlopen(req_jared, timeout=15) as resp:
            assert_true(False, f"Jared Thompson card {jared_card_id} should be deleted, but returned status {resp.status}")
    except urllib.error.HTTPError as e:
        assert_true(e.code == 404, f"Jared Thompson card {jared_card_id} is deleted on live API (HTTP {e.code})")
    except Exception as e:
        assert_true(False, f"Unexpected error checking Jared card: {e}")

    # Local FINAL/ cards check
    final_cards = [f for f in os.listdir("FINAL") if f.endswith("_card.json")]
    assert_true(len(final_cards) == 8, f"FINAL/ contains exactly 8 card JSON files (actual: {len(final_cards)}: {final_cards})")
    
    local_final_ids = {}
    for fc in final_cards:
        with open(os.path.join("FINAL", fc), "r", encoding="utf-8") as f:
            cdata = json.load(f)
            local_final_ids[cdata.get("id")] = cdata.get("name")

    assert_true(set(local_final_ids.keys()) == set(approved_card_ids.keys()), f"FINAL/ 8 card IDs match exactly the 8 approved cards")

    # Local ARCHIVIO/cards_legacy/ check
    legacy_dir = "ARCHIVIO/cards_legacy"
    assert_true(os.path.isdir(legacy_dir), f"Directory {legacy_dir} exists")
    legacy_files = [f for f in os.listdir(legacy_dir) if f.endswith("_card.json")]
    assert_true(len(legacy_files) == 6, f"{legacy_dir} contains exactly 6 card files (actual: {len(legacy_files)}: {legacy_files})")

    expected_legacy_files = {
        "Alyssa_Douglas_Bloodmoon_card.json": "_6exg3yPfe2eCDK4hTftkh",
        "Jared_Thompson_card.json": "_xJVPtBLL3dxy69RLKL9X9",
        "Russ_card.json": "_wn6DkCcg3Xqa2Xpx9ttnT",
        "Scarlett_Rose_card.json": "_qXgBMbFYJfc84hbLHhe92",
        "Sierra_Cruz_card.json": "_pnrXbkWqcgmFAf3meRWFY",
        "Stan_Davies_Jr_card.json": "_Xd3NhKnRJByMTtdb6PjxJ"
    }

    assert_true(set(legacy_files) == set(expected_legacy_files.keys()), f"{legacy_dir} has expected filenames")

    for fname, exp_id in expected_legacy_files.items():
        fpath = os.path.join(legacy_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            ldata = json.load(f)
            assert_true(ldata.get("id") == exp_id, f"Legacy card {fname} has expected id {exp_id} (actual: {ldata.get('id')})")

    # ---------------------------------------------------------
    # 5. CHECK NATIVE SUPPRESSION ON APPROVED CARDS IN LOREBOOKS
    # ---------------------------------------------------------
    print("\n--- Testing Native Suppression on Approved Cards in Lorebooks ---")
    active_cards_primary = {
        "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
        "_RDfz7XzTpM23LpPALVXHM": "Malachia Björn Douglas Bloodmoon",
        "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
        "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Dominic Járn Douglas",
        "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Báleygr Bloodmoon",
        "_zn24784jfcchQ7EwCyAnm": "Mackenzie Sanchez-Rogers"
    }

    # In Primary, let's search for these entries and verify ignored_characters
    for card_id, cname in active_cards_primary.items():
        # Find matching entry in Primary
        matched = [e for e in entries if card_id in e.get("ignored_characters", [])]
        assert_true(len(matched) >= 1, f"Approved card {cname} ({card_id}) is configured in ignored_characters of at least one Primary entry")

    # In Secondary, check Edric
    secondary_path = "FINAL/Svartulfr_NPC_Secondary.json"
    with open(secondary_path, "r", encoding="utf-8") as f:
        sec_data = json.load(f)
    sec_entries = sec_data.get("entries", [])
    edric_matched = [e for e in sec_entries if "_TbRM3EdxDjHFgqztTbCpL" in e.get("ignored_characters", [])]
    assert_true(len(edric_matched) >= 1, f"Approved card Edric Douglas (_TbRM3EdxDjHFgqztTbCpL) is configured in ignored_characters in Secondary lorebook")

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------
    print("\n======================================================================")
    print(f"AUDIT COMPLETE: {len(passes)} PASSED, {len(failures)} FAILED")
    print("======================================================================")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f" - {f}")
        return False
    else:
        print("\nALL EMPIRICAL TESTS PASSED PERFECTLY!")
        return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
