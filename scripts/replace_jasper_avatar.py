import os
import sys
import json
import requests

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from remediate_lorebook_npcs import build_compact_put_payload

API_BASE = 'https://app.wyvern.chat/api'
WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
LOREBOOK_ID = '_zwEqgEEzh12X6gHVmMKKC'
CHARACTER_ID = '_t4J9aQNJM36cUKAP4wB4U'
WORLD_CHAR_ID = '_x3VY2kcbaDbKyCqywGeET'
PERSONA_ID = '1792155173728'

IMAGE_PATH = 'asset/characters/main_cast/jasper/jasper.jpg'

def main():
    token = get_auth_token()
    headers_auth = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    headers_json = {**headers_auth, 'Content-Type': 'application/json'}

    print("=== Step 1: Upload Image to Cloudflare ===")
    filename = os.path.basename(IMAGE_PATH)
    filesize = os.path.getsize(IMAGE_PATH)
    
    req_upload_payload = {
        'metadata': {
            'filename': filename,
            'contentType': 'image/jpeg',
            'size': filesize,
            'context': 'gallery',
            'worldId': WORLD_ID
        }
    }
    
    r1 = requests.post(f'{API_BASE}/cloudflare/request-upload-url', headers=headers_json, json=req_upload_payload)
    if r1.status_code != 200:
        raise Exception(f"Failed to request upload URL: {r1.status_code} {r1.text}")
    
    upload_res = r1.json()
    upload_url = upload_res['uploadURL']
    image_id = upload_res['id']
    new_avatar_url = f"https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/{image_id}/public"
    print(f"  Got upload URL. Image ID: {image_id}")
    print(f"  Target Public URL: {new_avatar_url}")

    with open(IMAGE_PATH, 'rb') as f:
        files = {'file': (filename, f, 'image/jpeg')}
        r_cf = requests.post(upload_url, files=files)
    
    if r_cf.status_code not in (200, 201):
        raise Exception(f"Cloudflare upload failed: {r_cf.status_code} {r_cf.text}")
    print("  Binary uploaded successfully to Cloudflare!")

    print("\n=== Step 2: Register in Lorebook Gallery ===")
    lb_gal_payload = {
        'title': 'jasperMain',
        'description': 'Jasper Svartr Douglas Bloodmoon base avatar',
        'imageURL': new_avatar_url,
        'type': 'avatar',
        'tags': ['Avatar', 'character', 'jasper']
    }
    r_lb_gal = requests.post(f'{API_BASE}/gallery/lorebook/{LOREBOOK_ID}', headers=headers_json, json=lb_gal_payload)
    print(f"  Lorebook gallery registration: HTTP {r_lb_gal.status_code}")
    if r_lb_gal.status_code not in (200, 201):
        print(f"  Warning: {r_lb_gal.text}")

    print("\n=== Step 3: Register in World Gallery ===")
    w_gal_payload = {
        'title': 'jasperMain',
        'description': 'Jasper Svartr Douglas Bloodmoon base avatar',
        'imageURL': new_avatar_url,
        'type': 'avatar',
        'tags': ['avatar', 'character', 'jasper']
    }
    r_w_gal = requests.post(f'{API_BASE}/worlds/{WORLD_ID}/gallery', headers=headers_json, json=w_gal_payload)
    print(f"  World gallery registration: HTTP {r_w_gal.status_code}")

    print("\n=== Step 4: Update Stand-alone Character Card ===")
    r_char_get = requests.get(f'{API_BASE}/characters/{CHARACTER_ID}', headers=headers_auth)
    if r_char_get.status_code == 200:
        char_data = r_char_get.json()
        char_data['avatar'] = new_avatar_url
        # Clean read-only or computed fields if necessary
        clean_keys = ['_id', 'created_at', 'updated_at', 'creator', 'status', 'token_count', 'npc_count', 'lorebook_npc_count', 'sprite_count', 'collaborators', 'likes', 'liked_by_me', 'boosted_by_me']
        payload_char = {k: v for k, v in char_data.items() if k not in clean_keys}
        payload_char['avatar'] = new_avatar_url
        
        r_char_put = requests.put(f'{API_BASE}/characters/{CHARACTER_ID}', headers=headers_json, json=payload_char)
        print(f"  Character Card PUT: HTTP {r_char_put.status_code}")
        if r_char_put.status_code != 200:
            print(f"  Error payload response: {r_char_put.text[:200]}")
    else:
        print(f"  Error fetching character card: HTTP {r_char_get.status_code}")

    print("\n=== Step 5: Update World Character ===")
    r_wchar_get = requests.get(f'{API_BASE}/worlds/characters/{WORLD_CHAR_ID}?world_id={WORLD_ID}', headers=headers_auth)
    if r_wchar_get.status_code == 200:
        wchar_data = r_wchar_get.json()
        wchar_data['avatar'] = new_avatar_url
        r_wchar_put = requests.put(f'{API_BASE}/worlds/characters/{WORLD_CHAR_ID}?world_id={WORLD_ID}', headers=headers_json, json=wchar_data)
        print(f"  World Character PUT: HTTP {r_wchar_put.status_code}")
    else:
        print(f"  Error fetching world character: HTTP {r_wchar_get.status_code}")

    print("\n=== Step 6: Update User Persona ===")
    r_p_get = requests.get(f'{API_BASE}/user-personas/{PERSONA_ID}', headers=headers_auth)
    if r_p_get.status_code == 200:
        p_data = r_p_get.json()
        p_data['avatar'] = new_avatar_url
        r_p_put = requests.put(f'{API_BASE}/user-personas/{PERSONA_ID}', headers=headers_json, json=p_data)
        print(f"  User Persona PUT: HTTP {r_p_put.status_code}")
    else:
        print(f"  Error fetching persona: HTTP {r_p_get.status_code}")

    print("\n=== Step 7: Update Lorebook NPC Primary Live ===")
    r_lb_get = requests.get(f'{API_BASE}/lorebooks/{LOREBOOK_ID}', headers=headers_auth)
    if r_lb_get.status_code == 200:
        lb_data = r_lb_get.json()
        entries = lb_data.get('lexicon', lb_data.get('entries', []))
        updated_npc = False
        for e in entries:
            if 'jasper' in e.get('name', '').lower():
                old_av = e.get('avatar')
                e['avatar'] = new_avatar_url
                e['type'] = 'npc'
                e['scan_persona'] = True
                e['whole_words_only'] = True
                e['highlight_keys'] = True
                e['enable_highlighting'] = True
                updated_npc = True
                print(f"  Updated NPC Entry '{e.get('name')}': {old_av} -> {new_avatar_url}")
                break
        
        if updated_npc:
            lb_data['entries'] = entries
            lb_data['lexicon'] = entries
            put_payload = build_compact_put_payload(lb_data)
            r_lb_put = requests.put(
                f'{API_BASE}/lorebooks/{LOREBOOK_ID}',
                headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
                data=put_payload
            )
            print(f"  Lorebook PUT: HTTP {r_lb_put.status_code}")
            if r_lb_put.status_code != 200:
                print(f"  Error updating lorebook: {r_lb_put.text[:200]}")
    else:
        print(f"  Error fetching lorebook: HTTP {r_lb_get.status_code}")

    print("\n=== Step 8: Update Local Repository Files ===")
    local_files = [
        'FINAL/Jasper_Douglas_Bloodmoon_card.json',
        'FINAL/personas/Jasper_Persona.json',
        'FINAL/Svartulfr_NPC_Primary.json',
        'lorebooks/optimized/Svartulfr_NPC_Primary.json',
        'FINAL/Svartulfr_Master_Scenario.json',
        'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json'
    ]

    for fpath in local_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        modified = False
        if isinstance(data, dict):
            # Check direct avatar
            if 'avatar' in data and data['avatar'] != new_avatar_url and ('343ac305-0d85-4a8e-2ea6-e76750020800' in str(data['avatar']) or '440a57b3-c3f3-4bf7-ba5a-64fcd8309700' in str(data['avatar'])):
                data['avatar'] = new_avatar_url
                modified = True
            # Check entries / lexicon
            for e_list in ['entries', 'lexicon']:
                if e_list in data and isinstance(data[e_list], list):
                    for entry in data[e_list]:
                        if isinstance(entry, dict) and 'jasper' in entry.get('name', '').lower():
                            if entry.get('avatar') != new_avatar_url:
                                entry['avatar'] = new_avatar_url
                                entry['type'] = 'npc'
                                entry['scan_persona'] = True
                                entry['whole_words_only'] = True
                                entry['highlight_keys'] = True
                                entry['enable_highlighting'] = True
                                modified = True
                    if 'entries' in data and 'lexicon' in data:
                        data['lexicon'] = data['entries']
            
            # Check characters in scenarios
            if 'characters' in data and isinstance(data['characters'], list):
                for c in data['characters']:
                    if isinstance(c, dict) and 'jasper' in c.get('name', '').lower():
                        if c.get('avatar') != new_avatar_url:
                            c['avatar'] = new_avatar_url
                            modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"  Updated local file: {fpath}")

    print("\nAll steps completed successfully!")
    print(f"New Jasper Avatar URL: {new_avatar_url}")

if __name__ == '__main__':
    main()
