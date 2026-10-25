import json
import uuid

def generate_id():
    return '_' + uuid.uuid4().hex[:21]

path_lb3 = 'FINAL/Svartulfr_Lorebook_III.json'
with open(path_lb3, 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])
lexicon = data.get('lexicon', [])

print(f"Initial Lorebook III counts: entries={len(entries)}, lexicon={len(lexicon)}")

# 1. Update Demografia
demo_content = """[DEMOGRAFIA ACCADEMICA SUCC: Popolazione Studentesca e Docente]
Weres e Mutaforma (Shapeshifter): 25.8% (specie di maggioranza nell'area di Solarton, cicli di mutazione volontari o lunari)
Demi-umani (Demihumans): 24.0% (ibridi con tratti animali/mitici, dotati tassativamente di un solo paio di orecchie animali)
Umani ordinari (Mundane Humans): 13.3% (iscritti dopo la riforma del Rettore Archer Wolfwood nel 2002)
Vampiri: 7.5% (piccola comunita d'elite post-1999, concentrata prevalentemente nella vicina Hex Valley)
Demoni: 5.0% (succubi, incubi, imp, ifrit, fiend; soggetti a registro statale obbligatorio)
Fae: 4.9% (pixie, driadi, elfi, ninfe, sidhe; elevato talento magico naturale)
Ibridi (Cross-Species Hybrids): 4.7% (centauri, sirene, tritoni, fauni, naga; necessitano di varchi e alloggi speciali)
Non-morti (Undead): 4.0% (zombie, lich, spettri, wight; tutelati dal Supernatural Harm Act del 2001)
Umani magicamente dotati: 4.0% (streghe, maghi e individui con affinita arcane innate)
Altro / Criptidi rari: < 1.0% (forme mutanti RMH come Oskar Lindholm, troll ed entita esotiche)"""

# 2. Update Corsi di Laurea
degrees_content = """[CORSI DI LAUREA E SPECIALIZZAZIONI SOVRANNATURALI SUCC]
La Supernatural University of Central California offre circa 75 corsi di laurea tradizionali (BA, BS, BCOM, BFA, ME, MArch, PhD) integrati con 11 specializzazioni accademiche esoteriche d'eccellenza:
1. Alchemy: Studio della trasmutazione della materia, catalizzatori elementali e composti chimico-arcani.
2. Necromancy: Teoria e prassi dell'interazione con l'oltretomba, rianimazione controllata ed etica della morte.
3. Applied Divination: Metodologie di preveggenza, cartomanzia accademica, astrologia divinatoria e chiaroveggenza.
4. Paranormal Psychology: Analisi delle strutture mentali, fobie di specie e traumi somatici dei non-umani in societa mista.
5. Astral Studies: Scienze celesti, cicli stellari e manipolazione avanzata delle maree magiche lunari.
6. Potions: Laboratorio pratico di estrazione alchemica, pozioni mediche e biofarmacologia clinica.
7. Cryptozoology: Anatomia comparata, classificazione tassonomica e salvaguardia di specie rare e mitiche sul campo.
8. Supernatural/Human Relations: Giurisprudenza, mediazione interspecie e diplomazia tra comunita umane e non-umane.
9. Environmental Magic: Incantesimi per la bonifica ecologica, guarigione delle biosfere e simbiosi con gli elementi.
10. Vampiric Studies: Biologia molecolare del sangue, psicologia ematofaga, storia sociale e sociologia vampirica.
11. Lycanthropy Studies: Struttura del genoma mannaro, dinamiche di branco, feromoni, ruts e calori, frenesia lunare."""

