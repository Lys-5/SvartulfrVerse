import os, requests, json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'AuditorBot/1.0',
    'Content-Type': 'application/json'
}

dst_asset = r'asset\placeholder_npc_avatar.jpg'
filename = 'placeholder_npc_avatar.jpg'
size = os.path.getsize(dst_asset)
content_type = 'image/jpeg'

print(f"Requesting Cloudflare upload URL for {filename} (size: {size} bytes)...")
req_url = 'https://app.wyvern.chat/api/cloudflare/request-upload-url'
payload = {
    'metadata': {
        'filename': filename,
        'contentType': content_type,
        'size': size,
        'context': 'avatar'
    }
}

resp = requests.post(req_url, headers=headers, json=payload)
print("Response status:", resp.status_code)
if resp.status_code == 200:
    upload_data = resp.json()
    upload_url = upload_data.get('uploadURL')
    image_id = upload_data.get('id')
    print(f"Got upload URL: id={image_id}")
    
    with open(dst_asset, 'rb') as f:
        files = {'file': (filename, f, content_type)}
        cf_resp = requests.post(upload_url, files=files)
        
    print("Cloudflare upload status:", cf_resp.status_code)
    if cf_resp.status_code in (200, 201):
        public_url = f"https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/{image_id}/public"
        print(f"SUCCESS! Public CDN URL: {public_url}")
        with open('scratch/placeholder_image_url.txt', 'w', encoding='utf-8') as out:
            out.write(public_url)
else:
    print("Error requesting upload URL:", resp.text)
