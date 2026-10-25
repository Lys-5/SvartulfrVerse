import sys
import os
import json
import urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.patch_welcome_day_scenario_and_chat import get_auth_token

token = get_auth_token()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

chat_id = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
url = f"https://app.wyvern.chat/api/new/chat-logs/{chat_id}"

# Fetch current chat log state first
req_get = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req_get) as resp:
    current_chat = json.loads(resp.read().decode('utf-8'))

print("Current party_tied:", current_chat.get('party_tied'))
print("Current memory:", current_chat.get('memory'))

# Build payload
chat_overrides = {
    "version": 1,
    "values": {
        "vnMode": True,
        "vnTextSpeed": "normal",
        "vnDirections": True,
        "vnAutoAdvance": False,
        "vnAutoDelayMs": 2500,
        "vnSkipRead": False,
        "vnTextboxOpacity": 0.85,
        "vnSpriteLimit": 3,
        "vnItalicAsThought": False
    },
    "notes": {}
}

# Update memory with auto_approve: false and scene summaries auto-apply
memory = current_chat.get('memory') or {}
if not isinstance(memory, dict):
    memory = {}

memory_scan = memory.get('memory_scan') or {}
memory_scan['auto_approve'] = False
memory['memory_scan'] = memory_scan

scene_summaries = memory.get('scene_summaries') or {}
scene_summaries['auto_enabled'] = True
scene_summaries['replace_enabled'] = True
scene_summaries['dynamic_enabled'] = True
scene_summaries['tail_n'] = 12
scene_summaries['budget_fraction'] = 0.25
scene_summaries['auto_interval'] = 50
scene_summaries['auto_approve'] = False
scene_summaries['detail'] = "verbose"
memory['scene_summaries'] = scene_summaries

payload = {
    "chat_overrides": chat_overrides,
    "party_tied": True,
    "memory": memory
}

req_put = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
with urllib.request.urlopen(req_put) as resp:
    status = resp.status
    resp_data = json.loads(resp.read().decode('utf-8'))

print(f"PUT Status: {status}")
print("Updated chat_overrides:", resp_data.get('chat_overrides'))
print("Updated party_tied:", resp_data.get('party_tied'))
print("Updated memory:", resp_data.get('memory'))
