import sys
import json
import urllib.request
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

token = get_auth_token()
url_gal = 'https://app.wyvern.chat/api/gallery/lorebook/_zwEqgEEzh12X6gHVmMKKC'
gallery = json.loads(urllib.request.urlopen(urllib.request.Request(url_gal, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8'))

url_lb = 'https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC'
lb = json.loads(urllib.request.urlopen(urllib.request.Request(url_lb, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8'))
entries = lb.get('lexicon') or lb.get('entries') or []

mapping = {
    'Erik Ulfr Douglas': 'erikMain',
    'Logan Jörn Douglas': 'loganMain',
    'Malachia Björn Douglas Bloodmoon': 'mailMain', # or malachia
    'Noah Loki Douglas Bloodmoon': 'noahMain',
    'Wulfnic Bóleygr Bloodmoon': 'mainWulfnic',
    'Nixara Hvit Bloodmoon': 'nixara',
    'Scarlett Rose': 'scarlettMain',
    'Sierra Cruz': 'sierraMain',
    'Zefir Hvitskog': 'ZefirMain',
    'Kaladin Nargathon': 'Kaladin',
    'Elizabeth Duskwood': 'elizabeth'
}

gal_dict = {g['title']: g['imageURL'] for g in gallery}

for char_name, gal_title in mapping.items():
    entry = next((e for e in entries if char_name.lower() in e.get('name', '').lower() or e.get('name', '').lower() in char_name.lower()), None)
    img_url = gal_dict.get(gal_title)
    print(f"Match: {char_name:35s} -> Entry: {entry.get('name') if entry else 'MISSING':30s} | Gal: {gal_title:15s} | Img: {img_url}")
