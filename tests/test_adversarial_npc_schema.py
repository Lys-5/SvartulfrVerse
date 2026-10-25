#!/usr/bin/env python3
"""
tests/test_adversarial_npc_schema.py

Adversarial Stress Harness challenging scripts/verify_npc_schema_contract.py:
1. Invalid npc_info schemas (missing required fields, bad types, malformed lists).
2. Invalid avatar gallery structures (bad URL schemes, gallery_count mismatches, boolean types, non-HTTPS).
3. Anti-collision violations (selective without secondary_keys, broad umbrella keys, non-string IDs).
4. Parity violations (single-character diffs, length mismatches, key differences, element order).
5. Robustness & edge cases (non-dict inputs, nulls, booleans as ints, empty strings).
"""

import json
import sys
import unittest
from pathlib import Path

# Add repo root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.verify_npc_schema_contract import (
    validate_npc_info_schema,
    validate_avatar_gallery_contract,
    validate_anti_collision_contract,
    validate_entries_lexicon_parity,
    compile_wyvern_avatar_regex,
    detect_duplicate_surnames,
)

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "losangeles", "underworld",
    "vampire", "werewolf", "human", "demihuman", "demon",
    "college", "student", "alpha", "beta", "omega", "pack"
}


class AdversarialNpcInfoTests(unittest.TestCase):
    """Adversarial stress testing of validate_npc_info_schema."""

    def test_missing_first_name_adversarial(self):
        cases = [
            {},
            {"middle_names": [], "last_name": "Douglas"},
            {"titles": ["Lord"], "nicknames": ["Wolf"]},
        ]
        for case in cases:
            valid, errs = validate_npc_info_schema(case)
            self.assertFalse(valid, f"Expected invalid for missing first_name: {case}")
            self.assertTrue(any("first_name is required" in e for e in errs))

    def test_empty_whitespace_first_name_adversarial(self):
        cases = ["", " ", "   ", "\t", "\n", "\r\n", " \t \n "]
        for val in cases:
            valid, errs = validate_npc_info_schema({"first_name": val})
            self.assertFalse(valid, f"Expected invalid for whitespace first_name: repr({val})")
            self.assertTrue(any("cannot be empty or whitespace" in e for e in errs))

    def test_invalid_types_first_name(self):
        cases = [123, 0, -1, 3.14, True, False, [], ["Erik"], {}, {"name": "Erik"}]
        for val in cases:
            valid, errs = validate_npc_info_schema({"first_name": val})
            self.assertFalse(valid, f"Expected invalid for non-string first_name: {type(val)}")
            self.assertTrue(any("must be a string" in e for e in errs))

    def test_invalid_middle_names_structure(self):
        # Strings, numbers, dicts instead of list
        cases = ["Ulfr", "Ulfr, Douglas", 123, True, {"middle": "Ulfr"}]
        for val in cases:
            valid, errs = validate_npc_info_schema({"first_name": "Erik", "middle_names": val})
            self.assertFalse(valid, f"Expected invalid for non-list middle_names: {type(val)}")
            self.assertTrue(any("must be a list of strings" in e for e in errs))

    def test_invalid_middle_names_elements(self):
        # List containing non-string elements
        cases = [
            [123],
            ["Ulfr", 456],
            [None],
            ["Ulfr", None],
            [True],
            [False],
            [[]],
            [{"name": "Ulfr"}],
        ]
        for val in cases:
            valid, errs = validate_npc_info_schema({"first_name": "Erik", "middle_names": val})
            self.assertFalse(valid, f"Expected invalid for non-string element in middle_names: {val}")
            self.assertTrue(any("must be a string" in e for e in errs))

    def test_invalid_last_name_types(self):
        cases = [123, True, False, [], ["Douglas"], {"last": "Douglas"}]
        for val in cases:
            valid, errs = validate_npc_info_schema({"first_name": "Erik", "last_name": val})
            self.assertFalse(valid, f"Expected invalid for non-string last_name: {type(val)}")
            self.assertTrue(any("last_name must be a string or None" in e for e in errs))

    def test_invalid_nicknames_and_titles(self):
        for field_name in ["nicknames", "titles"]:
            # Non-list
            for bad_val in ["StringVal", 123, True, {}]:
                valid, errs = validate_npc_info_schema({"first_name": "Erik", field_name: bad_val})
                self.assertFalse(valid, f"Expected invalid for non-list {field_name}")
                self.assertTrue(any(f"{field_name} must be a list of strings" in e for e in errs))
            # List with bad elements
            for bad_elem in [123, None, True, []]:
                valid, errs = validate_npc_info_schema({"first_name": "Erik", field_name: [bad_elem]})
                self.assertFalse(valid, f"Expected invalid for bad element in {field_name}")
                self.assertTrue(any(f"{field_name}[0] must be a string" in e for e in errs))

    def test_invalid_npc_prefix_types(self):
        cases = [123, True, False, [], ["prefix"], {"p": "pre"}]
        for val in cases:
            valid, errs = validate_npc_info_schema({"first_name": "Erik", "npc_prefix": val})
            self.assertFalse(valid, f"Expected invalid for non-string npc_prefix: {type(val)}")
            self.assertTrue(any("npc_prefix must be a string or None" in e for e in errs))

    def test_non_dict_payload_adversarial(self):
        cases = ["string_payload", 123, 4.5, True, False, None, [], [1, 2, 3]]
        for val in cases:
            valid, errs = validate_npc_info_schema(val)
            self.assertFalse(valid, f"Expected non-dict payload to fail: {type(val)}")
            self.assertTrue(any("must be a dictionary" in e for e in errs))

    def test_zero_false_positives_valid_schemas(self):
        valid_cases = [
            {"first_name": "Erik", "middle_names": ["Ulfr"]},
            {"first_name": "Scarlett", "middle_names": [], "last_name": "Rose"},
            {"first_name": "Alyssa", "middle_names": ["Hvit"], "last_name": "Douglas Bloodmoon", "nicknames": ["Lys"], "titles": ["Healer"], "npc_prefix": ""},
            {"first_name": "Bruce", "middle_names": [], "last_name": None, "nicknames": [], "titles": ["President"], "npc_prefix": None},
            {"first_name": "Sierra", "middle_names": [], "last_name": "Cruz", "nicknames": ["Rainbow Lamia"], "titles": [], "npc_prefix": "=>"},
        ]
        for vc in valid_cases:
            valid, errs = validate_npc_info_schema(vc)
            self.assertTrue(valid, f"Valid case rejected: {vc}, errors: {errs}")
            self.assertEqual(len(errs), 0)


