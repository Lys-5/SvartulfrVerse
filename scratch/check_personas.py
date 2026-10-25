import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/api/user-personas', headers=headers)
print("Status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    personas = data.get('personas', []) if isinstance(data, dict) else data
    print(f"Total personas: {len(personas)}")
    for p in personas:
        print(f"  {p.get('persona_id', p.get('id'))} -> {p.get('name')}")
