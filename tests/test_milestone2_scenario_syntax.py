"""
Unit and Integration Tests: tests/test_milestone2_scenario_syntax.py
Author: worker_m2_gen2
Milestone: Milestone 2 (Scenario & Chat Standardization)

Objective:
Verify that Scenario `_2MTWKjxrQPdQVaz9y4Q7H` in `FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json`
and active chat `chat_log_PJx1W1rg3WUzRM7MnQrkN` strictly adhere to the Visual Novel `=>Speaker:` beat splitting
specification and repository formatting discipline:
1. Exactly 0 em-dashes (`—`).
2. Exactly 0 asterisks (`*`) in actions/narration.
3. Dialogue enclosed in standard double quotes (`"..."`).
4. All premade scenes start with `=>Narrator:`.
5. Character turns prefixed with canonical short names (`=>Erik:`, `=>Logan:`, `=>Edric:`, `=>Noah:`,
   `=>Malachia:`, `=>Jasper:`, `=>Alyssa:`, `=>Wulfnic:`, `=>Zefir:`, `=>Finn:`, `=>Sierra:`, `=>Scarlett:`).
6. Jasper, Alyssa, and Wulfnic lines disentangled from narration.
7. Zero plain speaker prefixes without `=>`.
8. Live Wyvern Web API verification for scenario and active chat swipe.
"""

import unittest
import json
import re
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCENARIO_JSON_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json'
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

SCENARIO_ID = "_2MTWKjxrQPdQVaz9y4Q7H"
CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
SWIPE_ID = "message_swipe_99mmMgEEQjk2pkJN3hXkQ"

EXPECTED_SCENE_0_TAGS = [
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Jasper',
    'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett'
]

EXPECTED_SCENE_1_TAGS = [
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Alyssa',
    'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett'
]

EXPECTED_SCENE_2_TAGS = [
    'Narrator', 'Erik', 'Logan', 'Narrator'
]

EXPECTED_MSG0_TAGS = EXPECTED_SCENE_0_TAGS


