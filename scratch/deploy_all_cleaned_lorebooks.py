import urllib.request
import urllib.error
import json
import pathlib
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

# 1. Refresh token
ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
rt_path = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\74bb3384-9979-419b-80ab-c29e070cbffe\scratch\refresh_token.txt')
wt_path = ROOT / 'scratch' / 'wyvern_token.txt'

rt = rt_path.read_text(encoding='utf-8').strip()
body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
req = urllib.request.Request(f'https://securetoken.googleapis.com/v1/token?key={ak}', data=body, headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    token = data['id_token']
    wt_path.write_text(token, encoding='utf-8')
    print("Token rinfrescato con successo.")

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

LOREBOOKS_SYNC = [
    ('_EjXxkmPVhpCXg8xABpFkK', 'Svartulfr_Location.json', 'Location'),
    ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 'Lorebook II'),
    ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 'Lorebook I'),
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary'),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary'),
]

print("\n=== DEPLOYMENT SUI 5 LOREBOOK AGGIORNATI ===")
for lid, fname, label in LOREBOOKS_SYNC:
    fpath = FINAL_DIR / fname
    d = json.loads(fpath.read_text(encoding='utf-8'))
    entries = d.get('lexicon') or d.get('entries') or []
    
    payload = {
        'name': d.get('name'),
        'description': d.get('description'),
        'visibility': 'private',
        'rating': 'explicit',
        'scan_depth': d.get('scan_depth', 5),
        'token_budget': d.get('token_budget', 5000),
        'recursive_scanning': d.get('recursive_scanning', True),
        'lexicon': entries
    }
    
    payload_bytes = json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    put_req = urllib.request.Request(f'https://app.wyvern.chat/api/lorebooks/{lid}', data=payload_bytes, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(put_req, timeout=60) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f"SUCCESS HTTP {resp.status} on {label} ({lid}) -> {len(res.get('lexicon', []))} entries salvate!")
    except urllib.error.HTTPError as e:
        print(f"ERROR HTTP {e.code} on {label}: {e.read().decode('utf-8', errors='ignore')[:250]}")
    except Exception as e:
        print(f"ERROR on {label}: {e}")
    time.sleep(1)

print("\n=== DEPLOYMENT LOREBOOK COMPLETATO CON SUCCESSO! ===")
