#!/usr/bin/env python3
"""
Deploy Svartúlfr — Game Master & World Engine to Wyvern Chat API.
Target: POST https://app.wyvern.chat/api/simple-assistant-config
Followed by GET https://app.wyvern.chat/api/simple-assistant-config/{id} for verification.
"""

import json
import pathlib
import sys
import urllib.request
import urllib.error

TOKEN_FILE = pathlib.Path("scratch/wyvern_token.txt")
PAYLOAD_FILE = pathlib.Path("FINAL/assistants/Svartulfr_Game_Master_Assistant.json")
OUTPUT_RECORD = pathlib.Path("scratch/deployed_assistant_record.json")
API_BASE = "https://app.wyvern.chat/api"

def main():
    if not TOKEN_FILE.exists():
        print(f"Error: Token file {TOKEN_FILE} not found.", file=sys.stderr)
        sys.exit(1)
    
    token = TOKEN_FILE.read_text(encoding="utf-8").strip()
    
    if not PAYLOAD_FILE.exists():
        print(f"Error: Payload file {PAYLOAD_FILE} not found.", file=sys.stderr)
        sys.exit(1)
        
    payload = json.loads(PAYLOAD_FILE.read_text(encoding="utf-8"))
    
    print(f"Deploying Assistant: '{payload.get('title')}'...")
    print(f"Kind: {payload.get('kind')}, Visibility: {payload.get('visibility')}, Rating: {payload.get('rating')}")
    
    # 1. Check existing assistants on user account to see if already deployed
    list_req = urllib.request.Request(
        f"{API_BASE}/simple-assistant-config",
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json"
        }
    )
    
    existing_id = None
    try:
        with urllib.request.urlopen(list_req) as res:
            list_data = json.loads(res.read().decode("utf-8"))
            configs = list_data.get("configs", [])
            for c in configs:
                if c.get("title") == payload.get("title"):
                    existing_id = c.get("_id") or c.get("id")
                    print(f"Found existing Assistant with same title: ID = {existing_id}")
                    break
    except Exception as e:
        print(f"Warning: Failed to query existing configs: {e}")
        
    req_body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    
    if existing_id:
        print(f"Updating existing Assistant '{existing_id}' via PUT...")
        deploy_req = urllib.request.Request(
            f"{API_BASE}/simple-assistant-config/{existing_id}",
            data=req_body,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept": "application/json"
            },
            method="PUT"
        )
    else:
        print("Creating new Assistant via POST...")
        deploy_req = urllib.request.Request(
            f"{API_BASE}/simple-assistant-config",
            data=req_body,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept": "application/json"
            },
            method="POST"
        )
        
    try:
        with urllib.request.urlopen(deploy_req) as res:
            status = res.status
            resp_bytes = res.read()
            resp_data = json.loads(resp_bytes.decode("utf-8"))
            assistant_id = resp_data.get("_id") or resp_data.get("id") or existing_id
            print(f"Deployment SUCCESS! HTTP {status}, Assistant ID: {assistant_id}")
    except urllib.error.HTTPError as he:
        print(f"Deployment HTTP Error: {he.code} {he.reason}")
        print(he.read().decode("utf-8"))
        sys.exit(1)
    except Exception as ex:
        print(f"Deployment Exception: {ex}")
        sys.exit(1)
        
    # 2. Verify persistence via GET
    print(f"Verifying persistence via GET {API_BASE}/simple-assistant-config/{assistant_id}...")
    verify_req = urllib.request.Request(
        f"{API_BASE}/simple-assistant-config/{assistant_id}",
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json"
        }
    )
    
    with urllib.request.urlopen(verify_req) as v_res:
        v_status = v_res.status
        v_data = json.loads(v_res.read().decode("utf-8"))
        print(f"Verification SUCCESS! HTTP {v_status}")
        print(f"Verified Title: {v_data.get('title')}")
        print(f"Verified Kind: {v_data.get('kind')}")
        print(f"Verified Visibility: {v_data.get('visibility')}")
        print(f"Verified Rating: {v_data.get('rating')}")
        print(f"Tags: {v_data.get('tags')}")
        
    record = {
        "assistant_id": assistant_id,
        "title": v_data.get("title"),
        "kind": v_data.get("kind"),
        "visibility": v_data.get("visibility"),
        "rating": v_data.get("rating"),
        "created_at": v_data.get("created_at"),
        "updated_at": v_data.get("updated_at"),
        "user_id": v_data.get("user", {}).get("id") or v_data.get("user", {}).get("uid")
    }
    OUTPUT_RECORD.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Recorded deployment to {OUTPUT_RECORD}")

if __name__ == "__main__":
    main()
