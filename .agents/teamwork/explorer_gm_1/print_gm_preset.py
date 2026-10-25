import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

url = 'https://app.wyvern.chat/api/simple-assistant-config/narrator-presets'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    for p in data.get('presets', []):
        if p.get('title') == 'Game Master':
            print("=== GAME MASTER PRESET ===")
            print(json.dumps(p, indent=2))
