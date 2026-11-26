#!/usr/bin/env python3
"""
Monitor Wyvern simulation chat logs at
https://app.wyvern.chat/sim/chat_log_<id>

Discovers all of the current user's chat_log_* ids via:
  GET /api/new/chat-logs?limit=&page=
  GET /api/new/chat-logs/sidebar-recents?page=&limit=&kind=...
then fetches each log's metadata and messages. 404/deleted chats are skipped
with a warning. Incremental mode (default) only fully fetches chats that are
new or updated since the last run, with a cap, to avoid hammering the API.

Does not hardcode or print authentication secrets.
"""

import os
import sys
import json
import re
import argparse
import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.wyvern_api_client import api_request, list_chat_logs, CHAT_LOGS_API

SCRATCH_DIR = os.path.join(REPO_ROOT, "scratch")
DEFAULT_MAX_CHATS = 20
MONITOR_STATE_PATH = os.path.join(SCRATCH_DIR, "chat_monitor_state.json")


class ChatLogNotFound(Exception):
    """Raised when a chat log returns HTTP 404 (missing or deleted)."""


def _output_path_for(chat_id):
    return os.path.join(SCRATCH_DIR, f"chat_export_{chat_id}.json")


def fetch_chat(chat_id, output_path=None):
    """Fetch one chat log (metadata + all message pages) and write JSON to disk."""
    if output_path is None:
        output_path = _output_path_for(chat_id)

    meta_url = f"{CHAT_LOGS_API}/{chat_id}"
    resp = api_request("GET", meta_url, timeout=30)
    if resp.status_code == 404:
        raise ChatLogNotFound(f"HTTP 404: chat log not found or deleted: {chat_id}")
    if resp.status_code != 200:
        body = ""
        try:
            body = (resp.text or "")[:180]
        except Exception:
            body = ""
        raise RuntimeError(f"HTTP {resp.status_code} fetching metadata for {chat_id}: {body}")

    chat_data = resp.json()

    all_messages = {}
    page = 1
    limit = 100
    while True:
        msg_url = f"{CHAT_LOGS_API}/{chat_id}/messages?page={page}&limit={limit}"
        try:
            mresp = api_request("GET", msg_url, timeout=45)
            if mresp.status_code == 404:
                raise ChatLogNotFound(f"HTTP 404: messages not found for {chat_id}")
            if mresp.status_code != 200:
                print(f"Warning: error fetching messages page {page} for {chat_id}: HTTP {mresp.status_code}", file=sys.stderr)
                break
            data = mresp.json()
        except ChatLogNotFound:
            raise
        except Exception as e:
            print(f"Warning: error fetching messages page {page} for {chat_id}: {e}", file=sys.stderr)
            break

        msgs = data.get("messages", []) if isinstance(data, dict) else []
        if not msgs:
            break
        for m in msgs:
            idx = m.get("index")
            if idx is not None:
                all_messages[idx] = m

        has_more = bool(data.get("hasMore")) if isinstance(data, dict) else False
        if not has_more or len(msgs) < limit:
            break
        page += 1

    sorted_msgs = [all_messages[i] for i in sorted(all_messages.keys())]
    chat_data["messages"] = sorted_msgs
    chat_data["total_messages_retrieved"] = len(sorted_msgs)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chat_data, f, indent=2, ensure_ascii=False)

    return chat_data


def analyze_chat(chat_data, previous_count=0):
    msgs = chat_data.get("messages", [])
    total = len(msgs)
    print(f"=== Chat Log Monitor: {chat_data.get('id')} ===")
    print(f"Total turns: {total} (New turns: {max(0, total - previous_count)})")

    insta_flags = []
    anatomical_violations = []

    for m in msgs:
        idx = m.get("index")
        txt = m.get("mes") or m.get("content") or ""
        if re.search(r"\b(compagno eterno|innamorato perso|vuole essere suo compagno|ha deciso che correra per lei)\b", txt, re.IGNORECASE):
            insta_flags.append((idx, txt[:140]))
        if re.search(r"\b(sierra)\b[^.\n]*?\b(gambe|piedi|scarpe|passi|cammin|walk|feet|legs|shoes)\b", txt, re.IGNORECASE):
            anatomical_violations.append((idx, txt[:140]))

    print(f"Audit Status: {len(insta_flags)} insta-love flags, {len(anatomical_violations)} locomotion violations.")

    lore_keywords = [
        "St. Brugge", "Revazhael", "cilindr", "cristall", "abissal",
        "dungeon", "Gilda", "Hunter", "Narghaton", "Archer", "Marcus", "Roxy",
        "Grave Mistake", "Theta Iota Theta", "Solarton",
    ]

    print("\n--- Emergent Lore Highlights ---")
    detected = {}
    for m in msgs:
        idx = m.get("index")
        txt = m.get("mes") or m.get("content") or ""
        for kw in lore_keywords:
            if re.search(rf"\b{re.escape(kw)}", txt, re.IGNORECASE):
                detected.setdefault(kw, []).append(idx)

    for kw, indices in detected.items():
        print(f"• {kw}: mentioned in turns {indices}")


