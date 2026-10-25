import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request
import json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

candidate_ids = [
    '_CgYT8fHXpDC4crjmegQF7',
    '_YpX47fNraQFw2dD7TdycJ',
]

for wid in candidate_ids:
    url = f'https://app.wyvern.chat/api/worlds/{wid}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            creator = data.get('creator')
            creator_name = creator.get('displayName') if isinstance(creator, dict) else creator
            print(f"EXISTS: {wid} | Name: {data.get('name')} | Creator: {creator_name} | Visibility: {data.get('visibility')}")
    except Exception as e:
        print(f"ERROR {wid}: {e}")

# Also check worlds owned by user
try:
    req = urllib.request.Request('https://app.wyvern.chat/api/worlds/user/all', headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print('User worlds count:', len(data))
        for w in data:
            print(f"  ID: {w.get('_id')} | Name: {w.get('name')}")
except Exception as e:
    print('Error user/all:', e)
