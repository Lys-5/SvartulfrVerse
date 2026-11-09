#!/usr/bin/env python3
"""
tests/test_adversarial_m2_standalone_lorebooks.py

Empirical Challenger Adversarial Test Suite for Milestone 2: Standalone Lorebooks Emergent Lore Integration.
Executed directly by challenger_m2_2 to verify:
1. Persona Protection Adversarial Checks and Attack Scenarios (Alyssa & Jasper dossiers).
2. Token Budget Stress Testing (Platform budgets: 7500 Primary, 5000 all others).
3. Regression and Parity Checking across all 6 standalone lorebooks and their mirrors.
4. Demi-Human Positive Framing, Em-Dash Eradication, and Macro Hygiene.
5. Schema Integrity and Field Normalization (Revazhael, Larek Steeltooth, Resonant Cylinders, etc.).
"""

import json
import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

MODIFIED_FILES = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'lorebooks/optimized/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'lorebooks/optimized/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Lorebook_III.json',
    'lorebooks/optimized/Svartulfr_Lorebook_III.json',
    'lorebooks/optimized/Svartulfr_Location.json',
    'FINAL/Svartulfr_NPC_Secondary.json',
    'lorebooks/optimized/Svartulfr_NPC_Secondary.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'lorebooks/optimized/Svartulfr_NPC_Primary.json'
]

PAIRED_MIRRORS = [
    ('FINAL/Svartulfr_Lorebook_I.json', 'lorebooks/optimized/Svartulfr_Lorebook_I.json'),
    ('FINAL/Svartulfr_Lorebook_II.json', 'lorebooks/optimized/Svartulfr_Lorebook_II.json'),
    ('FINAL/Svartulfr_Lorebook_III.json', 'lorebooks/optimized/Svartulfr_Lorebook_III.json'),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'lorebooks/optimized/Svartulfr_NPC_Secondary.json'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'lorebooks/optimized/Svartulfr_NPC_Primary.json')
]

TARGET_ENTRIES = [
    ('FINAL/Svartulfr_Lorebook_I.json', 'lb1_concept_applied_runic_crystallography', 5000),
    ('FINAL/Svartulfr_Lorebook_I.json', 'lb1_magic_abyssal_magic_distinction', 5000),
    ('FINAL/Svartulfr_Lorebook_II.json', 'lb2_item_enchanted_resonant_cylinders', 5000),
    ('FINAL/Svartulfr_Lorebook_III.json', 'succ_lb3_st_brugge_academy', 5000),
    ('lorebooks/optimized/Svartulfr_Location.json', 'ulTwlYo2jqObA7l_bFoa5', 5000),
    ('lorebooks/optimized/Svartulfr_Location.json', 'loc_theta_iota_theta_suite_3', 5000),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'jmh0MajEsRwrm4UYU14mY', 5000),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'npc_larek_steeltooth', 5000),
    ('FINAL/Svartulfr_NPC_Primary.json', 'alyssa_world_dossier_2b54a223', 7500),
    ('FINAL/Svartulfr_NPC_Primary.json', 'Vcj4h2TL4Usola2A4OOl6', 7500),
]


