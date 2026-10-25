#!/usr/bin/env python3
"""
auditor_m2_1/independent_live_cloud_audit.py
Independent live forensic audit script for Milestone 2.
Directly queries live Wyvern API cloud without using any worker helper classes.
"""

import sys
import os
import json
import re
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path("e:/repository/SvartulfrVerse")
TOKEN_PATH = ROOT / "scratch" / "wyvern_token.txt"

SCENARIO_ID = "_2MTWKjxrQPdQVaz9y4Q7H"
CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
SWIPE_ID = "message_swipe_99mmMgEEQjk2pkJN3hXkQ"

EXPECTED_SCENE_0_TAGS = [
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Jasper',
    'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett'
]

EXPECTED_SCENE_1_TAGS = [
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Alyssa',
    'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett'
]

EXPECTED_SCENE_2_TAGS = [
    'Narrator', 'Erik', 'Logan', 'Narrator'
]

EXPECTED_MSG0_TAGS = EXPECTED_SCENE_0_TAGS

def audit():
    print("=== FORENSIC AUDIT: LIVE WYVERN API PERSISTENCE CHECK ===")
    if not TOKEN_PATH.exists():
        print(f"[FAIL] Token path does not exist: {TOKEN_PATH}")
        sys.exit(1)
        
    token = TOKEN_PATH.read_text(encoding='utf-8').strip()
    if not token:
        print("[FAIL] Token is empty")
        sys.exit(1)
    print(f"[OK] Token loaded (length: {len(token)} chars)")

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'AuditorM2-IndependentProbe/1.0'
    }

    # 1. Query Scenario
    sc_url = f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}"
    print(f"\n[QUERY 1] GET {sc_url}")
    sc_req = urllib.request.Request(sc_url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(sc_req) as resp:
            status = resp.status
            sc_raw = resp.read().decode('utf-8')
            print(f"[RESPONSE] HTTP {status}, raw bytes={len(sc_raw)}")
            sc_data = json.loads(sc_raw)
    except urllib.error.HTTPError as e:
        print(f"[FAIL] Live Scenario GET failed with HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}")
        sys.exit(1)

    print(f"Scenario ID: {sc_data.get('id')}")
    print(f"Scenario Name: {sc_data.get('name')}")
    print(f"Scenario World: {sc_data.get('world')}")
    print(f"Updated At: {sc_data.get('updated_at')}")

    premade_scenes = sc_data.get('premade_scenes', [])
    print(f"Premade scenes count: {len(premade_scenes)}")
    assert len(premade_scenes) == 3, f"Expected 3 scenes, got {len(premade_scenes)}"

    # Audit Scene 0
    sc0 = premade_scenes[0]
    sc0_text = sc0.get('scene_text', '')
    sc0_id = sc0.get('id')
    sc0_name = sc0.get('name')
    sc0_tags = re.findall(r'^=>([A-Za-z0-9_]+):', sc0_text, flags=re.MULTILINE)
    sc0_em = sc0_text.count('—')
    sc0_ast = sc0_text.count('*')
    print(f"\n--- Scene 0 [{sc0_id} - {sc0_name}] ---")
    print(f"  Length: {len(sc0_text)} chars")
    print(f"  Em-dashes: {sc0_em}")
    print(f"  Asterisks: {sc0_ast}")
    print(f"  Starts with =>Narrator: {sc0_text.startswith('=>Narrator:')}")
    print(f"  Tags found ({len(sc0_tags)}): {sc0_tags}")
    assert sc0_em == 0, f"Scene 0 contains {sc0_em} em-dashes"
    assert sc0_ast == 0, f"Scene 0 contains {sc0_ast} asterisks"
    assert sc0_tags == EXPECTED_SCENE_0_TAGS, f"Scene 0 tags mismatch: {sc0_tags}"
    print("  [PASS] Scene 0 is 100% compliant!")

    # Audit Scene 1
    sc1 = premade_scenes[1]
    sc1_text = sc1.get('scene_text', '')
    sc1_id = sc1.get('id')
    sc1_name = sc1.get('name')
    sc1_tags = re.findall(r'^=>([A-Za-z0-9_]+):', sc1_text, flags=re.MULTILINE)
    sc1_em = sc1_text.count('—')
    sc1_ast = sc1_text.count('*')
    print(f"\n--- Scene 1 [{sc1_id} - {sc1_name}] ---")
    print(f"  Length: {len(sc1_text)} chars")
    print(f"  Em-dashes: {sc1_em}")
    print(f"  Asterisks: {sc1_ast}")
    print(f"  Starts with =>Narrator: {sc1_text.startswith('=>Narrator:')}")
    print(f"  Tags found ({len(sc1_tags)}): {sc1_tags}")
    assert sc1_em == 0, f"Scene 1 contains {sc1_em} em-dashes"
    assert sc1_ast == 0, f"Scene 1 contains {sc1_ast} asterisks"
    assert sc1_tags == EXPECTED_SCENE_1_TAGS, f"Scene 1 tags mismatch: {sc1_tags}"
    print("  [PASS] Scene 1 is 100% compliant!")

    # Audit Scene 2
    sc2 = premade_scenes[2]
    sc2_text = sc2.get('scene_text', '')
    sc2_id = sc2.get('id')
    sc2_name = sc2.get('name')
    sc2_tags = re.findall(r'^=>([A-Za-z0-9_]+):', sc2_text, flags=re.MULTILINE)
    sc2_em = sc2_text.count('—')
    sc2_ast = sc2_text.count('*')
    print(f"\n--- Scene 2 [{sc2_id} - {sc2_name}] ---")
    print(f"  Length: {len(sc2_text)} chars")
    print(f"  Em-dashes: {sc2_em}")
    print(f"  Asterisks: {sc2_ast}")
    print(f"  Starts with =>Narrator: {sc2_text.startswith('=>Narrator:')}")
    print(f"  Tags found ({len(sc2_tags)}): {sc2_tags}")
    assert sc2_em == 0, f"Scene 2 contains {sc2_em} em-dashes"
    assert sc2_ast == 0, f"Scene 2 contains {sc2_ast} asterisks"
    assert sc2_tags == EXPECTED_SCENE_2_TAGS, f"Scene 2 tags mismatch: {sc2_tags}"
    print("  [PASS] Scene 2 is 100% compliant!")

    # 2. Query Chat Log
    chat_url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}"
    print(f"\n[QUERY 2] GET {chat_url}")
    chat_req = urllib.request.Request(chat_url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(chat_req) as resp:
            status_chat = resp.status
            chat_raw = resp.read().decode('utf-8')
            print(f"[RESPONSE] HTTP {status_chat}, raw bytes={len(chat_raw)}")
            chat_data = json.loads(chat_raw)
    except urllib.error.HTTPError as e:
        print(f"[FAIL] Live Chat Log GET failed with HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}")
        sys.exit(1)

    print(f"Chat ID: {chat_data.get('id')}")
    print(f"Chat Character/World: {chat_data.get('character_id')} / {chat_data.get('world_id')}")
    print(f"Chat Updated At: {chat_data.get('updated_at')}")

    messages = chat_data.get('messages', [])
    print(f"Messages count: {len(messages)}")
    assert len(messages) >= 1, f"Expected at least 1 message, got {len(messages)}"

    msg0 = messages[0]
    msg0_id = msg0.get('id')
    msg0_swipes = msg0.get('swipes', [])
    print(f"Message 0 ID: {msg0_id}, Swipes count: {len(msg0_swipes)}")
    assert len(msg0_swipes) >= 1, f"Expected at least 1 swipe, got {len(msg0_swipes)}"

    # Check swipe
    target_swipe = None
    for sw in msg0_swipes:
        if sw.get('id') == SWIPE_ID:
            target_swipe = sw
            break

    if target_swipe is None:
        target_swipe = msg0_swipes[0]
        print(f"[WARN] Target swipe ID {SWIPE_ID} not explicitly matched; checking swipe 0 ({target_swipe.get('id')})")
    else:
        print(f"[OK] Found target swipe ID {SWIPE_ID}")

    sw_text = target_swipe.get('content', '')
    sw_em = sw_text.count('—')
    sw_ast = sw_text.count('*')
    sw_tags = re.findall(r'^=>([A-Za-z0-9_]+):', sw_text, flags=re.MULTILINE)
    print(f"\n--- Message 0 Swipe [{target_swipe.get('id')}] ---")
    print(f"  Length: {len(sw_text)} chars")
    print(f"  Em-dashes: {sw_em}")
    print(f"  Asterisks: {sw_ast}")
    print(f"  Starts with =>Narrator: {sw_text.startswith('=>Narrator:')}")
    print(f"  Tags found ({len(sw_tags)}): {sw_tags}")
    assert sw_em == 0, f"Swipe contains {sw_em} em-dashes"
    assert sw_ast == 0, f"Swipe contains {sw_ast} asterisks"
    assert sw_tags == EXPECTED_MSG0_TAGS, f"Swipe tags mismatch: {sw_tags}"
    print("  [PASS] Message 0 Swipe is 100% compliant!")

    # Check message level content
    msg0_content = msg0.get('content', '')
    print(f"\n--- Message 0 Active Content ---")
    print(f"  Length: {len(msg0_content)} chars")
    print(f"  Em-dashes: {msg0_content.count('—')}")
    print(f"  Asterisks: {msg0_content.count('*')}")
    msg0_tags = re.findall(r'^=>([A-Za-z0-9_]+):', msg0_content, flags=re.MULTILINE)
    print(f"  Tags found ({len(msg0_tags)}): {msg0_tags}")
    assert msg0_content.count('—') == 0
    assert msg0_content.count('*') == 0
    assert msg0_tags == EXPECTED_MSG0_TAGS

    print("\n=== LIVE CLOUD INTEGRITY VERIFIED: 100% AUTHENTIC AND PERSISTENT ===")

if __name__ == '__main__':
    audit()
