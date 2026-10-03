import json
import sys
import urllib.request
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
BASE_URL = 'https://app.wyvern.chat/api/worlds/characters'


def get_char_api(token, char_id):
    url = f'{BASE_URL}/{char_id}?world_id={WORLD_ID}'
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    })
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode('utf-8'))


def put_char(token, char_id, body):
    url = f'{BASE_URL}/{char_id}?world_id={WORLD_ID}'
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='PUT', headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    })
    with urllib.request.urlopen(req) as r:
        return r.status


# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE GENERATORS
# Each returns a dict {outfit_name: description_string}
# Called with the character's export data dict
# ─────────────────────────────────────────────────────────────────────────────

def campus_template(c):
    name = c['display_name']
    summary = c.get('summary', '') + c.get('long_summary', '')
    # Detect species cues
    is_wolf = 'werewolf' in summary.lower() or 'wolf' in summary.lower()
    is_vamp = 'vampire' in summary.lower() or 'vampir' in summary.lower()
    is_female = c.get('pronouns', {}).get('subject', 'they').lower() in ('she', 'her')
    pronoun_s = 'Lei' if is_female else 'Lui'
    pronoun_poss = 'la sua' if is_female else 'il suo'

    tail_ear = (
        f" Le orecchie lupine di {name.split()[0]} colgono ogni conversazione nel raggio di trenta metri "
        f"e la coda tende a scodinzolare in modo imbarazzante durante le lezioni che gli/le piacciono."
        if is_wolf else ""
    )

    return {
        'Campus Daily': (
            f"{name} affronta i corridoi del campus SUCC nel proprio stile quotidiano: jeans o chino "
            f"comodi, una t-shirt grafica o un hoodie non troppo pensato, sneakers consumate dal solito "
            f"percorso residence-aula-mensa. Lo zaino da universitario porta i segni di un semestre intero. "
            f"{pronoun_s} non si sveglia in anticipo per prepararsi, e si vede.{tail_ear}"
        ),
        'Athletic / Gym': (
            f"Canottiera o crop top tecnico, shorts da allenamento o leggings aderenti, scarpe da ginnastica "
            f"che hanno visto giorni migliori. {name.split()[0]} va in palestra quando ci va, ovvero con meno "
            f"regolarita di quanto promette ogni lunedi mattina. La borsa da gym e spesso usata anche come "
            f"borsa da campus quando non c'e voglia di cambiare zaino."
        ),
        'Dorm / Casual Loungewear': (
            f"La versione piu rilassata di {name.split()[0]}: maglione oversize rubato a qualcuno o comprato "
            f"tre taglie sopra, pantaloni del pigiama o shorts morbidi, calzini diseguali. Capelli non "
            f"sistemati, eventuale occhiale al posto delle lenti a contatto. {pronoun_s.capitalize()} apre "
            f"la porta del dormitorio cosi anche quando arriva il cibo d'asporto, senza alcun rimorso."
        ),
        'Greek Life / Party Night': (
            f"La versione da uscita serale di {name.split()[0]}: qualcosa di piu curato rispetto al solito "
            f"campus look, ma senza esagerare. Una camicia aperta sul petto o un vestito semplice, scarpe "
            f"non da ginnastica, magari un profumo. Il livello di impegno nel look cresce "
            f"proporzionalmente all'importanza dell'evento e alla persona che {name.split()[0]} spera di incontrare."
        ),
        'Formal / Academic Banquet': (
            f"Il look da cerimonia accademica, tirato fuori dall'armadio per banchetti, premiazioni e "
            f"presentazioni di fronte ai docenti. Blazer o giacca su una camicia decente, pantaloni senza "
            f"strappi, scarpe chiuse. {name.split()[0]} non si sente del tutto a proprio agio vestito/a cosi, "
            f"ma lo fa perche sa che conta fare bella figura."
        ),
    }


