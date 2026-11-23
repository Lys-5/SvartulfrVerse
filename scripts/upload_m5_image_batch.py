#!/usr/bin/env python3
"""
scripts/upload_m5_image_batch.py

Milestone 5: Missing Image Asset Creation Batch.
Uploads the 5 local character image assets in assets/characters/secondary_cast/
to Wyvern Cloudflare CDN:
  1. kian.jpg -> Kian (NPC Primary Index 6)
  2. Goran.jpg -> Goran (NPC Primary Index 7)
  3. radek.jpg -> Radek (NPC Primary Index 8)
  4. Eric.jpg -> Eric (NPC Primary Index 12)
  5. Javier.jpg -> Javier Reyes (NPC Primary Index 13)

Registers assets into Lorebook Gallery (_zwEqgEEzh12X6gHVmMKKC) and World Gallery (_YpX47fNraQFw2dD7TdycJ).
Updates FINAL/Svartulfr_NPC_Primary.json and lorebooks/optimized/Svartulfr_NPC_Primary.json (entries == lexicon byte parity).
Deploys updated lorebook to Wyvern live API via anti-413 payload strategy.
Verifies HTTP 200 response and confirms live entries for all 5 characters reflect the new CDN avatars.
"""

import os
import sys
import json
import time
import requests

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT_DIR, 'scripts'))

from wyvern_api_client import (
    get_auth_token,
    get_headers,
    api_request,
    get_lorebook,
    update_lorebook
)

API_BASE = 'https://app.wyvern.chat/api'
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
LOREBOOK_ID = '_zwEqgEEzh12X6gHVmMKKC'

TARGETS = [
    {
        'name': 'Kian',
        'entry_id': 'zlW_PSDs-w17mZqXA8WOY',
        'index': 6,
        'filepath': os.path.join(ROOT_DIR, 'assets', 'characters', 'secondary_cast', 'kian.jpg'),
        'title': 'kianMain',
        'description': 'Kian - Team Ukiyo Scout & Hunter base avatar',
        'tags': ['Avatar', 'character', 'kian', 'ukiyo', 'orc']
    },
    {
        'name': 'Goran',
        'entry_id': 'w-wcHqVIIvpNhN2kJh_NW',
        'index': 7,
        'filepath': os.path.join(ROOT_DIR, 'assets', 'characters', 'secondary_cast', 'Goran.jpg'),
        'title': 'goranMain',
        'description': 'Goran - Team Ukiyo Frontline Berserker base avatar',
        'tags': ['Avatar', 'character', 'goran', 'ukiyo', 'orc']
    },
    {
        'name': 'Radek',
        'entry_id': 'T-11cZKiuLPINjkJwyiQ0',
        'index': 8,
        'filepath': os.path.join(ROOT_DIR, 'assets', 'characters', 'secondary_cast', 'radek.jpg'),
        'title': 'radekMain',
        'description': 'Radek - Team Ukiyo Squad Leader & Heavy Tactician base avatar',
        'tags': ['Avatar', 'character', 'radek', 'ukiyo', 'orc']
    },
    {
        'name': 'Eric',
        'entry_id': '9vQ1lK3sbRRj_I6aIsX4m',
        'index': 12,
        'filepath': os.path.join(ROOT_DIR, 'assets', 'characters', 'secondary_cast', 'Eric.jpg'),
        'title': 'ericMain',
        'description': 'Eric - SUCC Undergrad & Demihuman Fox Musician base avatar',
        'tags': ['Avatar', 'character', 'eric', 'succ', 'fox', 'demihuman']
    },
    {
        'name': 'Javier Reyes',
        'entry_id': '_riI9AvE7q6mY5-8jaVaw',
        'index': 13,
        'filepath': os.path.join(ROOT_DIR, 'assets', 'characters', 'secondary_cast', 'Javier.jpg'),
        'title': 'javierReyesMain',
        'description': 'Javier Reyes - SUCC Film Student & Demihuman Owl base avatar',
        'tags': ['Avatar', 'character', 'javier', 'reyes', 'succ', 'owl', 'demihuman']
    }
]

def upload_image_to_cloudflare(token, filepath):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    headers = get_headers(token)

    req_payload = {
        'metadata': {
            'filename': filename,
            'contentType': 'image/jpeg',
            'size': filesize,
            'context': 'gallery',
            'worldId': WORLD_ID
        }
    }

    req_url = f'{API_BASE}/cloudflare/request-upload-url'
    r1 = api_request('POST', req_url, headers=headers, json_payload=req_payload, token=token)
    if r1.status_code != 200:
        raise Exception(f"Failed to request upload URL for {filename}: HTTP {r1.status_code} {r1.text}")

    upload_data = r1.json()
    upload_url = upload_data['uploadURL']
    image_id = upload_data['id']
    public_url = f"https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/{image_id}/public"

    with open(filepath, 'rb') as f:
        files = {'file': (filename, f, 'image/jpeg')}
        r_cf = requests.post(upload_url, files=files)

    if r_cf.status_code not in (200, 201):
        raise Exception(f"Cloudflare upload failed for {filename}: HTTP {r_cf.status_code} {r_cf.text}")

    return image_id, public_url

