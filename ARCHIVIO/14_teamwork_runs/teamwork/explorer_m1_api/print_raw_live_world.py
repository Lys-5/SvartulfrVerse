import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

url = "https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7"
req = urllib.request.Request(url, headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
})

with urllib.request.urlopen(req) as resp:
    text = resp.read().decode('utf-8')
    data = json.loads(text)
    print("Keys in live _CgYT8fHXpDC4crjmegQF7 response:")
    for k, v in data.items():
        v_str = str(v)
        if len(v_str) > 60: v_str = v_str[:60] + '...'
        print(f"  {k}: {v_str}")
