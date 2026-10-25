import requests, json, pathlib

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

approved_cards = [
    ('_QPea6g4Q1QfeYCVHCLMPR', 'FINAL/Erik_Douglas_card.json', 'Erik Ulfr Douglas'),
    ('_RDfz7XzTpM23LpPALVXHM', 'FINAL/Malachia_Douglas_Bloodmoon_card.json', 'Malachia Björn Douglas Bloodmoon'),
    ('_t4J9aQNJM36cUKAP4wB4U', 'FINAL/Jasper_Douglas_Bloodmoon_card.json', 'Jasper Svartr Douglas Bloodmoon'),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'FINAL/Noah_Douglas_Bloodmoon_card.json', 'Noah Loki Douglas Bloodmoon'),
    ('_TbRM3EdxDjHFgqztTbCpL', 'FINAL/Edric_Douglas_card.json', 'Edric Douglas'),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'FINAL/Logan_Douglas_card.json', 'Logan Járn Douglas'),
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'FINAL/Wulfnic_Bloodmoon_card.json', 'Wulfnic Báleygr Bloodmoon'),
    ('_zn24784jfcchQ7EwCyAnm', 'FINAL/Mackenzie_Sanchez_Rogers_card.json', 'Mackenzie Sanchez-Rogers'),
]

print("=== CHECKING 8 APPROVED CARDS (LIVE vs LOCAL) ===")
for cid, local_file, expected_name in approved_cards:
    # check local
    p = pathlib.Path(local_file)
    local_exists = p.exists()
    local_data = json.loads(p.read_text(encoding='utf-8')) if local_exists else {}
    local_id = local_data.get('id') or local_data.get('_id')
    local_name = local_data.get('name')
    local_outfits = len(local_data.get('outfits', []))

    # check live
    r = requests.get(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers)
    live_status = r.status_code
    live_data = r.json() if live_status == 200 else {}
    live_name = live_data.get('name')
    live_outfits = len(live_data.get('outfits', []))

    print(f"[{cid}] {expected_name}")
    print(f"  Local: exists={local_exists}, id={local_id}, name={local_name}, outfits={local_outfits}")
    print(f"  Live:  status={live_status}, name={live_name}, outfits={live_outfits}")
