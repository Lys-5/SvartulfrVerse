import os
import sys
import json
import time
import urllib.request
import urllib.error
from collections import defaultdict

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from execute_todo_phase4_homes import CHARACTER_HOMES, api_put_character
from execute_todo_phase2_marketplaces import api_put_location

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'

G1_CORE_IDS = {
    '_d44gDc8N18kkbEhAcfUCG',  # Erik Douglas
    '_rAcN9GXD1Le4WxY28e49W',  # Malachia Douglas Bloodmoon
    '_r42cVzMjcGTAx7bR1DQVt',  # Noah Douglas Bloodmoon
    '_x3VY2kcbaDbKyCqywGeET',  # Jasper Douglas Bloodmoon
    '_MXcEC8Y6B3BNm3b1ttHj6',  # Alyssa Douglas Bloodmoon
    '_JL37wK9PQMNDChULCDrWj',  # Logan Douglas
    '_YJQ4cjdrT7brm7HWVkf3K',  # Edric Douglas
    '_W9PLYt9ERTBJBXqKQL2en',  # Wulfnic Bloodmoon
    '_FJhtBq4xUM4aUWpaJAPYF',  # Zefir Hvitskog
    '_NYtBzeKNkm3pedHMnYaka',  # Ut Berg
    '_jeJTbxLcrYWXNWYPDx4ph',  # Magnus Douglas III
    '_rJKYcCt61hQa8XRamHEdM',  # Lord Cornelius Douglas
    '_EwPN1te7qtUKYEx4NLgag',  # Elizabeth Duskwood
    '_b7QqV43D8pU1tewx4qenY',  # Kaladin Nargathon
    '_PCC1PLfcGrdw2VfMnhVcL',  # Marcus Thornfield
    '_fmzBDjDn3Gnq2hXKy7tY6',  # Nixara Bloodmoon
}

# Secondary hangouts & frequent locations for characters
SECONDARY_LOCATIONS = {
    # Students -> Campus hub, coffee shop, club, student union
    '_xfz8yrt2RjqHyTa8MXG3W': ['_aLqMW6UHHj1D9M4xxENF7', '_XUV6jWXTXG6wgj2WKBEpr', '_j67Dp2PVwFCpdrfWRYV2M'],  # Wyrm students
    '_wEkzHgpxfetQr16bTWNUP': ['_aLqMW6UHHj1D9M4xxENF7', '_XUV6jWXTXG6wgj2WKBEpr', '_VbjcwqJnc7BaED9A9t2Dq'],  # Apollo students
    '_9YKj9HxFkRWnNJUJk84Tr': ['_aLqMW6UHHj1D9M4xxENF7', '_XUV6jWXTXG6wgj2WKBEpr', '_VbjcwqJnc7BaED9A9t2Dq'],  # Artemis students
    '_p1JatqFwBPeKPQrh6CmGe': ['_Bx2U1xzg1D3wpFRe39L7y', '_VbjcwqJnc7BaED9A9t2Dq', '_WRBThTNK3wJawVdLRhA1e'],  # BRO Frat athletes
    '_tFj1yzTVDaEhdJLYe13YM': ['_VbjcwqJnc7BaED9A9t2Dq', '_aLqMW6UHHj1D9M4xxENF7', '_hGpPMY77NaH4j6AxNGLVe'],  # ASS Sorority
    '_xLd2GzGayGJXUhjAdTPye': ['_aLqMW6UHHj1D9M4xxENF7', '_XUV6jWXTXG6wgj2WKBEpr', '_hGpPMY77NaH4j6AxNGLVe'],  # Extra student housing
}

