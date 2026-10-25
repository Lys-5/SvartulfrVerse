import urllib.request
import urllib.error
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

wid = '_CgYT8fHXpDC4crjmegQF7'
url = f"https://app.wyvern.chat/api/worlds/{wid}"
req = urllib.request.Request(url, headers=headers, method='DELETE')

try:
    with urllib.request.urlopen(req) as resp:
        print(f"DELETE {wid} -> Status: {resp.status}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8', errors='ignore')
    print(f"DELETE {wid} -> HTTP Error {e.code}: {err_body}")
except Exception as e:
    print(f"DELETE {wid} -> Error: {e}")
