#!/usr/bin/env python3
"""
Empirical Challenger Verification Script for Milestone 3
Targets:
- Chat Log: chat_log_PJx1W1rg3WUzRM7MnQrkN
- World: _YpX47fNraQFw2dD7TdycJ
- Characters: GET /api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ
"""

import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

# Fix stdout encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
REFRESH_SCRIPT = ROOT / 'scratch' / 'refresh_token.py'

CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
WORLD_ID = "_YpX47fNraQFw2dD7TdycJ"

def get_token():
    if TOKEN_PATH.exists():
        tok = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if tok:
            return tok
    import subprocess
    subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
    return TOKEN_PATH.read_text(encoding='utf-8').strip()

def api_get(url, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            return resp.status, json.loads(data) if data else {}
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            import subprocess
            subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
            new_tok = TOKEN_PATH.read_text(encoding='utf-8').strip()
            headers['Authorization'] = f'Bearer {new_tok}'
            retry_req = urllib.request.Request(url, headers=headers, method='GET')
            with urllib.request.urlopen(retry_req) as r2:
                data = r2.read().decode('utf-8')
                return r2.status, json.loads(data) if data else {}
        err = e.read().decode('utf-8', errors='replace')
        print(f"[FAIL] HTTP {e.code} for GET {url}: {err[:300]}")
        raise

def main():
    token = get_token()
    print("=== EMPIRICAL CHALLENGER VERIFICATION FOR MILESTONE 3 ===")

    # 1. Chat Log Query
    chat_url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}"
    status_chat, chat_data = api_get(chat_url, token)
    print(f"\n[1] Chat Log Query ({CHAT_LOG_ID}): HTTP {status_chat}")
    print(f"Top-level keys in chat_data: {list(chat_data.keys())}")

    # Inspect chat_overrides at root and in memory
    root_co = chat_data.get('chat_overrides')
    mem = chat_data.get('memory') or {}
    mem_co = mem.get('chat_overrides') if isinstance(mem, dict) else None

    print(f"Root chat_overrides present: {root_co is not None}")
    if root_co:
        print(f"Root chat_overrides: {json.dumps(root_co, indent=2)}")
    print(f"Memory chat_overrides present: {mem_co is not None}")
    if mem_co:
        print(f"Memory chat_overrides: {json.dumps(mem_co, indent=2)}")

    vnMode_root = root_co.get('values', {}).get('vnMode') if isinstance(root_co, dict) else None
    vnMode_mem = mem_co.get('values', {}).get('vnMode') if isinstance(mem_co, dict) else None
    print(f"vnMode (root): {vnMode_root}")
    print(f"vnMode (memory): {vnMode_mem}")

    # party_tied
    party_tied = chat_data.get('party_tied')
    print(f"party_tied: {party_tied}")

    # auto_approve across levels
    root_auto_approve = chat_data.get('auto_approve')
    mem_scan_auto_approve = mem.get('memory_scan', {}).get('auto_approve') if isinstance(mem, dict) else None
    scene_sum_auto_approve = mem.get('scene_summaries', {}).get('auto_approve') if isinstance(mem, dict) else None
    print(f"root auto_approve: {root_auto_approve}")
    print(f"memory.memory_scan.auto_approve: {mem_scan_auto_approve}")
    print(f"memory.scene_summaries.auto_approve: {scene_sum_auto_approve}")

    # Additional chat attributes
    print(f"chat_data.party: {chat_data.get('party')}")
    print(f"chat_data.world_id: {chat_data.get('world_id')}")
    print(f"chat_data.scenario_id: {chat_data.get('scenario_id')}")

    # 2. World Query
    world_url = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"
    status_world, world_data = api_get(world_url, token)
    print(f"\n[2] World Query ({WORLD_ID}): HTTP {status_world}")
    wf = world_data.get('world_features') or {}
    print(f"world_features.vn_mode: {wf.get('vn_mode')}")
    print(f"world_features.rpg_stats: {wf.get('rpg_stats')}")
    print(f"world_features.combat: {wf.get('combat')}")
    print(f"world_features.show_party_stats: {wf.get('show_party_stats')}")
    print(f"enable_ai_tool_creation: {world_data.get('enable_ai_tool_creation')}")

    # 3. Characters Query
    chars_url = f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}"
    status_chars, chars_data = api_get(chars_url, token)
    print(f"\n[3] World Characters Query: HTTP {status_chars}")
    print(f"Total characters returned: {len(chars_data)}")

    expected_names = [
        "Erik Ulfr Douglas",
        "Logan Járn Douglas",
        "Edric Douglas",
        "Noah Loki Douglas Bloodmoon",
        "Malachia Björn Douglas Bloodmoon",
        "Jasper Svartr Douglas Bloodmoon",
        "Alyssa Hvit Douglas Bloodmoon",
        "Wulfnic Báleygr Bloodmoon",
        "Zefir Hvitskog",
        "Mackenzie Sanchez-Rogers",
        "Finnegan Novak",
        "Sierra Cruz",
        "Scarlett Rose"
    ]

    char_names_found = []
    char_anomalies = []

    for idx, c in enumerate(chars_data):
        c_id = c.get('id')
        name = c.get('name') or c.get('display_name')
        d_name = c.get('display_name')
        char_names_found.append(d_name or name)
        rpg = c.get('rpg_stats')
        avatar = c.get('avatar')
        desc = c.get('description') or ''
        birthdate = c.get('birthdate')
        start_timeline = c.get('start_timeline_position')

        print(f"\nCharacter {idx+1}: {d_name} (ID: {c_id})")
        print(f"  Avatar: {avatar[:60] if avatar else 'MISSING'}...")
        print(f"  Desc length: {len(desc)} chars")
        print(f"  Birthdate: {birthdate}, StartTimeline: {start_timeline}")

        if not rpg:
            char_anomalies.append(f"{d_name}: missing rpg_stats")
            continue

        rpg_enabled = rpg.get('enabled')
        level = rpg.get('level')
        base_stats = rpg.get('base_stats') or {}
        print(f"  RPG enabled: {rpg_enabled}, Level: {level}")
        print(f"  Base stats: {base_stats}")

        stat_keys_1to6 = [f'stat_{i}' for i in range(1, 7)]
        named_keys = ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']

        missing_keys = [k for k in stat_keys_1to6 + named_keys if k not in base_stats]
        if missing_keys:
            char_anomalies.append(f"{d_name}: missing stat keys {missing_keys}")

        named_sum = sum(base_stats.get(k, 0) for k in named_keys)
        dual_sum = sum(base_stats.get(k, 0) for k in stat_keys_1to6)
        print(f"  Stat sum (named): {named_sum}, Stat sum (stat_1..6): {dual_sum}")

        if named_sum != 31:
            char_anomalies.append(f"{d_name}: named_sum is {named_sum} != 31")
        if dual_sum != 31:
            char_anomalies.append(f"{d_name}: dual_sum is {dual_sum} != 31")
        if not (1 <= level <= 99):
            char_anomalies.append(f"{d_name}: level {level} not in [1, 99]")
        if not avatar or not avatar.startswith("https://imagedelivery.net/"):
            char_anomalies.append(f"{d_name}: invalid avatar {avatar}")
        if len(desc) < 100:
            char_anomalies.append(f"{d_name}: description suspiciously short ({len(desc)} chars)")

    print("\n=== SUMMARY OF CHARACTER CHECKS ===")
    print(f"Expected 13: {len(expected_names)}")
    print(f"Found: {len(char_names_found)}")
    missing_characters = [n for n in expected_names if not any(n in f or f in n for f in char_names_found)]
    print(f"Missing characters: {missing_characters}")
    print(f"Anomalies detected: {char_anomalies}")

    # Output JSON summary for audit trail
    summary = {
        "chat_log_id": CHAT_LOG_ID,
        "world_id": WORLD_ID,
        "vnMode_root": vnMode_root,
        "vnMode_mem": vnMode_mem,
        "party_tied": party_tied,
        "root_auto_approve": root_auto_approve,
        "mem_scan_auto_approve": mem_scan_auto_approve,
        "scene_sum_auto_approve": scene_sum_auto_approve,
        "world_features": wf,
        "characters_count": len(chars_data),
        "missing_characters": missing_characters,
        "anomalies": char_anomalies
    }
    dump_path = ROOT / 'scratch' / 'challenger_m3_live_audit.json'
    with open(dump_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    print(f"\nAudit summary written to {dump_path}")

if __name__ == '__main__':
    main()
