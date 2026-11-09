#!/usr/bin/env python3
"""
tests/test_adversarial_m1_knowledge_vault.py

Empirical Challenger Test Suite for Milestone 1: Vault Second Brain Knowledge Documentation.
Stress-tests the 6 Knowledge Vault articles against:
1. Primary playtest log: scratch/chat_export_ftrtAD79eddk9Ue9Jr2WJ.json
2. Canonical marks specification: docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md
3. Monolithic world reference: docs/world/Svartulfr_World_Doc.md
4. External resources index: knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md
"""

import unittest
import os
import re
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

VAULT_FILES = [
    REPO_ROOT / 'knowledge/Lore_Worldbuilding/ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md',
    REPO_ROOT / 'knowledge/Lore_Worldbuilding/APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md',
    REPO_ROOT / 'knowledge/Lore_Worldbuilding/PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md',
    REPO_ROOT / 'knowledge/Lore_Worldbuilding/FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md',
    REPO_ROOT / 'knowledge/Lore_Worldbuilding/ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md',
    REPO_ROOT / 'knowledge/Lore_Worldbuilding/DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md',
]


class TestAdversarialM1KnowledgeVault(unittest.TestCase):

    def setUp(self):
        with open(REPO_ROOT / 'scratch/chat_export_ftrtAD79eddk9Ue9Jr2WJ.json', 'r', encoding='utf-8') as f:
            self.chat_data = json.load(f)
        self.chat_text = '\n'.join([m.get('content', '') for m in self.chat_data['messages']])

    def test_01_vault_files_exist_and_non_empty(self):
        """All 6 vault articles must exist and have substantial content (> 3500 bytes)."""
        for vf in VAULT_FILES:
            self.assertTrue(vf.exists(), f"File does not exist: {vf}")
            size = vf.stat().st_size
            self.assertGreater(size, 3500, f"File {vf.name} is smaller than 3500 bytes ({size} bytes)")

    def test_02_zero_em_dashes(self):
        """Zero em-dashes (\\u2014) allowed across all 6 vault articles and EXTERNAL_RESOURCES_INDEX.md."""
        for vf in VAULT_FILES:
            content = vf.read_text(encoding='utf-8')
            em_count = content.count('\u2014')
            self.assertEqual(em_count, 0, f"VIOLATION: {em_count} em-dashes found in {vf.name}")

        ext_idx = REPO_ROOT / 'knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md'
        content_idx = ext_idx.read_text(encoding='utf-8')
        self.assertEqual(content_idx.count('\u2014'), 0, "VIOLATION: em-dashes found in EXTERNAL_RESOURCES_INDEX.md")

    def test_03_positive_framing_ears(self):
        """No negative framing regarding human ears allowed in any vault article."""
        negative_ear_regex = re.compile(
            r'\b(?:no\s+human\s+ears|without\s+human\s+ears|senza\s+orecchie\s+umane|'
            r'non\s+hanno\s+orecchie\s+umane|prive\s+di\s+orecchie\s+umane|priva\s+di\s+orecchie\s+umane|'
            r'mancanza\s+di\s+orecchie\s+umane|assenza\s+di\s+orecchie\s+umane|no\s+secondary\s+ears)\b',
            re.IGNORECASE
        )
        for vf in VAULT_FILES:
            content = vf.read_text(encoding='utf-8')
            matches = negative_ear_regex.findall(content)
            self.assertEqual(len(matches), 0, f"Negative ear framing found in {vf.name}: {matches}")

    def test_04_cross_exam_playtest_log_entities(self):
        """All core emergent lore entities from chat log must be present and accurately represented."""
        # Check St. Brugge & Revazhael
        st_brugge_file = (REPO_ROOT / 'knowledge/Lore_Worldbuilding/ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md').read_text(encoding='utf-8')
        self.assertIn("St. Brugge Private Academy", st_brugge_file)
        self.assertIn("Father Revazhael", st_brugge_file)

        # Check Revazhael profile
        rev_file = (REPO_ROOT / 'knowledge/Lore_Worldbuilding/FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md').read_text(encoding='utf-8')
        self.assertIn("Superior Demon", rev_file)
        self.assertIn("Revazhael", rev_file)
        self.assertIn("consent", rev_file.lower())

        # Check Crystallography
        cryst_file = (REPO_ROOT / 'knowledge/Lore_Worldbuilding/APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md').read_text(encoding='utf-8')
        self.assertIn("Cristallografia Runica Applicata", cryst_file)
        self.assertIn("Incantesimi Congelati", cryst_file)
        self.assertIn("Cilindri Incantati", cryst_file)

        # Check Planar Cosmology
        plan_file = (REPO_ROOT / 'knowledge/Lore_Worldbuilding/PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md').read_text(encoding='utf-8')
        self.assertIn("Magia Abissale", plan_file)
        self.assertIn("Necromanzia", plan_file)
        self.assertIn("Nessuno al dipartimento di Necromanzia", plan_file)

        # Check Security & Athletics
        dcc_file = (REPO_ROOT / 'knowledge/Lore_Worldbuilding/DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md').read_text(encoding='utf-8')
        self.assertIn("Archer Wolfwood", dcc_file)
        self.assertIn("Erik Douglas", dcc_file)
        self.assertIn("Kaladin Nargathon", dcc_file)
        self.assertIn("Chief Warg", dcc_file)
        self.assertIn("Adelin Coso", dcc_file)
        self.assertIn("Barkley Rover", dcc_file)

    def test_05_runic_and_divine_marks_consistency(self):
        """Stress-test runic and divine mark invariants."""
        hunter_file = (REPO_ROOT / 'knowledge/Lore_Worldbuilding/ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md').read_text(encoding='utf-8')
        
        # Alyssa: left hip, Maniulfr
        self.assertIn("left hip", hunter_file.lower())
        self.assertIn("maniulfr", hunter_file.lower())
        
        # Jasper: right hip, Solulfr
        self.assertIn("right hip", hunter_file.lower())
        self.assertIn("solulfr", hunter_file.lower())

        # Prohibitions: no chest marks, no collarbone marks, no wing scars
        for forbidden in ['collarbone', 'clavicola', 'chest mark', 'wing scars']:
            for vf in VAULT_FILES:
                content = vf.read_text(encoding='utf-8')
                self.assertNotIn(forbidden, content.lower(), f"Forbidden mark term '{forbidden}' in {vf.name}")

    def test_06_external_resources_index_no_regressions(self):
        """Assert zero URL losses and clean additions in EXTERNAL_RESOURCES_INDEX.md."""
        ext_idx_path = REPO_ROOT / 'knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md'
        orig = subprocess.check_output(['git', 'show', 'HEAD:knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md'], encoding='utf-8')
        curr = ext_idx_path.read_text(encoding='utf-8')

        orig_urls = set(re.findall(r'https?://[^\s\)\`\|]+', orig))
        curr_urls = set(re.findall(r'https?://[^\s\)\`\|]+', curr))
        missing_urls = orig_urls - curr_urls
        self.assertEqual(len(missing_urls), 0, f"Regressed URLs in index: {missing_urls}")

        # Check table totals
        self.assertIn("| **TOTAL** | **83** | **33** | **50** | **0** |", curr)

    def test_07_world_doc_synced_lines_integrity(self):
        """Verify the 4 synchronized locations in docs/world/Svartulfr_World_Doc.md."""
        world_doc_path = REPO_ROOT / 'docs/world/Svartulfr_World_Doc.md'
        content = world_doc_path.read_text(encoding='utf-8')
        
        self.assertIn("Revazhael (Father Rev, an ancient Superior Demon", content)
        self.assertIn("St. Brugge Private Academy", content)
        self.assertIn("Father Revazhael secretly provided advanced private tutorials", content)
        self.assertIn("Dal 26 agosto 2024, in seguito all'accordo istituzionale tra il Cancelliere Archer Wolfwood ed Erik Douglas", content)
        self.assertIn("Al secondo piano nell'ala est si trova la Suite 3, condivisa da Alyssa Douglas, Scarlett Rose e Sierra Cruz", content)


if __name__ == '__main__':
    unittest.main()
