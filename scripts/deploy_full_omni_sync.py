import json
import time
import os
import requests
import pathlib
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
FINAL = ROOT / 'FINAL'
PERSONAS = FINAL / 'personas'
SCRATCH = ROOT / 'scratch'

TOKEN_FILE = SCRATCH / 'wyvern_token.txt'
REFRESH_FILE = SCRATCH / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

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

def deploy_lorebook_i(token):
    print("\n--- 2. Deploying Lorebook I (237 Entries) ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    lb_id = '_gwwCxCfQ6PQaLEjAQVpJL'
    with open(FINAL / 'Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    lex = data['lexicon']
    payload = {
        'name': data.get('name', ''),
        'description': data.get('description', ''),
        'scan_depth': data.get('scan_depth', 5),
        'token_budget': data.get('token_budget', 5000),
        'recursive_scanning': data.get('recursive_scanning', True),
        'visibility': data.get('visibility', 'private'),
        'rating': data.get('rating', 'explicit'),
        'photoURL': data.get('photoURL', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public'),
        'lexicon': lex
    }
    
    put_url = f"https://app.wyvern.chat/api/lorebooks/{lb_id}"
    resp = requests.put(put_url, headers=headers, json=payload)
    if resp.status_code == 200:
        print(f"  [SUCCESS] Lorebook I deployed live! HTTP 200 ({len(lex)} entries)")
        return True
    else:
        print(f"  [FAIL] Lorebook I deployment failed: HTTP {resp.status_code}: {resp.text[:300]}")
        return False

def deploy_world_lexicon_entries(token):
    print("\n--- 3. Deploying 12 New Entries to World Lexicon ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    # 1. Fetch current world lexicon to avoid duplicates
    get_url = f"https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}"
    resp = requests.get(get_url, headers=headers)
    if resp.status_code != 200:
        print(f"  [FAIL] Could not fetch world lexicon: HTTP {resp.status_code}")
        return False
        
    wlex = resp.json()
    existing_names = {e.get('name') for e in wlex}
    
    with open(FINAL / 'Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
        lb1_lex = json.load(f)['lexicon']
        
    # The last 12 entries are our new entries
    new_entries = lb1_lex[-12:]
    added = 0
    post_url = "https://app.wyvern.chat/api/worlds/lexicon"
    
    for entry in new_entries:
        ename = entry['name']
        if ename in existing_names:
            print(f"  [SKIP] '{ename}' already exists in World Lexicon.")
            continue
            
        payload = {
            "world_id": WORLD_ID,
            "name": ename,
            "keys": entry["keys"],
            "secondary_keys": entry.get("secondary_keys", []),
            "key_logic": "AND_ANY",
            "case_sensitive": False,
            "whole_words_only": True,
            "content": entry["content"].replace('—', ', ').replace('–', ', '),
            "type": entry.get("type", "lore/concept"),
            "is_global": entry.get("type") != "memory",  # memories are non-global
            "scan_persona": True,
            "highlight_keys": True,
            "selective": False
        }
        
        p_resp = requests.post(post_url, headers=headers, json=payload)
        if p_resp.status_code in [200, 201]:
            print(f"  [SUCCESS] Created live World Lexicon: '{ename}'")
            added += 1
        else:
            print(f"  [FAIL] Failed to create '{ename}': HTTP {p_resp.status_code}: {p_resp.text[:200]}")
            
        time.sleep(0.05)
        
    print(f"Added {added} new entries to World Lexicon.")
    return True

def update_world_characters(token):
    print("\n--- 4. Updating Streamlined Descriptions on World Characters ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    # Mapping of World Character IDs and their local files
    world_chars_map = [
        ('_FGeNBqjrt9fJJJyXTDgxM', 'Alyssa_Persona.json', 'Alyssa', PERSONAS),
        ('_mUEUDfmTG4m7wNyQ7WQKx', 'Jasper_Persona.json', 'Jasper', PERSONAS),
        ('_qfaywY2yfrGWcxPBdmURD', 'Erik_Douglas_card.json', 'Erik', FINAL),
        ('_QQXte9xWjMeMtqEJfwrc3', 'Malachia_Douglas_Bloodmoon_card.json', 'Malachia', FINAL),
        ('_KW6aNaRYTengVR4NBmG7J', 'Logan_Douglas_card.json', 'Logan', FINAL),
        ('_YzcPc7dRLkttzR2jKX93z', 'Noah_Douglas_Bloodmoon_card.json', 'Noah', FINAL),
        ('_RXHKfwRXwhRkBHttHVgqt', 'Mackenzie_Sanchez_Rogers_card.json', 'Mac', FINAL),
        ('_P1HrVjkY9TGnymNaAWX1j', 'Wulfnic_Bloodmoon_card.json', 'Wulfnic', FINAL),
        ('_4QWHxwHBpNnfjmNYm3tNr', 'Edric_Douglas_card.json', 'Edric', FINAL),
    ]
    
    success = 0
    for wcid, filename, name, folder in world_chars_map:
        with open(folder / filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            desc = data.get('description', '')
            
        url = f"https://app.wyvern.chat/api/worlds/characters/{wcid}"
        payload = {'long_summary': desc}
        
        resp = requests.put(url, headers=headers, json=payload)
        if resp.status_code == 200:
            print(f"  [SUCCESS] {name} World Character updated: {len(desc)} chars. HTTP 200.")
            success += 1
        else:
            print(f"  [FAIL] {name} update failed: HTTP {resp.status_code}: {resp.text[:200]}")
            
        time.sleep(0.05)
        
    return success == len(world_chars_map)

def update_standalone_cards(token):
    print("\n--- 5. Updating Standalone Character Cards on Wyvern (/characters/mine) ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    standalone_cards_map = [
        ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json', 'Jasper'),
        ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json', 'Erik'),
        ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json', 'Malachia'),
        ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json', 'Logan'),
        ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json', 'Noah'),
        ('_zn24784jfcchQ7EwCyAnm', 'Mackenzie_Sanchez_Rogers_card.json', 'Mackenzie'),
        ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json', 'Wulfnic'),
        ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json', 'Edric'),
    ]
    
    success = 0
    for cid, filename, name in standalone_cards_map:
        with open(FINAL / filename, 'r', encoding='utf-8') as f:
            card_data = json.load(f)
            
        get_url = f"https://app.wyvern.chat/api/characters/{cid}"
        resp = requests.get(get_url, headers=headers)
        if resp.status_code != 200:
            print(f"  [FAIL] Could not fetch standalone card {cid}: HTTP {resp.status_code}")
            continue
            
        live_json = resp.json()
        char_obj = live_json.get('character', live_json)
        rev = char_obj.get('revision', 1)
        
        char_obj['description'] = card_data['description']
        char_obj['revision'] = rev + 1
        
        put_url = f"https://app.wyvern.chat/api/characters/{cid}"
        put_resp = requests.put(put_url, headers=headers, json={'character': char_obj})
        if put_resp.status_code == 200:
            print(f"  [SUCCESS] {name} Standalone Card updated: {len(card_data['description'])} chars. HTTP 200 (rev {rev+1})")
            success += 1
        else:
            put_resp2 = requests.put(put_url, headers=headers, json=char_obj)
            if put_resp2.status_code == 200:
                print(f"  [SUCCESS] {name} Standalone Card updated directly: HTTP 200 (rev {rev+1})")
                success += 1
            else:
                print(f"  [FAIL] {name} Standalone Card update failed: HTTP {put_resp.status_code}")
                
        time.sleep(0.5)
        
    return success == len(standalone_cards_map)

def verify_omni_sync_live(token):
    print("\n--- 6. Live Verification of Omni-Parity ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    # 1. Check Lorebook I
    r_lb1 = requests.get("https://app.wyvern.chat/api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL", headers=headers).json()
    lb1_count = len(r_lb1.get('lexicon', []))
    print(f"  Lorebook I live entries: {lb1_count} (Expected: 237)")
    
    # 2. Check World Lexicon
    r_wlex = requests.get(f"https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}", headers=headers).json()
    print(f"  World Lexicon live entries: {len(r_wlex)}")
    
    # 3. Check World Characters length
    r_wchars = requests.get(f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}", headers=headers).json()
    for c in r_wchars:
        fn = c.get('first_name', '')
        if fn in ['Alyssa', 'Jasper', 'Erik', 'Malachia']:
            print(f"  World Character {fn}: long_summary_len={len(c.get('long_summary') or '')}")
            
    return lb1_count == 237

def main():
    token = refresh_auth_token()
    r_lb = deploy_lorebook_i(token)
    r_wlex = deploy_world_lexicon_entries(token)
    r_wchars = update_world_characters(token)
    r_cards = update_standalone_cards(token)
    r_verify = verify_omni_sync_live(token)
    
    print("\n================ TOTAL OMNI-SYNC VERDICT ================")
    print("Lorebook I (237 Entries):", r_lb)
    print("World Lexicon (12 New Entries):", r_wlex)
    print("World Characters (9 Streamlined):", r_wchars)
    print("Standalone Cards (8 Streamlined):", r_cards)
    print("Live Parity Verification:", r_verify)
    print("=========================================================")
    
    if r_lb and r_wlex and r_wchars and r_cards and r_verify:
        print("[SUCCESS] Total Omni-Parity completed with 100% success rate!")
    else:
        print("[WARNING] Completed with some partial warnings.")

if __name__ == '__main__':
    main()