def register_in_galleries(token, target, public_url):
    headers = get_headers(token)

    # Lorebook Gallery
    lb_payload = {
        'title': target['title'],
        'description': target['description'],
        'imageURL': public_url,
        'type': 'avatar',
        'tags': target['tags']
    }
    r_lb = api_request('POST', f'{API_BASE}/gallery/lorebook/{LOREBOOK_ID}', headers=headers, json_payload=lb_payload, token=token)
    lb_status = r_lb.status_code
    print(f"    Lorebook Gallery registration: HTTP {lb_status}")

    # World Gallery
    w_payload = {
        'title': target['title'],
        'description': target['description'],
        'imageURL': public_url,
        'type': 'avatar',
        'tags': target['tags']
    }
    r_w = api_request('POST', f'{API_BASE}/worlds/{WORLD_ID}/gallery', headers=headers, json_payload=w_payload, token=token)
    w_status = r_w.status_code
    print(f"    World Gallery registration: HTTP {w_status}")

    return lb_status, w_status

def update_local_lorebooks(uploaded_targets):
    paths = [
        os.path.join(ROOT_DIR, 'FINAL', 'Svartulfr_NPC_Primary.json'),
        os.path.join(ROOT_DIR, 'lorebooks', 'optimized', 'Svartulfr_NPC_Primary.json')
    ]

    for p in paths:
        print(f"\nUpdating {p}...")
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Update entries and lexicon identically
        for target in uploaded_targets:
            idx = target['index']
            name = target['name']
            eid = target['entry_id']
            new_avatar = target['public_url']

            # Check entries
            e = data['entries'][idx]
            assert e.get('name') == name, f"Index {idx} name mismatch: {e.get('name')} != {name}"
            assert e.get('entry_id') == eid, f"Index {idx} entry_id mismatch: {e.get('entry_id')} != {eid}"
            e['avatar'] = new_avatar

            # Check lexicon
            lex_e = data['lexicon'][idx]
            assert lex_e.get('name') == name, f"Lexicon {idx} name mismatch: {lex_e.get('name')} != {name}"
            assert lex_e.get('entry_id') == eid, f"Lexicon {idx} entry_id mismatch: {lex_e.get('entry_id')} != {eid}"
            lex_e['avatar'] = new_avatar

        # Validate entries == lexicon byte identity
        entries_json = json.dumps(data['entries'], sort_keys=True, ensure_ascii=False)
        lexicon_json = json.dumps(data['lexicon'], sort_keys=True, ensure_ascii=False)
        assert entries_json == lexicon_json, f"Parity mismatch in {p} between entries and lexicon!"

        with open(p, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Successfully saved {p} with byte-for-byte entries == lexicon parity.")

def deploy_and_verify_lorebook(token):
    local_path = os.path.join(ROOT_DIR, 'FINAL', 'Svartulfr_NPC_Primary.json')
    with open(local_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\nDeploying updated lorebook to Wyvern API (ID: {LOREBOOK_ID})...")
    status_code, resp = update_lorebook(LOREBOOK_ID, data, token=token)
    print(f"  PUT response: HTTP {status_code}")
    if status_code != 200:
        raise Exception(f"Failed to update lorebook: HTTP {status_code} {resp}")

    print("\nVerifying live lorebook entries...")
    get_status, live_data = get_lorebook(LOREBOOK_ID, token=token)
    if get_status != 200:
        raise Exception(f"Failed to GET live lorebook: HTTP {get_status} {live_data}")

    live_lexicon = live_data.get('lexicon', [])
    print(f"  Live lexicon entry count: {len(live_lexicon)}")

    for t in TARGETS:
        idx = t['index']
        name = t['name']
        expected_url = t['public_url']
        entry = live_lexicon[idx]
        assert entry.get('name') == name, f"Live name mismatch: {entry.get('name')} != {name}"
        live_avatar = entry.get('avatar')
        print(f"  [{name}] Live Avatar: {live_avatar}")
        assert live_avatar == expected_url, f"Live avatar mismatch for {name}: {live_avatar} != {expected_url}"

    print("\nALL 5 LIVE ENTRIES VERIFIED WITH NEW AVATARS!")

def main():
    print("=== MILESTONE 5: Missing Image Asset Upload & Live Deployment ===")
    token = get_auth_token()
    print(f"Authenticated with token (length: {len(token)})")

    # Step 1: Upload 5 images
    print("\n--- Step 1: Uploading Images to Cloudflare CDN ---")
    for t in TARGETS:
        filepath = t['filepath']
        name = t['name']
        print(f"\nUploading {name} from {filepath}...")
        assert os.path.exists(filepath), f"File not found: {filepath}"
        img_id, public_url = upload_image_to_cloudflare(token, filepath)
        t['image_id'] = img_id
        t['public_url'] = public_url
        print(f"  Uploaded {name}: ID={img_id}")
        print(f"  CDN URL: {public_url}")

        print(f"  Registering {name} in galleries...")
        register_in_galleries(token, t, public_url)

    # Save summary of uploaded CDN URLs
    scratch_out = os.path.join(ROOT_DIR, 'scratch', 'm5_uploaded_avatars.json')
    with open(scratch_out, 'w', encoding='utf-8') as f:
        json.dump(TARGETS, f, indent=2)
    print(f"\nUploaded metadata saved to {scratch_out}")

    # Step 2: Update local lorebook files
    print("\n--- Step 2: Updating Local Lorebook Files ---")
    update_local_lorebooks(TARGETS)

    # Step 3: Deploy to live lorebook and verify
    print("\n--- Step 3: Deploying Lorebook to Wyvern Web API ---")
    deploy_and_verify_lorebook(token)

    print("\n=== MILESTONE 5 SCRIPT COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    main()
