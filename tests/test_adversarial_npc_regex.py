#!/usr/bin/env python3
"""
tests/test_adversarial_npc_regex.py

Adversarial Stress Test Suite for Milestone 1 (R1):
- Module 93312 Regex Compiler Stress Harness
- Unicode, Nordic accents, Elder Futhark runes
- Tricky prefixes (=>, ->, [NPC], etc.) and delimiters (:, |, -, ::, empty)
- Hyphenated names, apostrophes, single quotes, double quotes, curly quotes
- Structural edge cases: single-word names, empty lists, titles with periods
- Regex engine compilation matrix: Python standard `re`, Python `regex` (PCRE), Node.js JavaScript RegExp
- Duplicate surname detection & elimination analysis on corrupt inputs
"""

import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.verify_npc_schema_contract import (
    compile_wyvern_avatar_regex,
    detect_duplicate_surnames,
    escape_wyvern,
    validate_npc_info_schema,
)

try:
    import regex as pcre_regex
except ImportError:
    pcre_regex = None


class TestAdversarialUnicodeAndRunes(unittest.TestCase):
    """
    Stress test Module 93312 with Nordic characters, accents, runes, and multilingual names.
    """

    def setUp(self):
        self.complex_names = [
            {
                "first_name": "Wulfnic",
                "middle_names": ["Báleygr"],
                "last_name": "Bloodmoon",
                "nicknames": ["The One-Eyed Wolf", "Jarl of Svartúlfr"],
                "titles": ["Jarl", "Firstborn"]
            },
            {
                "first_name": "Logan",
                "middle_names": ["Dominic", "Járn"],
                "last_name": "Douglas",
                "nicknames": ["The Iron Wolf", "Uncle Logan"],
                "titles": ["Beta"]
            },
            {
                "first_name": "Svartr",
                "middle_names": [],
                "last_name": None,
                "nicknames": ["The Shadow"],
                "titles": []
            },
            {
                "first_name": "Malachia",
                "middle_names": ["Björn"],
                "last_name": "Douglas Bloodmoon",
                "nicknames": ["The Ascended Enigma", "Big Bear"],
                "titles": ["Dominant Alpha"]
            },
            {
                "first_name": "Æthelred",
                "middle_names": ["Þórr"],
                "last_name": "Ragnarök",
                "nicknames": ["The Thunderer"],
                "titles": ["Chieftain"]
            },
            {
                "first_name": "ᛋᚢᚨᚱᛏᚢᛚᚠᚱ",  # Svartulfr in Elder Futhark runes
                "middle_names": ["ᚠᚢᚦᚨᚱᚲ"],
                "last_name": "ᛒᛚᛟᛟᛞᛗᛟᛟᚾ",
                "nicknames": ["Runemaster"],
                "titles": ["Ancient"]
            },
            {
                "first_name": "François-Noël",
                "middle_names": ["Chloë", "Håkon"],
                "last_name": "d'Artois",
                "nicknames": ["L'Étranger"],
                "titles": ["Comte"]
            }
        ]

    def test_nordic_and_rune_compilation_under_pcre(self):
        if pcre_regex is None:
            self.skipTest("pcre_regex not installed")
        for npc in self.complex_names:
            pat = compile_wyvern_avatar_regex(npc)
            self.assertTrue(len(pat) > 0, f"Pattern was empty for {npc['first_name']}")
            try:
                compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
                self.assertIsNotNone(compiled)
            except Exception as e:
                self.fail(f"PCRE compilation failed for {npc['first_name']}: {e}")

    def test_nordic_and_rune_compilation_under_js(self):
        """Verify compilation in JavaScript V8 engine (Node.js) with 'u' flag."""
        for npc in self.complex_names:
            pat = compile_wyvern_avatar_regex(npc)
            js_script = f"""
            const pat = {json.dumps(pat)};
            try {{
                const re = new RegExp(pat, 'u');
                process.exit(0);
            }} catch(e) {{
                console.error(e.message);
                process.exit(1);
            }}
            """
            res = subprocess.run(["node", "-e", js_script], capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, f"Node.js RegExp('u') failed for {npc['first_name']}: {res.stderr}")


