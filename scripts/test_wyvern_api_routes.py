import urllib.request
import json

with open('scratch/wyvern_token.txt', 'r') as f:
    token = f.read().strip()

test_urls = [
    'https://app.wyvern.chat/api/providers/custom',
    'https://app.wyvern.chat/api/custom-providers',
    'https://app.wyvern.chat/api/user-connections',
    'https://app.wyvern.chat/api/connections/user',
    'https://app.wyvern.chat/api/providers'
]

for url in test_urls:
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    })
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"200 OK: {url}")
            data = json.loads(resp.read().decode('utf-8'))
            print("  Data type:", type(data), "len:", len(data) if isinstance(data, (list, dict)) else 0)
    except urllib.error.HTTPError as e:
        print(f"{e.code} {e.reason}: {url}")
    except Exception as e:
        print(f"Error {url}: {e}")