def load_repo_json(rel_path):
    abs_path = REPO_ROOT / rel_path
    with open(abs_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def simulate_wyvern_trigger(entry, text, active_persona_id=None, active_character_ids=None):
    """
    Empirical simulation of Wyvern's Lorebook trigger evaluation:
    1. Check ignored_personas: if active_persona_id in entry['ignored_personas'], suppress (return False).
    2. Check ignored_characters: if any in active_character_ids in entry['ignored_characters'], suppress (return False).
    3. Check primary keys: whole-word, case-insensitive match against text.
    4. If not selective: triggers if any primary key matches.
    5. If selective:
       - If key_logic == 'AND_ANY': requires at least one primary key AND at least one secondary key to match.
       - If key_logic == 'AND_ALL': requires all secondary keys.
    """
    if active_character_ids is None:
        active_character_ids = []

    # 1. Native suppression checks
    ignored_personas = entry.get('ignored_personas', [])
    if active_persona_id and active_persona_id in ignored_personas:
        return False, "SUPPRESSED_BY_IGNORED_PERSONAS"

    ignored_chars = entry.get('ignored_characters', [])
    for cid in active_character_ids:
        if cid in ignored_chars:
            return False, "SUPPRESSED_BY_IGNORED_CHARACTERS"

    # 2. Primary key check
    primary_keys = entry.get('keys', [])
    matched_primary = []
    for k in primary_keys:
        # Word boundary matching
        pattern = r'\b' + re.escape(k.strip()) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            matched_primary.append(k)

    if not matched_primary:
        return False, "NO_PRIMARY_KEY_MATCH"

    # 3. Selective logic check
    selective = entry.get('selective', False)
    if not selective:
        return True, f"TRIGGERED_NON_SELECTIVE (matched: {matched_primary})"

    secondary_keys = entry.get('secondary_keys', [])
    key_logic = entry.get('key_logic', 'AND_ANY')

    matched_secondary = []
    for sk in secondary_keys:
        pattern = r'\b' + re.escape(sk.strip()) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            matched_secondary.append(sk)

    if key_logic == 'AND_ANY':
        if matched_secondary:
            return True, f"TRIGGERED_SELECTIVE_AND_ANY (primary: {matched_primary}, secondary: {matched_secondary})"
        else:
            return False, "SELECTIVE_BLOCKED_NO_SECONDARY_KEY"
    elif key_logic == 'AND_ALL':
        if len(matched_secondary) == len(secondary_keys):
            return True, f"TRIGGERED_SELECTIVE_AND_ALL"
        else:
            return False, "SELECTIVE_BLOCKED_MISSING_SECONDARY_KEYS"
    else:
        return False, f"UNKNOWN_KEY_LOGIC_{key_logic}"


class TestPersonaProtectionsAdversarial(unittest.TestCase):
    """Adversarial stress-testing of Persona protection flags and trigger engine."""

    def setUp(self):
        self.primary_data = load_repo_json('FINAL/Svartulfr_NPC_Primary.json')
        self.entries_by_id = {
            (e.get('entry_id') or e.get('id')): e for e in self.primary_data['entries']
        }
        self.alyssa = self.entries_by_id['alyssa_world_dossier_2b54a223']
        self.jasper = self.entries_by_id['Vcj4h2TL4Usola2A4OOl6']

    def test_persona_flags_exact_specification(self):
        """Verify Alyssa and Jasper possess exact required flags in entries and lexicon across mirrors."""
        check_files = [
            'FINAL/Svartulfr_NPC_Primary.json',
            'lorebooks/optimized/Svartulfr_NPC_Primary.json'
        ]
        expected_sec_keys = ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']

        for rel_path in check_files:
            data = load_repo_json(rel_path)
            for pool_key in ['entries', 'lexicon']:
                pool = data[pool_key]
                by_id = {(e.get('entry_id') or e.get('id')): e for e in pool}
                
                # Check Alyssa
                self.assertIn('alyssa_world_dossier_2b54a223', by_id, f"Alyssa missing in {rel_path} [{pool_key}]")
                a = by_id['alyssa_world_dossier_2b54a223']
                self.assertIs(a.get('selective'), True, f"Alyssa selective must be bool True in {rel_path} [{pool_key}]")
                self.assertEqual(a.get('secondary_keys'), expected_sec_keys, f"Alyssa secondary keys mismatch in {rel_path}")
                self.assertEqual(a.get('key_logic'), 'AND_ANY', f"Alyssa key_logic mismatch in {rel_path}")
                self.assertEqual(a.get('ignored_characters'), ['_6exg3yPfe2eCDK4hTftkh'], f"Alyssa ignored_characters mismatch in {rel_path}")
                self.assertEqual(a.get('ignored_personas'), ['persona_1786335754946'], f"Alyssa ignored_personas mismatch in {rel_path}")
                
                # Check Jasper
                self.assertIn('Vcj4h2TL4Usola2A4OOl6', by_id, f"Jasper missing in {rel_path} [{pool_key}]")
                j = by_id['Vcj4h2TL4Usola2A4OOl6']
                self.assertIs(j.get('selective'), True, f"Jasper selective must be bool True in {rel_path} [{pool_key}]")
                self.assertEqual(j.get('secondary_keys'), expected_sec_keys, f"Jasper secondary keys mismatch in {rel_path}")
                self.assertEqual(j.get('key_logic'), 'AND_ANY', f"Jasper key_logic mismatch in {rel_path}")
                self.assertEqual(j.get('ignored_characters'), ['_t4J9aQNJM36cUKAP4wB4U'], f"Jasper ignored_characters mismatch in {rel_path}")
                self.assertEqual(j.get('ignored_personas'), ['1792155173728'], f"Jasper ignored_personas mismatch in {rel_path}")

    def test_adversarial_alyssa_persona_play_immunity(self):
        """Simulate player playing as Persona Alyssa: assert zero triggers under aggressive adversarial prompts."""
        alyssa_persona_id = 'persona_1786335754946'
        
        attack_prompts = [
            "Hi, my name is Alyssa Douglas.",
            "Alyssa, please heal this wound.",
            "Open the Dossier for Alyssa Douglas immediately.",
            "Voglio consultare la scheda e l'archivio segreto di Alyssa.",
            "Database Profilo Alyssa: visualizza dati medici.",
            "The White Moon Alyssa steps forward with a smile.",
            "Dossier Scheda Archivio Database Profilo Alyssa Hvit Douglas-Bloodmoon"
        ]

        for prompt in attack_prompts:
            triggered, reason = simulate_wyvern_trigger(self.alyssa, prompt, active_persona_id=alyssa_persona_id)
            self.assertFalse(triggered, f"VULNERABILITY: Alyssa dossier triggered during Alyssa persona play on prompt: '{prompt}' (Reason: {reason})")
            self.assertEqual(reason, "SUPPRESSED_BY_IGNORED_PERSONAS")

    def test_adversarial_jasper_persona_play_immunity(self):
        """Simulate player playing as Persona Jasper: assert zero triggers under aggressive adversarial prompts."""
        jasper_persona_id = '1792155173728'

        attack_prompts = [
            "Jasper, slice that network node now.",
            "Yo DJ Frequency, drop that bass.",
            "Open the Jasper Dossier from the archive.",
            "Visualizza la scheda tecnica e l'archivio database di Jasper Svartr.",
            "Shadow Wolf Jasper accessing corporate database profilo.",
            "Dossier Scheda Archivio Database Profilo Jasper Douglas-Bloodmoon"
        ]

        for prompt in attack_prompts:
            triggered, reason = simulate_wyvern_trigger(self.jasper, prompt, active_persona_id=jasper_persona_id)
            self.assertFalse(triggered, f"VULNERABILITY: Jasper dossier triggered during Jasper persona play on prompt: '{prompt}' (Reason: {reason})")
            self.assertEqual(reason, "SUPPRESSED_BY_IGNORED_PERSONAS")

    def test_adversarial_character_card_suppression(self):
        """Verify that when Alyssa or Jasper's Character Cards are active in the party, dossier entries do not fire."""
        # Active Alyssa card
        triggered, reason = simulate_wyvern_trigger(
            self.alyssa, "Show me the Alyssa Dossier", active_character_ids=['_6exg3yPfe2eCDK4hTftkh']
        )
        self.assertFalse(triggered, "Alyssa dossier must be suppressed when her Character Card is in party.")
        self.assertEqual(reason, "SUPPRESSED_BY_IGNORED_CHARACTERS")

        # Active Jasper card
        triggered, reason = simulate_wyvern_trigger(
            self.jasper, "Open the Jasper Database Dossier", active_character_ids=['_t4J9aQNJM36cUKAP4wB4U']
        )
        self.assertFalse(triggered, "Jasper dossier must be suppressed when his Character Card is in party.")
        self.assertEqual(reason, "SUPPRESSED_BY_IGNORED_CHARACTERS")

    def test_spurious_trigger_resistance_in_casual_play(self):
        """
        When playing as a 3rd party persona, verify casual dialogue NEVER spuriously triggers the 14k-20k char dossiers.
        """
        third_party_persona = 'user_persona_random_student_12345'

        # Test A: Prompts containing Alyssa's name without secondary keys
        alyssa_casual = [
            "Hi Alyssa, how are you feeling today?",
            "I heard Alyssa talking by the fountain.",
            "Is the White Moon Alyssa going to the campus dance?",
            "I asked Alyssa Douglas if she could help me with my biology homework."
        ]
        for prompt in alyssa_casual:
            trig, reason = simulate_wyvern_trigger(self.alyssa, prompt, active_persona_id=third_party_persona)
            self.assertFalse(trig, f"SPURIOUS TRIGGER: Alyssa dossier triggered on: '{prompt}'")
            self.assertEqual(reason, "SELECTIVE_BLOCKED_NO_SECONDARY_KEY")

        # Test B: Prompts containing Jasper's name without secondary keys
        jasper_casual = [
            "Jasper told me he'd be at the library later.",
            "Hey Jasper, pass me the ethernet cable.",
            "Is Jasper Svartr attending the evening lab?",
            "Shadow Wolf Jasper was seen near the server room."
        ]
        for prompt in jasper_casual:
            trig, reason = simulate_wyvern_trigger(self.jasper, prompt, active_persona_id=third_party_persona)
            self.assertFalse(trig, f"SPURIOUS TRIGGER: Jasper dossier triggered on: '{prompt}'")
            self.assertEqual(reason, "SELECTIVE_BLOCKED_NO_SECONDARY_KEY")

        # Test C: General prompts without character names (e.g. secondary keys alone)
        general_prompts = [
            "The Douglas family is very influential in Blackwood City.",
            "Ho archiviato il dossier sul caso.",
            "Il database dell'universita e stato aggiornato.",
            "Hai compilato la scheda di iscrizione?"
        ]
        for prompt in general_prompts:
            trig_a, reason_a = simulate_wyvern_trigger(self.alyssa, prompt, active_persona_id=third_party_persona)
            self.assertFalse(trig_a, f"SPURIOUS TRIGGER: Alyssa dossier triggered on: '{prompt}'")
            self.assertEqual(reason_a, "NO_PRIMARY_KEY_MATCH")

            trig_j, reason_j = simulate_wyvern_trigger(self.jasper, prompt, active_persona_id=third_party_persona)
            self.assertFalse(trig_j, f"SPURIOUS TRIGGER: Jasper dossier triggered on: '{prompt}'")
            self.assertEqual(reason_j, "NO_PRIMARY_KEY_MATCH")

    def test_intentional_query_activation_for_third_party(self):
        """Verify that deliberate queries with both name and secondary keys DO activate when intended."""
        third_party_persona = 'user_persona_detective_hunter_999'

        valid_queries = [
            (self.alyssa, "Apro il dossier di Alyssa per verificare le sue abilità mediche."),
            (self.alyssa, "Consulta la scheda di Alyssa Douglas nel database."),
            (self.alyssa, "Accedi all'archivio relativo al profilo di Alyssa."),
            (self.jasper, "Scarica il dossier di Jasper dal terminale."),
            (self.jasper, "Apri la scheda di Jasper Douglas."),
            (self.jasper, "Cerca nell'archivio il profilo di Jasper Svartr.")
        ]

        for entry, query in valid_queries:
            triggered, reason = simulate_wyvern_trigger(entry, query, active_persona_id=third_party_persona)
            self.assertTrue(triggered, f"Intentional lookup failed to trigger on: '{query}' (Reason: {reason})")


class TestTokenBudgetsAndStressHarness(unittest.TestCase):
    """Stress tests for token budgets and context limits."""

    def test_lorebook_declared_token_budgets(self):
        """Assert declared token_budget in root objects match architectural requirements (7500 Primary, 5000 others)."""
        expected_budgets = {
            'FINAL/Svartulfr_NPC_Primary.json': 7500,
            'lorebooks/optimized/Svartulfr_NPC_Primary.json': 7500,
            'FINAL/Svartulfr_NPC_Secondary.json': 5000,
            'lorebooks/optimized/Svartulfr_NPC_Secondary.json': 5000,
            'FINAL/Svartulfr_Lorebook_I.json': 5000,
            'lorebooks/optimized/Svartulfr_Lorebook_I.json': 5000,
            'FINAL/Svartulfr_Lorebook_II.json': 5000,
            'lorebooks/optimized/Svartulfr_Lorebook_II.json': 5000,
            'FINAL/Svartulfr_Lorebook_III.json': 5000,
            'lorebooks/optimized/Svartulfr_Lorebook_III.json': 5000,
            'lorebooks/optimized/Svartulfr_Location.json': 5000
        }

        for rel_path, expected in expected_budgets.items():
            d = load_repo_json(rel_path)
            actual = d.get('token_budget')
            self.assertEqual(actual, expected, f"Token budget mismatch in {rel_path}: got {actual}, expected {expected}")

    def test_every_single_entry_within_budget(self):
        """Exhaustively verify that 100% of entries in all 11 files fit within their declared token budgets."""
        for rel_path in MODIFIED_FILES:
            d = load_repo_json(rel_path)
            budget = d.get('token_budget', 5000)
            for idx, entry in enumerate(d['entries']):
                eid = entry.get('entry_id') or entry.get('id')
                name = entry.get('name')
                content = entry.get('content', '')
                # Highly conservative token estimation: 3.5 characters per token
                est_tokens = len(content) / 3.5
                self.assertLessEqual(
                    est_tokens, budget,
                    f"Entry #{idx} ({eid} - '{name}') in {rel_path} exceeds token budget: "
                    f"{len(content)} chars -> ~{est_tokens:.0f} tokens > {budget}"
                )

    def test_milestone2_target_entries_token_headroom(self):
        """Verify exact token estimates and headroom for all 10 target entries touched in Milestone 2."""
        for file_path, eid, budget in TARGET_ENTRIES:
            d = load_repo_json(file_path)
            by_id = {(e.get('entry_id') or e.get('id')): e for e in d['entries']}
            self.assertIn(eid, by_id, f"Target entry {eid} not found in {file_path}")
            e = by_id[eid]
            c = e.get('content', '')
            chars = len(c)
            # 3.5 chars / token conservative bound
            est_tokens_35 = chars / 3.5
            headroom = budget - est_tokens_35
            headroom_pct = (headroom / budget) * 100.0

            # Assert at least 20% headroom remains on every entry (even Alyssa's massive 20k dossier has ~24% headroom in 7500)
            self.assertGreaterEqual(
                headroom_pct, 20.0,
                f"Entry {eid} in {file_path} has insufficient headroom: only {headroom_pct:.1f}% ({headroom:.0f} tokens) left in {budget}"
            )


class TestRegressionAndParityVerification(unittest.TestCase):
    """Rigorous checks ensuring zero regressions, complete parity, and compliance with all formatting rules."""

    def test_entries_lexicon_byte_for_byte_parity(self):
        """Assert entries and lexicon arrays are 100% identical byte-for-byte across all 11 files."""
        for rel_path in MODIFIED_FILES:
            d = load_repo_json(rel_path)
            entries = d.get('entries', [])
            lexicon = d.get('lexicon', [])
            self.assertEqual(len(entries), len(lexicon), f"Length mismatch in {rel_path}: entries({len(entries)}) != lexicon({len(lexicon)})")
            self.assertEqual(entries, lexicon, f"Byte-for-byte mismatch between entries and lexicon in {rel_path}")

    def test_cross_folder_mirror_identity(self):
        """Assert that FINAL/ and lorebooks/optimized/ mirrors are identical."""
        for p1, p2 in PAIRED_MIRRORS:
            d1 = load_repo_json(p1)
            d2 = load_repo_json(p2)
            self.assertEqual(d1, d2, f"Mirror desynchronization between {p1} and {p2}")

    def test_exact_entry_counts(self):
        """Assert total entry counts for each lorebook match canonical targets."""
        expected_counts = {
            'FINAL/Svartulfr_Lorebook_I.json': 239,
            'FINAL/Svartulfr_Lorebook_II.json': 143,
            'FINAL/Svartulfr_Lorebook_III.json': 47,
            'lorebooks/optimized/Svartulfr_Location.json': 226,
            'FINAL/Svartulfr_NPC_Secondary.json': 212,
            'FINAL/Svartulfr_NPC_Primary.json': 99
        }
        for path, count in expected_counts.items():
            d = load_repo_json(path)
            self.assertEqual(len(d['entries']), count, f"Entry count mismatch in {path}: expected {count}, got {len(d['entries'])}")

    def test_zero_age_macros(self):
        """Exhaustively verify 0 {{age}} macros exist across all 11 files."""
        for rel_path in MODIFIED_FILES:
            abs_path = REPO_ROOT / rel_path
            with open(abs_path, 'r', encoding='utf-8') as f:
                raw_text = f.read()
            self.assertNotIn('{{age}}', raw_text, f"VIOLATION: '{{{{age}}}}' macro detected in {rel_path}")

    def test_umbrella_keyword_eradication_on_npcs(self):
        """Verify zero broad/umbrella keys exist across all 311 NPC entries in Primary and Secondary."""
        npc_files = [
            'FINAL/Svartulfr_NPC_Primary.json',
            'FINAL/Svartulfr_NPC_Secondary.json'
        ]
        for rel_path in npc_files:
            d = load_repo_json(rel_path)
            for idx, entry in enumerate(d['entries']):
                keys = [k.lower().strip() for k in entry.get('keys', [])]
                for bk in BROAD_KEYS:
                    self.assertNotIn(
                        bk, keys,
                        f"Broad key '{bk}' found on NPC #{idx} ('{entry.get('name')}') in {rel_path}"
                    )

    def test_st_brugge_location_cleaning(self):
        """Verify St. Brugge Location entry #51 (ulTwlYo2jqObA7l_bFoa5) has purged umbrella keys."""
        loc_data = load_repo_json('lorebooks/optimized/Svartulfr_Location.json')
        by_id = {(e.get('entry_id') or e.get('id')): e for e in loc_data['entries']}
        self.assertIn('ulTwlYo2jqObA7l_bFoa5', by_id)
        e = by_id['ulTwlYo2jqObA7l_bFoa5']
        
        prohibited_keys = {'Douglas', 'Blackwood', 'Seven Hills', 'private academy'}
        for pk in prohibited_keys:
            self.assertNotIn(pk, e['keys'], f"Prohibited key '{pk}' still found in St. Brugge location keys")

        # Confirm specific valid keys remain
        self.assertIn('St. Brugge Private Academy', e['keys'])
        self.assertIn('St. Brugge', e['keys'])

    def test_larek_steeltooth_schema_normalization(self):
        """Verify Larek Steeltooth (entry #211) has fully normalized canonical NPC schema."""
        sec_data = load_repo_json('FINAL/Svartulfr_NPC_Secondary.json')
        by_id = {(e.get('entry_id') or e.get('id')): e for e in sec_data['entries']}
        self.assertIn('npc_larek_steeltooth', by_id)
        larek = by_id['npc_larek_steeltooth']

        self.assertEqual(larek.get('type'), 'npc')
        self.assertEqual(larek.get('name'), 'Larek Steeltooth')
        self.assertEqual(larek.get('avatar'), 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public')
        self.assertTrue(larek.get('custom_avatar_regex'))
        self.assertEqual(larek.get('lines_parsed'), 1)
        self.assertIn('npc_info', larek)
        self.assertEqual(larek['npc_info'].get('first_name'), 'Larek')
        self.assertEqual(larek['npc_info'].get('last_name'), 'Steeltooth')
        self.assertTrue(larek.get('scan_persona'))
        self.assertTrue(larek.get('whole_words_only'))

    def test_father_revazhael_entry_canonical_attributes(self):
        """Verify Father Revazhael entry (#23, jmh0MajEsRwrm4UYU14mY) attributes."""
        sec_data = load_repo_json('FINAL/Svartulfr_NPC_Secondary.json')
        by_id = {(e.get('entry_id') or e.get('id')): e for e in sec_data['entries']}
        self.assertIn('jmh0MajEsRwrm4UYU14mY', by_id)
        rev = by_id['jmh0MajEsRwrm4UYU14mY']

        self.assertEqual(rev.get('name'), 'Father Revazhael (Rev)')
        self.assertEqual(rev.get('type'), 'npc')
        expected_keys = ['Father Revazhael', 'Padre Revazhael', 'Father Rev', 'Padre Rev', 'Revazhael', 'Rev']
        self.assertEqual(rev.get('keys'), expected_keys)
        self.assertIn('TRUE NAME SECRET', rev.get('content', ''))
        self.assertIn('St. Brugge Private Academy', rev.get('content', ''))
        self.assertIn('Superior Demon', rev.get('content', ''))

    def test_formatting_discipline_in_target_entries(self):
        """Assert zero em-dashes and positive framing in all 10 target entries."""
        negative_patterns = ['no human ears', 'senza orecchie umane', 'privo di orecchie umane', 'prive di orecchie umane']

        for file_path, eid, _ in TARGET_ENTRIES:
            d = load_repo_json(file_path)
            by_id = {(e.get('entry_id') or e.get('id')): e for e in d['entries']}
            self.assertIn(eid, by_id)
            e = by_id[eid]
            raw_entry = json.dumps(e, ensure_ascii=False)

            # Zero em-dashes
            self.assertNotIn('—', raw_entry, f"Em-dash detected in target entry {eid} in {file_path}")

            # Zero negative framing
            raw_lower = raw_entry.lower()
            for pat in negative_patterns:
                self.assertNotIn(pat, raw_lower, f"Negative framing pattern '{pat}' detected in entry {eid} in {file_path}")


if __name__ == '__main__':
    unittest.main()
