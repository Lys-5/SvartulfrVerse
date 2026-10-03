import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from execute_todo_phase2_marketplaces import api_put_location

PARENT_ASSIGNMENTS = {
    # Villa Douglas Sanctuary
    '_dGxRVH174qAfzykbyPTCD': '_9H2EmzRm92QxBpkmJUR1z',  # Alyssa's Omega Nest -> Villa Douglas
    
    # Paradise District Sub-locations
    '_RTxCmM7pKQGx8VVA83B7Q': '_H6PUHPMMUEmM2wJbfd8et',  # Eidolon Creative Private Suites -> Paradise
    '_K1qQL7wBcWpkyyeyw76TU': '_H6PUHPMMUEmM2wJbfd8et',  # L'Iris d'Oro -> Paradise

    # Blackwood City Regional Districts
    '_RVRf9PtEdwhGt3rGGFjMC': '_D8B9QAfHPn3NfD4mAnJen',  # The Cable District -> Blackwood City
    '_pA2pCqnF2FenCeHAmyd37': '_Gnm9WMQNjhUWJLhrkpqQk',  # Old Cedar Clearing -> Oldtown
    '_8VAgXXpyFkhEPEzdzj6T9': '_Gnm9WMQNjhUWJLhrkpqQk',  # Old Cedar Clearing (dup) -> Oldtown
    '_fBmdJReXCqdRLzYzyKw7w': '_Gnm9WMQNjhUWJLhrkpqQk',  # Braceria McKay -> Oldtown

    # SUCC Campus Sub-locations
    '_jYJxF7fte2Gz1F2HGXpUR': '_j67Dp2PVwFCpdrfWRYV2M',  # Basilica Library -> SUCC
    '_xfz8yrt2RjqHyTa8MXG3W': '_j67Dp2PVwFCpdrfWRYV2M',  # Wyrm Dormitories -> SUCC
    '_nhdQ7xkycT1yfn1wWXN8U': '_j67Dp2PVwFCpdrfWRYV2M',  # Unicorn Hall -> SUCC
    '_Bx2U1xzg1D3wpFRe39L7y': '_j67Dp2PVwFCpdrfWRYV2M',  # Bulls Stadium -> SUCC
    '_G33ABhpFceN7HanHwp8rr': '_j67Dp2PVwFCpdrfWRYV2M',  # Supernatural Support Center (SSC) -> SUCC
    '_GnNYqapde8TGQtemCwJHT': '_j67Dp2PVwFCpdrfWRYV2M',  # Main Pool -> SUCC
    '_t3ReTGT1AjzaKqVM7PtDT': '_j67Dp2PVwFCpdrfWRYV2M',  # Parking Lot B -> SUCC
    '_Red8pjJGjMhP2XDBejrt2': '_j67Dp2PVwFCpdrfWRYV2M',  # Building A -> SUCC
    '_kTjtqx6n2r6JVhFFXe8D7': '_Bx2U1xzg1D3wpFRe39L7y',  # Dullahan's Quarters -> Bulls Stadium

    # CUMS Campus
    '_3kFK6JCz9WEM2wGNRXnxq': '_Caw9nRwKf4Gx9VzW21QJj',  # Nocturnal Hall -> CUMS

    # Solarton City Sub-locations
    '_CKkP1PfqRJDQLBPQeFyWF': '_761mFFeCcQyR9JxhLCWcy',  # Static & Ink -> Solarton
    '_Mq1DYmKdnkR83YBjNRyXr': '_761mFFeCcQyR9JxhLCWcy',  # Solarton Square -> Solarton
    '_aWcjmPKnChpzGndYD62gP': '_761mFFeCcQyR9JxhLCWcy',  # Clinica Ortus -> Solarton
    '_BD8F76PngMyD2yURFWV76': '_761mFFeCcQyR9JxhLCWcy',  # La Dimora del Rifugio -> Solarton
}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print(f"--- PUNTO 7: PERFEZIONAMENTO GERARCHIA LOCATION ({len(PARENT_ASSIGNMENTS)} ASSEGNAZIONI) ---")

    data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    loc_map = {l['id']: l['name'] for l in data['world_locations']}

    success_cnt = 0
    for child_id, parent_id in PARENT_ASSIGNMENTS.items():
        child_name = loc_map.get(child_id, child_id)
        parent_name = loc_map.get(parent_id, parent_id)
        safe_child = child_name.encode('ascii', 'replace').decode('ascii')
        safe_parent = parent_name.encode('ascii', 'replace').decode('ascii')
        try:
            res = api_put_location(child_id, {'parent_location_id': parent_id}, token)
            p_val = res.get('parent_location_id') or (res.get('parent_location', {}).get('id') if isinstance(res.get('parent_location'), dict) else res.get('parent_location'))
            print(f"  [LOC PARENT OK] {safe_child[:32]:32} -> Parent: {safe_parent[:30]} ({p_val})")
            success_cnt += 1
        except Exception as e:
            print(f"  [LOC PARENT ERR] {safe_child[:32]:32}: {e}")
        time.sleep(0.15)

    print(f"\n--- PUNTO 7 COMPLETATO: {success_cnt}/{len(PARENT_ASSIGNMENTS)} sub-location collegate con successo! ---")

if __name__ == '__main__':
    main()
