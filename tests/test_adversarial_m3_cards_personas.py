#!/usr/bin/env python3
"""
tests/test_adversarial_m3_cards_personas.py

Empirical Challenger Adversarial Test Suite for Milestone 3:
Character Cards & Personas Synchronization.

Executed directly by challenger_m3_2 to empirically verify:
1. Cross-file parity across Cards, Personas, and Lorebook NPC Primary dossiers.
2. Negative framing token eradication across all fields.
3. Avatar activation regex validity in V8 / Node.js.
4. Token budget and context window safety.
"""

import json
import re
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TARGET_FILES = {
    "jasper_card": REPO_ROOT / "FINAL/Jasper_Douglas_Bloodmoon_card.json",
    "jasper_persona": REPO_ROOT / "FINAL/personas/Jasper_Persona.json",
    "alyssa_persona": REPO_ROOT / "FINAL/personas/Alyssa_Persona.json",
    "alyssa_card": REPO_ROOT / "ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json",
    "npc_primary": REPO_ROOT / "FINAL/Svartulfr_NPC_Primary.json",
}

class TestAdversarialMilestone3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {}
        for key, path in TARGET_FILES.items():
            with open(path, "r", encoding="utf-8") as f:
                cls.data[key] = json.load(f)
                
        cls.j_npc = next(e for e in cls.data["npc_primary"]["entries"] if e.get("entry_id") == "Vcj4h2TL4Usola2A4OOl6")
        cls.a_npc = next(e for e in cls.data["npc_primary"]["entries"] if e.get("entry_id") == "alyssa_world_dossier_2b54a223")

    def test_01_line_1_plist_bracket_header_parity(self):
        """Line 1 [NAME: ...] must be byte-for-byte identical across Card, Persona, and NPC Primary dossier."""
        j_card_l1 = self.data["jasper_card"]["description"].split("\n\n")[0]
        j_pers_l1 = self.data["jasper_persona"]["description"].split("\n\n")[0]
        j_npc_l1 = self.j_npc["content"].split("\n\n")[0]
        
        self.assertEqual(j_card_l1, j_pers_l1, "Jasper Card and Persona Line 1 mismatch")
        self.assertEqual(j_card_l1, j_npc_l1, "Jasper Card and NPC Primary Line 1 mismatch")
        self.assertNotIn("\n", j_card_l1, "Jasper Line 1 contains embedded newlines")
        
        a_card_l1 = self.data["alyssa_card"]["description"].split("\n\n")[0]
        a_pers_l1 = self.data["alyssa_persona"]["description"].split("\n\n")[0]
        a_npc_l1 = self.a_npc["content"].split("\n\n")[0]
        
        self.assertEqual(a_card_l1, a_pers_l1, "Alyssa Card and Persona Line 1 mismatch")
        self.assertEqual(a_card_l1, a_npc_l1, "Alyssa Card and NPC Primary Line 1 mismatch")
        self.assertNotIn("\n", a_card_l1, "Alyssa Line 1 contains embedded newlines")

    def test_02_credentials_and_canonical_lore_attributes(self):
        """Verify presence of all newly integrated canonical attributes and credentials in Line 1."""
        j_l1 = self.data["jasper_card"]["description"].split("\n\n")[0]
        self.assertIn("St. Brugge Private Academy alumnus", j_l1)
        self.assertIn("Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555)", j_l1)
        self.assertIn("HEIGHT: 193 cm (6' 4\")", j_l1)
        self.assertIn("AGE: 19 (Born April 22, 2005)", j_l1)
        self.assertIn("Mark of Sol", j_l1)
        self.assertNotIn("collarbone", j_l1.lower())
        
        a_l1 = self.data["alyssa_card"]["description"].split("\n\n")[0]
        self.assertIn("St. Brugge Private Academy alumnus", a_l1)
        self.assertIn("Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555)", a_l1)
        self.assertIn("Applied Runic Crystallographer", a_l1)
        self.assertIn("HEIGHT: 155 cm (5' 1\")", a_l1)
        self.assertIn("AGE: 19 (Born April 22, 2005)", a_l1)
        self.assertIn("Mark of Mani", a_l1)
        self.assertNotIn("Novice Healing Mage", a_l1)

    def test_03_backstory_collaborative_tutelage_parity(self):
        """BACKSTORY must be identical across Card, Persona, and NPC dossier, detailing joint lessons under Revazhael."""
        def extract_bs(text):
            start = text.find("BACKSTORY:")
            end = text.find("FAMILY & PACK:")
            return text[start:end].strip() if start != -1 and end != -1 else ""

        j_c_bs = extract_bs(self.data["jasper_card"]["description"])
        j_p_bs = extract_bs(self.data["jasper_persona"]["description"])
        j_n_bs = extract_bs(self.j_npc["content"])
        
        self.assertEqual(j_c_bs, j_p_bs)
        self.assertEqual(j_c_bs, j_n_bs)
        self.assertIn("Father Revazhael", j_c_bs)
        self.assertIn("St. Brugge Private Academy", j_c_bs)
        self.assertIn("Abyssal Armor", j_c_bs)
        self.assertIn("Hunter ID JDB-555", j_c_bs)
        
        a_c_bs = extract_bs(self.data["alyssa_card"]["description"])
        a_p_bs = extract_bs(self.data["alyssa_persona"]["description"])
        a_n_bs = extract_bs(self.a_npc["content"])
        
        self.assertEqual(a_c_bs, a_p_bs)
        self.assertEqual(a_c_bs, a_n_bs)
        self.assertIn("Father Revazhael", a_c_bs)
        self.assertIn("St. Brugge Private Academy", a_c_bs)
        self.assertIn("applied runic crystallography", a_c_bs.lower())
        self.assertIn("Hunter ID ADB-555", a_c_bs)
        self.assertIn("Absolute Pacifist Vow", a_c_bs)
        self.assertNotIn("Novice Healing Mage", a_c_bs)

    def test_04_rpg_level_19_alignment(self):
        """All 4 target files must have [LEVEL: 19; aligned with age 19."""
        for label in ["jasper_card", "jasper_persona", "alyssa_persona", "alyssa_card"]:
            desc = self.data[label]["description"]
            m = re.search(r'\[LEVEL:\s*(\d+);', desc)
            self.assertIsNotNone(m, f"No [LEVEL: tag in {label}")
            self.assertEqual(int(m.group(1)), 19, f"Level mismatch in {label}")

    def test_05_adversarial_negative_framing_scan(self):
        """Zero negative anatomical framing across all fields in the 4 target files and target dossiers."""
        patterns = [
            r'no\s+human\s+ears',
            r'without\s+human\s+ears',
            r'senza\s+(?:alcun[ao]\s+)?orecchi[ae]\s+uman[ae]',
            r'prive?\s+di\s+(?:qualsiasi\s+)?orecchi[ae]\s+uman[ae]',
            r'nessun\s+orecchio\s+umano',
            r'zero\s+legs',
            r'zero\s+gambe',
            r'zero\s+feet',
            r'zero\s+piedi',
            r'lacking\s+human\s+ears',
        ]
        regex = re.compile('|'.join(f'({p})' for p in patterns), re.I)

        def walk(val, path=""):
            hits = []
            if isinstance(val, str):
                for m in regex.finditer(val):
                    snippet = val[max(0, m.start()-40):min(len(val), m.end()+40)]
                    if "never mention, describe, or reiterate the absence or lack of human ears" in snippet:
                        continue
                    hits.append((path, m.group(0), snippet))
            elif isinstance(val, list):
                for i, it in enumerate(val):
                    hits.extend(walk(it, f"{path}[{i}]"))
            elif isinstance(val, dict):
                for k, v in val.items():
                    hits.extend(walk(v, f"{path}.{k}" if path else k))
            return hits

        for label in ["jasper_card", "jasper_persona", "alyssa_persona", "alyssa_card"]:
            violations = walk(self.data[label])
            self.assertEqual(len(violations), 0, f"Found negative framing in {label}: {violations}")
            
        self.assertEqual(len(walk(self.j_npc["content"])), 0, "Negative framing in Jasper NPC content")
        self.assertEqual(len(walk(self.a_npc["content"])), 0, "Negative framing in Alyssa NPC content")

    def test_06_avatar_activation_regex_syntax_and_matching(self):
        """Verify avatar activation regexes in V8/Node.js."""
        cmd = ["node", "scratch/test_avatar_activation_v8.js"]
        res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"Node.js script failed: {res.stderr}")
        self.assertIn("Results: 31 / 31 test cases passed as predicted", res.stdout)

    def test_07_token_safety_and_context_window(self):
        """Verify descriptions and dossiers fit within their respective platform token budgets."""
        # Jasper Card and Persona descriptions ~3,405 tokens
        j_tokens = len(self.data["jasper_card"]["description"]) / 4
        self.assertLess(j_tokens, 4500, "Jasper description exceeds safe persona token budget")
        
        # Alyssa Persona description ~3,091 tokens
        a_tokens = len(self.data["alyssa_persona"]["description"]) / 4
        self.assertLess(a_tokens, 4500, "Alyssa persona exceeds safe persona token budget")
        
        # NPC Primary dossiers fit within 7500 Lorebook budget
        j_npc_tokens = len(self.j_npc["content"]) / 4
        a_npc_tokens = len(self.a_npc["content"]) / 4
        self.assertLess(j_npc_tokens, 7500, "Jasper NPC dossier exceeds Lorebook 7500 budget")
        self.assertLess(a_npc_tokens, 7500, "Alyssa NPC dossier exceeds Lorebook 7500 budget")

    def test_08_formatting_discipline_zero_em_dashes(self):
        """Zero em-dashes across all modified files."""
        for label in ["jasper_card", "jasper_persona", "alyssa_persona", "alyssa_card"]:
            raw = (TARGET_FILES[label]).read_text(encoding="utf-8")
            self.assertNotIn("—", raw, f"Em-dash found in {label}")

if __name__ == "__main__":
    unittest.main()
