#!/usr/bin/env python3
"""
tests/test_empirical_challenger_m1.py

Independent Empirical Challenger Test Suite for Milestone 1:
Validates live Wyvern Web API state for World `_YpX47fNraQFw2dD7TdycJ`
("Svartúlfr — Blackwood & Solarton") with zero trust in local snapshots or worker claims.

Assertions:
1. Live network query to GET https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ
2. Exact 13 Primary World Characters (no duplicates, no orphans, 100% canonical coverage)
3. BigInt integer birthdate and start_timeline_position [0, 10489902]
4. Cloudflare CDN gallery avatars with live HTTP 200 validation
5. Balanced 25-point 6-stat RPG blocks (sum = 31, level <= 99 cap, dual-key parity)
6. JED+ formatting compliance (PList single line, 4-block prose, 0 em-dashes, format discipline)
7. Anti-loop hygiene (0 broad umbrella keys, whole_words_only: true)
8. Canon lore invariants (Sierra lamia locomotion, Scarlett succubus anatomy)
"""

import sys
import os
import json
import re
import unittest
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# Import token refresher
sys.path.append(str(REPO_ROOT / 'scratch'))
try:
    import refresh_token
except ImportError:
    refresh_token = None

TARGET_WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
API_BASE = 'https://app.wyvern.chat/api/worlds'
CURRENT_WORLD_AGE = 10489902  # August 26, 2024, 06:00 UTC

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "losangeles", "underworld",
    "vampire", "werewolf", "human", "demihuman", "demon",
    "college", "student", "alpha", "beta", "omega", "pack"
}

CANONICAL_SPECS = {
    'Erik Ulfr Douglas': {
        'level': 55,
        'birthdate': 10009344,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public',
        'stats': {'might': 7, 'resilience': 7, 'agility': 4, 'wit': 5, 'presence': 7, 'scouting': 1},
        'min_len': 20000
    },
    'Logan Járn Douglas': {
        'level': 49,
        'birthdate': 10054920,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public',
        'stats': {'might': 7, 'resilience': 6, 'agility': 6, 'wit': 4, 'presence': 5, 'scouting': 3},
        'min_len': 12000
    },
    'Edric Douglas': {
        'level': 13,
        'birthdate': 10371552,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public',
        'stats': {'might': 3, 'resilience': 3, 'agility': 7, 'wit': 5, 'presence': 5, 'scouting': 8},
        'min_len': 6000
    },
    'Noah Loki Douglas Bloodmoon': {
        'level': 25,
        'birthdate': 10262928,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public',
        'stats': {'might': 6, 'resilience': 6, 'agility': 5, 'wit': 6, 'presence': 6, 'scouting': 2},
        'min_len': 8000
    },
    'Malachia Björn Douglas Bloodmoon': {
        'level': 28,
        'birthdate': 10244064,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public',
        'stats': {'might': 8, 'resilience': 7, 'agility': 5, 'wit': 4, 'presence': 5, 'scouting': 2},
        'min_len': 17000
    },
    'Jasper Svartr Douglas Bloodmoon': {
        'level': 19,
        'birthdate': 10320312,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public',
        'stats': {'might': 4, 'resilience': 3, 'agility': 8, 'wit': 9, 'presence': 3, 'scouting': 4},
        'min_len': 13000
    },
    'Alyssa Hvit Douglas Bloodmoon': {
        'level': 19,
        'birthdate': 10320312,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public',
        'stats': {'might': 2, 'resilience': 4, 'agility': 4, 'wit': 7, 'presence': 8, 'scouting': 6},
        'min_len': 15000
    },
    'Wulfnic Báleygr Bloodmoon': {
        'level': 99,
        'birthdate': 0,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public',
        'stats': {'might': 8, 'resilience': 8, 'agility': 5, 'wit': 3, 'presence': 5, 'scouting': 2},
        'min_len': 13000
    },
    'Zefir Hvitskog': {
        'level': 99,
        'birthdate': 176424,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bdd8961e-a68a-4c6b-b4e1-29a26db37e00/public',
        'stats': {'might': 5, 'resilience': 4, 'agility': 9, 'wit': 6, 'presence': 3, 'scouting': 4},
        'min_len': 13000
    },
    'Mackenzie Sanchez-Rogers': {
        'level': 19,
        'birthdate': 10316496,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public',
        'stats': {'might': 8, 'resilience': 7, 'agility': 7, 'wit': 3, 'presence': 3, 'scouting': 3},
        'min_len': 8000
    },
    'Finnegan Novak': {
        'level': 19,
        'birthdate': 10317984,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/75456c02-dddc-4879-7822-ab7c4628f600/public',
        'stats': {'might': 6, 'resilience': 6, 'agility': 8, 'wit': 3, 'presence': 4, 'scouting': 4},
        'min_len': 11000
    },
    'Sierra Cruz': {
        'level': 18,
        'birthdate': 10323648,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public',
        'stats': {'might': 7, 'resilience': 6, 'agility': 3, 'wit': 8, 'presence': 3, 'scouting': 4},
        'min_len': 5000
    },
    'Scarlett Rose': {
        'level': 20,
        'birthdate': 10307808,
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e96d176a-47e4-4829-2af4-7cd6ae239100/public',
        'stats': {'might': 2, 'resilience': 3, 'agility': 6, 'wit': 6, 'presence': 9, 'scouting': 5},
        'min_len': 4500
    }
}


