import os
import sys
import time
import json
import requests

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'
AVATAR_DIR = 'D:/SvartulfrVerse/asset/jai_av'

# Target assignments mapping
# key: file title (lowercase without extension)
# val: dict with:
#   - 'char_id': target character ID to set main avatar (or None)
#   - 'outfit_match': (char_id, outfit_name_or_keyword) to assign avatar to specific outfit
#   - 'lexicon_id': target lexicon ID to set avatar
ENTITY_TARGETS = {
    'andrew': {
        'char_id': '_acGaTVmCXxKDrTa6KNYzd', # Andrew Campbell
    },
    'casey': {
        'char_id': '_nBMDwWAEatHAggKWjNNCh', # Casey Williams
    },
    'chase': {
        'char_id': '_TLxzk97WmgYCA47nkDCVy', # Chase Anderson (fallback if missing)
    },
    'coso': {
        'char_id': '_UczWkLKQ2td6jrJCR66Eb', # Adelin Coso
    },
    'dominic': {
        'char_id': '_6h1dDQpmqTAckYaWRT2er', # Dominic Chen
    },
    'eric': {
        'char_id': '_68EgtxQCgFB8RNKqUbpxB', # Eric
    },
    'fade_2': {
        'outfit_match': ('_mbBqR74dFceBFB4YegpyN', 'Greek Life / Party Night') # Fade Greymoor
    },
    'finnegan_2': {
        'outfit_match': ('_PQHGb4gL2LwDhNDrLFa3A', 'Greek Life / Party Night') # Finnegan Novak
    },
    'jared_beach': {
        'char_id': '_BzKwAkgpPfbVkBzbDaEth', # Jared Thompson (set as main avatar too if empty)
        'outfit_match': ('_BzKwAkgpPfbVkBzbDaEth', 'Beach')
    },
    'kolya': {
        'char_id': '_k2hYW7HaWMzWHw2EpgVVF', # Kolya Varenkov
    },
    'oskar': {
        'char_id': '_RAPLVfmBbzaARYUpWGMga', # Oskar
    },
    'roman': {
        'char_id': '_9prjebmrgUC3zX3Qyew6a', # Roman Blackwood
        'outfit_match': ('_9prjebmrgUC3zX3Qyew6a', 'Campus Daily')
    },
    'roman_2': {
        'outfit_match': ('_9prjebmrgUC3zX3Qyew6a', 'Athletic / Gym')
    },
    'tomas': {
        'char_id': '_pbNb7PrEanM1twU612VNg', # Tomas Matthews (fallback if missing)
    },
    'venera': {
        'lexicon_id': '_xfRUQp8HN4fgzwa32YVer', # Venera Dolce
    },
    'vincent': {
        'char_id': '_U3JX1Xd9Um2ff4fA64wcr', # Vincent Campbell
    },
    'aiden': {
        'lexicon_id': '_MUTN6F1Qf4MpqA7t2gnJW', # Aiden Smith
    }
}

def get_current_gallery(token):
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    url = f'{API_BASE}/worlds/{WORLD_ID}/gallery'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return []

def upload_single_file(token, filepath, title):
    filename = os.path.basename(filepath)
    size = os.path.getsize(filepath)
    content_type = 'image/webp' if filepath.endswith('.webp') else 'image/png'

    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }

    # Step 1: Request upload URL
    req_url = f'{API_BASE}/cloudflare/request-upload-url'
    payload = {
        'metadata': {
            'filename': filename,
            'contentType': content_type,
            'size': size,
            'context': 'gallery',
            'worldId': WORLD_ID
        }
    }
    resp = requests.post(req_url, headers=headers, json=payload)
    if resp.status_code != 200:
        raise Exception(f"Failed to request upload URL: {resp.status_code} {resp.text}")

    upload_data = resp.json()
    upload_url = upload_data.get('uploadURL')
    image_id = upload_data.get('id')

    # Step 2: Upload binary
    with open(filepath, 'rb') as f:
        files = {'file': (filename, f, content_type)}
        cf_resp = requests.post(upload_url, files=files)

    if cf_resp.status_code not in (200, 201):
        raise Exception(f"Failed to upload to Cloudflare: {cf_resp.status_code} {cf_resp.text}")

    public_image_url = f"https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/{image_id}/public"

    # Step 3: Register in Gallery
    gallery_url = f'{API_BASE}/worlds/{WORLD_ID}/gallery'
    gallery_payload = {
        'title': title,
        'description': '',
        'imageURL': public_image_url,
        'type': 'avatar',
        'tags': []
    }
    gal_resp = requests.post(gallery_url, headers=headers, json=gallery_payload)
    if gal_resp.status_code not in (200, 201):
        raise Exception(f"Failed to create gallery item: {gal_resp.status_code} {gal_resp.text}")

    gal_item = gal_resp.json()
    return public_image_url, gal_item

def put_lexicon(token, lid, body):
    url = f'{API_BASE}/worlds/lexicon/{lid}?world_id={WORLD_ID}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    resp = requests.put(url, headers=headers, json=body)
    if resp.status_code in (200, 201):
        return resp.json()
    raise Exception(f"PUT lexicon failed: {resp.status_code} {resp.text}")

def get_lexicon(token, lid):
    url = f'{API_BASE}/worlds/lexicon/{lid}?world_id={WORLD_ID}'
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    raise Exception(f"GET lexicon failed: {resp.status_code} {resp.text}")

