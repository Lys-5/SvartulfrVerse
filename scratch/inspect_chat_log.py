import json
import urllib.request
from pathlib import Path

ROOT = Path('e:/repository/SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = TOKEN_PATH.read_text(encoding='utf-8').strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
url = "https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN"

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    chat = json.loads(resp.read().decode('utf-8'))

print("Chat ID:", chat.get('id') or chat.get('_id'))
print("Scenario ID:", chat.get('scenario_id') or chat.get('character_scenario_id') or chat.get('scenario'))
print("Character / World:", chat.get('character_id'), chat.get('world_id'))
print("Messages count:", len(chat.get('messages', [])))

for i, msg in enumerate(chat.get('messages', [])):
    print(f"\nMessage {i}:")
    print(f"  id: {msg.get('id')}")
    print(f"  role: {msg.get('role')}")
    print(f"  speaker: {msg.get('speaker')}")
    print(f"  speaker_slot: {msg.get('speaker_slot')}")
    print(f"  content length: {len(msg.get('content', ''))}")
    swipes = msg.get('swipes', [])
    print(f"  swipes count: {len(swipes)}")
    for j, sw in enumerate(swipes):
        print(f"    Swipe {j} id: {sw.get('id')}, len: {len(sw.get('content', ''))}")
