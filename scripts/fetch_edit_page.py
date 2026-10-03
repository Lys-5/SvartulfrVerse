import urllib.request
import re
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(f'https://app.wyvern.chat/worlds/edit/{WORLD_ID}', headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
print(f'Found {len(scripts)} scripts in world edit page:')
for s in scripts:
    if 'chunks' in s:
        print(' ', s)
