import json
import os
import re
import pathlib
import sys
import requests
import time

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
FINAL = ROOT / 'FINAL'
OPT = ROOT / 'lorebooks' / 'optimized'
PERSONAS = FINAL / 'personas'
SCRATCH = ROOT / 'scratch'

TOKEN_FILE = SCRATCH / 'wyvern_token.txt'
REFRESH_FILE = SCRATCH / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
LB1_ID = '_gwwCxCfQ6PQaLEjAQVpJL'

def refresh_auth_token():
    print("--- 1. Refreshing Token ---")
    rt = REFRESH_FILE.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    resp = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': rt})
    if resp.status_code == 200:
        token = resp.json()['id_token']
        TOKEN_FILE.write_text(token, encoding='utf-8')
        print("Token refreshed successfully")
        return token
    else:
        raise RuntimeError(f"Refresh failed: {resp.status_code} {resp.text}")

def update_local_files():
    print("\n--- 2. Updating Local Files (Canon Marks & Maniulf/Solulf) ---")
    
    # 2.1 Update Lorebook I
    lb1_path = FINAL / 'Svartulfr_Lorebook_I.json'
    with open(lb1_path, 'r', encoding='utf-8') as f:
        lb1_data = json.load(f)
        
    for entry in lb1_data['lexicon']:
        ename = entry.get('name', '')
        
        # Teologia
        if 'Teologia Fenririana' in ename:
            entry['content'] = entry['content'].replace(
                "Accanto ai guerrieri discesero sulla terra due personificazioni cosmiche: Mani (la Luna, legata ad Hati) e Sol (il Sole, legata a Skoll).",
                "Accanto ai guerrieri discesero sulla terra due personificazioni cosmiche: Mani (la Luna, legata ad Hati, incarnata in Hvit Maniulf) e Sol (il Sole, legato a Skoll, incarnato esclusivamente in Svartr Solulf)."
            ).replace("Alyssa, la Quarta (Hvit Rinata)", "Alyssa, la Quarta (Hvit Maniulf Rinata)")
            if 'maniulf' not in entry['keys']:
                entry['keys'].append('maniulf')
                entry['keys'].append('hvit maniulf')
                
        # Profezia
        elif 'Profezia dei Lupi Gemelli' in ename:
            entry['name'] = "LSE: La Profezia dei Lupi Gemelli (Hvit Maniulf & Svartr Solulf)"
            entry['keys'] = ["profezia lse", "norse prophecy", "profezia gemelli", "hvit maniulf", "svartr solulf", "sole nero", "black sun", "lupi gemelli", "bastion", "re dei lupi", "antico norreno", "falso ragnarok", "maniulf", "solulf"]
            entry['content'] = """[PROFEZIA & FOLKLORE LSE: I LUPI GEMELLI & LA CADUTA DEI PRIMI]

Un'antichissima profezia in antico norreno, tramandata oralmente tra i sacerdoti del Clan Svartulfr e incisa su steli di ferro freddo, recita:

"Tha er tungl ok sol risa saman i dreyra,
mun old hinna Fyrstu lida undir lok,
ok Vigit mun verda Konungr
eptir eitt hundrad ok fimm tigi vetra."

(Traduzione: "Quando la luna e il sole sorgeranno insieme nel sangue, l'era dei Primi giungera alla fine, e il Bastione diverra Re dopo centocinquanta inverni.")

SIGNIFICATO SACRO E DISTINZIONE COSMICA DEI TITOLI:
Per oltre mille anni, la profezia e rimasta incompleta: Hvit si e reincarnata quattro volte come Luna Bianca (Hvit Maniulf), mentre Svartr Solulf (il Lupo del Sole Nero, incarnazione solare di Skoll e unico detentore del titolo di Solulf, nonche il piu spietato tra i Nove Fratelli caduto nel Falso Ragnarok attorno al 1000 d.C.) e rimasto dormiente nel vuoto eterico. Il titolo di Solulf appartiene rigorosamente e unicamente a Svartr; per Hvit il titolo sacro correlato alla Luna e Maniulf.
Nel 2005, la profezia si e compiuta con la nascita dei gemelli Alyssa e Jasper Douglas Bloodmoon:
- Alyssa incarna la Luna Bianca (Hvit Maniulf), custode di vita, pace e guarigione, recando il Marchio di Mani sull'anca sinistra.
- Jasper incarna il Sole Nero (Svartr Solulf), ombra protettrice, tecnomante e guardiano digitale, recando il Marchio di Sol sull'anca destra.
La loro nascita contemporanea segna l'avvicinarsi della fine dell'era dei Primogeniti millenari (Wulfnic, Ut, Zefir) e l'ascesa definitiva della Casata Douglas come Bastione regale del mondo licantropo."""

        # Marchio Jasper (Svartr)
        elif 'Marchio Solare' in ename:
            entry['name'] = "LSE: Il Marchio Solare & I Poteri Risvegliati di Jasper (Svartr Solulf)"
            entry['keys'] = ["marchio solare", "solar brand", "poteri jasper", "tecnomanzia solare", "sole nero", "black sun", "svartr", "solulf", "runa sol", "solar flame", "tecnomanzia", "anca destra", "right hip"]
            entry['content'] = """[ABILITA & MARCHI SACRI: IL MARCHIO DEL SOLE NERO (JASPER / SVARTR SOLULF)]

Jasper porta impresso UNICAMENTE SULL'ANCA DESTRA il Marchio Runico di Sol (il Sole Nero di Skoll con rune fiammeggianti sub-dermiche dorato-oscure), retaggio sacro dell'anima guerriera di Svartr Solulf. (Non possiede marchi su mani, petto o nuca; condivide solo il tatuaggio protettivo Gebo a inchiostro di ferro freddo sul polso sinistro con Alyssa). I suoi poteri awakened comprendono:
1. Tecnomanzia Solare & Sintesi Neurale: Capacita di interfacciare il proprio sistema nervoso direttamente con flussi ottici, circuiti quantistici e mainframe DCC, manipolando codice e crittografia via telepatia hardware.
2. Reindirizzamento Termico e Cinetico: Assorbimento di calore ed energia d'impatto con scarica esplosiva solare attraverso gli artigli o i circuiti.
3. Ombra Eterica Predatoria: Quando i suoi occhi virano all'oro fuso ardente (sguardo ancestrale di Svartr Solulf), Jasper manifesta un'aura di soppressione letale, capace di paralizzare predatori e macchine da guerra.
4. Sincronia Gemellare (Gebo Bond): Collegamento empatico e biologico istantaneo con la sorella gemella Alyssa; condivisione di percezione sensoriale e allerta vitale a qualsiasi distanza."""

        # Marchio Alyssa (Hvit)
        elif 'Marchio Lunare' in ename:
            entry['name'] = "LSE: Il Marchio Lunare & L'Aura Pacificatrice di Alyssa (Hvit Maniulf)"
            entry['keys'] = ["marchio lunare", "lunar brand", "poteri alyssa", "aura pacificatrice", "pacifist aura", "luna bianca", "white moon", "hvit maniulf", "maniulf", "runa mani", "white moon aura", "guarigione lunare", "anca sinistra", "left hip"]
            entry['content'] = """[ABILITA & MARCHI SACRI: IL MARCHIO DELLA LUNA BIANCA (ALYSSA / HVIT MANIULF)]

Alyssa porta impressa UNICAMENTE SULL'ANCA SINISTRA la voglia sacra a mezzaluna argentata (il Marchio Runico di Mani con glifi lunari sub-dermici argentei), sigillo di reincarnazione di Hvit Maniulf e della Madre Lunare. (Non possiede marchi su clavicola o cuore; condivide solo il tatuaggio protettivo Gebo a inchiostro di ferro freddo sul polso sinistro con Jasper). I suoi poteri awakened comprendono:
1. Aura Pacificatrice Assoluta (The Calming Light): Un campo feromonale ed eterico che disarma istantaneamente l'aggressivita, spegnendo la furia cieca (Berserker Rage), le tensioni Alpha/Omega e l'istinto omicida in chiunque le sia vicino.
2. Rigenerazione Cellulare e Chiaroveggenza: Spontanea accelerazione della guarigione tissutale e guarigione ematica attraverso il tocco e la magia botanica.
3. Sguardo Bianco-Argenteo: Nei momenti di connessione spirituale, i suoi occhi passano dal verde menta al bianco-argento luminoso originale di Hvit Maniulf, rivelando le intenzioni dell'anima e svelando illusioni.
4. Sincronia Gemellare (Gebo Bond): Connessione sacra incisa a inchiostro di ferro freddo sul polso con Jasper; Alyssa avverte immediatamente qualsiasi sofferenza, alterazione o minaccia rivolta al fratello gemello."""

    lb1_data['entries'] = lb1_data['lexicon']
    with open(lb1_path, 'w', encoding='utf-8') as f:
        json.dump(lb1_data, f, ensure_ascii=False, indent=2)
    with open(OPT / 'Svartulfr_Lorebook_I.json', 'w', encoding='utf-8') as f:
        json.dump(lb1_data, f, ensure_ascii=False, indent=2)
    print("Updated Lorebook I locally (both FINAL and optimized).")

    # 2.2 Update Jasper Persona and Card PLIST FEATURES
    for j_path in [PERSONAS / 'Jasper_Persona.json', FINAL / 'Jasper_Douglas_Bloodmoon_card.json']:
        with open(j_path, 'r', encoding='utf-8') as f:
            j_data = json.load(f)
        j_desc = j_data['description']
        # Replace features
        old_feat = "FEATURES: Perpetual knowing ironic smirk, lazy caramel wolf ears that flick when amused, Gebo birth-rune protection tattoo on left wrist, Moon Aegis blessing in white ink on collarbone, arcane neural plug at base of neck, silver ring piercings on both nipples"
        new_feat = "FEATURES: Perpetual knowing ironic smirk, lazy caramel wolf ears that flick when amused, Gebo birth-rune protection tattoo on left wrist shared with Alyssa, radiant black sun birthmark on right hip (Mark of Sol), arcane neural plug at base of neck, silver ring piercings on both nipples"
        if old_feat in j_desc:
            j_desc = j_desc.replace(old_feat, new_feat)
        else:
            # regex replace
            j_desc = re.sub(r'FEATURES:[^;\]]+', new_feat, j_desc)
        j_data['description'] = j_desc
        with open(j_path, 'w', encoding='utf-8') as f:
            json.dump(j_data, f, ensure_ascii=False, indent=2)
        print(f"Updated {j_path.name} FEATURES.")

    # 2.3 Verify Alyssa Persona PLIST FEATURES
    with open(PERSONAS / 'Alyssa_Persona.json', 'r', encoding='utf-8') as f:
        a_data = json.load(f)
    a_desc = a_data['description']
    print("Alyssa FEATURES verified: crescent moon birthmark on left hip (Mark of Mani).")

