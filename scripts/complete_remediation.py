import urllib.request
import urllib.error
import json
import sys
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def main():
    token = get_auth_token()
    
    # 1. Delete remaining 5 ghosts
    remaining_ghosts = [
        ('_gYagUj1CAE7grnRCVLnyU', 'Malachia Douglas Bloodmoon (Ghost)'),
        ('_xLGRAXycw4eXVMdGYqbqf', 'Magnus Douglas III (Ghost)'),
        ('_gCzaABFtVKTVCwcHmNGW6', 'Logan Douglas (Ghost)'),
        ('_Rwb3wetNrX4CfEpYDJ4HE', 'Angelo Moreno (Ghost)'),
        ('_6h1dDQpmqTAckYaWRT2er', 'Dominic Chen (Ghost)')
    ]

    print("--- CANCELLAZIONE 5 GHOST RIMASTI ---")
    for cid, label in remaining_ghosts:
        url = f"{API_BASE}/characters/{cid}?world_id={WORLD_ID}"
        req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}, method='DELETE')
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"  [DELETE OK] {label} [{cid}] status {resp.status}")
        except urllib.error.HTTPError as e:
            print(f"  [DELETE ERRORE] {label} [{cid}]: {e.code} - {e.read().decode('utf-8')}")
        time.sleep(1)

    # 2. Deploy Outfits for the 4 Darkfire demons with IDs
    print("\n--- DEPLOY OUTFIT PER I 4 DEMONI DARKFIRE ---")
    darkfire_outfits = {
        # Boros Darkfire
        '_aaWfLtx19WQR7JyHKDBem': [
            {
                'id': 'outfit-boros-1',
                'name': 'Abiti da Lavoro Logistica & Deposito',
                'description': 'Abbigliamento: maglietta a maniche corte color carbone in cotone pesante rinforzato che lascia scoperte le braccia possenti e la pelle granitica, pantaloni cargo industriali scuri con cuciture triple.\nAccessori: cintura da carico con fibbia metallica rinforzata, bracciali in cuoio spesso per sostenere i polsi.\nScarpe: scarponi da lavoro antinfortunistici rinforzati con punta in acciaio brunito e suola spessa a carrarmato.\nGioielli: robusto anello in ferro battuto con incisione della runa della terra al pollice destro.\nTrucco: nessun trucco; polvere minerale e tracce di grafite sulla pelle scura, occhi ambrati calmi e attenti.\nAcconciatura: capelli neri corti e ordinati attorno alle corna ricurve da Vax della terra.'
            },
            {
                'id': 'outfit-boros-2',
                'name': 'Tenuta Cerimoniale Sotterranea',
                'description': 'Abbigliamento: ampia tunica cerimoniale senza maniche in lino grezzo color ocra scuro e ardesia, fissata da una pesante cintura di cuoio decorata con borchie in ferro nero e piastre di basalto levigato.\nAccessori: stendardo cerimoniale del Guardiano del Clan, fascia in tessuto pesante sui fianchi.\nScarpe: calzari cerimoniali in cuoio scuro rinforzati con lamine metalliche.\nGioielli: collare rigido in ferro grezzo con sigillo di casata Darkfire incastonato sul petto.\nTrucco: pittura rituale color terracotta tracciata geometricamente sugli avambracci e sulle spalle.\nAcconciatura: chioma raccolta all indietro con un fermaglio in bronzo antico tra le corna imponenti.'
            },
            {
                'id': 'outfit-boros-3',
                'name': 'Casual da Relax & Cucina',
                'description': 'Abbigliamento: canotta scura morbida in tessuto traspirante, comodi pantaloni larghi in lino antracite con coulisse elastica, grembiule da cuoco in pelle scamosciata marrone scuro.\nAccessori: canovaccio in lino infilato nella cintura del grembiule per quando cucina per i fratelli.\nScarpe: comode calzature aperte da interno in cuoio morbido sagomato.\nGioielli: semplice catenina in ferro con un pendente a forma di martello da forgia.\nTrucco: viso rilassato e accogliente, espressione rassicurante e bonaria.\nAcconciatura: capelli sciolti leggermente mossi, corna levigate e pulite.'
            },
            {
                'id': 'outfit-boros-4',
                'name': 'Assetto da Battaglia / Baluardo di Pietra',
                'description': 'Abbigliamento: pesante corazza pettorale segmentata in ferro nero forgiato a caldo, spallacci massicci in pietra lavica incantata e bracciali d arme completi.\nAccessori: grande scudo torre a goccia in ferro battuto e cinghie di ritegno balistico.\nScarpe: stivali corazzati con schinieri in ferro nero che si ancorano stabilmente a terra.\nGioielli: anelli runici che pulsano di tenue luminescenza color ambra quando attiva l indurimento minerale.\nTrucco: crepe luminose di mana terroso che si accendono lungo le braccia e il collo pietrificato.\nAcconciatura: capelli legati stretti a ciuffo guerriero per non intralciare la visuale tra le corna corazzate.'
            }
        ],
        # Karshin Darkfire
        '_Agf7FxKMzPDFJj3gktYtz': [
            {
                'id': 'outfit-karshin-1',
                'name': 'Equipaggiamento Tattico di Sicurezza HSK',
                'description': 'Abbigliamento: uniforme tattica corporativa completamente nera in tessuto antistrappo balistico, gilet tattico sagomato in kevlar che lascia scoperte le spalle e le braccia muscolose segnate da cicatrici rituali.\nAccessori: fondine cosciali rinforzate per armi da sfondamento, guanti tattici senza dita con nocche rinforzate in fibra di carbonio.\nScarpe: anfibi da combattimento neri impermeabili con suola ammortizzata silenziosa.\nGioielli: orecchino a spuntone in acciaio brunito sull orecchio destro.\nTrucco: nessun trucco; sguardo affilato e famelico, cicatrici evidenti sul collo e sulle braccia.\nAcconciatura: capelli neri rasati sui lati e leggermente più lunghi sulla cresta centrale tra le corna affilate.'
            },
            {
                'id': 'outfit-karshin-2',
                'name': 'Gala & Scorta Esecutiva',
                'description': 'Abbigliamento: completo formale scuro su misura, camicia nera in seta elasticizzata con colletto aperto senza cravatta, giacca monopetto sartoriale con fodera in seta rosso cremisi.\nAccessori: auricolare di sicurezza cifrato invisibile, guanti sottili in pelle d agnello nera.\nScarpe: scarpe eleganti Oxford in pelle nera lucidata a specchio.\nGioielli: fermaglio in platino e ossidiana sulla tasca interna della giacca.\nTrucco: pelle curata, postura minacciosa e letale celata dietro un portamento impeccabile.\nAcconciatura: capelli neri tirati a lucido con cera opaca, corna lucide e riflettenti.'
            },
            {
                'id': 'outfit-karshin-3',
                'name': 'Abbigliamento da Interrogatorio / Sala d Addestramento',
                'description': 'Abbigliamento: canotta nera elasticizzata impregnata del profumo di cenere e ferro caldo, pantaloni militari neri infilati negli stivali da addestramento.\nAccessori: cinghie di contenimento e strumenti di coercizione agganciati alla cintura in cuoio rinforzato.\nScarpe: stivaletti da lotta neri aderenti con suola in gomma antiscivolo.\nGioielli: fascia di metallo zigrinato all avambraccio sinistro.\nTrucco: sfumatura scura e minacciosa attorno agli occhi cremisi, sorriso crudele e beffardo.\nAcconciatura: capelli spettinati e madidi di sudore dopo il combattimento corpo a corpo.'
            },
            {
                'id': 'outfit-karshin-4',
                'name': 'Tenuta Tradizionale da Caccia',
                'description': 'Abbigliamento: vesti tradizionali Vax in pelle nera conciata e scaglie metalliche, mantello corto asimmetrico e collare di zanne e spuntoni in osso scuro.\nAccessori: faretra con dardi da caccia sotterranea e lame corte a scatto.\nScarpe: calzari da predatore in cuoio silenzioso con rinforzi alle caviglie.\nGioielli: anelli dentellati da combattimento sui medi di entrambe le mani.\nTrucco: polvere di carbone sfumata sugli zigomi per mimetizzarsi nel buio totale.\nAcconciatura: ciocche scure lasciate selvagge che ricadono sul viso attorno alle corna nere.'
            }
        ],
        # Aras Darkfire
        '_8catGJE98MTpfaajJD9zV': [
            {
                'id': 'outfit-aras-1',
                'name': 'Abito Sartoriale Corporate HSK',
                'description': 'Abbigliamento: completo a tre pezzi su misura in lana finissima color antracite con gessatura impercettibile color prugna, camicia in seta avorio con colletto diplomatico e cravatta in seta bordeaux.\nAccessori: fermacravatta d argento lavorato a filigrana, pochette da taschino coordinata in seta, ventiquattrore sottile in pelle pregiata.\nScarpe: scarpe eleganti modello Derby in pelle color testa di moro spazzolata a mano.\nGioielli: gemelli da polso in argento con ametiste scure incastonate.\nTrucco: incarnato perfetto, labbra leggermente scure, sguardo suadente e ipnotico.\nAcconciatura: capelli neri ondulati lunghi fino alle spalle, curatissimi e pettinati all indietro con grazia attorno alle corna slanciate.'
            },
            {
                'id': 'outfit-aras-2',
                'name': 'Ricevimento d Alta Società',
                'description': 'Abbigliamento: smoking serale in velluto nero notte con revers a lancia in raso lucido, camicia da sera candida con abbottonatura nascosta e pantaloni da sera sartoriali a taglio vivo.\nAccessori: sciarpa di seta da sera bicolore nero e cremisi adagiata morbidamente sulle spalle.\nScarpe: pantofole eleganti da sera in velluto nero con suola in cuoio sottile.\nGioielli: spilla da giacca in platino raffigurante un serpente alato avvolto su una gemma viola.\nTrucco: leggera polvere illuminante minerale sugli zigomi, fascino aristocratico irresistibile.\nAcconciatura: chioma fluente semiraccolta con un nastro di seta scura, corna ornate da sottili anelli d argento.'
            },
            {
                'id': 'outfit-aras-3',
                'name': 'Vesti Cerimoniali Sotterranee in Seta',
                'description': 'Abbigliamento: lunga veste fluttuante cerimoniale in pura seta d ombra nera e viola scuro, intessuta con fili d argento che riflettono la luce come ragnatele notturne.\nAccessori: scettro oratorio corto con prisma di quarzo d ombra all estremità.\nScarpe: babbucce cerimoniali in morbida pelle scura prive di suola rigida.\nGioielli: anello sigillo in oro bianco con sigillo magico per la tessitura di illusioni.\nTrucco: sottile linea di ombretto violaceo sfumato che esalta la natura arcana del Vax.\nAcconciatura: capelli completamente sciolti che ondeggiano morbidi assecondando i movimenti della seta.'
            },
            {
                'id': 'outfit-aras-4',
                'name': 'Notturno / Spionaggio & Intrigo',
                'description': 'Abbigliamento: dolcevita nero aderente in cashmere finissimo, pantaloni scuri su misura a taglio dritto e un lungo cappotto sartoriale in panno di lana che ondeggia come fumo denso a ogni passo.\nAccessori: guanti sottili in pelle di cervo scura che non lasciano impronte, occhiali da sole con montatura minimalista in titanio brunito.\nScarpe: stivaletti Chelsea in pelle nera con suola in gomma ultra-silenziosa.\nGioielli: nessun monile riflettente o metallico.\nTrucco: espressione neutra e imperscrutabile che dissimula qualsiasi intenzione.\nAcconciatura: capelli legati in una coda bassa per passare inosservato sotto il bavero del cappotto.'
            }
        ],
        # Varg Darkfire
        '_bh8AHn7WKkNTnLjwXrUWE': [
            {
                'id': 'outfit-varg-1',
                'name': 'Mantello del Patriarca & Pelli Sotterranee',
                'description': 'Abbigliamento: pesante mantello da guerra in pelliccia spessa di bestia cavernicola, foderato in cuoio indurito e trattenuto sulle spalle da due enormi fibbie a testa di drago in ferro nero battuto, tunica da guerra scura e pantaloni in cuoio pesante.\nAccessori: larga cintura borchiata con piastre di ferro e corno, pipa intagliata in legno fossile.\nScarpe: alti stivali invernali in spessa pelle bovina con suola chiodata in ferro battuto.\nGioielli: antico torque in ferro grezzo ritorto attorno al collo massiccio.\nTrucco: rughe profonde e cicatrici di guerra venerabili, barba corta sale e pepe, occhi d ambra antica.\nAcconciatura: criniera brizzolata legata in trecce tradizionali che scendono ai lati delle corna nodose e imponenti.'
            },
            {
                'id': 'outfit-varg-2',
                'name': 'Tenuta Formale da Consiglio HSK',
                'description': 'Abbigliamento: lunga giubba cerimoniale scura dal taglio austero e imponente, decorata con bordature geometriche tradizionali Vax cucite in filo di rame ossidato e bottoni in corno nero.\nAccessori: bastone da passeggio in legno pietrificato con pomo sferico in ferro nero.\nScarpe: stivali in cuoio scuro lavorato con fibbie laterali in metallo antico.\nGioielli: pesante anello del patriarca al mignolo sinistro con pietra tombale incastonata.\nTrucco: portamento maestoso e inflessibile carico di otto secoli di autorità indiscutibile.\nAcconciatura: barba pettinata e fermata con due perle in ferro nero, capelli ordinati all indietro.'
            },
            {
                'id': 'outfit-varg-3',
                'name': 'Armatura Cerimoniale da Guerra Antica',
                'description': 'Abbigliamento: antica armatura a piastre pesanti in ferro forgiato a fuoco vivo, segnata da colpi di lame, artigli e fenditure d ascia accumulatesi in secoli di conquiste sotterranee.\nAccessori: gonnellino di maglia di ferro pesante e spallacci titanici con zanne ricurve.\nScarpe: gambali e schinieri in piastre d acciaio temperato.\nGioielli: catena da guerra con pendenti votivi in osso di nemici sconfitti.\nTrucco: aura cupa e opprimente che incute timore reverenziale a chiunque si trovi nelle vicinanze.\nAcconciatura: capelli e barba lasciati liberi e selvaggi attorno alle corna segnate da fenditure.'
            },
            {
                'id': 'outfit-varg-4',
                'name': 'Tenuta Quotidiana negli Alloggi Privati',
                'description': 'Abbigliamento: comoda tunica ampia in lana grezza scura con maniche larghe, pantaloni morbidi in lino pesante grigio cenere.\nAccessori: borsa per tabacco da pipa e pietra focaia per accendere le radici aromatiche.\nScarpe: calzature da camera foderate in pelliccia morbida.\nGioielli: semplice bracciale in rame battuto all avambraccio destro.\nTrucco: espressione contemplativa e severa, mentre osserva il fumo salire verso le volte.\nAcconciatura: capelli e barba raccolti in modo informale per il riposo negli appartamenti privati.'
            }
        ]
    }

    for cid, outfits in darkfire_outfits.items():
        url = f"{API_BASE}/characters/{cid}?world_id={WORLD_ID}"
        payload = {
            'appearance_outfits': outfits,
            'outfits': outfits
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
            method='PUT'
        )
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"  [OUTFITS OK] Assegnati {len(outfits)} outfit al personaggio [{cid}] (status {resp.status})")
        except urllib.error.HTTPError as e:
            print(f"  [OUTFITS ERRORE] [{cid}]: {e.code} - {e.read().decode('utf-8')}")
        time.sleep(1)

    print("\nCompletato!")

if __name__ == '__main__':
    main()