# Specific character secondary mappings
CHAR_SECONDARY_LOCS = {
    # Grave Mistake Band members -> perform at Sidewinders & The Verve
    '_mbBqR74dFceBFB4YegpyN': ['_VbjcwqJnc7BaED9A9t2Dq', '_hfm1W4nYnXfQEqcNGwNxr'],
    '_Tq76qk4hArR8WUej4Hxh8': ['_VbjcwqJnc7BaED9A9t2Dq', '_hfm1W4nYnXfQEqcNGwNxr'],
    '_2g1adXnHXcK62pVzGHUBm': ['_VbjcwqJnc7BaED9A9t2Dq', '_hfm1W4nYnXfQEqcNGwNxr'],
    '_YY8VbpgzYk4dfFAL78rM3': ['_VbjcwqJnc7BaED9A9t2Dq', '_hfm1W4nYnXfQEqcNGwNxr'],

    # SUCC Athletes
    '_BzKwAkgpPfbVkBzbDaEth': ['_EmJg3zdjTT8kwteJJkyUR', '_WRBThTNK3wJawVdLRhA1e'],
    '_U3JX1Xd9Um2ff4fA64wcr': ['_EmJg3zdjTT8kwteJJkyUR', '_WRBThTNK3wJawVdLRhA1e'],
    '_PQHGb4gL2LwDhNDrLFa3A': ['_EmJg3zdjTT8kwteJJkyUR', '_WRBThTNK3wJawVdLRhA1e'],
    '_acGaTVmCXxKDrTa6KNYzd': ['_Bx2U1xzg1D3wpFRe39L7y', '_Dw9VQxmgEDGTyQdJzwJgG'],

    # Darkfire Clan -> A&Co. and Bricklane Mall
    '_a6KYGdN3BWTgbYEbT4mx8': ['_R7Cz4Uah9Tjkn4KDC7rxM', '_hGpPMY77NaH4j6AxNGLVe'],
    '_aaWfLtx19WQR7JyHKDBem': ['_R7Cz4Uah9Tjkn4KDC7rxM', '_hGpPMY77NaH4j6AxNGLVe'],
    '_Agf7FxKMzPDFJj3gktYtz': ['_R7Cz4Uah9Tjkn4KDC7rxM', '_hGpPMY77NaH4j6AxNGLVe'],
    '_8catGJE98MTpfaajJD9zV': ['_R7Cz4Uah9Tjkn4KDC7rxM', '_hGpPMY77NaH4j6AxNGLVe'],
    '_bh8AHn7WKkNTnLjwXrUWE': ['_R7Cz4Uah9Tjkn4KDC7rxM'],
    '_Ht3kV76zrCE9tPmDAYh8Q': ['_erHMcydnPVEyk7NY3K9wf'],

    # Team Ukiyo -> Dungeon Rift & Ironworks
    '_4bazKCAbPMmc19HzHAphC': ['_CaKc8CcYADYxLRmb2GYpG', '_fyC1LJ8CAK8rP7k8Dr2a2'],
    '_JQGgmwyA3qRaTLWck3GjX': ['_CaKc8CcYADYxLRmb2GYpG', '_fyC1LJ8CAK8rP7k8Dr2a2'],
    '_kc7TyfPDQwUALKXcmTMxQ': ['_CaKc8CcYADYxLRmb2GYpG', '_hGpPMY77NaH4j6AxNGLVe'],

    # Sinners / DDM -> Underground Fighting Ring, Skid Row, Dead Dog Motel
    '_F8ee4UpyLr7Fyr69KKhzV': ['_Bx2U1xzg1D3wpFRe39L7y', '_qBt3jf1kppwrmMwTBbYJB'],
    '_Mwqxw2M1NaxwXgTmxEXGr': ['_gpBY7HGddd4KHfqaDyy3c', '_NqaNWcjcwHXmXFTptBEbP'],
    '_NEw34RqyjnJHBApGXrt2M': ['_gpBY7HGddd4KHfqaDyy3c', '_NqaNWcjcwHXmXFTptBEbP'],
    '_jf8fr4B9TNxbERGnEcd6b': ['_gpBY7HGddd4KHfqaDyy3c', '_NqaNWcjcwHXmXFTptBEbP'],
    '_GEwyNtNGLVGjywcntBnLm': ['_gpBY7HGddd4KHfqaDyy3c', '_NqaNWcjcwHXmXFTptBEbP'],
    '_VAqqYVbLbhaDbdkrw8Cyn': ['_yqQeB1GzKJyqfwjUPRP2M', '_pTqkAfBAEFUtEA3BqUjRz'],
    '_23CNCRPX7rkcLbX8hbxGr': ['_X4A8gWVr43a7dRr9TbJ4m', '_pTqkAfBAEFUtEA3BqUjRz'],
    '_8CCMxWyPxRBaC1f2ycDqe': ['_X4A8gWVr43a7dRr9TbJ4m', '_pTqkAfBAEFUtEA3BqUjRz'],
    '_bKApUbVDFUMdyKc1gyr4L': ['_yqQeB1GzKJyqfwjUPRP2M', '_qBt3jf1kppwrmMwTBbYJB'],

    # Ballantine Family -> Los Angeles & Beverly Hills
    '_13rj1V7hPaJ2QederUYkx': ['_X4A8gWVr43a7dRr9TbJ4m', '_yqQeB1GzKJyqfwjUPRP2M'],
    '_E7kHtwcpVYedVkVTmMGKX': ['_X4A8gWVr43a7dRr9TbJ4m', '_yqQeB1GzKJyqfwjUPRP2M'],
    '_VGAN3gQXchpTC2VFAcKUH': ['_X4A8gWVr43a7dRr9TbJ4m', '_yqQeB1GzKJyqfwjUPRP2M'],
    '_F4qM3efBRVyQnXXUxVqH7': ['_X4A8gWVr43a7dRr9TbJ4m', '_NqaNWcjcwHXmXFTptBEbP'],

    # Oldtown Wolves & Artisans -> Bricklane Mall & Old Cedar Clearing
    '_hzhkJ7n4FGXBxAHc6Eykj': ['_pA2pCqnF2FenCeHAmyd37', '_hGpPMY77NaH4j6AxNGLVe'],
    '_bbWxM1b7q2eRCWp7fYUVd': ['_pA2pCqnF2FenCeHAmyd37', '_hGpPMY77NaH4j6AxNGLVe'],
    '_Vd2Jat7DLhEXaGFzTTr3Y': ['_pA2pCqnF2FenCeHAmyd37', '_D8B9QAfHPn3NfD4mAnJen'],
    '_ejE6Xp83PhtJrDKCqbjhH': ['_hGpPMY77NaH4j6AxNGLVe'],
    '_9J8jRp16w6NbjTWfeqTXy': ['_jX3bYbn8FHra6qNYUC3Ux'],

    # Ironworks & Nomads
    '_QqYg238LKb4K6t3ERh4YD': ['_jABzFFNTGRdRLEkNYTKx2', '_DJxYBCM7rNrXMj1WracGM'],
    '_AycV4d9dJRBakCmdH4q4J': ['_jABzFFNTGRdRLEkNYTKx2'],
    '_fztKQyNBwtnPkcRjRYyXn': ['_jABzFFNTGRdRLEkNYTKx2', '_RVRf9PtEdwhGt3rGGFjMC'],
    '_cDx2yGNtVbCCDUCHcUUxG': ['_FrXnp2CALTP44CP3KVAhb', '_fyC1LJ8CAK8rP7k8Dr2a2'],

    # Paradise & Luxury
    '_8wjMyUNV6yB7ACLk4dhWd': ['_K1qQL7wBcWpkyyeyw76TU', '_4w7Npw7VkhbAyU1Qy1Wt2'],
    '_tEjWAbTqE6abw8UApDADw': ['_K1qQL7wBcWpkyyeyw76TU', '_4w7Npw7VkhbAyU1Qy1Wt2'],
    '_yYNA9Mxj2tyGNeT9VJzbh': ['_K1qQL7wBcWpkyyeyw76TU', '_4w7Npw7VkhbAyU1Qy1Wt2', '_hGpPMY77NaH4j6AxNGLVe'],

    # SUCC Faculty
    '_6hc62Ay9tVBXecnAfmqdU': ['_j67Dp2PVwFCpdrfWRYV2M', '_jYJxF7fte2Gz1F2HGXpUR'],
    '_E2A8prBrWg1q9zNjAR7kQ': ['_jYJxF7fte2Gz1F2HGXpUR', '_hbH9FftNr3AzzVVDyJHgg'],
    '_14mG8nbb4Lh7AJ7ehGxcw': ['_jYJxF7fte2Gz1F2HGXpUR', '_XUV6jWXTXG6wgj2WKBEpr'],
    '_4rLXE2bVdJCWUNDeKat36': ['_jYJxF7fte2Gz1F2HGXpUR', '_eq11xwGJqa9rHTtaBQTkL'],
    '_wrcbW98qktK4gDFLTyC24': ['_jYJxF7fte2Gz1F2HGXpUR', '_QJUgPg6nGLqwdTgCL62NH'],
    '_q1rYKHndN64QUgjHQazXB': ['_j67Dp2PVwFCpdrfWRYV2M', '_XUV6jWXTXG6wgj2WKBEpr'],
}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    # Load master export
    data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    char_dict = {c['id']: (c.get('display_name') or c.get('first_name')) for c in data['world_characters']}
    loc_dict = {l['id']: l['name'] for l in data['world_locations']}

    print("--- PARTE A: COSTRUZIONE DEI CHARACTER POOL PER LOCATION ---")
    location_pools = defaultdict(dict)  # loc_id -> {char_id: weight}

    # 1. Primary home location for all characters
    for cid, lid in CHARACTER_HOMES.items():
        if lid in loc_dict:
            location_pools[lid][cid] = 2

    # 2. Add group secondary locations
    for home_lid, sec_list in SECONDARY_LOCATIONS.items():
        # find characters whose home is home_lid
        chars_at_home = [cid for cid, hlid in CHARACTER_HOMES.items() if hlid == home_lid]
        for sec_lid in sec_list:
            if sec_lid in loc_dict:
                for cid in chars_at_home:
                    if cid not in location_pools[sec_lid]:
                        location_pools[sec_lid][cid] = 1

    # 3. Add specific secondary locations
    for cid, sec_list in CHAR_SECONDARY_LOCS.items():
        for sec_lid in sec_list:
            if sec_lid in loc_dict:
                location_pools[sec_lid][cid] = 1

    print(f"Generate distribuzioni per {len(location_pools)} location con roster NPC dedicato.")

    # Apply character pools to locations
    loc_success = 0
    loc_err = 0
    for lid, pool_dict in location_pools.items():
        lname = loc_dict.get(lid, lid)
        pool_payload = [
            {'character_id': cid, 'participation_weight': weight}
            for cid, weight in pool_dict.items()
        ]
        try:
            res = api_put_location(lid, {'included_character_pool': pool_payload}, token)
            cnt = len(res.get('included_character_pool', []))
            safe_lname = lname.encode('ascii', 'replace').decode('ascii')
            print(f"  [LOC OK] {safe_lname[:35]:35} ({lid}): {cnt} personaggi nel pool")
            loc_success += 1
        except Exception as e:
            safe_lname = lname.encode('ascii', 'replace').decode('ascii')
            print(f"  [LOC ERR] {safe_lname[:35]:35} ({lid}): {e}")
            loc_err += 1
        time.sleep(0.2)

    print(f"\nLocation Pools completati: {loc_success} successi, {loc_err} errori.\n")

    print("--- PARTE B: AGGIORNAMENTO DEL FLAG IS_GLOBAL SUI PERSONAGGI ---")
    print(f"16 G1 Core Cast: is_global = True")
    print(f"94 Non-G1 Characters: is_global = False\n")

    char_success = 0
    char_err = 0

    for cid, cname in char_dict.items():
        should_be_global = (cid in G1_CORE_IDS)
        safe_cname = cname.encode('ascii', 'replace').decode('ascii')
        try:
            res = api_put_character(cid, {'is_global': should_be_global}, token)
            val = res.get('is_global')
            status_str = "GLOBAL (G1)" if val else "LOCAL (NPC)"
            print(f"  [CHAR OK] {safe_cname[:30]:30} -> {status_str}")
            char_success += 1
        except Exception as e:
            print(f"  [CHAR ERR] {safe_cname[:30]:30}: {e}")
            char_err += 1
        time.sleep(0.15)

    print(f"\nFlag is_global completato: {char_success} aggiornati, {char_err} errori.")
    print("--- FASE 5 COMPLETATA CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
