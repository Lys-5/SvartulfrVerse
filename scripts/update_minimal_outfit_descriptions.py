import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
PERSONA_ID = 'persona_1786335754946'
CARD_ID = '_MXcEC8Y6B3BNm3b1ttHj6'

UNIFIED_OUTFIT_DESCRIPTIONS = {
    "naked": """Completamente nuda, priva di indumenti. Corporatura minuta a clessidra, pelle chiara radiosa e liscia, priva di peli. Seno pesante e voluminoso DD-cup con piccoli capezzoli rosa. Fianchi morbidi e larghi con punto vita sottile; neo a forma di luna crescente sul fianco sinistro. Vagina liscia con labbra interne e clitoride rosa protetto. Ombelico forato con un anello d'argento a luna pendente. Capelli castano caramello sciolti in lunghe onde fino al coccige. Folta coda lupina color caramello con punta nera ed orecchie animali sulla sommità del capo.""",

    "tactic": """Tuta tattica bianca in tessuto tecnico incantato, ad alta resistenza ma leggera e flessibile. Top bianco a collo alto senza maniche, che lascia schiena, spalle e braccia scoperte; si chiude con cerniere rinforzate e fibbie metalliche sul petto abbondante DD-cup. Cintura medica modulare in vita accessoriata con fiale, pozioni e strumenti chirurgici da campo. Pantaloni cargo bianchi aderenti sui fianchi, dotati di fessura rinforzata alla base della colonna vertebrale da cui fuoriesce la folta coda caramello con punta nera. Stivali da esplorazione bianchi a metà polpaccio con suola rinforzata. Capelli castano caramello raccolti in una coda di cavallo alta; orecchie lupine erette e libere.""",

    "summer": """Top corto a portafoglio color giallo girasole con volant lungo i bordi, allacciato sul davanti con un nodo sotto il seno abbondante DD-cup, lasciando scoperto l'addome e l'anello all'ombelico con pendente a luna crescente. Shorts in denim lavato chiaro, aderenti sui fianchi, con un'apertura rinforzata sul retro per la folta coda da lupo. Scarpe da ginnastica basse in tela chiara. Capelli castano caramello sciolti in onde setose fino al coccige; cerchietti d'argento sottili applicati alla cartilagine delle orecchie da lupo. Trucco leggero con blush pesca e lucidalabbra.""",

    "winter": """Maglia color panna in lana grossa lavorata a maglia, taglio oversize con scollo asimmetrico che scivola da una spalla, indossata senza indumenti intimi sotto la trama morbida. Leggings neri in tessuto elasticizzato pesante e opaco, modellanti su fianchi e gambe, dotati di apertura posteriore rifinita per la folta coda caramello e nera. Lunghi capelli caramello raccolti morbidamente all'indietro con un fermaglio; orecchie lupine che spuntano tra le ciocche e l'ampio colletto della maglia.""",

    "beach": """Bikini due pezzi bianco ottico in tessuto elasticizzato liscio. Top a triangolo con coppe ridotte e sottili laccetti allacciati dietro il collo e attorno alla cassa toracica, che fasciano il seno voluminoso DD-cup. Slip coordinato a vita bassa con laccetti regolabili sui fianchi, posizionato sotto la base della coda da lupo caramello. Piedi nudi; anello all'ombelico con luna crescente d'argento ben visibile. Capelli sciolti e bagnati sulle spalle; orecchie da lupo caramello con punte scure erette e scoperte.""",

    "sleep": """Completo da notte composto da mutandine in morbido cotone bianco e una t-shirt nera oversize in cotone consumato, con maniche larghe e orlo lungo fino a metà coscia. L'ampio scollo rotondo della maglietta scivola lateralmente scoprendo una spalla e parte del décolleté. La biancheria inferiore è sagomata per alloggiare comodamente l'attaccatura della coda da lupo, che fuoriesce libera dall'orlo della maglia. Capelli castano caramello raccolti in uno chignon morbido e disordinato; piedi nudi.""",

    "fest": """Abito cerimoniale lungo in seta fluida color bianco lunare e dettagli in argento metallizzato. Taglio a impero con corpetto aderente, scollatura ampia e gonna fluida dotata di un profondo spacco laterale sulla gamba e di uno spacco posteriore ricamato in filo d'argento per il passaggio della folta coda. Sottile diadema a catenella d'argento posizionato sulla fronte con una pietra di luna a goccia centrale, modellato per aggirare la base delle orecchie da lupo. Capelli lunghi parzialmente intrecciati e decorati con piccoli fiori bianchi; sandali bassi argentati.""",

    "academy": """Uniforme della Divisione Medica dell'Accademia: giacca sartoriale a doppio petto in tessuto bianco con profili verde smeraldo e bottoni d'argento, tagliata su misura per accomodare le forme del busto. Minigonna a pieghe grigio scuro con fessura su misura sul retro per consentire la fuoriuscita della coda caramello e nera. Bracciale medico elastico verde smeraldo con emblema dell'Accademia sulla manica sinistra. Stivali alti in pelle nera stringati con suola piatta in gomma. Capelli ordinati sciolti con ciuffi frontali fermati dietro le orecchie lupine.""",

    "sport": """Completo sportivo bicolore giallo girasole e blu scuro. Reggiseno sportivo giallo a compressione e spalline incrociate sulla schiena. Giacca a vento tecnica ultraleggera in tessuto traspirante blu scuro con dettagli gialli, indossata aperta sul petto. Pantaloncini ciclisti aderenti a vita alta in tessuto tecnico elasticizzato, con apertura ergonomica rinforzata al coccige per la coda. Scarpe da running ammortizzate con calzini corti. Capelli castano caramello legati in una coda di cavallo alta e compatta.""",

    "spring": """Abito midi aderente in maglina a costine color blu oceano, con profondo scollo a cuore e spacco laterale che sale fino a metà coscia. La linea attillata fascia i fianchi e il busto, integrando una discreta cucitura aperta sul retro all'altezza del coccige per la folta coda da lupo. Sandali bassi in cuoio con cinturino sottile alla caviglia. Capelli castani ondulati che scendono liberi lungo la schiena; orecchie lupine caramello completamente scoperte.""",

    "hybrid": """Forma ibrida bipede di 185 cm di altezza. Mantello di pelliccia folta e vellutata color caramello, che sfuma sul petto e sul ventre in un bianco lunare luminescente a forma di cuore ben definito. Zampe inferiori con struttura digitigrade coperte di pelliccia chiara, artigli neri lucidi venati d'oro sia alle mani che ai piedi. Occhi grandi verde menta con pupilla umana; muso lupino corto e aggraziato. Grande e densa coda di lupo caramello con punta nera pronunciata. Nessun abito indossato.""",

    "fullshift": """Manifestazione quadrupede completa in forma di lupo bianco e caramello di taglia grande. Doppio mantello spesso e soffice color caramello dorato su dorso, fianchi e sommità del capo, che sfuma in bianco puro sul muso, sul petto (marcatura a cuore), sul ventre e su tutte e quattro le zampe. Sul quarto posteriore sinistro spicca una distinta marcatura naturale di pelo bianco a forma di luna crescente. Occhi grandi verde menta. Al collo indossa unicamente un cordino di cuoio intrecciato a cui è assicurato il pesante anello con sigillo d'argento della famiglia Douglas.""",

    "formal": """Tailleur formale sartoriale color avorio composto da giacca sfiancata monopetto a manica lunga e minigonna a tubino coordinata. Sotto la giacca indossa una camicetta in seta verde menta con colletto elegante e bottoni madreperla. La minigonna presenta un discreto spacco centrale sul retro studiato per la coda di lupo caramello con punta nera. Scarpe décolleté con tacco alto e plateau color avorio. Capelli pettinati in morbide onde lucide; orecchie lupine libere e adornate con piccoli cerchi d'argento.""",

    "clinic": """Tenuta professionale da clinica: camice medico bianco lungo fino a metà coscia in cotone pesante, portato aperto. Al di sotto, blusa bianca senza maniche in tessuto leggero con scollo a barca. Leggings neri elasticizzati a tre quarti che arrivano sotto il ginocchio, provvisti di occhiello elastico rinforzato sul retro da cui esce la folta coda da lupo caramello e nera. Scarpe da ginnastica basse in tela stile Converse con suola bianca. Capelli lunghi raccolti in una pratica coda di cavallo alta con elastico neutro; orecchie lupine libere ed erette.""",

    "biker": """Giacca corta da motociclista in pelle nera con cerniere diagonali e dettagli metallici cromati, lasciata aperta. Top a tubino elasticizzato giallo girasole senza spalline. Pantaloni in pelle nera aderenti con cuciture rinforzate e apertura posteriore sagomata per la coda da lupo. Pesanti stivali da moto in pelle nera con fibbie metalliche e suola carrarmato. Capelli castano caramello raccolti in una treccia spessa che scende dritta lungo la schiena; orecchie da lupo completamente esposte.""",

    "dinner": """Abito da sera lungo in raso di seta blu oltremare, caratterizzato da corpetto drappeggiato con scollatura generosa e spalline sottili. Gonna fluida con spacco sartoriale strategico sul retro che permette il passaggio naturale della folta coda caramello e nera. Scialle leggero semitrasparente abbinato posato sugli avambracci; pochette rigida argentata da sera. Sandali gioiello con tacco a spillo e sottili listini alla caviglia. Capelli acconciati in uno chignon morbido ed elegante da cui emergono le orecchie lupine erette.""",

    "angelo moreno couture": """Abito haute couture modello "Ocean Shadow" in tessuto cangiante e iridescente con sfumature liquide che virano dal blu notte profondo al verde smeraldo e ametista. Corpetto strutturato a corsetto sagomato sul busto, con spalline invisibili e gonna scivolata a taglio asimmetrico, dotata di uno spacco posteriore rinforzato per la folta coda da lupo. Fermagli geometrici in cristallo sfaccettato tra i capelli sciolti che riflettono la luce. Sandali imperiali in vernice blu notte con cinturini sottili allacciati attorno alla caviglia; orecchie lupine scoperte tra le onde dei capelli."""
}

