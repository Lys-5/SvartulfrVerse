import urllib.request
import urllib.parse
import json
import re
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
RT_PATH = ROOT / 'scratch' / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'

def get_token():
    try:
        token = WT_PATH.read_text(encoding='utf-8').strip()
    except Exception:
        token = None
    return token

def refresh_token():
    rt = RT_PATH.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    data = urllib.parse.urlencode({'grant_type': 'refresh_token', 'refresh_token': rt}).encode()
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        token = res['id_token']
        WT_PATH.write_text(token, encoding='utf-8')
        return token

token = get_token()

def test_endpoint(endpoint):
    global token
    url = f'https://app.wyvern.chat/api{endpoint}'
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"[HTTP {resp.status}] GET {endpoint} -> len: {len(data)}")
            try:
                j = json.loads(data)
                if isinstance(j, list):
                    print(f"  Count: {len(j)}")
                    if len(j) > 0:
                        print(f"  Sample keys: {list(j[0].keys()) if isinstance(j[0], dict) else type(j[0])}")
                elif isinstance(j, dict):
                    print(f"  Keys: {list(j.keys())}")
            except Exception:
                print(f"  Non-JSON body: {data[:200]}")
            return resp.status, data
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f"[HTTP {e.code}] GET {endpoint} -> {body[:250]}")
        if e.code == 500 and "Unauthorized" in body:
            print("Token expired, refreshing...")
            token = refresh_token()
            return test_endpoint(endpoint)
        return e.code, body
    except Exception as e:
        print(f"[ERROR] GET {endpoint} -> {e}")
        return None, str(e)

print("--- Testing API Endpoints ---")
endpoints = [
    '/assistants',
    '/mine/assistants',
    '/characters?type=assistant',
    '/characters?kind=assistant',
    '/characters/mine',
    '/characters',
    '/users/me',
    '/user/me',
    '/user-personas',
    '/character-scenarios',
    '/lorebooks',
    '/prompt-templates',
    '/prompts',
    '/story-engines'
]

for ep in endpoints:
    test_endpoint(ep)
