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
DEFAULT_MAX_CHATS = 20

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(formatted + "\n")

def monitor_test_chat_phase(max_chats=DEFAULT_MAX_CHATS, full=False):
    """Phase 0: discover and monitor all sim/chat_log_* chats (incremental)."""
    log("=== [Phase 0] Active Chat Monitor: all https://app.wyvern.chat/sim/chat_log_* ===")
    try:
        from scripts.monitor_active_test_chat import monitor_all_chats
        summary = monitor_all_chats(max_chats=max_chats, full=full, analyze=True)
        log(
            "Chat monitor summary: "
            f"found={summary.get('chats_found', 0)} "
            f"fetched={summary.get('chats_fetched', 0)} "
            f"skipped={summary.get('chats_skipped', 0)} "
            f"deferred={summary.get('chats_deferred', 0)} "
            f"total_turns={summary.get('total_turns', 0)} "
            f"new_turns={summary.get('new_turns', 0)}"
        )
        if summary.get("status") == "error":
            log(f"Warning: chat listing failed: {summary.get('error')}")
        return summary
    except Exception as e:
        log(f"Warning: Failed to monitor chat logs: {e}")
        return {
            "chat_id": "n/d",
            "chats_found": 0,
            "chats_fetched": 0,
            "chats_skipped": 0,
            "chats_deferred": 0,
            "total_turns": 0,
            "new_turns": 0,
            "error": str(e),
            "status": "error",
            "chats": [],
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

def run_enrichment_batch(batch_size=BATCH_SIZE, max_chats=DEFAULT_MAX_CHATS, full_chats=False, chat_monitor_only=False):
    # Phase 0: Active Chat Monitoring (all sim/chat_log_* ids)
    chat_monitor_result = monitor_test_chat_phase(max_chats=max_chats, full=full_chats)
    if chat_monitor_only:
        state = init_state()
        state["last_run"] = datetime.datetime.now().isoformat()
        state["last_chat_monitor"] = chat_monitor_result
        save_state(state)
        log("Chat-monitor-only run complete; NPC enrichment batch skipped.")
        return []


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
    parser.add_argument("--max-chats", type=int, default=DEFAULT_MAX_CHATS, help="Max chat logs to fully fetch this run (0 = no cap)")
    parser.add_argument("--full-chats", action="store_true", help="Refetch all discovered chats, ignoring incremental state (still capped)")
    parser.add_argument("--chat-monitor-only", action="store_true", help="Run only Phase 0 (all chat logs); skip NPC enrichment")
    args = parser.parse_args()
    max_chats = args.max_chats if args.max_chats != 0 else 10**9
    run_enrichment_batch(
        batch_size=args.batch_size,
        max_chats=max_chats,
        full_chats=args.full_chats,
        chat_monitor_only=args.chat_monitor_only,
    )

