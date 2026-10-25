import json
import urllib.request
from pathlib import Path

token = Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

# 1. Chat log check
req_chat = urllib.request.Request('https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN', headers=headers)
with urllib.request.urlopen(req_chat) as resp:
    print('CHAT_LOG STATUS:', resp.status)
    chat = json.loads(resp.read().decode('utf-8'))
    print('party_tied:', chat.get('party_tied'))
    mem = chat.get('memory', {})
    print('memory_scan:', mem.get('memory_scan'))
    print('scene_summaries:', mem.get('scene_summaries'))
    print('chat_overrides in memory:', mem.get('chat_overrides'))
    print('chat_overrides top-level:', chat.get('chat_overrides'))

# 2. World check
req_world = urllib.request.Request('https://app.wyvern.chat/api/worlds/_YpX47fNraQFw2dD7TdycJ', headers=headers)
with urllib.request.urlopen(req_world) as resp:
    print('\nWORLD STATUS:', resp.status)
    world = json.loads(resp.read().decode('utf-8'))
    print('world_features:', world.get('world_features'))
    print('enable_ai_tool_creation:', world.get('enable_ai_tool_creation'))

# 3. World characters check
req_chars = urllib.request.Request('https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ', headers=headers)
with urllib.request.urlopen(req_chars) as resp:
    print('\nWORLD CHARACTERS STATUS:', resp.status)
    chars = json.loads(resp.read().decode('utf-8'))
    print('Characters count:', len(chars))
    for c in chars:
        rpg = c.get('rpg_stats', {})
        base_stats = rpg.get('base_stats', {})
        stat_sum = sum(base_stats.get(k, 0) for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting'])
        print(f"  {c.get('display_name')}: rpg_enabled={rpg.get('enabled')}, level={rpg.get('level')}, stat_sum={stat_sum}, avatar={c.get('avatar')[:50]}...")