# 3. Update Campus Locations
campus_content = """[CAMPUS SUCC: Strutture e Servizi Specializzati]
- Archer Wolfwood Hall: Edificio principale e sede del rettorato, completamente schermato da barriere anti-magia; ospita le aule magne e i teatri di conferenza.
- St. Neptune Stadium: Complesso polisportivo climatizzato dotato di stadio da football, pista olimpionica per l'ice hockey, piscina riscaldata e saune rigenerative per shifters.
- Basilisk Library: Biblioteca su cinque piani che custodisce una delle collezioni di tomi magici e bestiari piu vaste del continente. Durante la stagione invernale mette a disposizione stanze a temperatura controllata per studenti e docenti a sangue freddo (demi-umani rettili, naga, gorgoni).
- Griffin Clocktower: Storica torre dell'orologio sormontata da doccioni a forma di grifone che prendono vita a ogni scoccare dell'ora. Attualmente chiusa per lavori di manutenzione straordinaria, con lezioni ricollocate presso l'Edificio C.
- Nocturnal Hall: Polo didattico insonorizzato e schermato dalla luce per le lezioni e i seminari serali e notturni.
- Unicorn Hall: Padiglione a pianta ribassata e porte allargate, completamente privo di barriere architettoniche per accomodare ibridi taurini, centauri e studenti con ali o code voluminose.
- Lunar Quad: Piazza centrale del campus con fontana monumentale in pietra lunare che riflette permanentemente le fasi della luna in tempo reale.
- Fraternity and Sorority Row: Viale alberato a ovest della biblioteca dove sorgono le sedi storiche delle confraternite universitarie.
- Wyrm Dormitories: Moderno complesso residenziale studentesco misto a suite con alloggi schermati per specie ad abitudini circadiane opposte."""

# 4. Update SUCC Bulls
bulls_content = """[SQUADRA FOOTBALL SUCC: The Bulls]
Mascotte: Il Toro (The Bulls). Colori sociali: Blu scuro e oro.
Campo: St. Neptune Stadium. Motto: #GoBulls.
Head Coach: Dullahan (veterano ed ex contractor).
Assistant Coach: Barkley Rover (demi-umano golden retriever).
Star Quarterback: Jared Thompson (half-minotaur).
Roster Principale: Santiago Herrera (offensive lineman, dragon demi-human), Bailey Rogers (offensive lineman, incubus), Tomas Matthews (human).
Rivalita Istituzionale: La partita piu sentita della stagione e il derby accademico contro i Clams della C.U.M.S (California University of Magical Sciences), disputata tradizionalmente ogni venerdi alle ore 19:00 davanti a spalti gremiti."""

# 5. Update SUCC Bears
bears_content = """[SQUADRA ICE HOCKEY SUCC: The Bears]
Mascotte: Grizzly Bear (The Bears). Colori sociali: Blu scuro e oro.
Pista: St. Neptune Ice Arena.
Caratteristiche di Gioco: La squadra unisce la resistenza fisica e la visione notturna dei vampiri con i riflessi fulminei dei mannari e dei demi-umani.
Capitano della Squadra: Vincent Campbell (vampiro, attaccante).
Mascotte di Pista: Andrew Campbell (vampiro).
Ala Sinistra: Finnegan 'Finn' Novak (demi-umano lupo artico).
La formazione e attualmente imbattuta nel campionato universitario intercollegiale della West Coast."""

# 6. Update Programmi Sportivi
sports_content = """[PROGRAMMI SPORTIVI E ATLETICA UNIVERSITARIA SUCC]
La SUCC garantisce pari opportunita a studenti umani e sovrannaturali nei provini sportivi. Sebbene zanne, ali e poteri somatici offrano un vantaggio naturale, rigidi protocolli di compensazione equilibrano le gare.
Discipline Attive:
- Football Americano: SUCC Bulls (squadra campione di stato, guidata da Coach Dullahan).
- Ice Hockey: SUCC Bears (squadra d'elite guidata dal capitano Vincent Campbell).
- Swim and Dive: The Kelpies (squadra acquatica composta in larga parte da selkie, tritoni e demi-umani marini).
- Basketball: The Phantoms (squadra perseguitata da incidenti e sfortuna cosmica, allenata dallo spettro di Coach Connors).
- Cheerleading: Squadra unisex agonistica di livello nazionale, guidata da Janice Thompson (holstaur).
- Altri Sport Competitivi: Baseball, Ginnastica, Lacrosse, Canottaggio (Rowing), Calcio (Soccer), Tennis, Atletica (Track and Field), Pallavolo, Wrestling."""

