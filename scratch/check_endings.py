import json
from pathlib import Path

ROOT = Path('e:/repository/SvartulfrVerse')
with open(ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json', 'r', encoding='utf-8') as f:
    sc = json.load(f)

for idx, s in enumerate(sc['premade_scenes']):
    text = s['scene_text']
    print(f"Scene {idx} end snippet: {repr(text[-50:])}")

import urllib.request
token = open(ROOT / 'scratch' / 'wyvern_token.txt', encoding='utf-8').read().strip()
req = urllib.request.Request('https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
chat = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
m0 = chat['messages'][0]['swipes'][0]['content']
print(f"Message 0 swipe end snippet: {repr(m0[-50:])}")
