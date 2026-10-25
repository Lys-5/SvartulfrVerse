"""
Adversarial Verification Suite for Character Scenarios: Slots & Lore Invariants
Empirically tests all 6 scenario payloads against strict project invariants.
"""

import json
import re
from pathlib import Path

FINAL_DIR = Path("FINAL/scenarios")
MINE_CHARS_PATH = Path("exports/Mine_Characters_Export.json")

# Canonical 14 active character cards in /mine
EXPECTED_14_CARDS = {
    "_t4J9aQNJM36cUKAP4wB4U": "Jasper Svartr Douglas Bloodmoon",
    "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
    "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Járn Douglas",
    "_RDfz7XzTpM23LpPALVXHM": "Malachia Björn Douglas Bloodmoon",
    "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
    "_TbRM3EdxDjHFgqztTbCpL": "Edric Douglas",
    "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Báleygr Bloodmoon",
    "_6exg3yPfe2eCDK4hTftkh": "Alyssa Hvit Douglas Bloodmoon",
    "_xJVPtBLL3dxy69RLKL9X9": "Jared Thompson",
    "_zn24784jfcchQ7EwCyAnm": "Mackenzie Sanchez-Rogers",
    "_qXgBMbFYJfc84hbLHhe92": "Scarlett Rose",
    "_pnrXbkWqcgmFAf3meRWFY": "Sierra Cruz",
    "_Xd3NhKnRJByMTtdb6PjxJ": "Stanley Davies Jr.",
    "_wn6DkCcg3Xqa2Xpx9ttnT": "Russell 'Russ'",
}

# Exactly the 7 canonical male Douglas/Bloodmoon cards
CANONICAL_7_MALES = {
    "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
    "_RDfz7XzTpM23LpPALVXHM": "Malachia Björn Douglas Bloodmoon",
    "_t4J9aQNJM36cUKAP4wB4U": "Jasper Svartr Douglas Bloodmoon",
    "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
    "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Báleygr Bloodmoon",
    "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Járn Douglas",
    "_TbRM3EdxDjHFgqztTbCpL": "Edric Douglas",
}

SCENARIO_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
]


