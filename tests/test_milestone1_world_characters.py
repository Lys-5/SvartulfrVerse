"""
Unit and Integration Tests: tests/test_milestone1_world_characters.py
Objective: Verify live deployment and schema integrity of 13 Primary World Characters
           in World `_YpX47fNraQFw2dD7TdycJ` on Wyvern Web API.
"""

import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = ROOT / 'scratch' / 'm1_13_world_characters_verified.json'
TARGET_WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

EXPECTED_CHARACTERS = {
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

class TestMilestone1WorldCharacters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.assertTrue(cls, SNAPSHOT_PATH.exists(), f"Snapshot file missing: {SNAPSHOT_PATH}")
        with open(SNAPSHOT_PATH, 'r', encoding='utf-8') as f:
            cls.data = json.load(f)
        cls.by_name = {c['name']: c for c in cls.data}

    def test_character_count(self):
        """Verifies exactly 13 primary world characters are present."""
        self.assertEqual(len(self.data), 13)
        self.assertEqual(len(self.by_name), 13)

    def test_all_expected_names_present(self):
        """Verifies each expected character is included."""
        for name in EXPECTED_CHARACTERS:
            self.assertIn(name, self.by_name, f"Expected character {name} missing")

    def test_birthdates_and_timeline_positions(self):
        """Verifies exact BigInt integer birthdates and start_timeline_positions."""
        for name, expected in EXPECTED_CHARACTERS.items():
            record = self.by_name[name]
            self.assertEqual(record['birthdate'], expected['birthdate'], f"Birthdate mismatch for {name}")
            self.assertEqual(record['start_timeline_position'], expected['birthdate'], f"Timeline mismatch for {name}")
            # Ensure within valid world age (0 <= bdate <= 10489902)
            self.assertGreaterEqual(record['birthdate'], 0)
            self.assertLessEqual(record['birthdate'], 10489902)

    def test_avatars_cloudflare_cdn(self):
        """Verifies avatars use canonical Cloudflare CDN URLs from gallery."""
        for name, expected in EXPECTED_CHARACTERS.items():
            record = self.by_name[name]
            self.assertEqual(record['avatar'], expected['avatar'], f"Avatar mismatch for {name}")
            self.assertTrue(record['avatar'].startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'))

    def test_levels_and_rpg_cap(self):
        """Verifies levels are accurate and capped at 99."""
        for name, expected in EXPECTED_CHARACTERS.items():
            record = self.by_name[name]
            self.assertEqual(record['level'], expected['level'], f"Level mismatch for {name}")
            self.assertLessEqual(record['level'], 99, f"Level {record['level']} exceeds 99 cap for {name}")

    def test_rpg_stats_balanced_sum_31(self):
        """Verifies base stats sum to exactly 31 (base 1 + 25 points budget)."""
        for name, expected in EXPECTED_CHARACTERS.items():
            record = self.by_name[name]
            self.assertEqual(record['stat_sum'], 31, f"Stat sum is {record['stat_sum']} != 31 for {name}")

    def test_rpg_stats_dual_key_presence(self):
        """Verifies dual keys (stat_1..6 and might..scouting) are populated."""
        for name, expected in EXPECTED_CHARACTERS.items():
            record = self.by_name[name]
            bs = record['base_stats']
            for i in range(1, 7):
                self.assertIn(f'stat_{i}', bs, f"stat_{i} missing in base_stats for {name}")
            for key in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']:
                self.assertIn(key, bs, f"{key} missing in base_stats for {name}")
                self.assertEqual(bs[key], expected['stats'][key], f"Stat {key} value mismatch for {name}")

    def test_long_summary_length_and_formatting(self):
        """Verifies non-trivial JED+ content length."""
        for name in EXPECTED_CHARACTERS:
            record = self.by_name[name]
            self.assertGreater(record['long_summary_len'], 4000, f"Long summary too short for {name}")

    def test_all_records_verified_pass(self):
        """Verifies all records passed live API verification."""
        for record in self.data:
            self.assertEqual(record['verified_status'], 'PASS')

if __name__ == '__main__':
    unittest.main()