class AdversarialAvatarGalleryTests(unittest.TestCase):
    """Adversarial stress testing of validate_avatar_gallery_contract."""

    def test_lorebook_root_missing_fields(self):
        cases = [
            ({}, "missing 'gallery'"),
            ({"gallery": []}, "missing 'gallery_count'"),
            ({"gallery_count": 0}, "missing 'gallery'"),
        ]
        for root, err_sub in cases:
            valid, errs = validate_avatar_gallery_contract(lorebook_root=root)
            self.assertFalse(valid, f"Expected root {root} to fail")
            self.assertTrue(any(err_sub in e for e in errs), f"Expected '{err_sub}' in {errs}")

    def test_lorebook_root_invalid_gallery_types(self):
        cases = ["not_a_list", 123, True, False, {"a": 1}]
        for val in cases:
            valid, errs = validate_avatar_gallery_contract(lorebook_root={"gallery": val, "gallery_count": 0})
            self.assertFalse(valid, f"Expected non-list gallery to fail: {type(val)}")
            self.assertTrue(any("'gallery' must be a list" in e for e in errs))

    def test_lorebook_root_invalid_gallery_count(self):
        # Negative count
        valid, errs = validate_avatar_gallery_contract(lorebook_root={"gallery": [], "gallery_count": -1})
        self.assertFalse(valid)
        self.assertTrue(any("non-negative integer" in e for e in errs))

        # String count
        valid, errs = validate_avatar_gallery_contract(lorebook_root={"gallery": [], "gallery_count": "0"})
        self.assertFalse(valid)
        self.assertTrue(any("non-negative integer" in e for e in errs))

        # Float count
        valid, errs = validate_avatar_gallery_contract(lorebook_root={"gallery": [], "gallery_count": 0.0})
        self.assertFalse(valid)
        self.assertTrue(any("non-negative integer" in e for e in errs))

        # Count mismatch
        valid, errs = validate_avatar_gallery_contract(lorebook_root={"gallery": [{"id": 1}], "gallery_count": 0})
        self.assertFalse(valid)
        self.assertTrue(any("does not match len(gallery)" in e for e in errs))

        valid, errs = validate_avatar_gallery_contract(lorebook_root={"gallery": [], "gallery_count": 2})
        self.assertFalse(valid)
        self.assertTrue(any("does not match len(gallery)" in e for e in errs))

    def test_lorebook_root_boolean_gallery_count_false_negative(self):
        """
        Adversarial test: in Python, bool is a subclass of int (isinstance(True, int) is True).
        A gallery with 1 item and gallery_count=True (bool) might bypass integer checks.
        """
        root_with_bool = {"gallery": [{"id": 1}], "gallery_count": True}
        valid, errs = validate_avatar_gallery_contract(lorebook_root=root_with_bool)
        self.assertFalse(valid, "gallery_count=True must be rejected as invalid integer")
        self.assertTrue(any("must be a non-negative integer, got bool" in e for e in errs))

    def test_entry_avatar_bad_schemes_and_protocols(self):
        adversarial_urls = [
            "http://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/pic/public",
            "ftp://files.example.com/avatar.png",
            "file:///C:/Users/avatar.png",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
            "javascript:alert('xss')",
            "gopher://gopher.floodgap.com/avatar",
            "ws://live.chat/avatar",
            "blob:https://app.wyvern.chat/38b81ce2-4e8c-4f8e",
            "//imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/pic/public",
            "avatar.png",
            "/static/avatar.png",
        ]
        for bad_url in adversarial_urls:
            entry = {"avatar": bad_url}
            valid, errs = validate_avatar_gallery_contract(entry=entry)
            self.assertFalse(valid, f"Expected non-HTTPS URL {bad_url} to fail")
            self.assertTrue(any("must be an HTTPS URL" in e for e in errs), f"Error didn't mention HTTPS URL: {errs}")

    def test_entry_avatar_empty_and_null(self):
        cases = [
            {},
            {"avatar": ""},
            {"avatar": "   "},
            {"avatar": None},
            {"avatar": False},
            {"avatar": 12345},
            {"avatar": ["https://imagedelivery.net/pic.png"]},
        ]
        for c in cases:
            valid, errs = validate_avatar_gallery_contract(entry=c)
            self.assertFalse(valid, f"Expected avatar case to fail: {c}")

    def test_alternate_avatars_adversarial(self):
        # Non-list
        valid, errs = validate_avatar_gallery_contract(entry={
            "avatar": "https://imagedelivery.net/pic.png",
            "alternate_avatars": "https://imagedelivery.net/alt.png"
        })
        self.assertFalse(valid)
        self.assertTrue(any("'alternate_avatars' must be a list" in e for e in errs))

        # Mixed valid and invalid
        valid, errs = validate_avatar_gallery_contract(entry={
            "avatar": "https://imagedelivery.net/pic.png",
            "alternate_avatars": [
                "https://imagedelivery.net/alt1.png",
                "http://insecure.net/alt2.png",
                123,
                None,
            ]
        })
        self.assertFalse(valid)
        self.assertEqual(len(errs), 3)  # 3 invalid items in alternate_avatars

    def test_entry_avatar_bare_https_scheme(self):
        """Adversarial test: avatar='https://' has no host or path."""
        entry = {"avatar": "https://"}
        valid, errs = validate_avatar_gallery_contract(entry=entry)
        self.assertFalse(valid, "avatar='https://' bare scheme must be rejected")
        self.assertTrue(any("must be an HTTPS URL with a valid domain and path" in e for e in errs))


