import unittest
import json
import os
import sys

sys.path.append(os.getcwd())
from scripts.sync_from_wyvern_web import get_auth_token
import urllib.request

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
CHAT_ID = 'chat_log_EG2dpGaMQ4DaEd4g287pE'

class TestChatAuditSync(unittest.TestCase):
    def setUp(self):
        self.token = get_auth_token()
        self.headers = {'Authorization': f'Bearer {self.token}', 'User-Agent': 'Mozilla/5.0'}

    def test_mac_card_and_world_pacing_lock(self):
        # Check local card
        with open('FINAL/Mackenzie_Sanchez_Rogers_card.json', 'r', encoding='utf-8') as f:
            card = json.load(f)
        self.assertIn('HOOKUP FIRST, ZERO INSTANT LOVE', card['personality'])
        self.assertIn('BEHAVIOR & PACING DISCIPLINE', card['post_history_instructions'])
        self.assertNotIn('—', card['post_history_instructions'])
        
        # Check live World Character
        mac_id = '_RXHKfwRXwhRkBHttHVgqt'
        req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/characters/{mac_id}', headers=self.headers)
        with urllib.request.urlopen(req) as resp:
            w_mac = json.loads(resp.read().decode('utf-8'))
        self.assertIn('BEHAVIOR & PACING DISCIPLINE', w_mac.get('final_instructions', ''))
        self.assertIn('Keyboardist/Synth player', w_mac.get('final_instructions', ''))
        self.assertNotIn('—', w_mac.get('final_instructions', ''))

    def test_jared_world_himbo_lock(self):
        jared_id = '_6faaEP3MKNKWyV1JnJK8D'
        req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/characters/{jared_id}', headers=self.headers)
        with urllib.request.urlopen(req) as resp:
            w_jared = json.loads(resp.read().decode('utf-8'))
        self.assertIn('half-minotaur', w_jared.get('summary', '').lower())
        self.assertIn('BEHAVIOR & FLIRT DISCIPLINE', w_jared.get('final_instructions', ''))
        self.assertIn('ZERO instant fiancé behavior', w_jared.get('final_instructions', ''))

    def test_cocketeers_lexicon_and_jasper_roommates(self):
        req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}', headers=self.headers)
        with urllib.request.urlopen(req) as resp:
            lex = json.loads(resp.read().decode('utf-8'))
        
        cocketeers = [e for e in lex if e.get('name') == 'The Five Cocketeers']
        self.assertTrue(len(cocketeers) > 0)
        c = cocketeers[0]
        content = c.get('content', '')
        self.assertIn('Wyrm Dormitory', content)
        self.assertIn('Dean', content)
        self.assertIn('Russ', content)
        self.assertIn('Raymond', content)
        self.assertIn('Eric', content)
        self.assertIn('Javier', content)
        self.assertIn('Jasper Douglas', content)
        self.assertIn('Demihuman Tiger', content)
        self.assertIn('Demihuman Golden Retriever', content)

    def test_world_and_gm_pacing_gate(self):
        req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{WORLD_ID}', headers=self.headers)
        with urllib.request.urlopen(req) as resp:
            w = json.loads(resp.read().decode('utf-8'))
        self.assertIn('<relationship_pacing_gate>', w.get('base_instructions', ''))
        self.assertIn('<relationship_pacing_gate>', w.get('system_prompt_override', ''))
        
        with open('FINAL/assistants/Svartulfr_Game_Master_Assistant.json', 'r', encoding='utf-8') as f:
            gm = json.load(f)
        self.assertIn('<relationship_pacing_gate>', gm.get('system_prompt', ''))

if __name__ == '__main__':
    unittest.main()
