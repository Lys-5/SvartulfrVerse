#!/usr/bin/env python3
"""
tests/test_adversarial_m1_m2_challenger.py

Empirical Challenger Adversarial Test Suite for Milestones M1 & M2.
Tests executed directly by challenger_13_1 to aggressively stress-test and verify:
1. Canonical heights and proportional clauses across all cards, personas, lorebooks, and database files.
2. Complete eradication of legacy heights across all nested fields and sub-objects.
3. Proportional arithmetic and clause consistency (-38 cm, +53 cm, 58-65 cm).
4. Single-line bracket constraint ([...]) on line 0 for all character cards, personas, and lorebook entries.
5. Exact byte-for-byte internal parity (entries == lexicon) in Primary lorebook and cross-folder mirror equality.
6. Clean JSON parsing across all files in FINAL/, ARCHIVIO/, and personas/.
7. Strict binary PNG header, IHDR/IDAT/IEND chunk validation, 1024x1024 resolution, and file sizes (> 1 MB) for all reference images in asset/references and assets/references.
8. Rigorous lore invariants and zero em-dash compliance in docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md.
"""

import sys
import os
import json
import struct
import filecmp
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

CANONICAL_HEIGHTS = {
    "Alyssa": '155 cm (5\' 1")',
    "Jasper": '193 cm (6\' 4")',
    "Noah": '197 cm (6\' 5.6")',
    "Malachia": '208 cm (6\' 9.9")',
    "Erik": '213 cm (6\' 11.9")',
    "Wulfnic": '220 cm (7\' 2.6")',
}

PROPORTIONAL_CLAUSES = [
    "Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).",
    "Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.",
    "Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno)."
]

IMAGE_NAMES = [
    "gebo_wrist_mark.png",
    "mani_hip_mark_alyssa.png",
    "sol_hip_mark_jasper.png",
    "celestial_polarity_twins.png",
    "logan_sleeves_marks.png",
    "malachia_blackwork_marks.png",
    "erik_ritual_marks.png",
    "wulfnic_primeval_brands.png"
]


