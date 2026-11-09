#!/usr/bin/env python3
"""
Monitor script for Wyvern test chat log:
https://app.wyvern.chat/sim/chat_log_ftrtAD79eddk9Ue9Jr2WJ (chat_log_ftrtAD79eddk9Ue9Jr2WJ)

Fetches latest turns, detects new messages, audits for drift, and highlights emergent lore.
"""

import os
import sys
import json
import re
import argparse

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.sync_from_wyvern_web import get_auth_token
import urllib.request
import urllib.error

DEFAULT_CHAT_ID = "chat_log_ftrtAD79eddk9Ue9Jr2WJ"
DEFAULT_OUTPUT = os.path.join(REPO_ROOT, "scratch", f"chat_export_{DEFAULT_CHAT_ID}.json")

def fetch_chat(chat_id=DEFAULT_CHAT_ID, output_path=DEFAULT_OUTPUT):
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    
    meta_url = f'https://app.wyvern.chat/api/new/chat-logs/{chat_id}'
    req = urllib.request.Request(meta_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chat_data = json.loads(resp.read().decode('utf-8'))
        
    all_messages = {}
    page = 1
    limit = 100
    while True:
        msg_url = f'https://app.wyvern.chat/api/new/chat-logs/{chat_id}/messages?page={page}&limit={limit}'
        try:
            req = urllib.request.Request(msg_url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"Error fetching page {page}: {e}", file=sys.stderr)
            break
            
        msgs = data.get('messages', [])
        if not msgs:
            break
        for m in msgs:
            idx = m.get('index')
            if idx is not None:
                all_messages[idx] = m
                
        if not data.get('hasMore') or len(msgs) < limit:
            break
        page += 1
        
    sorted_msgs = [all_messages[i] for i in sorted(all_messages.keys())]
    chat_data['messages'] = sorted_msgs
    chat_data['total_messages_retrieved'] = len(sorted_msgs)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chat_data, f, indent=2, ensure_ascii=False)
        
    return chat_data

def analyze_chat(chat_data, previous_count=0):
    msgs = chat_data.get('messages', [])
    total = len(msgs)
    print(f"=== Chat Log Monitor: {chat_data.get('id')} ===")
    print(f"Total turns: {total} (New turns: {max(0, total - previous_count)})")
    
    # Audit checks
    insta_flags = []
    anatomical_violations = []
    
    for m in msgs:
        idx = m.get('index')
        txt = m.get('mes') or m.get('content') or ''
        if re.search(r'\b(compagno eterno|innamorato perso|vuole essere suo compagno|ha deciso che correra per lei)\b', txt, re.IGNORECASE):
            insta_flags.append((idx, txt[:140]))
        if re.search(r'\b(sierra)\b[^.\n]*?\b(gambe|piedi|scarpe|passi|cammin|walk|feet|legs|shoes)\b', txt, re.IGNORECASE):
            anatomical_violations.append((idx, txt[:140]))

    print(f"Audit Status: {len(insta_flags)} insta-love flags, {len(anatomical_violations)} locomotion violations.")
    
    # Key lore markers
    lore_keywords = [
        "St. Brugge", "Revazhael", "cilindr", "cristall", "abissal",
        "dungeon", "Gilda", "Hunter", "Narghaton", "Archer", "Marcus", "Roxy",
        "Grave Mistake", "Theta Iota Theta", "Solarton"
    ]
    
    print("\n--- Emergent Lore Highlights ---")
    detected = {}
    for m in msgs:
        idx = m.get('index')
        txt = m.get('mes') or m.get('content') or ''
        for kw in lore_keywords:
            if re.search(rf'\b{re.escape(kw)}', txt, re.IGNORECASE):
                detected.setdefault(kw, []).append(idx)
                
    for kw, indices in detected.items():
        print(f"• {kw}: mentioned in turns {indices}")

def main():
    parser = argparse.ArgumentParser(description="Monitor Wyvern Test Chat Log")
    parser.add_argument('--chat-id', default=DEFAULT_CHAT_ID, help="Chat ID")
    parser.add_argument('--output', default=DEFAULT_OUTPUT, help="Output path")
    args = parser.parse_args()
    
    prev_count = 0
    if os.path.exists(args.output):
        try:
            with open(args.output, 'r', encoding='utf-8') as f:
                old = json.load(f)
                prev_count = len(old.get('messages', []))
        except Exception:
            pass
            
    chat_data = fetch_chat(args.chat_id, args.output)
    analyze_chat(chat_data, previous_count=prev_count)

if __name__ == "__main__":
    main()
