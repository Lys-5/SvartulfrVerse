"""
Challenger 1 Adversarial Test Suite: Formatting & Regex Verification
Target: 6 Character Scenario JSON files in FINAL/scenarios/

Covers:
1. Deep search for em-dash (\\u2014) and en-dash (\\u2013) across all keys and values in raw text & parsed JSON
2. Slot key regex validation: ^[a-zA-Z][a-zA-Z0-9_-]{0,63}$
3. Dialogue & narration formatting: spoken dialogue in standard quotes (\"...\"), plain text narration (no asterisks on narration, check internal thoughts usage)
4. Multi-message greeting parity: root content == messages[0].content, root speaker_slot == messages[0].speaker_slot
5. Redundant speaker name prefixes inside message content (e.g. 'Name: \"...\"')
"""

import json
import os
import re
import sys
import unittest
from pathlib import Path

SCENARIOS_DIR = Path(r"e:\repository\SvartulfrVerse\FINAL\scenarios")

SCENARIO_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
]

SLOT_KEY_REGEX = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}$")

# Disallowed dashes
EM_DASH = "\u2014"
EN_DASH = "\u2013"
DISALLOWED_DASHES = {
    "\u2014": "EM DASH (\\u2014)",
    "\u2013": "EN DASH (\\u2013)",
    "\u2015": "HORIZONTAL BAR (\\u2015)",
    "\u2012": "FIGURE DASH (\\u2012)",
    "\uFE58": "SMALL EM DASH (\\uFE58)",
    "\uFE63": "SMALL HYPHEN-MINUS (\\uFE63)",
    "\uFF0D": "FULLWIDTH HYPHEN-MINUS (\\uFF0D)",
}

