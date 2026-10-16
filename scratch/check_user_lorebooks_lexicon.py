import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
UID = '2r4fVpvImte5dbljedLkZJxre2d2'

req = urllib.request.Request(f'{API_BASE}/lorebooks/user/{UID}', headers={'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

lbs = data.get('lorebooks', [])
print(f'Found {len(lbs)} lorebooks for user {UID}:')
for lb in lbs:
    lid = lb.get('id')
    f_req = urllib.request.Request(f'{API_BASE}/lorebooks/{lid}', headers={'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(f_req) as f_resp:
            full = json.loads(f_resp.read().decode('utf-8'))
            e_cnt = len(full.get('entries', []))
            l_cnt = len(full.get('lexicon', []))
            print(f"  {lid} ({full.get('name')}) -> entries: {e_cnt}, lexicon: {l_cnt}")
    except Exception as e:
        print(f"  {lid} error: {e}")
