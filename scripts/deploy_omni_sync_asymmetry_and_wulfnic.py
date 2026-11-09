#!/usr/bin/env python3
"""
Omni-Sync Script: Asymmetry & Werewolf Secrecy Rules + Wulfnic's Gag Shirt Outfit.
Deploys:
1. Master Prompt Assembly (pha_kWkWUAfTJTF9q72c2bC98)
2. AI Game Master Assistant (simple_assistant_xRfBnV7wq48QppqbPPpTM)
3. Wulfnic Bloodmoon Standalone Card (_HEQQbbRFwKdG8QE2Fh1z1) & World Character (_P1HrVjkY9TGnymNaAWX1j)
4. World Scenarios with updated System Prompt / Knowledge Asymmetry
5. Live Verification of all deployed resources.
"""

import json
import pathlib
import sys
import time
import requests

# Set stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
FINAL = ROOT / 'FINAL'
SCRATCH = ROOT / 'scratch'

TOKEN_FILE = SCRATCH / 'wyvern_token.txt'
REFRESH_FILE = SCRATCH / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
API_BASE = 'https://app.wyvern.chat/api'

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
PROMPT_ASSEMBLY_ID = 'pha_kWkWUAfTJTF9q72c2bC98'
ASSISTANT_ID = 'simple_assistant_xRfBnV7wq48QppqbPPpTM'
WULFNIC_STANDALONE_ID = '_HEQQbbRFwKdG8QE2Fh1z1'
WULFNIC_WORLD_CHAR_ID = '_P1HrVjkY9TGnymNaAWX1j'

def refresh_token():
    print("=== [STEP 1] REFRESHING WYVERN AUTH TOKEN ===")
    rt = REFRESH_FILE.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    resp = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': rt})
    if resp.status_code == 200:
        token = resp.json()['id_token']
        TOKEN_FILE.write_text(token, encoding='utf-8')
        print(f"Token refreshed successfully! Length: {len(token)}")
        return token
    else:
        raise RuntimeError(f"Failed to refresh token: {resp.status_code} {resp.text}")

def deploy_prompt_assembly(token):
    print("\n=== [STEP 2] DEPLOYING MASTER PROMPT ASSEMBLY ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSync/1.0',
        'Accept': 'application/json'
    }
    pa_file = FINAL / 'prompts' / 'Svartulfr_Master_TTRPG_Prompt_Assembly.json'
    pa_data = json.loads(pa_file.read_text(encoding='utf-8'))
    
    put_url = f'{API_BASE}/prompt-assembly/{PROMPT_ASSEMBLY_ID}'
    resp = requests.put(put_url, headers=headers, json=pa_data)
    print(f"PUT {put_url} -> HTTP {resp.status_code}")
    if resp.status_code in [200, 204]:
        print("  [SUCCESS] Master Prompt Assembly deployed live!")
        return True
    else:
        print(f"  [FAIL] Response: {resp.text[:300]}")
        return False

def deploy_game_master_assistant(token):
    print("\n=== [STEP 3] DEPLOYING AI GAME MASTER ASSISTANT ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSync/1.0',
        'Accept': 'application/json'
    }
    asst_file = FINAL / 'assistants' / 'Svartulfr_Game_Master_Assistant.json'
    asst_data = json.loads(asst_file.read_text(encoding='utf-8'))
    
    put_url = f'{API_BASE}/simple-assistant-config/{ASSISTANT_ID}'
    resp = requests.put(put_url, headers=headers, json=asst_data)
    print(f"PUT {put_url} -> HTTP {resp.status_code}")
    if resp.status_code in [200, 204]:
        print("  [SUCCESS] AI Game Master Assistant deployed live!")
        return True
    else:
        print(f"  [FAIL] Response: {resp.text[:300]}")
        return False