class AdversarialAntiCollisionTests(unittest.TestCase):
    """Adversarial stress testing of validate_anti_collision_contract."""

    def test_ignored_characters_malformed(self):
        bad_types = ["_HEQQbbRFwKdG8QE2Fh1z1", 123, True, {"id": "1"}]
        for bt in bad_types:
            valid, errs = validate_anti_collision_contract({"ignored_characters": bt})
            self.assertFalse(valid, f"Expected non-list ignored_characters to fail: {type(bt)}")
            self.assertTrue(any("'ignored_characters' must be a list" in e for e in errs))

        bad_elements = [
            [123],
            ["_VALID_ID", None],
            ["_VALID_ID", True],
            ["_VALID_ID", []],
        ]
        for be in bad_elements:
            valid, errs = validate_anti_collision_contract({"ignored_characters": be})
            self.assertFalse(valid, f"Expected non-string element in ignored_characters to fail: {be}")
            self.assertTrue(any("must be a string card ID" in e for e in errs))

    def test_ignored_personas_malformed(self):
        bad_types = ["persona_1786335754946", 123, False, {}]
        for bt in bad_types:
            valid, errs = validate_anti_collision_contract({"ignored_personas": bt})
            self.assertFalse(valid, f"Expected non-list ignored_personas to fail: {type(bt)}")
            self.assertTrue(any("'ignored_personas' must be a list" in e for e in errs))

        bad_elements = [
            [123],
            ["persona_123", False],
            ["persona_123", None],
        ]
        for be in bad_elements:
            valid, errs = validate_anti_collision_contract({"ignored_personas": be})
            self.assertFalse(valid, f"Expected non-string element in ignored_personas to fail: {be}")
            self.assertTrue(any("must be a string persona ID" in e for e in errs))

    def test_selective_true_without_secondary_keys(self):
        cases = [
            {"selective": True},
            {"selective": True, "secondary_keys": []},
        ]
        for c in cases:
            valid, errs = validate_anti_collision_contract(c)
            self.assertFalse(valid, f"Expected selective: True without secondary_keys to fail: {c}")
            self.assertTrue(any("selective: true' but 'secondary_keys' is empty" in e for e in errs))

    def test_secondary_keys_non_list(self):
        for bad_val in ["Dossier", 123, True, {}]:
            valid, errs = validate_anti_collision_contract({"selective": False, "secondary_keys": bad_val})
            self.assertFalse(valid, f"Expected non-list secondary_keys to fail: {type(bad_val)}")
            self.assertTrue(any("'secondary_keys' must be a list" in e for e in errs))

    def test_broad_umbrella_keys_vulnerability(self):
        """
        Adversarial test: checks whether validate_anti_collision_contract detects
        umbrella keywords (BROAD_KEYS: 'solarton', 'succ', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega').
        GEMINI.md §7 mandates zero umbrella keywords on NPC entries.
        """
        entry_with_broad_keys = {
            "name": "Hugh Rivers",
            "type": "npc",
            "keys": ["alpha", "werewolf", "solarton"],
            "selective": False,
            "secondary_keys": [],
            "ignored_characters": [],
            "ignored_personas": [],
        }
        valid, errs = validate_anti_collision_contract(entry_with_broad_keys)
        self.assertFalse(valid, "BROAD_KEYS must be rejected in keys")
        self.assertTrue(any("Prohibited broad umbrella keyword" in e for e in errs))


