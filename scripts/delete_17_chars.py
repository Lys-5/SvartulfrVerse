import sys, json, requests, os, time
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API = 'https://app.wyvern.chat/api'
token = get_auth_token()
H = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
SNAP_DIR = r'd:\SvartulfrVerse\docs\snapshots_2026-10-03'
os.makedirs(SNAP_DIR, exist_ok=True)

to_delete = [
    "Rozalia Tănase", "Ruby Valerius", "Vesna", "Mikan", "Ginger", 
    "Orion and Sigrid Valois", "Henrey Cote", "Aria Xenthon", "Tori", 
    "River", "Ailsa Hourie", "Silas", "Bramble Mossmere", "Evan", 
    "Vespera Thorne", "Eira Elloway", "Darius Azadi"
]

chars = requests.get(f'{API}/worlds/characters/world/{WORLD_ID}', headers=H).json()
for c in chars:
    name = c.get('display_name', '')
    if name in to_delete:
        cid = c.get('id')
        
        # Snapshot
        d = requests.get(f'{API}/worlds/characters/{cid}', headers=H).json()
        with open(os.path.join(SNAP_DIR, f'DELETED_{name.replace(" ", "_")}_{cid}.json'), 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            
        # Delete
        r = requests.delete(f'{API}/worlds/characters/{cid}', headers=H)
        
        # Verify
        v = requests.get(f'{API}/worlds/characters/{cid}', headers=H)
        print(f'Deleted {name} ({cid}): {r.status_code}, verified 404={v.status_code == 404}')
        time.sleep(0.3)