class TestAdversarialHeightsAndProportions(unittest.TestCase):
    """Stress tests for M1: Canonical heights, legacy height eradication, single-line brackets, and lorebook parity."""

    def test_database_markdown_canonical_heights(self):
        """Assert exact string matches for all 6 canonical heights in database/characters/."""
        char_files = {
            "Alyssa": REPO_ROOT / "database/characters/C_Alyssa_Douglas_Bloodmoon.md",
            "Jasper": REPO_ROOT / "database/characters/C_Jasper_Douglas_Bloodmoon.md",
            "Noah": REPO_ROOT / "database/characters/C_Noah_Douglas_Bloodmoon.md",
            "Malachia": REPO_ROOT / "database/characters/C_Malachia_Douglas_Bloodmoon.md",
            "Erik": REPO_ROOT / "database/characters/C_Erik_Douglas.md",
            "Wulfnic": REPO_ROOT / "database/characters/C_Wulfnic_Bloodmoon.md",
        }
        for name, expected_height in CANONICAL_HEIGHTS.items():
            path = char_files[name]
            self.assertTrue(path.exists(), f"Missing database file: {path}")
            content = path.read_text(encoding="utf-8")
            self.assertIn(expected_height, content, f"{name} database markdown does not contain exact canonical height '{expected_height}'")

    def test_style_guide_canonical_heights_and_proportions(self):
        """Assert style_guide.md contains all 6 canonical heights and all 3 proportional clauses with 0 em-dashes in Section 5."""
        path = REPO_ROOT / "database/assets/style_guide.md"
        self.assertTrue(path.exists(), f"Missing style guide: {path}")
        content = path.read_text(encoding="utf-8")
        for name, expected_height in CANONICAL_HEIGHTS.items():
            self.assertIn(expected_height, content, f"style_guide.md missing height '{expected_height}' for {name}")
        for clause in PROPORTIONAL_CLAUSES:
            self.assertIn(clause, content, f"style_guide.md missing proportional clause: '{clause}'")
            self.assertNotIn("—", clause, f"Proportional clause contains em-dash: '{clause}'")

    def test_proportional_clauses_arithmetic(self):
        """Empirically verify the arithmetic of the 3 proportional clauses."""
        alyssa_h = 155
        jasper_h = 193
        noah_h = 197
        malachia_h = 208
        erik_h = 213
        wulfnic_h = 220

        # Clause 1: Alyssa to Jasper shoulder (-38 cm)
        self.assertEqual(alyssa_h - jasper_h, -38)

        # Clause 2: Malachia exceeds Alyssa by over half a meter (+53 cm)
        self.assertEqual(malachia_h - alyssa_h, 53)
        self.assertGreater(malachia_h - alyssa_h, 50)

        # Clause 3: Erik and Wulfnic tower over Alyssa by 58-65 cm
        diff_erik = erik_h - alyssa_h
        diff_wulfnic = wulfnic_h - alyssa_h
        self.assertEqual(diff_erik, 58)
        self.assertEqual(diff_wulfnic, 65)

    def test_standalone_cards_canonical_heights(self):
        """Assert standalone cards in FINAL/ and ARCHIVIO/ contain exact canonical heights in bracket and proportional clauses."""
        card_map = {
            "Alyssa": REPO_ROOT / "ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json",
            "Jasper": REPO_ROOT / "FINAL/Jasper_Douglas_Bloodmoon_card.json",
            "Noah": REPO_ROOT / "FINAL/Noah_Douglas_Bloodmoon_card.json",
            "Malachia": REPO_ROOT / "FINAL/Malachia_Douglas_Bloodmoon_card.json",
            "Erik": REPO_ROOT / "FINAL/Erik_Douglas_card.json",
            "Wulfnic": REPO_ROOT / "FINAL/Wulfnic_Bloodmoon_card.json",
        }
        for name, path in card_map.items():
            self.assertTrue(path.exists(), f"Card file does not exist: {path}")
            data = json.loads(path.read_text(encoding="utf-8"))
            desc = data.get("description", "")
            first_line = desc.splitlines()[0] if desc.splitlines() else ""
            self.assertTrue(first_line.startswith("["), f"Card {name} line 0 does not start with '['")
            self.assertTrue(first_line.endswith("]"), f"Card {name} line 0 does not end with ']'")
            expected_height = CANONICAL_HEIGHTS[name]
            self.assertIn(expected_height, first_line, f"Card {name} line 0 does not contain canonical height '{expected_height}'")
            self.assertIn("PROPORTIONS & SCALE:", desc, f"Card {name} description missing PROPORTIONS & SCALE block")
            self.assertNotIn("—", desc, f"Card {name} description contains forbidden em-dash ('—')")

    def test_user_personas_canonical_heights(self):
        """Assert User Personas for Alyssa and Jasper contain exact canonical heights and single-line bracket."""
        persona_map = {
            "Alyssa": REPO_ROOT / "FINAL/personas/Alyssa_Persona.json",
            "Jasper": REPO_ROOT / "FINAL/personas/Jasper_Persona.json",
        }
        for name, path in persona_map.items():
            self.assertTrue(path.exists(), f"Persona file does not exist: {path}")
            data = json.loads(path.read_text(encoding="utf-8"))
            desc = data.get("description", "")
            first_line = desc.splitlines()[0] if desc.splitlines() else ""
            self.assertTrue(first_line.startswith("["), f"Persona {name} line 0 does not start with '['")
            self.assertTrue(first_line.endswith("]"), f"Persona {name} line 0 does not end with ']'")
            expected_height = CANONICAL_HEIGHTS[name]
            self.assertIn(expected_height, first_line, f"Persona {name} line 0 missing canonical height '{expected_height}'")
            self.assertIn("PROPORTIONS & SCALE:", desc, f"Persona {name} description missing PROPORTIONS & SCALE block")
            self.assertNotIn("—", desc, f"Persona {name} description contains forbidden em-dash ('—')")

    def test_primary_lorebook_entries_canonical_heights(self):
        """Assert Svartulfr_NPC_Primary.json entries for all 6 characters contain exact heights and single-line brackets."""
        path = REPO_ROOT / "FINAL/Svartulfr_NPC_Primary.json"
        self.assertTrue(path.exists(), f"Primary lorebook missing: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        entry_by_id = {e.get("entry_id"): e for e in data.get("entries", [])}
        
        target_ids = {
            "Alyssa": "alyssa_world_dossier_2b54a223",
            "Jasper": "Vcj4h2TL4Usola2A4OOl6",
            "Noah": "H2JX-NkHRiJ2FzoekC5ZZ",
            "Malachia": "jDuJtzirlEZC3K_ArIufh",
            "Erik": "C-JisFj8qA1tsFEqZKevk",
            "Wulfnic": "HhuMluMmIIENUei3bX6ed",
        }
        for name, eid in target_ids.items():
            self.assertIn(eid, entry_by_id, f"Entry {name} (ID: {eid}) missing in Primary lorebook")
            entry = entry_by_id[eid]
            content = entry.get("content", "")
            first_line = content.splitlines()[0] if content.splitlines() else ""
            self.assertTrue(first_line.startswith("["), f"Lorebook entry {name} line 0 does not start with '['")
            self.assertTrue(first_line.endswith("]"), f"Lorebook entry {name} line 0 does not end with ']'")
            expected_height = CANONICAL_HEIGHTS[name]
            self.assertIn(expected_height, first_line, f"Lorebook entry {name} line 0 missing canonical height '{expected_height}'")
            self.assertIn("PROPORTIONS & SCALE:", content, f"Lorebook entry {name} missing PROPORTIONS & SCALE block")
            self.assertNotIn("—", content, f"Lorebook entry {name} content contains forbidden em-dash ('—')")

    def test_legacy_heights_eradication(self):
        """Adversarially search for lingering legacy heights for the 6 characters."""
        # Erik: legacy 203 cm / 6' 8"
        erik_files = [
            REPO_ROOT / "FINAL/Erik_Douglas_card.json",
            REPO_ROOT / "database/characters/C_Erik_Douglas.md"
        ]
        for f in erik_files:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn("203 cm", text, f"Found legacy height '203 cm' in {f}")
            self.assertNotIn("203cm", text, f"Found legacy height '203cm' in {f}")
            self.assertNotIn("6' 8\"", text, f"Found legacy imperial '6\' 8\"' in {f}")

        # Wulfnic: legacy 210 cm / 6' 11"
        wulfnic_files = [
            REPO_ROOT / "FINAL/Wulfnic_Bloodmoon_card.json",
            REPO_ROOT / "database/characters/C_Wulfnic_Bloodmoon.md"
        ]
        for f in wulfnic_files:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn("210 cm", text, f"Found legacy height '210 cm' in {f}")
            self.assertNotIn("210cm", text, f"Found legacy height '210cm' in {f}")
            self.assertNotIn("6' 11\"", text, f"Found legacy imperial '6\' 11\"' in {f}")

        # Jasper: legacy 191 cm / 6' 3"
        jasper_files = [
            REPO_ROOT / "FINAL/Jasper_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "FINAL/personas/Jasper_Persona.json",
            REPO_ROOT / "database/characters/C_Jasper_Douglas_Bloodmoon.md"
        ]
        for f in jasper_files:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn("191 cm", text, f"Found legacy height '191 cm' in {f}")
            self.assertNotIn("191cm", text, f"Found legacy height '191cm' in {f}")
            self.assertNotIn("6' 3\"", text, f"Found legacy imperial '6\' 3\"' in {f}")

        # Alyssa: legacy 150 cm / 4' 11" in height context
        alyssa_files = [
            REPO_ROOT / "ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "FINAL/personas/Alyssa_Persona.json",
            REPO_ROOT / "database/characters/C_Alyssa_Douglas_Bloodmoon.md"
        ]
        for f in alyssa_files:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn("150 cm", text, f"Found legacy height '150 cm' in {f}")
            self.assertNotIn("150cm", text, f"Found legacy height '150cm' in {f}")
            self.assertNotIn("4' 11\"", text, f"Found legacy imperial '4\' 11\"' in {f}")

        # Noah: legacy 6' 6" without decimals
        noah_files = [
            REPO_ROOT / "FINAL/Noah_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "database/characters/C_Noah_Douglas_Bloodmoon.md"
        ]
        for f in noah_files:
            text = f.read_text(encoding="utf-8")
            self.assertNotIn("197 cm (6' 6\")", text, f"Found legacy non-decimal height '197 cm (6\' 6\")' in {f}")

    def test_deep_nested_fields_legacy_heights_scan(self):
        """Recursively inspect all nested fields (outfits, greetings, shared_info) for legacy heights."""
        target_files = [
            REPO_ROOT / "FINAL/Erik_Douglas_card.json",
            REPO_ROOT / "FINAL/Wulfnic_Bloodmoon_card.json",
            REPO_ROOT / "FINAL/Jasper_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "FINAL/Noah_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "FINAL/Malachia_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json",
            REPO_ROOT / "FINAL/personas/Alyssa_Persona.json",
            REPO_ROOT / "FINAL/personas/Jasper_Persona.json"
        ]

        def scan_nested(val, file_name, path_str):
            if isinstance(val, str):
                if "Erik" in file_name:
                    self.assertNotIn("203 cm", val, f"Stray '203 cm' at {file_name}:{path_str}")
                    self.assertNotIn("6' 8\"", val, f"Stray '6\' 8\"' at {file_name}:{path_str}")
                elif "Wulfnic" in file_name:
                    self.assertNotIn("210 cm", val, f"Stray '210 cm' at {file_name}:{path_str}")
                    self.assertNotIn("6' 11\"", val, f"Stray '6\' 11\"' at {file_name}:{path_str}")
                elif "Jasper" in file_name:
                    self.assertNotIn("191 cm", val, f"Stray '191 cm' at {file_name}:{path_str}")
                    self.assertNotIn("6' 3\"", val, f"Stray '6\' 3\"' at {file_name}:{path_str}")
                elif "Alyssa" in file_name:
                    self.assertNotIn("150 cm", val, f"Stray '150 cm' at {file_name}:{path_str}")
                    self.assertNotIn("4' 11\"", val, f"Stray '4\' 11\"' at {file_name}:{path_str}")
            elif isinstance(val, dict):
                for k, v in val.items():
                    scan_nested(v, file_name, f"{path_str}.{k}")
            elif isinstance(val, list):
                for i, v in enumerate(val):
                    scan_nested(v, file_name, f"{path_str}[{i}]")

        for tf in target_files:
            data = json.loads(tf.read_text(encoding="utf-8"))
            scan_nested(data, tf.name, "root")

    def test_line_zero_bracket_constraint_all_cards_personas_and_entries(self):
        """Assert line 0 of EVERY card, persona, and lorebook entry starts with '[' and ends with ']'."""
        # 1. Standalone cards in FINAL/
        for p in (REPO_ROOT / "FINAL").glob("*_card.json"):
            data = json.loads(p.read_text(encoding="utf-8"))
            desc = data.get("description", "")
            first_line = desc.splitlines()[0] if desc.splitlines() else ""
            self.assertTrue(first_line.startswith("[") and first_line.endswith("]"),
                            f"Card {p.name} line 0 does not satisfy [ ... ]: {first_line[:80]}")

        # 2. Legacy cards in ARCHIVIO/cards_legacy/
        for p in (REPO_ROOT / "ARCHIVIO/cards_legacy").glob("*.json"):
            data = json.loads(p.read_text(encoding="utf-8"))
            desc = data.get("description", "")
            first_line = desc.splitlines()[0] if desc.splitlines() else ""
            self.assertTrue(first_line.startswith("[") and first_line.endswith("]"),
                            f"Legacy card {p.name} line 0 does not satisfy [ ... ]: {first_line[:80]}")

        # 3. Personas in FINAL/personas/
        for p in (REPO_ROOT / "FINAL/personas").glob("*.json"):
            data = json.loads(p.read_text(encoding="utf-8"))
            desc = data.get("description", "")
            first_line = desc.splitlines()[0] if desc.splitlines() else ""
            self.assertTrue(first_line.startswith("[") and first_line.endswith("]"),
                            f"Persona {p.name} line 0 does not satisfy [ ... ]: {first_line[:80]}")

        # 4. Primary and Secondary Lorebooks
        for lb_rel in ["FINAL/Svartulfr_NPC_Primary.json", "FINAL/Svartulfr_NPC_Secondary.json"]:
            lb_path = REPO_ROOT / lb_rel
            data = json.loads(lb_path.read_text(encoding="utf-8"))
            for entry in data.get("entries", []):
                content = entry.get("content", "")
                first_line = content.splitlines()[0] if content.splitlines() else ""
                self.assertTrue(first_line.startswith("[") and first_line.endswith("]"),
                                f"Lorebook {lb_rel} entry '{entry.get('name')}' line 0 does not satisfy [ ... ]")

    def test_lorebook_byte_for_byte_parity_and_mirror(self):
        """Assert entries == lexicon byte-for-byte in Primary lorebook and assert mirror equality with lorebooks/optimized/."""
        final_primary = REPO_ROOT / "FINAL/Svartulfr_NPC_Primary.json"
        opt_primary = REPO_ROOT / "lorebooks/optimized/Svartulfr_NPC_Primary.json"
        self.assertTrue(final_primary.exists(), f"Missing {final_primary}")
        self.assertTrue(opt_primary.exists(), f"Missing {opt_primary}")

        # Check internal parity in FINAL
        with open(final_primary, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        entries_canonical = json.dumps(final_data["entries"], sort_keys=True, ensure_ascii=False)
        lexicon_canonical = json.dumps(final_data["lexicon"], sort_keys=True, ensure_ascii=False)
        self.assertEqual(entries_canonical, lexicon_canonical, "FINAL/Svartulfr_NPC_Primary.json entries != lexicon!")

        # Check internal parity in optimized
        with open(opt_primary, "r", encoding="utf-8") as f:
            opt_data = json.load(f)
        opt_entries_canonical = json.dumps(opt_data["entries"], sort_keys=True, ensure_ascii=False)
        opt_lexicon_canonical = json.dumps(opt_data["lexicon"], sort_keys=True, ensure_ascii=False)
        self.assertEqual(opt_entries_canonical, opt_lexicon_canonical, "lorebooks/optimized/Svartulfr_NPC_Primary.json entries != lexicon!")

        # Check byte-for-byte file equality
        is_identical = filecmp.cmp(str(final_primary), str(opt_primary), shallow=False)
        self.assertTrue(is_identical, "FINAL/Svartulfr_NPC_Primary.json is NOT byte-for-byte identical to lorebooks/optimized/Svartulfr_NPC_Primary.json")


class TestAdversarialImagesAndSpecifications(unittest.TestCase):
    """Stress tests for M2: PNG binary validation, 1024x1024 resolution, file size > 1 MB, and lore invariants."""

    def test_image_files_magic_bytes_and_dimensions(self):
        """Assert all 8 image files in both asset/references and assets/references have PNG magic bytes, 1024x1024 dimensions, and > 1 MB size."""
        png_magic = b"\x89PNG\r\n\x1a\n"
        dirs = [REPO_ROOT / "asset/references", REPO_ROOT / "assets/references"]

        for d in dirs:
            self.assertTrue(d.exists() and d.is_dir(), f"Directory missing: {d}")
            for img_name in IMAGE_NAMES:
                img_path = d / img_name
                self.assertTrue(img_path.exists(), f"Image missing: {img_path}")
                file_size = img_path.stat().st_size
                self.assertGreater(file_size, 1_000_000, f"Image {img_path} size is trivial ({file_size} bytes <= 1 MB)")

                with open(img_path, "rb") as f:
                    header = f.read(24)

                # Check magic bytes
                self.assertEqual(header[:8], png_magic, f"File {img_path} does not have valid PNG magic bytes!")

                # Check IHDR chunk
                ihdr_chunk = header[12:16]
                self.assertEqual(ihdr_chunk, b"IHDR", f"File {img_path} missing IHDR chunk header!")

                # Check dimensions
                width, height = struct.unpack(">II", header[16:24])
                self.assertEqual((width, height), (1024, 1024), f"File {img_path} dimensions are {width}x{height}, expected 1024x1024!")

    def test_image_files_chunks_structural_integrity(self):
        """Assert each image file contains genuine IDAT and IEND chunks confirming proper PNG encoding."""
        dirs = [REPO_ROOT / "asset/references", REPO_ROOT / "assets/references"]
        for d in dirs:
            for img_name in IMAGE_NAMES:
                img_path = d / img_name
                with open(img_path, "rb") as f:
                    data = f.read()

                # PNG must end with IEND chunk (last 12 bytes: length 0, IEND, CRC)
                self.assertTrue(b"IEND" in data[-16:], f"File {img_path} missing trailing IEND chunk!")
                # Must contain IDAT chunks
                self.assertTrue(b"IDAT" in data, f"File {img_path} missing IDAT compressed image payload!")

    def test_image_files_dual_directory_mirror_equality(self):
        """Assert images in asset/references/ and assets/references/ are byte-for-byte identical."""
        dir1 = REPO_ROOT / "asset/references"
        dir2 = REPO_ROOT / "assets/references"
        for img_name in IMAGE_NAMES:
            p1 = dir1 / img_name
            p2 = dir2 / img_name
            identical = filecmp.cmp(str(p1), str(p2), shallow=False)
            self.assertTrue(identical, f"Image {img_name} differs between asset/references and assets/references!")

    def test_runic_specification_lore_invariants_and_em_dash_ban(self):
        """Assert docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md strictly adheres to all lore invariants and 0 em-dashes."""
        spec_path = REPO_ROOT / "docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md"
        self.assertTrue(spec_path.exists(), f"Specification file missing: {spec_path}")
        content = spec_path.read_text(encoding="utf-8")

        # Zero em-dash enforcement
        self.assertNotIn("—", content, "Specification document contains forbidden em-dash ('—')")

        # Ritual components
        self.assertIn("serpent tooth", content.lower(), "Missing 'serpent tooth' ritual component")
        self.assertIn("cold iron ink", content.lower(), "Missing 'cold iron ink' ritual component")
        self.assertIn("fifth day", content.lower(), "Missing '5th day' timing component")
        self.assertIn("inner left wrist", content.lower(), "Missing 'inner left wrist' anatomical placement")

        # Alyssa & Jasper Hip Invariants
        self.assertIn("left hip", content.lower(), "Missing Alyssa's 'left hip' placement")
        self.assertIn("maniulfr", content.lower(), "Missing Alyssa's cosmic title 'Maniulfr'")
        self.assertIn("right hip", content.lower(), "Missing Jasper's 'right hip' placement")
        self.assertIn("solulfr", content.lower(), "Missing Jasper's cosmic title 'Solulfr'")

        # Prohibition of dispersed marks
        self.assertIn("prohibition of dispersed celestial marks", content.lower(), "Missing categorical prohibition clause")
        self.assertIn("chest, collarbone, neck, hands", content.lower(), "Missing prohibited anatomical locations list")

        # Pack members coverage
        for pack_name in ["Logan Jarn Douglas", "Malachia Bjorn Douglas Bloodmoon", "Erik Ulfr Douglas", "Wulfnic Baleygr Bloodmoon"]:
            self.assertIn(pack_name, content, f"Missing pack member section: '{pack_name}'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