def main():
    token = get_auth_token()
    print("Token ottenuto.\n")

    # 1. Fetch live Persona
    req_p = urllib.request.Request(f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona = json.loads(urllib.request.urlopen(req_p).read().decode('utf-8'))

    # 2. Fetch live Card
    card = get_char(token, CARD_ID)

    # 3. Update outfits in Card
    updated_card_outfits = []
    for o in card['outfits']:
        k = o['name'].lower()
        new_desc = UNIFIED_OUTFIT_DESCRIPTIONS.get(k)
        if new_desc:
            o_copy = dict(o)
            o_copy['description'] = new_desc.strip()
            updated_card_outfits.append(o_copy)
        else:
            print(f"[WARN CARD] Nessuna descrizione trovata per '{o['name']}'")
            updated_card_outfits.append(o)

    # 4. Update outfits in Persona
    updated_persona_outfits = []
    for o in persona['outfits']:
        k = o['name'].lower()
        new_desc = UNIFIED_OUTFIT_DESCRIPTIONS.get(k)
        if new_desc:
            o_copy = dict(o)
            o_copy['description'] = new_desc.strip()
            updated_persona_outfits.append(o_copy)
        else:
            print(f"[WARN PERSONA] Nessuna descrizione trovata per '{o['name']}'")
            updated_persona_outfits.append(o)

    # 5. PUT Card
    print("=== Aggiornamento Card World ===")
    put_char(token, CARD_ID, {'outfits': updated_card_outfits})
    card_ver = get_char(token, CARD_ID)
    print(f"Card verificata! {len(card_ver['outfits'])} outfits.")

    # 6. PUT Persona
    print("\n=== Aggiornamento Persona Utente ===")
    persona_payload = dict(persona)
    persona_payload['outfits'] = updated_persona_outfits
    put_url = f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}'
    req_put = urllib.request.Request(
        put_url,
        data=json.dumps(persona_payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    with urllib.request.urlopen(req_put) as resp:
        res = json.loads(resp.read().decode('utf-8'))
    
    # Verify Persona
    req_ver = urllib.request.Request(put_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona_ver = json.loads(urllib.request.urlopen(req_ver).read().decode('utf-8'))
    print(f"Persona verificata! {len(persona_ver['outfits'])} outfits.")

    print("\nEntrambe le entità sono state aggiornate con le descrizioni visive pulite!")

if __name__ == '__main__':
    main()
