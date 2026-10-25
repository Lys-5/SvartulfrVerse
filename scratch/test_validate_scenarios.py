import json
import pathlib
import re
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
SCENARIOS_DIR = ROOT / 'FINAL' / 'scenarios'

EXPECTED_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
]

EXPECTED_LOREBOOKS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

VILLA_DOUGLAS_MALES = {
    "father": "_QPea6g4Q1QfeYCVHCLMPR",
    "eldest_brother": "_RDfz7XzTpM23LpPALVXHM",
    "tech_brother": "_t4J9aQNJM36cUKAP4wB4U",
    "politician_brother": "_zFLUjV8aVxQRAfQxGcAcY",
    "maternal_grandfather": "_HEQQbbRFwKdG8QE2Fh1z1",
    "uncle": "_T8Ywcr9FEqNf9JxbK6eHP",
    "cousin": "_TbRM3EdxDjHFgqztTbCpL",
}

DMHA_SLOTS = [
    "twin_healer",
    "twin_tech",
    "eldest_brother",
    "demihuman_representative",
    "biker_enforcer",
    "raid_leader",
    "tank_frontline",
    "scout_infiltrator",
    "faction_support"
]

def validate_all_scenarios():
    errors = []
    print("=== STARTING CHARACTER SCENARIOS VALIDATION SUITE ===")

    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        if not fpath.exists():
            errors.append(f"Missing required scenario file: {fname}")
            continue

        raw_text = fpath.read_text(encoding='utf-8')

        # 1. Em-dash and en-dash check on raw text
        if '—' in raw_text:
            errors.append(f"Em-dash ('—' \u2014) detected in {fname}")
        if '–' in raw_text:
            errors.append(f"En-dash ('–' \u2013) detected in {fname}")

        # 2. JSON validity
        try:
            sc = json.loads(raw_text)
        except Exception as e:
            errors.append(f"JSON parse error in {fname}: {e}")
            continue

        # 3. Visibility invariant
        vis = sc.get('visibility')
        if vis != 'private':
            errors.append(f"{fname}: 'visibility' must be 'private', got '{vis}'")

        # 4. Rating invariant
        if sc.get('rating') != 'explicit':
            errors.append(f"{fname}: 'rating' must be 'explicit', got '{sc.get('rating')}'")

        # 5. Lorebook IDs invariant
        l_ids = sc.get('lorebook_ids', [])
        if set(l_ids) != set(EXPECTED_LOREBOOKS):
            errors.append(f"{fname}: lorebook_ids mismatch. Expected {EXPECTED_LOREBOOKS}, got {l_ids}")

        # 6. Slots check
        slots = sc.get('slots', [])
        if not (1 <= len(slots) <= 20):
            errors.append(f"{fname}: slots count {len(slots)} not between 1 and 20")
        
        slot_keys = set()
        for idx, slot in enumerate(slots):
            key = slot.get('key')
            label = slot.get('label')
            pool = slot.get('pool')
            unavail = slot.get('unavailable_count')

            if not key or not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{0,63}$', key):
                errors.append(f"{fname} slot[{idx}] key '{key}' is invalid")
            if key in slot_keys:
                errors.append(f"{fname} duplicate slot key '{key}'")
            slot_keys.add(key)

            if not label or not (1 <= len(label) <= 120):
                errors.append(f"{fname} slot '{key}' label is invalid length")

            if not isinstance(pool, list):
                errors.append(f"{fname} slot '{key}' pool must be a list")

            if unavail != 0:
                errors.append(f"{fname} slot '{key}' unavailable_count must be 0, got {unavail}")

        # 7. Greetings check
        greetings = sc.get('greetings', [])
        if not (1 <= len(greetings) <= 100):
            errors.append(f"{fname}: greetings count {len(greetings)} not between 1 and 100")

        for g_idx, g in enumerate(greetings):
            g_name = g.get('name', '')
            g_desc = g.get('description', '')
            g_content = g.get('content', '')
            g_speaker = g.get('speaker_slot', '')
            messages = g.get('messages', [])

            if not (1 <= len(g_name) <= 200):
                errors.append(f"{fname} greeting[{g_idx}] name length invalid")
            if len(g_desc) > 10000:
                errors.append(f"{fname} greeting[{g_idx}] desc > 10000")
            if not messages or not (1 <= len(messages) <= 20):
                errors.append(f"{fname} greeting[{g_idx}] messages count {len(messages)} not 1-20")
                continue

            # Parity check
            first_msg = messages[0]
            if g_content != first_msg.get('content'):
                errors.append(f"{fname} greeting[{g_idx}] content does not match messages[0].content")
            if g_speaker != first_msg.get('speaker_slot'):
                errors.append(f"{fname} greeting[{g_idx}] speaker_slot does not match messages[0].speaker_slot")

            for m_idx, msg in enumerate(messages):
                m_slot = msg.get('speaker_slot')
                m_content = msg.get('content', '')

                if m_slot not in slot_keys:
                    errors.append(f"{fname} greeting[{g_idx}] msg[{m_idx}] speaker_slot '{m_slot}' not in slots")
                if len(m_content) > 100000:
                    errors.append(f"{fname} greeting[{g_idx}] msg[{m_idx}] content > 100k")

                # Dialogue formatting: Spoken dialogue inside double quotes. Plain text narration (no asterisks).
                # Check for illicit speaker prefixes inside content (e.g. "Santiago Herrera: ")
                if re.match(r'^[A-Z][a-zA-Z\s\'-]+:\s', m_content):
                    errors.append(f"{fname} greeting[{g_idx}] msg[{m_idx}] has hardcoded name prefix in content")

        # 8. Scenario specific checks
        if fname == "Svartulfr_Scenario_Camp_Mystic.json":
            startup = sc.get('startup_script', '')
            if not startup or 'Marcus Vale' not in startup or 'Celeste Nadir' not in startup:
                errors.append(f"Camp Mystic: startup_script missing Marcus Vale or Celeste Nadir resolution")
            if 'Mara Voss' not in sc.get('scenario', ''):
                errors.append("Camp Mystic: scenario text missing Mara Voss")
            if 'Lake Erie' not in raw_text:
                errors.append("Camp Mystic: missing Lake Erie reference")
            # Verify Edric 13yo
            if '13-year-old' not in sc.get('scenario', '') and 'Age 13' not in raw_text:
                errors.append("Camp Mystic: missing Edric 13yo reference")

        elif fname == "Svartulfr_Scenario_SUCC_Route_Alyssa.json":
            if 'Finnegan Novak' not in raw_text or 'Arctic Wolf' not in raw_text or 'demi-human' not in raw_text:
                errors.append("SUCC Alyssa: Finnegan Novak Arctic Wolf demi-human reference missing")
            if 'Scarlett Rose' not in raw_text:
                errors.append("SUCC Alyssa: Scarlett Rose surname missing")
            if len(greetings) < 6:
                errors.append(f"SUCC Alyssa: Expected 6 greetings, got {len(greetings)}")

        elif fname == "Svartulfr_Scenario_SUCC_Route_Jasper.json":
            if 'Russell \'Russ\' Sinclair' not in raw_text and 'Russ Sinclair' not in raw_text:
                errors.append("SUCC Jasper: Russ Sinclair surname missing")
            if 'Scarlett Rose' not in raw_text:
                errors.append("SUCC Jasper: Scarlett Rose surname missing")
            if 'Echo' not in raw_text:
                errors.append("SUCC Jasper: Echo AI companion missing")
            if 'Cocketeers' not in raw_text:
                errors.append("SUCC Jasper: Cocketeers reference missing")
            if len(greetings) < 5:
                errors.append(f"SUCC Jasper: Expected 5 greetings, got {len(greetings)}")

        elif fname == "Svartulfr_Scenario_Villa_Douglas.json":
            if len(slots) != 7:
                errors.append(f"Villa Douglas: Expected exactly 7 slots, got {len(slots)}")
            slot_map = {s['key']: s['pool'][0]['character_id'] for s in slots if s['pool']}
            for expected_key, expected_cid in VILLA_DOUGLAS_MALES.items():
                if expected_key not in slot_map:
                    errors.append(f"Villa Douglas: Missing required male slot '{expected_key}'")
                elif slot_map[expected_key] != expected_cid:
                    errors.append(f"Villa Douglas: Slot '{expected_key}' mapped to wrong card ID: {slot_map[expected_key]} vs {expected_cid}")
            if len(greetings) < 5:
                errors.append(f"Villa Douglas: Expected 5 greetings, got {len(greetings)}")

        elif fname == "Svartulfr_Scenario_DMHA_Dungeons.json":
            if len(slots) != 9:
                errors.append(f"DMHA: Expected 9 slots, got {len(slots)}")
            dmha_keys = [s['key'] for s in slots]
            if dmha_keys != DMHA_SLOTS:
                errors.append(f"DMHA slots mismatch: expected {DMHA_SLOTS}, got {dmha_keys}")
            if 'Radek' not in raw_text or 'Goran' not in raw_text or 'Kian' not in raw_text or 'Barrow' not in raw_text or 'Marek' not in raw_text:
                errors.append("DMHA: Missing Team Ukiyo or Nomads characters")

        elif fname == "Svartulfr_Scenario_Underworld_Sindacato.json":
            if len(slots) != 6:
                errors.append(f"Underworld: Expected 6 slots, got {len(slots)}")
            if 'Human Telepath' not in raw_text and 'Human, Telepath' not in raw_text:
                errors.append("Underworld: Jean-Luc Virtuoso Human Telepath specification missing")
            if 'Rory' not in raw_text or 'Sully' not in raw_text or 'Ambrosia' not in raw_text or 'Sinclair' not in raw_text:
                errors.append("Underworld: Missing Rory, Sully, Ambrosia, or Sinclair")

    print(f"\nVALIDATION SUMMARY:")
    print(f"Total files checked: {len(EXPECTED_FILES)}")
    print(f"Total errors: {len(errors)}")
    if errors:
        for e in errors:
            print(f"  [ERROR] {e}")
        return False
    else:
        print("  >>> ALL 6 CHARACTER SCENARIOS PASSED 100% OF SCHEMA, LORE, AND INVARIANT TESTS! <<<")
        return True

if __name__ == '__main__':
    ok = validate_all_scenarios()
    sys.exit(0 if ok else 1)
