import os
import sys
import json
import requests

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char
from test_upload_single_avatar import upload_image_to_gallery

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def main():
    token = get_auth_token()
    
    char_id = '_rAcN9GXD1Le4WxY28e49W'  # Malachia
    filepath = r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\malachia_polaroid_final.png'
    title = 'Malachia Polaroid Avatar'
    
    print(f"Uploading {filepath}...")
    img_url, gal_item = upload_image_to_gallery(token, filepath, title)
    print(f"Uploaded successfully. Image URL: {img_url}")
    
    print("Fetching Malachia's current data...")
    char_data = get_char(token, WORLD_ID, char_id)
    print(f"Current avatar: {char_data.get('avatar')}")
    
    # Update the avatar
    print("Updating avatar...")
    put_char(token, WORLD_ID, char_id, {'avatar': img_url})
    
    # Verify
    char_data_updated = get_char(token, WORLD_ID, char_id)
    print(f"Updated avatar: {char_data_updated.get('avatar')}")
    print("Done!")

if __name__ == '__main__':
    main()
