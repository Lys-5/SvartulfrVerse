import sys
import json
import urllib.request
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

token = get_auth_token()

for lb_id, name in [('_zwEqgEEzh12X6gHVmMKKC', 'Primary'), ('_Uht3Ckz44JBDrPnUHq7LV', 'Secondary')]:
    url = f'https://app.wyvern.chat/api/gallery/lorebook/{lb_id}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    try:
        gallery = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        print(f"\n=== {name} Lorebook Gallery: {len(gallery)} items ===")
        for g in gallery:
            print(f"  title={g.get('title'):20s} | type={g.get('type'):10s} | url={g.get('imageURL')}")
    except Exception as e:
        print(f"{name} Gallery Error:", e)
