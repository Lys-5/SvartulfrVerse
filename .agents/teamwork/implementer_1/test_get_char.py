import json
import requests
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

cid = '_QPea6g4Q1QfeYCVHCLMPR'
r = requests.get(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers)
print("GET status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    print("Character keys:", list(data.keys()))
    print("Name:", data.get('name'))
    print("Avatar:", data.get('avatar'))
