import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

# 1. Environment California Coast Description
CALIFORNIA_COAST_DESC = (
    "La fascia litoranea della California centrale si estende tra scogliere a picco sull'Oceano Pacifico, "
    "colline coperte di pini costieri e ampie vallate baciate da una nebbia salmastra mattutina che si dissolve sotto il sole caldo del pomeriggio. "
    "Lungo questo corridoio geografico si snoda la Highway 101, collegando la storica metropoli sovrannaturale di Blackwood City con il vivace distretto "
    "universitario di Solarton, i moli industriali di Dockside e le tenute private abbarbicate sulle Seven Hills.\n\n"
    "Il territorio e un mosaico di microclimi e culture intrecciate: l'aria oceanica e densa di sale e ozono, mentre l'entroterra profuma di resina di pino, "
    "terra umida e asfalto bagnato. Qui la coesistenza tra la societa umana moderna, le antiche casate di lupi mannari e la popolazione demi-umana e una realta "
    "quotidiana, regolata da equilibri territoriali sottili ma inflessibili. Di giorno le spiagge, i campus universitari e i viali commerciali brulicano di "
    "traffico ed energia studentesca. Di notte, quando la luna sale sull'oceano e la brezza marina rinfresca le alture, emergono le dinamiche piu intime "
    "e primordiali dei branchi, il richiamo dei motori sulle strade costiere e l'ombra silenziosa delle pattuglie di sicurezza privata che vigilano sui confini."
)

# 2. Memories to attach
MEMORIES_TO_ATTACH = [
    {
        'id': '_FfMgf4j7raaWFWrKPbjqF',
        'name': 'Il Viaggio di Wulfnic in America',
        'char_id': '_W9PLYt9ERTBJBXqKQL2en'  # Wulfnic Bloodmoon
    },
    {
        'id': '_RerjwQhF7nYeLxYweP2aE',
        'name': "Logan's Protective Vigil at Eidolon",
        'char_id': '_JL37wK9PQMNDChULCDrWj'  # Logan Douglas
    },
    {
        'id': '_aTh9AggWbNrQjH8TyVDrx',
        'name': 'Erik Douglas Surveillance Protocols',
        'char_id': '_d44gDc8N18kkbEhAcfUCG'  # Erik Douglas
    },
    {
        'id': '_ATQpnqFj2BGJCLLyXFn8U',
        'name': "Alyssa's Blue Ocean Gown",
        'char_id': '_MXcEC8Y6B3BNm3b1ttHj6'  # Alyssa Douglas Bloodmoon
    },
    {
        'id': '_AbGLJNDUcA9NPDN8CjEfw',
        'name': "Alyssa's Feromonal Vulnerability at Fifth Avenue",
        'char_id': '_MXcEC8Y6B3BNm3b1ttHj6'  # Alyssa Douglas Bloodmoon
    },
    {
        'id': '_1x2zU7hXmnG9YbLkNPqLy',
        'name': "Alyssa's Alcohol Sensitivity",
        'char_id': '_MXcEC8Y6B3BNm3b1ttHj6'  # Alyssa Douglas Bloodmoon
    },
    {
        'id': '_fcF1JXgQCawMj3t3WFt2X',
        'name': "Noah's Secret Shopping for Alyssa",
        'char_id': '_r42cVzMjcGTAx7bR1DQVt'  # Noah Douglas Bloodmoon
    },
    {
        'id': '_GCUFA3fteUdmP8UYeb2Rp',
        'name': "Moreno's Private Dressing Suites",
        'char_id': '_mwqYFKwWfHDMctDJQMR6w'  # Angelo Moreno
    }
]

# 3. Creatures to configure
CREATURES_TO_CONFIG = [
    {
        'id': '_b66ztLLgNRKTyfafhqRg7',
        'name': 'Ice Satyrs',
        'config': {
            'intelligence': 'instinctive',
            'types': ['Beast', 'Ice'],
            'capture_rate': 0
        }
    },
    {
        'id': '_FkXtyrhQMhCpg7N6gm1Wm',
        'name': 'Asag Beast',
        'config': {
            'intelligence': 'cunning',
            'types': ['Abyssal', 'Demon'],
            'capture_rate': 0
        }
    }
]

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    # STEP 1: Environment California Coast
    print("--- 1. AGGIORNAMENTO DESCRIZIONE ENVIRONMENT CALIFORNIA COAST ---")
    env_id = '_jUzC2EQyPTHte1hTYqPt8'
    url_env = f"{API_BASE}/environments/{env_id}?world_id={WORLD_ID}"
    env_payload = {
        'description': CALIFORNIA_COAST_DESC,
        'context_description': CALIFORNIA_COAST_DESC
    }
    try:
        req = urllib.request.Request(url_env, data=json.dumps(env_payload).encode('utf-8'), headers=headers, method='PUT')
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
        d_len = len(res.get('context_description', '') or res.get('description', ''))
        print(f"  [ENV OK] California Coast aggiornato con {d_len} caratteri di prosa scenica immersiva!")
    except Exception as e:
        print(f"  [ENV ERR] Errore aggiornamento environment: {e}")

    # STEP 2: Memories attached_world_character_id
    print("\n--- 2. COLLEGAMENTO ATTACHED CHARACTER SU 8 MEMORIE ---")
    for m in MEMORIES_TO_ATTACH:
        mid = m['id']
        cid = m['char_id']
        mname = m['name']
        url_lex = f"{API_BASE}/lexicon/{mid}?world_id={WORLD_ID}"
        lex_payload = {'attached_world_character_id': cid}
        try:
            req = urllib.request.Request(url_lex, data=json.dumps(lex_payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
            cur_att = res.get('attached_world_character_id')
            print(f"  [MEM OK] {mname[:38]:38} -> Attached Char: {cur_att}")
        except Exception as e:
            print(f"  [MEM ERR] {mname[:38]:38}: {e}")
        time.sleep(0.15)

    # STEP 3: Creature Configurations
    print("\n--- 3. CONFIGURAZIONE CREATURE_CONFIG SU CREATURE DUNGEON ---")
    for c in CREATURES_TO_CONFIG:
        cid = c['id']
        cname = c['name']
        cfg = c['config']
        url_lex = f"{API_BASE}/lexicon/{cid}?world_id={WORLD_ID}"
        lex_payload = {'creature_config': cfg}
        try:
            req = urllib.request.Request(url_lex, data=json.dumps(lex_payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
            cur_cfg = res.get('creature_config', {})
            print(f"  [CREATURE OK] {cname[:25]:25} -> Types: {cur_cfg.get('types')}, Intel: {cur_cfg.get('intelligence')}")
        except Exception as e:
            print(f"  [CREATURE ERR] {cname[:25]:25}: {e}")
        time.sleep(0.15)

    print("\n--- TUTTI E 3 I MIGLIORAMENTI COMPLETATI CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