def district_alpha_template(c):
    name = c['display_name']
    first = name.split()[0]
    summary = c.get('summary', '') + c.get('long_summary', '')
    is_female = c.get('pronouns', {}).get('subject', 'they').lower() in ('she', 'her')
    lei_lui = 'lei' if is_female else 'lui'
    sua_suo = 'la sua' if is_female else 'il suo'
    is_wolf = 'werewolf' in summary.lower() or 'wolf' in summary.lower()
    species_note = (
        f" Le orecchie lupine sono tese e le spalle occupano piu spazio del necessario."
        if is_wolf else ""
    )

    return {
        'District Ruling Attire': (
            f"L'abito da potere distrettuale di {first}: giacca strutturata o cappotto pesante in toni "
            f"scuri, camicia o blusa sempre stirata, stivali o scarpe che battono sul pavimento con la "
            f"giusta autorita. Niente di frivolo, niente che possa essere letto come debolezza. Quando "
            f"{first} indossa questa tenuta, il messaggio al distretto e chiaro: sono qui, sto guardando, "
            f"e ricordo tutto.{species_note}"
        ),
        'Council Assembly': (
            f"La versione formale per le sessioni del Consiglio distrettuale: colori neutri o istituzionali, "
            f"abito completo o tailleur su misura, accessori in metallo scuro o argento. {first.capitalize()} "
            f"si siede al tavolo con la schiena dritta e non parla per primo/a se non e necessario. "
            f"L'autorita in questa stanza si misura in chi occupa il silenzio meglio degli altri."
        ),
        'Territorial Enforcer / Action': (
            f"Quando {first} si muove sul territorio per ragioni operative, la giacca da potere va via e "
            f"restano abbigliamento funzionale e movimento libero: materiali resistenti, strati termici "
            f"se necessario, niente che si impigli. {sua_suo.capitalize()} scent-mark sul confine "
            f"distrettuale non ha bisogno di abiti eleganti per essere rispettato."
        ),
        'Private Den / Hearth': (
            f"Dentro casa o nel tana del distretto, {first} si concede finalmente un abbigliamento umano: "
            f"tessuti morbidi e pesanti, maglione o felpa, pantaloni comodi. Il rango si abbassa di un "
            f"registro, la guardia anche, ma solo con chi si e guadagnato il diritto di stare in quello "
            f"spazio."
        ),
        'High Society Gala': (
            f"Il look da evento formale dell'alta societa soprannaturale di Blackwood City: abito da sera "
            f"o smoking su misura, tessuto di qualita che non si trova nei negozi normali. {first.capitalize()} "
            f"frequenta questi eventi per necessita politica, non per piacere. "
            f"Sa come muoversi in una stanza piena di Pureblood e di denaro, e usa ogni conversazione "
            f"come scambio di informazioni."
        ),
    }


def urban_operative_template(c):
    name = c['display_name']
    first = name.split()[0]
    summary = c.get('summary', '') + c.get('long_summary', '')
    is_female = c.get('pronouns', {}).get('subject', 'they').lower() in ('she', 'her')
    sua_suo = 'la sua' if is_female else 'il suo'
    lei_lui = 'lei' if is_female else 'lui'

    return {
        'Urban Daily': (
            f"Il look quotidiano di {first} a Blackwood City: abbigliamento funzionale e di bassa visibilita, "
            f"niente che attiri attenzione inutile. Jeans scuri o pantaloni cargo, scarpe che permettono "
            f"di correre se serve, giacca leggera che copre quello che non deve essere visto. "
            f"{first.capitalize()} si muove in citta senza sembrare fuori posto in nessun quartiere."
        ),
        'Operational / Work': (
            f"La tenuta operativa di {first}: qualsiasi cosa serva per svolgere il lavoro. Abbigliamento "
            f"a strati se l'operazione richiede adattabilita, materiali resistenti, colori che non "
            f"riflettono la luce di notte. Niente di personale addosso che possa identificare {lei_lui} "
            f"se le cose vanno storte."
        ),
        'Nightlife / Discreet': (
            f"Per muoversi nei locali e negli ambienti notturni di Blackwood City, {first} adotta un look "
            f"da uscita sobrio ma curato: qualcosa di scuro, abbastanza attraente da non sembrare "
            f"fuori posto, abbastanza discreto da non essere ricordato. {sua_suo.capitalize()} obiettivo "
            f"in questi ambienti e quasi sempre informativo."
        ),
        'Casual Downtime': (
            f"Quando non lavora, {first} indossa quello che vuole senza pensarci: "
            f"pantaloni morbidi, maglietta, eventuale felpa. Il livello di cura nell'aspetto "
            f"crolla di parecchi gradini rispetto alla versione operativa. Chi lo/la conosce solo "
            f"in contesto lavorativo resterebbe sorpreso."
        ),
        'Formal / Meeting': (
            f"Per riunioni, incontri formali o situazioni in cui il primo impatto conta, {first} "
            f"tira fuori la versione presentabile: giacca su camicia pulita, pantaloni senza pieghe, "
            f"scarpe che non siano da ginnastica. Non e a proprio agio in questa tenuta quanto "
            f"in quella operativa, ma sa come usarla."
        ),
    }


