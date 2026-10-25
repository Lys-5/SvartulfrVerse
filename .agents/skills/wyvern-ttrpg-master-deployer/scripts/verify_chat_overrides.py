#!/usr/bin/env python3
"""
Wyvern TTRPG Master & Chat Deployment Verifier
CLI tool to inspect, verify, and audit Assistants, Prompt Assemblies, and Chat Overrides.
"""

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[4]
TOKEN_FILE = ROOT / "scratch" / "wyvern_token.txt"
REFRESH_FILE = ROOT / "scratch" / "refresh_token.txt"
FIREBASE_API_KEY = "AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw"
API_BASE = "https://app.wyvern.chat/api"

def get_token() -> str:
    if not TOKEN_FILE.exists():
        refresh_token()
    token = TOKEN_FILE.read_text(encoding="utf-8").strip()
    return token

def refresh_token() -> str:
    if not REFRESH_FILE.exists():
        sys.stderr.write(f"Error: Refresh token file not found at {REFRESH_FILE}\n")
        sys.exit(1)
    rt = REFRESH_FILE.read_text(encoding="utf-8").strip()
    url = f"https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}"
    data = urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": rt}).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read().decode())
            token = body["id_token"]
            TOKEN_FILE.write_text(token, encoding="utf-8")
            return token
    except Exception as e:
        sys.stderr.write(f"Failed to refresh Firebase token: {e}\n")
        sys.exit(1)

def api_request(endpoint: str, method: str = "GET", data: dict = None, retry: bool = True) -> dict:
    token = get_token()
    url = f"{API_BASE}/{endpoint.lstrip('/')}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    payload = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if (e.code in (401, 500)) and retry:
            # Check for token expiration in HTTP 500
            refresh_token()
            return api_request(endpoint, method, data, retry=False)
        error_body = e.read().decode("utf-8", errors="replace")
        sys.stderr.write(f"HTTP {e.code} Error for {url}: {error_body}\n")
        raise
    except Exception as e:
        sys.stderr.write(f"Request Error for {url}: {e}\n")
        raise

def cmd_refresh(args):
    token = refresh_token()
    print(f"Success! Bearer token refreshed (length: {len(token)}).")

def cmd_verify_assistant(args):
    data = api_request(f"simple-assistant-config/{args.id}")
    report = {
        "id": data.get("id"),
        "title": data.get("title"),
        "kind": data.get("kind"),
        "visibility": data.get("visibility"),
        "rating": data.get("rating"),
        "tags": data.get("tags", []),
        "has_system_prompt": bool(data.get("system_prompt")),
        "has_final_instructions": bool(data.get("final_instructions")),
        "is_game_master": data.get("kind") == "narrator"
    }
    out_path = pathlib.Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Success! Assistant verification written to: {out_path}")

def cmd_verify_assembly(args):
    data = api_request(f"prompt-assembly/{args.id}")
    blocks = data.get("blocks", [])
    report = {
        "id": data.get("id"),
        "name": data.get("name"),
        "block_count": len(blocks),
        "block_labels": [b.get("label") for b in blocks],
        "has_main_template": bool(data.get("main_prompt_template")),
        "has_lore_template": bool(data.get("lore_template")),
        "has_floating_prompt": bool(data.get("floating_prompt_template")),
        "floating_role": data.get("floating_role"),
        "floating_depth_percent": data.get("floating_depth_percent"),
        "all_blocks_user_role": all(b.get("role") == "user" for b in blocks)
    }
    out_path = pathlib.Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Success! Prompt assembly verification written to: {out_path}")

def cmd_verify_chat(args):
    data = api_request(f"new/chat-logs/{args.id}")
    report = {
        "id": data.get("id"),
        "name": data.get("name"),
        "narrator_profile_id": data.get("narrator_profile_id"),
        "narrator_enabled": data.get("narrator_enabled"),
        "has_character_scenario": bool(data.get("character_scenario_snapshot")),
        "scenario_override": bool(data.get("scenario_override"))
    }
    out_path = pathlib.Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Success! Chat verification written to: {out_path}")

def cmd_full_audit(args):
    ast = api_request(f"simple-assistant-config/{args.assistant_id}")
    pa = api_request(f"prompt-assembly/{args.assembly_id}")
    chat = api_request(f"new/chat-logs/{args.chat_id}")

    audit = {
        "assistant": {
            "id": ast.get("id"),
            "title": ast.get("title"),
            "kind": ast.get("kind"),
            "valid_narrator": ast.get("kind") == "narrator"
        },
        "prompt_assembly": {
            "id": pa.get("id"),
            "name": pa.get("name"),
            "blocks": len(pa.get("blocks", [])),
            "floating_role": pa.get("floating_role"),
            "valid_roles": pa.get("floating_role") == "user"
        },
        "chat_log": {
            "id": chat.get("id"),
            "name": chat.get("name"),
            "narrator_profile_id": chat.get("narrator_profile_id")
        },
        "summary": {
            "all_entities_reachable": True,
            "assistant_verified": bool(ast.get("id")),
            "assembly_verified": bool(pa.get("id")),
            "chat_reachable": bool(chat.get("id"))
        }
    }
    out_path = pathlib.Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(audit, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Success! Full audit written to: {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Wyvern TTRPG Master Deployment & Verification CLI")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # refresh-token
    p_ref = subparsers.add_parser("refresh-token", help="Refresh Firebase bearer token")
    p_ref.set_defaults(func=cmd_refresh)

    # verify-assistant
    p_ast = subparsers.add_parser("verify-assistant", help="Verify Simple Assistant / Game Master")
    p_ast.add_argument("--id", required=True, help="Assistant ID (simple_assistant_...)")
    p_ast.add_argument("--output", required=True, help="Output JSON path")
    p_ast.set_defaults(func=cmd_verify_assistant)

    # verify-assembly
    p_pa = subparsers.add_parser("verify-assembly", help="Verify Custom Prompt Assembly")
    p_pa.add_argument("--id", required=True, help="Prompt Assembly ID (pha_...)")
    p_pa.add_argument("--output", required=True, help="Output JSON path")
    p_pa.set_defaults(func=cmd_verify_assembly)

    # verify-chat
    p_chat = subparsers.add_parser("verify-chat", help="Verify Chat Log status")
    p_chat.add_argument("--id", required=True, help="Chat Log ID (chat_log_...)")
    p_chat.add_argument("--output", required=True, help="Output JSON path")
    p_chat.set_defaults(func=cmd_verify_chat)

    # full-audit
    p_aud = subparsers.add_parser("full-audit", help="Run full audit across all 3 entities")
    p_aud.add_argument("--assistant-id", required=True, help="Assistant ID")
    p_aud.add_argument("--assembly-id", required=True, help="Prompt Assembly ID")
    p_aud.add_argument("--chat-id", required=True, help="Chat Log ID")
    p_aud.add_argument("--output", required=True, help="Output JSON path")
    p_aud.set_defaults(func=cmd_full_audit)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