class TestAdversarialPrefixesAndDelimiters(unittest.TestCase):
    """
    Stress test tricky prefixes (=>, ->, [NPC], (!), etc.) and delimiters (:, |, -, ::, empty).
    """

    def setUp(self):
        self.base_npc = {
            "first_name": "Sierra",
            "middle_names": [],
            "last_name": "Cruz",
            "nicknames": ["Rainbow Lamia"],
            "titles": []
        }
        self.prefixes = [
            "=>",
            "->",
            "[NPC]",
            "(!)",
            "(BOT)",
            "[SYSTEM]:",
            "***",
            "#",
            "//",
            "<<<",
            ""
        ]
        self.delimiters = [
            ":",
            "|",
            "-",
            "::",
            ";",
            ">",
            "",
            "   "
        ]

    def test_all_prefix_and_delimiter_combinations_under_pcre(self):
        if pcre_regex is None:
            self.skipTest("pcre_regex not installed")
        for pref in self.prefixes:
            for delim in self.delimiters:
                pat = compile_wyvern_avatar_regex(self.base_npc, prefix=pref, delimiter=delim)
                try:
                    compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
                    self.assertIsNotNone(compiled)
                except Exception as e:
                    self.fail(f"PCRE failed on prefix={repr(pref)}, delim={repr(delim)}: {e}")

    def test_all_prefix_and_delimiter_combinations_under_js(self):
        for pref in self.prefixes:
            for delim in self.delimiters:
                pat = compile_wyvern_avatar_regex(self.base_npc, prefix=pref, delimiter=delim)
                js_script = f"""
                const pat = {json.dumps(pat)};
                try {{
                    const re = new RegExp(pat, 'u');
                    process.exit(0);
                }} catch(e) {{
                    console.error('Prefix={pref}, Delim={delim}:', e.message);
                    process.exit(1);
                }}
                """
                res = subprocess.run(["node", "-e", js_script], capture_output=True, text=True)
                self.assertEqual(res.returncode, 0, f"JS failed on prefix={repr(pref)}, delim={repr(delim)}: {res.stderr}")

    def test_prefix_dialogue_matching(self):
        if pcre_regex is None:
            self.skipTest("pcre_regex not installed")
        # Test bracketed prefix [NPC]
        pat = compile_wyvern_avatar_regex(self.base_npc, prefix="[NPC]", delimiter=":")
        compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
        m = compiled.search('[NPC] Sierra Cruz: "I glide across the sand."')
        self.assertIsNotNone(m, "Failed to match dialogue with [NPC] prefix")
        self.assertEqual(m.group("coreName").lower(), "sierra cruz")


