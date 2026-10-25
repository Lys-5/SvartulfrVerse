import json
import urllib.request
import urllib.error
import sys
import os

# Add scratch to path to import refresh_token if needed
sys.path.append(r'e:\repository\SvartulfrVerse\scratch')
try:
    import refresh_token
except ImportError:
    refresh_token = None

TOKEN_PATH = r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt'

def get_token():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        return f.read().strip()

def test_get(lb_id, token):
    url = f"https://app.wyvern.chat/api/lorebooks/{lb_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'ExplorerR73/1.0',
        'Accept': 'application/json'
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return resp.status, data
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')
    except Exception as e:
        return -1, str(e)

token = get_token()
print(f"Testing with existing token (len={len(token)})...")

status, res = test_get('_zwEqgEEzh12X6gHVmMKKC', token)
print(f"GET Primary (_zwEqgEEzh12X6gHVmMKKC): status={status}")

if status == 401 or status == 403:
    print("Token appears expired or invalid. Attempting refresh...")
    if refresh_token:
        token = refresh_token.refresh()
        status, res = test_get('_zwEqgEEzh12X6gHVmMKKC', token)
        print(f"After refresh, GET Primary status: {status}")

if status == 200:
    print("Primary metadata:")
    print(f"  id: {res.get('id') or res.get('_id')}")
    print(f"  name: {res.get('name')}")
    print(f"  photoURL: {res.get('photoURL')}")
    print(f"  token_budget: {res.get('token_budget')}")
    print(f"  entries in entries: {len(res.get('entries', []))}")
    print(f"  entries in lexicon: {len(res.get('lexicon', []))}")

status_sec, res_sec = test_get('_Uht3Ckz44JBDrPnUHq7LV', token)
print(f"\nGET Secondary (_Uht3Ckz44JBDrPnUHq7LV): status={status_sec}")
if status_sec == 200:
    print("Secondary metadata:")
    print(f"  id: {res_sec.get('id') or res_sec.get('_id')}")
    print(f"  name: {res_sec.get('name')}")
    print(f"  photoURL: {res_sec.get('photoURL')}")
    print(f"  token_budget: {res_sec.get('token_budget')}")
    print(f"  entries in entries: {len(res_sec.get('entries', []))}")
    print(f"  entries in lexicon: {len(res_sec.get('lexicon', []))}")