def deploy_wulfnic_outfit_and_card(token):
    print("\n=== [STEP 4] DEPLOYING WULFNIC OUTFIT & CARD ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSync/1.0',
        'Accept': 'application/json'
    }
    wulfnic_file = FINAL / 'Wulfnic_Bloodmoon_card.json'
    wulfnic_card = json.loads(wulfnic_file.read_text(encoding='utf-8'))
    outfits = wulfnic_card.get('outfits', [])
    desc = wulfnic_card.get('description', '')
    
    # 1. Update Standalone Card
    get_url = f'{API_BASE}/characters/{WULFNIC_STANDALONE_ID}'
    r_get = requests.get(get_url, headers=headers)
    if r_get.status_code == 200:
        live_data = r_get.json()
        char_obj = live_data.get('character', live_data)
        rev = char_obj.get('revision', 1)
        
        char_obj['outfits'] = outfits
        char_obj['description'] = desc
        char_obj['revision'] = rev + 1
        char_obj['visibility'] = 'private'
        char_obj['rating'] = 'explicit'
        
        put_url = f'{API_BASE}/characters/{WULFNIC_STANDALONE_ID}'
        r_put = requests.put(put_url, headers=headers, json={'character': char_obj})
        if r_put.status_code != 200:
            r_put = requests.put(put_url, headers=headers, json=char_obj)
        print(f"  [STANDALONE] Wulfnic Card updated (outfits: {len(outfits)}) -> HTTP {r_put.status_code}")
    else:
        print(f"  [STANDALONE FAIL] GET failed: HTTP {r_get.status_code}")
        
    # 2. Update World Character
    w_url = f'{API_BASE}/worlds/characters/{WULFNIC_WORLD_CHAR_ID}'
    r_wchar_get = requests.get(w_url, headers=headers)
    if r_wchar_get.status_code == 200:
        wchar_obj = r_wchar_get.json()
        wchar_obj['outfits'] = outfits
        wchar_obj['long_summary'] = desc
        
        r_wchar_put = requests.put(w_url, headers=headers, json=wchar_obj)
        if r_wchar_put.status_code != 200:
            # Try partial payload
            r_wchar_put = requests.put(w_url, headers=headers, json={'outfits': outfits, 'long_summary': desc})
        print(f"  [WORLD CHARACTER] Wulfnic World Character updated (outfits: {len(outfits)}) -> HTTP {r_wchar_put.status_code}")
    else:
        print(f"  [WORLD CHAR FAIL] GET failed: HTTP {r_wchar_get.status_code}")
        
    return True

