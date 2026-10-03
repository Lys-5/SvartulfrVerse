import os
import sys
import json
import requests

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def upload_image_to_gallery(token, filepath, title, img_type='avatar'):
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
    print(f"  Got upload URL for {filename}: id={image_id}")

    # Step 2: Upload binary to Cloudflare uploadURL
    with open(filepath, 'rb') as f:
        files = {'file': (filename, f, content_type)}
        cf_resp = requests.post(upload_url, files=files)

    if cf_resp.status_code not in (200, 201):
        raise Exception(f"Failed to upload to Cloudflare: {cf_resp.status_code} {cf_resp.text}")

    public_image_url = f"https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/{image_id}/public"
    print(f"  Uploaded to Cloudflare: {public_image_url}")

    # Step 3: Register in World Gallery
    gallery_url = f'{API_BASE}/worlds/{WORLD_ID}/gallery'
    gallery_payload = {
        'title': title,
        'description': '',
        'imageURL': public_image_url,
        'type': img_type,
        'tags': []
    }
    gal_resp = requests.post(gallery_url, headers=headers, json=gallery_payload)
    if gal_resp.status_code not in (200, 201):
        raise Exception(f"Failed to create gallery item: {gal_resp.status_code} {gal_resp.text}")

    gallery_item = gal_resp.json()
    print(f"  Registered in Gallery: id={gallery_item.get('id')}, title={title}")

    return public_image_url, gallery_item

def main():
    token = get_auth_token()
    filepath = 'D:/SvartulfrVerse/asset/jai_av/andrew.webp'
    title = 'andrew'
    print(f"Testing single upload for {title}...")
    img_url, gal_item = upload_image_to_gallery(token, filepath, title)
    print("SUCCESS! Public image URL:", img_url)

if __name__ == '__main__':
    main()
