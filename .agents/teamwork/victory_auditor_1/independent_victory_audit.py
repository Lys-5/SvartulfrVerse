import os
import sys
import json
import requests
from pathlib import Path

ROOT = Path("e:/repository/SvartulfrVerse")
WORKSPACE = ROOT / ".agents/teamwork/victory_auditor_1"

CARDS_TO_CHECK = {
    "Edric Douglas": {
        "file": "FINAL/Edric_Douglas_card.json",
        "cid": "_TbRM3EdxDjHFgqztTbCpL",
        "lb_file": "FINAL/Svartulfr_NPC_Secondary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public",
        "gallery_tag": "edric"
    },
    "Erik Ulfr Douglas": {
        "file": "FINAL/Erik_Douglas_card.json",
        "cid": "_QPea6g4Q1QfeYCVHCLMPR",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public",
        "gallery_tag": "erikMain"
    },
    "Jasper Svartr Douglas Bloodmoon": {
        "file": "FINAL/Jasper_Douglas_Bloodmoon_card.json",
        "cid": "_t4J9aQNJM36cUKAP4wB4U",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public",
        "gallery_tag": "jasperMain"
    },
    "Logan Járn Douglas": {
        "file": "FINAL/Logan_Douglas_card.json",
        "cid": "_T8Ywcr9FEqNf9JxbK6eHP",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public",
        "gallery_tag": "loganMain"
    },
    "Mackenzie Sanchez-Rogers": {
        "file": "FINAL/Mackenzie_Sanchez_Rogers_card.json",
        "cid": "_zn24784jfcchQ7EwCyAnm",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public",
        "gallery_tag": "macSanchez"
    },
    "Malachia Björn Douglas Bloodmoon": {
        "file": "FINAL/Malachia_Douglas_Bloodmoon_card.json",
        "cid": "_RDfz7XzTpM23LpPALVXHM",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public",
        "gallery_tag": "mailMain"
    },
    "Noah Loki Douglas Bloodmoon": {
        "file": "FINAL/Noah_Douglas_Bloodmoon_card.json",
        "cid": "_zFLUjV8aVxQRAfQxGcAcY",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public",
        "gallery_tag": "noahMain"
    },
    "Wulfnic Bóleygr Bloodmoon": {
        "file": "FINAL/Wulfnic_Bloodmoon_card.json",
        "cid": "_HEQQbbRFwKdG8QE2Fh1z1",
        "lb_file": "FINAL/Svartulfr_NPC_Primary.json",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public",
        "gallery_tag": "mainWulfnic"
    }
}

ALL_6_LOREBOOKS = [
    "Svartulfr_Lorebook_I.json",
    "Svartulfr_Lorebook_II.json",
    "Svartulfr_Lorebook_III.json",
    "Svartulfr_Location.json",
    "Svartulfr_NPC_Primary.json",
    "Svartulfr_NPC_Secondary.json"
]

