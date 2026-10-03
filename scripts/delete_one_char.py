import sys, requests
sys.path.append(r'd:\SvartulfrVerse\scripts')
from sync_from_wyvern_web import get_auth_token

API = 'https://app.wyvern.chat/api'
cid = sys.argv[1]
H = {'Authorization': f'Bearer {get_auth_token()}'}
d = requests.get(f'{API}/worlds/characters/{cid}', headers=H)
if d.status_code == 200 and (d.json().get('long_summary') or ''):
    print('ABORT: target has long_summary content, not an empty duplicate'); sys.exit(1)
r = requests.delete(f'{API}/worlds/characters/{cid}', headers=H)
v = requests.get(f'{API}/worlds/characters/{cid}', headers=H)
print(f'{cid}: DELETE {r.status_code}, verify GET {v.status_code}')
