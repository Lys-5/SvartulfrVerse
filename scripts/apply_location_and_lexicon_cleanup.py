import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

SNAPSHOT_DIR = os.path.join('scratch', 'audit_cleanup_snapshots')
os.makedirs(SNAPSHOT_DIR, exist_ok=True)


def get_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }


def snapshot_and_delete(token, endpoint_resource, entity_id, label):
    headers = get_headers(token)
    url = f"{API_BASE}/{endpoint_resource}/{entity_id}?world_id={WORLD_ID}"
    
    # 1. Snapshot
    try:
        req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        snap_path = os.path.join(SNAPSHOT_DIR, f"{endpoint_resource}_{entity_id}_{label.replace(' ', '_')}.json")
        with open(snap_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  [SNAPSHOT] {label} salvato in {snap_path}")
    except Exception as e:
        print(f"  [WARN] Snapshot fallito per {label} ({entity_id}): {e}")

    # 2. Delete
    try:
        del_req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}, method='DELETE')
        with urllib.request.urlopen(del_req) as resp:
            print(f"  [DELETED] {label} ({entity_id}): status {resp.status}")
            return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"  [ALREADY DELETED] {label} ({entity_id}) non esiste piu (404)")
            return True
        print(f"  [ERROR] Eliminazione fallita per {label} ({entity_id}): HTTP {e.code}")
        return False
    except Exception as e:
        print(f"  [ERROR] Eliminazione fallita per {label} ({entity_id}): {e}")
        return False


def put_entity(token, endpoint_resource, entity_id, payload, label):
    headers = get_headers(token)
    url = f"{API_BASE}/{endpoint_resource}/{entity_id}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f"  [UPDATED] {label} ({entity_id}): status {resp.status}")
            return res
    except Exception as e:
        print(f"  [ERROR] Aggiornamento fallito per {label} ({entity_id}): {e}")
        return None


