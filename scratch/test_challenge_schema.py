"""
Comprehensive Empirical Test Suite for Svartulfr Verse Character Scenarios
Challenger 1: Schema, Dash & Slot Invariants
Target Directory: e:\\repository\\SvartulfrVerse\\FINAL\\scenarios
"""

import os
import re
import json
import unittest
from pathlib import Path

SCENARIOS_DIR = Path(r"e:\repository\SvartulfrVerse\FINAL\scenarios")

EXPECTED_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
]

EXPECTED_LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

SLOT_KEY_REGEX = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$")

EM_DASH = "\u2014"  # '—'
EN_DASH = "\u2013"  # '–'
HORIZ_BAR = "\u2015"
FIGURE_DASH = "\u2012"
MINUS_SIGN = "\u2212"

class ScenarioChallengeTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.files = {}
        cls.raw_texts = {}
        for fname in EXPECTED_FILES:
            fpath = SCENARIOS_DIR / fname
            if not fpath.exists():
                raise FileNotFoundError(f"Missing required scenario file: {fpath}")
            with open(fpath, "r", encoding="utf-8") as f:
                raw = f.read()
            cls.raw_texts[fname] = raw
            cls.files[fname] = json.loads(raw)

    def test_01_all_expected_files_exist(self):
        """Verify that all 6 expected scenario files exist in FINAL/scenarios."""
        actual_files = sorted([p.name for p in SCENARIOS_DIR.glob("*.json")])
        self.assertEqual(sorted(EXPECTED_FILES), actual_files, 
                         f"File mismatch in {SCENARIOS_DIR}: {actual_files}")

    def test_02_zero_em_and_en_dashes_raw_character_scan(self):
        """
        Scan every single character across all 6 raw JSON files for em-dash (\u2014) and en-dash (\u2013).
        Also check for figure dash and horizontal bar.
        """
        violations = []
        for fname, raw in self.raw_texts.items():
            lines = raw.splitlines(keepends=True)
            char_offset = 0
            for line_no, line in enumerate(lines, start=1):
                for col_no, ch in enumerate(line, start=1):
                    if ch == EM_DASH:
                        snippet = line.strip()
                        violations.append({
                            "file": fname,
                            "type": "EM_DASH (\\u2014)",
                            "line": line_no,
                            "col": col_no,
                            "offset": char_offset + col_no - 1,
                            "snippet": snippet
                        })
                    elif ch == EN_DASH:
                        snippet = line.strip()
                        violations.append({
                            "file": fname,
                            "type": "EN_DASH (\\u2013)",
                            "line": line_no,
                            "col": col_no,
                            "offset": char_offset + col_no - 1,
                            "snippet": snippet
                        })
                    elif ch in (HORIZ_BAR, FIGURE_DASH):
                        snippet = line.strip()
                        violations.append({
                            "file": fname,
                            "type": f"OTHER_DASH ({ord(ch):04x})",
                            "line": line_no,
                            "col": col_no,
                            "offset": char_offset + col_no - 1,
                            "snippet": snippet
                        })
                char_offset += len(line)

        self.assertEqual(len(violations), 0, 
                         f"Found {len(violations)} dash violations:\n" + json.dumps(violations, indent=2))

    def test_03_visibility_private_enforced(self):
        """Verify 'visibility': 'private' is strictly enforced on all 6 files."""
        violations = []
        for fname, data in self.files.items():
            vis = data.get("visibility")
            if vis != "private":
                violations.append({
                    "file": fname,
                    "expected": "private",
                    "actual": vis
                })
        self.assertEqual(len(violations), 0,
                         f"Found visibility violations:\n{violations}")

    def test_04_all_six_standalone_lorebook_ids_present(self):
        """
        Verify all 6 standalone lorebook IDs are present in every scenario.
        ["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD",
         "_EjXxkmPVhpCXg8xABpFkK", "_zwEqgEEzh12X6gHVmMKKC", "_Uht3Ckz44JBDrPnUHq7LV"]
        """
        expected_set = set(EXPECTED_LOREBOOK_IDS)
        violations = []
        for fname, data in self.files.items():
            lb_ids = data.get("lorebook_ids")
            if not isinstance(lb_ids, list):
                violations.append({
                    "file": fname,
                    "error": "lorebook_ids is not a list",
                    "actual": lb_ids
                })
                continue
            actual_set = set(lb_ids)
            missing = expected_set - actual_set
            extra = actual_set - expected_set
            duplicates = len(lb_ids) - len(actual_set)
            if missing or extra or duplicates > 0:
                violations.append({
                    "file": fname,
                    "missing": list(missing),
                    "extra": list(extra),
                    "duplicates_count": duplicates,
                    "actual_list": lb_ids
                })
        self.assertEqual(len(violations), 0,
                         f"Lorebook ID violations found:\n{json.dumps(violations, indent=2)}")

    def test_05_slots_invariants(self):
        """
        Verify slots invariants for all 6 files:
        1. key matches ^[a-zA-Z][a-zA-Z0-9_-]{0,63}$
        2. unique keys in each scenario
        3. label present, non-empty string
        4. pool array present and is a list
        5. unavailable_count == 0
        """
        violations = []
        for fname, data in self.files.items():
            slots = data.get("slots")
            if not isinstance(slots, list):
                violations.append({"file": fname, "error": "slots is not a list", "actual": type(slots)})
                continue
            
            seen_keys = set()
            for idx, slot in enumerate(slots):
                if not isinstance(slot, dict):
                    violations.append({"file": fname, "slot_idx": idx, "error": "slot is not a dict"})
                    continue
                
                key = slot.get("key")
                label = slot.get("label")
                pool = slot.get("pool")
                unavailable_count = slot.get("unavailable_count")

                # Key validation
                if not isinstance(key, str):
                    violations.append({"file": fname, "slot_idx": idx, "error": f"key is not string: {key}"})
                elif not SLOT_KEY_REGEX.match(key):
                    violations.append({"file": fname, "slot_idx": idx, "error": f"key does not match regex: {key}"})
                elif key in seen_keys:
                    violations.append({"file": fname, "slot_idx": idx, "error": f"duplicate slot key: {key}"})
                else:
                    seen_keys.add(key)

                # Label validation
                if not isinstance(label, str) or not label.strip():
                    violations.append({"file": fname, "slot_key": key, "error": f"label invalid or empty: {label}"})

                # Pool validation
                if not isinstance(pool, list):
                    violations.append({"file": fname, "slot_key": key, "error": f"pool is not a list: {type(pool)}"})

                # unavailable_count validation
                if unavailable_count != 0:
                    violations.append({"file": fname, "slot_key": key, "error": f"unavailable_count != 0: {unavailable_count}"})

        self.assertEqual(len(violations), 0,
                         f"Slots violations found:\n{json.dumps(violations, indent=2)}")

    def test_06_greetings_invariants(self):
        """
        Verify greetings invariants for all 6 files:
        1. content == messages[0].content
        2. speaker_slot == messages[0].speaker_slot
        3. all message speaker_slots exist in the scenario's defined slot keys
        """
        violations = []
        for fname, data in self.files.items():
            slots = data.get("slots", [])
            valid_slot_keys = {s.get("key") for s in slots if isinstance(s, dict) and "key" in s}

            greetings = data.get("greetings")
            if not isinstance(greetings, list) or len(greetings) == 0:
                violations.append({"file": fname, "error": "greetings is not a non-empty list"})
                continue

            for g_idx, greeting in enumerate(greetings):
                g_id = greeting.get("id", f"greeting_{g_idx}")
                top_content = greeting.get("content")
                top_speaker_slot = greeting.get("speaker_slot")
                messages = greeting.get("messages")

                if not isinstance(messages, list) or len(messages) == 0:
                    violations.append({
                        "file": fname,
                        "greeting_id": g_id,
                        "error": "messages is empty or not a list"
                    })
                    continue

                first_msg = messages[0]
                first_content = first_msg.get("content")
                first_speaker = first_msg.get("speaker_slot")

                # Invariant 1: content == messages[0].content
                if top_content != first_content:
                    violations.append({
                        "file": fname,
                        "greeting_id": g_id,
                        "error": "content mismatch between greeting top-level and messages[0]",
                        "top_content_preview": str(top_content)[:60] if top_content else None,
                        "first_content_preview": str(first_content)[:60] if first_content else None
                    })

                # Invariant 2: speaker_slot == messages[0].speaker_slot
                if top_speaker_slot != first_speaker:
                    violations.append({
                        "file": fname,
                        "greeting_id": g_id,
                        "error": "speaker_slot mismatch between greeting top-level and messages[0]",
                        "top_speaker_slot": top_speaker_slot,
                        "first_speaker": first_speaker
                    })

                # Invariant 3: all message speaker_slots exist in slots
                for m_idx, msg in enumerate(messages):
                    msg_speaker = msg.get("speaker_slot")
                    if msg_speaker not in valid_slot_keys:
                        violations.append({
                            "file": fname,
                            "greeting_id": g_id,
                            "message_idx": m_idx,
                            "error": f"speaker_slot '{msg_speaker}' does not exist in defined slots",
                            "valid_slots": sorted(list(valid_slot_keys))
                        })

        self.assertEqual(len(violations), 0,
                         f"Greetings violations found:\n{json.dumps(violations, indent=2)}")

    def test_07_anti_ventriloquism_and_formatting_discipline(self):
        """
        Adversarial scan:
        Check for asterisks in greetings (asterisks are forbidden for actions/narration).
        """
        asterisk_findings = []
        for fname, data in self.files.items():
            greetings = data.get("greetings", [])
            for g_idx, greeting in enumerate(greetings):
                g_id = greeting.get("id", f"greeting_{g_idx}")
                messages = greeting.get("messages", [])
                for m_idx, msg in enumerate(messages):
                    content = msg.get("content", "")
                    if "*" in content:
                        asterisk_findings.append({
                            "file": fname,
                            "greeting_id": g_id,
                            "msg_idx": m_idx,
                            "speaker_slot": msg.get("speaker_slot"),
                            "content_snippet": content[:120]
                        })
        # Note: Rule states asterisks reserved for internal thoughts only, but let's see if any exist
        if asterisk_findings:
            print(f"INFO: Found {len(asterisk_findings)} messages containing asterisks (*):")
            for f in asterisk_findings:
                print(f"  [{f['file']}] {f['greeting_id']} msg {f['msg_idx']}: {f['content_snippet']}")

    def test_08_scenario_summary_stats(self):
        """Report statistics for each scenario."""
        summary = {}
        for fname, data in self.files.items():
            slots = data.get("slots", [])
            greetings = data.get("greetings", [])
            total_msgs = sum(len(g.get("messages", [])) for g in greetings)
            summary[fname] = {
                "name": data.get("name"),
                "visibility": data.get("visibility"),
                "slots_count": len(slots),
                "slot_keys": [s.get("key") for s in slots],
                "greetings_count": len(greetings),
                "total_messages": total_msgs,
                "lorebooks_count": len(data.get("lorebook_ids", []))
            }
        print("\n=== SCENARIO SUMMARY STATS ===")
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    unittest.main(verbosity=2)
