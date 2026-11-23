import os
import sys
import time
import requests
import json

sys.path.append('.')
from scripts.wyvern_api_client import get_auth_token, get_headers

CHATS_TO_RECONCILE = [
    'chat_log_ftrtAD79eddk9Ue9Jr2WJ',
    'chat_log_6a2nQtKMKpHjn7xG4Abxa',
    'chat_log_VamEmDLQa1h8rWeQLeX9N',
    'chat_log_TMAa1k3AWLLFd476R2jrp'
]

def reconcile_live_chats():
    token = get_auth_token()
    headers = get_headers(token)

    total_patched = 0
    total_scanned = 0

    for chat_id in CHATS_TO_RECONCILE:
        print(f"\n==========================================")
        print(f"Reconciling Live Chat: {chat_id}")
        print(f"==========================================")
        
        page = 1
        all_messages = []
        while True:
            url = f"https://app.wyvern.chat/api/new/chat-logs/{chat_id}/messages?page={page}&limit=100"
            res = requests.get(url, headers=headers)
            if res.status_code != 200:
                print(f"Failed to fetch page {page}: {res.status_code}")
                break
            data = res.json()
            msgs = data.get('messages', [])
            if not msgs:
                break
            all_messages.extend(msgs)
            if not data.get('hasMore') or len(msgs) < 100:
                break
            page += 1

        print(f"Retrieved {len(all_messages)} messages for {chat_id}.")
        total_scanned += len(all_messages)

        chat_patched = 0
        for m in all_messages:
            mid = m.get('id')
            swipes = m.get('swipes', [])
            s_idx = m.get('current_swipe_index', 0)
            
            # Check all swipes in the message
            for idx, s in enumerate(swipes):
                sid = s.get('id')
                content = s.get('content', '')
                if not content:
                    continue

                needs_patch = False
                new_content = content

                if 'Sunday, August 26' in new_content:
                    new_content = new_content.replace('Sunday, August 26', 'Monday, August 26')
                    needs_patch = True

                if 'Monday, August 27' in new_content:
                    new_content = new_content.replace('Monday, August 27', 'Tuesday, August 27')
                    needs_patch = True

                if '**, August 26' in new_content:
                    new_content = new_content.replace('**, August 26', '**Monday, August 26')
                    needs_patch = True

                if '**, August 27' in new_content:
                    new_content = new_content.replace('**, August 27', '**Tuesday, August 27')
                    needs_patch = True

                if needs_patch:
                    put_url = f"https://app.wyvern.chat/api/new/chat-logs/swipe/{sid}"
                    success = False
                    for attempt in range(3):
                        put_res = requests.put(put_url, json={'content': new_content}, headers=headers)
                        if put_res.status_code == 200:
                            success = True
                            chat_patched += 1
                            total_patched += 1
                            print(f"  [PATCHED] Msg #{m.get('index')} (swipe {idx}/{len(swipes)} - {sid})")
                            break
                        elif put_res.status_code == 401:
                            token = get_auth_token()
                            headers = get_headers(token)
                            time.sleep(1)
                        else:
                            time.sleep(0.5)

                    if not success:
                        print(f"  [FAIL] Could not patch swipe {sid} after 3 attempts.")
                    time.sleep(0.05) # Gentle pacing

        print(f"Completed {chat_id}: patched {chat_patched} swipes.")

    print(f"\n==========================================")
    print(f"Total live messages scanned: {total_scanned}")
    print(f"Total live swipes patched: {total_patched}")
    print(f"==========================================")
    return total_patched

if __name__ == '__main__':
    reconcile_live_chats()