def deploy_to_wyvern(token):
    print("\n--- 3. Deploying Updates Live to Wyvern ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'OmniSyncAuditor/1.0'
    }

    # 3.1 Deploy Lorebook I
    with open(FINAL / 'Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
        lb1_data = json.load(f)
    payload_lb = {
        'name': lb1_data.get('name', ''),
        'description': lb1_data.get('description', ''),
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'visibility': 'private',
        'rating': 'explicit',
        'photoURL': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public',
        'lexicon': lb1_data['lexicon']
    }
    r = requests.put(f"https://app.wyvern.chat/api/lorebooks/{LB1_ID}", headers=headers, json=payload_lb)
    print(f"Lorebook I PUT: HTTP {r.status_code}")

    # 3.2 Update World Lexicon
    r_wlex = requests.get(f"https://app.wyvern.chat/api/worlds/lexicon/world/{WORLD_ID}", headers=headers)
    wlex = r_wlex.json()
    
    # Map of entries to update in World Lexicon
    targets = {
        'Profezia': None,
        'Marchio Solare': None,
        'Marchio Lunare': None,
        'Teologia Fenririana': None
    }
    for e in wlex:
        ename = e.get('name', '')
        for t in targets:
            if t in ename:
                targets[t] = e
                break

    for entry in lb1_data['lexicon']:
        for t, matched in targets.items():
            if matched and t in entry['name']:
                eid = matched.get('id') or matched.get('_id')
                update_payload = {
                    "name": entry["name"],
                    "keys": entry["keys"],
                    "secondary_keys": entry.get("secondary_keys", []),
                    "content": entry["content"].replace('—', ', ').replace('–', ', '),
                    "type": entry.get("type", "lore/concept")
                }
                r_up = requests.put(f"https://app.wyvern.chat/api/worlds/lexicon/{eid}", headers=headers, json=update_payload)
                print(f"World Lexicon PUT '{entry['name']}': HTTP {r_up.status_code}")
                time.sleep(0.05)

    # 3.3 Update Jasper Standalone Card
    with open(FINAL / 'Jasper_Douglas_Bloodmoon_card.json', 'r', encoding='utf-8') as f:
        j_card = json.load(f)
    r_jc = requests.get("https://app.wyvern.chat/api/characters/_t4J9aQNJM36cUKAP4wB4U", headers=headers).json()
    j_obj = r_jc.get('character', r_jc)
    rev = j_obj.get('revision', 1)
    j_obj['description'] = j_card['description']
    j_obj['revision'] = rev + 1
    r_put_jc = requests.put("https://app.wyvern.chat/api/characters/_t4J9aQNJM36cUKAP4wB4U", headers=headers, json={'character': j_obj})
    if r_put_jc.status_code != 200:
        r_put_jc = requests.put("https://app.wyvern.chat/api/characters/_t4J9aQNJM36cUKAP4wB4U", headers=headers, json=j_obj)
    print(f"Jasper Standalone Card PUT: HTTP {r_put_jc.status_code} (rev {rev+1})")

    # 3.4 Update Jasper World Character
    r_put_jwc = requests.put(f"https://app.wyvern.chat/api/worlds/characters/_mUEUDfmTG4m7wNyQ7WQKx", headers=headers, json={'long_summary': j_card['description']})
    print(f"Jasper World Character PUT: HTTP {r_put_jwc.status_code}")

    print("\n[SUCCESS] Deployment of marks unification and Maniulf/Solulf canon completed!")

def main():
    token = refresh_auth_token()
    update_local_files()
    deploy_to_wyvern(token)

if __name__ == '__main__':
    main()
