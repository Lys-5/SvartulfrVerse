import json
import requests
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

cards_info = {
    'Edric': (ROOT / 'FINAL' / 'Edric_Douglas_card.json', '_TbRM3EdxDjHFgqztTbCpL'),
    'Erik': (ROOT / 'FINAL' / 'Erik_Douglas_card.json', '_QPea6g4Q1QfeYCVHCLMPR'),
    'Jasper': (ROOT / 'FINAL' / 'Jasper_Douglas_Bloodmoon_card.json', '_t4J9aQNJM36cUKAP4wB4U'),
    'Logan': (ROOT / 'FINAL' / 'Logan_Douglas_card.json', '_T8Ywcr9FEqNf9JxbK6eHP'),
    'Mackenzie': (ROOT / 'FINAL' / 'Mackenzie_Sanchez_Rogers_card.json', '_zn24784jfcchQ7EwCyAnm'),
    'Malachia': (ROOT / 'FINAL' / 'Malachia_Douglas_Bloodmoon_card.json', '_RDfz7XzTpM23LpPALVXHM'),
    'Noah': (ROOT / 'FINAL' / 'Noah_Douglas_Bloodmoon_card.json', '_zFLUjV8aVxQRAfQxGcAcY'),
    'Wulfnic': (ROOT / 'FINAL' / 'Wulfnic_Bloodmoon_card.json', '_HEQQbbRFwKdG8QE2Fh1z1')
}

print('=== LOCAL CARD AVATARS ===')
for name, (path, cid) in cards_info.items():
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f'{name:10} | CID: {cid} | Local Avatar: {data.get("avatar")}')

print('\n=== LIVE CARD AVATARS ===')
r = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
if r.status_code == 200:
    chars = {c['id']: c for c in r.json().get('characters', [])}
    for name, (path, cid) in cards_info.items():
        c = chars.get(cid)
        if c:
            print(f'{name:10} | CID: {cid} | Live Avatar: {c.get("avatar")}')
        else:
            print(f'{name:10} | CID: {cid} | NOT FOUND IN LIVE MINE!')
else:
    print('Failed to get live mine:', r.status_code)

# Check Gallery for Lorebook Primary and Secondary
lb_prim_id = '_zwEqgEEzh12X6gHVmMKKC'
lb_sec_id = '_Uht3Ckz44JBDrPnUHq7LV'

print('\n=== GALLERY ASSETS IN PRIMARY LB ===')
r_gal = requests.get(f'https://app.wyvern.chat/api/gallery/lorebook/{lb_prim_id}', headers=headers)
if r_gal.status_code == 200:
    gal = r_gal.json()
    for item in gal:
        name = item.get('name', '')
        url = item.get('imageURL', '')
        if any(k in name.lower() for k in ['erik', 'logan', 'mal', 'noah', 'wulf', 'jasper', 'mack']):
            print(f"  Gallery asset: {name:20} -> {url}")
else:
    print('Failed to fetch gallery for primary lb:', r_gal.status_code)

print('\n=== LOREBOOK ENTRY AVATARS ===')
with open(ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    lb_prim = json.load(f)

for e in lb_prim.get('lexicon', []):
    for name, (path, cid) in cards_info.items():
        if cid in e.get('ignored_characters', []):
            print(f"Lorebook Primary: {e.get('name'):32} | Avatar: {e.get('avatar')}")

with open(ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    lb_sec = json.load(f)

for e in lb_sec.get('lexicon', []):
    for name, (path, cid) in cards_info.items():
        if cid in e.get('ignored_characters', []):
            print(f"Lorebook Secondary: {e.get('name'):32} | Avatar: {e.get('avatar')}")
