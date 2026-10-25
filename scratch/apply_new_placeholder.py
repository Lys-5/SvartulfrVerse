import json, time, requests, sys

OLD_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"
NEW_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public"

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

def update_lorebook(filename, lb_id):
    path_final = f"FINAL/{filename}"
    path_opt = f"lorebooks/optimized/{filename}"
    
    data = json.load(open(path_final, encoding='utf-8'))
    lex = data.get('lexicon', [])
    replaced = 0
    for e in lex:
        if e.get('avatar') == OLD_URL:
            e['avatar'] = NEW_URL
            replaced += 1
            
    print(f"[{filename}] Replaced {replaced} avatar placeholders with NEW_URL.")
    data['lexicon'] = lex
    data['entries'] = lex
    
    with open(path_final, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    with open(path_opt, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    # Deploy via API
    payload = {
        'name': data.get('name', ''),
        'description': data.get('description', ''),
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'lexicon': lex
    }
    
    print(f"Deploying {filename} to Wyvern API ({lb_id})...")
    resp = requests.put(f"https://app.wyvern.chat/api/lorebooks/{lb_id}", headers=headers, json=payload)
    print(f"PUT response: {resp.status_code}")
    if resp.status_code != 200:
        print("Error:", resp.text[:200])
        sys.exit(1)
        
    time.sleep(2.5)
    
    # Verification GET
    v_resp = requests.get(f"https://app.wyvern.chat/api/lorebooks/{lb_id}", headers=headers).json()
    v_lex = v_resp.get('lexicon', [])
    v_new_count = sum(1 for e in v_lex if e.get('avatar') == NEW_URL)
    print(f"Verified live {filename}: total entries={len(v_lex)}, with NEW_URL={v_new_count}")

def main():
    print("=== UPDATING NPC PLACEHOLDER AVATARS ACROSS PRIMARY & SECONDARY ===")
    
    # 1. NPC Primary (_zwEqgEEzh12X6gHVmMKKC)
    update_lorebook("Svartulfr_NPC_Primary.json", "_zwEqgEEzh12X6gHVmMKKC")
    
    # 2. NPC Secondary (_Uht3Ckz44JBDrPnUHq7LV)
    update_lorebook("Svartulfr_NPC_Secondary.json", "_Uht3Ckz44JBDrPnUHq7LV")
    
    print("\n=== ALL NPC PLACEHOLDERS UPDATED & DEPLOYED SUCCESSFULLY ===")

if __name__ == '__main__':
    main()