class TestAdversarialQuotesHyphensAndApostrophes(unittest.TestCase):
    """
    Stress test hyphenated names, single quotes, double quotes, and typographic curly quotes.
    """

    def setUp(self):
        self.quote_npcs = [
            {
                "first_name": "Jean-Luc",
                "middle_names": [],
                "last_name": "Virtuoso",
                "nicknames": ["The Human Telepath"],
                "titles": ["Master"]
            },
            {
                "first_name": "Marcus",
                "middle_names": [],
                "last_name": "O'Connor",
                "nicknames": ["Mark", "O’Connor"],  # with curly apostrophe
                "titles": ["Officer"]
            },
            {
                "first_name": "Luisa",
                "middle_names": [],
                "last_name": "Sanchez-Rogers",
                "nicknames": ["Mac's Sister", 'The "Iron" Lass'],
                "titles": []
            },
            {
                "first_name": "D'Angelo",
                "middle_names": ["D′Artagnan"],  # prime symbol
                "last_name": "De’Medici",
                "nicknames": ["‘The Prince’", "“Capo”"],
                "titles": ["Don"]
            },
            {
                "first_name": "Marie‑Claire",  # non-breaking hyphen
                "middle_names": [],
                "last_name": "Saint—Germain",  # em-dash
                "nicknames": ["Alchemist"],
                "titles": ["Lady"]
            }
        ]

    def test_quotes_and_hyphens_under_pcre(self):
        if pcre_regex is None:
            self.skipTest("pcre_regex not installed")
        for npc in self.quote_npcs:
            pat = compile_wyvern_avatar_regex(npc)
            try:
                compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
                self.assertIsNotNone(compiled)
            except Exception as e:
                self.fail(f"PCRE failed on {npc['first_name']}: {e}")

    def test_quotes_and_hyphens_under_js(self):
        for npc in self.quote_npcs:
            pat = compile_wyvern_avatar_regex(npc)
            js_script = f"""
            const pat = {json.dumps(pat)};
            try {{
                const re = new RegExp(pat, 'u');
                process.exit(0);
            }} catch(e) {{
                console.error(e.message);
                process.exit(1);
            }}
            """
            res = subprocess.run(["node", "-e", js_script], capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, f"JS failed on {npc['first_name']}: {res.stderr}")

    def test_matching_with_curly_and_straight_apostrophes(self):
        if pcre_regex is None:
            self.skipTest("pcre_regex not installed")
        npc = {"first_name": "Marcus", "last_name": "O'Connor"}
        pat = compile_wyvern_avatar_regex(npc)
        compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)

        # Straight apostrophe
        m1 = compiled.search('Marcus O\'Connor: "Stand down."')
        self.assertIsNotNone(m1, "Failed to match straight apostrophe")

        # Typographic right curly apostrophe U+2019
        m2 = compiled.search('Marcus O’Connor: "Stand down."')
        self.assertIsNotNone(m2, "Failed to match curly apostrophe U+2019")


class TestAdversarialStructuralEdgeCases(unittest.TestCase):
    """
    Stress test structural edge cases: single-word names, empty lists, titles with periods, special symbols.
    """

    def test_single_word_name(self):
        npc = {"first_name": "Bruce"}
        pat = compile_wyvern_avatar_regex(npc)
        self.assertIn("(?<coreName>Bruce)", pat)

        if pcre_regex:
            compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
            m = compiled.search('Bruce: "Welcome to KSA."')
            self.assertIsNotNone(m)

    def test_titles_with_periods(self):
        npc = {
            "first_name": "Arthur",
            "last_name": "Sinclair",
            "titles": ["Dr.", "Prof.", "M.D.", "Ph.D."]
        }
        pat = compile_wyvern_avatar_regex(npc)
        # Verify periods are escaped
        self.assertIn(r"Dr\.", pat)
        self.assertIn(r"Prof\.", pat)
        self.assertIn(r"M\.D\.", pat)

        if pcre_regex:
            compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
            m = compiled.search('Dr. Arthur Sinclair: "The formula is stable."')
            self.assertIsNotNone(m)

    def test_empty_lists_and_whitespace_elements(self):
        npc = {
            "first_name": "Adrian",
            "middle_names": ["", "   "],
            "last_name": "",
            "nicknames": ["", "   ", "Ade"],
            "titles": ["", "  "]
        }
        pat = compile_wyvern_avatar_regex(npc)
        self.assertIn("(?<coreName>", pat)
        self.assertIn("Adrian", pat)
        self.assertIn("Ade", pat)

        if pcre_regex:
            compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
            m = compiled.search('Ade: "Checking in."')
            self.assertIsNotNone(m)

    def test_nicknames_with_parentheses_and_brackets(self):
        npc = {
            "first_name": "John",
            "last_name": "Doe",
            "nicknames": ["Agent #7 (Undercover)", "Shadow [Omega]"]
        }
        pat = compile_wyvern_avatar_regex(npc)
        self.assertIn(r"Agent #7 \(Undercover\)", pat)
        self.assertIn(r"Shadow \[Omega\]", pat)

        if pcre_regex:
            compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
            m = compiled.search('Agent #7 (Undercover): "Target spotted."')
            self.assertIsNotNone(m)


