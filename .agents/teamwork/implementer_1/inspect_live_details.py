import json
import requests
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

cids = [
    ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik'),
    ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan'),
    ('_RDfz7XzTpM23LpPALVXHM', 'Malachia'),
    ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah'),
    ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic')
]

for cid, name in cids:
    r = requests.get(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers)
    if r.status_code == 200:
        cdata = r.json()
        print(f"=== {name} ({cid}) ===")
        print(f"  lorebooks: {cdata.get('lorebooks')}")
        print(f"  story_engine_id: {cdata.get('story_engine_id')}")
        print(f"  outfits count: {len(cdata.get('outfits', []))}")
        print(f"  tags: {cdata.get('tags')}")
