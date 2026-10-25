#!/usr/bin/env python3
"""
scratch/challenger_m3_empirical_verification.py
Independent Empirical Verification & Stress Test Harness for Milestone 3.

Evaluates live Wyvern Web API endpoints:
1. GET /api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN
2. GET /api/worlds/_YpX47fNraQFw2dD7TdycJ
3. GET /api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ
4. Direct GET /api/worlds/characters/{id} for individual character persistence
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

CANONICAL_13_CHARACTERS = {
    "Erik Ulfr Douglas": {
        "level": 55, "birthdate": 10009344, "stats": {"might": 7, "resilience": 7, "agility": 4, "wit": 5, "presence": 7, "scouting": 1}
    },
    "Logan Járn Douglas": {
        "level": 49, "birthdate": 10054920, "stats": {"might": 7, "resilience": 6, "agility": 6, "wit": 4, "presence": 5, "scouting": 3}
    },
    "Edric Douglas": {
        "level": 13, "birthdate": 10371552, "stats": {"might": 3, "resilience": 3, "agility": 7, "wit": 5, "presence": 5, "scouting": 8}
    },
    "Noah Loki Douglas Bloodmoon": {
        "level": 25, "birthdate": 10262928, "stats": {"might": 6, "resilience": 6, "agility": 5, "wit": 6, "presence": 6, "scouting": 2}
    },
    "Malachia Björn Douglas Bloodmoon": {
        "level": 28, "birthdate": 10244064, "stats": {"might": 8, "resilience": 7, "agility": 5, "wit": 4, "presence": 5, "scouting": 2}
    },
    "Jasper Svartr Douglas Bloodmoon": {
        "level": 19, "birthdate": 10320312, "stats": {"might": 4, "resilience": 3, "agility": 8, "wit": 9, "presence": 3, "scouting": 4}
    },
    "Alyssa Hvit Douglas Bloodmoon": {
        "level": 19, "birthdate": 10320312, "stats": {"might": 2, "resilience": 4, "agility": 4, "wit": 7, "presence": 8, "scouting": 6}
    },
    "Wulfnic Báleygr Bloodmoon": {
        "level": 99, "birthdate": 0, "stats": {"might": 8, "resilience": 8, "agility": 5, "wit": 3, "presence": 5, "scouting": 2}
    },
    "Zefir Hvitskog": {
        "level": 99, "birthdate": 176424, "stats": {"might": 5, "resilience": 4, "agility": 9, "wit": 6, "presence": 3, "scouting": 4}
    },
    "Mackenzie Sanchez-Rogers": {
        "level": 19, "birthdate": 10316496, "stats": {"might": 8, "resilience": 7, "agility": 7, "wit": 3, "presence": 3, "scouting": 3}
    },
    "Finnegan Novak": {
        "level": 19, "birthdate": 10317984, "stats": {"might": 6, "resilience": 6, "agility": 8, "wit": 3, "presence": 4, "scouting": 4}
    },
    "Sierra Cruz": {
        "level": 18, "birthdate": 10323648, "stats": {"might": 7, "resilience": 6, "agility": 3, "wit": 8, "presence": 3, "scouting": 4}
    },
    "Scarlett Rose": {
        "level": 20, "birthdate": 10307808, "stats": {"might": 2, "resilience": 3, "agility": 6, "wit": 6, "presence": 9, "scouting": 5}
    }
}

def get_auth_token():
    if TOKEN_PATH.exists():
        tok = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if tok:
            return tok
    import subprocess
    subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
    return TOKEN_PATH.read_text(encoding='utf-8').strip()

def http_get(url, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        return resp.status, json.loads(content) if content else {}

def run_challenger_audit():
    print("================================================================================")
    print("CHALLENGER EMPIRICAL VERIFICATION HARNESS — MILESTONE 3")
    print("================================================================================")
    token = get_auth_token()
    failures = []
    passes = []

    # -------------------------------------------------------------------------
    # TEST 1: Chat Log Display Settings & Sidebar Flags
    # -------------------------------------------------------------------------
    print("\n[TEST 1] Querying Chat Log:", CHAT_LOG_ID)
    status_chat, chat_data = http_get(f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}", token)
    if status_chat != 200:
        failures.append(f"Chat log GET returned HTTP {status_chat}")
    else:
        passes.append("Chat log returned HTTP 200")

    # 1.1 party_tied
    party_tied = chat_data.get('party_tied')
    print(f"  party_tied: {party_tied}")
    if party_tied is True:
        passes.append("party_tied == True")
    else:
        failures.append(f"party_tied is {party_tied}, expected True")

    # 1.2 auto_approve flags
    mem = chat_data.get('memory') or {}
    mem_scan = mem.get('memory_scan') or {}
    scene_sums = mem.get('scene_summaries') or {}
    mem_scan_auto_approve = mem_scan.get('auto_approve')
    scene_sum_auto_approve = scene_sums.get('auto_approve')
    print(f"  memory_scan.auto_approve: {mem_scan_auto_approve}")
    print(f"  scene_summaries.auto_approve: {scene_sum_auto_approve}")

    if mem_scan_auto_approve is False:
        passes.append("memory_scan.auto_approve == False")
    else:
        failures.append(f"memory_scan.auto_approve is {mem_scan_auto_approve}, expected False")

    if scene_sum_auto_approve is False:
        passes.append("scene_summaries.auto_approve == False")
    else:
        failures.append(f"scene_summaries.auto_approve is {scene_sum_auto_approve}, expected False")

    # 1.3 chat_overrides.values.vnMode
    mem_co = mem.get('chat_overrides') or {}
    co_vals = mem_co.get('values') or {}
    vn_mode = co_vals.get('vnMode')
    print(f"  memory.chat_overrides.values.vnMode: {vn_mode}")
    if vn_mode is True:
        passes.append("chat_overrides.values.vnMode == True")
    else:
        failures.append(f"chat_overrides.values.vnMode is {vn_mode}, expected True")

    # Check secondary VN parameters
    expected_co_subset = {
        "vnTextSpeed": "normal",
        "vnDirections": True,
        "vnTextboxOpacity": 0.85,
        "vnSpriteLimit": 3,
        "vnAutoAdvance": False,
        "vnAutoDelayMs": 2500,
        "vnSkipRead": False,
        "vnItalicAsThought": False
    }
    for k, v in expected_co_subset.items():
        actual = co_vals.get(k)
        if actual == v:
            passes.append(f"chat_overrides.values.{k} == {v}")
        else:
            failures.append(f"chat_overrides.values.{k} is {actual}, expected {v}")

    # -------------------------------------------------------------------------
    # TEST 2: World Features & AI Tool Creation
    # -------------------------------------------------------------------------
    print("\n[TEST 2] Querying World Core:", WORLD_ID)
    status_world, world_data = http_get(f"https://app.wyvern.chat/api/worlds/{WORLD_ID}", token)
    if status_world != 200:
        failures.append(f"World GET returned HTTP {status_world}")
    else:
        passes.append("World returned HTTP 200")

    wf = world_data.get('world_features') or {}
    print(f"  world_features.vn_mode: {wf.get('vn_mode')}")
    print(f"  world_features.rpg_stats: {wf.get('rpg_stats')}")
    print(f"  world_features.combat: {wf.get('combat')}")
    print(f"  world_features.show_party_stats: {wf.get('show_party_stats')}")
    print(f"  enable_ai_tool_creation: {world_data.get('enable_ai_tool_creation')}")

    if wf.get('vn_mode') is True:
        passes.append("world_features.vn_mode == True")
    else:
        failures.append(f"world_features.vn_mode is {wf.get('vn_mode')}, expected True")

    if wf.get('rpg_stats') is True:
        passes.append("world_features.rpg_stats == True")
    else:
        failures.append(f"world_features.rpg_stats is {wf.get('rpg_stats')}, expected True")

    if wf.get('show_party_stats') is True:
        passes.append("world_features.show_party_stats == True")
    else:
        failures.append(f"world_features.show_party_stats is {wf.get('show_party_stats')}, expected True")

    if world_data.get('enable_ai_tool_creation') is False:
        passes.append("enable_ai_tool_creation == False")
    else:
        failures.append(f"enable_ai_tool_creation is {world_data.get('enable_ai_tool_creation')}, expected False")

    # -------------------------------------------------------------------------
    # TEST 3: 13 World Characters & Character Sheets
    # -------------------------------------------------------------------------
    print("\n[TEST 3] Querying World Characters for World:", WORLD_ID)
    status_chars, chars_list = http_get(f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}", token)
    if status_chars != 200:
        failures.append(f"World Characters GET returned HTTP {status_chars}")
    else:
        passes.append("World Characters returned HTTP 200")

    print(f"  Count of returned characters: {len(chars_list)}")
    if len(chars_list) == 13:
        passes.append("Exact character count == 13")
    else:
        failures.append(f"Characters count is {len(chars_list)}, expected 13")

    chars_by_name = {c.get('display_name'): c for c in chars_list}
    seen_ids = set()

    for canon_name, canon_spec in CANONICAL_13_CHARACTERS.items():
        c = chars_by_name.get(canon_name)
        if not c:
            failures.append(f"Character {canon_name} not found in world characters list")
            continue

        cid = c.get('id') or c.get('_id')
        if cid in seen_ids:
            failures.append(f"Duplicate character ID {cid} detected for {canon_name}")
        seen_ids.add(cid)

        # RPG stats
        rpg = c.get('rpg_stats') or {}
        rpg_enabled = rpg.get('enabled')
        if rpg_enabled is True:
            passes.append(f"{canon_name}: rpg_stats.enabled == True")
        else:
            failures.append(f"{canon_name}: rpg_stats.enabled is {rpg_enabled}, expected True")

        # Level
        level = rpg.get('level')
        if level == canon_spec['level']:
            passes.append(f"{canon_name}: level == {level}")
        else:
            failures.append(f"{canon_name}: level is {level}, expected {canon_spec['level']}")

        # Base stats
        bs = rpg.get('base_stats') or {}
        stat_sum = sum(bs.get(k, 0) for k in ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting'])
        if stat_sum == 31:
            passes.append(f"{canon_name}: base stats sum == 31")
        else:
            failures.append(f"{canon_name}: base stats sum is {stat_sum}, expected 31")

        # Dual keys check
        for i in range(1, 7):
            if f'stat_{i}' not in bs:
                failures.append(f"{canon_name}: missing stat_{i}")
        for k, v in canon_spec['stats'].items():
            if bs.get(k) != v:
                failures.append(f"{canon_name}: stat {k} is {bs.get(k)}, expected {v}")

        # CDN avatar
        avatar = c.get('avatar') or ''
        if avatar.startswith("https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/"):
            passes.append(f"{canon_name}: valid Cloudflare CDN avatar")
        else:
            failures.append(f"{canon_name}: invalid avatar {avatar}")

        # Profile / long_summary
        long_sum = c.get('long_summary') or ''
        if len(long_sum) > 4000:
            passes.append(f"{canon_name}: long_summary populated ({len(long_sum)} chars)")
        else:
            failures.append(f"{canon_name}: long_summary too short ({len(long_sum)} chars)")

        # Em-dash check
        if '\u2014' in long_sum or '\u2014' in (c.get('summary') or '') or '\u2014' in canon_name:
            failures.append(f"{canon_name}: em-dash found in profile text")

        print(f"  [PASS] {canon_name} (ID: {cid}): Lv={level}, Sum={stat_sum}, RPG={rpg_enabled}, Text={len(long_sum)} chars")

    # -------------------------------------------------------------------------
    # TEST 4: Direct Single Character GET Probe
    # -------------------------------------------------------------------------
    print("\n[TEST 4] Direct Single Character GET Probes...")
    sample_erik = chars_by_name.get("Erik Ulfr Douglas")
    if sample_erik:
        erik_id = sample_erik.get('id') or sample_erik.get('_id')
        st_e, data_e = http_get(f"https://app.wyvern.chat/api/worlds/characters/{erik_id}", token)
        if st_e == 200 and data_e.get('display_name') == "Erik Ulfr Douglas":
            passes.append(f"Single character GET /api/worlds/characters/{erik_id} returned HTTP 200 and matches Erik")
            print(f"  [PASS] Single Character GET {erik_id} succeeded.")
        else:
            failures.append(f"Single character GET failed: HTTP {st_e}")

    # -------------------------------------------------------------------------
    # FINAL VERDICT
    # -------------------------------------------------------------------------
    print("\n================================================================================")
    print(f"AUDIT COMPLETE: {len(passes)} checks passed, {len(failures)} failures.")
    print("================================================================================")

    if failures:
        print("\n[FAILURES DETECTED]:")
        for f in failures:
            print(f"  - {f}")
        verdict = "CHALLENGE"
    else:
        print("\nAll empirical assertions passed with 100% compliance!")
        verdict = "APPROVE"

    print(f"\n>>> FINAL VERDICT: {verdict} <<<\n")
    return verdict, passes, failures

if __name__ == '__main__':
    verdict, passes, failures = run_challenger_audit()
    sys.exit(0 if verdict == "APPROVE" else 1)