class TestRegexEngineCompatibilityMatrix(unittest.TestCase):
    """
    EMPIRICAL CHALLENGE: Verify cross-engine compilation behavior across
    1. Python `re` standard library
    2. Python `regex` (PCRE) library
    3. Node.js JavaScript RegExp (with 'u' flag)
    4. Node.js JavaScript RegExp (with 'v' flag)
    """

    def test_python_standard_re_compatibility_assessment(self):
        """
        EMPIRICAL OBSERVATION: Python's built-in `re` module cannot compile
        Module 93312 regexes directly because built-in `re` does NOT support:
        1. ES2018 named group syntax `(?<name>...)` (requires `(?P<name>...)`)
        2. Unicode property escapes `\\p{L}`, `\\p{N}`, `\\p{Lu}`.
        """
        pat = compile_wyvern_avatar_regex({"first_name": "Erik", "last_name": "Douglas"})
        with self.assertRaises(Exception) as ctx:
            re.compile(pat)
        err_msg = str(ctx.exception)
        # Verify exact failure mechanism
        self.assertTrue(
            "unknown extension" in err_msg or "unrecognized extension" in err_msg or "bad escape" in err_msg,
            f"Unexpected error from re.compile: {err_msg}"
        )

    def test_python_pcre_regex_package_compatibility(self):
        """Verify that Python's `regex` (PCRE) module compiles 100% of Module 93312 patterns."""
        if pcre_regex is None:
            self.skipTest("pcre_regex not installed")
        test_cases = [
            {"first_name": "Erik", "last_name": "Douglas"},
            {"first_name": "Wulfnic", "middle_names": ["Báleygr"], "last_name": "Bloodmoon"},
            {"first_name": "Sierra", "last_name": "Cruz", "nicknames": ["Rainbow Lamia"]},
            {"first_name": "Jean-Luc", "last_name": "Virtuoso", "titles": ["Master"]},
        ]
        for tc in test_cases:
            pat = compile_wyvern_avatar_regex(tc)
            compiled = pcre_regex.compile(pat, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)
            self.assertIsNotNone(compiled)

    def test_javascript_v8_u_flag_compatibility(self):
        """Verify that Node.js with 'u' flag compiles 100% of Module 93312 patterns."""
        test_cases = [
            {"first_name": "Erik", "last_name": "Douglas"},
            {"first_name": "Wulfnic", "middle_names": ["Báleygr"], "last_name": "Bloodmoon"},
            {"first_name": "Sierra", "last_name": "Cruz", "nicknames": ["Rainbow Lamia"]},
            {"first_name": "Jean-Luc", "last_name": "Virtuoso", "titles": ["Master"]},
        ]
        for tc in test_cases:
            pat = compile_wyvern_avatar_regex(tc)
            js_script = f"""
            const pat = {json.dumps(pat)};
            const re = new RegExp(pat, 'u');
            console.log(re.test('Erik Douglas: test'));
            """
            res = subprocess.run(["node", "-e", js_script], capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, f"Node.js failed: {res.stderr}")

    def test_javascript_v8_v_flag_hyphen_behavior(self):
        """
        EMPIRICAL OBSERVATION: Under ES2024 'v' flag (unicodeSets), unescaped hyphens
        inside `[-‐‑‒–—−]` cause:
        'Invalid regular expression: /[-‐‑‒–—−]/v: Invalid character in character class'.
        Wyvern uses the 'u' flag where it is valid.
        """
        js_script = """
        try {
            new RegExp('[-‐‑‒–—−]', 'v');
            console.log('V_SUCCESS');
        } catch(e) {
            console.log('V_SYNTAX_ERROR');
        }
        """
        res = subprocess.run(["node", "-e", js_script], capture_output=True, text=True)
        self.assertIn("V_SYNTAX_ERROR", res.stdout)


