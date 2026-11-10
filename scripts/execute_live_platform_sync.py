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

TOKEN_FILE = SCRATCH / 'wyvern_token.txt'
REFRESH_FILE = SCRATCH / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'

def refresh_token():
    print("=== [1] REFRESHING AUTHENTICATION TOKEN ===")
    rt = REFRESH_FILE.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    resp = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': rt})
    if resp.status_code == 200:
        token = resp.json()['id_token']
        TOKEN_FILE.write_text(token, encoding='utf-8')
        print(f"Token refreshed successfully! (len={len(token)})")
        return token
    else:
        raise RuntimeError(f"Failed to refresh token: HTTP {resp.status_code} {resp.text}")

def deploy_lorebooks(token):
    print("\n=== [2] SYNCHRONIZING STANDALONE LOREBOOKS TO LIVE WYVERN ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    lorebooks_map = [
        ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 'Lorebook I (Casate & Lore)'),
        ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 'Lorebook II (Contratti & DDM)'),
        ('_9zWTGqYJNJ4BCDMj8gfcD', 'Svartulfr_Lorebook_III.json', 'Lorebook III (SUCC Campus)'),
        ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary (Main Dossiers)'),
        ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary (Batch 115)'),
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
            print(f"  -> SUCCESS! HTTP 200. {name} live on Wyvern.")
            results[name] = True
        else:
            print(f"  -> FAILED: HTTP {resp.status_code}: {resp.text[:200]}")
            results[name] = False
            
        time.sleep(1.0)
        
    return results

def deploy_mackenzie_modern(token):
    print("\n=== [3] SYNCHRONIZING MACKENZIE SANCHEZ-ROGERS (MODERNA: 204 CM & 9 OUTFITS) ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    # 1. Standalone Card (_zn24784jfcchQ7EwCyAnm)
    card_id = '_zn24784jfcchQ7EwCyAnm'
    card_path = FINAL / 'Mackenzie_Sanchez_Rogers_card.json'
    with open(card_path, 'r', encoding='utf-8') as f:
        card_data = json.load(f)
        
    get_url = f"https://app.wyvern.chat/api/characters/{card_id}"
    resp = requests.get(get_url, headers=headers)
    if resp.status_code != 200:
        print(f"  -> FAIL: Could not fetch live card {card_id}: HTTP {resp.status_code}")
        return False
        
    live_json = resp.json()
    char_obj = live_json.get('character', live_json)
    rev = char_obj.get('revision', 1)
    
    # Update fields
    char_obj['description'] = card_data['description']
    char_obj['personality'] = card_data.get('personality', card_data.get('summary', ''))
    char_obj['post_history_instructions'] = card_data['post_history_instructions']
    if 'outfits' in card_data:
        char_obj['outfits'] = card_data['outfits']
    char_obj['revision'] = rev + 1
    
    put_url = f"https://app.wyvern.chat/api/characters/{card_id}"
    put_resp = requests.put(put_url, headers=headers, json={'character': char_obj})
    if put_resp.status_code == 200:
        print(f"  -> SUCCESS! Standalone Card '{char_obj.get('name')}' updated: 204 cm, 9 outfits. HTTP 200 (rev {rev+1})")
    else:
        # Fallback without wrapping in 'character'
        put_resp2 = requests.put(put_url, headers=headers, json=char_obj)
        if put_resp2.status_code == 200:
            print(f"  -> SUCCESS! Standalone Card '{char_obj.get('name')}' updated directly. HTTP 200 (rev {rev+1})")
        else:
            print(f"  -> FAIL Standalone Card: HTTP {put_resp.status_code}: {put_resp.text[:200]}")
            
    # 2. World Character (_RXHKfwRXwhRkBHttHVgqt)
    wcid = '_RXHKfwRXwhRkBHttHVgqt'
    w_url = f"https://app.wyvern.chat/api/worlds/characters/{wcid}"
    w_payload = {'long_summary': card_data['description']}
    w_resp = requests.put(w_url, headers=headers, json=w_payload)
    if w_resp.status_code == 200:
        print(f"  -> SUCCESS! World Character Mac updated with 204 cm description. HTTP 200.")
    else:
        print(f"  -> FAIL World Character Mac: HTTP {w_resp.status_code}: {w_resp.text[:200]}")
        
    return True

def update_other_standalone_cards(token):
    print("\n=== [4] UPDATING OTHER STANDALONE CARDS (DDM ARC_LEVEL & TRAITS) ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }
    
    cards_to_sync = [
        ('_t4J9aQNJM36cUKAP4wB4U', 'Jasper_Douglas_Bloodmoon_card.json', 'Jasper'),
        ('_QPea6g4Q1QfeYCVHCLMPR', 'Erik_Douglas_card.json', 'Erik'),
        ('_RDfz7XzTpM23LpPALVXHM', 'Malachia_Douglas_Bloodmoon_card.json', 'Malachia'),
        ('_T8Ywcr9FEqNf9JxbK6eHP', 'Logan_Douglas_card.json', 'Logan'),
        ('_zFLUjV8aVxQRAfQxGcAcY', 'Noah_Douglas_Bloodmoon_card.json', 'Noah'),
        ('_HEQQbbRFwKdG8QE2Fh1z1', 'Wulfnic_Bloodmoon_card.json', 'Wulfnic'),
        ('_TbRM3EdxDjHFgqztTbCpL', 'Edric_Douglas_card.json', 'Edric'),
    ]
    
    for cid, filename, name in cards_to_sync:
        card_path = FINAL / filename
        with open(card_path, 'r', encoding='utf-8') as f:
            card_data = json.load(f)
            
        get_url = f"https://app.wyvern.chat/api/characters/{cid}"
        resp = requests.get(get_url, headers=headers)
        if resp.status_code != 200:
            print(f"  -> [SKIP] Could not fetch {name} ({cid}): HTTP {resp.status_code}")
            continue
            
        live_json = resp.json()
        char_obj = live_json.get('character', live_json)
        rev = char_obj.get('revision', 1)
        
        char_obj['description'] = card_data['description']
        char_obj['post_history_instructions'] = card_data['post_history_instructions']
        char_obj['revision'] = rev + 1
        
        put_url = f"https://app.wyvern.chat/api/characters/{cid}"
        put_resp = requests.put(put_url, headers=headers, json={'character': char_obj})
        if put_resp.status_code == 200:
            print(f"  -> SUCCESS! {name} standalone card synced. HTTP 200 (rev {rev+1})")
        else:
            put_resp2 = requests.put(put_url, headers=headers, json=char_obj)
            if put_resp2.status_code == 200:
                print(f"  -> SUCCESS! {name} standalone card synced directly. HTTP 200 (rev {rev+1})")
            else:
                print(f"  -> FAIL {name}: HTTP {put_resp.status_code}")
                
        time.sleep(0.5)

if __name__ == '__main__':
    tok = refresh_token()
    deploy_lorebooks(tok)
    deploy_mackenzie_modern(tok)
    update_other_standalone_cards(tok)
    print("\n🎉 AUTOMATIC SYNCHRONIZATION BATCH COMPLETE!")
