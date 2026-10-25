import urllib.request
import json

# Check what headers or endpoints work
headers = {
    'Host': 'localhost:9222',
    'Origin': 'http://localhost:9222'
}

for path in ['/json', '/json/list', '/json/version']:
    for h in [
        {'Host': 'localhost:9222'},
        {'Host': '127.0.0.1:9222'},
        {'Host': 'localhost:9222', 'Origin': 'http://localhost:9222'},
        {}
    ]:
        url = f'http://127.0.0.1:9222{path}'
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req) as resp:
                print(f"SUCCESS: {url} with {h} -> {resp.status}")
                print(resp.read().decode()[:200])
                break
        except Exception as e:
            pass
