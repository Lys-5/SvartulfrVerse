import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

# 1. Chat log
req = urllib.request.Request('https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN', headers=headers)
with urllib.request.urlopen(req) as resp:
    chat = json.loads(resp.read().decode('utf-8'))

print('=== CHAT LOG LIVE INSPECTION ===')
print('chat.party_tied:', chat.get('party_tied'))
print('chat.chat_overrides:', json.dumps(chat.get('chat_overrides'), indent=2))
print('chat.memory.chat_overrides:', json.dumps(chat.get('memory', {}).get('chat_overrides'), indent=2))
print('chat.memory.memory_scan:', json.dumps(chat.get('memory', {}).get('memory_scan'), indent=2))
print('chat.memory.scene_summaries:', json.dumps(chat.get('memory', {}).get('scene_summaries'), indent=2))

# 2. World
req2 = urllib.request.Request('https://app.wyvern.chat/api/worlds/_YpX47fNraQFw2dD7TdycJ', headers=headers)
with urllib.request.urlopen(req2) as resp:
    world = json.loads(resp.read().decode('utf-8'))

print('\n=== WORLD LIVE INSPECTION ===')
print('world.world_features:', json.dumps(world.get('world_features'), indent=2))
print('world.enable_ai_tool_creation:', world.get('enable_ai_tool_creation'))

# 3. Characters
req3 = urllib.request.Request('https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ', headers=headers)
with urllib.request.urlopen(req3) as resp:
    chars = json.loads(resp.read().decode('utf-8'))

print(f'\n=== WORLD CHARACTERS COUNT: {len(chars)} ===')
stat_keys = ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']
for c in chars:
    rpg = c.get('rpg_stats') or {}
    bs = rpg.get('base_stats') or {}
    stat_sum = sum(bs.get(k, 0) for k in stat_keys)
    avatar = c.get('avatar', '')
    b = c.get('birthdate')
    s = c.get('start_timeline_position')
    print(f"Char: {c.get('display_name')} (ID: {c.get('id')})")
    print(f"  RPG Enabled: {rpg.get('enabled')} | Level: {rpg.get('level')} | Sum: {stat_sum}")
    print(f"  Base stats: {bs}")
    print(f"  Avatar: {avatar}")
    print(f"  Timeline: birthdate={b} ({type(b).__name__}), start_pos={s} ({type(s).__name__}), match={b==s}")
