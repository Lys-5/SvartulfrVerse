"""
Adversarial Boundary Stress Test Suite: tests/test_milestone2_boundary_stress.py
Author: challenger_m2_2 (empirical-challenger)
Milestone: Milestone 2 (Scenario & Chat Standardization)

Objective:
Empirically stress-test boundary conditions across all 3 premade scenes in Scenario `_2MTWKjxrQPdQVaz9y4Q7H`
(local and live Wyvern Web API) and Message #0 in active chat `chat_log_PJx1W1rg3WUzRM7MnQrkN`:
1. Exact count of em-dashes: assert 0 (including Unicode dash variants).
2. Exact count of asterisks outside quotes: assert 0 (and total asterisks = 0).
3. Quotes balance: assert all dialogue quotes are balanced standard ASCII double quotes (zero curly quotes, even parity per beat).
4. Speaker tags: assert no plain untagged dialogue, narrator beats contain 0 quotes, character beats contain >= 1 quotes.
"""

import unittest
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Set stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
SCENARIO_JSON_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json'
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

SCENARIO_ID = "_2MTWKjxrQPdQVaz9y4Q7H"
CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
SWIPE_ID = "message_swipe_99mmMgEEQjk2pkJN3hXkQ"

VALID_CANONICAL_SPEAKERS = {
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah',
    'Malachia', 'Jasper', 'Alyssa', 'Wulfnic', 'Zefir',
    'Finn', 'Sierra', 'Scarlett'
}

DASH_VARIANTS = {
    'em-dash': '\u2014',          # —
    'en-dash': '\u2013',          # –
    'horizontal-bar': '\u2015',   # ―
    'two-em-dash': '\u2e3a',      # ⸺
    'three-em-dash': '\u2e3b',    # ⸻
    'small-em-dash': '\ufe58',    # ﹘
}

CURLY_QUOTES = {
    'left-double': '\u201c',      # “
    'right-double': '\u201d',     # ”
    'low-double': '\u201e',       # „
    'high-reversed-double': '\u201f' # ‟
}


