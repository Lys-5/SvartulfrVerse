import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

url = 'https://app.wyvern.chat/api/simple-assistant-config'

# 1. Send empty POST
req = urllib.request.Request(url, data=b'{}', headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as resp:
        print("[HTTP 200] POST empty:", resp.read().decode())
except urllib.error.HTTPError as e:
    print(f"[HTTP {e.code}] POST empty:\n", e.read().decode())
except Exception as e:
    print("Err:", e)
