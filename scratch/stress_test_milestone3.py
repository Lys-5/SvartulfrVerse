#!/usr/bin/env python3
"""
scratch/stress_test_milestone3.py
Empirical stress-testing and boundary verification harness for Milestone 3.
Executed by: challenger_m3_2
"""

import sys
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
WORLD_ID = "_YpX47fNraQFw2dD7TdycJ"

EXPECTED_13_NAMES = [
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

EXPECTED_VN_VALUES = {
    "vnMode": True,
    "vnTextSpeed": "normal",
    "vnDirections": True,
    "vnAutoAdvance": False,
    "vnAutoDelayMs": 2500,
    "vnSkipRead": False,
    "vnTextboxOpacity": 0.85,
    "vnSpriteLimit": 3,
    "vnItalicAsThought": False
}


def get_token():
    assert TOKEN_PATH.exists(), f"Token path {TOKEN_PATH} does not exist"
    token = TOKEN_PATH.read_text(encoding='utf-8').strip()
    assert len(token) > 20, "Token is too short or empty"
    return token


def fetch_api(endpoint, token):
    url = f"https://app.wyvern.chat/api/{endpoint}"
    req = urllib.request.Request(
        url,
        headers={
            'Authorization': f'Bearer {token}',
            'User-Agent': 'Challenger-Empirical-Harness/1.0',
            'Cache-Control': 'no-cache, no-store, must-revalidate'
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        assert resp.status == 200, f"HTTP status {resp.status} != 200 for {url}"
        data = resp.read().decode('utf-8')
        return json.loads(data)


def main():
    print("=== EMPIRICAL STRESS TEST: MILESTONE 3 ===")
    token = get_token()
    print(f"Token loaded (length: {len(token)})")

    # 1. Stress-test Chat Overrides Persistence across 5 consecutive re-fetches
    print("\n--- TEST 1: Chat Overrides Re-fetch Persistence (5 rounds) ---")
    chat_endpoint = f"new/chat-logs/{CHAT_LOG_ID}"
    fetches = []
    for i in range(5):
        t0 = time.time()
        chat_data = fetch_api(chat_endpoint, token)
        dt = time.time() - t0
        fetches.append(chat_data)
        print(f"Round {i+1}: GET {chat_endpoint} returned in {dt:.3f}s")
        time.sleep(0.5)

    # Check persistence and stability across all 5 fetches
    for i, data in enumerate(fetches):
        # Check top-level chat_overrides
        top_co = data.get('chat_overrides')
        # Check memory.chat_overrides
        mem = data.get('memory', {})
        mem_co = mem.get('chat_overrides')

        assert mem_co is not None, f"Round {i+1}: memory.chat_overrides is None!"
        assert mem_co.get('version') == 1, f"Round {i+1}: memory.chat_overrides version != 1"
        mem_vals = mem_co.get('values', {})
        for k, expected_v in EXPECTED_VN_VALUES.items():
            actual_v = mem_vals.get(k)
            assert actual_v == expected_v, (
                f"Round {i+1}: memory.chat_overrides.values[{k}] is {actual_v} != {expected_v}"
            )

        # Check top-level if present
        if top_co is not None:
            top_vals = top_co.get('values', {})
            for k, expected_v in EXPECTED_VN_VALUES.items():
                actual_v = top_vals.get(k)
                assert actual_v == expected_v, (
                    f"Round {i+1}: chat_overrides.values[{k}] is {actual_v} != {expected_v}"
                )

        # Check party_tied
        assert data.get('party_tied') is True, f"Round {i+1}: party_tied != True"

        # Check scene_summaries auto-apply flags
        ss = mem.get('scene_summaries', {})
        assert ss.get('auto_enabled') is True, f"Round {i+1}: scene_summaries.auto_enabled != True"
        assert ss.get('replace_enabled') is True, f"Round {i+1}: scene_summaries.replace_enabled != True"
        assert ss.get('dynamic_enabled') is True, f"Round {i+1}: scene_summaries.dynamic_enabled != True"

        # Check AI content creation disabled at chat level
        assert mem.get('memory_scan', {}).get('auto_approve') is False, (
            f"Round {i+1}: memory.memory_scan.auto_approve != False"
        )
        assert ss.get('auto_approve') is False, (
            f"Round {i+1}: memory.scene_summaries.auto_approve != False"
        )

    print(">>> PASS: Chat overrides and sidebar flags persisted identically across all 5 re-fetches.")

    # 2. Test World Level Flags
    print("\n--- TEST 2: World Level Features & AI Content Creation ---")
    world_endpoint = f"worlds/{WORLD_ID}"
    world_data = fetch_api(world_endpoint, token)

    wf = world_data.get('world_features', {})
    print(f"World features: vn_mode={wf.get('vn_mode')}, rpg_stats={wf.get('rpg_stats')}, combat={wf.get('combat')}, show_party_stats={wf.get('show_party_stats')}")
    assert wf.get('vn_mode') is True, "world_features.vn_mode is not True"
    assert wf.get('rpg_stats') is True, "world_features.rpg_stats is not True"
    assert wf.get('combat') is True, "world_features.combat is not True"

    ai_tool_creation = world_data.get('enable_ai_tool_creation')
    print(f"World enable_ai_tool_creation: {ai_tool_creation}")
    assert ai_tool_creation is False, f"World enable_ai_tool_creation is {ai_tool_creation} != False"
    print(">>> PASS: World features and AI content creation guardrails verified.")

    # 3. Test World Characters RPG Blocks & Avatars
    print("\n--- TEST 3: World Characters (13 Characters RPG & Avatar Invariants) ---")
    chars_endpoint = f"worlds/characters/world/{WORLD_ID}"
    chars_data = fetch_api(chars_endpoint, token)

    print(f"Retrieved {len(chars_data)} characters from world {WORLD_ID}")
    assert len(chars_data) == 13, f"Character count is {len(chars_data)} != 13"

    retrieved_names = [c.get('name') or c.get('display_name') for c in chars_data]
    print(f"Character names: {retrieved_names}")

    missing_names = set(EXPECTED_13_NAMES) - set(retrieved_names)
    assert not missing_names, f"Missing expected characters: {missing_names}"

    for c in chars_data:
        char_name = c.get('display_name') or c.get('name')
        char_id = c.get('id') or c.get('_id')
        print(f"\nEvaluating: {char_name} (ID: {char_id})")

        # Name non-empty
        assert char_name and char_name.strip(), f"Empty name for character {char_id}"

        # Avatar non-empty & valid CDN URL
        avatar = c.get('avatar')
        assert avatar and avatar.strip(), f"Empty avatar for {char_name}"
        assert avatar.startswith("https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/"), (
            f"Avatar URL invalid for {char_name}: {avatar}"
        )
        print(f"  Avatar: {avatar[:60]}... [VALID CDN]")

        # RPG stats block
        rpg = c.get('rpg_stats')
        assert rpg is not None, f"Character {char_name} has NO rpg_stats"
        assert rpg.get('enabled') is True, f"Character {char_name} rpg_stats.enabled is not True"

        level = rpg.get('level')
        assert isinstance(level, int), f"Character {char_name} level {level} is not int"
        assert 1 <= level <= 99, f"Character {char_name} level {level} outside [1, 99]"
        print(f"  Level: {level}")

        # Check special cap for Wulfnic and Zefir
        if "Wulfnic" in char_name or "Zefir" in char_name:
            assert level == 99, f"Centenarian {char_name} level {level} != 99 cap!"

        # Base stats
        bs = rpg.get('base_stats', {})
        named_keys = ['might', 'resilience', 'agility', 'wit', 'presence', 'scouting']
        for k in named_keys:
            val = bs.get(k)
            assert isinstance(val, int), f"{char_name} stat {k} is not int: {val}"
            assert val >= 1, f"{char_name} stat {k} is < 1: {val}"

        # Check numbered stats stat_1..6
        for idx, k in enumerate(named_keys, start=1):
            num_key = f"stat_{idx}"
            num_val = bs.get(num_key)
            named_val = bs.get(k)
            assert num_val == named_val, (
                f"{char_name} mismatch: {num_key}={num_val} != {k}={named_val}"
            )

        stat_sum = sum(bs[k] for k in named_keys)
        print(f"  Base stats: MGT={bs['might']}, RES={bs['resilience']}, AGI={bs['agility']}, WIT={bs['wit']}, PRS={bs['presence']}, SCT={bs['scouting']} => SUM = {stat_sum}")
        assert stat_sum == 31, f"{char_name} base stats sum {stat_sum} != 31 (25-pt budget violated!)"

    print("\n>>> PASS: All 13 World Characters satisfy all invariants.")

    # 4. Check CDN Avatar Reachability (Adversarial stress check)
    print("\n--- TEST 4: CDN Avatar HTTP Reachability Spot Check ---")
    for c in chars_data[:3]:  # Check first 3 avatars with HTTP HEAD/GET
        char_name = c.get('display_name') or c.get('name')
        avatar_url = c.get('avatar')
        req = urllib.request.Request(
            avatar_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                print(f"  {char_name}: HTTP {r.status} Content-Type: {r.headers.get('Content-Type')}")
                assert r.status == 200
        except Exception as e:
            print(f"  WARNING: Avatar fetch for {char_name} failed: {e}")
            raise

    print("\n=== ALL EMPIRICAL CHALLENGE TESTS PASSED SUCCESSFULLY! ===")


if __name__ == '__main__':
    main()
