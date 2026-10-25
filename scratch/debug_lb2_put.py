import urllib.request
import urllib.error
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()

lid = '_HfG7TeV6MJyj6bxMwxkpt'
fpath = 'FINAL/Svartulfr_Lorebook_II.json'

with open(fpath, 'r', encoding='utf-8') as f:
    src = json.load(f)

entries = src.get('lexicon') or src.get('entries') or []
payload = {
    'name': src.get('name', 'Svartúlfr - Lorebook II'),
    'description': src.get('description', ''),
    'visibility': src.get('visibility', 'private'),
    'rating': src.get('rating', 'explicit'),
    'scan_depth': src.get('scan_depth', 5),
    'token_budget': src.get('token_budget', 5000),
    'recursive_scanning': src.get('recursive_scanning', True),
    'lexicon': entries
}

url = f'https://app.wyvern.chat/api/lorebooks/{lid}'
data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
req = urllib.request.Request(
    url,
    data=data,
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    method='PUT'
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print("Success:", resp.status)
except urllib.error.HTTPError as e:
    print(f"HTTPError {e.code}: {e.reason}")
    body = e.read().decode('utf-8', errors='ignore')
    print("Error body:", body[:1000])
