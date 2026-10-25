import json
import re
import urllib.request
from pathlib import Path

ROOT = Path('e:/repository/SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = TOKEN_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

print("=== 1. Live GET Scenario Verification ===")
scenario_url = "https://app.wyvern.chat/api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H"
req_sc = urllib.request.Request(scenario_url, headers=headers)
with urllib.request.urlopen(req_sc) as resp:
    sc_code = resp.status
    live_sc = json.loads(resp.read().decode('utf-8'))

print(f"Status: {sc_code}")
print(f"Scenario ID: {live_sc.get('id')}")
print(f"Scenario Name: {live_sc.get('name')}")
print(f"World ID: {live_sc.get('world')}")
scenes = live_sc.get('premade_scenes', [])
print(f"Premade scenes count: {len(scenes)}")

for idx, scene in enumerate(scenes):
    sid = scene.get('id')
    desc = scene.get('description')
    text = scene.get('scene_text', '')
    
    # Check em-dashes
    em_dashes = [c for c in text if c in '—\u2014\u2013\u2015']
    # Check asterisks
    asterisks = [c for c in text if c == '*']
    # Check quotes balance
    double_quotes = [c for c in text if c == '"']
    curly_quotes = [c for c in text if c in '“”']
    
    # Check speaker tags
    tags = re.findall(r'^=>([A-Za-z0-9_]+):', text, flags=re.MULTILINE)
    
    # Check plain prefixes
    plain = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', text, flags=re.MULTILINE)
    plain = [p for p in plain if not p.startswith('=>')]
    
    print(f"\n--- Scene {idx}: {sid} ---")
    print(f"  Title: {desc}")
    print(f"  Length: {len(text)} characters")
    print(f"  Em-dashes count: {len(em_dashes)}")
    print(f"  Asterisks count: {len(asterisks)}")
    print(f"  Double quotes count: {len(double_quotes)} (balanced: {len(double_quotes) % 2 == 0})")
    print(f"  Curly quotes count: {len(curly_quotes)}")
    print(f"  Speaker tags count: {len(tags)}")
    print(f"  Tags: {tags}")
    print(f"  Plain prefixes: {plain}")

print("\n=== 2. Compare Local Scenario JSON vs Live Scenario ===")
with open(ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json', 'r', encoding='utf-8') as f:
    local_sc = json.load(f)

for idx in range(3):
    local_text = local_sc['premade_scenes'][idx]['scene_text']
    live_text = scenes[idx]['scene_text']
    if local_text == live_text:
        print(f"Scene {idx} text: 100% IDENTICAL BYTE-FOR-BYTE")
    else:
        print(f"Scene {idx} text: MISMATCH! local len={len(local_text)} vs live len={len(live_text)}")

print("\n=== 3. Live GET Chat Log Verification ===")
chat_url = "https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN"
req_chat = urllib.request.Request(chat_url, headers=headers)
with urllib.request.urlopen(req_chat) as resp:
    chat_code = resp.status
    live_chat = json.loads(resp.read().decode('utf-8'))

print(f"Status: {chat_code}")
messages = live_chat.get('messages', [])
print(f"Total messages in chat: {len(messages)}")

msg0 = messages[0]
print(f"Message 0 ID: {msg0.get('id')}")
swipes = msg0.get('swipes', [])
print(f"Message 0 swipes count: {len(swipes)}")
swipe0 = swipes[0]
print(f"Swipe 0 ID: {swipe0.get('id')}")

swipe_content = swipe0.get('content', '')
msg_content = msg0.get('content', '')

# Check em-dashes
em_dashes_swipe = [c for c in swipe_content if c in '—\u2014\u2013\u2015']
asterisks_swipe = [c for c in swipe_content if c == '*']
double_quotes_swipe = [c for c in swipe_content if c == '"']
curly_quotes_swipe = [c for c in swipe_content if c in '“”']
tags_swipe = re.findall(r'^=>([A-Za-z0-9_]+):', swipe_content, flags=re.MULTILINE)
plain_swipe = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', swipe_content, flags=re.MULTILINE)
plain_swipe = [p for p in plain_swipe if not p.startswith('=>')]
user_macros_swipe = re.findall(r'\{\{[^}]+\}\}', swipe_content)

print(f"\nSwipe 0 Analysis:")
print(f"  Length: {len(swipe_content)} characters")
print(f"  Em-dashes count: {len(em_dashes_swipe)}")
print(f"  Asterisks count: {len(asterisks_swipe)}")
print(f"  Double quotes count: {len(double_quotes_swipe)} (balanced: {len(double_quotes_swipe) % 2 == 0})")
print(f"  Curly quotes count: {len(curly_quotes_swipe)}")
print(f"  Speaker tags count: {len(tags_swipe)}")
print(f"  Tags: {tags_swipe}")
print(f"  Plain prefixes: {plain_swipe}")
print(f"  User macros in swipe: {user_macros_swipe}")

if msg_content == swipe_content:
    print("  Message 0 content == Swipe 0 content: YES (100% identical)")
else:
    print(f"  Message 0 content vs Swipe 0 content: DIFFERENT len({len(msg_content)}) vs len({len(swipe_content)})")