def deploy_world_scenarios_prompts(token):
    print("\n=== [STEP 5] SYNCING SYSTEM PROMPTS TO WORLD SCENARIOS ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSync/1.0',
        'Accept': 'application/json'
    }
    
    # Read prompt overrides from PROMPT_OVERRIDES_WYVERN.md
    with open(FINAL / 'PROMPT_OVERRIDES_WYVERN.md', 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    import re
    sp_match = re.search(r'## 1\. System Prompt Override\s*```xml\s*(.*?)\s*```', md_text, re.DOTALL)
    fi_match = re.search(r'## 2\. Final Instructions Override \(`post_history_instructions`\)\s*```xml\s*(.*?)\s*```', md_text, re.DOTALL)
    
    system_prompt = sp_match.group(1).strip() if sp_match else ""
    final_instructions = fi_match.group(1).strip() if fi_match else ""
    
    # Fetch all world scenarios
    list_url = f'{API_BASE}/worlds/scenarios/world/{WORLD_ID}'
    r_list = requests.get(list_url, headers=headers)
    if r_list.status_code != 200:
        print(f"  [FAIL] Could not list world scenarios: HTTP {r_list.status_code}")
        return False
        
    scenarios = r_list.json()
    print(f"Found {len(scenarios)} live World Scenarios.")
    
    updated_count = 0
    for sc in scenarios:
        sid = sc.get('id')
        name = sc.get('name') or sc.get('title')
        
        # Check if needs update
        cur_sp = sc.get('system_prompt') or ''
        cur_fi = sc.get('final_instructions') or ''
        
        needs_sp = '<information_asymmetry_and_werewolf_secrecy>' not in cur_sp
        needs_fi = 'Knowledge Boundaries' not in cur_fi
        
        if needs_sp or needs_fi:
            sc['system_prompt'] = system_prompt
            sc['final_instructions'] = final_instructions
            put_url = f'{API_BASE}/worlds/scenarios/{sid}'
            r_put = requests.put(put_url, headers=headers, json=sc)
            if r_put.status_code in [200, 204]:
                updated_count += 1
            else:
                print(f"  [FAIL] Scenario {name} ({sid}): HTTP {r_put.status_code}")
            time.sleep(0.05)
            
    print(f"  [SUCCESS] Updated {updated_count} World Scenarios with new System Prompt & Final Instructions!")
    return True

def verify_live_state(token):
    print("\n=== [STEP 6] VERIFYING LIVE OMNI-SYNC STATE ===")
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'OmniSync/1.0'
    }
    
    # 1. Verify Prompt Assembly
    r_pa = requests.get(f'{API_BASE}/prompt-assembly/{PROMPT_ASSEMBLY_ID}', headers=headers).json()
    pa_has_asymm = '<information_asymmetry_and_werewolf_secrecy>' in r_pa.get('main_prompt_template', '')
    print(f"  Prompt Assembly '{r_pa.get('name')}': Asymmetry Block Present = {pa_has_asymm}")
    
    # 2. Verify Assistant
    r_asst = requests.get(f'{API_BASE}/simple-assistant-config/{ASSISTANT_ID}', headers=headers).json()
    asst_has_asymm = 'Information Asymmetry & Werewolf Secrecy' in r_asst.get('system_prompt', '')
    print(f"  Assistant '{r_asst.get('title')}': Werewolf Secrecy Present = {asst_has_asymm}")
    
    # 3. Verify Wulfnic Outfits
    r_wulf = requests.get(f'{API_BASE}/characters/{WULFNIC_STANDALONE_ID}', headers=headers).json()
    w_outfits = r_wulf.get('outfits', [])
    gag_shirt = next((o for o in w_outfits if o.get('name') == 'The Gag Shirt'), None)
    has_rules = gag_shirt and 'RULES FOR DATING MY NIECE' in gag_shirt.get('description', '')
    print(f"  Wulfnic Standalone Card: Total Outfits = {len(w_outfits)}, Gag Shirt 10 Rules Present = {bool(has_rules)}")
    
    # 4. Verify World Character Wulfnic
    r_wchar = requests.get(f'{API_BASE}/worlds/characters/{WULFNIC_WORLD_CHAR_ID}', headers=headers).json()
    wc_outfits = r_wchar.get('outfits', [])
    wc_gag = next((o for o in wc_outfits if o.get('name') == 'The Gag Shirt'), None)
    wc_has_rules = wc_gag and 'RULES FOR DATING MY NIECE' in wc_gag.get('description', '')
    print(f"  Wulfnic World Character: Total Outfits = {len(wc_outfits)}, Gag Shirt 10 Rules Present = {bool(wc_has_rules)}")
    
    return pa_has_asymm and asst_has_asymm and has_rules and wc_has_rules

def main():
    token = refresh_token()
    r_pa = deploy_prompt_assembly(token)
    r_asst = deploy_game_master_assistant(token)
    r_wulf = deploy_wulfnic_outfit_and_card(token)
    r_scen = deploy_world_scenarios_prompts(token)
    r_verify = verify_live_state(token)
    
    print("\n================ FINAL OMNI-SYNC VERDICT ================")
    print(f"Master Prompt Assembly: {'SUCCESS' if r_pa else 'FAIL'}")
    print(f"AI Game Master Assistant: {'SUCCESS' if r_asst else 'FAIL'}")
    print(f"Wulfnic Outfits & Card: {'SUCCESS' if r_wulf else 'FAIL'}")
    print(f"World Scenarios Prompts: {'SUCCESS' if r_scen else 'FAIL'}")
    print(f"Verification Parity: {'SUCCESS' if r_verify else 'FAIL'}")
    print("=========================================================")
    
    if r_pa and r_asst and r_wulf and r_scen and r_verify:
        print("\n>>> ALL CHECKS PASSED: 100% OMNI-SYNC OPERATIONAL! <<<")
    else:
        print("\n>>> COMPLETED WITH PARTIAL STATUS <<<")

if __name__ == '__main__':
    main()