def _load_monitor_state(path=MONITOR_STATE_PATH):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                data.setdefault("chats", {})
                return data
        except Exception:
            pass
    return {"last_run": None, "chats": {}}


def _save_monitor_state(state, path=MONITOR_STATE_PATH):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def _previous_turn_count(chat_id):
    path = _output_path_for(chat_id)
    if not os.path.exists(path):
        return 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            old = json.load(f)
        return len(old.get("messages", []))
    except Exception:
        return 0


def _needs_fetch(item, state_entry, full=False):
    if full or not state_entry:
        return True
    listed_updated = item.get("_updated_at")
    last_fetched = state_entry.get("last_fetched_at")
    last_listed = state_entry.get("updated_at")
    if listed_updated and last_fetched:
        return str(listed_updated) > str(last_fetched) or (
            last_listed is not None and str(listed_updated) > str(last_listed)
        )
    # No reliable timestamp: re-fetch only if never fetched.
    return not last_fetched


def select_chats_to_fetch(listed_items, state, max_chats=DEFAULT_MAX_CHATS, full=False):
    chats_state = state.get("chats", {})
    to_fetch = []
    deferred = []
    for item in listed_items:
        cid = item.get("id")
        if not cid:
            continue
        entry = chats_state.get(cid, {})
        if _needs_fetch(item, entry, full=full):
            to_fetch.append(item)
        else:
            deferred.append(item)

    def sort_key(item):
        cid = item.get("id")
        entry = chats_state.get(cid, {})
        never = 0 if entry.get("last_fetched_at") else 1
        updated = str(item.get("_updated_at") or "")
        return (-never, updated)

    to_fetch.sort(key=sort_key, reverse=True)
    overflow = []
    if max_chats is not None and max_chats >= 0 and len(to_fetch) > max_chats:
        overflow = to_fetch[max_chats:]
        to_fetch = to_fetch[:max_chats]
    return to_fetch, deferred, overflow


