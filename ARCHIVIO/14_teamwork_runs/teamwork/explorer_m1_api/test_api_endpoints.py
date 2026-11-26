import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

endpoints = [
    ("GET", "https://app.wyvern.chat/api/characters/mine"),
    ("GET", "https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7"),
    ("GET", "https://app.wyvern.chat/api/worlds"),
    ("GET", "https://app.wyvern.chat/api/worlds/mine"),
    ("GET", "https://app.wyvern.chat/api/worlds/user"),
    ("GET", "https://app.wyvern.chat/api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL"),
]

for method, url in endpoints:
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            print(f"[{method}] {url} -> {resp.status} (len {len(data)})")
            try:
                parsed = json.loads(data.decode('utf-8'))
                if isinstance(parsed, list):
                    print(f"   List of {len(parsed)} items. Sample: {[x.get('name') or x.get('display_name') or x.get('id') for x in parsed[:3]]}")
                elif isinstance(parsed, dict):
                    print(f"   Dict keys: {list(parsed.keys())[:8]}")
                    if 'name' in parsed:
                        print(f"   Name: {parsed.get('name')}")
            except Exception as e:
                print("   Could not parse JSON:", e)
    except urllib.error.HTTPError as e:
        print(f"[{method}] {url} -> HTTPError {e.code}: {e.reason}")
        err_body = e.read()
        print("   Body:", err_body[:200])
    except Exception as e:
        print(f"[{method}] {url} -> Error: {e}")