class AdversarialParityTests(unittest.TestCase):
    """Adversarial stress testing of validate_entries_lexicon_parity."""

    def test_missing_entries_or_lexicon(self):
        valid, errs = validate_entries_lexicon_parity({})
        self.assertFalse(valid)
        self.assertEqual(len(errs), 2)

        valid, errs = validate_entries_lexicon_parity({"entries": []})
        self.assertFalse(valid)
        self.assertTrue(any("missing 'lexicon'" in e for e in errs))

        valid, errs = validate_entries_lexicon_parity({"lexicon": []})
        self.assertFalse(valid)
        self.assertTrue(any("missing 'entries'" in e for e in errs))

    def test_non_list_entries_or_lexicon(self):
        valid, errs = validate_entries_lexicon_parity({"entries": "not_list", "lexicon": []})
        self.assertFalse(valid)
        self.assertTrue(any("'entries' must be a list" in e for e in errs))

        valid, errs = validate_entries_lexicon_parity({"entries": [], "lexicon": "not_list"})
        self.assertFalse(valid)
        self.assertTrue(any("'lexicon' must be a list" in e for e in errs))

    def test_length_mismatch(self):
        cases = [
            ({"entries": [{}], "lexicon": []}, 1, 0),
            ({"entries": [], "lexicon": [{}]}, 0, 1),
            ({"entries": [{"id": 1}, {"id": 2}], "lexicon": [{"id": 1}]}, 2, 1),
        ]
        for data, l_ent, l_lex in cases:
            valid, errs = validate_entries_lexicon_parity(data)
            self.assertFalse(valid)
            self.assertTrue(any(f"Length mismatch: entries has {l_ent} items, lexicon has {l_lex} items" in e for e in errs))

    def test_single_character_content_diff_fails_loudly(self):
        item_base = {"id": "1", "name": "Erik Douglas", "content": "JED+ Description with full detail."}
        item_mutated = {"id": "1", "name": "Erik Douglas", "content": "JED+ Description with full detail!"}  # period -> exclamation
        data = {
            "entries": [item_base],
            "lexicon": [item_mutated],
        }
        valid, errs = validate_entries_lexicon_parity(data)
        self.assertFalse(valid, "Expected 1-character content divergence to fail parity")
        self.assertTrue(any("Byte-for-byte mismatch" in e for e in errs))
        self.assertTrue(any("First mismatch at entry index 0 ('Erik Douglas')" in e for e in errs))

    def test_single_character_name_diff_fails_loudly(self):
        item_base = {"id": "1", "name": "Erik Douglas", "content": "Desc"}
        item_mutated = {"id": "1", "name": "Eric Douglas", "content": "Desc"}  # k -> c
        data = {
            "entries": [item_base],
            "lexicon": [item_mutated],
        }
        valid, errs = validate_entries_lexicon_parity(data)
        self.assertFalse(valid)
        self.assertTrue(any("Byte-for-byte mismatch" in e for e in errs))

    def test_boolean_flag_flip_fails_loudly(self):
        item_base = {"id": "1", "name": "Test", "selective": False}
        item_mutated = {"id": "1", "name": "Test", "selective": True}
        data = {
            "entries": [item_base],
            "lexicon": [item_mutated],
        }
        valid, errs = validate_entries_lexicon_parity(data)
        self.assertFalse(valid)
        self.assertTrue(any("Byte-for-byte mismatch" in e for e in errs))

    def test_array_element_order_reversal_fails_loudly(self):
        item_a = {"id": "1", "name": "Erik"}
        item_b = {"id": "2", "name": "Scarlett"}
        data = {
            "entries": [item_a, item_b],
            "lexicon": [item_b, item_a],
        }
        valid, errs = validate_entries_lexicon_parity(data)
        self.assertFalse(valid, "Reordered arrays must fail parity")
        self.assertTrue(any("Byte-for-byte mismatch" in e for e in errs))

    def test_nested_attribute_divergence_fails_loudly(self):
        item_base = {
            "id": "1",
            "name": "Erik",
            "npc_info": {"first_name": "Erik", "middle_names": ["Ulfr"]}
        }
        item_mutated = {
            "id": "1",
            "name": "Erik",
            "npc_info": {"first_name": "Erik", "middle_names": ["Ulfr", "Jarn"]}
        }
        data = {
            "entries": [item_base],
            "lexicon": [item_mutated]
        }
        valid, errs = validate_entries_lexicon_parity(data)
        self.assertFalse(valid)
        self.assertTrue(any("Byte-for-byte mismatch" in e for e in errs))


class RobustnessCrashTests(unittest.TestCase):
    """Tests for unexpected exceptions and edge-case crash conditions."""

    def test_non_dict_entry_to_avatar_validator_crashes(self):
        """
        Adversarial test: non-dict entry passed to validate_avatar_gallery_contract
        must return (False, errors) without raising AttributeError.
        """
        valid, errs = validate_avatar_gallery_contract(entry="not_a_dict")
        self.assertFalse(valid)
        self.assertTrue(any("must be a dictionary" in e for e in errs))

    def test_non_dict_lorebook_root_to_avatar_validator_crashes(self):
        """
        Adversarial test: non-dict root passed to validate_avatar_gallery_contract
        must return (False, errors) without raising TypeError.
        """
        valid, errs = validate_avatar_gallery_contract(lorebook_root=123)
        self.assertFalse(valid)
        self.assertTrue(any("must be a dictionary" in e for e in errs))

    def test_non_dict_to_parity_validator_crashes(self):
        """
        Adversarial test: non-dict lorebook_data passed to validate_entries_lexicon_parity
        must return (False, errors) without raising TypeError.
        """
        valid, errs = validate_entries_lexicon_parity(456)
        self.assertFalse(valid)
        self.assertTrue(any("must be a dictionary" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