def monitor_all_chats(max_chats=DEFAULT_MAX_CHATS, full=False, analyze=True):
    """Discover, incrementally fetch, and audit all accessible chat_log_* chats."""
    now = datetime.datetime.now().isoformat()
    state = _load_monitor_state()

    status, listed = list_chat_logs()
    if status != 200 and not listed:
        summary = {
            "status": "error",
            "chats_found": 0,
            "chats_fetched": 0,
            "chats_skipped": 0,
            "chats_deferred": 0,
            "total_turns": 0,
            "new_turns": 0,
            "chat_id": "n/d",
            "error": f"HTTP {status} listing chat logs",
            "chats": [],
        }
        print(f"Warning: failed to list chat logs (HTTP {status}).", file=sys.stderr)
        return summary

    # Dedupe by id (list_chat_logs already does this, keep as a safety net).
    by_id = {}
    for item in listed:
        cid = item.get("id")
        if cid and cid.startswith("chat_log_") and cid not in by_id:
            by_id[cid] = item
    listed_items = list(by_id.values())
    print(f"Discovered {len(listed_items)} unique chat_log ids.")

    to_fetch, unchanged, overflow = select_chats_to_fetch(
        listed_items, state, max_chats=max_chats, full=full
    )
    print(
        f"Selected {len(to_fetch)} chats to fetch "
        f"({len(unchanged)} unchanged since last run, {len(overflow)} deferred by cap {max_chats})."
    )

    chat_results = []
    fetched = 0
    skipped = 0
    total_turns = 0
    new_turns = 0

    # Carry forward turn counts for chats not fetched this run.
    for item in unchanged + overflow:
        cid = item["id"]
        entry = state.get("chats", {}).get(cid, {})
        turns = entry.get("total_turns", 0) or 0
        total_turns += turns
        chat_results.append({
            "chat_id": cid,
            "total_turns": turns,
            "new_turns": 0,
            "status": "deferred" if item in overflow else "unchanged",
        })

    for item in to_fetch:
        cid = item["id"]
        prev = _previous_turn_count(cid)
        try:
            chat_data = fetch_chat(cid, _output_path_for(cid))
            msgs = chat_data.get("messages", [])
            count = len(msgs)
            delta = max(0, count - prev)
            total_turns += count
            new_turns += delta
            fetched += 1
            if analyze:
                analyze_chat(chat_data, previous_count=prev)
            else:
                print(f"Chat {cid}: {count} total turns fetched ({delta} new).")
            state.setdefault("chats", {})[cid] = {
                "updated_at": item.get("_updated_at"),
                "last_fetched_at": now,
                "total_turns": count,
                "name": item.get("name") or chat_data.get("name"),
            }
            chat_results.append({
                "chat_id": cid,
                "total_turns": count,
                "new_turns": delta,
                "status": "success",
            })
        except ChatLogNotFound as e:
            skipped += 1
            print(f"Warning: skipping {cid}: {e}", file=sys.stderr)
            state.setdefault("chats", {})[cid] = {
                **state.get("chats", {}).get(cid, {}),
                "updated_at": item.get("_updated_at"),
                "last_error": "404",
                "last_skipped_at": now,
            }
            chat_results.append({
                "chat_id": cid,
                "total_turns": 0,
                "new_turns": 0,
                "status": "skipped",
                "error": "HTTP 404",
            })
        except Exception as e:
            skipped += 1
            print(f"Warning: failed to fetch/monitor {cid}: {e}", file=sys.stderr)
            chat_results.append({
                "chat_id": cid,
                "total_turns": prev,
                "new_turns": 0,
                "status": "skipped",
                "error": str(e),
            })

    state["last_run"] = now
    _save_monitor_state(state)

    overall = "success"
    if skipped and fetched:
        overall = "partial"
    elif skipped and not fetched:
        overall = "partial" if listed_items else "error"
    elif not listed_items:
        overall = "success"

    label = f"{fetched}/{len(listed_items)} chat_log (saltate {skipped}"
    if overflow:
        label += f", rinviate {len(overflow)}"
    label += ")"

    summary = {
        "status": overall,
        "chats_found": len(listed_items),
        "chats_fetched": fetched,
        "chats_skipped": skipped,
        "chats_deferred": len(unchanged) + len(overflow),
        "total_turns": total_turns,
        "new_turns": new_turns,
        "chat_id": label,
        "chats": chat_results,
    }
    print(
        f"Chat monitor summary: found={summary['chats_found']} "
        f"fetched={summary['chats_fetched']} skipped={summary['chats_skipped']} "
        f"deferred={summary['chats_deferred']} total_turns={summary['total_turns']} "
        f"new_turns={summary['new_turns']}"
    )
    return summary


def main():
    parser = argparse.ArgumentParser(description="Monitor one or all Wyvern simulation chat logs")
    parser.add_argument("--chat-id", default=None, help="Single chat_log id (legacy one-chat mode)")
    parser.add_argument("--output", default=None, help="Output path (single-chat mode only)")
    parser.add_argument("--all", dest="all_chats", action="store_true", help="Discover and monitor all chat_log ids")
    parser.add_argument("--max-chats", type=int, default=DEFAULT_MAX_CHATS, help="Max chats to fully fetch this run (incremental cap)")
    parser.add_argument("--full", action="store_true", help="Ignore incremental state and fetch all discovered chats (still capped unless --max-chats 0)")
    parser.add_argument("--no-analyze", action="store_true", help="Skip lore/audit highlights (still fetch logs)")
    args = parser.parse_args()

    if args.all_chats or args.chat_id is None:
        max_chats = args.max_chats
        if max_chats == 0:
            max_chats = 10**9
        monitor_all_chats(max_chats=max_chats, full=args.full, analyze=not args.no_analyze)
        return

    output = args.output or _output_path_for(args.chat_id)
    prev_count = 0
    if os.path.exists(output):
        try:
            with open(output, "r", encoding="utf-8") as f:
                old = json.load(f)
                prev_count = len(old.get("messages", []))
        except Exception:
            pass
    chat_data = fetch_chat(args.chat_id, output)
    analyze_chat(chat_data, previous_count=prev_count)


if __name__ == "__main__":
    main()