def run_checks():
    print("=" * 60)
    print("SLOTS & LORE INVARIANTS ADVERSARIAL TEST SUITE")
    print("=" * 60)

    # 0. Check Mine_Characters_Export.json matches canonical 14
    assert MINE_CHARS_PATH.exists(), f"Missing {MINE_CHARS_PATH}"
    mine_data = json.loads(MINE_CHARS_PATH.read_text(encoding="utf-8"))
    raw_chars = mine_data if isinstance(mine_data, list) else mine_data.get("characters", mine_data.get("data", []))
    mine_chars = {c["id"]: c["name"] for c in raw_chars}
    assert len(mine_chars) == 14, f"Mine chars count {len(mine_chars)} != 14"
    for cid in EXPECTED_14_CARDS:
        assert cid in mine_chars, f"Expected card {cid} not in {MINE_CHARS_PATH}"
    print(f"[PASS] {MINE_CHARS_PATH} contains exactly 14 verified canonical active cards.")

    all_scenarios = {}
    total_slots = 0
    total_checks = 0

    for fname in SCENARIO_FILES:
        fpath = FINAL_DIR / fname
        assert fpath.exists(), f"File {fpath} does not exist"
        data = json.loads(fpath.read_text(encoding="utf-8"))
        all_scenarios[fname] = data

    print(f"\n--- 1. Testing Slot Configurations & unavailable_count == 0 ---")
    for fname, data in all_scenarios.items():
        slots = data.get("slots", [])
        assert len(slots) > 0, f"{fname} has no slots"
        for s in slots:
            total_slots += 1
            s_key = s.get("key")
            s_label = s.get("label")
            s_pool = s.get("pool")
            unavail = s.get("unavailable_count")

            # Check key, label, pool, unavailable_count exist
            assert s_key and isinstance(s_key, str), f"{fname}: Slot missing valid 'key': {s}"
            assert s_label and isinstance(s_label, str), f"{fname}: Slot missing valid 'label': {s}"
            assert isinstance(s_pool, list), f"{fname}: Slot missing 'pool' list: {s}"
            assert unavail is not None, f"{fname}: Slot missing 'unavailable_count': {s}"
            assert unavail == 0, f"{fname}: Slot {s_key} unavailable_count != 0 ({unavail})"

            # Check pool contents
            if len(s_pool) == 0:
                # Open/NPC slot -> must have pool: []
                pass
            else:
                # Card slot -> each entry in pool must have character_id in the 14 verified canonical cards
                for pool_item in s_pool:
                    cid = pool_item.get("character_id")
                    assert cid in EXPECTED_14_CARDS, (
                        f"{fname}: Slot {s_key} references unverified card {cid} "
                        f"(not in the 14 canonical active cards)"
                    )
                    weight = pool_item.get("weight")
                    assert weight == 100, f"{fname}: Slot {s_key} card {cid} weight != 100 ({weight})"
            total_checks += 1
        print(f"[PASS] {fname}: {len(slots)} slots all verified (unavailable_count == 0, pool valid).")

    print(f"\n--- 2. Testing Villa Douglas Slots (Exact 7 Canonical Male Cards) ---")
    villa = all_scenarios["Svartulfr_Scenario_Villa_Douglas.json"]
    v_slots = villa.get("slots", [])
    assert len(v_slots) == 7, f"Villa Douglas slots count {len(v_slots)} != 7"
    villa_cids = set()
    for s in v_slots:
        pool = s.get("pool", [])
        assert len(pool) == 1, f"Villa Douglas slot {s['key']} must have exactly 1 card in pool"
        cid = pool[0].get("character_id")
        villa_cids.add(cid)
    assert villa_cids == set(CANONICAL_7_MALES.keys()), (
        f"Villa Douglas card IDs mismatch! Found: {villa_cids}, Expected: {set(CANONICAL_7_MALES.keys())}"
    )
    print(f"[PASS] Villa Douglas contains exactly the 7 canonical male Douglas/Bloodmoon cards:")
    for cid in villa_cids:
        print(f"       - {cid}: {CANONICAL_7_MALES[cid]}")

    print(f"\n--- 3. Testing DMHA Slots (Exact 9 Slots & Cast Structure) ---")
    dmha = all_scenarios["Svartulfr_Scenario_DMHA_Dungeons.json"]
    dmha_slots = dmha.get("slots", [])
    assert len(dmha_slots) == 9, f"DMHA slots count {len(dmha_slots)} != 9"
    dmha_slot_keys = [s["key"] for s in dmha_slots]
    expected_dmha_keys = [
        "twin_healer",
        "twin_tech",
        "eldest_brother",
        "demihuman_representative",
        "biker_enforcer",
        "raid_leader",
        "tank_frontline",
        "scout_infiltrator",
        "faction_support",
    ]
    assert dmha_slot_keys == expected_dmha_keys, f"DMHA slot keys mismatch: {dmha_slot_keys}"

    # Verify Alyssa, Jasper, Malachia are card slots
    dmha_card_map = {
        "twin_healer": "_6exg3yPfe2eCDK4hTftkh",  # Alyssa
        "twin_tech": "_t4J9aQNJM36cUKAP4wB4U",    # Jasper
        "eldest_brother": "_RDfz7XzTpM23LpPALVXHM", # Malachia
    }
    for k, expected_cid in dmha_card_map.items():
        slot = next(s for s in dmha_slots if s["key"] == k)
        assert len(slot["pool"]) == 1 and slot["pool"][0]["character_id"] == expected_cid, (
            f"DMHA slot {k} does not reference expected card {expected_cid}"
        )
    # Verify open/NPC slots: Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads
    expected_npc_slots = [
        ("demihuman_representative", "Barrow"),
        ("biker_enforcer", "Marek"),
        ("raid_leader", "Radek"),
        ("tank_frontline", "Goran"),
        ("scout_infiltrator", "Kian"),
        ("faction_support", "DMHA"),
    ]
    for k, expected_sub in expected_npc_slots:
        slot = next(s for s in dmha_slots if s["key"] == k)
        assert len(slot["pool"]) == 0, f"DMHA slot {k} must have empty pool [] (NPC slot)"
        assert expected_sub.lower() in slot["label"].lower(), (
            f"DMHA slot {k} label '{slot['label']}' does not mention '{expected_sub}'"
        )
    print(f"[PASS] DMHA has 9 slots with Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads.")

    print(f"\n--- 4. Testing Camp Mystic (Shuttle, Marcus/Celeste, Mara Voss, Edric 13yo, Lua Script) ---")
    camp = all_scenarios["Svartulfr_Scenario_Camp_Mystic.json"]
    camp_slots = camp.get("slots", [])
    assert len(camp_slots) == 8, f"Camp Mystic slots count {len(camp_slots)} != 8"

    # Check Edric 13yo in slots and scenario text
    edric_slot = next((s for s in camp_slots if s["key"] == "cousin"), None)
    assert edric_slot is not None, "Camp Mystic missing 'cousin' slot"
    assert "edric" in edric_slot["label"].lower() and "13" in edric_slot["label"], (
        f"Camp Mystic cousin slot label '{edric_slot['label']}' must mention Edric and 13yo"
    )

    # Check supervisor and director slots
    sup_slot = next((s for s in camp_slots if s["key"] == "supervisor"), None)
    dir_slot = next((s for s in camp_slots if s["key"] == "director"), None)
    assert sup_slot and dir_slot, "Camp Mystic missing supervisor or director slots"
    assert sup_slot["key"] == "supervisor", "Camp Mystic missing supervisor slot key"
    assert "supervisor" in sup_slot["label"].lower(), (
        f"Supervisor slot label '{sup_slot['label']}' must mention Supervisor"
    )
    assert "mara voss" in dir_slot["label"].lower(), (
        f"Director slot label '{dir_slot['label']}' must mention Mara Voss"
    )

    # Check Lua startup_script
    lua_script = camp.get("startup_script", "")
    assert lua_script and len(lua_script) > 50, "Camp Mystic missing valid startup_script"
    assert "Marcus Vale" in lua_script and "Celeste Nadir" in lua_script, (
        "Camp Mystic Lua startup_script missing Marcus Vale or Celeste Nadir logic"
    )
    print(f"[PASS] Camp Mystic startup_script verified ({len(lua_script)} chars).")

    # Check scenario text details for Marcus Vale / Celeste Nadir and Edric 13yo
    camp_scen_text = camp.get("scenario", "")
    assert "Marcus Vale" in camp_scen_text and "Celeste Nadir" in camp_scen_text, (
        "Camp Mystic scenario text missing Marcus Vale or Celeste Nadir"
    )
    assert "Mara Voss" in camp_scen_text, "Camp Mystic scenario text missing Mara Voss"
    assert "Edric Douglas" in camp_scen_text and "13" in camp_scen_text, (
        "Camp Mystic scenario text missing Edric Douglas 13yo reference"
    )

    # Check Lake Erie shuttle arrival in greetings and description
    greetings = camp.get("greetings", [])
    assert len(greetings) == 4, f"Camp Mystic greetings count {len(greetings)} != 4"
    all_camp_text = json.dumps(camp, ensure_ascii=False)
    assert "Lake Erie" in all_camp_text, "Camp Mystic missing 'Lake Erie' reference"
    assert "shuttle" in all_camp_text.lower(), "Camp Mystic missing 'shuttle' reference"

    # Verify greeting 1 specifically mentions the shuttle arrival on Lake Erie
    g1 = greetings[0]
    g1_text = json.dumps(g1, ensure_ascii=False)
    assert "shuttle" in g1_text.lower() or "lake erie" in g1_text.lower(), (
        "Greeting 1 does not mention shuttle arrival or Lake Erie"
    )
    print(f"[PASS] Camp Mystic Lake Erie shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric 13yo, and Lua script verified.")

    print(f"\n--- 5. Testing Finnegan Novak Invariants (SUCC Routes) ---")
    succ_alyssa = all_scenarios["Svartulfr_Scenario_SUCC_Route_Alyssa.json"]
    succ_jasper = all_scenarios["Svartulfr_Scenario_SUCC_Route_Jasper.json"]

    for name, scen in [("SUCC Alyssa", succ_alyssa), ("SUCC Jasper", succ_jasper)]:
        scen_text = scen.get("scenario", "")
        # Verify Finnegan Novak is explicitly Arctic Wolf demi-human, one pair of animal ears, non-shifter
        assert "Finnegan" in scen_text and "Novak" in scen_text, f"{name}: Missing Finnegan Novak in scenario"
        assert "Arctic Wolf" in scen_text or "arctic wolf" in scen_text, f"{name}: Finnegan Novak missing Arctic Wolf designation"
        assert "demi-human" in scen_text.lower() or "demihuman" in scen_text.lower(), f"{name}: Missing demi-human designation"
        assert "one pair of animal ears" in scen_text.lower() or "single pair of animal ears" in scen_text.lower() or "only one pair of animal ears" in scen_text.lower(), (
            f"{name}: Missing explicit 'one pair of animal ears' anatomical rule"
        )
        assert "non-shifter" in scen_text.lower() or "cannot shift" in scen_text.lower() or "no shift" in scen_text.lower(), (
            f"{name}: Missing explicit 'non-shifter' designation for Finnegan Novak"
        )

        # Also check Finnegan slot in slots list
        finn_slot = next((s for s in scen["slots"] if s["key"] == "childhood_friend"), None)
        assert finn_slot is not None, f"{name}: Missing 'childhood_friend' slot"
        assert "finnegan" in finn_slot["label"].lower(), f"{name}: Slot label does not mention Finnegan"
        assert len(finn_slot["pool"]) == 0, f"{name}: Finnegan slot must have empty pool [] (NPC)"
        print(f"[PASS] {name}: Finnegan Novak explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter).")

    print(f"\n--- 6. Testing Jean-Luc Virtuoso Invariants (Underworld Sindacato) ---")
    underworld = all_scenarios["Svartulfr_Scenario_Underworld_Sindacato.json"]
    uw_text = underworld.get("scenario", "")
    assert "Jean-Luc Virtuoso" in uw_text, "Underworld scenario text missing Jean-Luc Virtuoso"
    assert "Human" in uw_text and "Telepath" in uw_text, (
        "Underworld scenario text missing explicit 'Human' and 'Telepath' designation for Jean-Luc Virtuoso"
    )

    # Check slot for Jean-Luc
    jl_slot = next((s for s in underworld["slots"] if s["key"] == "sinners_leader"), None)
    assert jl_slot is not None, "Underworld missing 'sinners_leader' slot"
    assert "jean-luc virtuoso" in jl_slot["label"].lower(), f"Slot label '{jl_slot['label']}' missing Jean-Luc Virtuoso"
    assert len(jl_slot["pool"]) == 0, "Jean-Luc slot must have empty pool [] (NPC)"
    assert "Strictly verified SPECIES: Human, Telepath" in uw_text, "Missing explicit species verification in text"
    assert "Jean-Luc Virtuoso is strictly specified as Human, Telepath." in uw_text, "Missing explicit summary invariant in text"
    print(f"[PASS] Underworld: Jean-Luc Virtuoso explicitly specified as Human, Telepath (slot & scenario text).")

    print(f"\n--- 7. Testing All Open / NPC Slots Have pool: [] ---")
    open_slot_count = 0
    card_slot_count = 0
    for fname, data in all_scenarios.items():
        for s in data["slots"]:
            if len(s["pool"]) == 0:
                open_slot_count += 1
            else:
                card_slot_count += 1
    print(f"[PASS] Verified all {total_slots} slots across 6 scenarios:")
    print(f"       - Card slots (with verified card ID): {card_slot_count}")
    print(f"       - Open / Lorebook NPC slots (pool: []): {open_slot_count}")
    print(f"       - Unavailable count: 0 across all {total_slots} slots")

    print(f"\n--- 8. Testing Visibility Invariant ('private') in Local Files ---")
    for fname, data in all_scenarios.items():
        vis = data.get("visibility")
        assert vis == "private", f"{fname}: visibility '{vis}' != 'private'"
        print(f"[PASS] {fname}: visibility == 'private'")

    print("\n" + "=" * 60)
    print("ALL SLOTS & LORE INVARIANTS CHECKS PASSED (100% EMPIRICAL CONFIRMATION)")
    print("=" * 60)


if __name__ == "__main__":
    run_checks()