# Update in entries and lexicon
for e in entries:
    name = e.get('name', '')
    if 'Demografia' in name:
        e['content'] = demo_content
    elif 'Corsi di Laurea' in name:
        e['content'] = degrees_content
    elif 'Campus SUCC' in name:
        e['content'] = campus_content
    elif 'SUCC Bulls' in name:
        e['content'] = bulls_content
    elif 'SUCC Bears' in name:
        e['content'] = bears_content
    elif 'Programmi Sportivi' in name:
        e['content'] = sports_content

for l in lexicon:
    name = l.get('name', '')
    if 'Demografia' in name:
        l['content'] = demo_content
    elif 'Corsi di Laurea' in name:
        l['content'] = degrees_content
    elif 'Campus SUCC' in name:
        l['content'] = campus_content
    elif 'SUCC Bulls' in name:
        l['content'] = bulls_content
    elif 'SUCC Bears' in name:
        l['content'] = bears_content
    elif 'Programmi Sportivi' in name:
        l['content'] = sports_content

# 7. Add Nuova Voce: Quadro Giuridico Modern Fantasy
legal_id = generate_id()
legal_entry = {
    'id': legal_id,
    'name': 'Quadro Giuridico Modern Fantasy (Nozze Miste, Registro Demoni, Harm Act)',
    'type': 'lore/concept',
    'keys': ['Quadro Giuridico', 'Nozze Miste', 'Registro Demoni', 'Supernatural Harm Act', 'Leggi Modern Fantasy', 'Matrimonio Misto', 'Diritti Sovrannaturali'],
    'secondary_keys': ['legge', 'tribunale', 'divieto', 'certificato', 'stato', 'governo', 'diritti', 'reato'],
    'key_logic': 'AND_ANY',
    'content': """[ORDINAMENTO GIURIDICO E NORMATIVE CIVILI: Modern Fantasy]
Il tessuto socio-politico dell'ambientazione Modern Fantasy (2022-2025) e regolato da severe restrizioni federali e statali volte a gestire la convivenza tra umani e sovrannaturali:
1. Divieto di Matrimonio Misto: Nella quasi totalita degli stati e delle giurisdizioni nazionali e severamente proibito il matrimonio legale tra esseri umani e creature sovrannaturali o ibridi. Le unioni interspecie non godono di riconoscimento giuridico, successorio o patrimoniale.
2. Registro Obbligatorio dei Demoni: Per disposizioni di sicurezza federale, tutte le entita di lignaggio infernale (succubi, incubi, ifrit, fiend) sono tenute a registrarsi periodicamente presso le autorita competenti. Rigidi controlli regolano le specie ematofaghe o energetiche che necessitano di nutrirsi di esseri umani.
3. Supernatural Harm Act del 2001: Legge quadro emanata per risarcire e tutelare le vittime di resurrezione forzata, necromanzia abusiva o trasformazione occulta involontaria (come nel caso del batterista Roland Vickers). Lo statuto riconosce lo status civile di Non-Morto, garantendo borse di studio e pensioni compensative.
4. Assenza di Robotica Avanzata: Il livello tecnologico e strettamente ancorato al 2023-2024 con integrazioni magiche; la legge e la tecnologia non consentono androidi, cyborg o intelligenze artificiali dotate di corpo fisico senziente.""",
    'selective': True,
    'priority': 2,
    'position': 'before_char',
    'enabled': True
}

entries.append(legal_entry)
lexicon.append(legal_entry)

with open(path_lb3, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated Lorebook III: entries={len(entries)}, lexicon={len(lexicon)}")