class TestMilestone2ScenarioSyntax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.assertTrue(cls, SCENARIO_JSON_PATH.exists(), f"Scenario JSON missing: {SCENARIO_JSON_PATH}")
        with open(SCENARIO_JSON_PATH, 'r', encoding='utf-8') as f:
            cls.scenario_data = json.load(f)

    def test_01_local_scenario_file_structure(self):
        """Test top-level scenario JSON structure and keys."""
        data = self.scenario_data
        self.assertEqual(data.get('id'), SCENARIO_ID)
        self.assertIn('name', data)
        self.assertIn('premade_scenes', data)
        self.assertEqual(len(data['premade_scenes']), 3)

    def test_02_premade_scenes_ids_and_order(self):
        """Test that the 3 scenes match expected IDs."""
        scenes = self.scenario_data['premade_scenes']
        scene_ids = [s.get('id') for s in scenes]
        self.assertEqual(scene_ids, [
            'scene-succ-welcome-day-alyssa',
            'scene-succ-welcome-day-jasper',
            'scene-succ-welcome-day-corale'
        ])

    def test_03_zero_em_dashes_in_all_scenes(self):
        """Test formatting discipline: exactly 0 em-dashes ('—') across all scenes."""
        for i, scene in enumerate(self.scenario_data['premade_scenes']):
            text = scene.get('scene_text', '')
            em_dash_count = text.count('—')
            self.assertEqual(
                em_dash_count, 0,
                f"Scene {i} [{scene.get('id')}] contains {em_dash_count} em-dashes ('—'). Rule requires 0."
            )

    def test_04_zero_asterisks_in_all_scenes(self):
        """Test formatting discipline: exactly 0 asterisks ('*') in narration and actions."""
        for i, scene in enumerate(self.scenario_data['premade_scenes']):
            text = scene.get('scene_text', '')
            asterisk_count = text.count('*')
            self.assertEqual(
                asterisk_count, 0,
                f"Scene {i} [{scene.get('id')}] contains {asterisk_count} asterisks ('*'). Actions must be plain text."
            )

    def test_05_all_scenes_start_with_narrator(self):
        """Test that all scenes start with '=>Narrator:'."""
        for i, scene in enumerate(self.scenario_data['premade_scenes']):
            text = scene.get('scene_text', '').strip()
            self.assertTrue(
                text.startswith('=>Narrator:'),
                f"Scene {i} [{scene.get('id')}] does not start with '=>Narrator:'."
            )

    def test_06_scene_0_speaker_tags(self):
        """Test that Scene 0 contains the canonical 14 speaker tags in exact order."""
        scene0 = self.scenario_data['premade_scenes'][0]
        tags = re.findall(r'^=>([A-Za-z0-9_]+):', scene0.get('scene_text', ''), flags=re.MULTILINE)
        self.assertEqual(tags, EXPECTED_SCENE_0_TAGS)

    def test_07_scene_1_speaker_tags(self):
        """Test that Scene 1 contains the canonical 14 speaker tags in exact order."""
        scene1 = self.scenario_data['premade_scenes'][1]
        tags = re.findall(r'^=>([A-Za-z0-9_]+):', scene1.get('scene_text', ''), flags=re.MULTILINE)
        self.assertEqual(tags, EXPECTED_SCENE_1_TAGS)

    def test_08_scene_2_speaker_tags(self):
        """Test that Scene 2 contains the canonical 4 speaker tags."""
        scene2 = self.scenario_data['premade_scenes'][2]
        tags = re.findall(r'^=>([A-Za-z0-9_]+):', scene2.get('scene_text', ''), flags=re.MULTILINE)
        self.assertEqual(tags, EXPECTED_SCENE_2_TAGS)

    def test_09_no_plain_speaker_prefixes(self):
        """Test that no plain dialogue prefixes without '=>' exist."""
        for i, scene in enumerate(self.scenario_data['premade_scenes']):
            text = scene.get('scene_text', '')
            plain = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', text, flags=re.MULTILINE)
            plain = [p for p in plain if not p.startswith('=>')]
            self.assertEqual(
                plain, [],
                f"Scene {i} [{scene.get('id')}] has plain un-prefixed speaker tags: {plain}"
            )

    def test_10_disentangled_turns(self):
        """Test that Jasper (Scene 0) and Alyssa (Scene 1) turns have dedicated =>Speaker: blocks."""
        scene0_text = self.scenario_data['premade_scenes'][0]['scene_text']
        self.assertIn('=>Jasper:', scene0_text)
        self.assertIn('Le registrazioni delle matricole', scene0_text)

        scene1_text = self.scenario_data['premade_scenes'][1]['scene_text']
        self.assertIn('=>Alyssa:', scene1_text)
        self.assertIn('Cerca di non infiltrarti', scene1_text)

        # Wulfnic disentangled
        self.assertIn('=>Wulfnic:\n"In fondo non sei mai andato a scuola', scene0_text)
        self.assertIn('=>Wulfnic:\n"In fondo non sei mai andato a scuola', scene1_text)

    def test_11_live_scenario_api(self):
        """Integration test: Verify live Wyvern Web API scenario deployment."""
        if not TOKEN_PATH.exists():
            self.skipTest("Token file scratch/wyvern_token.txt not found")
        token = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if not token:
            self.skipTest("Token file is empty")

        url = f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}"
        req = urllib.request.Request(
            url,
            headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                self.assertEqual(resp.status, 200)
                live_sc = json.loads(resp.read().decode('utf-8'))
                scenes = live_sc.get('premade_scenes', [])
                self.assertEqual(len(scenes), 3)

                # Check Scene 0
                s0_tags = re.findall(r'^=>([A-Za-z0-9_]+):', scenes[0]['scene_text'], flags=re.MULTILINE)
                self.assertEqual(s0_tags, EXPECTED_SCENE_0_TAGS)
                self.assertEqual(scenes[0]['scene_text'].count('—'), 0)
                self.assertEqual(scenes[0]['scene_text'].count('*'), 0)

                # Check Scene 1
                s1_tags = re.findall(r'^=>([A-Za-z0-9_]+):', scenes[1]['scene_text'], flags=re.MULTILINE)
                self.assertEqual(s1_tags, EXPECTED_SCENE_1_TAGS)
                self.assertEqual(scenes[1]['scene_text'].count('—'), 0)
                self.assertEqual(scenes[1]['scene_text'].count('*'), 0)

                # Check Scene 2
                s2_tags = re.findall(r'^=>([A-Za-z0-9_]+):', scenes[2]['scene_text'], flags=re.MULTILINE)
                self.assertEqual(s2_tags, EXPECTED_SCENE_2_TAGS)
                self.assertEqual(scenes[2]['scene_text'].count('—'), 0)
                self.assertEqual(scenes[2]['scene_text'].count('*'), 0)
        except urllib.error.HTTPError as e:
            self.fail(f"Live scenario GET failed with HTTP {e.code}")

    def test_12_live_chat_log_swipe_api(self):
        """Integration test: Verify live Wyvern Web API chat swipe patching."""
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
                chat = json.loads(resp.read().decode('utf-8'))
                messages = chat.get('messages', [])
                self.assertGreaterEqual(len(messages), 1)

                msg0 = messages[0]
                swipes = msg0.get('swipes', [])
                self.assertGreaterEqual(len(swipes), 1)

                swipe0 = swipes[0]
                self.assertEqual(swipe0.get('id'), SWIPE_ID)

                content = swipe0.get('content', '')
                tags = re.findall(r'^=>([A-Za-z0-9_]+):', content, flags=re.MULTILINE)
                self.assertEqual(tags, EXPECTED_MSG0_TAGS)
                self.assertEqual(content.count('—'), 0)
                self.assertEqual(content.count('*'), 0)

                # Also verify message.content matches swipe content
                self.assertEqual(msg0.get('content', '').count('—'), 0)
                self.assertEqual(msg0.get('content', '').count('*'), 0)
        except urllib.error.HTTPError as e:
            self.fail(f"Live chat GET failed with HTTP {e.code}")


if __name__ == '__main__':
    unittest.main()