def run():
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    # =========================================================================
    # PARTE 1 — PULIZIA E UNIFICAZIONE LOCATION
    # =========================================================================
    print("=== PARTE 1.1: UNIFICAZIONE E PULIZIA ALYSSA'S OMEGA NEST ===")
    
    # 1. Aggiorna Villa Douglas: Alyssa's Sanctuary / Omega Nest con tutte le info uniche della vecchia
    alyssa_nest_unified_context = (
        "Ricavato all'interno dell'ex solarium al terzo piano di Villa Douglas, il santuario privato di Alyssa e il punto piu protetto, "
        "isolato e sacro dell'intera tenuta: la cellula di rigenerazione e nido biologico per la White Moon. "
        "L'ambiente e dotato di oscuramento totale tramite pannelli pesanti anti-luce UV e insonorizzazione acustica di grado militare "
        "per schermare completamente rumori esterni o comandi vocali degli Alpha. Grandi vetrate blindate con filtri solari polarizzati "
        "possono essere aperte per rivelare la vista panoramica sui boschi di Seven Hills e sulla costa californiana. "
        "Un sistema di micro-ventilazione dedicato permette ad Alyssa di saturare l'aria esclusivamente con i propri feromoni naturali o con "
        "quelli di un partner approvato, mantenendo una temperatura calda e costante ideale per la gestione della Heat o per il recupero da trauma. "
        "L'accesso e strettamente controllato e limitato biometricamente. Biosensori invisibili monitorano discretamente i parametri vitali di Alyssa: "
        "qualora dovessero deviare bruscamente per panico sensoriale o shock, scatta un segnale silenzioso diretto unicamente ai terminali di Erik e Malachia. "
        "L'interno e un abisso di morbidezza: cashmere, lana merino, seta e pesanti coperte che trattengono il calore corporeo, in una palette cromatica "
        "rilassante nei toni crema, grigio perla e tocchi di giallo caldo, priva di angoli vivi o superfici dure. Al centro della stanza, sollevato su "
        "un soppalco in legno chiaro, si trova il nido: piumini soffici e cuscini in velluto intrecciati con vecchie felpe e indumenti che portano l'odore "
        "rassicurante del gemello Jasper, del padre e dei fratelli. L'aria odora densamente di latte caldo, miele selvatico, fiori di luna e lavanda essiccata. "
        "Per Alyssa il Nest non e soltanto un rifugio fisico, ma una barriera metafisica contro il mondo esterno: l'unico luogo in cui puo abbassare la guardia, "
        "cessare di essere il pilastro emotivo del branco e permettersi di essere vulnerabile, protetta e accolta."
    )

    canonical_nest_id = '_kfXfwkXrzPTRetcBmUt9T'
    old_nest_id = '_y4DhWPWPfU6Mt3dcxyj2e'

    put_entity(token, 'locations', canonical_nest_id, {
        "context_description": alyssa_nest_unified_context,
        "keys": ["Villa Douglas Alyssa's Sanctuary", "Alyssa's Sanctuary", "Omega Nest", "Nido di Alyssa", "Stanza di Alyssa", "ex-solarium", "Alyssas nest", "third floor solarium"],
        "secondary_keys": ["Alyssa", "nido", "Omega", "miele", "terzo piano", "solarium", "sanctuary", "refuge", "bolthole"],
        "key_logic": "AND_ANY",
        "case_sensitive": False,
        "whole_words_only": True
    }, "Villa Douglas: Alyssa's Sanctuary / Omega Nest (Unificato)")

    # Elimina vecchia location duplicata
    snapshot_and_delete(token, 'locations', old_nest_id, "Vecchia Alyssa's Omega Nest")

    print("\n=== PARTE 1.2: TRASFERIMENTO INFO DA LEXICON A LOCATION & ELIMINAZIONE DUPLICATI ===")
    
    # The Roasted Bean
    roasted_bean_loc_id = '_XUV6jWXTXG6wgj2WKBEpr'
    roasted_bean_lex_id = '_pFUMj4B4BBnLkfEqJBykg'
    roasted_bean_context = (
        "The Roasted Bean sits behind the Griffin Clocktower at SUCC and runs on academic stress and sensory overload. "
        "The air is thick with the scents of burnt sugar, roasted arabica and ozone. It was among the very first stops for the "
        "Douglas-Bloodmoon siblings on their first day of classes at SUCC.\n\n"
        "The counter is fast, staffed by a rotating crew of vampires and demi-humans known for elaborate piercings. The window seats "
        "look out over the Lunar Quad and are the most fought-over tables in the building, though anyone with security training reads "
        "them as exposed on three sides, which is a thing Malachia notices and nobody else does. The corner tables have reinforced outlets "
        "and are known as the Tech Nook, permanently occupied by hackers and research students.\n\n"
        "On the board: specialty lattes customised with honey, cinnamon and anise; glazed cinnamon rolls served warm; dense triple chocolate "
        "brownies bought almost exclusively for stress-eating; and a high-potency roast called The Final Exam, which does exactly what the name says."
    )
    put_entity(token, 'locations', roasted_bean_loc_id, {
        "context_description": roasted_bean_context,
        "keys": ["The Roasted Bean", "Roasted Bean", "Roasted Bean coffee shop"]
    }, "The Roasted Bean (Location aggiornata)")
    snapshot_and_delete(token, 'lexicon', roasted_bean_lex_id, "The Roasted Bean (Lexicon duplicato)")

    # Lunar Quad
    lunar_quad_loc_id = '_WrymW8qTETkm7r1QXQGaT'
    lunar_quad_lex_id = '_DynQQkknmLeFWwy3nJHxt'
    lunar_quad_context = (
        "Il piazzale centrale del SUCC, incrocio nevralgico della vita studentesca. Affollato a tutte le ore da migliaia di studenti soprannaturali. "
        "All'ingresso svetta lo striscione 'Welcome Freshman 2024!', costantemente monitorato dall'alto dalla discreta sorveglianza aerea dei droni DCC.\n\n"
        "Prato calpestato e cemento chiaro accecante sotto il sole, gruppi sparsi sulle panchine e sull'erba, biciclette abbandonate ovunque. "
        "Il chiacchiericcio sovrapposto di decine di specie diverse, qualcuno che ripassa ad alta voce, qualcuno che dorme sullo zaino. "
        "Da qui si vede la Griffin Clocktower e si raggiunge tutto il resto del campus.\n\n"
        "Nelle sere in cui non si tiene a Nocturnal Hall (a rotazione stagionale), il Lunar Quad ospita anche le riunioni del martedi di The Pack, "
        "la societa ufficiale were e canide/lupina del campus.\n\n"
        "Al centro del piazzale c'e la fontana decorativa della luna. La sua faccia riproduce sempre la fase lunare corrente, quindi cambia di notte "
        "in notte, ed e il modo piu veloce che ha chiunque attraversi il campus per sapere a che punto e il mese. Nei giorni intorno alla luna piena "
        "il piazzale si riempie molto oltre il solito.\n\n"
        "[LOCATION INSTRUCTIONS: Luogo di passaggio e di incontri casuali. Qualcuno di conosciuto puo sempre comparire qui senza bisogno di spiegazioni. "
        "Spazio pubblico e visibile: le conversazioni private qui vengono sentite.]"
    )
    put_entity(token, 'locations', lunar_quad_loc_id, {
        "context_description": lunar_quad_context,
        "keys": ["Lunar Quad", "piazza del SUCC", "piazzale del SUCC", "Lunar Quad SUCC"]
    }, "Lunar Quad (Location aggiornata)")
    snapshot_and_delete(token, 'lexicon', lunar_quad_lex_id, "Lunar Quad (Lexicon duplicato)")

    # Dragon's Shortcut
    dragons_shortcut_lex_id = '_6KpjDR4jFQGggrMXFJdh8'
    snapshot_and_delete(token, 'lexicon', dragons_shortcut_lex_id, "Dragon's Shortcut (Lexicon duplicato errato)")

    print("\n=== PARTE 1.3: DIVISIONE THE CABLE DISTRICT E THE VOID ===")
    cable_district_id = '_RVRf9PtEdwhGt3rGGFjMC'
    the_void_id = '_xJ9zaHVxUNnWw6UwwpAVe'

    # Aggiorna Cable District (rimuovi The Void dal nome e dalle chiavi)
    cable_context = (
        "Chicago's notorious industrial grey zone, situated in the Old Warehouses Sector. A dense, foreboding labyrinth of suspended "
        "high-voltage cables, hissing steam conduits, and heavily unstable aetheric ley-lines. While nominally subject to municipal law, "
        "it is de facto governed by syndicate bosses, energy barons, and black-market operators who thrive in the shadow of heavy industry."
    )
    put_entity(token, 'locations', cable_district_id, {
        "name": "The Cable District",
        "keys": ["The Cable District", "Cable District", "Old Warehouses Sector"],
        "context_description": cable_context
    }, "The Cable District (Rinominato e ripulito)")

    # Aggiorna The Void (imposta parent = Cable District, assegna chiavi e descrizione)
    the_void_context = (
        "Club sotterraneo e centro nevralgico clandestino situato nei livelli interrati del settore vecchi magazzini industriali "
        "all'interno del Cable District. Operante nella zona d'ombra al limite della legalita e protetto dall'influenza degli Ironhorn Nomads, "
        "The Void funge da snodo per lo scambio di dati riservati, compravendita di hardware modificato, comunicazioni criptate, contrabbando "
        "tecnologico e bazar di cristalli di mana grezzo, in un'area in cui le linee eteriche e i campi magnetici industriali schermano "
        "qualsiasi intercettazione convenzionale."
    )
    put_entity(token, 'locations', the_void_id, {
        "parent_location_id": cable_district_id,
        "keys": ["The Void", "The Void Club", "The Void Ironworks"],
        "secondary_keys": ["bazar", "club sotterraneo", "black market", "magazzini"],
        "context_description": the_void_context
    }, "The Void (Parent impostato su Cable District)")

    print("\n=== PARTE 1.4: FORT MACARTHUR E LOS ANGELES ===")
    fort_macarthur_id = '_cDDqVXg3jbxEhBd3qJ3ME'
    los_angeles_id = '_X4A8gWVr43a7dRr9TbJ4m'
    put_entity(token, 'locations', fort_macarthur_id, {
        "parent_location_id": los_angeles_id,
        "keys": ["Fort MacArthur", "S.R.F.", "military", "Alpha squad"],
        "secondary_keys": ["Los Angeles", "base militare", "presidio militare", "San Pedro"]
    }, "Fort MacArthur (Parent LA, chiave spostata in secondary)")

    # =========================================================================
    # PARTE 2 — PULIZIA, UNIFICAZIONE E TIPIZZAZIONE LEXICON
    # =========================================================================
    print("\n=== PARTE 2.1: PULIZIA DOPPIONI STORICI LEXICON ===")

    # 1. Valentine Rossfeld Stub
    val_stub_id = '_7C6ehhGXMqcF6gKEbcPrb'
    snapshot_and_delete(token, 'lexicon', val_stub_id, "[OBSOLETE DUPLICATE] Valentine Rossfeld")

    # 2. Ironhorn Nomads MC duplicato
    ironhorn_canonical_id = '_eVzj3Ve4fxDCXyAmc9qXD'
    ironhorn_old_id = '_nfnLQgmj11V2pmMzGV7Tq'
    put_entity(token, 'lexicon', ironhorn_canonical_id, {
        "keys": ["Ironhorn Nomads", "Ironhorn Nomads MC", "Ironhorn Nomads Motorcycle Club", "Nomads MC", "Obsidian Blades", "biker gang", "Ironworks gang"]
    }, "Ironhorn Nomads MC (Chiavi unificate)")
    snapshot_and_delete(token, 'lexicon', ironhorn_old_id, "Ironhorn Nomads Motorcycle Club (Bozza duplicata)")

    # 3. Item: Jasper's Porsche unificata
    porsche_canonical_id = '_AnjFMMp2TXJebQWUHKMYW'
    porsche_old_id = '_Hk8fbwR2qnc7qyn87w7KE'
    porsche_unified_content = (
        "Jasper Bloodmoon's custom matte black Porsche 911, its factory paint buried under a wraparound mural of fluorescent acid-green "
        "street art, tags, drips, and a stylized wolf howling across the hood with the vanity license plate 'DJ-FRQ'. "
        "Under the hood it is pure high-performance engineering, featuring heavily sound-dampened interiors, concealed weapon compartments, "
        "and an overclocked audio subwoofer system crammed into what used to be the back seats, wired directly to a professional mixing setup. "
        "Capable of vibrating nearby structures and masking arcane signatures, Jasper pops the trunk to turn parking lots into impromptu live sets. "
        "The Douglas security detail hates it, and Jasper loves that they hate it."
    )
    put_entity(token, 'lexicon', porsche_canonical_id, {
        "content": porsche_unified_content,
        "keys": ["Porsche di Jasper", "DJ-FRQ", "Jasper's Porsche", "Custom Porsche", "Porsche 911 di Jasper"]
    }, "Porsche Custom di Jasper (DJ-FRQ) (Unificata)")
    snapshot_and_delete(token, 'lexicon', porsche_old_id, "Jasper's Porsche (Duplicato)")

    # 4. Item: Portafoglio unificato con Wallet
    portafoglio_id = '_bPh4kGmBQWczPJW2yf7G6'
    wallet_old_id = '_PRnARzHmDLjC2ELUCFP2A'
    portafoglio_content = (
        "Un portafoglio in pelle consumata contenente documenti personali, tessere d'accesso, qualche carta di credito e i contanti sopravvissuti alla serata precedente."
    )
    put_entity(token, 'lexicon', portafoglio_id, {
        "content": portafoglio_content,
        "keys": ["Portafoglio", "portafoglio", "wallet", "Wallet"]
    }, "Portafoglio (Arricchito con dettagli Wallet)")
    snapshot_and_delete(token, 'lexicon', wallet_old_id, "Wallet (Duplicato inglese)")

    # 5. Abilità: The Absolute Pacifist Vow
    vow_id = '_rrWzpe1tcr8f8URgMNMDf'
    put_entity(token, 'lexicon', vow_id, {
        "type": "ability"
    }, "The Absolute Pacifist Vow (Type -> ability)")

    print("\n=== PARTE 2.2: CONVERSIONE 14 MEMORY CON DATA SPECIFICA IN TYPE 'EVENT' ===")
    events_to_convert = [
        ('_HBPbn7GG6C91bGHd2MPp2', '2026-04-22 Alyssa compie 21 anni e diventa Pack Mom'),
        ('_wrTH8P9nDTrwWD6YpdXKm', '2024-06-05 Disneyland con lo zio Logan'),
        ('_KEK3YY9gcadUH3qdaU9t2', "2024-08-21 L'accordo Wolfwood-Douglas"),
        ('_xfHb6W1tpMtYgDWjGyTY9', '1887 Fondazione della SUCC'),
        ('_GxhgVnn4brPz4x39Qcb9D', '2002 La SUCC apre agli studenti umani'),
        ('_mwmXfD1cW9B1tmptgDWrQ', '1999 Nocturnal Crisis'),
        ('_yawHCFKdE7cEEqy8YELTY', '2024-04-13 Admitted Student Days (SUCC)'),
        ('_XDR8caVC3BEcKU8qXbw8a', '2024-04-22 Compleanno dei gemelli e festa di Wulfnic'),
        ('_HpWLBadUEPJf1EQYwgAmR', '2024-05-01 National College Decision Day'),
        ('_aaQJ1aXtbc4cmeNUa8MJG', '2024-07-15 Road trip con Logan'),
        ('_j9n7hfXrxW9Y29yTyn27T', '2024-08-19 Full Moon Festival'),
        ('_fdaTEhbC9fHGY84t2KDLy', '2024-08-25 Pranzo della domenica'),
        ('_nmrk3jbXPeXqr4X16A3d9', '2024-08-26 Primo giorno alla SUCC'),
        ('_cU7JNJgP7kBKhej3nUDWj', '2024-10-31 Halloween University Party'),
    ]

    for ev_id, ev_name in events_to_convert:
        put_entity(token, 'lexicon', ev_id, {"type": "event"}, f"Event: {ev_name}")

    print("\n=== PARTE 2.3: CONVERSIONE 151 SCHEDE NPC G3 IN TYPE 'NPC' ===")
    d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    lexicon_all = d.get('world_lexicon_entries', [])

    npc_count = 0
    for item in lexicon_all:
        iid = item.get('id')
        name = item.get('name', '')
        content = item.get('content', '').strip()
        curr_type = item.get('type')

        # Identify G3 NPCs: starts with [NAME: and is currently lore/concept
        # Exclude already processed or deleted items
        if iid in [val_stub_id, vow_id] or iid in [x[0] for x in events_to_convert]:
            continue

        if content.startswith('[NAME:') and curr_type == 'lore/concept':
            res = put_entity(token, 'lexicon', iid, {"type": "npc"}, f"NPC G3: {name}")
            if res:
                npc_count += 1

    print(f"\nTotale NPC G3 convertiti a type 'npc': {npc_count}")
    print("\nOperazione completata con successo.")


if __name__ == '__main__':
    run()
