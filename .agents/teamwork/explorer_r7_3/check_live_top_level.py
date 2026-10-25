import json
import urllib.request

TOKEN_PATH = r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt'
with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ExplorerR73/1.0',
    'Accept': 'application/json'
}

for name, lb_id in [('Primary', '_zwEqgEEzh12X6gHVmMKKC'), ('Secondary', '_Uht3Ckz44JBDrPnUHq7LV')]:
    url = f"https://app.wyvern.chat/api/lorebooks/{lb_id}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    print(f"=== Top-level live fields for {name} ({lb_id}) ===")
    for k, v in data.items():
        if k not in ['lexicon', 'entries', 'creator']:
            print(f"  {k}: {repr(v)}")
    print()
