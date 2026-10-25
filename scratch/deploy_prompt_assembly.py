#!/usr/bin/env python3
"""
Deploy Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich) to Wyvern Chat API.
Target: POST https://app.wyvern.chat/api/prompt-assembly
Followed by GET https://app.wyvern.chat/api/prompt-assembly/{id} for verification.
"""

import json
import pathlib
import sys
import urllib.request
import urllib.error

TOKEN_FILE = pathlib.Path("scratch/wyvern_token.txt")
PAYLOAD_FILE = pathlib.Path("FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json")
OUTPUT_RECORD = pathlib.Path("scratch/deployed_prompt_assembly_record.json")
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
    
    print(f"Deploying Prompt Assembly: '{payload.get('name')}'...")
    print(f"Floating Depth: {payload.get('floating_depth_percent')}%, Role: {payload.get('floating_role')}, Blocks: {len(payload.get('blocks', []))}")
    
    # 1. Check existing prompt assemblies on user account to see if already deployed
    list_req = urllib.request.Request(
        f"{API_BASE}/prompt-assembly",
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
            assemblies = list_data.get("assemblies", [])
            for a in assemblies:
                if a.get("name") == payload.get("name"):
                    existing_id = a.get("id") or a.get("_id")
                    print(f"Found existing Prompt Assembly with same name: ID = {existing_id}")
                    break
    except Exception as e:
        print(f"Warning: Failed to query existing prompt assemblies: {e}")
        
    req_body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    
    if existing_id:
        print(f"Updating existing Prompt Assembly '{existing_id}' via PUT...")
        deploy_req = urllib.request.Request(
            f"{API_BASE}/prompt-assembly/{existing_id}",
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
        print("Creating new Prompt Assembly via POST...")
        deploy_req = urllib.request.Request(
            f"{API_BASE}/prompt-assembly",
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
            assembly_id = resp_data.get("id") or resp_data.get("_id") or existing_id
            print(f"Deployment SUCCESS! HTTP {status}, Prompt Assembly ID: {assembly_id}")
    except urllib.error.HTTPError as he:
        print(f"Deployment HTTP Error: {he.code} {he.reason}")
        print(he.read().decode("utf-8"))
        sys.exit(1)
    except Exception as ex:
        print(f"Deployment Exception: {ex}")
        sys.exit(1)
        
    # 2. Verify persistence via GET
    print(f"Verifying persistence via GET {API_BASE}/prompt-assembly/{assembly_id}...")
    verify_req = urllib.request.Request(
        f"{API_BASE}/prompt-assembly/{assembly_id}",
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
        print(f"Verified Name: {v_data.get('name')}")
        print(f"Verified Visibility: {v_data.get('visibility')}")
        print(f"Verified Floating Depth: {v_data.get('floating_depth_percent')}%")
        print(f"Verified Floating Role: {v_data.get('floating_role')}")
        print(f"Verified Blocks Count: {len(v_data.get('blocks', []))}")
        print(f"Verified Lore Header: {v_data.get('lore_template_header')}")
        print(f"Verified Lore Footer: {v_data.get('lore_template_footer')}")
        print(f"Verified Whisper Template: {v_data.get('whisper_template')}")
        
    record = {
        "prompt_assembly_id": assembly_id,
        "name": v_data.get("name"),
        "description": v_data.get("description"),
        "visibility": v_data.get("visibility"),
        "floating_depth_percent": v_data.get("floating_depth_percent"),
        "floating_role": v_data.get("floating_role"),
        "blocks_count": len(v_data.get("blocks", [])),
        "created_at": v_data.get("created_at"),
        "updated_at": v_data.get("updated_at"),
        "creator_id": v_data.get("creator", {}).get("id") or v_data.get("creator", {}).get("uid")
    }
    OUTPUT_RECORD.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Recorded deployment to {OUTPUT_RECORD}")

if __name__ == "__main__":
    main()
