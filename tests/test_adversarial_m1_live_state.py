"""
Adversarial Stress Test Suite: tests/test_adversarial_m1_live_state.py
Objective: Empirically stress-test Milestone 1 live state in World `_YpX47fNraQFw2dD7TdycJ`
           ("Svartúlfr — Blackwood & Solarton") on Wyvern Web API.

Author: challenger_m1_2 (empirical-challenger)
Target: 13 Primary World Characters
"""

import unittest
import json
import re
import urllib.request
import urllib.error
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
TARGET_WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
API_URL = f"https://app.wyvern.chat/api/worlds/characters/world/{TARGET_WORLD_ID}"
SNAPSHOT_PATH = ROOT / 'scratch' / 'm1_13_world_characters_verified.json'

sys.path.append(str(ROOT / 'scratch'))
try:
    import refresh_token
except ImportError:
    refresh_token = None

CANONICAL_SPEC = {
    'Erik Ulfr Douglas': {
        'level': 55,
        'birthdate': 10009344,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public',
        'stats': {'might': 7, 'resilience': 7, 'agility': 4, 'wit': 5, 'presence': 7, 'scouting': 1}
    },
    'Logan Járn Douglas': {
        'level': 49,
        'birthdate': 10054920,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public',
        'stats': {'might': 7, 'resilience': 6, 'agility': 6, 'wit': 4, 'presence': 5, 'scouting': 3}
    },
    'Edric Douglas': {
        'level': 13,
        'birthdate': 10371552,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public',
        'stats': {'might': 3, 'resilience': 3, 'agility': 7, 'wit': 5, 'presence': 5, 'scouting': 8}
    },
    'Noah Loki Douglas Bloodmoon': {
        'level': 25,
        'birthdate': 10262928,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public',
        'stats': {'might': 6, 'resilience': 6, 'agility': 5, 'wit': 6, 'presence': 6, 'scouting': 2}
    },
    'Malachia Björn Douglas Bloodmoon': {
        'level': 28,
        'birthdate': 10244064,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public',
        'stats': {'might': 8, 'resilience': 7, 'agility': 5, 'wit': 4, 'presence': 5, 'scouting': 2}
    },
    'Jasper Svartr Douglas Bloodmoon': {
        'level': 19,
        'birthdate': 10320312,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public',
        'stats': {'might': 4, 'resilience': 3, 'agility': 8, 'wit': 9, 'presence': 3, 'scouting': 4}
    },
    'Alyssa Hvit Douglas Bloodmoon': {
        'level': 19,
        'birthdate': 10320312,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public',
        'stats': {'might': 2, 'resilience': 4, 'agility': 4, 'wit': 7, 'presence': 8, 'scouting': 6}
    },
    'Wulfnic Báleygr Bloodmoon': {
        'level': 99,
        'birthdate': 0,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public',
        'stats': {'might': 8, 'resilience': 8, 'agility': 5, 'wit': 3, 'presence': 5, 'scouting': 2}
    },
    'Zefir Hvitskog': {
        'level': 99,
        'birthdate': 176424,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bdd8961e-a68a-4c6b-b4e1-29a26db37e00/public',
        'stats': {'might': 5, 'resilience': 4, 'agility': 9, 'wit': 6, 'presence': 3, 'scouting': 4}
    },
    'Mackenzie Sanchez-Rogers': {
        'level': 19,
        'birthdate': 10316496,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public',
        'stats': {'might': 8, 'resilience': 7, 'agility': 7, 'wit': 3, 'presence': 3, 'scouting': 3}
    },
    'Finnegan Novak': {
        'level': 19,
        'birthdate': 10317984,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/75456c02-dddc-4879-7822-ab7c4628f600/public',
        'stats': {'might': 6, 'resilience': 6, 'agility': 8, 'wit': 3, 'presence': 4, 'scouting': 4}
    },
    'Sierra Cruz': {
        'level': 18,
        'birthdate': 10323648,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public',
        'stats': {'might': 7, 'resilience': 6, 'agility': 3, 'wit': 8, 'presence': 3, 'scouting': 4}
    },
    'Scarlett Rose': {
        'level': 20,
        'birthdate': 10307808,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e96d176a-47e4-4829-2af4-7cd6ae239100/public',
        'stats': {'might': 2, 'resilience': 3, 'agility': 6, 'wit': 6, 'presence': 9, 'scouting': 5}
    }
}

STAT_KEYS_MAPPING = {
    'stat_1': 'might',
    'stat_2': 'resilience',
    'stat_3': 'agility',
    'stat_4': 'wit',
    'stat_5': 'presence',
    'stat_6': 'scouting'
}


