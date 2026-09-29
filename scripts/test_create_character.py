import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

token = get_auth_token()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

test_payload = {
    'world_id': WORLD_ID,
    'display_name': 'Radek',
    'first_name': 'Radek',
    'last_name': '',
    'nicknames': ['The Tactician'],
    'titles': ['Team Ukiyo Leader'],
    'tags': ['Male', 'Orc', 'Team Ukiyo', 'Hunter'],
    'is_global': True,
    'birthdate': 10219328,
    'start_timeline_position': 10219328,
    'display_description': "Massive orc combat tactician and squad leader of Team Ukiyo.",
    'summary': "[NAME: Radek; ROLE: Team Ukiyo Leader, Heavy Tactician; TRAITS: Authoritative, Disciplined]",
    'long_summary': "[NAME: Radek; SPECIES: Orc; AGE: {{age}}; HEIGHT: 208cm / 6'10\"]\n\nBACKSTORY: Born in the slums of Chicago post-Veilfall, Radek pulled Goran and Kian from the gutter to form Team Ukiyo.\n\nSQUAD AND BROTHERHOOD: Team Ukiyo is his family.\n\nVOICE AND BEHAVIOR: Speaks in measured, authoritative clipped sentences.",
    'final_instructions': 'Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.'
}

req = urllib.request.Request(f"{API_BASE}/characters", data=json.dumps(test_payload).encode('utf-8'), headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print('SUCCESS creating character! ID:', res.get('id'), res.get('_id'))
except urllib.error.HTTPError as e:
    print('HTTP ERROR:', e.code, e.read().decode('utf-8'))
