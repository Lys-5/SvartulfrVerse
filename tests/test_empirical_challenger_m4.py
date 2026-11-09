"""
tests/test_empirical_challenger_m4.py

Adversarial Stress-Test Suite for Milestone 4:
1. Interrogates FINAL/Svartulfr_Lorebook_III.json & lorebooks/optimized/Svartulfr_Lorebook_III.json
   - Entry #39 vs #40 IDs and names
   - 47/47 unique entry IDs
   - entries == lexicon byte-for-byte
   - FINAL/ matches lorebooks/optimized/ byte-for-byte
2. Verifies all standalone lorebooks for entries == lexicon parity and mirror identity
3. Scans CHANGELOG.md for zero em-dashes and comprehensive milestone coverage
4. Scans all 6 new knowledge vault articles for zero em-dashes and required topics
5. Scans character cards and personas for M3/M4 invariants (Level 19, credentials, positive framing)
"""

import unittest
import json
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

class TestEmpiricalChallengerM4(unittest.TestCase):

    def test_lorebook_iii_entries_39_and_40(self):
        """Interrogate entry #39 and #40 in both FINAL and lorebooks/optimized."""
        target_files = [
            REPO_ROOT / "FINAL" / "Svartulfr_Lorebook_III.json",
            REPO_ROOT / "lorebooks" / "optimized" / "Svartulfr_Lorebook_III.json"
        ]

        for path in target_files:
            self.assertTrue(path.exists(), f"File does not exist: {path}")
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            entries = data.get("entries", [])
            lexicon = data.get("lexicon", [])

            self.assertEqual(len(entries), 47, f"Expected 47 entries in {path}, found {len(entries)}")
            self.assertEqual(len(lexicon), 47, f"Expected 47 lexicon items in {path}, found {len(lexicon)}")
            self.assertEqual(entries, lexicon, f"entries != lexicon in {path}")

            # Interrogate entry #39
            e39 = entries[39]
            self.assertEqual(
                e39.get("entry_id"), "event_partita_di_campionato_",
                f"Entry #39 has unexpected ID: {e39.get('entry_id')}"
            )
            self.assertIn(
                "Football", e39.get("name", ""),
                f"Entry #39 name does not mention Football: {e39.get('name')}"
            )

            # Interrogate entry #40
            e40 = entries[40]
            self.assertEqual(
                e40.get("entry_id"), "event_partita_di_campionato_hockey",
                f"Entry #40 has unexpected ID: {e40.get('entry_id')}"
            )
            self.assertIn(
                "Ice Hockey", e40.get("name", ""),
                f"Entry #40 name does not mention Ice Hockey: {e40.get('name')}"
            )

            # Assert uniqueness of all 47 IDs
            all_entry_ids = [e.get("entry_id") for e in entries]
            duplicates = [x for x in all_entry_ids if all_entry_ids.count(x) > 1]
            self.assertEqual(len(duplicates), 0, f"Duplicate entry IDs in {path}: {duplicates}")
            self.assertEqual(len(set(all_entry_ids)), 47, f"Unique ID count != 47 in {path}")

    def test_lorebook_iii_file_parity(self):
        """Interrogate byte-for-byte and SHA256 identity between FINAL and lorebooks/optimized."""
        p1 = REPO_ROOT / "FINAL" / "Svartulfr_Lorebook_III.json"
        p2 = REPO_ROOT / "lorebooks" / "optimized" / "Svartulfr_Lorebook_III.json"

        with open(p1, "rb") as f1, open(p2, "rb") as f2:
            bytes1 = f1.read()
            bytes2 = f2.read()

        h1 = hashlib.sha256(bytes1).hexdigest()
        h2 = hashlib.sha256(bytes2).hexdigest()

        self.assertEqual(h1, h2, f"SHA256 mismatch between FINAL and optimized: {h1} vs {h2}")
        self.assertEqual(bytes1, bytes2, "Byte-for-byte content mismatch between FINAL and optimized!")

    def test_all_six_lorebooks_mirror_and_entries_lexicon_parity(self):
        """Stress-test standalone lorebooks for entries == lexicon parity and mirror identity."""
        paired_mirrors = [
            ("FINAL/Svartulfr_Lorebook_I.json", "lorebooks/optimized/Svartulfr_Lorebook_I.json"),
            ("FINAL/Svartulfr_Lorebook_II.json", "lorebooks/optimized/Svartulfr_Lorebook_II.json"),
            ("FINAL/Svartulfr_Lorebook_III.json", "lorebooks/optimized/Svartulfr_Lorebook_III.json"),
            ("FINAL/Svartulfr_NPC_Primary.json", "lorebooks/optimized/Svartulfr_NPC_Primary.json"),
            ("FINAL/Svartulfr_NPC_Secondary.json", "lorebooks/optimized/Svartulfr_NPC_Secondary.json")
        ]

        for rel_final, rel_opt in paired_mirrors:
            p_final = REPO_ROOT / rel_final
            p_opt = REPO_ROOT / rel_opt

            self.assertTrue(p_final.exists(), f"Missing FINAL file: {p_final}")
            self.assertTrue(p_opt.exists(), f"Missing optimized file: {p_opt}")

            with open(p_final, "r", encoding="utf-8") as f:
                d_final = json.load(f)
            with open(p_opt, "r", encoding="utf-8") as f:
                d_opt = json.load(f)

            # Check entries == lexicon in FINAL
            self.assertEqual(
                d_final.get("entries"), d_final.get("lexicon"),
                f"entries != lexicon in {p_final}"
            )
            # Check entries == lexicon in optimized
            self.assertEqual(
                d_opt.get("entries"), d_opt.get("lexicon"),
                f"entries != lexicon in {p_opt}"
            )
            # Check equality between FINAL and optimized
            self.assertEqual(
                d_final.get("entries"), d_opt.get("entries"),
                f"entries mismatch between FINAL and optimized for {rel_final}"
            )

        # Standalone Location Lorebook in lorebooks/optimized/
        loc_opt = REPO_ROOT / "lorebooks" / "optimized" / "Svartulfr_Location.json"
        self.assertTrue(loc_opt.exists(), f"Missing {loc_opt}")
        with open(loc_opt, "r", encoding="utf-8") as f:
            d_loc = json.load(f)
        self.assertEqual(
            d_loc.get("entries"), d_loc.get("lexicon"),
            f"entries != lexicon in {loc_opt}"
        )
        self.assertEqual(len(d_loc.get("entries", [])), 226)

    def test_changelog_em_dash_absence(self):
        """Scrutinize the newly added CHANGELOG.md section for zero em-dashes and milestone coverage."""
        cl_path = REPO_ROOT / "CHANGELOG.md"
        self.assertTrue(cl_path.exists(), "CHANGELOG.md not found")

        with open(cl_path, "r", encoding="utf-8") as f:
            content = f.read()

        header = "### 02/11/2026 - Integrazione Completa della Lore Emergente: St. Brugge, Padre Revazhael, Cristallografia Runica e Allineamento Multi-Tier"
        self.assertIn(header, content, "Target changelog header missing")

        start_idx = content.find(header)
        end_idx = content.find("### 01/11/2026", start_idx)
        self.assertNotEqual(start_idx, -1)
        self.assertNotEqual(end_idx, -1)

        new_section = content[start_idx:end_idx]

        # Check em-dash
        em_dash = "\u2014"
        count = new_section.count(em_dash)
        self.assertEqual(count, 0, f"Found {count} em-dashes in new CHANGELOG section!")

        # Verify milestone coverage
        self.assertIn("Tier 2 Knowledge Vault", new_section)
        self.assertIn("Tier 2 Standalone Lorebooks", new_section)
        self.assertIn("Tier 2 Character Cards & User Personas", new_section)
        self.assertIn("Tier 3 Verifica Rigorosa", new_section)
        self.assertIn("St. Brugge Private Academy", new_section)
        self.assertIn("Padre Revazhael", new_section)
        self.assertIn("Cristallografia runica", new_section)
        self.assertIn("cilindri incantati a risonanza individuale", new_section)
        self.assertIn("Magia Abissale", new_section)
        self.assertIn("ADB-555", new_section)
        self.assertIn("JDB-555", new_section)
        self.assertIn("event_partita_di_campionato_hockey", new_section)

    def test_new_vault_articles_em_dash_free(self):
        """Verify that all 6 newly created knowledge vault articles contain zero em-dashes."""
        vault_files = [
            "ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md",
            "APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md",
            "PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md",
            "FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md",
            "ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md",
            "DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md"
        ]

        vault_dir = REPO_ROOT / "knowledge" / "Lore_Worldbuilding"
        for vname in vault_files:
            vpath = vault_dir / vname
            self.assertTrue(vpath.exists(), f"Vault article missing: {vpath}")
            with open(vpath, "r", encoding="utf-8") as f:
                text = f.read()

            em_dash_count = text.count("\u2014")
            self.assertEqual(em_dash_count, 0, f"Found {em_dash_count} em-dashes in {vname}!")

    def test_character_cards_and_personas_emergent_lore_invariants(self):
        """Verify character cards and personas have Level 19, credentials, and positive framing."""
        jasper_card_path = REPO_ROOT / "FINAL" / "Jasper_Douglas_Bloodmoon_card.json"
        with open(jasper_card_path, "r", encoding="utf-8") as f:
            j_card = json.load(f)

        j_desc = j_card.get("description", "")
        self.assertIn("JDB-555", j_desc)
        self.assertIn("Registered Guild Hunter", j_desc)
        self.assertIn("St. Brugge Private Academy", j_desc)
        self.assertNotIn("collarbone", j_desc.lower())
        self.assertNotIn("no human ears", j_desc.lower())
        self.assertNotIn("senza orecchie umane", j_desc.lower())

        # Check Jasper RPG Level in description
        self.assertIn("[LEVEL: 19;", j_desc, "Jasper card description missing [LEVEL: 19;")

        # Check Jasper Persona
        jasper_persona_path = REPO_ROOT / "FINAL" / "personas" / "Jasper_Persona.json"
        with open(jasper_persona_path, "r", encoding="utf-8") as f:
            j_pers = json.load(f)
        j_pers_desc = j_pers.get("description", "")
        self.assertIn("JDB-555", j_pers_desc)
        self.assertIn("Registered Guild Hunter", j_pers_desc)
        self.assertNotIn("collarbone", j_pers_desc.lower())
        self.assertNotIn("no human ears", j_pers_desc.lower())

        # Check Alyssa Persona
        alyssa_persona_path = REPO_ROOT / "FINAL" / "personas" / "Alyssa_Persona.json"
        with open(alyssa_persona_path, "r", encoding="utf-8") as f:
            a_pers = json.load(f)
        a_pers_desc = a_pers.get("description", "")
        self.assertIn("ADB-555", a_pers_desc)
        self.assertIn("Certified Guild Healer", a_pers_desc)
        self.assertNotIn("Novice Healing Mage", a_pers_desc)
        self.assertNotIn("no human ears", a_pers_desc.lower())

        # Check Alyssa Legacy Card
        alyssa_card_path = REPO_ROOT / "ARCHIVIO" / "cards_legacy" / "Alyssa_Douglas_Bloodmoon_card.json"
        with open(alyssa_card_path, "r", encoding="utf-8") as f:
            a_card = json.load(f)
        a_desc = a_card.get("description", "")
        self.assertIn("ADB-555", a_desc)
        self.assertIn("Certified Guild Healer", a_desc)
        self.assertNotIn("Novice Healing Mage", a_desc)
        self.assertNotIn("no human ears", a_desc.lower())

if __name__ == "__main__":
    unittest.main()
