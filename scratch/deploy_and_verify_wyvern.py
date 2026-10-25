import json
import pathlib
import time
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
TOKEN_FILE = ROOT / 'scratch' / 'wyvern_token.txt'

PRIMARY_ID = '_zwEqgEEzh12X6gHVmMKKC'
SECONDARY_ID = '_Uht3Ckz44JBDrPnUHq7LV'

def get_token():
    token = TOKEN_FILE.read_text(encoding='utf-8').strip()
    return token

def make_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }

def check_or_refresh_token():
    token = get_token()
    req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{PRIMARY_ID}',
        headers=make_headers(token),
        method='GET'
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status == 200:
                print("Token is valid and active.")
                return token
    except urllib.error.HTTPError as e:
        if e.code in [401, 403]:
            print(f"Token expired (HTTP {e.code}). Refreshing...")
            import sys
            sys.path.append(str(ROOT / 'scratch'))
            import refresh_token
            token = refresh_token.refresh()
            return token
        else:
            raise
    return token

def deploy_lorebook(lb_id, name, data, token):
    print(f"\n--- Deploying {name} ({lb_id}) ---")
    compact_payload = {
        'name': data.get('name'),
        'description': data.get('description', ''),
        'photoURL': data.get('photoURL'),
        'token_budget': data.get('token_budget'),
        'visibility': data.get('visibility', 'private'),
        'rating': data.get('rating', 'explicit'),
        'scan_depth': data.get('scan_depth', 5),
        'recursive_scanning': data.get('recursive_scanning', True),
        'lexicon': data.get('lexicon', [])
    }
    
    payload_bytes = json.dumps(compact_payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    print(f"Payload size: {len(payload_bytes):,} bytes | Lexicon entries: {len(compact_payload['lexicon'])}")
    
    req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{lb_id}',
        data=payload_bytes,
        headers=make_headers(token),
        method='PUT'
    )
    
    with urllib.request.urlopen(req, timeout=90) as resp:
        print(f"PUT Response Status: {resp.status}")
        res_data = resp.read()
        return resp.status

def verify_live(lb_id, name, expected_count, expected_budget, expected_cover, token):
    print(f"\n--- Verifying Live {name} ({lb_id}) ---")
    req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{lb_id}',
        headers=make_headers(token),
        method='GET'
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        print(f"GET Response Status: {resp.status}")
        data = json.loads(resp.read().decode('utf-8'))
        
    print(f"  Live Name: {data.get('name')}")
    print(f"  Live photoURL: {data.get('photoURL')}")
    print(f"  Live token_budget: {data.get('token_budget')}")
    lexicon = data.get('lexicon', [])
    print(f"  Live lexicon entry count: {len(lexicon)}")
    
    assert data.get('photoURL') == expected_cover, f"Cover mismatch: {data.get('photoURL')}"
    assert data.get('token_budget') == expected_budget, f"Token budget mismatch: {data.get('token_budget')}"
    assert len(lexicon) == expected_count, f"Entry count mismatch: {len(lexicon)} != {expected_count}"
    
    empty_avatars = [e.get('name') for e in lexicon if not e.get('avatar')]
    print(f"  Empty avatars count: {len(empty_avatars)}")
    assert len(empty_avatars) == 0, f"Found empty avatars: {empty_avatars}"
    
    # Check specific character entries
    lex_map = {e.get('entry_id'): e for e in lexicon}
    if lb_id == PRIMARY_ID:
        erik = lex_map.get('C-JisFj8qA1tsFEqZKevk')
        assert erik['type'] == 'npc', f"Erik type is {erik['type']}"
        assert len(erik['content']) == 22775, f"Erik content len: {len(erik['content'])}"
        logan = lex_map.get('tAcrWLtWSDGf3xJJRwUOM')
        assert logan['avatar'], "Logan avatar is still empty!"
        print(f"  -> Erik verified (type=npc, len=22775), Logan avatar restored ({logan['avatar'][:60]}...)")
    elif lb_id == SECONDARY_ID:
        edric = lex_map.get('h-ttmlgJYeRXqyDvQjSX7')
        assert edric['type'] == 'npc', f"Edric type is {edric['type']}"
        assert len(edric['content']) == 7240, f"Edric content len: {len(edric['content'])}"
        bruce = lex_map.get('NQd7n3QacMcK-TzowQ2LE')
        assert bruce['content'].startswith('['), "Bruce does not start with ["
        print(f"  -> Edric verified (type=npc, len=7240), Bruce verified ([...])")

def main():
    print("=== Wyvern API Deployment & Verification ===")
    token = check_or_refresh_token()
    
    with open(FINAL_DIR / 'Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
        prim_data = json.load(f)
    with open(FINAL_DIR / 'Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
        sec_data = json.load(f)
        
    HOUSE_EMBLEM = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"
    
    # 1. Deploy Primary
    status_prim = deploy_lorebook(PRIMARY_ID, "Svartúlfr - NPC Primary", prim_data, token)
    
    # 2. Pacing delay
    print("\nPacing delay: sleeping 2.5 seconds...")
    time.sleep(2.5)
    
    # 3. Deploy Secondary
    status_sec = deploy_lorebook(SECONDARY_ID, "Svartúlfr - NPC Secondary", sec_data, token)
    
    # 4. Pacing delay before verification
    print("\nPacing delay: sleeping 2.5 seconds...")
    time.sleep(2.5)
    
    # 5. Live GET Verification
    verify_live(PRIMARY_ID, "Svartúlfr - NPC Primary", 99, 7500, HOUSE_EMBLEM, token)
    verify_live(SECONDARY_ID, "Svartúlfr - NPC Secondary", 211, 5000, HOUSE_EMBLEM, token)
    
    print("\n=== ALL LIVE DEPLOYMENTS AND POST-DEPLOY VERIFICATIONS SUCCEEDED (HTTP 200 OK) ===")

if __name__ == '__main__':
    main()
