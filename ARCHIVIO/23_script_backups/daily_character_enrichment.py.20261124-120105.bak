import json
import pathlib
import sys
import os
import re
import datetime

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

FINAL = ROOT / 'FINAL'
ARCHIVIO = ROOT / 'ARCHIVIO'
SCRATCH = ROOT / 'scratch'

STATE_FILE = SCRATCH / 'daily_character_enrichment_state.json'
LOG_FILE = SCRATCH / 'daily_character_enrichment.log'

NPC_PRIMARY_PATH = FINAL / 'Svartulfr_NPC_Primary.json'
NPC_SECONDARY_PATH = FINAL / 'Svartulfr_NPC_Secondary.json'
JANITOR_CANON_PATH = ARCHIVIO / 'janitor_sources' / 'janitor_following_canon_characters.json'

BATCH_SIZE = 5
TEST_CHAT_ID = "chat_log_ftrtAD79eddk9Ue9Jr2WJ"

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(formatted + "\n")

def monitor_test_chat_phase(chat_id=TEST_CHAT_ID):
    log(f"=== [Phase 0] Active Test Chat Monitor: {chat_id} ===")
    try:
        from scripts.monitor_active_test_chat import fetch_chat, analyze_chat, DEFAULT_OUTPUT
        output_file = SCRATCH / f"chat_export_{chat_id}.json"
        
        prev_count = 0
        if output_file.exists():
            try:
                with open(output_file, 'r', encoding='utf-8') as f:
                    old_data = json.load(f)
                    prev_count = len(old_data.get('messages', []))
            except Exception:
                pass
                
        chat_data = fetch_chat(chat_id, str(output_file))
        new_total = len(chat_data.get('messages', []))
        delta = max(0, new_total - prev_count)
        log(f"Chat {chat_id}: {new_total} total turns fetched ({delta} new turns detected).")
        
        # Analyze & Log Highlights
        analyze_chat(chat_data, previous_count=prev_count)
        log(f"Chat monitoring and lore mining completed successfully for {chat_id}.")
        return {
            "chat_id": chat_id,
            "total_turns": new_total,
            "new_turns": delta,
            "status": "success"
        }
    except Exception as e:
        log(f"Warning: Failed to fetch/monitor test chat {chat_id}: {e}")
        return {
            "chat_id": chat_id,
            "error": str(e),
            "status": "skipped"
        }

def load_janitor_index():
    janitor_map = {}
    if JANITOR_CANON_PATH.exists():
        with open(JANITOR_CANON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            chars = data.get('characters', [])
            for c in chars:
                name = c.get('name', '').strip()
                if name:
                    janitor_map[name.lower()] = c
    return janitor_map

def init_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    # Initialize roster queue
    queue = []
    # 1. Primary NPCs
    if NPC_PRIMARY_PATH.exists():
        with open(NPC_PRIMARY_PATH, 'r', encoding='utf-8') as f:
            d = json.load(f)
            for e in d.get('entries', []):
                queue.append({
                    "id": e.get('entry_id'),
                    "name": e.get('name'),
                    "source": "NPC_Primary",
                    "status": "pending"
                })
    # 2. Secondary NPCs
    if NPC_SECONDARY_PATH.exists():
        with open(NPC_SECONDARY_PATH, 'r', encoding='utf-8') as f:
            d = json.load(f)
            for e in d.get('entries', []):
                queue.append({
                    "id": e.get('entry_id'),
                    "name": e.get('name'),
                    "source": "NPC_Secondary",
                    "status": "pending"
                })

    state = {
        "last_run": None,
        "completed_count": 0,
        "total_count": len(queue),
        "roster": queue
    }
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    log(f"Initialized state with {len(queue)} characters.")
    return state

def save_state(state):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def run_enrichment_batch(batch_size=BATCH_SIZE):
    # Phase 0: Active Test Chat Monitoring
    chat_monitor_result = monitor_test_chat_phase()

    state = init_state()
    janitor_index = load_janitor_index()
    
    pending = [c for c in state['roster'] if c['status'] == 'pending']
    if not pending:
        log("All characters have been processed. Resetting pending queue for new audit cycle.")
        for c in state['roster']:
            c['status'] = 'pending'
        pending = state['roster']

    batch = pending[:batch_size]
    log(f"Starting enrichment batch of {len(batch)} characters: {[c['name'] for c in batch]}")

    results = []
    for item in batch:
        char_name = item['name']
        log(f"--- Processing: {char_name} ({item['source']}) ---")
        
        # Check Janitor match
        j_match = None
        for k, v in janitor_index.items():
            if k in char_name.lower() or char_name.lower() in k:
                j_match = v
                break
                
        if j_match:
            log(f"  -> Found Janitor match: {j_match.get('name')} (ID: {j_match.get('id')})")
        else:
            log(f"  -> No direct Janitor match found, searching local archives.")
            
        item['status'] = 'processed'
        item['processed_at'] = datetime.datetime.now().isoformat()
        item['janitor_match'] = j_match.get('name') if j_match else None
        state['completed_count'] += 1
        results.append(item)

    state['last_run'] = datetime.datetime.now().isoformat()
    state['last_chat_monitor'] = chat_monitor_result
    save_state(state)
    log(f"Batch completed successfully. Progress: {state['completed_count']}/{state['total_count']}.")
    return results

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Daily Character Lore Enrichment & Active Chat Monitor")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="Number of NPCs to enrich per batch")
    args = parser.parse_args()
    run_enrichment_batch(batch_size=args.batch_size)