def main():
    token = get_auth_token()
    if not token:
        print("ERROR: Could not get token.")
        return

    print("Step 1: Inspecting current World Gallery...")
    gallery_items = get_current_gallery(token)
    print(f"Current items in gallery: {len(gallery_items)}")
    gallery_map = {it.get('title', '').lower(): it.get('imageURL') for it in gallery_items if it.get('title')}

    files = sorted(os.listdir(AVATAR_DIR))
    print(f"\nStep 2: Processing {len(files)} avatar files from {AVATAR_DIR}...")

    uploaded_urls = {}

    for i, fname in enumerate(files, 1):
        title = os.path.splitext(fname)[0].lower()
        fpath = os.path.join(AVATAR_DIR, fname)

        if title in gallery_map and gallery_map[title]:
            print(f"[{i}/{len(files)}] ALREADY IN GALLERY: {fname} -> {gallery_map[title]}")
            uploaded_urls[title] = gallery_map[title]
        else:
            print(f"[{i}/{len(files)}] UPLOADING TO GALLERY: {fname} as '{title}'...")
            try:
                img_url, item = upload_single_file(token, fpath, title)
                print(f"  -> Uploaded successfully: {img_url}")
                uploaded_urls[title] = img_url
                gallery_map[title] = img_url
                time.sleep(0.5)
            except Exception as e:
                print(f"  -> ERROR uploading {fname}: {e}")

    print("\n" + "="*60)
    print("Step 3: Assigning avatars to character cards and lexicon entries...")
    print("="*60)

    # Track updates to characters
    # Dict of char_id -> {'avatar': ..., 'outfit_updates': {outfit_name: url}}
    char_updates = {}
    lexicon_updates = {}

    for title, target in ENTITY_TARGETS.items():
        if title not in uploaded_urls:
            continue
        img_url = uploaded_urls[title]

        # 1. Main Character Avatar
        cid = target.get('char_id')
        if cid:
            if cid not in char_updates:
                char_updates[cid] = {'avatar': None, 'outfits': {}}
            char_updates[cid]['avatar'] = img_url

        # 2. Outfit Avatar
        omatch = target.get('outfit_match')
        if omatch:
            ocid, oname = omatch
            if ocid not in char_updates:
                char_updates[ocid] = {'avatar': None, 'outfits': {}}
            char_updates[ocid]['outfits'][oname] = img_url

        # 3. Lexicon Avatar
        lid = target.get('lexicon_id')
        if lid:
            lexicon_updates[lid] = (title, img_url)

    # Execute Character Updates
    for cid, up in char_updates.items():
        try:
            char = get_char(token, cid)
            dn = char.get('display_name') or char.get('first_name', cid)
            put_body = {}

            # Check main avatar
            if up['avatar']:
                # Update if currently empty or if this is the explicit target
                current_av = char.get('avatar', '')
                if not current_av or cid in ['_acGaTVmCXxKDrTa6KNYzd', '_nBMDwWAEatHAggKWjNNCh', '_UczWkLKQ2td6jrJCR66Eb', '_6h1dDQpmqTAckYaWRT2er', '_68EgtxQCgFB8RNKqUbpxB', '_BzKwAkgpPfbVkBzbDaEth', '_k2hYW7HaWMzWHw2EpgVVF', '_RAPLVfmBbzaARYUpWGMga', '_9prjebmrgUC3zX3Qyew6a', '_U3JX1Xd9Um2ff4fA64wcr']:
                    put_body['avatar'] = up['avatar']
                    print(f"Updating main avatar for {dn} ({cid}) -> {up['avatar']}")

            # Check outfits
            if up['outfits']:
                existing_outfits = char.get('outfits', [])
                modified = False
                for o in existing_outfits:
                    oname = o.get('name')
                    for target_oname, ourl in up['outfits'].items():
                        if target_oname.lower() in oname.lower():
                            o['avatar'] = ourl
                            modified = True
                            print(f"Updating outfit avatar for {dn} [{oname}] -> {ourl}")
                if modified:
                    put_body['outfits'] = existing_outfits

            if put_body:
                put_char(token, cid, put_body)
                time.sleep(0.5)
                # Verify
                vchar = get_char(token, cid)
                print(f"  -> Verified {dn}: avatar={bool(vchar.get('avatar'))}, outfits={len(vchar.get('outfits', []))}")
            else:
                print(f"No changes needed for {dn} ({cid}).")

        except Exception as e:
            print(f"Error updating character {cid}: {e}")

    # Execute Lexicon Updates
    for lid, (title, img_url) in lexicon_updates.items():
        try:
            lex = get_lexicon(token, lid)
            lname = lex.get('name', lid)
            print(f"Updating lexicon entry: {lname} ({lid}) with avatar -> {img_url}")
            put_body = {'image': img_url, 'avatar': img_url}
            put_lexicon(token, lid, put_body)
            time.sleep(0.5)
            vlex = get_lexicon(token, lid)
            print(f"  -> Verified {lname}: image={bool(vlex.get('image') or vlex.get('avatar'))}")
        except Exception as e:
            print(f"Error updating lexicon entry {lid}: {e}")

    print("\nSUCCESS: All files processed, gallery updated, and entities assigned!")

if __name__ == '__main__':
    main()