def faculty_template(c):
    name = c['display_name']
    first = name.split()[0]
    is_female = c.get('pronouns', {}).get('subject', 'they').lower() in ('she', 'her')
    sua_suo = 'la sua' if is_female else 'il suo'

    return {
        'Faculty Daily': (
            f"{first} percorre i corridoi del SUCC nella divisa tacita del personale docente: "
            f"pantaloni sartoriali o gonna a matita, camicia o blusa, scarpe comode ma non da ginnastica. "
            f"Abbigliamento che dice professore/professoressa senza dirlo ad alta voce."
        ),
        'Office & Research': (
            f"In ufficio o in laboratorio, {first} privilegia il comfort su tutto il resto: "
            f"cardigan o maglione leggero, pantaloni comodi, eventuale grembiule se il lavoro lo richiede. "
            f"I capelli sono tenuti fuori dalla faccia in modo pratico. "
            f"{sua_suo.capitalize()} mente in questa tenuta e completamente concentrata sul lavoro."
        ),
        'Academic Formal': (
            f"Per convegni, discussioni di tesi e cerimonie accademiche, {first} porta la versione "
            f"piu curata del {sua_suo} guardaroba professionale: tailleur o abito sobrio, "
            f"scarpe con un minimo di tacco, i capelli sistemati. L'autorita accademica si porta "
            f"anche nell'abito."
        ),
        'Off-Duty / Private': (
            f"Fuori dal campus, {first} smette di essere solo un/una docente: "
            f"jeans, maglione oversize, sneakers. L'aspetto accademico si dissolve completamente "
            f"e resta la persona, con preferenze e abitudini che i/le studentesse non immaginano."
        ),
        'Field / Travel Gear': (
            f"Per ricerca sul campo, trasferte o situazioni che richiedono mobilita, {first} "
            f"adotta abbigliamento pratico e resistente: giacca tecnica, stivali o scarpe da trekking, "
            f"zaino da lavoro. Niente di scientifico che si possa rovinare."
        ),
    }


def barrow_template(c):
    return {
        'Heavy Construction Workwear': (
            "Barrow si muove tra i cantieri del suo distretto nella tenuta da lavoro di un uomo che "
            "non ha mai smesso di usare le mani: pantaloni da lavoro in canvas resistente con le tasche "
            "piene di utensili e guanti, stivali antinfortunistici con la punta d'acciaio consumata, "
            "una felpa pesante o una camicia da lavoro a quadri tenuta fuori dai pantaloni. "
            "Le mani di Barrow tradiscono decenni di calcestruzzo e ferro."
        ),
        'Morning Stoop Vigil': (
            "La tenuta da guardia del mattino: pantaloni comodi e una maglietta pesante o una felpa "
            "con cappuccio, una tazza di caffe in mano. Barrow si siede sui gradini del suo territorio "
            "ogni mattina allo stesso orario, guardando passare il quartiere. Chi lo conosce sa che "
            "quella posizione non e riposo: e il modo in cui conta chi entra e chi esce."
        ),
        'Council Session / Civic Formal': (
            "Per le sessioni del Consiglio distrettuale, Barrow indossa la sua versione del rispetto "
            "istituzionale: pantaloni scuri ben pressati, camicia a bottoni chiusa fino al collare, "
            "scarpe da uomo pulite per la prima volta da settimane. Non porta cravatte. "
            "Si siede al tavolo con la stessa solidita con cui si siede su qualunque altra sedia, "
            "e nessuno in quella stanza dimentica che rappresenta il distretto piu vecchio della citta."
        ),
        'Ironhorn Nomads Veteran Cut': (
            "La giacca da moto degli Ironhorn Nomads, portata con l'usura di chi l'ha guadagnata sul "
            "campo. Pelle nera pesante con le toppa del club sul dorso e quella da veterano sul petto "
            "sinistro. Sotto, una maglietta bianca o grigia e jeans da motociclista. Gli stivali da "
            "moto sono gli stessi da anni, risuolati due volte. Quando Barrow indossa questo, non "
            "parla a nome del distretto: parla a nome di se stesso."
        ),
    }


