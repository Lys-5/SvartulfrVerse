import sys
import json
import pathlib
import urllib.request

root = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(root / 'scratch'))
import refresh_token

token = refresh_token.refresh()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'AuditorBot/1.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

for base in ['https://app.wyvern.chat/api', 'https://api.wyvern.chat']:
    for path in ['/lorebooks/_zwEqgEEzh12X6gHVmMKKC']:
        url = f"{base}{path}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                print(f"GET {url} -> {resp.status}")
        except Exception as e:
            print(f"GET {url} -> ERROR: {e}")
