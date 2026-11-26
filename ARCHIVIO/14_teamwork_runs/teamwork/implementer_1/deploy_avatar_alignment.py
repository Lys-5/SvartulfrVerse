import json
import time
import requests
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

CARDS_TO_ALIGN = [
    {
        'name': 'Erik Ulfr Douglas',
        'cid': '_QPea6g4Q1QfeYCVHCLMPR',
        'file': 'FINAL/Erik_Douglas_card.json',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public',
        'asset_title': 'erikMain'
    },
    {
        'name': 'Logan Járn Douglas',
        'cid': '_T8Ywcr9FEqNf9JxbK6eHP',
        'file': 'FINAL/Logan_Douglas_card.json',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public',
        'asset_title': 'loganMain'
    },
    {
        'name': 'Malachia Björn Douglas Bloodmoon',
        'cid': '_RDfz7XzTpM23LpPALVXHM',
        'file': 'FINAL/Malachia_Douglas_Bloodmoon_card.json',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public',
        'asset_title': 'mailMain'
    },
    {
        'name': 'Noah Loki Douglas Bloodmoon',
        'cid': '_zFLUjV8aVxQRAfQxGcAcY',
        'file': 'FINAL/Noah_Douglas_Bloodmoon_card.json',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public',
        'asset_title': 'noahMain'
    },
    {
        'name': 'Wulfnic Bóleygr Bloodmoon',
        'cid': '_HEQQbbRFwKdG8QE2Fh1z1',
        'file': 'FINAL/Wulfnic_Bloodmoon_card.json',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public',
        'asset_title': 'mainWulfnic'
    }
]

EDITABLE_FIELDS = [
    'name', 'display_name', 'avatar', 'description', 'personality', 'mes_example',
    'first_mes', 'scenario', 'post_history_instructions', 'pre_history_instructions',
    'visual_description', 'creator_notes', 'model_url', 'soundcloud_url', 'character_note',
    'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating', 'chat_name',
    'pronouns', 'outfits', 'default_outfit', 'shared_info', 'alternate_greetings',
    'secretFields', 'secrets', 'fields', 'commands', 'metadata'
]

print("=== STEP 1: UPDATING LOCAL CARD FILES ===")
for item in CARDS_TO_ALIGN:
    cpath = ROOT / item['file']
    with open(cpath, 'r', encoding='utf-8') as f:
        cdata = json.load(f)
    
    old_avatar = cdata.get('avatar')
    cdata['avatar'] = item['avatar']
    
    with open(cpath, 'w', encoding='utf-8') as f:
        json.dump(cdata, f, indent=2, ensure_ascii=False)
    print(f"Updated {item['file']}:\n  Old: {old_avatar}\n  New: {item['avatar']}")

print("\n=== STEP 2: SYNCING LOREBOOKS/OPTIMIZED WITH FINAL ===")
f_prim = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'
o_prim = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'
with open(f_prim, 'r', encoding='utf-8') as f:
    prim_data = json.load(f)
with open(o_prim, 'w', encoding='utf-8') as f:
    json.dump(prim_data, f, indent=2, ensure_ascii=False)
print("Synced FINAL/Svartulfr_NPC_Primary.json -> lorebooks/optimized/Svartulfr_NPC_Primary.json")

print("\n=== STEP 3: DEPLOYING LIVE VIA WYVERN WEB API ===")
for item in CARDS_TO_ALIGN:
    cid = item['cid']
    cpath = ROOT / item['file']
    with open(cpath, 'r', encoding='utf-8') as f:
        cdata = json.load(f)
        
    safe_payload = {k: cdata[k] for k in EDITABLE_FIELDS if k in cdata}
    
    print(f"\nDeploying {item['name']} ({cid})...")
    url = f'https://app.wyvern.chat/api/characters/{cid}'
    r_put = requests.put(url, headers=headers, json=safe_payload)
    print(f"PUT {url} -> Status {r_put.status_code}")
    if r_put.status_code != 200:
        print(f"ERROR: {r_put.text[:400]}")
        raise RuntimeError(f"Failed to update character {item['name']}")
        
    # Verify immediately via GET
    r_get = requests.get(url, headers=headers)
    assert r_get.status_code == 200, f"Failed GET for {item['name']}"
    live_char = r_get.json()
    assert live_char.get('avatar') == item['avatar'], f"Avatar mismatch for {item['name']}! Got {live_char.get('avatar')}"
    assert live_char.get('description') == cdata.get('description'), f"Description mismatch for {item['name']}!"
    print(f"Verified live {item['name']}: Avatar matches ({item['asset_title']}), Description length: {len(live_char.get('description'))}")
    time.sleep(1.0)

print("\n=== ALL 5 CARDS SUCCESSFULLY UPDATED AND DEPLOYED LIVE! ===")
