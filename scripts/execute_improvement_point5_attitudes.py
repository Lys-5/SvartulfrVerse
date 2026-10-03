import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from execute_todo_phase4_homes import api_put_character

NEW_ATTITUDES = {
    # 1. Lord Cornelius Douglas
    '_rJKYcCt61hQa8XRamHEdM': [
        {'id': 'att-cor-mag', 'target_type': 'world_character', 'target_id': '_jeJTbxLcrYWXNWYPDx4ph', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'My eldest successor, continuing the colonial dignity and legal legacy of House Douglas.'},
        {'id': 'att-cor-erik', 'target_type': 'world_character', 'target_id': '_d44gDc8N18kkbEhAcfUCG', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'The reigning Prime Alpha, who transformed our house into a corporate and territorial titan.'},
        {'id': 'att-cor-aly', 'target_type': 'world_character', 'target_id': '_MXcEC8Y6B3BNm3b1ttHj6', 'target': '', 'tier': 'best_friend', 'intensity': 92, 'reasoning': 'The precious White Moon jewel of our house, carrying the sacred line forward.'}
    ],
    # 2. Magnus Douglas III
    '_jeJTbxLcrYWXNWYPDx4ph': [
        {'id': 'att-mag-eli', 'target_type': 'world_character', 'target_id': '_EwPN1te7qtUKYEx4NLgag', 'target': '', 'tier': 'love', 'intensity': 98, 'reasoning': 'My beloved Lady, the quiet unshakeable soul of Seven Hills.'},
        {'id': 'att-mag-erik', 'target_type': 'world_character', 'target_id': '_d44gDc8N18kkbEhAcfUCG', 'target': '', 'tier': 'best_friend', 'intensity': 92, 'reasoning': 'My formidable heir, ruling both the corporate boardroom and the pack territory.'},
        {'id': 'att-mag-log', 'target_type': 'world_character', 'target_id': '_JL37wK9PQMNDChULCDrWj', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'My headstrong second son, rebellious but fiercely protective of our name.'},
        {'id': 'att-mag-cor', 'target_type': 'world_character', 'target_id': '_rJKYcCt61hQa8XRamHEdM', 'target': '', 'tier': 'friend', 'intensity': 88, 'reasoning': 'The founder whose charter and bloodline we maintain with absolute rigor.'}
    ],
    # 3. Lady Elizabeth Duskwood
    '_EwPN1te7qtUKYEx4NLgag': [
        {'id': 'att-eli-mag', 'target_type': 'world_character', 'target_id': '_jeJTbxLcrYWXNWYPDx4ph', 'target': '', 'tier': 'love', 'intensity': 98, 'reasoning': 'My devoted husband, whose rigid formality softens only in private.'},
        {'id': 'att-eli-erik', 'target_type': 'world_character', 'target_id': '_d44gDc8N18kkbEhAcfUCG', 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My eldest son, carrying the weight of the entire territory and the ghost of Nixara.'},
        {'id': 'att-eli-log', 'target_type': 'world_character', 'target_id': '_JL37wK9PQMNDChULCDrWj', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'My youngest boy, finding his own sanctuary in The Verve.'},
        {'id': 'att-eli-aly', 'target_type': 'world_character', 'target_id': '_MXcEC8Y6B3BNm3b1ttHj6', 'target': '', 'tier': 'best_friend', 'intensity': 98, 'reasoning': 'My darling granddaughter, the gentle heartbeat of our home.'}
    ],
    # 4. Nixara Bloodmoon
    '_fmzBDjDn3Gnq2hXKy7tY6': [
        {'id': 'att-nix-erik', 'target_type': 'world_character', 'target_id': '_d44gDc8N18kkbEhAcfUCG', 'target': '', 'tier': 'love', 'intensity': 100, 'reasoning': 'My fierce, devoted Alpha, my eternal mate across life and death.'},
        {'id': 'att-nix-aly', 'target_type': 'world_character', 'target_id': '_MXcEC8Y6B3BNm3b1ttHj6', 'target': '', 'tier': 'love', 'intensity': 100, 'reasoning': 'My daughter, the White Moon born of my last breath, my soul in this world.'},
        {'id': 'att-nix-jas', 'target_type': 'world_character', 'target_id': '_x3VY2kcbaDbKyCqywGeET', 'target': '', 'tier': 'love', 'intensity': 95, 'reasoning': 'My twin son, bearing my spirit of defiance and creative brilliance.'},
        {'id': 'att-nix-mal', 'target_type': 'world_character', 'target_id': '_rAcN9GXD1Le4WxY28e49W', 'target': '', 'tier': 'love', 'intensity': 95, 'reasoning': 'My brave firstborn warrior, shield of his younger siblings.'},
        {'id': 'att-nix-noah', 'target_type': 'world_character', 'target_id': '_r42cVzMjcGTAx7bR1DQVt', 'target': '', 'tier': 'love', 'intensity': 95, 'reasoning': 'My gentle healer and diplomat, warmth in a hard world.'},
        {'id': 'att-nix-wulf', 'target_type': 'world_character', 'target_id': '_W9PLYt9ERTBJBXqKQL2en', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'The ancient grandfather of my blood, who guards our legacy.'}
    ],
    # 5. Marcus Thornfield
    '_PCC1PLfcGrdw2VfMnhVcL': [
        {'id': 'att-mar-kal', 'target_type': 'world_character', 'target_id': '_b7QqV43D8pU1tewx4qenY', 'target': '', 'tier': 'best_friend', 'intensity': 98, 'reasoning': 'My brother-in-arms from Gamma-7. We survived hell together; I trust him with my life.'},
        {'id': 'att-mar-erik', 'target_type': 'world_character', 'target_id': '_d44gDc8N18kkbEhAcfUCG', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'The CEO and Prime Alpha who gave our unit purpose and a fortress to defend.'},
        {'id': 'att-mar-mal', 'target_type': 'world_character', 'target_id': '_rAcN9GXD1Le4WxY28e49W', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'The brute force of the vanguard. Reliable in a breach, even if he hits first and asks questions never.'}
    ],
    # 6. Fenris
    '_wpMTPQ2VVA2pWqJ3cMztJ': [
        {'id': 'att-fen-wulf', 'target_type': 'world_character', 'target_id': '_W9PLYt9ERTBJBXqKQL2en', 'target': '', 'tier': 'best_friend', 'intensity': 99, 'reasoning': 'My first chosen son, consecrated in blood, carrying my divine covenant across millennia.'},
        {'id': 'att-fen-ut', 'target_type': 'world_character', 'target_id': '_NYtBzeKNkm3pedHMnYaka', 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'The mountain of my creation, forged in ice and iron.'},
        {'id': 'att-fen-zef', 'target_type': 'world_character', 'target_id': '_FJhtBq4xUM4aUWpaJAPYF', 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My silent shadow, frozen in the cold truth of my hunt.'},
        {'id': 'att-fen-aly', 'target_type': 'world_character', 'target_id': '_MXcEC8Y6B3BNm3b1ttHj6', 'target': '', 'tier': 'love', 'intensity': 98, 'reasoning': 'The White Moon born of the purest primordial seed, bearer of my blessing.'}
    ],
    # 7. Varg Darkfire
    '_bh8AHn7WKkNTnLjwXrUWE': [
        {'id': 'att-varg-zee', 'target_type': 'world_character', 'target_id': '_a6KYGdN3BWTgbYEbT4mx8', 'target': '', 'tier': 'friend', 'intensity': 80, 'reasoning': 'My son who defeated me in ritual combat. He replaced brute slavery with corporate domination; he earned my cold respect.'},
        {'id': 'att-varg-bor', 'target_type': 'world_character', 'target_id': '_aaWfLtx19WQR7JyHKDBem', 'target': '', 'tier': 'friend', 'intensity': 82, 'reasoning': 'The earthen guardian of our roots, steadfast and immovable.'},
        {'id': 'att-varg-kar', 'target_type': 'world_character', 'target_id': '_Agf7FxKMzPDFJj3gktYtz', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'The executioner, holding the old savagery of the Red Lineage.'}
    ],
    # 8. Boros Darkfire
    '_aaWfLtx19WQR7JyHKDBem': [
        {'id': 'att-bor-zee', 'target_type': 'world_character', 'target_id': '_a6KYGdN3BWTgbYEbT4mx8', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'Our Clan Leader and CEO. I ensure every shipment and logistical foundation holds firm under his orders.'},
        {'id': 'att-bor-kar', 'target_type': 'world_character', 'target_id': '_Agf7FxKMzPDFJj3gktYtz', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'My brutal brother, the enforcer who clears any obstacle in our supply lines.'},
        {'id': 'att-bor-ara', 'target_type': 'world_character', 'target_id': '_8catGJE98MTpfaajJD9zV', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'Our silver-tongued diplomat, masking our clan\'s iron grip with velvet illusions.'}
    ],
    # 9. Karshin Darkfire
    '_Agf7FxKMzPDFJj3gktYtz': [
        {'id': 'att-kar-zee', 'target_type': 'world_character', 'target_id': '_a6KYGdN3BWTgbYEbT4mx8', 'target': '', 'tier': 'best_friend', 'intensity': 92, 'reasoning': 'The Clan Leader whose word is law. Any threat to HSK or the Horned Skull meets my blades.'},
        {'id': 'att-kar-bor', 'target_type': 'world_character', 'target_id': '_aaWfLtx19WQR7JyHKDBem', 'target': '', 'tier': 'friend', 'intensity': 84, 'reasoning': 'My solid brother, the anchor of our operations.'},
        {'id': 'att-kar-yael', 'target_type': 'world_character', 'target_id': '_Ht3kV76zrCE9tPmDAYh8Q', 'target': '', 'tier': 'friend', 'intensity': 82, 'reasoning': 'The exile from the north, a lethal hunter who commands our tracking units.'}
    ],
    # 10. Aras Darkfire
    '_8catGJE98MTpfaajJD9zV': [
        {'id': 'att-ara-zee', 'target_type': 'world_character', 'target_id': '_a6KYGdN3BWTgbYEbT4mx8', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'Our pragmatic visionary. I translate his ruthless strategy into corporate contracts and alliances.'},
        {'id': 'att-ara-kar', 'target_type': 'world_character', 'target_id': '_Agf7FxKMzPDFJj3gktYtz', 'target': '', 'tier': 'friend', 'intensity': 78, 'reasoning': 'A terrifying enforcer, useful when diplomacy is deliberately intended to fail.'}
    ],
    # 11. Nicole O'Connor
    '_bbWxM1b7q2eRCWp7fYUVd': [
        {'id': 'att-nic-mar', 'target_type': 'world_character', 'target_id': '_hzhkJ7n4FGXBxAHc6Eykj', 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My grandfather and Pack Leader, guardian of Oldtown\'s traditions.'},
        {'id': 'att-nic-aly', 'target_type': 'world_character', 'target_id': '_MXcEC8Y6B3BNm3b1ttHj6', 'target': '', 'tier': 'friend', 'intensity': 85, 'reasoning': 'A fellow high-born pack daughter, navigating the immense pressures of our bloodlines.'},
        {'id': 'att-nic-noah', 'target_type': 'world_character', 'target_id': '_r42cVzMjcGTAx7bR1DQVt', 'target': '', 'tier': 'friend', 'intensity': 82, 'reasoning': 'A charming diplomat from Villa Douglas, always bringing peace and incredible pastries.'}
    ],
    # 12. Ren
    '_yYNA9Mxj2tyGNeT9VJzbh': [
        {'id': 'att-ren-dom', 'target_type': 'world_character', 'target_id': '_8wjMyUNV6yB7ACLk4dhWd', 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'The velvet emperor of Paradise West, mentor in high-fashion diplomacy.'},
        {'id': 'att-ren-bia', 'target_type': 'world_character', 'target_id': '_tEjWAbTqE6abw8UApDADw', 'target': '', 'tier': 'friend', 'intensity': 88, 'reasoning': 'A brilliant, sharp-tongued stylist and confidante in the luxury district.'},
        {'id': 'att-ren-aly', 'target_type': 'world_character', 'target_id': '_MXcEC8Y6B3BNm3b1ttHj6', 'target': '', 'tier': 'friend', 'intensity': 84, 'reasoning': 'An absolute sweetheart with radiant taste, always deserving the best care.'}
    ]
}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print(f"--- PUNTO 5: COMPLETAMENTO ATTITUDES NETWORK SU {len(NEW_ATTITUDES)} PERSONAGGI ---")

    data = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    char_map = {c['id']: (c.get('display_name') or c.get('first_name')) for c in data['world_characters']}

    success_cnt = 0
    for cid, atts in NEW_ATTITUDES.items():
        cname = char_map.get(cid, cid)
        safe_name = cname.encode('ascii', 'replace').decode('ascii')
        try:
            res = api_put_character(cid, {'attitudes': atts}, token)
            cur_atts = res.get('attitudes', [])
            print(f"  [ATT OK] {safe_name[:35]:35} -> {len(cur_atts)} relazioni configurate")
            success_cnt += 1
        except Exception as e:
            print(f"  [ATT ERR] {safe_name[:35]:35}: {e}")
        time.sleep(0.15)

    print(f"\n--- PUNTO 5 COMPLETATO: {success_cnt}/{len(NEW_ATTITUDES)} personaggi aggiornati! Attitudes Network al 100%! ---")

if __name__ == '__main__':
    main()