class TestChallenger1FormattingAndRegex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.raw_data = {}
        cls.json_data = {}
        for fname in SCENARIO_FILES:
            fpath = SCENARIOS_DIR / fname
            if not fpath.exists():
                raise FileNotFoundError(f"File not found: {fpath}")
            raw = fpath.read_text(encoding="utf-8")
            cls.raw_data[fname] = raw
            cls.json_data[fname] = json.loads(raw)

    def test_01_deep_search_for_dashes_in_raw_text(self):
        """1a. Search raw file bytes/chars for any disallowed dash codepoints."""
        violations = []
        for fname, raw in self.raw_data.items():
            for line_no, line in enumerate(raw.splitlines(), start=1):
                for dash_char, dash_name in DISALLOWED_DASHES.items():
                    if dash_char in line:
                        col = line.find(dash_char) + 1
                        violations.append({
                            "file": fname,
                            "line": line_no,
                            "col": col,
                            "dash_name": dash_name,
                            "snippet": line.strip()[:100]
                        })
        self.assertEqual(len(violations), 0, f"Disallowed dashes found in raw text: {violations}")

    def test_02_deep_search_for_dashes_in_parsed_json(self):
        """1b. Recursively traverse all keys and values in parsed JSON for any disallowed dash."""
        violations = []

        def traverse(node, path, fname):
            if isinstance(node, dict):
                for k, v in node.items():
                    current_path = f"{path}.{k}"
                    for d_char, d_name in DISALLOWED_DASHES.items():
                        if d_char in k:
                            violations.append({"file": fname, "path": f"{current_path} (key)", "dash": d_name})
                    traverse(v, current_path, fname)
            elif isinstance(node, list):
                for idx, item in enumerate(node):
                    traverse(item, f"{path}[{idx}]", fname)
            elif isinstance(node, str):
                for d_char, d_name in DISALLOWED_DASHES.items():
                    if d_char in node:
                        violations.append({
                            "file": fname,
                            "path": path,
                            "dash": d_name,
                            "snippet": node[:80]
                        })

        for fname, data in self.json_data.items():
            traverse(data, "root", fname)

        self.assertEqual(len(violations), 0, f"Disallowed dashes found in parsed JSON structure: {violations}")

    def test_03_escaped_dash_sequences(self):
        """1c. Check for literal string representations of escaped dashes (e.g. '\\u2014')."""
        violations = []
        pattern = re.compile(r"\\u201[3452]|\\uFE58|\\uFE63|\\uFF0D", re.IGNORECASE)
        for fname, raw in self.raw_data.items():
            for m in pattern.finditer(raw):
                violations.append({
                    "file": fname,
                    "matched": m.group(0),
                    "pos": m.start(),
                    "context": raw[max(0, m.start() - 25): min(len(raw), m.end() + 25)]
                })
        self.assertEqual(len(violations), 0, f"Escaped dash patterns found: {violations}")

    def test_04_slot_keys_regex_validation(self):
        """2. Verify all slot keys match regex ^[a-zA-Z][a-zA-Z0-9_-]{0,63}$."""
        violations = []
        total_slots = 0
        for fname, data in self.json_data.items():
            slots = data.get("slots", [])
            self.assertIsInstance(slots, list, f"slots is not a list in {fname}")
            self.assertGreater(len(slots), 0, f"slots is empty in {fname}")
            seen_keys = set()
            for idx, s in enumerate(slots):
                total_slots += 1
                key = s.get("key")
                if not key or not isinstance(key, str):
                    violations.append({"file": fname, "slot_index": idx, "issue": f"missing/non-str key: {key}"})
                    continue
                if not SLOT_KEY_REGEX.match(key):
                    violations.append({"file": fname, "slot_index": idx, "key": key, "issue": "regex failure"})
                if key in seen_keys:
                    violations.append({"file": fname, "slot_index": idx, "key": key, "issue": "duplicate key"})
                seen_keys.add(key)

                # Check label and pool and unavailable_count
                if not s.get("label"):
                    violations.append({"file": fname, "key": key, "issue": "empty label"})
                if not isinstance(s.get("pool"), list):
                    violations.append({"file": fname, "key": key, "issue": "pool not list"})
                if s.get("unavailable_count") != 0:
                    violations.append({"file": fname, "key": key, "issue": f"unavailable_count={s.get('unavailable_count')}"})

        print(f"\n[Test 04] Total slots validated: {total_slots}")
        self.assertEqual(len(violations), 0, f"Slot key / schema violations found: {violations}")

    def test_05_greeting_multi_message_parity(self):
        """
        4. Multi-message greeting parity:
           - root content == messages[0].content
           - root speaker_slot == messages[0].speaker_slot
           - all speaker_slots in messages exist in slots
        """
        violations = []
        total_greetings = 0
        total_messages = 0

        for fname, data in self.json_data.items():
            declared_slots = {s["key"] for s in data.get("slots", [])}
            greetings = data.get("greetings", [])
            self.assertIsInstance(greetings, list, f"greetings not list in {fname}")
            self.assertGreater(len(greetings), 0, f"greetings empty in {fname}")

            for g_idx, g in enumerate(greetings):
                total_greetings += 1
                gid = g.get("id", f"idx_{g_idx}")
                root_content = g.get("content")
                root_speaker = g.get("speaker_slot")
                msgs = g.get("messages", [])

                if not isinstance(msgs, list) or len(msgs) == 0:
                    violations.append({"file": fname, "greeting_id": gid, "issue": "empty messages list"})
                    continue

                first_msg = msgs[0]
                first_content = first_msg.get("content")
                first_speaker = first_msg.get("speaker_slot")

                if root_content != first_content:
                    violations.append({
                        "file": fname,
                        "greeting_id": gid,
                        "issue": "content parity mismatch",
                        "root_content_len": len(root_content) if root_content else None,
                        "first_msg_len": len(first_content) if first_content else None,
                    })

                if root_speaker != first_speaker:
                    violations.append({
                        "file": fname,
                        "greeting_id": gid,
                        "issue": "speaker_slot parity mismatch",
                        "root_speaker": root_speaker,
                        "first_speaker": first_speaker,
                    })

                for m_idx, m in enumerate(msgs):
                    total_messages += 1
                    mid = m.get("id", f"msg_{m_idx}")
                    spk = m.get("speaker_slot")
                    if spk not in declared_slots:
                        violations.append({
                            "file": fname,
                            "greeting_id": gid,
                            "message_id": mid,
                            "issue": f"speaker_slot '{spk}' not declared in slots",
                        })

        print(f"\n[Test 05] Total greetings: {total_greetings}, Total messages: {total_messages}")
        self.assertEqual(len(violations), 0, f"Greeting parity violations found: {violations}")

    def test_06_spoken_dialogue_quotes_and_plain_text_narration(self):
        """
        3. Check spoken dialogue in quotes (\"...\"), plain text narration (no asterisks).
           Verify:
           - Double quotes are balanced in each message.
           - No curly/smart quotes (“ ” ‘ ’).
           - Inspect asterisks: are there asterisks in narration?
             (Rule: plain text narration without asterisks; asterisks reserved strictly for internal thoughts).
        """
        violations = []
        asterisk_usages = []
        total_messages = 0

        # Smart quotes
        SMART_QUOTES = ["“", "”", "‘", "’"]

        for fname, data in self.json_data.items():
            greetings = data.get("greetings", [])
            for g_idx, g in enumerate(greetings):
                gid = g.get("id", f"idx_{g_idx}")
                for m_idx, m in enumerate(g.get("messages", [])):
                    total_messages += 1
                    mid = m.get("id", f"msg_{m_idx}")
                    content = m.get("content", "")

                    # 1. Smart quotes check
                    for sq in SMART_QUOTES:
                        if sq in content:
                            violations.append({
                                "file": fname,
                                "greeting_id": gid,
                                "message_id": mid,
                                "issue": f"Smart quote found: {sq}"
                            })

                    # 2. Balanced standard double quotes
                    q_count = content.count('"')
                    if q_count % 2 != 0:
                        violations.append({
                            "file": fname,
                            "greeting_id": gid,
                            "message_id": mid,
                            "issue": f"Unbalanced double quotes: count={q_count}"
                        })

                    # 3. Asterisk check: find any asterisks
                    if "*" in content:
                        # Check whether asterisks are balanced and how they are used
                        ast_count = content.count("*")
                        if ast_count % 2 != 0:
                            violations.append({
                                "file": fname,
                                "greeting_id": gid,
                                "message_id": mid,
                                "issue": f"Unbalanced asterisks: count={ast_count}"
                            })
                        # Collect snippet of asterisk usage
                        matches = re.findall(r"\*([^*]+)\*", content)
                        for match in matches:
                            asterisk_usages.append({
                                "file": fname,
                                "greeting_id": gid,
                                "message_id": mid,
                                "thought": match.strip()
                            })

        print(f"\n[Test 06] Messages checked: {total_messages}, Asterisk internal thoughts found: {len(asterisk_usages)}")
        for u in asterisk_usages[:5]:
            print(f"   Sample internal thought: *{u['thought']}* ({u['file']} {u['message_id']})")

        self.assertEqual(len(violations), 0, f"Dialogue / narration formatting violations: {violations}")

    def test_07_zero_redundant_speaker_name_prefixes(self):
        """
        5. Ensure zero redundant speaker name prefixes inside message content.
           e.g. 'Rory Ballantine: ...' or 'Radek: ...' or 'twin: ...'
           The Wyvern UI displays the avatar and speaker name via speaker_slot.
           Hardcoded speaker prefixes inside content are redundant and prohibited.
        """
        violations = []
        total_messages = 0

        # Pattern for suspicious speaker prefix at the beginning of a message or paragraph:
        # e.g., "Name:", "First Last:", "SLOT_NAME:", "[Name]:", etc.
        prefix_pattern = re.compile(r"^\s*(\[?[A-Za-z0-9_'\s-]{2,30}\]?)\s*:\s*(?:\"|[A-Za-z])")

        # Exclusions for valid colons (e.g. timestamps like 10:00, or specific phrases)
        for fname, data in self.json_data.items():
            # Build list of slot keys and slot labels in this scenario
            slots = data.get("slots", [])
            slot_identifiers = set()
            for s in slots:
                slot_identifiers.add(s.get("key", "").lower())
                label = s.get("label", "").lower()
                slot_identifiers.add(label)
                # Split label into words
                for w in label.split():
                    if len(w) > 3:
                        slot_identifiers.add(w)

            greetings = data.get("greetings", [])
            for g_idx, g in enumerate(greetings):
                gid = g.get("id", f"idx_{g_idx}")
                for m_idx, m in enumerate(g.get("messages", [])):
                    total_messages += 1
                    mid = m.get("id", f"msg_{m_idx}")
                    spk = m.get("speaker_slot")
                    content = m.get("content", "")

                    lines = content.strip().splitlines()
                    for line_no, line in enumerate(lines, start=1):
                        line_str = line.strip()
                        if not line_str:
                            continue

                        # Check if line starts with "<Speaker>:"
                        m_prefix = prefix_pattern.match(line_str)
                        if m_prefix:
                            candidate_speaker = m_prefix.group(1).strip("[]").strip()
                            cand_lower = candidate_speaker.lower()

                            # If candidate speaker matches a slot key, or character name, or matches known character names
                            if cand_lower in slot_identifiers or cand_lower == spk.lower():
                                violations.append({
                                    "file": fname,
                                    "greeting_id": gid,
                                    "message_id": mid,
                                    "line": line_no,
                                    "prefix": candidate_speaker,
                                    "snippet": line_str[:60]
                                })
                            # Also check generic speaker patterns like "Radek:", "Goran:", "Erik:", "Mara Voss:"
                            elif any(cand_lower.startswith(x) for x in ["radek", "goran", "alyssa", "jasper", "erik", "logan", "malachia", "noah", "wulfnic", "edric", "rory", "sully", "sinclair", "jean-luc", "alicia", "mara", "marcus", "celeste", "russ", "scarlett", "finnegan", "jared", "vincent"]):
                                violations.append({
                                    "file": fname,
                                    "greeting_id": gid,
                                    "message_id": mid,
                                    "line": line_no,
                                    "prefix": candidate_speaker,
                                    "snippet": line_str[:60]
                                })

        print(f"\n[Test 07] Messages checked for redundant speaker prefixes: {total_messages}")
        self.assertEqual(len(violations), 0, f"Redundant speaker name prefixes found: {violations}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
