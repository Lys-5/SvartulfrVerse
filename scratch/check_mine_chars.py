import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/api/characters/mine', headers=headers)
print("Status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    chars = data.get('characters', [])
    print(f"Total characters in /mine: {len(chars)}")
    for c in chars:
        print(f"  {c.get('id')} -> {c.get('name')}")
