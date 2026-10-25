import sys
sys.path.insert(0, '.')
import urllib.request
import json
from scripts.configure_display_settings_and_flags import get_auth_token

token = get_auth_token()
req = urllib.request.Request(
    'https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN',
    headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(req) as resp:
    chat = json.loads(resp.read().decode('utf-8'))

print("=== PARTY TIED ===")
print("party_tied:", chat.get('party_tied'))

print("\n=== MEMORY SCAN ===")
print("memory.memory_scan:", json.dumps(chat.get('memory', {}).get('memory_scan'), indent=2))

print("\n=== SCENE SUMMARIES ===")
print("memory.scene_summaries:", json.dumps(chat.get('memory', {}).get('scene_summaries'), indent=2))

print("\n=== SUMMARIES (TOP LEVEL) ===")
print("summaries:", chat.get('summaries'))

print("\n=== WORLD PARTY ===")
print("world_party:", chat.get('world_party'))

print("\n=== PARTICIPANTS ===")
print("participants:", len(chat.get('participants', [])))
print("world_characters:", len(chat.get('world_characters', [])))
