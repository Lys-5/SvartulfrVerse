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

url = 'https://app.wyvern.chat/api/simple-assistant-config'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    for c in data.get('configs', []):
        print(f"ID: {c.get('id')}")
        print(f"Title: {c.get('title')}")
        print(f"Kind: {c.get('kind')}")
        print(f"Description: {c.get('description')}")
        print(f"System Prompt len: {len(c.get('system_prompt', ''))}")
        print(f"Final Instructions len: {len(c.get('final_instructions', ''))}")
        print(f"Keys: {list(c.keys())}")
        print("-" * 50)
