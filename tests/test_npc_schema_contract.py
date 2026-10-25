#!/usr/bin/env python3
"""
tests/test_npc_schema_contract.py

Authoritative Test Suite for Wyvern NPC Schema Contracts (Milestone 1 / R1):
- Contract 1: `npc_info` schema validation (first_name, middle_names, last_name, nicknames, titles, npc_prefix).
- Contract 2: Avatar gallery contract (HTTPS Cloudflare/Janitor URLs, root gallery array, gallery_count).
- Contract 3: Wyvern Module 93312 compilation logic (replicated native compiler, duplicate surname elimination).
- Contract 4: Anti-collision preservation (ignored_characters, ignored_personas, selective/secondary_keys rules).
- Contract 5: Byte-for-byte parity contract between entries and lexicon.

Compatible with both `unittest` and `pytest`.
"""

import json
import os
import sys
import unittest
from pathlib import Path
from typing import Any, Dict, List

# Ensure scripts directory is on sys.path for direct import
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.verify_npc_schema_contract import (
    CANONICAL_BROAD_KEYS,
    NpcInfoSchema,
    compile_wyvern_avatar_regex,
    detect_duplicate_surnames,
    escape_wyvern,
    is_valid_https_url,
    normalize_wyvern_regex_pattern,
    validate_anti_collision_contract,
    validate_avatar_gallery_contract,
    validate_entries_lexicon_parity,
    validate_npc_info_schema,
)

try:
    import regex as pcre_regex
except ImportError:
    pcre_regex = None