class TestAdversarialM1LiveState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Fetch directly from live Wyvern API
        token = None
        token_path = ROOT / 'scratch' / 'wyvern_token.txt'
        if token_path.exists():
            token = token_path.read_text(encoding='utf-8').strip()
        if not token and refresh_token and hasattr(refresh_token, 'refresh'):
            try:
                token = refresh_token.refresh()
            except Exception as e:
                print(f"[!] Warning: Token refresh failed: {e}")

        cls.live_characters = []
        cls.source = "UNKNOWN"
        if token:
            headers = {
                'Authorization': f'Bearer {token}',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
            req = urllib.request.Request(API_URL, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    cls.live_characters = json.loads(resp.read().decode('utf-8'))
                    cls.source = "LIVE_API"
            except Exception as e:
                print(f"[!] Warning: Could not fetch from live API: {e}")

        # If live API fetch failed or returned empty, fallback to verified snapshot
        if not cls.live_characters:
            if SNAPSHOT_PATH.exists():
                with open(SNAPSHOT_PATH, 'r', encoding='utf-8') as f:
                    cls.live_characters = json.load(f)
                    cls.source = "SNAPSHOT"

        cls.by_name = {
            (c.get('display_name') or c.get('name')): c
            for c in cls.live_characters
        }

    def test_live_api_source_freshness(self):
        """Verify that characters were fetched directly from the live Wyvern API."""
        self.assertEqual(self.source, "LIVE_API", f"Expected live data from API, but source was {self.source}")

    def test_erik_record_id_retention(self):
        """Stress-test that Erik's pre-existing MongoDB ID was retained to prevent orphaned pointers."""
        erik = self.by_name['Erik Ulfr Douglas']
        erik_id = erik.get('_id') or erik.get('id')
        self.assertEqual(erik_id, '_qfaywY2yfrGWcxPBdmURD', f"Erik ID was not preserved! Got: {erik_id}")

    def test_zero_broad_umbrella_keys(self):
        """Stress-test anti-collision: no NPC or World Character should have bare broad umbrella keys."""
        broad_keys = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega', 'werewolves', 'vampires', 'students'}
        for name in CANONICAL_SPEC:
            record = self.by_name[name]
            keys = [k.lower().strip() for k in (record.get('keys') or [])]
            for bk in broad_keys:
                self.assertNotIn(bk, keys, f"Character {name} has forbidden umbrella key: '{bk}'")

    # 1. Cardinality and Population Bounds
    def test_exact_character_population_cardinality(self):
        """Stress-test that the live world has exactly 13 primary characters (no ghost or duplicate records)."""
        self.assertEqual(len(self.live_characters), 13, f"Expected exactly 13 characters, found {len(self.live_characters)}")
        self.assertEqual(len(self.by_name), 13, f"Duplicate character names detected in live state! Unique names: {len(self.by_name)}")

    def test_all_canonical_names_present_without_spurious_records(self):
        """Stress-test that all expected canonical characters exist and no unknown records are present."""
        expected_names = set(CANONICAL_SPEC.keys())
        live_names = set(self.by_name.keys())
        missing = expected_names - live_names
        extra = live_names - expected_names
        self.assertEqual(missing, set(), f"Missing characters in live state: {missing}")
        self.assertEqual(extra, set(), f"Unexpected extra characters in live state: {extra}")

    # 2. Stat Sum and Boundary Conditions (Sum must be exactly 31)
    def test_stat_sums_strictly_equal_31(self):
        """Stress-test that both named and numbered stat blocks sum to exactly 31 (25-point budget + 6 base 1)."""
        for name, spec in CANONICAL_SPEC.items():
            record = self.by_name[name]
            rpg = record.get('rpg_stats') or {}
            base_stats = rpg.get('base_stats') or record.get('base_stats') or {}
            
            # Check numbered stats
            num_sum = sum(base_stats[f'stat_{i}'] for i in range(1, 7))
            self.assertEqual(num_sum, 31, f"{name}: stat_1..6 sum is {num_sum} != 31")

            # Check named stats
            named_sum = sum(base_stats[k] for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting'])
            self.assertEqual(named_sum, 31, f"{name}: named stats sum is {named_sum} != 31")

    def test_individual_stats_base_minimum_and_data_types(self):
        """Stress-test that every single stat is an int >= 1 and not float, str, or bool."""
        for name in CANONICAL_SPEC:
            record = self.by_name[name]
            rpg = record.get('rpg_stats') or {}
            base_stats = rpg.get('base_stats') or record.get('base_stats') or {}

            for i in range(1, 7):
                k = f'stat_{i}'
                val = base_stats.get(k)
                self.assertIsInstance(val, int, f"{name} {k} is type {type(val)}, expected int")
                self.assertNotIsInstance(val, bool, f"{name} {k} is bool {val}, expected int")
                self.assertGreaterEqual(val, 1, f"{name} {k} value {val} is below base 1 minimum!")

            for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']:
                val = base_stats.get(k)
                self.assertIsInstance(val, int, f"{name} {k} is type {type(val)}, expected int")
                self.assertNotIsInstance(val, bool, f"{name} {k} is bool {val}, expected int")
                self.assertGreaterEqual(val, 1, f"{name} {k} value {val} is below base 1 minimum!")

    # 3. Dual-Key Symmetry (stat_1..6 must identically equal named attributes)
    def test_dual_key_stat_symmetry(self):
        """Stress-test that stat_1..6 and might..scouting are perfectly symmetrical and cross-matched."""
        for name, spec in CANONICAL_SPEC.items():
            record = self.by_name[name]
            rpg = record.get('rpg_stats') or {}
            base_stats = rpg.get('base_stats') or record.get('base_stats') or {}

            for num_k, named_k in STAT_KEYS_MAPPING.items():
                self.assertIn(num_k, base_stats, f"{name} missing {num_k}")
                self.assertIn(named_k, base_stats, f"{name} missing {named_k}")
                self.assertEqual(
                    base_stats[num_k], base_stats[named_k],
                    f"{name} dual-key mismatch: {num_k}={base_stats[num_k]} != {named_k}={base_stats[named_k]}"
                )
                expected_val = spec['stats'][named_k]
                self.assertEqual(
                    base_stats[named_k], expected_val,
                    f"{name} stat {named_k} has value {base_stats[named_k]}, expected canonical {expected_val}"
                )

    # 4. Level Cap Enforcement (Level <= 99)
    def test_level_cap_and_mortality_bounds(self):
        """Stress-test level bounds: all characters must have level <= 99, with immortals capped at 99."""
        for name, spec in CANONICAL_SPEC.items():
            record = self.by_name[name]
            rpg = record.get('rpg_stats') or {}
            level = rpg.get('level') if 'level' in rpg else record.get('level')
            
            self.assertIsInstance(level, int, f"{name} level is not an int: {type(level)}")
            self.assertNotIsInstance(level, bool, f"{name} level is a bool!")
            self.assertGreater(level, 0, f"{name} level must be > 0, got {level}")
            self.assertLessEqual(level, 99, f"{name} level {level} exceeds 99 cap!")

            expected_level = spec['level']
            self.assertEqual(level, expected_level, f"{name} level is {level}, expected {expected_level}")

        # Explicit check for Wulfnic and Zefir (immortals over 1000 years old)
        wulfnic = self.by_name['Wulfnic Báleygr Bloodmoon']
        wulfnic_level = (wulfnic.get('rpg_stats') or {}).get('level') or wulfnic.get('level')
        self.assertEqual(wulfnic_level, 99, f"Wulfnic level is {wulfnic_level}, MUST be capped at 99!")

        zefir = self.by_name['Zefir Hvitskog']
        zefir_level = (zefir.get('rpg_stats') or {}).get('level') or zefir.get('level')
        self.assertEqual(zefir_level, 99, f"Zefir level is {zefir_level}, MUST be capped at 99!")

    # 5. Timeline, Epoch Anchors, and BigInt Integrity
    def test_timeline_positions_and_birthdates(self):
        """Stress-test BigInt timeline bounds: birthdate == start_timeline_position, Wulfnic anchored at 0."""
        for name, spec in CANONICAL_SPEC.items():
            record = self.by_name[name]
            bdate = record.get('birthdate')
            tl_pos = record.get('start_timeline_position')

            self.assertIsInstance(bdate, int, f"{name} birthdate is not int: {type(bdate)}")
            self.assertIsInstance(tl_pos, int, f"{name} start_timeline_position is not int: {type(tl_pos)}")
            self.assertEqual(bdate, tl_pos, f"{name} birthdate ({bdate}) != start_timeline_position ({tl_pos})")
            self.assertEqual(bdate, spec['birthdate'], f"{name} birthdate mismatch with canonical spec")

            # World age bounds
            self.assertGreaterEqual(bdate, 0, f"{name} birthdate {bdate} is negative (breaks MongoDB index)!")
            self.assertLessEqual(bdate, 10489902, f"{name} birthdate {bdate} is in the future (> current world age)!")

        # Explicit boundary test for Wulfnic (born 824 AD, prior to epoch 827 AD)
        wulfnic = self.by_name['Wulfnic Báleygr Bloodmoon']
        self.assertEqual(wulfnic.get('birthdate'), 0, "Wulfnic MUST be anchored at 0 to avoid negative BigInt!")
        self.assertEqual(wulfnic.get('start_timeline_position'), 0, "Wulfnic timeline position MUST be 0!")

    # 6. Cloudflare CDN Avatar Delivery
    def test_avatar_canonical_cdn_delivery(self):
        """Stress-test avatar URLs: HTTPS Cloudflare CDN from gallery, non-empty, matching canonical spec."""
        for name, spec in CANONICAL_SPEC.items():
            record = self.by_name[name]
            avatar = record.get('avatar')
            self.assertIsInstance(avatar, str, f"{name} avatar is not string")
            self.assertTrue(avatar.startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'), f"{name} avatar not on Cloudflare CDN: {avatar}")
            self.assertTrue(avatar.endswith('/public'), f"{name} avatar does not end in /public: {avatar}")
            self.assertEqual(avatar, spec['avatar'], f"{name} avatar URL does not match canonical spec")

    # 7. JED+ Formatting Discipline and Section Integrity
    def test_jed_structure_and_mandatory_sections(self):
        """Stress-test JED+ prose: bracket block [...] on line 1, BACKSTORY, VOICE & BEHAVIOR, and closing thematic block."""
        for name in CANONICAL_SPEC:
            record = self.by_name[name]
            long_summary = record.get('long_summary') or ''
            
            # If we are testing raw API object, long_summary is present
            if not long_summary and 'long_summary_len' in record:
                # In snapshot, long_summary_len was recorded
                self.assertGreater(record['long_summary_len'], 4000)
                continue

            self.assertGreater(len(long_summary), 4000, f"{name} description too short ({len(long_summary)} chars)")
            
            # 1. Bracket block on line 1
            lines = [l for l in long_summary.splitlines() if l.strip()]
            self.assertTrue(lines[0].startswith('['), f"{name} line 1 must start with '[' bracket block, got: {lines[0][:30]}")
            self.assertTrue(']' in lines[0] or ']' in long_summary[:500], f"{name} missing closing bracket ']' in header")
            self.assertIn('NAME:', long_summary[:200], f"{name} bracket block missing 'NAME:'")

            # 2. Mandatory prose sections
            self.assertIn('BACKSTORY:', long_summary, f"{name} missing BACKSTORY: section")
            has_voice = ('VOICE & BEHAVIOR:' in long_summary or 'VOICE AND BEHAVIOR:' in long_summary)
            self.assertTrue(has_voice, f"{name} missing VOICE & BEHAVIOR: section")

            # 3. Family / Clan section
            has_fam_clan = ('FAMILY & PACK:' in long_summary or 'CLAN AND COMPANY:' in long_summary or 'RELATIONSHIPS:' in long_summary or 'FAMILY & CONNECTIONS:' in long_summary or 'FAMILY & CIRCLE:' in long_summary or 'FACTION & ALLIANCES:' in long_summary)
            self.assertTrue(has_fam_clan, f"{name} missing FAMILY & PACK / CLAN AND COMPANY section")

    # 8. Absolute Zero Em-Dashes Across All Live Fields
    def test_absolute_zero_em_dashes(self):
        """Stress-test format discipline: assert exactly 0 em-dashes (—, \\u2014) in descriptions and summaries."""
        em_dash = '\u2014'
        horizontal_bar = '\u2015'

        for name in CANONICAL_SPEC:
            record = self.by_name[name]

            # Check all text fields
            text_fields = ['long_summary', 'summary', 'display_description', 'final_instructions']
            for field in text_fields:
                val = record.get(field)
                if isinstance(val, str):
                    em_count = val.count(em_dash)
                    bar_count = val.count(horizontal_bar)
                    self.assertEqual(
                        em_count, 0,
                        f"EM-DASH VIOLATION: {name} field '{field}' contains {em_count} em-dash(es) ('—')!"
                    )
                    self.assertEqual(
                        bar_count, 0,
                        f"HORIZONTAL BAR VIOLATION: {name} field '{field}' contains {bar_count} horizontal bar(s) ('―')!"
                    )
                    self.assertNotIn('&mdash;', val, f"HTML EM-DASH VIOLATION: {name} field '{field}' contains '&mdash;'!")

    # 9. Format Discipline Instruction
    def test_final_instructions_enforces_format_discipline(self):
        """Stress-test final_instructions field to confirm mandatory format discipline is attached."""
        for name in CANONICAL_SPEC:
            record = self.by_name[name]
            final_inst = record.get('final_instructions')
            if final_inst is not None:
                self.assertIn('Format discipline:', final_inst, f"{name} final_instructions missing 'Format discipline:'")
                self.assertIn('Never use the em dash', final_inst, f"{name} final_instructions missing em dash ban")
                self.assertIn('dialogue in quotes', final_inst, f"{name} final_instructions missing dialogue in quotes")


if __name__ == '__main__':
    unittest.main()
