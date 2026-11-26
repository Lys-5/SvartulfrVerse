import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

endpoints = [
    '/simple-assistant-config',
    '/simple-assistant-config/usable',
    '/simple-assistant-config/browse',
    '/simple-assistant-config/mine'
]

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

for ep in endpoints:
    url = f'https://app.wyvern.chat/api{ep}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"[HTTP {resp.status}] GET {ep} -> len: {len(data)}")
            try:
                j = json.loads(data)
                if isinstance(j, list):
                    print(f"  Count: {len(j)}")
                    if len(j) > 0:
                        print(f"  Item 0 keys: {list(j[0].keys())}")
                        print(f"  Item 0 sample: {json.dumps(j[0], indent=2)[:500]}")
                elif isinstance(j, dict):
                    print(f"  Keys: {list(j.keys())}")
                    for k in j:
                        if isinstance(j[k], list):
                            print(f"    Key '{k}' has {len(j[k])} items")
                            if len(j[k]) > 0 and isinstance(j[k][0], dict):
                                print(f"      Item keys: {list(j[k][0].keys())}")
                                print(f"      Item sample:\n{json.dumps(j[k][0], indent=2)[:800]}")
            except Exception as e:
                print(f"  Parse error: {e}, text: {data[:200]}")
    except urllib.error.HTTPError as e:
        print(f"[HTTP {e.code}] GET {ep} -> {e.read().decode('utf-8', errors='replace')[:300]}")
    except Exception as e:
        print(f"[ERROR] GET {ep} -> {e}")
