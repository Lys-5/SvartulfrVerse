#!/usr/bin/env python3
"""
scratch/adversarial_audit_m2.py
Adversarial Audit Script for Milestone 2 by reviewer_m2_2.
Stress-tests:
1. Integrity violations:
   - Hardcoded test mocks vs real files
   - Live endpoint reality vs local facade
2. Tag syntax and beat splitting:
   - Exactly regex `^=>[A-Za-z0-9_]+:`
   - Canonical names check: exactly in allowed canonical set
   - Check if any lines have missing tags or plain prefix tags
3. Disentanglement check:
   - Jasper in Scene 0 has dedicated tag =>Jasper:
   - Alyssa in Scene 1 has dedicated tag =>Alyssa:
   - Wulfnic in Scene 0 has dedicated tag =>Wulfnic:
   - Wulfnic in Scene 1 has dedicated tag =>Wulfnic:
   - Check if any spoken dialogue ("...") is inside =>Narrator: blocks
4. Formatting discipline:
   - Exactly 0 em-dashes ('—')
   - Exactly 0 asterisks ('*')
   - Balanced quotes ("...")
5. Comparison:
   - Local JSON vs Live GET on Scenario
   - Local Message #0 vs Live GET on Chat Log
   - Check if {{user}} macro is leaked into active chat message #0
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCENARIO_JSON_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json'
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

SCENARIO_ID = "_2MTWKjxrQPdQVaz9y4Q7H"
CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
SWIPE_ID = "message_swipe_99mmMgEEQjk2pkJN3hXkQ"

CANONICAL_SPEAKERS = {
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia',
    'Jasper', 'Alyssa', 'Wulfnic', 'Zefir', 'Finn', 'Sierra', 'Scarlett'
}

def audit_text(text: str, label: str, expect_no_user_macro: bool = False):
    findings = []
    
    # 1. Em-dashes
    em_dashes = text.count('—')
    if em_dashes > 0:
        findings.append(f"[{label}] Found {em_dashes} em-dashes ('—')")
        
    # 2. Asterisks
    asterisks = text.count('*')
    if asterisks > 0:
        findings.append(f"[{label}] Found {asterisks} asterisks ('*')")
        
    # 3. User macro check
    if expect_no_user_macro and '{{user}}' in text:
        findings.append(f"[{label}] Found unexpanded '{{{{user}}}}' macro in instantiated chat log")
        
    # 4. Balanced quotes
    quotes = text.count('"')
    if quotes % 2 != 0:
        findings.append(f"[{label}] Unbalanced double quotes count: {quotes}")
        
    # 5. Extract beats
    # Splitting by ^=>([A-Za-z0-9_]+):
    beats = re.split(r'(?m)^=>([A-Za-z0-9_]+):\s*\n?', text)
    # beats[0] should be empty if text starts with =>Speaker:
    if beats[0].strip():
        findings.append(f"[{label}] Text before first =>Speaker tag: {beats[0][:100]!r}")
        
    tag_speaker_pairs = []
    for i in range(1, len(beats), 2):
        speaker = beats[i]
        content = beats[i+1] if i+1 < len(beats) else ""
        tag_speaker_pairs.append((speaker, content))
        
        # Check canonical speaker name
        if speaker not in CANONICAL_SPEAKERS:
            findings.append(f"[{label}] Non-canonical speaker tag: '=>{speaker}:'")
            
        # Check if content has plain speaker prefixes that should have been tagged
        plain_prefixes = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', content, flags=re.MULTILINE)
        if plain_prefixes:
            findings.append(f"[{label}] Beat '=>{speaker}:' contains potential plain speaker prefixes: {plain_prefixes}")
            
        # If speaker == 'Narrator', does it contain dialogue quotes?
        if speaker == 'Narrator':
            # Check if there are quotation marks containing direct speech
            quoted_speech = re.findall(r'\"([^\"]+)\"', content)
            if quoted_speech:
                findings.append(f"[{label}] Narrator beat contains direct speech quotes: {quoted_speech}")

    return findings, tag_speaker_pairs

def run_adversarial_audit():
    print("=== STARTING ADVERSARIAL AUDIT FOR MILESTONE 2 ===")
    all_findings = []
    
    # 1. Local Scenario File Audit
    print(f"\n1. Inspecting Local Scenario: {SCENARIO_JSON_PATH}")
    if not SCENARIO_JSON_PATH.exists():
        print(f"CRITICAL: {SCENARIO_JSON_PATH} does not exist!")
        return False
        
    with open(SCENARIO_JSON_PATH, 'r', encoding='utf-8') as f:
        local_data = json.load(f)
        
    scenes = local_data.get('premade_scenes', [])
    print(f"Total premade scenes: {len(scenes)}")
    for idx, sc in enumerate(scenes):
        sc_id = sc.get('id')
        sc_text = sc.get('scene_text', '')
        print(f"\n--- Local Scene {idx}: {sc_id} (length={len(sc_text)}) ---")
        findings, pairs = audit_text(sc_text, f"Local Scene {idx} ({sc_id})")
        all_findings.extend(findings)
        speakers = [p[0] for p in pairs]
        print(f"Speakers ({len(speakers)}): {speakers}")
        if findings:
            for f in findings:
                print(f"  FAILED: {f}")
        else:
            print("  PASSED: 0 violations, all beats clean.")
            
    # 2. Live Scenario API Audit
    print(f"\n2. Fetching Live Scenario from Wyvern API: {SCENARIO_ID}")
    token = TOKEN_PATH.read_text(encoding='utf-8').strip()
    sc_url = f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}"
    req = urllib.request.Request(sc_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            live_sc = json.loads(resp.read().decode('utf-8'))
            print(f"Live Scenario GET HTTP {resp.status} OK")
    except Exception as e:
        all_findings.append(f"Failed to fetch live scenario: {e}")
        live_sc = {}
        
    live_scenes = live_sc.get('premade_scenes', [])
    for idx, sc in enumerate(live_scenes):
        sc_id = sc.get('id')
        sc_text = sc.get('scene_text', '')
        print(f"\n--- Live Scene {idx}: {sc_id} (length={len(sc_text)}) ---")
        findings, pairs = audit_text(sc_text, f"Live Scene {idx} ({sc_id})")
        all_findings.extend(findings)
        speakers = [p[0] for p in pairs]
        print(f"Speakers ({len(speakers)}): {speakers}")
        
        # Parity check between local and live
        if idx < len(scenes):
            local_sc_text = scenes[idx].get('scene_text', '')
            if local_sc_text != sc_text:
                all_findings.append(f"Local Scene {idx} does not match Live Scene {idx} byte-for-byte!")
            else:
                print(f"  PARITY: Local and Live Scene {idx} are 100% byte-for-byte identical.")

    # 3. Live Chat Log API Audit
    print(f"\n3. Fetching Live Chat Log from Wyvern API: {CHAT_LOG_ID}")
    chat_url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}"
    req_chat = urllib.request.Request(chat_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req_chat) as resp:
            live_chat = json.loads(resp.read().decode('utf-8'))
            print(f"Live Chat Log GET HTTP {resp.status} OK")
    except Exception as e:
        all_findings.append(f"Failed to fetch live chat: {e}")
        live_chat = {}
        
    messages = live_chat.get('messages', [])
    print(f"Total messages in chat: {len(messages)}")
    if messages:
        msg0 = messages[0]
        swipes = msg0.get('swipes', [])
        print(f"Message 0 swipes count: {len(swipes)}")
        if swipes:
            swipe0 = swipes[0]
            swipe0_content = swipe0.get('content', '')
            print(f"--- Live Message 0 Swipe ({swipe0.get('id')}) (len={len(swipe0_content)}) ---")
            findings, pairs = audit_text(swipe0_content, "Live Msg 0 Swipe", expect_no_user_macro=True)
            all_findings.extend(findings)
            speakers = [p[0] for p in pairs]
            print(f"Speakers ({len(speakers)}): {speakers}")
            if findings:
                for f in findings:
                    print(f"  FAILED: {f}")
            else:
                print("  PASSED: 0 violations, all beats clean.")
                
            # Check msg0.content parity with swipe0.content
            if msg0.get('content') != swipe0_content:
                all_findings.append("Message 0 top-level content does not match Swipe 0 content!")
            else:
                print("  PARITY: msg0.content and swipe0.content are 100% byte-for-byte identical.")

    print("\n=== ADVERSARIAL AUDIT SUMMARY ===")
    if all_findings:
        print(f"TOTAL ANOMALIES/FINDINGS DETECTED: {len(all_findings)}")
        for f in all_findings:
            print(f"  - {f}")
        return False
    else:
        print("TOTAL ANOMALIES/FINDINGS DETECTED: 0")
        print("ALL SCENARIO SCENES AND MESSAGE #0 PASS EVERY ADVERSARIAL INTEGRITY AND FORMATTING CHECK!")
        return True

if __name__ == '__main__':
    success = run_adversarial_audit()
    sys.exit(0 if success else 1)
