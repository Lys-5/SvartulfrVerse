import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token, sync_world

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def api_request(resource, item_id='', method='GET', payload=None, token=None):
    if not token:
        token = get_auth_token()
    
    if item_id:
        url = f"{API_BASE}/{resource}/{item_id}?world_id={WORLD_ID}"
    else:
        url = f"{API_BASE}/{resource}?world_id={WORLD_ID}"
        
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    data = json.dumps(payload).encode('utf-8') if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.")

    # =========================================================================
    # STEP 1: SNAPSHOT AND SAFELY DELETE 6 GHOST CARDS
    # =========================================================================
    print("\n--- STEP 1: Snapshot e cancellazione sicura 6 schede ghost duplicate ---")
    ghost_ids = [
        ('_Y8VPp7PwtHCCgnEzd6qkK', 'Marcus Thornfield (Ghost)'),
        ('_gYagUj1CAE7grnRCVLnyU', 'Malachia Douglas Bloodmoon (Ghost)'),
        ('_xLGRAXycw4eXVMdGYqbqf', 'Magnus Douglas III (Ghost)'),
        ('_gCzaABFtVKTVCwcHmNGW6', 'Logan Douglas (Ghost)'),
        ('_Rwb3wetNrX4CfEpYDJ4HE', 'Angelo Moreno (Ghost)'),
        ('_6h1dDQpmqTAckYaWRT2er', 'Dominic Chen (Ghost)')
    ]

    snapshots = {}
    for cid, label in ghost_ids:
        try:
            char_data = api_request('characters', cid, method='GET', token=token)
            snapshots[cid] = char_data
            print(f"  [SNAPSHOT OK] {label} [{cid}]")
        except Exception as e:
            print(f"  [SNAPSHOT ERRORE] {label} [{cid}]: {e}")

    with open('exports/ghost_characters_snapshot.json', 'w', encoding='utf-8') as f:
        json.dump(snapshots, f, indent=2, ensure_ascii=False)
    print("Tutti gli snapshot delle schede ghost salvati in exports/ghost_characters_snapshot.json")

    # Now execute DELETE one by one
    for cid, label in ghost_ids:
        try:
            api_request('characters', cid, method='DELETE', token=token)
            print(f"  [DELETE OK] Cancellata scheda ghost {label} [{cid}]")
        except Exception as e:
            print(f"  [DELETE ERRORE] {label} [{cid}]: {e}")

    # =========================================================================
    # STEP 2: FORMATTING CLEANUP (NOAH & EM-DASHES)
    # =========================================================================
    print("\n--- STEP 2: Correzione formattazione (Noah JED+ e 3 Em-dash) ---")

    # 1. Noah Douglas Bloodmoon
    noah_id = '_r42cVzMjcGTAx7bR1DQVt'
    try:
        noah = api_request('characters', noah_id, method='GET', token=token)
        ls = noah.get('long_summary') or ''
        if ls.startswith('# [Noah]\n\n'):
            new_ls = ls[len('# [Noah]\n\n'):]
            api_request('characters', noah_id, method='PUT', payload={'long_summary': new_ls}, token=token)
            print("  [OK] Ripulita intestazione '# [Noah]' da Noah Douglas Bloodmoon.")
        elif ls.startswith('# [Noah]'):
            new_ls = ls[len('# [Noah]'):].lstrip()
            api_request('characters', noah_id, method='PUT', payload={'long_summary': new_ls}, token=token)
            print("  [OK] Ripulita intestazione '# [Noah]' da Noah Douglas Bloodmoon.")
        else:
            print("  [SKIP] Noah non necessita modifiche o già ripulito.")
    except Exception as e:
        print(f"  [ERRORE] Fix Noah: {e}")

    # 2. Rory's Estate location em-dash
    rory_id = '_TLEaxwQCB24kQYfYHy8pq'
    try:
        rory = api_request('locations', rory_id, method='GET', token=token)
        desc = rory.get('context_description') or rory.get('description') or ''
        clean_desc = desc.replace('—', ', ').replace('–', ', ')
        api_request('locations', rory_id, method='PUT', payload={'context_description': clean_desc, 'description': clean_desc}, token=token)
        print("  [OK] Ripulito em-dash da Rory's Estate.")
    except Exception as e:
        print(f"  [ERRORE] Fix Rory's Estate: {e}")

    # 3. Bloodline Selection Strategy lexicon em-dash
    bss_id = '_X9mjTXheUBkX7nwDYr49f'
    try:
        bss = api_request('lexicon', bss_id, method='GET', token=token)
        content = bss.get('content') or ''
        clean_content = content.replace('—', ', ').replace('–', ', ')
        api_request('lexicon', bss_id, method='PUT', payload={'content': clean_content}, token=token)
        print("  [OK] Ripulito em-dash da Bloodline Selection Strategy.")
    except Exception as e:
        print(f"  [ERRORE] Fix Bloodline Selection Strategy: {e}")

    # 4. Vampiric Aesthetic Seduction lexicon em-dash
    vas_id = '_7MPnV2X9cLB86WUhmJKyp'
    try:
        vas = api_request('lexicon', vas_id, method='GET', token=token)
        content = vas.get('content') or ''
        clean_content = content.replace('—', ', ').replace('–', ', ')
        api_request('lexicon', vas_id, method='PUT', payload={'content': clean_content}, token=token)
        print("  [OK] Ripulito em-dash da Vampiric Aesthetic Seduction.")
    except Exception as e:
        print(f"  [ERRORE] Fix Vampiric Aesthetic Seduction: {e}")

    # =========================================================================
    # STEP 3: POPULATE 7 EMPTY LOCATIONS & REFINE ARMA BASE
    # =========================================================================
    print("\n--- STEP 3: Popolamento 7 Location vuote e rifinitura Arma Base ---")

    loc_updates = [
        (
            '_4FMaQm3xQCUVHeRf3AWYk',
            'Library Basement Meeting Room 005',
            'A restricted basement study and seminar chamber concealed beneath the ancient gothic stone vaults of the SUCC Basilica Library. Encased by massive oak doors reinforced with arcane containment wards, the quiet room features archival bookshelves, dim crystal sconces casting amber light, slate floors traced with protective chalk circles, and a long scarred wooden conference table where faculty, senior researchers, and private occult student societies convene confidential deliberations away from public ears.'
        ),
        (
            '_Ra4fXd8BEdKUeKTbGAw3b',
            'Storage & Supplies',
            'A sprawling subterranean logistics hub and supply depot located in the lower sub-levels. Heavy-duty industrial steel shelving stretches from floor to ceiling, systematically organized with alchemical ingredients, enchanted storage containers, emergency medical supplies, tactical surplus gear, and silver-lined containment restraints. Smells of ozone, corrugated cardboard, hydraulic oil, and bundles of dried protective herbs.'
        ),
        (
            '_h9UDyMzPtBwnzfbjj3DP3',
            'Ventura Square',
            'The sunlit historic central plaza of Ventura, California. Paved with smooth weathered flagstones and fringed with tall Pacific palms, the square features Spanish mission-revival architecture, open-air cafes, artisan craft kiosks, and broad tiled fountains. A vibrant public gathering hub where coastal residents, university students on weekend trips, and discreet supernatural travelers mingle freely under the cooling sea breeze.'
        ),
        (
            '_Mq1DYmKdnkR83YBjNRyXr',
            'Solarton Square',
            'The bustling town plaza at the commercial heart of Solarton, situated within easy walking distance from the SUCC campus perimeter. Framed by charming brick facades, outdoor dining terraces catering to both human and non-human diets, occult apothecaries, and novelty bookstores, the square serves as the social crossroads for the entire student body and hosts signature regional gatherings including the monthly Full Moon Market and the lively annual Solar Festival.'
        ),
        (
            '_82cNpDwVJwVd8qGRUgFw8',
            'Simi Valley Infopoint',
            'A discreet municipal transit pavilion and civic information kiosk nestled against the scenic hillsides of Simi Valley. Featuring regional route schedules, emergency contact terminals, and unobtrusive administrative assistance, the facility serves as a practical transit station for cross-county commuters and newly arriving supernatural residents entering the Greater Los Angeles metropolitan corridor.'
        ),
        (
            '_16nUQjhqXaFaUEKy1zgpA',
            'Pershing Square',
            'The iconic urban park and public square situated in Downtown Los Angeles. Distinguished by its modernist purple campanile bell tower, sunken gardens, palm groves, and concrete terraces, the plaza is framed on all sides by soaring corporate skyscrapers and historic hotels. A dense civic intersection where business professionals, supernatural couriers, night-shift operatives, and city residents cross paths at all hours.'
        ),
        (
            '_11LzwJB9B6rGrEQTTd7xd',
            'Bakersfield Square',
            'The broad civic centerpiece of downtown Bakersfield, California. Characterized by wide sunbaked avenues, red-brick municipal halls, classic clock towers, and heat-resistant desert landscaping, the square acts as a prominent Central Valley hub where regional logistics, agricultural commercial interests, and inland supernatural packs intersect.'
        )
    ]

    for lid, name, desc in loc_updates:
        try:
            api_request('locations', lid, method='PUT', payload={'context_description': desc, 'description': desc}, token=token)
            print(f"  [OK] Aggiornata descrizione location {name} [{lid}]")
        except Exception as e:
            print(f"  [ERRORE] Update location {name} [{lid}]: {e}")

    # Refine Arma Base
    arma_base_id = '_XyPQbcYGhh7FbQTN4Py2p'
    arma_base_desc = 'A dependable, concealed self-defense weapon kept close for personal protection in the unpredictable supernatural underworld. Well-maintained, balanced, and discreet enough to carry under casual clothing or within an inner jacket pocket.'
    try:
        api_request('lexicon', arma_base_id, method='PUT', payload={'content': arma_base_desc}, token=token)
        print("  [OK] Rifinita descrizione item 'Arma Base'.")
    except Exception as e:
        print(f"  [ERRORE] Update Arma Base: {e}")

    # =========================================================================
    # STEP 4: OUTFITS FOR THE 4 DARKFIRE DEMONS
    # =========================================================================
    print("\n--- STEP 4: Assegnazione set di Outfits per i 4 demoni Darkfire ---")

    darkfire_outfits = {
        # Boros Darkfire
        '_aaWfLtx19WQR7JyHKDBem': [
            {
                'name': 'Abiti da Lavoro Logistica & Deposito',
                'description': 'Abbigliamento: maglietta a maniche corte color carbone in cotone pesante rinforzato che lascia scoperte le braccia possenti e la pelle granitica, pantaloni cargo industriali scuri con cuciture triple.\nAccessori: cintura da carico con fibbia metallica rinforzata, bracciali in cuoio spesso per sostenere i polsi.\nScarpe: scarponi da lavoro antinfortunistici rinforzati con punta in acciaio brunito e suola spessa a carrarmato.\nGioielli: robusto anello in ferro battuto con incisione della runa della terra al pollice destro.\nTrucco: nessun trucco; polvere minerale e tracce di grafite sulla pelle scura, occhi ambrati calmi e attenti.\nAcconciatura: capelli neri corti e ordinati attorno alle corna ricurve da Vax della terra.'
            },
            {
                'name': 'Tenuta Cerimoniale Sotterranea',
                'description': 'Abbigliamento: ampia tunica cerimoniale senza maniche in lino grezzo color ocra scuro e ardesia, fissata da una pesante cintura di cuoio decorata con borchie in ferro nero e piastre di basalto levigato.\nAccessori: stendardo cerimoniale del Guardiano del Clan, fascia in tessuto pesante sui fianchi.\nScarpe: calzari cerimoniali in cuoio scuro rinforzati con lamine metalliche.\nGioielli: collare rigido in ferro grezzo con sigillo di casata Darkfire incastonato sul petto.\nTrucco: pittura rituale color terracotta tracciata geometricamente sugli avambracci e sulle spalle.\nAcconciatura: chioma raccolta all indietro con un fermaglio in bronzo antico tra le corna imponenti.'
            },
            {
                'name': 'Casual da Relax & Cucina',
                'description': 'Abbigliamento: canotta scura morbida in tessuto traspirante, comodi pantaloni larghi in lino antracite con coulisse elastica, grembiule da cuoco in pelle scamosciata marrone scuro.\nAccessori: canovaccio in lino infilato nella cintura del grembiule per quando cucina per i fratelli.\nScarpe: comode calzature aperte da interno in cuoio morbido sagomato.\nGioielli: semplice catenina in ferro con un pendente a forma di martello da forgia.\nTrucco: viso rilassato e accogliente, espressione rassicurante e bonaria.\nAcconciatura: capelli sciolti leggermente mossi, corna levigate e pulite.'
            },
            {
                'name': 'Assetto da Battaglia / Baluardo di Pietra',
                'description': 'Abbigliamento: pesante corazza pettorale segmentata in ferro nero forgiato a caldo, spallacci massicci in pietra lavica incantata e bracciali d arme completi.\nAccessori: grande scudo torre a goccia in ferro battuto e cinghie di ritegno balistico.\nScarpe: stivali corazzati con schinieri in ferro nero che si ancorano stabilmente a terra.\nGioielli: anelli runici che pulsano di tenue luminescenza color ambra quando attiva l indurimento minerale.\nTrucco: crepe luminose di mana terroso che si accendono lungo le braccia e il collo pietrificato.\nAcconciatura: capelli legati stretti a ciuffo guerriero per non intralciare la visuale tra le corna corazzate.'
            }
        ],
        # Karshin Darkfire
        '_Agf7FxKMzPDFJj3gktYtz': [
            {
                'name': 'Equipaggiamento Tattico di Sicurezza HSK',
                'description': 'Abbigliamento: uniforme tattica corporativa completamente nera in tessuto antistrappo balistico, gilet tattico sagomato in kevlar che lascia scoperte le spalle e le braccia muscolose segnate da cicatrici rituali.\nAccessori: fondine cosciali rinforzate per armi da sfondamento, guanti tattici senza dita con nocche rinforzate in fibra di carbonio.\nScarpe: anfibi da combattimento neri impermeabili con suola ammortizzata silenziosa.\nGioielli: orecchino a spuntone in acciaio brunito sull orecchio destro.\nTrucco: nessun trucco; sguardo affilato e famelico, cicatrici evidenti sul collo e sulle braccia.\nAcconciatura: capelli neri rasati sui lati e leggermente più lunghi sulla cresta centrale tra le corna affilate.'
            },
            {
                'name': 'Gala & Scorta Esecutiva',
                'description': 'Abbigliamento: completo formale scuro su misura, camicia nera in seta elasticizzata con colletto aperto senza cravatta, giacca monopetto sartoriale con fodera in seta rosso cremisi.\nAccessori: auricolare di sicurezza cifrato invisibile, guanti sottili in pelle d agnello nera.\nScarpe: scarpe eleganti Oxford in pelle nera lucidata a specchio.\nGioielli: fermaglio in platino e ossidiana sulla tasca interna della giacca.\nTrucco: pelle curata, postura minacciosa e letale celata dietro un portamento impeccabile.\nAcconciatura: capelli neri tirati a lucido con cera opaca, corna lucide e riflettenti.'
            },
            {
                'name': 'Abbigliamento da Interrogatorio / Sala d Addestramento',
                'description': 'Abbigliamento: canotta nera elasticizzata impregnata del profumo di cenere e ferro caldo, pantaloni militari neri infilati negli stivali da addestramento.\nAccessori: cinghie di contenimento e strumenti di coercizione agganciati alla cintura in cuoio rinforzato.\nScarpe: stivaletti da lotta neri aderenti con suola in gomma antiscivolo.\nGioielli: fascia di metallo zigrinato all avambraccio sinistro.\nTrucco: sfumatura scura e minacciosa attorno agli occhi cremisi, sorriso crudele e beffardo.\nAcconciatura: capelli spettinati e madidi di sudore dopo il combattimento corpo a corpo.'
            },
            {
                'name': 'Tenuta Tradizionale da Caccia',
                'description': 'Abbigliamento: vesti tradizionali Vax in pelle nera conciata e scaglie metalliche, mantello corto asimmetrico e collare di zanne e spuntoni in osso scuro.\nAccessori: faretra con dardi da caccia sotterranea e lame corte a scatto.\nScarpe: calzari da predatore in cuoio silenzioso con rinforzi alle caviglie.\nGioielli: anelli dentellati da combattimento sui medi di entrambe le mani.\nTrucco: polvere di carbone sfumata sugli zigomi per mimetizzarsi nel buio totale.\nAcconciatura: ciocche scure lasciate selvagge che ricadono sul viso attorno alle corna nere.'
            }
        ],
        # Aras Darkfire
        '_8catGJE98MTpfaajJD9zV': [
            {
                'name': 'Abito Sartoriale Corporate HSK',
                'description': 'Abbigliamento: completo a tre pezzi su misura in lana finissima color antracite con gessatura impercettibile color prugna, camicia in seta avorio con colletto diplomatico e cravatta in seta bordeaux.\nAccessori: fermacravatta d argento lavorato a filigrana, pochette da taschino coordinata in seta, ventiquattrore sottile in pelle pregiata.\nScarpe: scarpe eleganti modello Derby in pelle color testa di moro spazzolata a mano.\nGioielli: gemelli da polso in argento con ametiste scure incastonate.\nTrucco: incarnato perfetto, labbra leggermente scure, sguardo suadente e ipnotico.\nAcconciatura: capelli neri ondulati lunghi fino alle spalle, curatissimi e pettinati all indietro con grazia attorno alle corna slanciate.'
            },
            {
                'name': 'Ricevimento d Alta Società',
                'description': 'Abbigliamento: smoking serale in velluto nero notte con revers a lancia in raso lucido, camicia da sera candida con abbottonatura nascosta e pantaloni da sera sartoriali a taglio vivo.\nAccessori: sciarpa di seta da sera bicolore nero e cremisi adagiata morbidamente sulle spalle.\nScarpe: pantofole eleganti da sera in velluto nero con suola in cuoio sottile.\nGioielli: spilla da giacca in platino raffigurante un serpente alato avvolto su una gemma viola.\nTrucco: leggera polvere illuminante minerale sugli zigomi, fascino aristocratico irresistibile.\nAcconciatura: chioma fluente semiraccolta con un nastro di seta scura, corna ornate da sottili anelli d argento.'
            },
            {
                'name': 'Vesti Cerimoniali Sotterranee in Seta',
                'description': 'Abbigliamento: lunga veste fluttuante cerimoniale in pura seta d ombra nera e viola scuro, intessuta con fili d argento che riflettono la luce come ragnatele notturne.\nAccessori: scettro oratorio corto con prisma di quarzo d ombra all estremità.\nScarpe: babbucce cerimoniali in morbida pelle scura prive di suola rigida.\nGioielli: anello sigillo in oro bianco con sigillo magico per la tessitura di illusioni.\nTrucco: sottile linea di ombretto violaceo sfumato che esalta la natura arcana del Vax.\nAcconciatura: capelli completamente sciolti che ondeggiano morbidi assecondando i movimenti della seta.'
            },
            {
                'name': 'Notturno / Spionaggio & Intrigo',
                'description': 'Abbigliamento: dolcevita nero aderente in cashmere finissimo, pantaloni scuri su misura a taglio dritto e un lungo cappotto sartoriale in panno di lana che ondeggia come fumo denso a ogni passo.\nAccessori: guanti sottili in pelle di cervo scura che non lasciano impronte, occhiali da sole con montatura minimalista in titanio brunito.\nScarpe: stivaletti Chelsea in pelle nera con suola in gomma ultra-silenziosa.\nGioielli: nessun monile riflettente o metallico.\nTrucco: espressione neutra e imperscrutabile che dissimula qualsiasi intenzione.\nAcconciatura: capelli legati in una coda bassa per passare inosservato sotto il bavero del cappotto.'
            }
        ],
        # Varg Darkfire
        '_bh8AHn7WKkNTnLjwXrUWE': [
            {
                'name': 'Mantello del Patriarca & Pelli Sotterranee',
                'description': 'Abbigliamento: pesante mantello da guerra in pelliccia spessa di bestia cavernicola, foderato in cuoio indurito e trattenuto sulle spalle da due enormi fibbie a testa di drago in ferro nero battuto, tunica da guerra scura e pantaloni in cuoio pesante.\nAccessori: larga cintura borchiata con piastre di ferro e corno, pipa intagliata in legno fossile.\nScarpe: alti stivali invernali in spessa pelle bovina con suola chiodata in ferro battuto.\nGioielli: antico torque in ferro grezzo ritorto attorno al collo massiccio.\nTrucco: rughe profonde e cicatrici di guerra venerabili, barba corta sale e pepe, occhi d ambra antica.\nAcconciatura: criniera brizzolata legata in trecce tradizionali che scendono ai lati delle corna nodose e imponenti.'
            },
            {
                'name': 'Tenuta Formale da Consiglio HSK',
                'description': 'Abbigliamento: lunga giubba cerimoniale scura dal taglio austero e imponente, decorata con bordature geometriche tradizionali Vax cucite in filo di rame ossidato e bottoni in corno nero.\nAccessori: bastone da passeggio in legno pietrificato con pomo sferico in ferro nero.\nScarpe: stivali in cuoio scuro lavorato con fibbie laterali in metallo antico.\nGioielli: pesante anello del patriarca al mignolo sinistro con pietra tombale incastonata.\nTrucco: portamento maestoso e inflessibile carico di otto secoli di autorità indiscutibile.\nAcconciatura: barba pettinata e fermata con due perle in ferro nero, capelli ordinati all indietro.'
            },
            {
                'name': 'Armatura Cerimoniale da Guerra Antica',
                'description': 'Abbigliamento: antica armatura a piastre pesanti in ferro forgiato a fuoco vivo, segnata da colpi di lame, artigli e fenditure d ascia accumulatesi in secoli di conquiste sotterranee.\nAccessori: gonnellino di maglia di ferro pesante e spallacci titanici con zanne ricurve.\nScarpe: gambali e schinieri in piastre d acciaio temperato.\nGioielli: catena da guerra con pendenti votivi in osso di nemici sconfitti.\nTrucco: aura cupa e opprimente che incute timore reverenziale a chiunque si trovi nelle vicinanze.\nAcconciatura: capelli e barba lasciati liberi e selvaggi attorno alle corna segnate da fenditure.'
            },
            {
                'name': 'Tenuta Quotidiana negli Alloggi Privati',
                'description': 'Abbigliamento: comoda tunica ampia in lana grezza scura con maniche larghe, pantaloni morbidi in lino pesante grigio cenere.\nAccessori: borsa per tabacco da pipa e pietra focaia per accendere le radici aromatiche.\nScarpe: calzature da camera foderate in pelliccia morbida.\nGioielli: semplice bracciale in rame battuto all avambraccio destro.\nTrucco: espressione contemplativa e severa, mentre osserva il fumo salire verso le volte.\nAcconciatura: capelli e barba raccolti in modo informale per il riposo negli appartamenti privati.'
            }
        ]
    }

    for cid, outfits in darkfire_outfits.items():
        try:
            api_request('characters', cid, method='PUT', payload={'appearance_outfits': outfits, 'outfits': outfits}, token=token)
            print(f"  [OK] Assegnati {len(outfits)} outfit al personaggio [{cid}]")
        except Exception as e:
            print(f"  [ERRORE] Update outfits [{cid}]: {e}")

    print("\n--- Tutte le operazioni di remediation completate! ---")

if __name__ == '__main__':
    main()