def run_audit():
    print("=" * 80)
    print("STARTING INDEPENDENT VICTORY AUDIT")
    print("=" * 80)
    
    # 1. Local Cards & Lorebooks Parity
    print("\n--- 1. AUDITING LOCAL CARDS & LOREBOOKS PARITY ---")
    local_cards_data = {}
    for name, meta in CARDS_TO_CHECK.items():
        card_p = ROOT / meta["file"]
        assert card_p.exists(), f"Card file {card_p} does not exist!"
        with open(card_p, "r", encoding="utf-8") as f:
            card_json = json.load(f)
        local_cards_data[name] = card_json
        
        # Verify avatar
        card_avatar = card_json.get("avatar")
        assert card_avatar == meta["expected_avatar"], (
            f"Avatar mismatch for {name}! Found: {card_avatar}, Expected: {meta['expected_avatar']}"
        )
        print(f"[PASS] Local Card {name:32} avatar: {card_avatar} (matches expected)")
        
        # Verify Lorebook entry
        lb_p = ROOT / meta["lb_file"]
        with open(lb_p, "r", encoding="utf-8") as f:
            lb_json = json.load(f)
        
        found = None
        for entry in lb_json.get("lexicon", []):
            if meta["cid"] in entry.get("ignored_characters", []):
                found = entry
                break
            if entry.get("name") == name:
                found = entry
                break
        
        assert found is not None, f"Could not find Lorebook entry for {name} in {meta['lb_file']}"
        assert found.get("avatar") == meta["expected_avatar"], (
            f"Lorebook avatar mismatch for {name}! Found: {found.get('avatar')}, Expected: {meta['expected_avatar']}"
        )
        assert meta["cid"] in found.get("ignored_characters", []), (
            f"Card ID {meta['cid']} missing from ignored_characters of {name} in {meta['lb_file']}"
        )
        
        # 1:1 byte-for-byte description check
        card_desc = card_json.get("description", "")
        entry_content = found.get("content", "")
        assert card_desc == entry_content, (
            f"1:1 Textual parity mismatch for {name}! Diff len: {len(entry_content) - len(card_desc)}"
        )
        print(f"[PASS] Local Parity {name:28} -> Text 1:1 (len {len(card_desc)}), Avatar 1:1, ignored_characters: {found.get('ignored_characters')}")

    # 2. Mirror & Zod Parity Across All 6 Lorebooks
    print("\n--- 2. AUDITING MIRROR & ZOD PARITY (ALL 6 LOREBOOKS) ---")
    for lb_name in ALL_6_LOREBOOKS:
        final_p = ROOT / "FINAL" / lb_name
        opt_p = ROOT / "lorebooks/optimized" / lb_name
        assert final_p.exists(), f"FINAL/{lb_name} missing"
        assert opt_p.exists(), f"lorebooks/optimized/{lb_name} missing"
        
        with open(final_p, "rb") as f:
            final_bytes = f.read()
        with open(opt_p, "rb") as f:
            opt_bytes = f.read()
        assert final_bytes == opt_bytes, f"Byte-for-byte mismatch between FINAL and optimized for {lb_name}!"
        
        final_data = json.loads(final_bytes.decode("utf-8"))
        entries = final_data.get("entries", [])
        lexicon = final_data.get("lexicon", [])
        assert len(entries) == len(lexicon), f"entries vs lexicon length mismatch in {lb_name}: {len(entries)} != {len(lexicon)}"
        assert entries == lexicon, f"entries != lexicon semantic content mismatch in {lb_name}!"
        print(f"[PASS] {lb_name:30} -> Mirror byte-for-byte 1:1, Entries == Lexicon ({len(entries)} entries)")

    # 3. Lorebook I & II Memory Entries Active Check
    print("\n--- 3. AUDITING MEMORY ENTRIES IN LOREBOOK I & II ---")
    for lb_name in ["Svartulfr_Lorebook_I.json", "Svartulfr_Lorebook_II.json"]:
        with open(ROOT / "FINAL" / lb_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        memories = [e for e in data.get("lexicon", []) if e.get("type") == "memory"]
        assert len(memories) > 0, f"No memory entries found in {lb_name}!"
        for m in memories:
            assert m.get("ignored_characters", []) == [], (
                f"Memory entry {m.get('name')} in {lb_name} has non-empty ignored_characters: {m.get('ignored_characters')}"
            )
            # Memory entries must not be disabled
            assert m.get("status") != "disabled", f"Memory entry {m.get('name')} is disabled!"
        print(f"[PASS] {lb_name:28} -> {len(memories)} active memory entries, all ignored_characters == []")

    # 4. Wyvern Live Web API Audit
    print("\n--- 4. AUDITING WYVERN LIVE WEB API ---")
    with open(ROOT / "scratch/wyvern_token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()
    headers = {"Authorization": f"Bearer {token}", "User-Agent": "VictoryAuditor/1.0"}
    
    # 4.1 Check characters/mine
    res_mine = requests.get("https://app.wyvern.chat/api/characters/mine", headers=headers)
    assert res_mine.status_code == 200, f"GET /api/characters/mine failed with {res_mine.status_code}: {res_mine.text}"
    live_chars_list = res_mine.json().get("characters", [])
    assert len(live_chars_list) == 8, f"Expected exactly 8 active characters in /api/characters/mine, found {len(live_chars_list)}"
    print(f"[PASS] GET /api/characters/mine: HTTP 200, exactly 8 active characters.")
    
    live_chars_map = {c["id"]: c for c in live_chars_list}
    for name, meta in CARDS_TO_CHECK.items():
        cid = meta["cid"]
        assert cid in live_chars_map, f"Character ID {cid} ({name}) not found in live /api/characters/mine!"
        live_c = live_chars_map[cid]
        
        # Verify live avatar
        assert live_c.get("avatar") == meta["expected_avatar"], (
            f"Live avatar mismatch for {name}! Found: {live_c.get('avatar')}, Expected: {meta['expected_avatar']}"
        )
        
        # Verify live description matches local card 1:1 byte-for-byte
        local_c = local_cards_data[name]
        assert live_c.get("description") == local_c.get("description"), (
            f"Live description mismatch for {name}! Lengths: live={len(live_c.get('description', ''))}, local={len(local_c.get('description', ''))}"
        )
        print(f"[PASS] Live Card {name:28} -> Avatar 1:1, Description 1:1 ({len(live_c.get('description', ''))} chars)")

    # 4.2 Check Live Lorebooks (Primary and Secondary)
    res_prim = requests.get("https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC", headers=headers)
    assert res_prim.status_code == 200, f"GET Primary Lorebook failed: {res_prim.status_code}"
    prim_live = res_prim.json()
    assert len(prim_live.get("lexicon", [])) == 99, f"Expected 99 entries in live Primary Lorebook, found {len(prim_live.get('lexicon', []))}"
    
    res_sec = requests.get("https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV", headers=headers)
    assert res_sec.status_code == 200, f"GET Secondary Lorebook failed: {res_sec.status_code}"
    sec_live = res_sec.json()
    assert len(sec_live.get("lexicon", [])) == 211, f"Expected 211 entries in live Secondary Lorebook, found {len(sec_live.get('lexicon', []))}"
    print(f"[PASS] Live Lorebooks: Primary (99 entries), Secondary (211 entries) both HTTP 200.")
    
    # 4.3 Check Live Gallery for Primary Lorebook
    res_gal = requests.get("https://app.wyvern.chat/api/gallery/lorebook/_zwEqgEEzh12X6gHVmMKKC", headers=headers)
    assert res_gal.status_code == 200, f"GET Primary Gallery failed: {res_gal.status_code}"
    gallery_items = res_gal.json()
    if isinstance(gallery_items, dict):
        gallery_items = gallery_items.get("gallery", [])
    
    gallery_url_set = {item.get("imageURL") for item in gallery_items if item.get("imageURL")}
    print(f"[PASS] Live Gallery contains {len(gallery_url_set)} asset URLs.")
    
    for name in ["Erik Ulfr Douglas", "Logan Járn Douglas", "Malachia Björn Douglas Bloodmoon", "Noah Loki Douglas Bloodmoon", "Wulfnic Bóleygr Bloodmoon"]:
        expected_url = CARDS_TO_CHECK[name]["expected_avatar"]
        assert expected_url in gallery_url_set, f"Expected gallery URL {expected_url} for {name} not found in live Gallery!"
        print(f"[PASS] Gallery Asset confirmed for {name:32} -> {expected_url}")

    print("\n" + "=" * 80)
    print("ALL INDEPENDENT VICTORY AUDIT CHECKS PASSED 100%!")
    print("=" * 80)

if __name__ == "__main__":
    try:
        run_audit()
    except AssertionError as e:
        print(f"\n[VICTORY AUDIT REJECTED] Assertion failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[VICTORY AUDIT REJECTED] Unexpected error: {e}")
        sys.exit(1)
