"""
Unit and Integration Tests: tests/test_milestone3_display_settings.py
Author: worker_m3
Milestone: Milestone 3 (Display Settings & Right Sidebar Flags)

Objective:
Verify that:
1. Visual Novel Mode Display Settings are configured according to schema $ in chunk 14685:
   - vnMode: true, vnTextSpeed: "normal", vnDirections: true, vnAutoAdvance: false,
     vnAutoDelayMs: 2500, vnSkipRead: false, vnTextboxOpacity: 0.85, vnSpriteLimit: 3,
     vnItalicAsThought: false.
2. Right sidebar flags are enforced:
   - scene/party auto-apply ON: party_tied: true on chat log, scene_summaries auto flags enabled.
   - AI content creation OFF: memory.memory_scan.auto_approve: false, enable_ai_tool_creation: false.
   - World-level VN mode and simulation features are enabled: vn_mode: true, rpg_stats: true, combat: true.
3. Stats tab renders full character sheets:
   - All 13 Primary World Characters in World _YpX47fNraQFw2dD7TdycJ have rpg_stats.enabled: true
     with balanced 25-point 6-stat blocks (sum = 31, level <= 99) and canonical CDN avatars,
     preventing the "No RPG-enabled characters" placeholder.
4. Live Wyvern Web API verification for chat log, world, and world characters.
"""

import unittest
import json
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
SNAPSHOT_PATH = ROOT / 'scratch' / 'm3_display_settings_and_flags_verified.json'

CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
WORLD_ID = "_YpX47fNraQFw2dD7TdycJ"

EXPECTED_VN_VALUES = {
    "vnMode": True,
    "vnTextSpeed": "normal",
    "vnDirections": True,
    "vnAutoAdvance": False,
    "vnAutoDelayMs": 2500,
    "vnSkipRead": False,
    "vnTextboxOpacity": 0.85,
    "vnSpriteLimit": 3,
    "vnItalicAsThought": False
}

EXPECTED_13_CHARACTERS = [
    "Erik Ulfr Douglas",
    "Logan Járn Douglas",
    "Edric Douglas",
    "Noah Loki Douglas Bloodmoon",
    "Malachia Björn Douglas Bloodmoon",
    "Jasper Svartr Douglas Bloodmoon",
    "Alyssa Hvit Douglas Bloodmoon",
    "Wulfnic Báleygr Bloodmoon",
    "Zefir Hvitskog",
    "Mackenzie Sanchez-Rogers",
    "Finnegan Novak",
    "Sierra Cruz",
    "Scarlett Rose"
]


