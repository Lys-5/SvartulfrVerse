import urllib.request
import json
import pathlib
import time

token = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

lorebooks = [
    ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartúlfr - Lorebook I', 'FINAL/Svartulfr_Lorebook_I.json'),
    ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartúlfr - Lorebook II', 'FINAL/Svartulfr_Lorebook_II.json'),
    ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartúlfr - Lorebook III', 'FINAL/Svartulfr_Lorebook_III.json'),
    ('_EjXxkmPVhpCXg8xABpFkK', 'Svartúlfr - Location', 'FINAL/Svartulfr_Location.json'),
    ('_zwEqgEEzh12X6gHVmMKKC', 'Svartúlfr - NPC Primary', 'FINAL/Svartulfr_NPC_Primary.json'),
    ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartúlfr - NPC Secondary', 'FINAL/Svartulfr_NPC_Secondary.json')
]

print("=== VERIFYING STANDALONE LOREBOOKS (LOCAL VS LIVE API) ===")
for lbid, expected_name, local_file in lorebooks:
    local_path = pathlib.Path(local_file)
    local_count = 0
    if local_path.exists():
        with open(local_path, 'r', encoding='utf-8') as f:
            ld = json.load(f)
            local_count = len(ld.get('entries', []))
    
    url = f'https://app.wyvern.chat/api/lorebooks/{lbid}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            live_name = data.get('name')
            live_count = len(data.get('lexicon', []))
            scan_depth = data.get('scan_depth')
            token_budget = data.get('token_budget')
            rec_scan = data.get('recursive_scanning')
            print(f"ID: {lbid} | Status: 200 OK")
            print(f"  Name: '{live_name}' (expected: '{expected_name}')")
            print(f"  Local entries: {local_count} | Live lexicon count: {live_count}")
            print(f"  scan_depth: {scan_depth} | token_budget: {token_budget} | recursive_scanning: {rec_scan}")
    except Exception as e:
        print(f"ID: {lbid} | ERROR: {e}")
    time.sleep(0.5)
