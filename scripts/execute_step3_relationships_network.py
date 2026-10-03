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

def api_put(resource, entity_id, payload, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
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

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print("--- STEP 3: DISTRIBUZIONE ATTITUDES E RETE DI RELAZIONI ---")

    # Mappatura IDs
    ID_ERIK = '_d44gDc8N18kkbEhAcfUCG'
    ID_ALYSSA = '_MXcEC8Y6B3BNm3b1ttHj6'
    ID_JASPER = '_x3VY2kcbaDbKyCqywGeET'
    ID_MALACHIA = '_rAcN9GXD1Le4WxY28e49W'
    ID_NOAH = '_r42cVzMjcGTAx7bR1DQVt'
    ID_LOGAN = '_JL37wK9PQMNDChULCDrWj'
    ID_EDRIC = '_YJQ4cjdrT7brm7HWVkf3K'
    ID_KALADIN = '_b7QqV43D8pU1tewx4qenY'
    ID_WULFNIC = '_W9PLYt9ERTBJBXqKQL2en'
    ID_ZEFIR = '_FJhtBq4xUM4aUWpaJAPYF'
    ID_UT = '_NYtBzeKNkm3pedHMnYaka'
    ID_JARED = '_BzKwAkgpPfbVkBzbDaEth'
    ID_JANICE = '_DKY9cDLMUaYpELYAdckH2'
    ID_DULLAHAN = '_F8ee4UpyLr7Fyr69KKhzV'

    characters_attitudes = [
        # 1. ERIK DOUGLAS
        {
            'id': ID_ERIK,
            'name': 'Erik Douglas',
            'attitudes': [
                {'id': 'att-erik-alyssa', 'target_type': 'world_character', 'target_id': ID_ALYSSA, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My only daughter, precious omega of our bloodline. I will deploy entire tactical strike teams to protect her.'},
                {'id': 'att-erik-jasper', 'target_type': 'world_character', 'target_id': ID_JASPER, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'My twin son, cybernetic innovator and technical pillar of DCC.'},
                {'id': 'att-erik-malachia', 'target_type': 'world_character', 'target_id': ID_MALACHIA, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My firstborn vanguard enforcer, shoulder-to-shoulder pack defender.'},
                {'id': 'att-erik-noah', 'target_type': 'world_character', 'target_id': ID_NOAH, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'My second son, master chef, diplomat, and heart of Villa Douglas.'},
                {'id': 'att-erik-logan', 'target_type': 'world_character', 'target_id': ID_LOGAN, 'target': '', 'tier': 'best_friend', 'intensity': 88, 'reasoning': 'My younger brother, king of The Verve, trusted pack muscle.'},
                {'id': 'att-erik-edric', 'target_type': 'world_character', 'target_id': ID_EDRIC, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'My youngest son, developing into a powerful future alpha.'},
                {'id': 'att-erik-kaladin', 'target_type': 'world_character', 'target_id': ID_KALADIN, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'Major Kaladin, commander of DCC Security Division and trusted brother-in-arms.'},
                {'id': 'att-erik-wulfnic', 'target_type': 'world_character', 'target_id': ID_WULFNIC, 'target': '', 'tier': 'best_friend', 'intensity': 99, 'reasoning': 'The Firstborn Primordial Patriarch of our bloodline, living covenant of Fenris.'}
            ]
        },
        # 2. JASPER DOUGLAS
        {
            'id': ID_JASPER,
            'name': 'Jasper Douglas',
            'attitudes': [
                {'id': 'att-jasper-alyssa', 'target_type': 'world_character', 'target_id': ID_ALYSSA, 'target': '', 'tier': 'soulmate', 'intensity': 98, 'reasoning': 'My twin sister, shared breath and heartbeat since the womb. Anyone who touches her answers to me.'},
                {'id': 'att-jasper-erik', 'target_type': 'world_character', 'target_id': ID_ERIK, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'Our father and Alpha, carrying the massive weight of DCC.'},
                {'id': 'att-jasper-logan', 'target_type': 'world_character', 'target_id': ID_LOGAN, 'target': '', 'tier': 'close_friend', 'intensity': 85, 'reasoning': 'Uncle Logan, always backing up our garage and bike custom projects.'},
                {'id': 'att-jasper-malachia', 'target_type': 'world_character', 'target_id': ID_MALACHIA, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'Big brother Malachia, immovable rock of the pack.'}
            ]
        },
        # 3. ALYSSA DOUGLAS
        {
            'id': ID_ALYSSA,
            'name': 'Alyssa Douglas Bloodmoon',
            'attitudes': [
                {'id': 'att-alyssa-jasper', 'target_type': 'world_character', 'target_id': ID_JASPER, 'target': '', 'tier': 'soulmate', 'intensity': 98, 'reasoning': 'My twin brother, inseparable bond of thought, scent, and blood.'},
                {'id': 'att-alyssa-erik', 'target_type': 'world_character', 'target_id': ID_ERIK, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'Our father, protective alpha whose heavy love shields us all.'},
                {'id': 'att-alyssa-noah', 'target_type': 'world_character', 'target_id': ID_NOAH, 'target': '', 'tier': 'best_friend', 'intensity': 92, 'reasoning': 'Noah, my gentle brother whose cooking and warmth anchor the house.'},
                {'id': 'att-alyssa-malachia', 'target_type': 'world_character', 'target_id': ID_MALACHIA, 'target': '', 'tier': 'best_friend', 'intensity': 93, 'reasoning': 'Malachia, terrifying to outsiders, deeply tender and protective to me.'},
                {'id': 'att-alyssa-wulfnic', 'target_type': 'world_character', 'target_id': ID_WULFNIC, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'Ancient Great-Grandfather Wulfnic, whose single eye watches over our destiny.'}
            ]
        },
        # 4. MALACHIA DOUGLAS
        {
            'id': ID_MALACHIA,
            'name': 'Malachia Douglas Bloodmoon',
            'attitudes': [
                {'id': 'att-malachia-erik', 'target_type': 'world_character', 'target_id': ID_ERIK, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My father and Alpha. I execute his commands without question.'},
                {'id': 'att-malachia-alyssa', 'target_type': 'world_character', 'target_id': ID_ALYSSA, 'target': '', 'tier': 'best_friend', 'intensity': 96, 'reasoning': 'My little sister. Any harm threatened against her is met with immediate lethal force.'},
                {'id': 'att-malachia-jasper', 'target_type': 'world_character', 'target_id': ID_JASPER, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'My younger brother Jasper, brilliant hacker and innovator.'},
                {'id': 'att-malachia-kaladin', 'target_type': 'world_character', 'target_id': ID_KALADIN, 'target': '', 'tier': 'close_friend', 'intensity': 88, 'reasoning': 'Major Kaladin, synchronized military tactician in our family operations.'}
            ]
        },
        # 5. EDRIC DOUGLAS
        {
            'id': ID_EDRIC,
            'name': 'Edric Douglas',
            'attitudes': [
                {'id': 'att-edric-erik', 'target_type': 'world_character', 'target_id': ID_ERIK, 'target': '', 'tier': 'best_friend', 'intensity': 92, 'reasoning': 'Father and Pack Alpha, my ultimate role model in strength and honor.'},
                {'id': 'att-edric-alyssa', 'target_type': 'world_character', 'target_id': ID_ALYSSA, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'Big sister Alyssa, always watching over her at family dinners.'},
                {'id': 'att-edric-jasper', 'target_type': 'world_character', 'target_id': ID_JASPER, 'target': '', 'tier': 'close_friend', 'intensity': 85, 'reasoning': 'Big brother Jasper, who tweaks my training gadgets and consoles.'}
            ]
        },
        # 6. WULFNIC BLOODMOON
        {
            'id': ID_WULFNIC,
            'name': 'Wulfnic Bloodmoon',
            'attitudes': [
                {'id': 'att-wulfnic-zefir', 'target_type': 'world_character', 'target_id': ID_ZEFIR, 'target': '', 'tier': 'best_friend', 'intensity': 98, 'reasoning': 'Youngest of the Firstborn, faithful scout who sailed the Arctic by my side.'},
                {'id': 'att-wulfnic-ut', 'target_type': 'world_character', 'target_id': ID_UT, 'target': '', 'tier': 'best_friend', 'intensity': 98, 'reasoning': 'My mountain brother among the Nine, stone-solid anchor across a millennium.'},
                {'id': 'att-wulfnic-erik', 'target_type': 'world_character', 'target_id': ID_ERIK, 'target': '', 'tier': 'best_friend', 'intensity': 90, 'reasoning': 'Current patriarch of my line, bearing the modern burden with lupine dignity.'},
                {'id': 'att-wulfnic-alyssa', 'target_type': 'world_character', 'target_id': ID_ALYSSA, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'The sacred bloom of our Bloodmoon line, carrying Fenris blessing.'}
            ]
        },
        # 7. ZEFIR HVITSKOG
        {
            'id': ID_ZEFIR,
            'name': 'Zefir Hvitskog',
            'attitudes': [
                {'id': 'att-zefir-wulfnic', 'target_type': 'world_character', 'target_id': ID_WULFNIC, 'target': '', 'tier': 'soulmate', 'intensity': 99, 'reasoning': 'Lord Wulfnic, my father in blood and battle, my eternal Alpha.'},
                {'id': 'att-zefir-ut', 'target_type': 'world_character', 'target_id': ID_UT, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'Brother Ut, mountain of patience and ancient shield.'}
            ]
        },
        # 8. UT BERG
        {
            'id': ID_UT,
            'name': 'Ut Berg',
            'attitudes': [
                {'id': 'att-ut-wulfnic', 'target_type': 'world_character', 'target_id': ID_WULFNIC, 'target': '', 'tier': 'soulmate', 'intensity': 99, 'reasoning': 'Wulfnic Baleygr, true leader of Fenris Nine Firstborn.'},
                {'id': 'att-ut-zefir', 'target_type': 'world_character', 'target_id': ID_ZEFIR, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'Brother Zefir, swift as the northern squall, eternal shield-brother.'}
            ]
        },
        # 9. JARED THOMPSON
        {
            'id': ID_JARED,
            'name': 'Jared Thompson',
            'attitudes': [
                {'id': 'att-jared-janice', 'target_type': 'world_character', 'target_id': ID_JANICE, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My younger sister, watching over her safety across the SUCC campus.'},
                {'id': 'att-jared-dullahan', 'target_type': 'world_character', 'target_id': ID_DULLAHAN, 'target': '', 'tier': 'close_friend', 'intensity': 85, 'reasoning': 'Coach D, mysterious head coach of the Bulls who pushes my physical limits.'}
            ]
        },
        # 10. JANICE THOMPSON
        {
            'id': ID_JANICE,
            'name': 'Janice Thompson',
            'attitudes': [
                {'id': 'att-janice-jared', 'target_type': 'world_character', 'target_id': ID_JARED, 'target': '', 'tier': 'best_friend', 'intensity': 95, 'reasoning': 'My big brother Jared, star quarterback and family protector.'}
            ]
        }
    ]

    for char_entry in characters_attitudes:
        try:
            cid = char_entry['id']
            name = char_entry['name']
            atts = char_entry['attitudes']
            res = api_put('characters', cid, {'attitudes': atts}, token)
            print(f"  [OK] Character '{name}' ({cid}): {len(res.get('attitudes', []))} attitudes registrate")
        except Exception as e:
            print(f"  [ERRORE] Character '{char_entry['name']}': {e}")
        time.sleep(0.3)

    print("\n--- STEP 3 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
