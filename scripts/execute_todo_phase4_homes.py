import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def api_put_character(character_id, payload, token):
    url = f"{API_BASE}/characters/{character_id}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

CHARACTER_HOMES = {
    # 1. DOUGLAS FAMILY & MAIN PACK (Villa Douglas: _9H2EmzRm92QxBpkmJUR1z)
    '_MXcEC8Y6B3BNm3b1ttHj6': '_9H2EmzRm92QxBpkmJUR1z',  # Alyssa Douglas Bloodmoon (already set)
    '_d44gDc8N18kkbEhAcfUCG': '_9H2EmzRm92QxBpkmJUR1z',  # Erik Douglas
    '_rAcN9GXD1Le4WxY28e49W': '_9H2EmzRm92QxBpkmJUR1z',  # Malachia Douglas Bloodmoon
    '_r42cVzMjcGTAx7bR1DQVt': '_9H2EmzRm92QxBpkmJUR1z',  # Noah Douglas Bloodmoon
    '_x3VY2kcbaDbKyCqywGeET': '_9H2EmzRm92QxBpkmJUR1z',  # Jasper Douglas Bloodmoon
    '_YJQ4cjdrT7brm7HWVkf3K': '_9H2EmzRm92QxBpkmJUR1z',  # Edric Douglas
    '_jeJTbxLcrYWXNWYPDx4ph': '_9H2EmzRm92QxBpkmJUR1z',  # Magnus Douglas III
    '_rJKYcCt61hQa8XRamHEdM': '_9H2EmzRm92QxBpkmJUR1z',  # Lord Cornelius Douglas
    '_EwPN1te7qtUKYEx4NLgag': '_9H2EmzRm92QxBpkmJUR1z',  # Elizabeth Duskwood

    # 2. LOGAN DOUGLAS (The Verve: _hfm1W4nYnXfQEqcNGwNxr)
    '_JL37wK9PQMNDChULCDrWj': '_hfm1W4nYnXfQEqcNGwNxr',  # Logan Douglas

    # 3. PRIMORDIAL FIRSTBORN & DEITY (Bloodmoon Longhouse: _RXULtwFjxCBUcxBbTfWrh)
    '_W9PLYt9ERTBJBXqKQL2en': '_RXULtwFjxCBUcxBbTfWrh',  # Wulfnic Bloodmoon
    '_NYtBzeKNkm3pedHMnYaka': '_RXULtwFjxCBUcxBbTfWrh',  # Ut Berg
    '_FJhtBq4xUM4aUWpaJAPYF': '_RXULtwFjxCBUcxBbTfWrh',  # Zefir Hvitskog
    '_fmzBDjDn3Gnq2hXKy7tY6': '_RXULtwFjxCBUcxBbTfWrh',  # Nixara Bloodmoon
    '_wpMTPQ2VVA2pWqJ3cMztJ': '_RXULtwFjxCBUcxBbTfWrh',  # Fenris

    # 4. DCC SECURITY & MILITARY (DCC Tower: _XD2gWgyhTYmDEXWkxMLer)
    '_b7QqV43D8pU1tewx4qenY': '_XD2gWgyhTYmDEXWkxMLer',  # Kaladin Nargathon
    '_PCC1PLfcGrdw2VfMnhVcL': '_XD2gWgyhTYmDEXWkxMLer',  # Marcus Thornfield

    # 5. DARKFIRE CLAN / HSK CONSULTING (The Cable District: _RVRf9PtEdwhGt3rGGFjMC)
    '_a6KYGdN3BWTgbYEbT4mx8': '_RVRf9PtEdwhGt3rGGFjMC',  # Zeera Darkfire
    '_aaWfLtx19WQR7JyHKDBem': '_RVRf9PtEdwhGt3rGGFjMC',  # Boros Darkfire
    '_Agf7FxKMzPDFJj3gktYtz': '_RVRf9PtEdwhGt3rGGFjMC',  # Karshin Darkfire
    '_8catGJE98MTpfaajJD9zV': '_RVRf9PtEdwhGt3rGGFjMC',  # Aras Darkfire
    '_bh8AHn7WKkNTnLjwXrUWE': '_RVRf9PtEdwhGt3rGGFjMC',  # Varg Darkfire
    '_Ht3kV76zrCE9tPmDAYh8Q': '_RVRf9PtEdwhGt3rGGFjMC',  # Yael

    # 6. BLACKWOOD CITY LEADERS & OLDTOWN / DISTRICTS
    '_9prjebmrgUC3zX3Qyew6a': '_D8B9QAfHPn3NfD4mAnJen',  # Roman Blackwood (Blackwood City)
    '_AjMH4N66RxKj2Pr84wqgz': '_D8B9QAfHPn3NfD4mAnJen',  # Harlan "Huck" Beaumont (Blackwood City)
    '_hzhkJ7n4FGXBxAHc6Eykj': '_Gnm9WMQNjhUWJLhrkpqQk',  # Marcus O'Connor (Oldtown)
    '_bbWxM1b7q2eRCWp7fYUVd': '_Gnm9WMQNjhUWJLhrkpqQk',  # Nicole O'Connor (Oldtown)
    '_Vd2Jat7DLhEXaGFzTTr3Y': '_Gnm9WMQNjhUWJLhrkpqQk',  # Federico "Riki" Savini (Oldtown)
    '_ejE6Xp83PhtJrDKCqbjhH': '_Gnm9WMQNjhUWJLhrkpqQk',  # Harrison Black (Oldtown)
    '_9J8jRp16w6NbjTWfeqTXy': '_Gnm9WMQNjhUWJLhrkpqQk',  # Marlowe Voss (Oldtown)

    # IRONWORKS & INDUSTRIAL
    '_QqYg238LKb4K6t3ERh4YD': '_fyC1LJ8CAK8rP7k8Dr2a2',  # Vito Marino (Ironworks)
    '_AycV4d9dJRBakCmdH4q4J': '_fyC1LJ8CAK8rP7k8Dr2a2',  # Brak Ironfist (Ironworks)
    '_fztKQyNBwtnPkcRjRYyXn': '_fyC1LJ8CAK8rP7k8Dr2a2',  # Eithne Dal'Kereth (Ironworks)

    # DOCKSIDE & THE HORNS
    '_7pEEWTeTLzd3ATh1y4FYd': '_B7Eq8K8CUXrCe9NKATXGE',  # Isobel Blackwater (Dockside)
    '_LEeEzdCCyGjQ8kfVkcra8': '_MxFzj8MUgHPXd8Y9m8hX4',  # Barrow (The Horns)

    # ARCADIA & UPTOWN
    '_yNt949MTQnVmCpVQq8ebF': '_X6R6dKTzkjdFk6cqdt2we',  # Helena Weiss (Arcadia)
    '_xDFyKfnKEfKWA9NdVhVV7': '_8fRJTJVkd7VjkQ3jfJWQ1',  # Naomi Black (Uptown)
    '_R6XD6qLdQTrm7F3nd2j1V': '_8fRJTJVkd7VjkQ3jfJWQ1',  # Darius Vale (Uptown)
    '_AyqP2RkHCKXPjDMK3bLUH': '_8fRJTJVkd7VjkQ3jfJWQ1',  # Cass Harrow (Uptown)

    # BLUEMOON
    '_A6Wmm1tCLybVYMqGeTckb': '_MkkwDR7AHq4tYLmnk134f',  # Aurora Night (Bluemoon)
    '_f3w1hw3qejBNjzNj8thqx': '_MkkwDR7AHq4tYLmnk134f',  # Eclipse Noir (Bluemoon)

    # PARADISE DISTRICT
    '_8wjMyUNV6yB7ACLk4dhWd': '_H6PUHPMMUEmM2wJbfd8et',  # Dominic Chen (Paradise)
    '_tEjWAbTqE6abw8UApDADw': '_H6PUHPMMUEmM2wJbfd8et',  # Bianca Rossi (Paradise)
    '_yYNA9Mxj2tyGNeT9VJzbh': '_H6PUHPMMUEmM2wJbfd8et',  # Ren (Paradise)

    # 7. TEAM UKIYO (Team Ukiyo Operational Base: _erHMcydnPVEyk7NY3K9wf)
    '_4bazKCAbPMmc19HzHAphC': '_erHMcydnPVEyk7NY3K9wf',  # Radek
    '_JQGgmwyA3qRaTLWck3GjX': '_erHMcydnPVEyk7NY3K9wf',  # Goran
    '_kc7TyfPDQwUALKXcmTMxQ': '_erHMcydnPVEyk7NY3K9wf',  # Kian

    # 8. DDM INC. & SINNERS / VOIDSPACE
    '_F8ee4UpyLr7Fyr69KKhzV': '_88QNj8BnFMN143XxNat1n',  # Dullahan (Dullahan's Condo)
    '_Mwqxw2M1NaxwXgTmxEXGr': '_qBt3jf1kppwrmMwTBbYJB',  # Zero (The Dead Dog Motel)
    '_NEw34RqyjnJHBApGXrt2M': '_qBt3jf1kppwrmMwTBbYJB',  # Raymond (The Dead Dog Motel)
    '_jf8fr4B9TNxbERGnEcd6b': '_qBt3jf1kppwrmMwTBbYJB',  # GREED - Roxie (The Dead Dog Motel)
    '_GEwyNtNGLVGjywcntBnLm': '_qBt3jf1kppwrmMwTBbYJB',  # GLUTTONY - Kevin (The Dead Dog Motel)
    '_VAqqYVbLbhaDbdkrw8Cyn': '_qBt3jf1kppwrmMwTBbYJB',  # ENVY - Siobhan (The Dead Dog Motel)
    '_23CNCRPX7rkcLbX8hbxGr': '_yqQeB1GzKJyqfwjUPRP2M',  # Jean-Luc Virtuoso (Beverly Hills)
    '_8CCMxWyPxRBaC1f2ycDqe': '_yqQeB1GzKJyqfwjUPRP2M',  # Alicia Virtuoso (Beverly Hills)
    '_aRzJCwP9EwgHMbCytNAJc': '_X4A8gWVr43a7dRr9TbJ4m',  # Dr. Arthur Sinclair (Los Angeles)
    '_bKApUbVDFUMdyKc1gyr4L': '_pTqkAfBAEFUtEA3BqUjRz',  # Dante (Hollywood)

    # 9. BALLANTINE FAMILY (Rory's Estate: _TLEaxwQCB24kQYfYHy8pq)
    '_13rj1V7hPaJ2QederUYkx': '_TLEaxwQCB24kQYfYHy8pq',  # Ruaraidh "Rory" Ballantine
    '_E7kHtwcpVYedVkVTmMGKX': '_TLEaxwQCB24kQYfYHy8pq',  # Sullivan "Sully" Jones
    '_VGAN3gQXchpTC2VFAcKUH': '_TLEaxwQCB24kQYfYHy8pq',  # Daniel "Danny" Boone
    '_F4qM3efBRVyQnXXUxVqH7': '_TLEaxwQCB24kQYfYHy8pq',  # Harper Aries

    # 10. IRONHORN NOMADS / BIKERS (Club House Ironhorn Nomads: _DJxYBCM7rNrXMj1WracGM)
    '_cDx2yGNtVbCCDUCHcUUxG': '_DJxYBCM7rNrXMj1WracGM',  # Marek

    # 11. THOMPSON FAMILY
    '_4GdzX4McREFg4zRpEqth2': '_UeKEhHTnCP6yQk7mhMVU1',  # Hank "Coach" Thompson (Coastal Residential)
    '_mfjaQDYUnAhLG8UggXg6N': '_UeKEhHTnCP6yQk7mhMVU1',  # Jasmin "Jas" Thompson (Coastal Residential)
    '_BzKwAkgpPfbVkBzbDaEth': '_Bx2U1xzg1D3wpFRe39L7y',  # Jared Thompson (Bulls Stadium)
    '_DKY9cDLMUaYpELYAdckH2': '_9YKj9HxFkRWnNJUJk84Tr',  # Janice Thompson (Artemis Dorms)

    # 12. GRAVE MISTAKE BAND
    '_mbBqR74dFceBFB4YegpyN': '_xfz8yrt2RjqHyTa8MXG3W',  # Fade Greymoor (Wyrm Dormitories)
    '_Tq76qk4hArR8WUej4Hxh8': '_9YKj9HxFkRWnNJUJk84Tr',  # Viola Carter (Artemis Dorms)
    '_2g1adXnHXcK62pVzGHUBm': '_wEkzHgpxfetQr16bTWNUP',  # Roland Vickers (Apollo Dorms)
    '_YY8VbpgzYk4dfFAL78rM3': '_wEkzHgpxfetQr16bTWNUP',  # Mackenzie Sanchez-Rogers (Apollo Dorms)

    # 13. SUCC STUDENTS & DORMS / FRATERNITIES
    '_U3JX1Xd9Um2ff4fA64wcr': '_Bx2U1xzg1D3wpFRe39L7y',  # Vincent Campbell (Bulls Stadium)
    '_acGaTVmCXxKDrTa6KNYzd': '_wEkzHgpxfetQr16bTWNUP',  # Andrew Campbell (Apollo Dorms)
    '_pbNb7PrEanM1twU612VNg': '_p1JatqFwBPeKPQrh6CmGe',  # Tomas Matthews (Beta Rho Omega)
    '_c643VDjNFzAMgj7xGKGXT': '_p1JatqFwBPeKPQrh6CmGe',  # Santiago Herrera (Beta Rho Omega)
    '_C18UjnQzGMLcQaNW3UaKq': '_wEkzHgpxfetQr16bTWNUP',  # Stanley Davies Jr. (Apollo Dorms)
    '_J3pEpeWqWFQBPtN3mjrDW': '_9YKj9HxFkRWnNJUJk84Tr',  # Sierra (Artemis Dorms)
    '_ykqALFc4CQN14zTrMQpat': '_tFj1yzTVDaEhdJLYe13YM',  # Scarlett Rose (Alpha Sigma Sigma)
    '_cmFQKKpC14U6qa4FtV9WK': '_9YKj9HxFkRWnNJUJk84Tr',  # Brittany Willow (Artemis Dorms)
    '_Rngxy8LRVnPqGqBamkjMW': '_9YKj9HxFkRWnNJUJk84Tr',  # Allegra Lumsden (Artemis Dorms)
    '_RQQcCAN4MHETcJLhXPe9k': '_xfz8yrt2RjqHyTa8MXG3W',  # Tate (Wyrm Dormitories)
    '_AdCJWrQaTgC7xkPQECrtK': '_xfz8yrt2RjqHyTa8MXG3W',  # Nikolaj Jökull (Wyrm Dormitories)
    '_RAPLVfmBbzaARYUpWGMga': '_xfz8yrt2RjqHyTa8MXG3W',  # Oskar (Wyrm Dormitories)
    '_4BPXYczVx9WratBCyJjfN': '_xLd2GzGayGJXUhjAdTPye',  # Dean (Additional Student Housing)
    '_68EgtxQCgFB8RNKqUbpxB': '_xLd2GzGayGJXUhjAdTPye',  # Eric (Additional Student Housing)
    '_RrLx1FeCAHzffm11fFMXz': '_wEkzHgpxfetQr16bTWNUP',  # Javier Reyes (Apollo Dorms)
    '_PQHGb4gL2LwDhNDrLFa3A': '_Bx2U1xzg1D3wpFRe39L7y',  # Finnegan Novak (Bulls Stadium)
    '_eF7HAqWkLLYhQwt2tm4rn': '_p1JatqFwBPeKPQrh6CmGe',  # Bailey Rogers (Beta Rho Omega)
    '_TLxzk97WmgYCA47nkDCVy': '_wEkzHgpxfetQr16bTWNUP',  # Chase Anderson (Apollo Dorms)
    '_k2hYW7HaWMzWHw2EpgVVF': '_3kFK6JCz9WEM2wGNRXnxq',  # Kolya Varenkov (Nocturnal Hall)
    '_QfcJQRWUV2yfHGUUjLD8V': '_CPWKPYwWeDY7ktNgBLWAy',  # Iordan R. Vess (Apartment C)
    '_8yfNebN71a73b3W84Nee1': '_3tNeXcGBfcUX6J1mtjqAw',  # Russ Sinclair (Claws Steel & Ink)
    '_DGkc2ALEYzNJ6mqGCW1KC': '_yXApVAkzqLrFkLkhW7fdU',  # Rev (Fraternity & Sorority Row)

    # 14. SUCC FACULTY & STAFF
    '_6hc62Ay9tVBXecnAfmqdU': '_hbH9FftNr3AzzVVDyJHgg',  # Archer Wolfwood (Archer Wolfwood Hall)
    '_E2A8prBrWg1q9zNjAR7kQ': '_j67Dp2PVwFCpdrfWRYV2M',  # Professor Loewe (SUCC Campus)
    '_14mG8nbb4Lh7AJ7ehGxcw': '_j67Dp2PVwFCpdrfWRYV2M',  # Professor Marit Christiansen (SUCC Campus)
    '_4rLXE2bVdJCWUNDeKat36': '_j67Dp2PVwFCpdrfWRYV2M',  # Professor Mollusk Moreau (SUCC Campus)
    '_wrcbW98qktK4gDFLTyC24': '_j67Dp2PVwFCpdrfWRYV2M',  # Hideo Reid (SUCC Campus)
    '_q1rYKHndN64QUgjHQazXB': '_G33ABhpFceN7HanHwp8rr',  # Ariadne Cirillo (Supernatural Support Center)
    '_EXFAYyRCjRU19eebCFfXz': '_Bx2U1xzg1D3wpFRe39L7y',  # Barkley Rover (Bulls Stadium)
    '_UczWkLKQ2td6jrJCR66Eb': '_Bx2U1xzg1D3wpFRe39L7y',  # Adelin Coso (Bulls Stadium)
    '_71Bc3wDdCkKmXD8EmLgFe': '_Caw9nRwKf4Gx9VzW21QJj',  # Coach Mithers (CUMS Campus)
    '_nBMDwWAEatHAggKWjNNCh': '_Dw9VQxmgEDGTyQdJzwJgG',  # Casey Williams (Arts Building)

    # 15. OTHER CIVILIANS & REGIONAL
    '_gqFXEaVj4aG9a8QL8R7f1': '_BgLjFRGNj9YX7tzybBzda',  # Stanley Davies Sr. (Solarton High School)
    '_q1n7hcz23ThY63JGEjdNq': '_UeKEhHTnCP6yQk7mhMVU1',  # Eris Davies (Coastal Residential)
    '_XthUhAMktzmFYAVeQbx6a': '_761mFFeCcQyR9JxhLCWcy',  # Luisa Sanchez Rogers (Solarton)
    '_dDXdeJrcYHbwagGFQVKQR': '_761mFFeCcQyR9JxhLCWcy',  # Dominic Rogers (Solarton)
    '_GBPCNEWLL2NmdaWAhg6Cn': '_6JEr2rqCjJa9tWzgbDcrb',  # Cassian Aralas (Hex Valley)
    '_c9RzyCnzzLey247dtph9x': '_QJUgPg6nGLqwdTgCL62NH',  # Bryson (Magick Research Labs)
    '_mwqYFKwWfHDMctDJQMR6w': '_L8UpkDzCNTFWH7gBWep2r',  # Angelo Moreno (Gallery)
    '_bVgKYYURnWGWdX142q99k': '_a2pRKBjYnQ1Q1LaN6xdeh',  # Abel Vilas (Solarton Public Beach)
}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    # Load master export to validate IDs and get names
    data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    char_dict = {c['id']: (c.get('display_name') or c.get('first_name')) for c in data['world_characters']}
    loc_dict = {l['id']: l['name'] for l in data['world_locations']}

    print(f"Verifica mapping: {len(CHARACTER_HOMES)} assegnazioni per {len(char_dict)} personaggi totali.")
    missing_chars = [cid for cid in char_dict if cid not in CHARACTER_HOMES]
    if missing_chars:
        print(f"ATTENZIONE: Mancano {len(missing_chars)} personaggi nel mapping!")
        for cid in missing_chars:
            print(f"  - {cid}: {char_dict[cid]}")
        sys.exit(1)

    invalid_locs = [lid for lid in CHARACTER_HOMES.values() if lid not in loc_dict]
    if invalid_locs:
        print(f"ERRORE: Ci sono location ID non valide: {invalid_locs}")
        sys.exit(1)

    print("Validazione completata: tutti i 110 personaggi sono mappati su location esistenti.\n")

    print("--- FASE 4: AGGIORNAMENTO DELLE HOME LOCATION SULLE CARD ---")
    success_count = 0
    error_count = 0

    for cid, lid in CHARACTER_HOMES.items():
        cname = char_dict[cid]
        lname = loc_dict[lid]
        try:
            res = api_put_character(cid, {'home_location_id': lid}, token)
            cur_home = res.get('home_location_id')
            if cur_home == lid:
                print(f"  [OK] {cname:30} -> {lname} ({lid})")
                success_count += 1
            else:
                print(f"  [WARN] {cname:30} -> Valore ritornato inatteso: {cur_home}")
        except Exception as e:
            print(f"  [ERRORE] {cname:30}: {e}")
            error_count += 1
        time.sleep(0.15)

    print(f"\n--- FASE 4 COMPLETATA: {success_count} aggiornati, {error_count} errori ---")

if __name__ == '__main__':
    main()
