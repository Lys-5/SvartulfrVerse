import urllib.request
import json

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

eps = [
    '/api/prompt-assemblies',
    '/api/prompt-assemblies/mine',
    '/api/prompt-pieces',
    '/api/prompt-pieces/mine',
    '/api/user/prompt-assemblies',
    '/api/userInventory/prompt-assemblies',
    '/api/user-inventory/prompt-assemblies'
]

for ep in eps:
    url = f"https://app.wyvern.chat{ep}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"[OK {resp.status}] {ep}: len={len(data)}")
            try:
                parsed = json.loads(data)
                print(f"   Parsed: {type(parsed).__name__}, keys/len={list(parsed.keys()) if isinstance(parsed, dict) else len(parsed)}")
            except:
                pass
    except urllib.error.HTTPError as e:
        print(f"[{e.code}] {ep}")
    except Exception as e:
        print(f"[ERR] {ep}: {e}")