def get_token():
    token_file = REPO_ROOT / 'scratch' / 'wyvern_token.txt'
    if token_file.exists():
        t = token_file.read_text(encoding='utf-8').strip()
        if t:
            return t
    if refresh_token:
        return refresh_token.refresh()
    raise RuntimeError("Cannot retrieve auth token.")


def query_live_world_characters():
    token = get_token()
    url = f"{API_BASE}/characters/world/{TARGET_WORLD_ID}"
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'EmpiricalChallenger/1.0'
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except urllib.error.HTTPError as e:
        if e.code == 401 and refresh_token:
            print("[Challenger] Token expired (401). Refreshing token and retrying...")
            new_token = refresh_token.refresh()
            headers['Authorization'] = f'Bearer {new_token}'
            req2 = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req2, timeout=15) as resp2:
                return json.loads(resp2.read().decode('utf-8'))
        raise


class EmpiricalChallengerMilestone1Test(unittest.TestCase):
    """Adversarial challenger test suite executed directly against live Wyvern API."""

    @classmethod
    def setUpClass(cls):
        print(f"\n[Empirical Challenger] Querying live Wyvern API for World {TARGET_WORLD_ID}...")
        cls.characters = query_live_world_characters()
        assert isinstance(cls.characters, list), "API response must be a JSON array"
        print(f"[Empirical Challenger] Received {len(cls.characters)} characters from live cloud.")
        cls.by_name = {c.get('display_name'): c for c in cls.characters}

    def test_01_exact_character_count_and_uniqueness(self):
        """Assert exactly 13 characters, no more, no less, and strictly unique IDs."""
        self.assertEqual(len(self.characters), 13, f"Expected exactly 13 characters, found {len(self.characters)}")
        self.assertEqual(len(self.by_name), 13, f"Duplicate character display_names detected: {list(self.by_name.keys())}")
        
        ids = [c.get('_id') or c.get('id') for c in self.characters]
        self.assertEqual(len(ids), 13, "Every character must have an ID")
        self.assertEqual(len(set(ids)), 13, f"Duplicate character IDs detected: {ids}")

    def test_02_canonical_identity_coverage(self):
        """Assert 100% of the 13 canonical characters are present in the world."""
        for expected_name in CANONICAL_SPECS:
            self.assertIn(expected_name, self.by_name, f"Missing canonical character: {expected_name}")

    def test_03_world_id_association(self):
        """Assert every character record is explicitly bound to TARGET_WORLD_ID."""
        for c in self.characters:
            name = c.get('display_name')
            world_field = c.get('world')
            if isinstance(world_field, dict):
                wid = world_field.get('_id') or world_field.get('id')
            else:
                wid = c.get('world_id') or world_field
            self.assertEqual(wid, TARGET_WORLD_ID, f"Character {name} has incorrect world reference {wid}")

    def test_04_timeline_bigint_integrity(self):
        """Assert birthdate and start_timeline_position are exact non-negative BigInt integers."""
        for name, spec in CANONICAL_SPECS.items():
            c = self.by_name[name]
            bdate = c.get('birthdate')
            tl_pos = c.get('start_timeline_position')
            
            # Type assertion: strictly int, not bool, not float, not str
            self.assertIsInstance(bdate, int, f"birthdate for {name} must be an integer, got {type(bdate)}")
            self.assertNotIsInstance(bdate, bool, f"birthdate for {name} must not be a boolean")
            self.assertIsInstance(tl_pos, int, f"start_timeline_position for {name} must be an integer, got {type(tl_pos)}")
            self.assertNotIsInstance(tl_pos, bool, f"start_timeline_position for {name} must not be a boolean")
            
            # Equality assertion between birthdate and start position
            self.assertEqual(bdate, tl_pos, f"birthdate != start_timeline_position for {name} ({bdate} vs {tl_pos})")
            
            # Range assertion: 0 <= bdate <= CURRENT_WORLD_AGE
            self.assertGreaterEqual(bdate, 0, f"birthdate for {name} cannot be negative: {bdate}")
            self.assertLessEqual(bdate, CURRENT_WORLD_AGE, f"birthdate for {name} exceeds current world age: {bdate} > {CURRENT_WORLD_AGE}")
            
            # Certified value assertion
            self.assertEqual(bdate, spec['birthdate'], f"birthdate mismatch for {name}: expected {spec['birthdate']}, got {bdate}")

    def test_05_avatar_cloudflare_cdn_format(self):
        """Assert avatars use the canonical Cloudflare CDN format and certified asset keys."""
        for name, spec in CANONICAL_SPECS.items():
            c = self.by_name[name]
            avatar = c.get('avatar')
            self.assertIsInstance(avatar, str, f"avatar for {name} must be a string")
            self.assertTrue(avatar.startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'),
                            f"avatar for {name} must use official Cloudflare CDN domain: {avatar}")
            self.assertTrue(avatar.endswith('/public'), f"avatar for {name} must end with /public: {avatar}")
            self.assertEqual(avatar, spec['avatar'], f"avatar URL mismatch for {name}: expected {spec['avatar']}, got {avatar}")

    def test_06_avatar_cdn_liveness_http(self):
        """Adversarially probe Cloudflare CDN for every avatar to ensure images are live (HTTP 200)."""
        tested_urls = set()
        for name, spec in CANONICAL_SPECS.items():
            url = spec['avatar']
            if url in tested_urls:
                continue
            tested_urls.add(url)
            
            req = urllib.request.Request(url, headers={'User-Agent': 'EmpiricalChallenger/1.0'}, method='HEAD')
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    self.assertEqual(resp.status, 200, f"CDN returned non-200 for {name} avatar: {resp.status}")
                    content_type = resp.headers.get('Content-Type', '')
                    self.assertTrue(content_type.startswith('image/'), f"CDN content-type is not image for {name}: {content_type}")
            except urllib.error.HTTPError as e:
                self.fail(f"HTTPError {e.code} probing avatar for {name}: {url}")

    def test_07_rpg_stats_structure_and_level_cap(self):
        """Assert rpg_stats enabled, level capped at 99, and level matches canonical age."""
        for name, spec in CANONICAL_SPECS.items():
            c = self.by_name[name]
            rpg = c.get('rpg_stats')
            self.assertIsInstance(rpg, dict, f"rpg_stats missing or not a dict for {name}")
            self.assertTrue(rpg.get('enabled'), f"rpg_stats.enabled must be True for {name}")
            
            level = rpg.get('level')
            self.assertIsInstance(level, int, f"level must be an integer for {name}")
            self.assertGreaterEqual(level, 1, f"level must be >= 1 for {name}")
            self.assertLessEqual(level, 99, f"CRITICAL: level exceeds 99 cap for {name}: {level}")
            self.assertEqual(level, spec['level'], f"Level mismatch for {name}: expected {spec['level']}, got {level}")

    def test_08_rpg_stats_balance_25pt_sum31(self):
        """Assert balanced 25-point 6-stat RPG blocks (base 1 per stat, sum must be exactly 31)."""
        named_keys = ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']
        indexed_keys = ['stat_1', 'stat_2', 'stat_3', 'stat_4', 'stat_5', 'stat_6']
        
        for name, spec in CANONICAL_SPECS.items():
            c = self.by_name[name]
            rpg = c.get('rpg_stats', {})
            base_stats = rpg.get('base_stats')
            self.assertIsInstance(base_stats, dict, f"base_stats missing or not a dict for {name}")
            
            # Check all 6 stats exist in both naming conventions
            for k in named_keys:
                self.assertIn(k, base_stats, f"Missing named stat {k} in base_stats for {name}")
                v = base_stats[k]
                self.assertIsInstance(v, int, f"Stat {k} must be int for {name}")
                self.assertGreaterEqual(v, 1, f"Stat {k} must be at least base 1 for {name}, found {v}")
                
            for k in indexed_keys:
                self.assertIn(k, base_stats, f"Missing indexed stat {k} in base_stats for {name}")
                v = base_stats[k]
                self.assertIsInstance(v, int, f"Stat {k} must be int for {name}")
                self.assertGreaterEqual(v, 1, f"Stat {k} must be at least base 1 for {name}, found {v}")
                
            # Dual-key equality check
            for idx, n_key in enumerate(named_keys, 1):
                i_key = f"stat_{idx}"
                self.assertEqual(base_stats[n_key], base_stats[i_key],
                                 f"Dual-key mismatch for {name}: {n_key}={base_stats[n_key]} vs {i_key}={base_stats[i_key]}")
                
            # Stat sum check
            named_sum = sum(base_stats[k] for k in named_keys)
            indexed_sum = sum(base_stats[k] for k in indexed_keys)
            self.assertEqual(named_sum, 31, f"Named stats sum is {named_sum} != 31 (base 6 + 25 budget) for {name}")
            self.assertEqual(indexed_sum, 31, f"Indexed stats sum is {indexed_sum} != 31 (base 6 + 25 budget) for {name}")
            
            # Certified values check
            for k, expected_v in spec['stats'].items():
                self.assertEqual(base_stats[k], expected_v, f"Stat {k} mismatch for {name}: expected {expected_v}, got {base_stats[k]}")

    def test_09_jed_plus_formatting_rules(self):
        """Assert JED+ format compliance across summary and long_summary."""
        for name, spec in CANONICAL_SPECS.items():
            c = self.by_name[name]
            summary = c.get('summary') or ''
            long_summary = c.get('long_summary') or ''
            
            # Summary checks
            self.assertTrue(summary.startswith('['), f"summary for {name} must start with '['")
            self.assertTrue(summary.endswith(']'), f"summary for {name} must end with ']'")
            self.assertIn('NAME:', summary, f"summary for {name} missing 'NAME:'")
            self.assertIn('SPECIES:', summary, f"summary for {name} missing 'SPECIES:'")
            self.assertIn('AGE:', summary, f"summary for {name} missing 'AGE:'")
            
            # Long summary checks
            self.assertGreaterEqual(len(long_summary), spec['min_len'],
                                    f"long_summary for {name} is suspiciously short: {len(long_summary)} < {spec['min_len']}")
            
            # JED+ single-line bracket header
            first_line = long_summary.splitlines()[0].strip()
            self.assertTrue(first_line.startswith('[NAME:'), f"long_summary for {name} must start with '[NAME:' on line 1")
            self.assertTrue(first_line.endswith(']'), f"Bracket header on line 1 for {name} must close with ']' on the same line")
            
            # Prose sections
            self.assertIn('BACKSTORY:', long_summary, f"Missing 'BACKSTORY:' in long_summary for {name}")
            has_pack = ('FAMILY & PACK:' in long_summary or
                        'CLAN AND COMPANY:' in long_summary or
                        'FAMILY AND PACK:' in long_summary)
            self.assertTrue(has_pack, f"Missing 'FAMILY & PACK:' or company equivalent for {name}")
            
            has_voice = ('VOICE & BEHAVIOR:' in long_summary or
                         'VOICE AND BEHAVIOR:' in long_summary)
            self.assertTrue(has_voice, f"Missing 'VOICE & BEHAVIOR:' for {name}")

    def test_10_formatting_discipline_and_em_dash_ban(self):
        """Assert ZERO em-dashes (\\u2014) across all fields and presence of format discipline instruction."""
        for name in CANONICAL_SPECS:
            c = self.by_name[name]
            fields_to_check = {
                'display_name': c.get('display_name', ''),
                'summary': c.get('summary', ''),
                'display_description': c.get('display_description', ''),
                'long_summary': c.get('long_summary', ''),
                'final_instructions': c.get('final_instructions', '')
            }
            
            for field_name, content in fields_to_check.items():
                em_count = content.count('\u2014')
                self.assertEqual(em_count, 0, f"VIOLATION: Found {em_count} forbidden em-dashes (\\u2014) in {field_name} for {name}")
                
            # Verify final_instructions content
            fin = c.get('final_instructions', '')
            self.assertIn("Format discipline:", fin, f"final_instructions missing format discipline for {name}")
            self.assertIn("dialogue in quotes", fin, f"final_instructions missing dialogue discipline for {name}")
            self.assertIn("Never use the em dash", fin, f"final_instructions missing em-dash directive for {name}")

    def test_11_anti_loop_and_umbrella_keys_hygiene(self):
        """Assert keys have zero broad umbrella keywords and whole_words_only is True."""
        for name in CANONICAL_SPECS:
            c = self.by_name[name]
            keys = c.get('keys', [])
            self.assertIsInstance(keys, list, f"keys must be a list for {name}")
            self.assertGreater(len(keys), 0, f"keys list must not be empty for {name}")
            
            for k in keys:
                lower_k = k.lower().strip()
                self.assertNotIn(lower_k, BROAD_KEYS, f"VIOLATION: Broad umbrella keyword '{lower_k}' found in keys for {name}")
                
            self.assertTrue(c.get('whole_words_only'), f"whole_words_only must be True for {name}")

    def test_12_canon_lore_edge_cases(self):
        """Assert domain-specific canon lore invariants."""
        # Sierra Cruz (Lamia): Must have explicit anatomy rule prohibiting walking and mandating coils/slithering
        sierra = self.by_name['Sierra Cruz']
        sierra_text = sierra.get('long_summary', '').lower()
        
        self.assertIn("locomotion & anatomy rule", sierra_text, "Sierra Cruz missing explicit LOCOMOTION & ANATOMY RULE")
        self.assertIn("she never walks", sierra_text, "Sierra Cruz missing 'She NEVER walks' mandate")
        self.assertIn("zero human legs", sierra_text, "Sierra Cruz missing 'zero human legs' specification")
        self.assertTrue(any(t in sierra_text for t in ['slithers', 'coils', 'glides']),
                        "Sierra Cruz missing serpentine movement terms (slithers, coils, glides)")
        
        # Ensure Sierra herself is not depicted positively walking or having feet
        forbidden_positive_locomotion = [
            r'sierra\s+walks', r'sierra\s+walked', r'sierra\s+is\s+walking',
            r'on\s+her\s+feet', r'on\s+her\s+legs', r'wearing\s+shoes', r'wearing\s+pants'
        ]
        for pattern in forbidden_positive_locomotion:
            matches = re.findall(pattern, sierra_text)
            self.assertEqual(len(matches), 0,
                             f"VIOLATION: Sierra Cruz contains positive human locomotion pattern '{pattern}': {matches}")

        # Scarlett Rose (Succubus): Candy-pink hair and scarlet horns
        scarlett = self.by_name['Scarlett Rose']
        scarlett_text = scarlett.get('long_summary', '').lower() + scarlett.get('summary', '').lower()
        self.assertTrue('pink' in scarlett_text or 'candy-pink' in scarlett_text,
                        "Scarlett Rose missing candy-pink hair reference in canon text")
        self.assertTrue('horn' in scarlett_text, "Scarlett Rose missing horn reference in canon text")

    def test_13_macro_residual_hygiene(self):
        """Assert zero unexpanded template macros (e.g. {{age}}, {{scenarioChar}}) in all character descriptions."""
        macro_pattern = re.compile(r'\{\{[^}]+\}\}')
        for name in CANONICAL_SPECS:
            c = self.by_name[name]
            long_summary = c.get('long_summary', '')
            matches = macro_pattern.findall(long_summary)
            self.assertEqual(len(matches), 0, f"VIOLATION: Unexpanded template macros found in {name}: {matches}")

    def test_14_lorebook_canonical_parity(self):
        """Assert live character descriptions match authoritative lorebook entries byte-for-byte."""
        from scripts.deploy_13_world_characters import CHARACTER_SPECS, load_canonical_content
        for spec in CHARACTER_SPECS:
            name = spec['display_name']
            source_file, entry_id = spec['lorebook_source']
            canonical_content = load_canonical_content(source_file, entry_id)
            live_content = self.by_name[name].get('long_summary', '')
            self.assertEqual(live_content, canonical_content,
                             f"Parity mismatch for {name}: live text diverges from {source_file}:{entry_id}")

    def test_15_erik_preexisting_id_retention(self):
        """Assert Erik Ulfr Douglas retained his preexisting MongoDB ID _qfaywY2yfrGWcxPBdmURD."""
        erik = self.by_name['Erik Ulfr Douglas']
        erik_id = erik.get('_id') or erik.get('id')
        self.assertEqual(erik_id, '_qfaywY2yfrGWcxPBdmURD',
                         f"Erik ID was not preserved: expected _qfaywY2yfrGWcxPBdmURD, got {erik_id}")

    def test_16_rpg_stats_non_zero_remediation(self):
        """Assert Erik's prior defect (stat_6: 0) is resolved and every stat across all characters is >= 1."""
        erik = self.by_name['Erik Ulfr Douglas']
        bs = erik.get('rpg_stats', {}).get('base_stats', {})
        self.assertEqual(bs.get('stat_6'), 1, f"Erik stat_6 should be remediated to 1, got {bs.get('stat_6')}")
        self.assertEqual(bs.get('scouting'), 1, f"Erik scouting should be remediated to 1, got {bs.get('scouting')}")
        
        for name in CANONICAL_SPECS:
            char_bs = self.by_name[name].get('rpg_stats', {}).get('base_stats', {})
            for k, v in char_bs.items():
                self.assertGreaterEqual(v, 1, f"Character {name} has stat {k} below base 1: {v}")


if __name__ == '__main__':
    unittest.main()
