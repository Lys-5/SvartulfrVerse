import urllib.request
import urllib.error
import json
import pathlib
import sys

WT_PATH = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt')
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

url = 'https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC'
print(f"Requesting {url} ...", flush=True)

req = urllib.request.Request(url, headers=headers, method='GET')
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"HTTP Status: {resp.status}", flush=True)
        raw = resp.read().decode('utf-8')
        data = json.loads(raw)
        print(f"ID: {data.get('id')}", flush=True)
        print(f"Revision: {data.get('revision')}", flush=True)
        print(f"Name: {data.get('name')}", flush=True)
        print(f"Entries count: {len(data.get('entries', []))}", flush=True)
        print(f"Lexicon count: {len(data.get('lexicon', []))}", flush=True)
        print(f"Keys: {list(data.keys())}", flush=True)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}", flush=True)
    print(e.read().decode('utf-8', errors='ignore')[:500], flush=True)
except Exception as e:
    print(f"Exception: {type(e).__name__} - {e}", flush=True)
