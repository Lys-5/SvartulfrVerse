import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request
import json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}

world_id = "_YpX47fNraQFw2dD7TdycJ"

payload = {
    "world_id": world_id,
    "world": world_id,
    "name": "SUCC Welcome Day",
    "description": "Cerimonia del Welcome Day della SUCC sul Lunar Quad il 26 agosto 2024.",
    "visibility": "private"
}

url = 'https://app.wyvern.chat/api/worlds/scenarios'

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as resp:
        print(f'Test POST -> HTTP {resp.status}')
        data = resp.read().decode('utf-8')
        print('  data:', data[:500])
except urllib.error.HTTPError as e:
    err = e.read().decode('utf-8', errors='ignore')
    print(f'Test POST -> HTTP {e.code}: {err[:500]}')
except Exception as e:
    print(f'Test POST -> {e}')