class TestNpcInfoSchemaContract(unittest.TestCase):
    """
    Contract 1: Validation of `npc_info` schema.
    Verifies that all 6 fields (first_name, middle_names, last_name, nicknames, titles, npc_prefix)
    conform to Wyvern's frontend and runtime contracts.
    """

    def setUp(self):
        self.erik_full = {
            "first_name": "Erik",
            "middle_names": ["Ulfr"],
            "last_name": "Douglas",
            "nicknames": ["The Old Wolf", "Pack Leader"],
            "titles": ["Lord", "Alpha"],
            "npc_prefix": ""
        }
        self.scarlett_minimal = {
            "first_name": "Scarlett",
            "middle_names": [],
            "last_name": "Rose",
            "nicknames": ["Red"],
            "titles": [],
            "npc_prefix": None
        }

    def test_valid_full_npc_info_passes(self):
        valid, errors = validate_npc_info_schema(self.erik_full)
        self.assertTrue(valid, f"Expected valid full schema, got errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_valid_minimal_npc_info_passes(self):
        valid, errors = validate_npc_info_schema(self.scarlett_minimal)
        self.assertTrue(valid, f"Expected valid minimal schema, got errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_dataclass_conversion_to_dict(self):
        schema = NpcInfoSchema(
            first_name="Alyssa",
            middle_names=["Hvit"],
            last_name="Douglas Bloodmoon",
            nicknames=["Lys", "Sunflower"],
            titles=["The White Moon"],
            npc_prefix=""
        )
        as_dict = schema.to_dict()
        valid, errors = validate_npc_info_schema(as_dict)
        self.assertTrue(valid)
        self.assertEqual(as_dict["first_name"], "Alyssa")
        self.assertEqual(as_dict["middle_names"], ["Hvit"])
        self.assertEqual(as_dict["last_name"], "Douglas Bloodmoon")

    def test_missing_first_name_fails(self):
        payload = {"middle_names": [], "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("first_name is required" in e for e in errors))

    def test_empty_or_whitespace_first_name_fails(self):
        for empty_fn in ["", "   ", "\t\n"]:
            payload = {"first_name": empty_fn, "middle_names": [], "last_name": "Douglas"}
            valid, errors = validate_npc_info_schema(payload)
            self.assertFalse(valid, f"Expected whitespace-only first_name {repr(empty_fn)} to fail")
            self.assertTrue(any("cannot be empty or whitespace" in e for e in errors))

    def test_non_string_first_name_fails(self):
        for bad_fn in [123, 45.6, True, [], {}]:
            payload = {"first_name": bad_fn, "middle_names": []}
            valid, errors = validate_npc_info_schema(payload)
            self.assertFalse(valid, f"Expected non-string first_name {bad_fn} to fail")
            self.assertTrue(any("must be a string" in e for e in errors))

    def test_missing_middle_names_fails(self):
        payload = {"first_name": "Erik", "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names is required in npc_info" in e for e in errors))

    def test_middle_names_none_fails(self):
        payload = {"first_name": "Erik", "middle_names": None, "last_name": "Douglas"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names must be a list of strings, got null" in e for e in errors))

    def test_valid_empty_middle_names_passes(self):
        payload = {"first_name": "Scarlett", "middle_names": [], "last_name": "Rose"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertTrue(valid, f"Unexpected errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_valid_multiple_middle_names_passes(self):
        payload = {"first_name": "Alistair", "middle_names": ["Ambrose", "Alexander"], "last_name": "DeVille"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertTrue(valid, f"Unexpected errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_middle_names_as_string_fails(self):
        # Frontend TagInput requires an array, not a comma-separated string
        payload = {"first_name": "Erik", "middle_names": "Ulfr"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("must be a list of strings" in e for e in errors))

    def test_middle_names_with_non_string_elements_fails(self):
        payload = {"first_name": "Erik", "middle_names": ["Ulfr", 42]}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("middle_names[1] must be a string" in e for e in errors))

    def test_last_name_non_string_fails(self):
        payload = {"first_name": "Erik", "middle_names": [], "last_name": ["Douglas"]}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("last_name must be a string or None" in e for e in errors))

    def test_nicknames_as_string_fails(self):
        payload = {"first_name": "Erik", "middle_names": [], "nicknames": "The Old Wolf"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("nicknames must be a list of strings" in e for e in errors))

    def test_nicknames_with_non_string_elements_fails(self):
        payload = {"first_name": "Erik", "middle_names": [], "nicknames": ["The Old Wolf", None]}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("nicknames[1] must be a string" in e for e in errors))

    def test_titles_as_string_fails(self):
        payload = {"first_name": "Erik", "middle_names": [], "titles": "Alpha"}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("titles must be a list of strings" in e for e in errors))

    def test_npc_prefix_non_string_fails(self):
        payload = {"first_name": "Erik", "middle_names": [], "npc_prefix": 100}
        valid, errors = validate_npc_info_schema(payload)
        self.assertFalse(valid)
        self.assertTrue(any("npc_prefix must be a string or None" in e for e in errors))

    def test_non_dict_payload_fails(self):
        valid, errors = validate_npc_info_schema("not_a_dict")
        self.assertFalse(valid)
        self.assertTrue(any("must be a dictionary" in e for e in errors))


class TestAvatarGalleryContract(unittest.TestCase):
    """
    Contract 2: Validation of Avatar Gallery and Root Structure.
    Verifies that Lorebooks conform to root `gallery` and `gallery_count` contracts,
    and that NPC entries reference secure HTTPS Cloudflare Images or CDN avatars.
    """

    def test_valid_root_empty_gallery(self):
        root = {"gallery": [], "gallery_count": 0}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertTrue(valid, f"Expected empty root gallery to pass, got: {errors}")

    def test_valid_root_populated_gallery(self):
        root = {
            "gallery": [
                {
                    "id": "item_1",
                    "imageURL": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
                    "title": "Svartulfr Crest",
                    "type": "avatar"
                }
            ],
            "gallery_count": 1
        }
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertTrue(valid, f"Expected populated root gallery to pass, got: {errors}")

    def test_missing_root_gallery_property_fails(self):
        root = {"gallery_count": 0}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertFalse(valid)
        self.assertTrue(any("missing 'gallery'" in e for e in errors))

    def test_missing_root_gallery_count_fails(self):
        root = {"gallery": []}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertFalse(valid)
        self.assertTrue(any("missing 'gallery_count'" in e for e in errors))

    def test_gallery_not_a_list_fails(self):
        root = {"gallery": "invalid", "gallery_count": 0}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertFalse(valid)
        self.assertTrue(any("'gallery' must be a list" in e for e in errors))

    def test_negative_gallery_count_fails(self):
        root = {"gallery": [], "gallery_count": -5}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertFalse(valid)
        self.assertTrue(any("non-negative integer" in e for e in errors))

    def test_gallery_count_mismatch_fails(self):
        root = {"gallery": [{"id": "1"}], "gallery_count": 5}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root)
        self.assertFalse(valid)
        self.assertTrue(any("does not match len(gallery)" in e for e in errors))

    def test_valid_cloudflare_avatar_url(self):
        entry = {"avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"}
        valid, errors = validate_avatar_gallery_contract(entry=entry)
        self.assertTrue(valid, f"Expected valid Cloudflare avatar URL, got: {errors}")

    def test_valid_janitor_avatar_url(self):
        entry = {"avatar": "https://ella.janitorai.com/bot-avatars/b4b7fa65-1d6f-4423-8cfb-bc1944e99f0e_6cb711e6-3475-429a-b4ff-57bc932a9c3d.webp"}
        valid, errors = validate_avatar_gallery_contract(entry=entry)
        self.assertTrue(valid, f"Expected valid Janitor avatar URL, got: {errors}")

    def test_insecure_http_avatar_fails(self):
        entry = {"avatar": "http://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/test/public"}
        valid, errors = validate_avatar_gallery_contract(entry=entry)
        self.assertFalse(valid)
        self.assertTrue(any("must be an HTTPS URL" in e for e in errors))

    def test_missing_or_empty_avatar_fails(self):
        for bad_av in ["", None, False]:
            entry = {"avatar": bad_av}
            valid, errors = validate_avatar_gallery_contract(entry=entry)
            self.assertFalse(valid)
            self.assertTrue(any("missing 'avatar' field" in e for e in errors))

    def test_alternate_avatars_list_validation(self):
        entry = {
            "avatar": "https://imagedelivery.net/main.png",
            "alternate_avatars": [
                "https://imagedelivery.net/alt1.png",
                "https://imagedelivery.net/alt2.png"
            ]
        }
        valid, errors = validate_avatar_gallery_contract(entry=entry)
        self.assertTrue(valid)

        # Insecure entry in alternate_avatars
        bad_entry = {
            "avatar": "https://imagedelivery.net/main.png",
            "alternate_avatars": ["http://insecure.net/alt1.png"]
        }
        valid, errors = validate_avatar_gallery_contract(entry=bad_entry)
        self.assertFalse(valid)
        self.assertTrue(any("alternate_avatars[0]" in e for e in errors))

    def test_gallery_count_boolean_disallowed(self):
        """Negative test: gallery_count=True or False must be rejected even though bool is subclass of int."""
        root_true = {"gallery": [{"id": "1"}], "gallery_count": True}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root_true)
        self.assertFalse(valid, "Expected gallery_count=True to fail validation")
        self.assertTrue(any("non-negative integer" in e for e in errors))

        root_false = {"gallery": [], "gallery_count": False}
        valid, errors = validate_avatar_gallery_contract(lorebook_root=root_false)
        self.assertFalse(valid, "Expected gallery_count=False to fail validation")
        self.assertTrue(any("non-negative integer" in e for e in errors))

    def test_non_dict_lorebook_root_handled_gracefully(self):
        """Negative test: non-dict lorebook_root must return validation error tuple without raising TypeError."""
        for bad_root in [123, "not_a_dict", True, False, [1, 2, 3]]:
            valid, errors = validate_avatar_gallery_contract(lorebook_root=bad_root)
            self.assertFalse(valid, f"Expected non-dict lorebook_root {bad_root} to fail")
            self.assertTrue(any("must be a dictionary" in e for e in errors))

    def test_non_dict_entry_handled_gracefully(self):
        """Negative test: non-dict entry must return validation error tuple without raising AttributeError."""
        for bad_entry in ["invalid_str", 123, True, False, ["list"]]:
            valid, errors = validate_avatar_gallery_contract(entry=bad_entry)
            self.assertFalse(valid, f"Expected non-dict entry {bad_entry} to fail")
            self.assertTrue(any("must be a dictionary" in e for e in errors))

    def test_bare_https_and_invalid_avatar_urls(self):
        """Negative test: bare scheme 'https://', missing host, or invalid domains must fail validation."""
        invalid_urls = [
            "https://",
            "https://   ",
            "https:///",
            "https://localhost",
            "https://bad",
            "https://.com",
            "https://bad..com",
        ]
        for bad_url in invalid_urls:
            valid, errors = validate_avatar_gallery_contract(entry={"avatar": bad_url})
            self.assertFalse(valid, f"Expected invalid avatar URL '{bad_url}' to fail")
            self.assertTrue(any("must be an HTTPS URL" in e for e in errors))

    def test_alternate_avatars_invalid_urls(self):
        """Negative test: invalid or bare HTTPS URLs in alternate_avatars list must be caught."""
        entry = {
            "avatar": "https://imagedelivery.net/valid/public",
            "alternate_avatars": [
                "https://",
                "https://bad",
                123,
            ]
        }
        valid, errors = validate_avatar_gallery_contract(entry=entry)
        self.assertFalse(valid)
        self.assertEqual(len(errors), 3)

    def test_is_valid_https_url_helper(self):
        self.assertTrue(is_valid_https_url("https://imagedelivery.net/abc/123/public"))
        self.assertTrue(is_valid_https_url("https://ella.janitorai.com/bot-avatars/image.webp"))
        self.assertTrue(is_valid_https_url("https://io-modernfantasy.uwu.ai/avatar.png"))
        self.assertFalse(is_valid_https_url("https://"))
        self.assertFalse(is_valid_https_url("https://   "))
        self.assertFalse(is_valid_https_url("https:///"))
        self.assertFalse(is_valid_https_url("http://insecure.com/pic.jpg"))
        self.assertFalse(is_valid_https_url("https://localhost"))
        self.assertFalse(is_valid_https_url("https://bad"))
        self.assertFalse(is_valid_https_url(None))
        self.assertFalse(is_valid_https_url(123))


class TestModule93312CompilationLogic(unittest.TestCase):
    """
    Contract 3: Replicated Wyvern Module 93312 Compilation Logic & Regex Engine.
    Verifies that the Python implementation matches Module 93312 WH(npc_info, prefix, delimiter),
    implements stable weighting, Unicode NFC normalization, quote/hyphen classes, and duplicate surname avoidance.
    """

    def test_empty_first_name_returns_empty_regex(self):
        self.assertEqual(compile_wyvern_avatar_regex(None), "")
        self.assertEqual(compile_wyvern_avatar_regex({}), "")
        self.assertEqual(compile_wyvern_avatar_regex({"first_name": ""}), "")
        self.assertEqual(compile_wyvern_avatar_regex({"first_name": "   "}), "")

    def test_erik_douglas_exact_pattern_structure(self):
        erik = {
            "first_name": "Erik",
            "middle_names": ["Ulfr"],
            "last_name": "Douglas",
            "nicknames": ["The Old Wolf", "Pack Leader"],
            "titles": ["Lord", "Alpha"]
        }
        regex_str = compile_wyvern_avatar_regex(erik, prefix="", delimiter=":")
        self.assertTrue(regex_str.startswith(r"(?<=^|\n)\s*(?:\*\*)?"))
        self.assertIn("((Lord|Alpha)\\s+)?", regex_str)
        self.assertIn("(?<coreName>", regex_str)
        self.assertIn("Erik\\s+(Ulfr)\\s+Douglas", regex_str)
        self.assertIn("Douglas\\s+(Ulfr)\\s+Erik", regex_str)
        self.assertIn("'The Old Wolf'", regex_str)
        self.assertIn('"The Old Wolf"', regex_str)
        self.assertIn("Erik\\s+Douglas", regex_str)
        self.assertIn("Douglas\\s+Erik", regex_str)
        self.assertIn("(\\s+(Lord|Alpha))?", regex_str)
        self.assertTrue(regex_str.endswith(r"(?:\*\*)?\s*:(?:\*\*(?=\s|$))?"))

    def test_scarlett_rose_exact_pattern_structure(self):
        scarlett = {
            "first_name": "Scarlett",
            "last_name": "Rose",
            "nicknames": ["Red"]
        }
        regex_str = compile_wyvern_avatar_regex(scarlett, prefix="", delimiter=":")
        self.assertIn("(?<coreName>Scarlett\\s+Rose|Rose\\s+Scarlett|Scarlett|'Red'|\"Red\"|Rose|Red)", regex_str)
        self.assertTrue(regex_str.endswith(r"(?:\*\*)?\s*:(?:\*\*(?=\s|$))?"))

    def test_prefix_marker_lookbehind(self):
        # Empty prefix uses (?<=^|\n)\s*
        empty_pref_regex = compile_wyvern_avatar_regex({"first_name": "Sierra", "last_name": "Cruz"}, prefix="")
        self.assertTrue(empty_pref_regex.startswith(r"(?<=^|\n)\s*"))

        # Non-empty prefix uses (?:\*\*)?<prefix>\s*(?:\*\*)?(?<=^|[^\p{L}\p{N}_])
        custom_pref_regex = compile_wyvern_avatar_regex({"first_name": "Sierra", "last_name": "Cruz"}, prefix="=>")
        self.assertTrue(custom_pref_regex.startswith(r"(?:\*\*)?=>\s*(?:\*\*)?"))
        self.assertIn(r"(?<=^|[^\p{L}\p{N}_])(?<coreName>", custom_pref_regex)

    def test_custom_delimiter_handling(self):
        reg_pipe = compile_wyvern_avatar_regex({"first_name": "Sierra"}, delimiter="|")
        self.assertTrue(reg_pipe.endswith(r"(?:\*\*)?\s*\|(?:\*\*(?=\s|$))?"))

        reg_none = compile_wyvern_avatar_regex({"first_name": "Sierra"}, delimiter="")
        # Delimiter omitted when empty
        self.assertFalse(reg_none.endswith(r":(?:\*\*(?=\s|$))?"))

    def test_unicode_normalization_quotes_and_hyphens(self):
        escaped_quote = escape_wyvern("O'Connor")
        self.assertEqual(escaped_quote, "O['‘’ʼ‛′]Connor")

        escaped_hyphen = escape_wyvern("Jean-Luc")
        self.assertEqual(escaped_hyphen, "Jean[-‐‑‒–—−]Luc")

        curly_quote = escape_wyvern("“Quotes”")
        self.assertIn("Quotes", curly_quote)

    def test_normalize_wyvern_regex_pattern(self):
        self.assertEqual(normalize_wyvern_regex_pattern(r"Alpha\ Rivers\ Rivers"), "Alpha Rivers Rivers")
        self.assertEqual(normalize_wyvern_regex_pattern(r"Mr\.\ Rogers\ Rogers"), "Mr. Rogers Rogers")
        self.assertEqual(normalize_wyvern_regex_pattern(r"O['‘’ʼ‛′]Connor"), "O'Connor")
        self.assertEqual(normalize_wyvern_regex_pattern(r"Jean[-‐‑‒–—−]Luc"), "Jean-Luc")
        self.assertEqual(normalize_wyvern_regex_pattern(r"Hugh\s+Rivers"), "Hugh Rivers")
        self.assertEqual(normalize_wyvern_regex_pattern(""), "")
        self.assertEqual(normalize_wyvern_regex_pattern(None), "")

    def test_duplicate_surname_detector_flags_legacy_defects(self):
        defective_patterns = [
            (r"(?:^|\n)\s*(?:Alpha Rivers Rivers|The Mountain Sovereign Rivers)\s*:", "Rivers"),
            (r"(?:^|\n)\s*(?:Mr. Rogers Rogers|Dom Rogers Rogers)\s*:", "Rogers"),
            (r"(?:^|\n)\s*(?:Boone Boone)\s*:", "Boone"),
            (r"(?:^|\n)\s*(?:Councilman Black Black)\s*:", "Black"),
            (r"(?:^|\n)\s*(?:Mrs Virtuoso Virtuoso)\s*:", "Virtuoso"),
            (r"(?:^|\n)\s*(?:Bishop Bishop|The Hellhound Detective Bishop)\s*:", "Bishop"),
        ]
        for pattern, last_name in defective_patterns:
            detected = detect_duplicate_surnames(pattern, last_name)
            self.assertGreater(len(detected), 0, f"Expected duplicate surname detected in {pattern}")
            self.assertTrue(any(last_name.lower() in d.lower() for d in detected))

    def test_duplicate_surname_detector_flags_escaped_whitespace_defects(self):
        legacy_defective_cases = [
            (r"(?:^|\n)\s*(?:Alpha\ Rivers\ Rivers|Alpha\ Rivers)\s*:", "Rivers", "Rivers Rivers"),
            (r"(?:^|\n)\s*(?:Mr\.\ Rogers\ Rogers|Mr\.\ Rogers)\s*:", "Rogers", "Rogers Rogers"),
            (r"(?:^|\n)\s*(?:Boone\ Boone)\s*:", "Boone", "Boone Boone"),
            (r"(?:^|\n)\s*(?:Councilman\ Black\ Black)\s*:", "Black", "Black Black"),
            (r"(?:^|\n)\s*(?:O['‘’ʼ‛′]Connor\ O['‘’ʼ‛′]Connor)\s*:", "O'Connor", "O'Connor O'Connor"),
            (r"(?:^|\n)\s*(?:Mrs\ Virtuoso\ Virtuoso)\s*:", "Virtuoso", "Virtuoso Virtuoso"),
            (r"(?:^|\n)\s*(?:Nurse\ Cirillo\ Cirillo)\s*:", "Cirillo", "Cirillo Cirillo"),
            (r"(?:^|\n)\s*(?:Bishop\ Bishop)\s*:", "Bishop", "Bishop Bishop"),
            (r"(?:^|\n)\s*(?:Mr\.\ DeVille\ DeVille)\s*:", "DeVille", "DeVille DeVille"),
            (r"(?:^|\n)\s*(?:rat\ Rat)\s*:", "Rat", "Rat Rat"),
            (r"(?:^|\n)\s*(?:Professor\ Weiss\ Weiss)\s*:", "Weiss", "Weiss Weiss"),
            (r"(?:^|\n)\s*(?:Major\ Purcell\ Purcell)\s*:", "Purcell", "Purcell Purcell"),
            (r"Hugh\s+Rivers\s+Rivers", "Rivers", "Rivers Rivers"),
        ]
        for pattern, last_name, expected_dupe in legacy_defective_cases:
            detected = detect_duplicate_surnames(pattern, last_name)
            self.assertGreater(len(detected), 0, f"Expected duplicate surname detected in {pattern}")
            self.assertIn(expected_dupe, detected, f"Expected {expected_dupe} in detected: {detected}")

    def test_clean_patterns_have_zero_duplicate_surname_defects(self):
        clean_patterns = [
            (r"(?:^|\n)\s*(?:Alpha Rivers|The Mountain Sovereign)\s*:", "Rivers"),
            (r"(?:^|\n)\s*(?:Mr. Rogers|Dom Rogers)\s*:", "Rogers"),
            (r"(?:^|\n)\s*(?:Daniel Boone|Danny Boone)\s*:", "Boone"),
            (r"(?:^|\n)\s*(?:Councilman Black|Harrison Black)\s*:", "Black"),
            (r"(?:^|\n)\s*(?:Mrs Virtuoso|Alicia Virtuoso)\s*:", "Virtuoso"),
        ]
        for pattern, last_name in clean_patterns:
            detected = detect_duplicate_surnames(pattern, last_name)
            self.assertEqual(len(detected), 0, f"False positive duplicate surname in clean pattern: {pattern}")

    def test_clean_patterns_with_escaped_whitespace_have_zero_defects(self):
        clean_patterns = [
            (r"(?:^|\n)\s*(?:Alpha\ Rivers|The\ Mountain\ Sovereign)\s*:", "Rivers"),
            (r"(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers)\s*:", "Rogers"),
            (r"(?:^|\n)\s*(?:Daniel\ \"Danny\"\ Boone|Danny\ Boone)\s*:", "Boone"),
            (r"(?:^|\n)\s*(?:Mrs\ Virtuoso|Alicia\ Virtuoso)\s*:", "Virtuoso"),
            (r"(?:^|\n)\s*(?:Marcus\ O['‘’ʼ‛′]Connor|Oldtown)\s*:", "O'Connor"),
            (r"(?:^|\n)\s*(?:Mr\.\ DeVille|Alistair\ DeVille)\s*:", "DeVille"),
            (r"Hugh\s+Rivers", "Rivers"),
        ]
        for pattern, last_name in clean_patterns:
            detected = detect_duplicate_surnames(pattern, last_name)
            self.assertEqual(len(detected), 0, f"False positive duplicate surname in clean pattern: {pattern}")

    def test_replicated_compiler_produces_no_duplicate_surnames(self):
        npc = {
            "first_name": "Hugh",
            "last_name": "Rivers",
            "nicknames": ["Alpha Rivers", "The Mountain Sovereign"]
        }
        compiled = compile_wyvern_avatar_regex(npc)
        dupes = detect_duplicate_surnames(compiled, "Rivers")
        self.assertEqual(len(dupes), 0, f"Replicated compiler produced duplicate surname: {dupes}")

    def test_pcre_regex_execution_and_avatar_splitting(self):
        if pcre_regex is None:
            self.skipTest("pcre_regex module not available")

        scarlett = {"first_name": "Scarlett", "last_name": "Rose", "nicknames": ["Red"]}
        pattern_str = compile_wyvern_avatar_regex(scarlett)
        compiled_re = pcre_regex.compile(pattern_str, pcre_regex.IGNORECASE | pcre_regex.MULTILINE)

        # Dialogue cases that MUST match
        valid_turns = [
            'Scarlett Rose: "I knew you would come."',
            'Rose Scarlett: "Take a seat."',
            'Scarlett: "Are you ready?"',
            '**Scarlett Rose**: "Look at me."',
            'Red: "Do not underestimate me."',
            '"Red": "Let us begin."',
        ]
        for turn in valid_turns:
            match = compiled_re.search(turn)
            self.assertIsNotNone(match, f"Regex failed to match valid speaker turn: {turn}")
            self.assertIn("coreName", match.groupdict())

        # Dialogue cases that MUST NOT match
        invalid_turns = [
            'Someone else: "Hello Scarlett Rose."',
            'Narrator described Scarlett Rose in detail.',
            'The rose on the table was scarlet.',
        ]
        for turn in invalid_turns:
            match = compiled_re.search(turn)
            self.assertIsNone(match, f"Regex erroneously matched non-speaker text: {turn}")


class TestAntiCollisionContract(unittest.TestCase):
    """
    Contract 4: Anti-Collision Preservation (`ignored_characters` & `ignored_personas`).
    Verifies that Character Card IDs and User Persona IDs are preserved,
    preventing duplicate bot injection in Wyvern scenarios.
    """

    def test_valid_anti_collision_entry_passes(self):
        entry = {
            "name": "Wulfnic Báleygr Bloodmoon",
            "ignored_characters": ["_HEQQbbRFwKdG8QE2Fh1z1"],
            "ignored_personas": [],
            "selective": False,
            "secondary_keys": []
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertTrue(valid, f"Expected valid anti-collision entry, got: {errors}")

    def test_valid_dual_persona_entry_passes(self):
        # Alyssa / Jasper have selective: true with secondary_keys
        entry = {
            "name": "Alyssa Hvit Douglas Bloodmoon",
            "ignored_characters": ["alyssa_world_dossier_2b54a223"],
            "ignored_personas": ["persona_1786335754946"],
            "selective": True,
            "secondary_keys": ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertTrue(valid, f"Expected valid dual-mode persona entry, got: {errors}")

    def test_ignored_characters_non_list_fails(self):
        entry = {"ignored_characters": "_HEQQbbRFwKdG8QE2Fh1z1"}
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("'ignored_characters' must be a list" in e for e in errors))

    def test_ignored_characters_non_string_elements_fails(self):
        entry = {"ignored_characters": [123, 456]}
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("must be a string card ID" in e for e in errors))

    def test_ignored_personas_non_list_fails(self):
        entry = {"ignored_personas": "persona_1786335754946"}
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("'ignored_personas' must be a list" in e for e in errors))

    def test_ignored_personas_non_string_elements_fails(self):
        entry = {"ignored_personas": [True]}
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("must be a string persona ID" in e for e in errors))

    def test_selective_true_without_secondary_keys_fails(self):
        entry = {
            "name": "Invalid Selective NPC",
            "selective": True,
            "secondary_keys": []
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("selective: true' but 'secondary_keys' is empty" in e for e in errors))

    def test_broad_umbrella_keys_in_keys_fails(self):
        """Rejects broad umbrella keywords in primary keys (GEMINI.md §7)."""
        entry = {
            "name": "Hugh Rivers",
            "keys": ["Hugh Rivers", "Alpha", "werewolf", "solarton"],
            "selective": False,
            "secondary_keys": []
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("Prohibited broad umbrella keyword 'Alpha' found in 'keys'" in e for e in errors))
        self.assertTrue(any("Prohibited broad umbrella keyword 'werewolf' found in 'keys'" in e for e in errors))
        self.assertTrue(any("Prohibited broad umbrella keyword 'solarton' found in 'keys'" in e for e in errors))

    def test_broad_umbrella_keys_in_secondary_keys_fails(self):
        """Rejects broad umbrella keywords in secondary_keys (GEMINI.md §7)."""
        entry = {
            "name": "Damien Bishop",
            "keys": ["Damien", "Bishop"],
            "selective": False,
            "secondary_keys": ["detective", "demon", "horns"]
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("Prohibited broad umbrella keyword 'demon' found in 'secondary_keys'" in e for e in errors))

    def test_broad_umbrella_keys_in_nicknames_fails(self):
        """Rejects broad umbrella keywords in top-level nicknames and npc_info.nicknames."""
        entry = {
            "name": "Student NPC",
            "keys": ["Student NPC"],
            "nicknames": ["student", "Freshman"],
            "npc_info": {
                "first_name": "Test",
                "nicknames": ["college"]
            }
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("Prohibited broad umbrella keyword 'student' found in 'nicknames'" in e for e in errors))
        self.assertTrue(any("Prohibited broad umbrella keyword 'college' found in 'npc_info.nicknames'" in e for e in errors))

    def test_compound_names_containing_broad_substrings_pass(self):
        """Ensures exact matching prevents false positives on legitimate compound proper names."""
        entry = {
            "name": "Roman Blackwood",
            "keys": ["Roman Blackwood", "Roman", "Alpha Rivers", "Douglas Pack"],
            "secondary_keys": ["Blackwood Heir", "Alpha of the Douglas Pack"],
            "selective": False
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertTrue(valid, f"False positive rejection of valid compound names: {errors}")
        self.assertEqual(len(errors), 0)

    def test_case_insensitive_and_whitespace_broad_keys_matching(self):
        """Verifies case-insensitive and stripped matching for broad keys."""
        for raw_key in ["  ALPHA  ", "sUcC", "WEREWOLF", "Demihuman", "demi-human"]:
            entry = {"keys": [raw_key]}
            valid, errors = validate_anti_collision_contract(entry)
            self.assertFalse(valid, f"Expected {repr(raw_key)} to be caught")
            self.assertTrue(any("Prohibited broad umbrella keyword" in e for e in errors))

    def test_malformed_keys_and_nicknames_types_fail(self):
        """Verifies type safety for keys and nicknames."""
        entry_str_keys = {"keys": "NotAList"}
        valid, errors = validate_anti_collision_contract(entry_str_keys)
        self.assertFalse(valid)
        self.assertTrue(any("'keys' must be a list" in e for e in errors))

        entry_bad_elem = {"keys": ["Valid", 123]}
        valid, errors = validate_anti_collision_contract(entry_bad_elem)
        self.assertFalse(valid)
        self.assertTrue(any("'keys[1]' must be a string" in e for e in errors))

    def test_non_dict_entry_anti_collision_handled_gracefully(self):
        """Negative test: non-dict entry must return validation error tuple without crashing."""
        for bad_entry in ["not_a_dict", 123, None, [1, 2]]:
            valid, errors = validate_anti_collision_contract(bad_entry)
            self.assertFalse(valid)
            self.assertTrue(any("must be a dictionary" in e for e in errors))


class TestEntriesLexiconParityContract(unittest.TestCase):
    """
    Contract 5: Byte-for-Byte Parity Between `entries` and `lexicon`.
    Verifies that lorebook['entries'] and lorebook['lexicon'] maintain 100% byte-for-byte equality.
    """

    def test_identical_arrays_pass_parity(self):
        entry_a = {"id": "1", "name": "Erik Douglas", "content": "JED+ Description"}
        entry_b = {"id": "2", "name": "Scarlett Rose", "content": "JED+ Description"}
        lorebook = {
            "entries": [entry_a, entry_b],
            "lexicon": [entry_a, entry_b]
        }
        valid, errors = validate_entries_lexicon_parity(lorebook)
        self.assertTrue(valid, f"Expected identical arrays to pass parity: {errors}")
        self.assertEqual(len(errors), 0)

    def test_length_mismatch_fails_parity(self):
        lorebook = {
            "entries": [{"id": "1"}],
            "lexicon": [{"id": "1"}, {"id": "2"}]
        }
        valid, errors = validate_entries_lexicon_parity(lorebook)
        self.assertFalse(valid)
        self.assertTrue(any("Length mismatch" in e for e in errors))

    def test_content_difference_fails_parity(self):
        lorebook = {
            "entries": [{"id": "1", "name": "Erik"}],
            "lexicon": [{"id": "1", "name": "Erik Modified"}]
        }
        valid, errors = validate_entries_lexicon_parity(lorebook)
        self.assertFalse(valid)
        self.assertTrue(any("Byte-for-byte mismatch" in e for e in errors))

    def test_missing_array_fails_parity(self):
        valid, errors = validate_entries_lexicon_parity({"entries": []})
        self.assertFalse(valid)
        self.assertTrue(any("missing 'lexicon'" in e for e in errors))

        valid, errors = validate_entries_lexicon_parity({"lexicon": []})
        self.assertFalse(valid)
        self.assertTrue(any("missing 'entries'" in e for e in errors))

    def test_non_dict_lorebook_data_parity_handled_gracefully(self):
        """Negative test: non-dict lorebook_data must return validation error tuple without raising TypeError."""
        for bad_data in [456, "string_data", True, False, None, [1, 2]]:
            valid, errors = validate_entries_lexicon_parity(bad_data)
            self.assertFalse(valid, f"Expected non-dict lorebook_data {bad_data} to fail")
            self.assertTrue(any("must be a dictionary" in e for e in errors))

    def test_real_repository_primary_and_secondary_parity(self):
        # Verify that existing repository files maintain entries == lexicon parity
        primary_path = REPO_ROOT / "FINAL" / "Svartulfr_NPC_Primary.json"
        secondary_path = REPO_ROOT / "FINAL" / "Svartulfr_NPC_Secondary.json"

        if primary_path.exists():
            with open(primary_path, "r", encoding="utf-8") as f:
                primary_data = json.load(f)
            valid, errors = validate_entries_lexicon_parity(primary_data)
            self.assertTrue(valid, f"Parity failure in {primary_path}: {errors}")

        if secondary_path.exists():
            with open(secondary_path, "r", encoding="utf-8") as f:
                secondary_data = json.load(f)
            valid, errors = validate_entries_lexicon_parity(secondary_data)
            self.assertTrue(valid, f"Parity failure in {secondary_path}: {errors}")


if __name__ == "__main__":
    unittest.main()
