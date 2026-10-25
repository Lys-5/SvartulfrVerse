import urllib.request
import urllib.error
import json

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

user_id = '2r4fVpvImte5dbljedLkZJxre2d2'

queries = [
    '',
    '?visibility=private',
    '?visibility=all',
    '?private=true',
    '?include_private=true',
    '?rating=explicit',
    '?rating=all',
    '?all=true',
    '?limit=50',
    '?page=1&limit=50',
    '?type=all',
    '?mine=true',
    '?sort=recent',
    '?show_private=true',
    '?includePrivate=true'
]

for q in queries:
    url = f'https://app.wyvern.chat/api/worlds/user/{user_id}{q}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            res = json.loads(data)
            count = len(res.get('worlds', [])) if isinstance(res, dict) else len(res)
            print(f"Query '{q}' -> count: {count}, total: {res.get('total') if isinstance(res, dict) else 'N/A'}")
            if count > 0:
                print(f"  FOUND: {res}")
    except urllib.error.HTTPError as e:
        print(f"Query '{q}' -> {e.code}")