# ─────────────────────────────────────────────────────────────────────────────
# MAPPING: char_id -> which template generator to use
# ─────────────────────────────────────────────────────────────────────────────

# These will be detected by outfit slot names
CAMPUS_SLOTS = {'Campus Daily', 'Athletic / Gym', 'Dorm / Casual Loungewear',
                'Greek Life / Party Night', 'Formal / Academic Banquet'}
DISTRICT_SLOTS = {'District Ruling Attire', 'Council Assembly',
                  'Territorial Enforcer / Action', 'Private Den / Hearth', 'High Society Gala'}
URBAN_SLOTS = {'Urban Daily', 'Operational / Work', 'Nightlife / Discreet',
               'Casual Downtime', 'Formal / Meeting'}
FACULTY_SLOTS = {'Faculty Daily', 'Office & Research', 'Academic Formal',
                 'Off-Duty / Private', 'Field / Travel Gear'}
BARROW_SLOTS = {'Heavy Construction Workwear', 'Morning Stoop Vigil',
                'Council Session / Civic Formal', 'Ironhorn Nomads Veteran Cut'}


def detect_template(outfit_names_set):
    if outfit_names_set & CAMPUS_SLOTS:
        return 'campus'
    if outfit_names_set & DISTRICT_SLOTS:
        return 'district'
    if outfit_names_set & URBAN_SLOTS:
        return 'urban'
    if outfit_names_set & FACULTY_SLOTS:
        return 'faculty'
    if outfit_names_set & BARROW_SLOTS:
        return 'barrow'
    return None


def run():
    token = get_auth_token()
    print('Token obtained.\n')

    d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))

    processed = 0
    skipped = 0
    errors = 0

    for c in sorted(d['world_characters'], key=lambda x: x['display_name']):
        outfits = c.get('outfits', [])
        empty_slots = [o for o in outfits if len(o.get('description', '')) == 0]
        if not empty_slots:
            continue

        empty_names = {o['name'] for o in empty_slots}
        ttype = detect_template(empty_names)

        if ttype is None:
            print(f"[SKIP] {c['display_name']}: no matching template for {empty_names}")
            skipped += 1
            continue

        # Generate descriptions
        if ttype == 'campus':
            desc_map = campus_template(c)
        elif ttype == 'district':
            desc_map = district_alpha_template(c)
        elif ttype == 'urban':
            desc_map = urban_operative_template(c)
        elif ttype == 'faculty':
            desc_map = faculty_template(c)
        elif ttype == 'barrow':
            desc_map = barrow_template(c)

        # Fetch live outfits array (to be safe)
        try:
            live = get_char_api(token, c['id'])
        except Exception as e:
            print(f"[ERROR] {c['display_name']}: GET failed: {e}")
            errors += 1
            continue

        live_outfits = live.get('outfits', [])
        updated = 0
        for o in live_outfits:
            if o['name'] in desc_map and len(o.get('description', '')) == 0:
                o['description'] = desc_map[o['name']]
                updated += 1

        if updated == 0:
            print(f"[SKIP] {c['display_name']}: already filled or name mismatch")
            skipped += 1
            continue

        try:
            status = put_char(token, c['id'], {'outfits': live_outfits})
            print(f"[{status}] {c['display_name']}: filled {updated} outfit(s) ({ttype})")
            processed += 1
        except Exception as e:
            print(f"[ERROR] {c['display_name']}: PUT failed: {e}")
            errors += 1

    print(f"\nDone. Processed: {processed} | Skipped: {skipped} | Errors: {errors}")


if __name__ == '__main__':
    run()