class TestMilestone3DisplaySettings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.assertTrue(cls, SNAPSHOT_PATH.exists(), f"Snapshot file missing: {SNAPSHOT_PATH}")
        with open(SNAPSHOT_PATH, 'r', encoding='utf-8') as f:
            cls.snapshot = json.load(f)

    def test_01_local_snapshot_structure(self):
        """Verifies local snapshot file structure and expected metadata."""
        snap = self.snapshot
        self.assertEqual(snap.get('chat_id'), CHAT_LOG_ID)
        self.assertEqual(snap.get('world_id'), WORLD_ID)
        self.assertIn('chat_overrides', snap)
        self.assertIn('characters', snap)
        self.assertEqual(snap.get('characters_count'), 13)

    def test_02_vn_display_settings_values(self):
        """Verifies Visual Novel Mode Display Settings match schema $ specification."""
        co = self.snapshot.get('chat_overrides', {})
        self.assertEqual(co.get('version'), 1)
        self.assertEqual(co.get('notes'), {})

        vals = co.get('values', {})
        for key, expected_val in EXPECTED_VN_VALUES.items():
            self.assertIn(key, vals, f"Key {key} missing from chat_overrides.values")
            self.assertEqual(vals[key], expected_val, f"Mismatch for {key}: expected {expected_val}, got {vals[key]}")

    def test_03_party_auto_apply_flag(self):
        """Verifies party_tied is True (scene/party auto-apply ON)."""
        self.assertIs(self.snapshot.get('party_tied'), True)

    def test_04_scene_auto_apply_flags(self):
        """Verifies scene summaries auto-apply flags are enabled."""
        ss = self.snapshot.get('scene_summaries', {})
        self.assertIs(ss.get('auto_enabled'), True)
        self.assertIs(ss.get('replace_enabled'), True)
        self.assertIs(ss.get('dynamic_enabled'), True)
        self.assertEqual(ss.get('tail_n'), 12)
        self.assertEqual(ss.get('budget_fraction'), 0.25)
        self.assertEqual(ss.get('auto_interval'), 50)
        self.assertEqual(ss.get('detail'), "verbose")

    def test_05_ai_content_creation_off(self):
        """Verifies AI content creation is disabled without manual review."""
        self.assertIs(self.snapshot.get('memory_scan_auto_approve'), False)
        self.assertIs(self.snapshot.get('enable_ai_tool_creation'), False)
        self.assertIs(self.snapshot.get('scene_summaries', {}).get('auto_approve'), False)

    def test_06_world_features_vn_mode_active(self):
        """Verifies world_features.vn_mode is True."""
        self.assertIs(self.snapshot.get('world_features_vn_mode'), True)

    def test_07_world_features_rpg_stats_active(self):
        """Verifies world_features.rpg_stats is True."""
        self.assertIs(self.snapshot.get('world_features_rpg_stats'), True)

    def test_08_stats_tab_characters_count(self):
        """Verifies exactly 13 characters are ready for the Stats tab."""
        chars = self.snapshot.get('characters', [])
        self.assertEqual(len(chars), 13)

    def test_09_all_13_characters_rpg_enabled(self):
        """Verifies all 13 characters have rpg_enabled: True."""
        chars = self.snapshot.get('characters', [])
        for c in chars:
            self.assertIs(c.get('rpg_enabled'), True, f"Character {c.get('name')} rpg_enabled is not True")
            self.assertEqual(c.get('verified_status'), "READY_FOR_STATS_TAB")

    def test_10_stats_tab_level_bounds(self):
        """Verifies levels are positive integers capped at 99."""
        chars = self.snapshot.get('characters', [])
        for c in chars:
            level = c.get('level')
            self.assertIsInstance(level, int)
            self.assertGreaterEqual(level, 1)
            self.assertLessEqual(level, 99, f"Character {c.get('name')} level {level} exceeds 99 cap")

    def test_11_stats_tab_balanced_stat_sums(self):
        """Verifies base stats sum to exactly 31 (25-point budget)."""
        chars = self.snapshot.get('characters', [])
        for c in chars:
            self.assertEqual(c.get('stat_sum'), 31, f"Character {c.get('name')} stat_sum is {c.get('stat_sum')} != 31")

    def test_12_stats_tab_dual_keys_structure(self):
        """Verifies each character base_stats dictionary has dual keys."""
        chars = self.snapshot.get('characters', [])
        for c in chars:
            bs = c.get('base_stats', {})
            for i in range(1, 7):
                self.assertIn(f'stat_{i}', bs, f"stat_{i} missing for {c.get('name')}")
            for key in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']:
                self.assertIn(key, bs, f"{key} missing for {c.get('name')}")

    def test_13_stats_tab_avatar_cdn(self):
        """Verifies Cloudflare CDN avatar URLs."""
        chars = self.snapshot.get('characters', [])
        for c in chars:
            avatar = c.get('avatar', '')
            self.assertTrue(
                avatar.startswith('https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/'),
                f"Invalid avatar URL for {c.get('name')}: {avatar}"
            )

    def test_14_live_chat_log_api(self):
        """Integration test: Verify live Wyvern Web API chat log parameters."""
        if not TOKEN_PATH.exists():
            self.skipTest("Token file scratch/wyvern_token.txt not found")
        token = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if not token:
            self.skipTest("Token file is empty")

        url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}"
        req = urllib.request.Request(
            url,
            headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                self.assertEqual(resp.status, 200)
                data = json.loads(resp.read().decode('utf-8'))

                self.assertIs(data.get('party_tied'), True)
                mem = data.get('memory', {})
                self.assertIs(mem.get('memory_scan', {}).get('auto_approve'), False)
                self.assertIs(mem.get('scene_summaries', {}).get('auto_enabled'), True)
                self.assertIs(mem.get('scene_summaries', {}).get('replace_enabled'), True)
                self.assertIs(mem.get('scene_summaries', {}).get('dynamic_enabled'), True)

                # Verify VN overrides embedded in memory
                co = mem.get('chat_overrides', {})
                self.assertEqual(co.get('version'), 1)
                self.assertEqual(co.get('values', {}).get('vnMode'), True)
                self.assertEqual(co.get('values', {}).get('vnDirections'), True)
                self.assertEqual(co.get('values', {}).get('vnTextSpeed'), "normal")
                self.assertEqual(co.get('values', {}).get('vnTextboxOpacity'), 0.85)
        except urllib.error.HTTPError as e:
            self.fail(f"Live chat GET failed with HTTP {e.code}")

    def test_15_live_world_api(self):
        """Integration test: Verify live Wyvern Web API world features."""
        if not TOKEN_PATH.exists():
            self.skipTest("Token file scratch/wyvern_token.txt not found")
        token = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if not token:
            self.skipTest("Token file is empty")

        url = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"
        req = urllib.request.Request(
            url,
            headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                self.assertEqual(resp.status, 200)
                world = json.loads(resp.read().decode('utf-8'))
                wf = world.get('world_features', {})
                self.assertIs(wf.get('vn_mode'), True)
                self.assertIs(wf.get('rpg_stats'), True)
                self.assertIs(wf.get('combat'), True)
                self.assertIs(wf.get('show_party_stats'), True)
                self.assertIs(world.get('enable_ai_tool_creation'), False)
        except urllib.error.HTTPError as e:
            self.fail(f"Live world GET failed with HTTP {e.code}")

    def test_16_live_world_characters_stats_api(self):
        """Integration test: Verify live Wyvern Web API world characters RPG blocks."""
        if not TOKEN_PATH.exists():
            self.skipTest("Token file scratch/wyvern_token.txt not found")
        token = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if not token:
            self.skipTest("Token file is empty")

        url = f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}"
        req = urllib.request.Request(
            url,
            headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                self.assertEqual(resp.status, 200)
                chars = json.loads(resp.read().decode('utf-8'))
                self.assertEqual(len(chars), 13)

                for c in chars:
                    rpg = c.get('rpg_stats')
                    self.assertIsNotNone(rpg, f"Character {c.get('display_name')} missing rpg_stats")
                    self.assertIs(rpg.get('enabled'), True)
                    self.assertGreaterEqual(rpg.get('level'), 1)
                    self.assertLessEqual(rpg.get('level'), 99)

                    bs = rpg.get('base_stats', {})
                    stat_sum = sum(bs[k] for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting'])
                    self.assertEqual(stat_sum, 31, f"Character {c.get('display_name')} sum is {stat_sum} != 31")
        except urllib.error.HTTPError as e:
            self.fail(f"Live world characters GET failed with HTTP {e.code}")


if __name__ == '__main__':
    unittest.main()
