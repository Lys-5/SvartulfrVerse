import json
import time
import requests

def main():
    token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    # 1. Location
    loc_id = '_EjXxkmPVhpCXg8xABpFkK'
    with open('FINAL/Svartulfr_Location.json', 'r', encoding='utf-8') as f:
        loc_data = json.load(f)

    payload_loc = {
        'name': loc_data.get('name', 'Svartúlfr - Location'),
        'description': loc_data.get('description', ''),
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'lexicon': loc_data['lexicon']
    }
    print(f"Deploying Location ({loc_id}) with {len(loc_data['lexicon'])} lexicon entries...")
    r_put_loc = requests.put(f'https://app.wyvern.chat/api/lorebooks/{loc_id}', headers=headers, json=payload_loc)
    print("PUT Location response status:", r_put_loc.status_code)
    if r_put_loc.status_code != 200:
        print("PUT Location Error:", r_put_loc.text[:500])
        return False

    time.sleep(2.5)

    # 2. NPC Secondary
    npc_id = '_Uht3Ckz44JBDrPnUHq7LV'
    with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
        npc_data = json.load(f)

    payload_npc = {
        'name': npc_data.get('name', 'Svartúlfr - NPC Secondary'),
        'description': npc_data.get('description', ''),
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'lexicon': npc_data['lexicon']
    }
    print(f"Deploying NPC Secondary ({npc_id}) with {len(npc_data['lexicon'])} lexicon entries...")
    r_put_npc = requests.put(f'https://app.wyvern.chat/api/lorebooks/{npc_id}', headers=headers, json=payload_npc)
    print("PUT NPC Secondary response status:", r_put_npc.status_code)
    if r_put_npc.status_code != 200:
        print("PUT NPC Secondary Error:", r_put_npc.text[:500])
        return False

    time.sleep(2.5)

    # 3. Verification GET
    print("\n--- Verifying Live Deployments ---")
    r_get_loc = requests.get(f'https://app.wyvern.chat/api/lorebooks/{loc_id}', headers=headers)
    print("GET Location status:", r_get_loc.status_code)
    if r_get_loc.status_code == 200:
        res = r_get_loc.json()
        live_lex = res.get('lexicon', [])
        print(f"Verified live Location entries count: {len(live_lex)}")
        # Check Moonflower & Ironwood
        for e in live_lex:
            t = e.get('comment') or e.get('name') or ''
            if 'Moonflower' in t:
                print(f"Live Moonflower found: {t}, keys={e.get('keys')[:3]}...")
            if 'Ironwood' in t:
                print(f"Live Ironwood found: {t}, keys={e.get('keys')[:3]}...")

    time.sleep(1.0)

    r_get_npc = requests.get(f'https://app.wyvern.chat/api/lorebooks/{npc_id}', headers=headers)
    print("GET NPC Secondary status:", r_get_npc.status_code)
    if r_get_npc.status_code == 200:
        res = r_get_npc.json()
        live_lex = res.get('lexicon', [])
        print(f"Verified live NPC Secondary entries count: {len(live_lex)}")
        for e in live_lex:
            c = e.get('comment') or ''
            if 'Rylan' in c:
                aff = [line for line in e.get('content', '').split('\n') if 'AFFILIATION' in line]
                print(f"Live Rylan found: {aff}")

    print("\nDEPLOYMENT AND VERIFICATION COMPLETED SUCCESSFULLY.")
    return True

if __name__ == '__main__':
    main()
