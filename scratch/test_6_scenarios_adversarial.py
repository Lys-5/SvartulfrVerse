"""
test_6_scenarios_adversarial.py
Adversarial test suite verifying all 6 thematic scenario JSON files in FINAL/scenarios/.
"""

import json
import pathlib
import re

ROOT = pathlib.Path(r"e:\repository\SvartulfrVerse")
SCENARIOS_DIR = ROOT / "FINAL" / "scenarios"

LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

EXPECTED_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
]

def run_adversarial_tests():
    print("=== STARTING ADVERSARIAL VALIDATION SUITE ===")
    total_checks = 0
    failures = []

    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        total_checks += 1
        if not fpath.exists():
            failures.append(f"{fname} DOES NOT EXIST on disk!")
            continue

        raw_bytes = fpath.read_bytes()
        raw_text = raw_bytes.decode("utf-8")

        # Em-dash and en-dash adversarial scan
        total_checks += 1
        if "\u2014" in raw_text:
            failures.append(f"{fname}: Found em-dash (\\u2014) in file!")
        total_checks += 1
        if "\u2013" in raw_text:
            failures.append(f"{fname}: Found en-dash (\\u2013) in file!")

        data = json.loads(raw_text)

        # Invariant: visibility == "private"
        total_checks += 1
        if data.get("visibility") != "private":
            failures.append(f"{fname}: visibility is '{data.get('visibility')}', expected 'private'")

        # Invariant: rating == "explicit"
        total_checks += 1
        if data.get("rating") != "explicit":
            failures.append(f"{fname}: rating is '{data.get('rating')}', expected 'explicit'")

        # Invariant: all 6 lorebooks
        total_checks += 1
        if set(data.get("lorebook_ids", [])) != set(LOREBOOK_IDS) or len(data.get("lorebook_ids", [])) != 6:
            failures.append(f"{fname}: lorebook_ids mismatch: {data.get('lorebook_ids')}")

        # Invariant: slots
        slots = data.get("slots", [])
        total_checks += 1
        if not (1 <= len(slots) <= 20):
            failures.append(f"{fname}: slot count {len(slots)} not between 1 and 20")

        slot_keys = set()
        for s in slots:
            total_checks += 1
            k = s.get("key", "")
            if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$", k):
                failures.append(f"{fname}: invalid slot key format '{k}'")
            if k in slot_keys:
                failures.append(f"{fname}: duplicate slot key '{k}'")
            slot_keys.add(k)

            total_checks += 1
            if s.get("unavailable_count", 0) != 0:
                failures.append(f"{fname}: slot '{k}' has unavailable_count={s.get('unavailable_count')}, must be 0")

            pool = s.get("pool", [])
            for cand in pool:
                total_checks += 1
                if not cand.get("character_id"):
                    failures.append(f"{fname}: candidate missing character_id in slot '{k}'")
                if cand.get("weight") != 100:
                    failures.append(f"{fname}: candidate weight {cand.get('weight')} != 100 in slot '{k}'")

        # Invariant: greetings
        greetings = data.get("greetings", [])
        total_checks += 1
        if not (1 <= len(greetings) <= 100):
            failures.append(f"{fname}: greeting count {len(greetings)} outside [1, 100]")

        for g in greetings:
            gid = g.get("id")
            msgs = g.get("messages", [])
            total_checks += 1
            if not (1 <= len(msgs) <= 20):
                failures.append(f"{fname}: greeting '{gid}' message count {len(msgs)} outside [1, 20]")

            total_checks += 1
            if g.get("content") != msgs[0].get("content"):
                failures.append(f"{fname}: greeting '{gid}' content != messages[0].content")

            total_checks += 1
            if g.get("speaker_slot") != msgs[0].get("speaker_slot"):
                failures.append(f"{fname}: greeting '{gid}' speaker_slot != messages[0].speaker_slot")

            for m_idx, m in enumerate(msgs):
                total_checks += 1
                spk = m.get("speaker_slot")
                if spk not in slot_keys:
                    failures.append(f"{fname}: greeting '{gid}' msg {m_idx} speaker_slot '{spk}' not in slot keys: {slot_keys}")

                cnt = m.get("content", "")
                total_checks += 1
                if re.match(r"^[A-Z][a-zA-Z\s\.\-']{1,30}:\s*[\"']", cnt):
                    failures.append(f"{fname}: greeting '{gid}' msg {m_idx} contains redundant speaker name prefix: '{cnt[:25]}'")

                # Dialogue quotes check: if there is dialogue, ensure balanced standard double quotes
                quote_count = cnt.count('"')
                total_checks += 1
                if quote_count % 2 != 0:
                    failures.append(f"{fname}: greeting '{gid}' msg {m_idx} has unbalanced double quotes ({quote_count})")

        # Scenario-specific checks
        prompt = data.get("scenario", "")
        if fname == "Svartulfr_Scenario_Camp_Mystic.json":
            total_checks += 5
            assert len(slots) == 8
            assert len(greetings) == 4
            assert "Marcus Vale" in prompt and "Celeste Nadir" in prompt
            assert "Mara Voss" in prompt
            assert "13" in prompt
            assert data.get("startup_script")

        elif fname == "Svartulfr_Scenario_SUCC_Route_Alyssa.json":
            total_checks += 5
            assert len(slots) == 8
            assert len(greetings) == 6
            assert "Arctic Wolf demi-human" in prompt
            assert "Scarlett Rose" in prompt
            assert "Mackenzie" in prompt

        elif fname == "Svartulfr_Scenario_SUCC_Route_Jasper.json":
            total_checks += 5
            assert len(slots) == 8
            assert len(greetings) == 5
            assert "Russell" in prompt and "Sinclair" in prompt
            assert "Echo" in prompt
            assert "Wyrm Hall" in prompt

        elif fname == "Svartulfr_Scenario_Villa_Douglas.json":
            total_checks += 4
            assert len(slots) == 7
            assert len(greetings) == 5
            male_keys = {"father", "eldest_brother", "tech_brother", "politician_brother", "maternal_grandfather", "uncle", "cousin"}
            assert set(slot_keys) == male_keys
            for s in slots:
                assert len(s["pool"]) == 1

        elif fname == "Svartulfr_Scenario_DMHA_Dungeons.json":
            total_checks += 4
            assert len(slots) == 9
            assert len(greetings) == 4
            dmha_keys = {"twin_healer", "twin_tech", "eldest_brother", "demihuman_representative", "biker_enforcer", "raid_leader", "tank_frontline", "scout_infiltrator", "faction_support"}
            assert set(slot_keys) == dmha_keys

        elif fname == "Svartulfr_Scenario_Underworld_Sindacato.json":
            total_checks += 4
            assert len(slots) == 6
            assert len(greetings) == 4
            assert "Human, Telepath" in prompt
            uw_keys = {"syndicate_boss", "syndicate_fixer", "sinners_leader", "sinners_matriarch", "sinners_alchemist", "mercenary_tracker"}
            assert set(slot_keys) == uw_keys

        print(f"[OK] {fname}: all tests passed!")

    print(f"\nTotal checks executed: {total_checks}")
    print(f"Total failures: {len(failures)}")
    if failures:
        for f in failures:
            print("  FAIL:", f)
        raise AssertionError("Adversarial validation failed!")
    else:
        print("ALL ADVERSARIAL VALIDATION CHECKS PASSED 100%!")

if __name__ == "__main__":
    run_adversarial_tests()
