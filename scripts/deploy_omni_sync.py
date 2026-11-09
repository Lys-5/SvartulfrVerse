import json
import time
import os
import requests
import pathlib
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
FINAL = ROOT / 'FINAL'
OPT = ROOT / 'lorebooks' / 'optimized'

TOKEN_FILE = SCRATCH / 'wyvern_token.txt'
REFRESH_FILE = SCRATCH / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'

def refresh_auth_token():
    print("--- 1. Refreshing Wyvern Firebase Auth Token ---")
    rt = REFRESH_FILE.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    resp = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': rt})
    if resp.status_code == 200:
        token = resp.json()['id_token']
        TOKEN_FILE.write_text(token, encoding='utf-8')
        print(f"Token refreshed successfully (len={len(token)})")
        return token
    else:
        raise RuntimeError(f"Failed to refresh token: {resp.status_code} {resp.text}")

def deploy_lorebooks(token):
    print("\n--- 2. Deploying Standalone Lorebooks to Wyvern API ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    lorebooks_map = [
        ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 'Lorebook I'),
        ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 'Lorebook II'),
        ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartulfr_Lorebook_III.json', 'Lorebook III'),
        ('_EjXxkmPVhpCXg8xABpFkK', 'Svartulfr_Location.json', 'Location'),
        ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary'),
        ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary'),
    ]
    
    results = {}
    
    for lb_id, filename, name in lorebooks_map:
        file_path = FINAL / filename
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        lex = data.get('lexicon', data.get('entries', []))
        
        payload = {
            'name': data.get('name', ''),
            'description': data.get('description', ''),
            'scan_depth': data.get('scan_depth', 5),
            'token_budget': data.get('token_budget', 5000),
            'recursive_scanning': data.get('recursive_scanning', True),
            'visibility': data.get('visibility', 'private'),
            'rating': data.get('rating', 'explicit'),
            'photoURL': data.get('photoURL', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public'),
            'lexicon': lex,
            'entries': lex  # For strict Zod frontend validator parity
        }
        
        print(f"Deploying {name} ({lb_id}) with {len(lex)} entries...")
        put_url = f"https://app.wyvern.chat/api/lorebooks/{lb_id}"
        resp = requests.put(put_url, headers=headers, json=payload)
        
        if resp.status_code == 200:
            print(f"  [SUCCESS] {name} deployed. HTTP 200.")
            results[name] = True
        else:
            print(f"  [FAIL] {name} deployment failed: HTTP {resp.status_code}: {resp.text[:200]}")
            results[name] = False
            
        time.sleep(2.0)
        
    return results

def deploy_mackenzie_card(token):
    print("\n--- 3. Deploying Standalone Character Card: Mackenzie Sanchez-Rogers ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    card_id = '_zn24784jfcchQ7EwCyAnm'
    card_path = FINAL / 'Mackenzie_Sanchez_Rogers_card.json'
    with open(card_path, 'r', encoding='utf-8') as f:
        card_data = json.load(f)
        
    # Get current live revision
    get_url = f"https://app.wyvern.chat/api/characters/{card_id}"
    resp = requests.get(get_url, headers=headers)
    if resp.status_code != 200:
        print(f"  [FAIL] Could not fetch live card {card_id}: HTTP {resp.status_code}")
        return False
        
    live_json = resp.json()
    char_obj = live_json.get('character', live_json)
    rev = char_obj.get('revision', 1)
    print(f"Live Mackenzie card revision: {rev}")
    
    # Update post_history_instructions
    char_obj['post_history_instructions'] = card_data['post_history_instructions']
    char_obj['revision'] = rev + 1
    
    put_url = f"https://app.wyvern.chat/api/characters/{card_id}"
    put_resp = requests.put(put_url, headers=headers, json={'character': char_obj})
    if put_resp.status_code == 200:
        print(f"  [SUCCESS] Mackenzie card updated successfully! HTTP 200 (revision {rev+1})")
        return True
    else:
        # Some endpoints accept the character dict directly
        put_resp2 = requests.put(put_url, headers=headers, json=char_obj)
        if put_resp2.status_code == 200:
            print(f"  [SUCCESS] Mackenzie card updated directly! HTTP 200 (revision {rev+1})")
            return True
        else:
            print(f"  [FAIL] Mackenzie update failed: HTTP {put_resp.status_code}: {put_resp.text[:200]}")
            return False

def verify_live_lorebooks(token):
    print("\n--- 4. Live Verification of Standalone Lorebooks ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    lorebooks_map = [
        ('_gwwCxCfQ6PQaLEjAQVpJL', 'Lorebook I', 225),
        ('_HfG7TeV6MJyj6bxMwxkpt', 'Lorebook II', 142),
        ('_9zWTGqYJNJ4BCDMj8gfcD', 'Lorebook III', 46),
        ('_EjXxkmPVhpCXg8xABpFkK', 'Location', 225),
        ('_zwEqgEEzh12X6gHVmMKKC', 'NPC Primary', 99),
        ('_Uht3Ckz44JBDrPnUHq7LV', 'NPC Secondary', 211),
    ]
    
    all_ok = True
    for lb_id, name, expected_count in lorebooks_map:
        url = f"https://app.wyvern.chat/api/lorebooks/{lb_id}"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print(f"  [FAIL] {name}: HTTP {resp.status_code}")
            all_ok = False
            continue
            
        data = resp.json()
        lex_count = len(data.get('lexicon', []))
        if lex_count == expected_count:
            print(f"  [PASS] {name}: {lex_count}/{expected_count} entries live.")
        else:
            print(f"  [MISMATCH] {name}: found {lex_count}, expected {expected_count}")
            all_ok = False
            
    return all_ok

def main():
    token = refresh_auth_token()
    lb_results = deploy_lorebooks(token)
    mac_result = deploy_mackenzie_card(token)
    verify_ok = verify_live_lorebooks(token)
    
    print("\n================ OMNI-SYNC SUMMARY ================")
    print("Lorebooks Deployment:", all(lb_results.values()))
    print("Mackenzie Standalone Card:", mac_result)
    print("Live Lorebooks Count Verification:", verify_ok)
    print("====================================================")
    
    if all(lb_results.values()) and mac_result and verify_ok:
        print("[SUCCESS] All Omni-Parity /mine assets are 100% synchronized!")
    else:
        print("[WARNING] Some assets encountered issues during synchronization.")

if __name__ == '__main__':
    main()
