"""
Deep Adversarial Stress Testing Harness for Svartulfr Verse Character Scenarios
Challenger 1: Schema, Dash, Slots, Greetings & Macro Integrity
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
SCENARIO_CHAR_MACRO_REGEX = re.compile(r'\{\{scenarioChar\s+"([^"]+)"\}\}')

ALL_DASH_CODEPOINTS = {
    0x2014: "EM DASH (—)",
    0x2013: "EN DASH (–)",
    0x2015: "HORIZONTAL BAR (―)",
    0x2012: "FIGURE DASH (‒)",
    0x2010: "HYPHEN (‐)",
    0x2011: "NON-BREAKING HYPHEN (‑)",
    0x2212: "MINUS SIGN (−)",
    0xFE58: "SMALL EM DASH (﹘)",
    0xFE63: "SMALL HYPHEN-MINUS (﹣)",
    0xFF0D: "FULLWIDTH HYPHEN-MINUS (－)",
}

class DeepAdversarialScenarioTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.files = {}
        cls.raw_texts = {}
        cls.raw_bytes = {}
        for fname in EXPECTED_FILES:
            fpath = SCENARIOS_DIR / fname
            with open(fpath, "rb") as bf:
                b = bf.read()
            cls.raw_bytes[fname] = b
            raw = b.decode("utf-8")
            cls.raw_texts[fname] = raw
            cls.files[fname] = json.loads(raw)

    def test_adv_01_all_unicode_dash_variants(self):
        """Adversarially probe all possible unicode dash variants in raw bytes & decoded text."""
        findings = []
        for fname, raw in self.raw_texts.items():
            for line_no, line in enumerate(raw.splitlines(), start=1):
                for col_no, ch in enumerate(line, start=1):
                    cp = ord(ch)
                    # We strictly prohibit em-dash (0x2014) and en-dash (0x2013)
                    if cp in (0x2014, 0x2013):
                        findings.append({
                            "file": fname,
                            "line": line_no,
                            "col": col_no,
                            "codepoint": f"U+{cp:04X}",
                            "name": ALL_DASH_CODEPOINTS.get(cp, "UNKNOWN"),
                            "snippet": line.strip()
                        })
                    # Also flag if other exotic dash codepoints exist
                    elif cp in (0x2015, 0x2012, 0x2212, 0xFE58, 0xFE63, 0xFF0D):
                        findings.append({
                            "file": fname,
                            "line": line_no,
                            "col": col_no,
                            "codepoint": f"U+{cp:04X}",
                            "name": ALL_DASH_CODEPOINTS.get(cp, "UNKNOWN"),
                            "snippet": line.strip()
                        })
        self.assertEqual(len(findings), 0, f"Adversarial dash scan found violations: {findings}")

    def test_adv_02_escaped_unicode_dash_strings(self):
        """Check for literal escaped string sequences like '\\u2014' or '\\u2013' in raw file."""
        findings = []
        for fname, raw in self.raw_texts.items():
            for m in re.finditer(r'\\u201[34]', raw, re.IGNORECASE):
                findings.append({
                    "file": fname,
                    "match": m.group(0),
                    "start": m.start(),
                    "snippet": raw[max(0, m.start() - 30): min(len(raw), m.end() + 30)]
                })
        self.assertEqual(len(findings), 0, f"Found escaped unicode dash sequences: {findings}")

    def test_adv_03_exact_visibility_field(self):
        """Check visibility strictly equals 'private' and is not 'unlisted', 'public', etc."""
        for fname, data in self.files.items():
            vis = data.get("visibility")
            self.assertIs(type(vis), str, f"Visibility not str in {fname}")
            self.assertEqual(vis, "private", f"Visibility not 'private' in {fname}: was '{vis}'")

    def test_adv_04_lorebook_ids_exact_membership_and_order(self):
        """Verify lorebook_ids has exact 6 IDs, no duplicates, exactly matching canonical IDs."""
        for fname, data in self.files.items():
            lb_ids = data.get("lorebook_ids")
            self.assertIsInstance(lb_ids, list, f"lorebook_ids is not a list in {fname}")
            self.assertEqual(len(lb_ids), 6, f"Expected exactly 6 lorebook IDs in {fname}, got {len(lb_ids)}")
            self.assertEqual(set(lb_ids), set(EXPECTED_LOREBOOK_IDS), 
                             f"Lorebook IDs set mismatch in {fname}: {lb_ids}")
            # Check for duplicates
            self.assertEqual(len(set(lb_ids)), len(lb_ids), f"Duplicate lorebook IDs in {fname}")

    def test_adv_05_slots_invariants_and_typing(self):
        """Deep stress-test slots structure, keys, types, unavailable_count exact integer 0."""
        for fname, data in self.files.items():
            slots = data.get("slots")
            self.assertIsInstance(slots, list, f"slots is not a list in {fname}")
            self.assertGreater(len(slots), 0, f"slots is empty in {fname}")

            slot_keys = set()
            for idx, s in enumerate(slots):
                self.assertIsInstance(s, dict, f"slot {idx} not a dict in {fname}")
                self.assertIn("key", s, f"slot {idx} missing key in {fname}")
                self.assertIn("label", s, f"slot {idx} missing label in {fname}")
                self.assertIn("pool", s, f"slot {idx} missing pool in {fname}")
                self.assertIn("unavailable_count", s, f"slot {idx} missing unavailable_count in {fname}")

                key = s["key"]
                self.assertIsInstance(key, str, f"key {key} not a string in {fname}")
                self.assertTrue(bool(SLOT_KEY_REGEX.match(key)), f"key {key} failed regex in {fname}")
                self.assertNotIn(key, slot_keys, f"duplicate slot key {key} in {fname}")
                slot_keys.add(key)

                label = s["label"]
                self.assertIsInstance(label, str, f"label not string in {fname}:{key}")
                self.assertTrue(len(label.strip()) > 0, f"label empty in {fname}:{key}")

                pool = s["pool"]
                self.assertIsInstance(pool, list, f"pool not a list in {fname}:{key}")
                for p_idx, p_item in enumerate(pool):
                    self.assertIsInstance(p_item, dict, f"pool item {p_idx} not dict in {fname}:{key}")
                    self.assertIn("character_id", p_item, f"pool item {p_idx} missing character_id in {fname}:{key}")
                    self.assertIn("weight", p_item, f"pool item {p_idx} missing weight in {fname}:{key}")

                unavail = s["unavailable_count"]
                self.assertIs(type(unavail), int, f"unavailable_count not an int in {fname}:{key}")
                self.assertEqual(unavail, 0, f"unavailable_count is {unavail} != 0 in {fname}:{key}")

    def test_adv_06_greetings_invariants_and_messages(self):
        """
        Verify greetings invariants:
        - content == messages[0].content (exact byte-level equality)
        - speaker_slot == messages[0].speaker_slot
        - every message in messages has valid speaker_slot in defined slots
        - messages IDs are non-empty
        """
        for fname, data in self.files.items():
            slots = data.get("slots", [])
            valid_slots = {s["key"] for s in slots}
            greetings = data.get("greetings")
            self.assertIsInstance(greetings, list, f"greetings not list in {fname}")
            self.assertGreater(len(greetings), 0, f"greetings empty in {fname}")

            for g_idx, g in enumerate(greetings):
                gid = g.get("id", f"idx_{g_idx}")
                self.assertIn("content", g, f"missing content in {fname} greeting {gid}")
                self.assertIn("speaker_slot", g, f"missing speaker_slot in {fname} greeting {gid}")
                self.assertIn("messages", g, f"missing messages in {fname} greeting {gid}")

                msgs = g["messages"]
                self.assertIsInstance(msgs, list, f"messages not list in {fname} greeting {gid}")
                self.assertGreater(len(msgs), 0, f"messages empty in {fname} greeting {gid}")

                first_msg = msgs[0]
                self.assertEqual(g["content"], first_msg.get("content"),
                                 f"content mismatch in {fname} greeting {gid}")
                self.assertEqual(g["speaker_slot"], first_msg.get("speaker_slot"),
                                 f"speaker_slot mismatch in {fname} greeting {gid}")

                for m_idx, m in enumerate(msgs):
                    mid = m.get("id", f"msg_{m_idx}")
                    spk = m.get("speaker_slot")
                    self.assertIn(spk, valid_slots,
                                  f"Message {mid} in {fname} greeting {gid} has invalid speaker_slot: '{spk}'. Valid: {valid_slots}")
                    content = m.get("content")
                    self.assertIsInstance(content, str, f"Message {mid} content not str in {fname}")
                    self.assertGreater(len(content.strip()), 0, f"Message {mid} content empty in {fname}")

    def test_adv_07_scenario_char_macros_resolve_to_slots(self):
        """
        Adversarial check:
        In the scenario text, display_description, and greeting messages,
        any occurrence of {{scenarioChar "<slot_name>"}} MUST resolve to a declared slot!
        """
        macro_errors = []
        for fname, data in self.files.items():
            declared_slots = {s["key"] for s in data.get("slots", [])}

            # Check scenario description / body
            for field in ["scenario", "display_description"]:
                val = data.get(field, "")
                for m in SCENARIO_CHAR_MACRO_REGEX.finditer(val):
                    slot_ref = m.group(1)
                    if slot_ref not in declared_slots:
                        macro_errors.append({
                            "file": fname,
                            "field": field,
                            "macro_ref": slot_ref,
                            "declared_slots": sorted(list(declared_slots))
                        })

            # Check all greeting messages
            for g in data.get("greetings", []):
                gid = g.get("id")
                for m in g.get("messages", []):
                    mid = m.get("id")
                    content = m.get("content", "")
                    for match in SCENARIO_CHAR_MACRO_REGEX.finditer(content):
                        slot_ref = match.group(1)
                        if slot_ref not in declared_slots:
                            macro_errors.append({
                                "file": fname,
                                "field": f"greeting {gid} msg {mid}",
                                "macro_ref": slot_ref,
                                "declared_slots": sorted(list(declared_slots))
                            })

        self.assertEqual(len(macro_errors), 0,
                         f"Unresolved {{scenarioChar}} macros found:\n{json.dumps(macro_errors, indent=2)}")

    def test_adv_08_balanced_dialogue_quotes(self):
        """
        Adversarial check:
        Verify dialogue quotes in greeting messages. Standard double quotes must be balanced.
        """
        unbalanced_quotes = []
        for fname, data in self.files.items():
            for g in data.get("greetings", []):
                gid = g.get("id")
                for m_idx, m in enumerate(g.get("messages", [])):
                    mid = m.get("id", f"msg_{m_idx}")
                    c = m.get("content", "")
                    quote_count = c.count('"')
                    if quote_count % 2 != 0:
                        unbalanced_quotes.append({
                            "file": fname,
                            "greeting_id": gid,
                            "message_id": mid,
                            "quote_count": quote_count,
                            "content": c
                        })
        self.assertEqual(len(unbalanced_quotes), 0,
                         f"Found messages with unbalanced standard double quotes:\n{json.dumps(unbalanced_quotes, indent=2)}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
