import urllib.request
import json

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

eps = [
    '/api/exploreSearch/prompt-assemblies?page=1&limit=10',
    '/api/exploreSearch/prompt-templates?page=1&limit=10',
    '/api/prompt-templates?page=1&limit=10',
    '/api/prompt-templates/mine',
]

for ep in eps:
    url = f"https://app.wyvern.chat{ep}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            parsed = json.loads(data)
            print(f"[OK 200] {ep}:")
            if isinstance(parsed, dict):
                print(f"   Keys: {list(parsed.keys())}")
                for k in ['results', 'assemblies', 'templates', 'items', 'total']:
                    if k in parsed:
                        print(f"   {k}: {len(parsed[k]) if isinstance(parsed[k], list) else parsed[k]}")
                        if isinstance(parsed[k], list) and len(parsed[k]) > 0:
                            print(f"      First item: {parsed[k][0].get('id')} - {parsed[k][0].get('name')}")
            elif isinstance(parsed, list):
                print(f"   List len: {len(parsed)}")
                if len(parsed) > 0:
                    print(f"      First item: {parsed[0]}")
    except Exception as e:
        print(f"[ERR] {ep}: {e}")