class TestMilestone2BoundaryStress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 1. Load local scenario JSON
        assert SCENARIO_JSON_PATH.exists(), f"Missing {SCENARIO_JSON_PATH}"
        with open(SCENARIO_JSON_PATH, 'r', encoding='utf-8') as f:
            cls.local_scenario = json.load(f)

        # 2. Fetch live Wyvern API scenario and chat log
        assert TOKEN_PATH.exists(), f"Missing {TOKEN_PATH}"
        cls.token = TOKEN_PATH.read_text(encoding='utf-8').strip()
        assert len(cls.token) > 0, "Wyvern token is empty"

        headers = {'Authorization': f'Bearer {cls.token}', 'User-Agent': 'Mozilla/5.0'}

        # Fetch Live Scenario
        sc_req = urllib.request.Request(f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}", headers=headers)
        with urllib.request.urlopen(sc_req) as resp:
            assert resp.status == 200, f"Scenario GET failed with status {resp.status}"
            cls.live_scenario = json.loads(resp.read().decode('utf-8'))

        # Fetch Live Chat Log
        ch_req = urllib.request.Request(f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}", headers=headers)
        with urllib.request.urlopen(ch_req) as resp:
            assert resp.status == 200, f"Chat GET failed with status {resp.status}"
            cls.live_chat_log = json.loads(resp.read().decode('utf-8'))


        # Prepare target texts for parameterized stress tests
        cls.targets = {
            'local_scene_0': cls.local_scenario['premade_scenes'][0]['scene_text'],
            'local_scene_1': cls.local_scenario['premade_scenes'][1]['scene_text'],
            'local_scene_2': cls.local_scenario['premade_scenes'][2]['scene_text'],
            'live_scene_0': cls.live_scenario['premade_scenes'][0]['scene_text'],
            'live_scene_1': cls.live_scenario['premade_scenes'][1]['scene_text'],
            'live_scene_2': cls.live_scenario['premade_scenes'][2]['scene_text'],
            'live_msg0_swipe': cls.live_chat_log['messages'][0]['swipes'][0]['content'],
            'live_msg0_content': cls.live_chat_log['messages'][0]['content'],
        }

    # =========================================================================
    # Group 1: Em-Dashes and Dash Variants Boundary Testing
    # =========================================================================

    def test_01_exact_count_em_dashes_zero(self):
        """Assert exactly 0 em-dashes ('—', \\u2014) across all scenes and Message #0."""
        for label, text in self.targets.items():
            count = text.count('\u2014')
            self.assertEqual(count, 0, f"Target '{label}' contains {count} em-dashes (\\u2014). Expected 0.")

    def test_02_extended_unicode_dash_variants_zero(self):
        """Assert 0 occurrences of all extended Unicode dash variants (en-dash, horizontal bar, multi-em)."""
        for label, text in self.targets.items():
            for name, char in DASH_VARIANTS.items():
                count = text.count(char)
                self.assertEqual(
                    count, 0,
                    f"Target '{label}' contains {count} occurrences of {name} ({repr(char)}). Expected 0."
                )

    def test_03_no_markdown_pseudo_em_dashes(self):
        """Assert no markdown double hyphens ('--') or triple hyphens ('---') acting as em-dashes."""
        for label, text in self.targets.items():
            # Allow negative numbers or hyphenated words (e.g. single '-'), but reject '--' or '---'
            double_hyphens = text.count('--')
            self.assertEqual(
                double_hyphens, 0,
                f"Target '{label}' contains {double_hyphens} pseudo em-dashes ('--'). Rule requires commas or periods."
            )

    # =========================================================================
    # Group 2: Asterisks Outside (and Inside) Quotes
    # =========================================================================

    def test_04_asterisks_outside_quotes_zero(self):
        """Assert exact count of asterisks outside quotes is strictly 0."""
        for label, text in self.targets.items():
            in_quote = False
            asterisks_outside = 0
            for idx, ch in enumerate(text):
                if ch == '"':
                    in_quote = not in_quote
                elif ch == '*':
                    if not in_quote:
                        asterisks_outside += 1
            self.assertEqual(
                asterisks_outside, 0,
                f"Target '{label}' contains {asterisks_outside} asterisks outside quotes! Actions must be plain text."
            )

    def test_05_total_asterisks_zero(self):
        """Assert total asterisks is strictly 0 (no markdown bolding, italics, or spurious asterisks)."""
        for label, text in self.targets.items():
            total_asterisks = text.count('*')
            self.assertEqual(
                total_asterisks, 0,
                f"Target '{label}' contains {total_asterisks} asterisks total. Expected 0."
            )

    # =========================================================================
    # Group 3: Quotes Balance and Double Quotes Discipline
    # =========================================================================

    def test_06_overall_quotes_balance(self):
        """Assert all dialogue quotes have even parity (every opening quote has a closing quote)."""
        for label, text in self.targets.items():
            q_count = text.count('"')
            self.assertGreater(q_count, 0, f"Target '{label}' has 0 quotes, expected dialogue.")
            self.assertEqual(
                q_count % 2, 0,
                f"Target '{label}' has unbalanced quotes! Total count is odd ({q_count})."
            )

    def test_07_zero_curly_quotes(self):
        """Assert 0 curly quotation marks (“ ” „ ‟) across all targets; standard ASCII quotes only."""
        for label, text in self.targets.items():
            for name, char in CURLY_QUOTES.items():
                count = text.count(char)
                self.assertEqual(
                    count, 0,
                    f"Target '{label}' contains {count} curly quotes of type {name} ({repr(char)}). Standard double quotes only."
                )

    def test_08_beat_level_quotes_balance(self):
        """Assert every individual speaker beat independently has balanced quotes (no cross-beat bleeding)."""
        for label, text in self.targets.items():
            beats = [b for b in text.split('=>') if b.strip()]
            for b_idx, beat in enumerate(beats):
                lines = beat.strip().splitlines()
                speaker = lines[0].split(':')[0].strip()
                q_count = beat.count('"')
                self.assertEqual(
                    q_count % 2, 0,
                    f"Target '{label}' beat {b_idx} [{speaker}] has unbalanced quotes! Count={q_count}."
                )

    def test_09_all_quotes_non_empty(self):
        """Assert no empty dialogue quotes (\"\" or \"  \")."""
        for label, text in self.targets.items():
            quotes = re.findall(r'"([^"]*)"', text)
            for q_idx, quote in enumerate(quotes):
                self.assertTrue(
                    len(quote.strip()) > 0,
                    f"Target '{label}' quote #{q_idx} is empty or whitespace-only!"
                )

    # =========================================================================
    # Group 4: Speaker Tags and No Plain Untagged Dialogue
    # =========================================================================

    def test_10_all_texts_start_with_narrator(self):
        """Assert all scenes and Message #0 start strictly with '=>Narrator:' without untagged leading text."""
        for label, text in self.targets.items():
            stripped = text.strip()
            self.assertTrue(
                stripped.startswith('=>Narrator:'),
                f"Target '{label}' does not start with '=>Narrator:'. Leading text is untagged!"
            )

    def test_11_no_plain_unprefixed_speaker_tags(self):
        """Assert no plain speaker prefixes without '=>' (e.g. 'Erik: \"...\"' or 'Erik Ulfr Douglas: \"...\"')."""
        for label, text in self.targets.items():
            # Match any line starting with CapitalizedName: followed by quote or text, not preceded by =>
            plain_matches = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', text, flags=re.MULTILINE)
            self.assertEqual(
                plain_matches, [],
                f"Target '{label}' has plain un-prefixed speaker tags: {plain_matches}"
            )

    def test_12_all_speaker_tags_in_canonical_whitelist(self):
        """Assert all '=>Speaker:' tags use canonical short whitelist names."""
        for label, text in self.targets.items():
            tags = re.findall(r'^=>([A-Za-z0-9_]+):', text, flags=re.MULTILINE)
            for tag in tags:
                self.assertIn(
                    tag, VALID_CANONICAL_SPEAKERS,
                    f"Target '{label}' contains non-canonical speaker tag '=>{tag}:'!"
                )

    def test_13_narrator_beats_contain_zero_dialogue(self):
        """Assert all Narrator beats contain exactly 0 dialogue quotes (no untagged speech in narration)."""
        for label, text in self.targets.items():
            beats = [b for b in text.split('=>') if b.strip()]
            for b_idx, beat in enumerate(beats):
                speaker = beat.strip().splitlines()[0].split(':')[0].strip()
                if speaker == 'Narrator':
                    quotes = re.findall(r'"([^"]*)"', beat)
                    self.assertEqual(
                        quotes, [],
                        f"Target '{label}' Narrator beat {b_idx} contains dialogue quotes: {quotes}! Speech must have a character speaker tag."
                    )

    def test_14_character_beats_contain_dialogue(self):
        """Assert all character beats contain at least 1 dialogue quote."""
        for label, text in self.targets.items():
            beats = [b for b in text.split('=>') if b.strip()]
            for b_idx, beat in enumerate(beats):
                speaker = beat.strip().splitlines()[0].split(':')[0].strip()
                if speaker != 'Narrator':
                    quotes = re.findall(r'"([^"]*)"', beat)
                    self.assertGreater(
                        len(quotes), 0,
                        f"Target '{label}' character beat {b_idx} [{speaker}] contains 0 dialogue quotes!"
                    )

    # =========================================================================
    # Group 5: Exact Live-to-Local Parity & Message Synchronization
    # =========================================================================

    def test_15_live_to_local_scene_texts_exact_match(self):
        """Assert all 3 premade scenes in live Wyvern scenario match local JSON byte-for-byte."""
        for i in range(3):
            local_txt = self.local_scenario['premade_scenes'][i]['scene_text']
            live_txt = self.live_scenario['premade_scenes'][i]['scene_text']
            self.assertEqual(
                live_txt, local_txt,
                f"Scene {i} in live API does NOT match local JSON byte-for-byte!"
            )

    def test_16_chat_log_msg0_content_matches_swipe0_content(self):
        """Assert message_swipe_99mmMgEEQjk2pkJN3hXkQ content matches messages[0].content byte-for-byte."""
        swipe_content = self.live_chat_log['messages'][0]['swipes'][0]['content']
        msg_content = self.live_chat_log['messages'][0]['content']
        self.assertEqual(
            swipe_content, msg_content,
            "Active chat message #0 content differs from swipe #0 content!"
        )


if __name__ == '__main__':
    unittest.main()
