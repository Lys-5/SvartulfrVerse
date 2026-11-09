#!/usr/bin/env python3
"""
CLI Tool for Wyvern Chat Log Forensic Audit, Summary Sanitization, and World Sync.
Part of the 'wyvern-chat-audit-world-sync' skill.
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error

# Resolve repository root
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

try:
    from scripts.sync_from_wyvern_web import get_auth_token
except ImportError:
    def get_auth_token():
        raise RuntimeError("Could not import get_auth_token from scripts.sync_from_wyvern_web.")

def get_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def cmd_fetch(args):
    token = get_auth_token()
    headers = get_headers(token)
    chat_id = args.chat_id
    print(f"Fetching metadata for {chat_id}...")
    
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
    
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(chat_data, f, indent=2, ensure_ascii=False)
        
    print(f"Success! Data written to: {args.output} ({len(sorted_msgs)} messages)")

def cmd_audit(args):
    with open(args.input, 'r', encoding='utf-8') as f:
        chat = json.load(f)
        
    messages = chat.get('messages', [])
    summaries = chat.get('summaries', [])
    
    report = {
        'total_messages': len(messages),
        'total_summaries': len(summaries),
        'insta_love_flags': [],
        'anatomical_violations': [],
        'summary_drift': []
    }
    
    for m in messages:
        idx = m.get('index')
        txt = m.get('content', '')
        if re.search(r'\b(compagno eterno|innamorato perso|vuole essere suo compagno|ha deciso che correrà per lei)\b', txt, re.IGNORECASE):
            report['insta_love_flags'].append({'index': idx, 'snippet': txt[:200]})
        if re.search(r'\b(sierra)\b[^.\n]*?\b(gambe|piedi|scarpe|passi|cammin|walk|feet|legs|shoes)\b', txt, re.IGNORECASE):
            report['anatomical_violations'].append({'index': idx, 'type': 'sierra_locomotion', 'snippet': txt[:200]})
            
    for s_idx, s in enumerate(summaries):
        sum_txt = s.get('summary', '')
        if any(w in sum_txt.lower() for w in ['ha deciso che correrà', 'romantic interest', 'fixation', 'gambe incrociate']):
            report['summary_drift'].append({'summary_index': s_idx, 'snippet': sum_txt[:250]})
            
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        
    print(f"Success! Data written to: {args.output}")

def cmd_sanitize(args):
    token = get_auth_token()
    headers = get_headers(token)
    chat_id = args.chat_id
    
    meta_url = f'https://app.wyvern.chat/api/new/chat-logs/{chat_id}'
    req = urllib.request.Request(meta_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chat = json.loads(resp.read().decode('utf-8'))
        
    summaries = chat.get('summaries', [])
    modified = 0
    for s in summaries:
        txt = s.get('summary', '')
        if not txt:
            continue
        orig = txt
        txt = txt.replace("ha deciso che correrà per lei nella Grande Caccia", "mantiene curiosità ma rigido distacco sentimentale")
        txt = txt.replace("seduta a gambe incrociate", "adagiata sulle sue spire iridescenti")
        txt = txt.replace("ai piedi del letto", "lungo il bordo del letto sulle sue spire")
        if txt != orig:
            s['summary'] = txt
            modified += 1
            
    if modified > 0:
        patch_req = urllib.request.Request(meta_url, data=json.dumps({'summaries': summaries}).encode('utf-8'), headers=headers, method='PUT')
        with urllib.request.urlopen(patch_req) as resp:
            print(f"Sanitized {modified} summaries live on Wyvern for {chat_id}.")
    else:
        print("No contaminated summaries found.")

def main():
    parser = argparse.ArgumentParser(description="Wyvern Chat Audit & Sync CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # fetch
    p_fetch = subparsers.add_parser('fetch')
    p_fetch.add_argument('--chat-id', required=True, help="Wyvern Chat Log ID")
    p_fetch.add_argument('--output', required=True, help="Path to write JSON output")
    
    # audit
    p_audit = subparsers.add_parser('audit')
    p_audit.add_argument('--input', required=True, help="Path to fetched chat JSON")
    p_audit.add_argument('--output', required=True, help="Path to write audit report JSON")
    
    # sanitize-summaries
    p_san = subparsers.add_parser('sanitize-summaries')
    p_san.add_argument('--chat-id', required=True, help="Wyvern Chat Log ID")
    
    args = parser.parse_args()
    if args.command == 'fetch':
        cmd_fetch(args)
    elif args.command == 'audit':
        cmd_audit(args)
    elif args.command == 'sanitize-summaries':
        cmd_sanitize(args)

if __name__ == '__main__':
    main()