class TestAdversarialDuplicateSurnameElimination(unittest.TestCase):
    """
    Stress test duplicate surname detection and elimination on corrupt vs clean entries.
    """

    def test_clean_input_generates_zero_duplicate_surnames(self):
        # Cleanly structured NPC
        clean_hugh = {
            "first_name": "Hugh",
            "last_name": "Rivers",
            "nicknames": ["Alpha Rivers", "The Mountain Sovereign"]
        }
        pat = compile_wyvern_avatar_regex(clean_hugh)
        defects = detect_duplicate_surnames(pat, clean_hugh["last_name"])
        self.assertEqual(len(defects), 0, f"Expected 0 duplicate surnames, got {defects}")

    def test_corrupt_input_with_embedded_duplicate_surname_detected(self):
        # Corrupt input where legacy data already concatenated surname into first_name or nickname
        corrupt_hugh = {
            "first_name": "Hugh Rivers",
            "last_name": "Rivers",
            "nicknames": ["Alpha Rivers Rivers"]
        }
        pat = compile_wyvern_avatar_regex(corrupt_hugh)
        defects = detect_duplicate_surnames(pat, corrupt_hugh["last_name"])
        self.assertGreater(len(defects), 0, "Expected detect_duplicate_surnames to flag corrupt entry")
        self.assertIn("Rivers Rivers", defects)

    def test_detector_catches_escaped_apostrophe_surname(self):
        """
        HARDENED VERIFICATION: detect_duplicate_surnames normalizes quote character classes
        such as ['‘’ʼ‛′] via normalize_wyvern_regex_pattern, correctly catching duplicate surnames
        even when escaped (e.g. O'Connor O'Connor).
        """
        escaped_pat = r"(?:^|\n)\s*(?:O['‘’ʼ‛′]Connor O['‘’ʼ‛′]Connor)\s*:"
        defects = detect_duplicate_surnames(escaped_pat, "O'Connor")
        self.assertEqual(len(defects), 1, "Hardened detector catches escaped apostrophe duplicate")
        self.assertIn("O'Connor O'Connor", defects)

    def test_detector_catches_escaped_hyphenated_surname(self):
        """
        HARDENED VERIFICATION: detect_duplicate_surnames normalizes hyphen character classes
        such as [-‐‑‒–—−] via normalize_wyvern_regex_pattern, correctly catching duplicate surnames
        even when escaped (e.g. Sanchez-Rogers Sanchez-Rogers).
        """
        escaped_pat = r"(?:^|\n)\s*(?:Sanchez[-‐‑‒–—−]Rogers Sanchez[-‐‑‒–—−]Rogers)\s*:"
        defects = detect_duplicate_surnames(escaped_pat, "Sanchez-Rogers")
        self.assertEqual(len(defects), 1, "Hardened detector catches escaped hyphen duplicate")
        self.assertIn("Sanchez-Rogers Sanchez-Rogers", defects)

    def test_detector_blindspot_on_nordic_accented_generic_duplicates(self):
        """
        EMPIRICAL FINDING: generic_dupes regex r'\\b([A-Za-z]{3,})\\s+\\1\\b' uses ASCII-only
        [A-Za-z], so uncataloged Nordic duplicate surnames (e.g. Báleygr Báleygr) are missed
        unless explicitly passed in last_name.
        """
        pat_nordic = r"(?:^|\n)\s*(?:Báleygr Báleygr)\s*:"
        # Without last_name argument
        defects_generic = detect_duplicate_surnames(pat_nordic)
        self.assertEqual(len(defects_generic), 0, "Generic regex missed accented Báleygr Báleygr")

        # With last_name argument
        defects_explicit = detect_duplicate_surnames(pat_nordic, "Báleygr")
        self.assertEqual(len(defects_explicit), 1, "Explicit check found Báleygr Báleygr")


if __name__ == "__main__":
    unittest.main()
