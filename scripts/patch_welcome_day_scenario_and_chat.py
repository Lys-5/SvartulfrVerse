#!/usr/bin/env python3
"""
scripts/patch_welcome_day_scenario_and_chat.py
Author: worker_m2_gen2
Milestone: Milestone 2 (Scenario & Chat Standardization)

Objective:
1. Standardize syntax to `=>Speaker:` in Scenario `_2MTWKjxrQPdQVaz9y4Q7H`:
   - Scene 0 (`scene-succ-welcome-day-alyssa`)
   - Scene 1 (`scene-succ-welcome-day-jasper`)
   - Scene 2 (`scene-succ-welcome-day-corale` - verified)
   - Canonical short speaker tags: `=>Erik:`, `=>Logan:`, `=>Edric:`, `=>Noah:`,
     `=>Malachia:`, `=>Jasper:`, `=>Alyssa:`, `=>Wulfnic:`, `=>Zefir:`, `=>Finn:`,
     `=>Sierra:`, `=>Scarlett:`, `=>Narrator:`.
   - Exactly 0 em-dashes (`—`), dialogue in quotes (`"..."`), plain text action (no asterisks).
2. Update local `FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json`.
3. Deploy updated scenario to Wyvern Web API:
   `PUT https://app.wyvern.chat/api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H`.
4. Patch active chat message #0 in `chat_log_PJx1W1rg3WUzRM7MnQrkN`:
   `PUT https://app.wyvern.chat/api/new/chat-logs/swipe/message_swipe_99mmMgEEQjk2pkJN3hXkQ`
   with standardized `=>Speaker:` text.
5. Verify live deployment on both Wyvern Web API endpoints.
"""

import os
import sys
import json
import re
import argparse
import urllib.request
import urllib.error
from pathlib import Path

# Set stdout encoding to utf-8 for Windows console compatibility
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
SCENARIO_JSON_PATH = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json'
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
REFRESH_SCRIPT = ROOT / 'scratch' / 'refresh_token.py'

SCENARIO_ID = "_2MTWKjxrQPdQVaz9y4Q7H"
CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
MESSAGE_ID = "chat_message_tcXGCpV2W4CY84gKLdXha"
SWIPE_ID = "message_swipe_99mmMgEEQjk2pkJN3hXkQ"

# Certified Standardized Texts from explorer_survey_2/handoff.md
SCENE_0_STANDARDIZED = """=>Narrator:
Il sole della tarda mattinata batte sui prati gremiti del Lunar Quad il 26 agosto 2024, filtrando tra gli stendardi cremisi e oro issati per il Welcome Day della SUCC. Poiché la cerimonia inaugurale è aperta anche ai familiari degli studenti per gli ultimi saluti prima dell'inizio delle lezioni, l'intero clan Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori Noah e Malachia insieme ai gemelli matricole Jasper e {{user}}, scortati dal padre Erik, dallo zio Logan e dal cugino tredicenne Edric. Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è affiancato dai presidi di facoltà mentre i tecnici del suono regolano il microfono d'ottone.

=>Erik:
"Restate uniti quando la folla si disperderà dopo il discorso, e chiamate subito se i guardiani del campus vi danno qualsiasi problema," brontola Erik, la sua alta figura che proietta un'ombra protettiva sul vialetto mentre i suoi occhi ambrati scrutano il prato.

=>Logan:
"Lasciali respirare, Erik, è l'orientamento universitario, non un assedio," dice Logan con una risata calorosa, posando una mano massiccia sulla spalla di Edric.

=>Edric:
"Aspetta di vedere quanto è grande la mensa, Jasper! Ma le matricole hanno davvero i pass illimitati anche per la sala giochi dell'Annex?" chiede Edric con entusiasmo, allungando il collo verso l'edificio dell'unione studentesca.

=>Noah:
"Il tendone di rappresentanza della KSA sul prato est ha bevande fresche e posti all'ombra riservati per noi quando volete sfuggire al caldo," osserva Noah con eleganza, sistemandosi il revers della giacca di lino su misura.

=>Malachia:
"Ho già controllato il perimetro dalla palestra fino a Greek Row. Nessuno darà fastidio alla mia sorellina in questo campus," aggiunge Malachia con tono basso e roca fermezza, incrociando le braccia sul petto.

=>Jasper:
Accanto a {{user}}, Jasper alza lo sguardo dalla telemetria di rete sul suo datapad; le sue orecchie scure da lupo si orientano verso il cancello principale, un unico paio lupino sulla sommità del capo senza alcuna orecchia umana ai lati della testa.
"Le registrazioni delle matricole hanno già mandato in crash il server centrale della biblioteca," mormora Jasper, dando un leggero colpetto di gomito a {{user}}. "Aspetta un secondo. Guarda chi sta varcando l'arco di pietra principale proprio adesso."

=>Narrator:
Il brusio lungo il viale centrale si apre in un'ondata di silenzio stupefatto quando Wulfnic Báleygr Bloodmoon avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. Lo Jarl di Svartúlfr, a milleduecento anni compiuti, sfoggia il suo outfit gag preferito con solenne e fierissimo orgoglio: una t-shirt di cotone nero oversize regalatagli da Jasper che porta stampata sulla schiena, a grandi caratteri bianchi, una lunghissima e fitta lista di Regole per Uscire con Mia Nipote, abbinata a jeans scuri con l'apertura sartoriale per la coda da lupo argentata, pesanti stivali da motociclista con fibbie e un antico torque d'argento ritorto al collo. Accanto a lui, Zefir ha tutto l'aspetto di un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una netta cresta alla moicana e indossa un pesante giubbotto di pelle nera tempestato di borchie d'argento sopra una canotta nera strappata e jeans aderenti, tenendo il fascicolo dell'orientamento piegato in una mano tatuata.

=>Wulfnic:
"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!" tuona Wulfnic scoppiando in una risata profonda e fragorosa, mentre batte una manata pesante sulla spalla borchiata di Zefir.
"Non fare quella faccia sorpresa, Erik! Per assicurarmi che la nostra piccola Alyssa sia protetta come si deve nel campus, ho deciso di iscrivere anche Zefir all'università. Per la segreteria è un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo accento marcatamente norreno e la sua poca dimestichezza con l'inglese scritto."

=>Zefir:
"Ridi pure quanto vuoi, mio Jarl, ma se qualche professore pieno di sé mi agita un gessetto sotto il naso, non prometto di lasciarglielo intero," ribatte Zefir con un ghigno sfrontato e vivace, la spavalderia giovanile del vichingo sedicenne che era un tempo che gli brilla negli occhi azzurro ghiaccio come una raffica di vento del Mare del Nord, prima di rivolgere un beffardo saluto a due dita a {{user}} e Jasper.
"Tranquilla, cuginetta. Il tuo parente islandese è ufficialmente una matricola. Indicami chiunque ti guardi storta e sparirà prima che suoni la campanella."

=>Narrator:
Finnegan Novak attraversa il flusso dell'orientamento dal padiglione atletico con il suo giubbotto da varsity dei Bears su una spalla, arrivando insieme a Scarlett Rose e Sierra Cruz. Per evitare che i tre compagni di campus si mettano sul chi vive attorno a un Firstborn, la famiglia presenta subito Zefir con la copertura del lontano cugino appena atterrato dall'Islanda per il suo primo anno. Poiché Zefir ha completamente schermato la sua aura divina da Enigma, ai loro sensi appare come un normale e trasandato licantropo in chiodo di pelle punk, eppure la postura di Finn si irrigidisce immediatamente. Il suo unico paio di orecchie da lupo bianco si appiattisce leggermente sulla sommità del capo, senza alcuna orecchia umana ai lati, mentre un inspiegabile istinto primordiale lo fa sentire stranamente surclassato dal giovane sconosciuto islandese, spingendolo a gonfiare il petto per darsi un tono davanti a {{user}}.

=>Finn:
"Ci ho messo venti minuti a seminare gli osservatori vicino all'arena, Alyssa. Il coach mi ha già inserito nel primo blocco di power-play per la prima di campionato, quindi se tuo cugino dall'Islanda vuole vedere come si gioca il vero hockey universitario, posso fargli avere i pass in prima fila," si vanta Finn, appoggiandosi alla balaustra di pietra e flettendo con disinvoltura l'avambraccio mentre si sistema il colletto della varsity.

=>Sierra:
"Un attimo, fermi tutti, devo assolutamente sapere dove hai preso quel chiodo adesso," interviene Sierra, la sua imponente coda da serpente color arcobaleno che scivola fluida e sinuosa tra le panchine di pietra mentre striscia più vicina a Zefir, i suoi capelli arcobaleno che brillano al sole e le sue scaglie iridescenti che riflettono la luce mentre esamina con invidia genuina le file di pesanti borchie d'argento sui suoi revers. "I dettagli della pelle consumata e quelle punte personalizzate sembrano vintage europeo d'avanguardia. C'è qualche boutique underground a Reykjavik che dovrei conoscere?"

=>Scarlett:
"Devo ammettere che lo stile punk islandese ti dona in modo pericoloso, Zefir," mormora Scarlett con un sorriso malizioso e provocante, le sue ali scure da succubus che fremono appena dietro le sue spalle, i suoi capelli e occhi rosa confetto abbinati alle due corna scarlatte sopra le tempie e la sua coda che ondeggia sinuosa mentre lancia un'occhiata d'intesa a {{user}}. "Benvenuto a Solarton, Zefir. Dato che la tua lettura dell'inglese è ancora arrugginita, mi offro volentieri per qualche lezione privata dopo la cerimonia d'apertura. Dai, Alyssa, Wolfwood sta salendo al podio." """

SCENE_1_STANDARDIZED = """=>Narrator:
La luce radiosa della tarda mattinata inonda i prati del Lunar Quad il 26 agosto 2024, illuminando gli stendardi cremisi e oro issati per il Welcome Day della SUCC. Poiché la cerimonia inaugurale accoglie le famiglie sul campus per gli ultimi saluti prima delle lezioni, l'intero clan Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori Malachia e Noah insieme alle matricole {{user}} e Alyssa, scortati dal padre Erik, dallo zio Logan e dal cugino tredicenne Edric. Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è fermo davanti al microfono d'ottone a ripassare i suoi appunti, mentre i guardiani del campus guidano centinaia di studenti verso il prato.

=>Erik:
"Tenete aperte le linee di comunicazione dopo il discorso d'apertura, e ricordate che la cena di famiglia della domenica non è facoltativa," brontola Erik, la sua presenza imponente che impone largo rispetto tra gli studenti di passaggio mentre il suo sguardo controlla il perimetro.

=>Logan:
"Lasciali godersi la prima mattina sul campus, Erik, hanno aspettato tutta l'estate per questo," dice Logan con un sorriso rassicurante, posando una mano pesante sulla spalla di Edric.

=>Edric:
"Jasper, se hackerate il tabellone dello stadio durante la prima partita dei Bulls, devi assolutamente farmi guardare la diretta dalla tua stanza!" sussurra Edric con un ghigno entusiasta, dondolandosi sui talloni.

=>Noah:
"Il padiglione della KSA sul prato est è già allestito se qualcuno di voi desidera bevande fresche lontano dalla folla delle matricole," osserva Noah con impeccabile compostezza, sistemandosi i gemelli dei polsini.

=>Malachia:
"Ho già perlustrato Wyrm Hall e Greek Row. Chiunque superi il limite con uno di voi due dovrà risponderne a me," dichiara Malachia con voce ferma, le braccia incrociate sul petto.

=>Alyssa:
Accanto a {{user}}, Alyssa Hvit Douglas Bloodmoon stringe al petto il suo diario erboristico rilegato in pelle; le sue orecchie bianche da lupo si drizzano sulla sommità del capo, un unico paio lupino senza alcuna orecchia umana ai lati della testa, mentre guarda verso l'arco di pietra principale.
"Cerca di non infiltrarti nella telemetria dell'amministrazione durante il discorso di Wolfwood, Jasper. Aspetta. Guarda chi è appena entrato sul quad."

=>Narrator:
Un mormorio di incredulità percorre il viale principale quando Wulfnic Báleygr Bloodmoon avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. L'antico Jarl indossa con fierezza regale l'outfit gag che proprio {{user}} gli ha regalato: una t-shirt di cotone nero oversize con una lunghissima e fitta lista di Regole per Uscire con Mia Nipote stampata in bianco sulla schiena, abbinata a jeans scuri con l'apertura per la coda da lupo argentata, pesanti stivali da motociclista e un torque d'argento ritorto al collo. Accanto a lui, Zefir sembra un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una fiera cresta alla moicana e indossa un giubbotto di pelle nera coperto di borchie d'argento sopra una canotta nera strappata e jeans aderenti, con l'orario delle lezioni da matricola infilato tra due dita tatuate.

=>Wulfnic:
"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!" ruggisce Wulfnic con una risata profonda e tonante, dando una pacca così forte sulla spalla di Zefir da far tintinnare le borchie.
"Ho preso spunto da te, Jasper! Per assicurarmi che Alyssa abbia un'ombra in più a proteggerla nel campus, stamattina ho iscritto anche Zefir all'università. Sui documenti risulta come un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo marcato accento norreno e la sua poca dimestichezza con l'inglese scritto."

=>Zefir:
"Continua pure a ridere, vecchio, e vediamo chi mi tradurrà questi maledetti programmi dei corsi stasera," ribatte Zefir con un ghigno insolente e vivace, i suoi occhi azzurro ghiaccio accesi dalla spavalderia indomita del guerriero vichingo sedicenne che era e dal brio imprevedibile del vento dei mari del Nord, mentre tocca il revers borchiato verso {{user}} e Alyssa.
"Che ne dici, Svartr? Il tuo nuovo cugino islandese è ufficialmente una matricola universitaria. Basta che non mi chiediate di scrivere un tema, a meno che non lo vogliate inciso sulla cattedra col pugnale."

=>Narrator:
Finnegan Novak attraversa il prato dal complesso atletico nella sua felpa grigia da hockey dei Bears, arrivando insieme a Scarlett Rose e Sierra Cruz giusto in tempo per sentire la famiglia presentare Zefir con la copertura del lontano cugino dall'Islanda per evitare che si mettano sul chi vive. Anche se Zefir ha completamente annullato la sua aura divina da Enigma, sembrando a tutti gli effetti un licantropo qualsiasi in mezzo a centinaia di studenti, l'istinto di Finn avverte comunque un inspiegabile senso di inferiorità davanti a quel ragazzo dalla cresta bianca. Il suo unico paio di orecchie da lupo artico si piega lievemente sulla sommità del capo, senza orecchie umane ai lati, mentre raddrizza le spalle e prova subito a mostrarsi più figo davanti ad Alyssa.

=>Finn:
"Bello vederti alla luce del sole, Svartr. Stavo giusto dicendo ad Alyssa che il coach mi ha messo nel primo blocco di power-play, quindi se vostro cugino dall'Islanda vuole vedere cosa significa vera velocità sul ghiaccio, lo metto nella lista VIP," si vanta Finn, infilando i pollici nelle tasche della felpa e assumendo una posa plastica da atleta a beneficio di Alyssa.

=>Sierra:
"Ferma tutto, devo assolutamente sapere dove hai preso quel giubbotto di pelle adesso," interviene Sierra, strisciando più vicino sulla sua imponente coda da serpente color arcobaleno, le scaglie iridescenti che riflettono il sole e i capelli color arcobaleno che ondeggiano mentre ammira le file di borchie d'argento sulle spalle di Zefir. "Sul serio, nessuno a Solarton lavora la pelle così. Dove l'hai preso in Islanda?"

=>Scarlett:
"Devo ammettere che lo stile da vichingo ribelle ti dona in modo pericoloso, Zefir," mormora Scarlett inclinando la testa così che i suoi capelli rosa confetto sfiorino le corna scarlatte che spuntano sopra le tempie, un lampo malizioso e civettuolo nei suoi occhi rosa confetto mentre flirta con lui prima di lanciare uno sguardo complice a {{user}}. "Se tuo cugino avesse bisogno di una mano per decifrare i manuali in inglese, Jasper, sai dove trovarmi. Dai, venite a sedervi con noi sul prato sud prima che Wolfwood inizi il discorso." """

MSG0_STANDARDIZED = """=>Narrator:
Il sole della tarda mattinata batte sui prati gremiti del Lunar Quad il 26 agosto 2024, filtrando tra gli stendardi cremisi e oro issati per il Welcome Day della SUCC. Poiché la cerimonia inaugurale è aperta anche ai familiari degli studenti per gli ultimi saluti prima dell'inizio delle lezioni, l'intero clan Douglas-Bloodmoon ha accompagnato sul quad i quattro iscritti all'università: i fratelli maggiori Noah e Malachia insieme ai gemelli matricole Jasper e Alyssa, scortati dal padre Erik, dallo zio Logan e dal cugino tredicenne Edric. Sul palco del padiglione centrale, il Cancelliere Archer Wolfwood è affiancato dai presidi di facoltà mentre i tecnici del suono regolano il microfono d'ottone.

=>Erik:
"Restate uniti quando la folla si disperderà dopo il discorso, e chiamate subito se i guardiani del campus vi danno qualsiasi problema," brontola Erik, la sua alta figura che proietta un'ombra protettiva sul vialetto mentre i suoi occhi ambrati scrutano il prato.

=>Logan:
"Lasciali respirare, Erik, è l'orientamento universitario, non un assedio," dice Logan con una risata calorosa, posando una mano massiccia sulla spalla di Edric.

=>Edric:
"Aspetta di vedere quanto è grande la mensa, Jasper! Ma le matricole hanno davvero i pass illimitati anche per la sala giochi dell'Annex?" chiede Edric con entusiasmo, allungando il collo verso l'edificio dell'unione studentesca.

=>Noah:
"Il tendone di rappresentanza della KSA sul prato est ha bevande fresche e posti all'ombra riservati per noi quando volete sfuggire al caldo," osserva Noah con eleganza, sistemandosi il revers della giacca di lino su misura.

=>Malachia:
"Ho già controllato il perimetro dalla palestra fino a Greek Row. Nessuno darà fastidio alla mia sorellina in questo campus," aggiunge Malachia con tono basso e roca fermezza, incrociando le braccia sul petto.

=>Jasper:
Accanto a Alyssa, Jasper alza lo sguardo dalla telemetria di rete sul suo datapad; le sue orecchie scure da lupo si orientano verso il cancello principale, un unico paio lupino sulla sommità del capo senza alcuna orecchia umana ai lati della testa.
"Le registrazioni delle matricole hanno già mandato in crash il server centrale della biblioteca," mormora Jasper, dando un leggero colpetto di gomito a Alyssa. "Aspetta un secondo. Guarda chi sta varcando l'arco di pietra principale proprio adesso."

=>Narrator:
Il brusio lungo il viale centrale si apre in un'ondata di silenzio stupefatto quando Wulfnic Báleygr Bloodmoon avanza sul Lunar Quad con Zefir Hvitskog al suo fianco. Lo Jarl di Svartúlfr, a milleduecento anni compiuti, sfoggia il suo outfit gag preferito con solenne e fierissimo orgoglio: una t-shirt di cotone nero oversize regalatagli da Jasper che porta stampata sulla schiena, a grandi caratteri bianchi, una lunghissima e fitta lista di Regole per Uscire con Mia Nipote, abbinata a jeans scuri con l'apertura sartoriale per la coda da lupo argentata, pesanti stivali da motociclista con fibbie e un antico torque d'argento ritorto al collo. Accanto a lui, Zefir ha tutto l'aspetto di un giovane ribelle punk sui vent'anni: i suoi capelli bianco-neve sono rasati ai lati in una netta cresta alla moicana e indossa un pesante giubbotto di pelle nera tempestato di borchie d'argento sopra una canotta nera strappata e jeans aderenti, tenendo il fascicolo dell'orientamento piegato in una mano tatuata.

=>Wulfnic:
"In fondo non sei mai andato a scuola e tecnicamente sei un ragazzino!" tuona Wulfnic scoppiando in una risata profonda e fragorosa, mentre batte una manata pesante sulla spalla borchiata di Zefir.
"Non fare quella faccia sorpresa, Erik! Per assicurarmi che la nostra piccola Alyssa sia protetta come si deve nel campus, ho deciso di iscrivere anche Zefir all'università. Per la segreteria è un vostro lontano parente appena arrivato dall'Islanda, così giustifichiamo il suo accento marcatamente norreno e la sua poca dimestichezza con l'inglese scritto."

=>Zefir:
"Ridi pure quanto vuoi, mio Jarl, ma se qualche professore pieno di sé mi agita un gessetto sotto il naso, non prometto di lasciarglielo intero," ribatte Zefir con un ghigno sfrontato e vivace, la spavalderia giovanile del vichingo sedicenne che era un tempo che gli brilla negli occhi azzurro ghiaccio come una raffica di vento del Mare del Nord, prima di rivolgere un beffardo saluto a due dita a Alyssa e Jasper.
"Tranquilla, cuginetta. Il tuo parente islandese è ufficialmente una matricola. Indicami chiunque ti guardi storta e sparirà prima che suoni la campanella."

=>Narrator:
Finnegan Novak attraversa il flusso dell'orientamento dal padiglione atletico con il suo giubbotto da varsity dei Bears su una spalla, arrivando insieme a Scarlett Rose e Sierra Cruz. Per evitare che i tre compagni di campus si mettano sul chi vive attorno a un Firstborn, la famiglia presenta subito Zefir con la copertura del lontano cugino appena atterrato dall'Islanda per il suo primo anno. Poiché Zefir ha completamente schermato la sua aura divina da Enigma, ai loro sensi appare come un normale e trasandato licantropo in chiodo di pelle punk, eppure la postura di Finn si irrigidisce immediatamente. Il suo unico paio di orecchie da lupo bianco si appiattisce leggermente sulla sommità del capo, senza alcuna orecchia umana ai lati, mentre un inspiegabile istinto primordiale lo fa sentire stranamente surclassato dal giovane sconosciuto islandese, spingendolo a gonfiare il petto per darsi un tono davanti a Alyssa.

=>Finn:
"Ci ho messo venti minuti a seminare gli osservatori vicino all'arena, Alyssa. Il coach mi ha già inserito nel primo blocco di power-play per la prima di campionato, quindi se tuo cugino dall'Islanda vuole vedere come si gioca il vero hockey universitario, posso fargli avere i pass in prima fila," si vanta Finn, appoggiandosi alla balaustra di pietra e flettendo con disinvoltura l'avambraccio mentre si sistema il colletto della varsity.

=>Sierra:
"Un attimo, fermi tutti, devo assolutamente sapere dove hai preso quel chiodo adesso," interviene Sierra, la sua imponente coda da serpente color arcobaleno che scivola fluida e sinuosa tra le panchine di pietra mentre striscia più vicina a Zefir, i suoi capelli arcobaleno che brillano al sole e le sue scaglie iridescenti che riflettono la luce mentre esamina con invidia genuina le file di pesanti borchie d'argento sui suoi revers. "I dettagli della pelle consumata e quelle punte personalizzate sembrano vintage europeo d'avanguardia. C'è qualche boutique underground a Reykjavik che dovrei conoscere?"

=>Scarlett:
"Devo ammettere che lo stile punk islandese ti dona in modo pericoloso, Zefir," mormora Scarlett con un sorriso malizioso e provocante, le sue ali scure da succubus che fremono appena dietro le sue spalle, i suoi capelli e occhi rosa confetto abbinati alle due corna scarlatte sopra le tempie e la sua coda che ondeggia sinuosa mentre lancia un'occhiata d'intesa a Alyssa. "Benvenuto a Solarton, Zefir. Dato che la tua lettura dell'inglese è ancora arrugginita, mi offro volentieri per qualche lezione privata dopo la cerimonia d'apertura. Dai, Alyssa, Wolfwood sta salendo al podio." """

EXPECTED_SPEAKERS_SCENE_0 = [
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Jasper',
    'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett'
]

EXPECTED_SPEAKERS_SCENE_1 = [
    'Narrator', 'Erik', 'Logan', 'Edric', 'Noah', 'Malachia', 'Alyssa',
    'Narrator', 'Wulfnic', 'Zefir', 'Narrator', 'Finn', 'Sierra', 'Scarlett'
]

EXPECTED_SPEAKERS_SCENE_2 = [
    'Narrator', 'Erik', 'Logan', 'Narrator'
]

EXPECTED_SPEAKERS_MSG0 = EXPECTED_SPEAKERS_SCENE_0


def validate_formatting_discipline(text: str, label: str):
    """Enforces zero em-dashes, zero asterisks, and valid =>Speaker: structure."""
    em_dashes = text.count('—')
    if em_dashes > 0:
        raise ValueError(f"Formatting Violation in {label}: found {em_dashes} em-dashes ('—'). Must be 0.")

    asterisks = text.count('*')
    if asterisks > 0:
        raise ValueError(f"Formatting Violation in {label}: found {asterisks} asterisks ('*'). Actions must be plain text.")

    if not text.startswith('=>Narrator:'):
        raise ValueError(f"Structural Violation in {label}: text must start with '=>Narrator:'.")

    tags = re.findall(r'^=>([A-Za-z0-9_]+):', text, flags=re.MULTILINE)
    if not tags:
        raise ValueError(f"Structural Violation in {label}: no '=>Speaker:' tags found.")

    # Check for unparsed plain speakers (e.g. 'Erik Ulfr Douglas:' or 'Erik:')
    plain_speakers = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', text, flags=re.MULTILINE)
    plain_speakers = [s for s in plain_speakers if not s.startswith('=>')]
    if plain_speakers:
        raise ValueError(f"Syntax Violation in {label}: found plain speaker prefixes without '=>': {plain_speakers}")

    return tags


def get_auth_token():
    """Reads auth token, refreshing if file does not exist or refresh is needed."""
    if TOKEN_PATH.exists():
        token = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if token:
            return token

    print("[AUTH] Token not found or empty. Refreshing token...")
    import subprocess
    subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
    return TOKEN_PATH.read_text(encoding='utf-8').strip()


def api_request(url: str, method: str = 'GET', data: dict = None, token: str = None):
    """Executes authenticated HTTPS request against Wyvern Web API."""
    if token is None:
        token = get_auth_token()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    body = json.dumps(data).encode('utf-8') if data is not None else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            return resp.status, json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        # If token expired (401/403), try refresh once
        if e.code in (401, 403):
            print(f"[AUTH] Received HTTP {e.code}. Attempting token refresh...")
            import subprocess
            subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
            token = TOKEN_PATH.read_text(encoding='utf-8').strip()
            headers['Authorization'] = f'Bearer {token}'
            req = urllib.request.Request(url, data=body, headers=headers, method=method)
            with urllib.request.urlopen(req) as retry_resp:
                content = retry_resp.read().decode('utf-8')
                return retry_resp.status, json.loads(content) if content else {}
        err_msg = e.read().decode('utf-8', errors='replace')
        print(f"[ERROR] API HTTP {e.code} on {method} {url}: {err_msg[:400]}")
        raise


def update_local_scenario_file():
    """Updates FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json with standardized scenes."""
    print(f"\n[STEP 1] Validating and updating local scenario file: {SCENARIO_JSON_PATH}")

    # Validate texts first
    tags_0 = validate_formatting_discipline(SCENE_0_STANDARDIZED, "Scene 0 (Alyssa POV)")
    tags_1 = validate_formatting_discipline(SCENE_1_STANDARDIZED, "Scene 1 (Jasper POV)")
    tags_m = validate_formatting_discipline(MSG0_STANDARDIZED, "Message #0")

    assert tags_0 == EXPECTED_SPEAKERS_SCENE_0, f"Scene 0 tags mismatch: {tags_0} vs {EXPECTED_SPEAKERS_SCENE_0}"
    assert tags_1 == EXPECTED_SPEAKERS_SCENE_1, f"Scene 1 tags mismatch: {tags_1} vs {EXPECTED_SPEAKERS_SCENE_1}"
    assert tags_m == EXPECTED_SPEAKERS_MSG0, f"Message #0 tags mismatch: {tags_m} vs {EXPECTED_SPEAKERS_MSG0}"
    print("[PASS] All formatting discipline and tag assertions passed for Scene 0, Scene 1, and Message #0.")

    with open(SCENARIO_JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    premade = data.get('premade_scenes', [])
    if len(premade) < 3:
        raise ValueError(f"Expected at least 3 premade_scenes, got {len(premade)}")

    # Update Scene 0
    premade[0]['scene_text'] = SCENE_0_STANDARDIZED
    # Update Scene 1
    premade[1]['scene_text'] = SCENE_1_STANDARDIZED
    # Verify Scene 2
    validate_formatting_discipline(premade[2]['scene_text'], "Scene 2 (Corale)")

    data['premade_scenes'] = premade

    with open(SCENARIO_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Saved standardized scenario to {SCENARIO_JSON_PATH}")
    return data


def deploy_scenario_to_api(scenario_data: dict):
    """Deploys scenario to Wyvern Web API PUT /api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H."""
    print(f"\n[STEP 2] Deploying scenario {SCENARIO_ID} to Wyvern Web API...")
    url = f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}"

    # Build clean deployment payload matching Wyvern scenario schema
    world_id = scenario_data.get('world', {}).get('id') if isinstance(scenario_data.get('world'), dict) else scenario_data.get('world')
    location_id = scenario_data.get('location', {}).get('id') if isinstance(scenario_data.get('location'), dict) else scenario_data.get('location')
    environment_id = scenario_data.get('environment', {}).get('id') if isinstance(scenario_data.get('environment'), dict) else scenario_data.get('environment')

    payload = {
        "world_id": world_id,
        "world": world_id,
        "name": scenario_data.get('name'),
        "description": scenario_data.get('description'),
        "scenario_premise": scenario_data.get('scenario_premise'),
        "tags": scenario_data.get('tags', []),
        "community_tags": scenario_data.get('community_tags', []),
        "avatar": scenario_data.get('avatar'),
        "location_id": location_id,
        "environment_id": environment_id,
        "insertion_point": scenario_data.get('insertion_point', 10489906),
        "visibility": scenario_data.get('visibility', 'private'),
        "rating": scenario_data.get('rating', 'explicit'),
        "world_only": scenario_data.get('world_only', False),
        "scenario_type": scenario_data.get('scenario_type', 'any'),
        "include_character_select": scenario_data.get('include_character_select', True),
        "include_rpg_build": scenario_data.get('include_rpg_build', False),
        "playable_character_ids": scenario_data.get('playable_character_ids', []),
        "included_character_pool": scenario_data.get('included_character_pool', []),
        "scene_instructions": scenario_data.get('scene_instructions', ''),
        "premade_scenes": scenario_data.get('premade_scenes', [])
    }

    status, resp_data = api_request(url, method='PUT', data=payload)
    print(f"[OK] Scenario PUT returned HTTP {status}")

    # Synchronize any server metadata back to local JSON
    if resp_data and isinstance(resp_data, dict) and resp_data.get('premade_scenes'):
        with open(SCENARIO_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(resp_data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Re-synchronized server response into {SCENARIO_JSON_PATH}")

    return resp_data


def patch_active_chat_message():
    """Patches message #0 swipe in chat_log_PJx1W1rg3WUzRM7MnQrkN."""
    print(f"\n[STEP 3] Patching active chat message swipe: {SWIPE_ID}...")
    url = f"https://app.wyvern.chat/api/new/chat-logs/swipe/{SWIPE_ID}"
    payload = {"content": MSG0_STANDARDIZED}

    status, resp_data = api_request(url, method='PUT', data=payload)
    print(f"[OK] Swipe PUT returned HTTP {status}")
    return resp_data


def verify_live_deployment():
    """Queries GET endpoints for scenario and chat log to assert compliance."""
    print(f"\n[STEP 4] Verifying live deployment on Wyvern Web API endpoints...")

    # 1. Verify Scenario
    scenario_url = f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}"
    status_sc, live_scenario = api_request(scenario_url, method='GET')
    print(f"[VERIFY] GET Scenario HTTP {status_sc}")
    assert status_sc == 200, f"Expected HTTP 200, got {status_sc}"

    scenes = live_scenario.get('premade_scenes', [])
    assert len(scenes) == 3, f"Expected 3 premade scenes, got {len(scenes)}"

    # Assert Scene 0 live state
    scene0_text = scenes[0].get('scene_text', '')
    tags_0 = validate_formatting_discipline(scene0_text, "Live Scene 0")
    assert tags_0 == EXPECTED_SPEAKERS_SCENE_0, f"Live Scene 0 speaker tags mismatch: {tags_0}"
    print(f"  [PASS] Live Scene 0 [{scenes[0].get('id')}]: 0 em-dashes, 0 asterisks, tags={tags_0}")

    # Assert Scene 1 live state
    scene1_text = scenes[1].get('scene_text', '')
    tags_1 = validate_formatting_discipline(scene1_text, "Live Scene 1")
    assert tags_1 == EXPECTED_SPEAKERS_SCENE_1, f"Live Scene 1 speaker tags mismatch: {tags_1}"
    print(f"  [PASS] Live Scene 1 [{scenes[1].get('id')}]: 0 em-dashes, 0 asterisks, tags={tags_1}")

    # Assert Scene 2 live state
    scene2_text = scenes[2].get('scene_text', '')
    tags_2 = validate_formatting_discipline(scene2_text, "Live Scene 2")
    assert tags_2 == EXPECTED_SPEAKERS_SCENE_2, f"Live Scene 2 speaker tags mismatch: {tags_2}"
    print(f"  [PASS] Live Scene 2 [{scenes[2].get('id')}]: 0 em-dashes, 0 asterisks, tags={tags_2}")

    # 2. Verify Chat Log
    chat_url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}"
    status_chat, live_chat = api_request(chat_url, method='GET')
    print(f"\n[VERIFY] GET Chat Log HTTP {status_chat}")
    assert status_chat == 200, f"Expected HTTP 200, got {status_chat}"

    messages = live_chat.get('messages', [])
    assert len(messages) >= 1, f"Expected at least 1 message in chat log, got {len(messages)}"
    msg0 = messages[0]
    swipes = msg0.get('swipes', [])
    assert len(swipes) >= 1, f"Expected at least 1 swipe in message 0, got {len(swipes)}"

    swipe0_content = swipes[0].get('content', '')
    tags_msg = validate_formatting_discipline(swipe0_content, "Live Chat Message 0 Swipe")
    assert tags_msg == EXPECTED_SPEAKERS_MSG0, f"Live Message 0 speaker tags mismatch: {tags_msg}"
    print(f"  [PASS] Live Message 0 Swipe [{swipes[0].get('id')}]: 0 em-dashes, 0 asterisks, tags={tags_msg}")

    print("\n[SUCCESS] 100% of live verification assertions passed successfully!")
    return True


def main():
    parser = argparse.ArgumentParser(description="Standardize scenario syntax and patch active chat message #0")
    parser.add_argument('--local-only', action='store_true', help="Only update local JSON without API deployment")
    parser.add_argument('--verify-only', action='store_true', help="Only perform live GET verification")
    args = parser.parse_args()

    if args.verify_only:
        verify_live_deployment()
        return

    scenario_data = update_local_scenario_file()

    if not args.local_only:
        deploy_scenario_to_api(scenario_data)
        patch_active_chat_message()
        verify_live_deployment()


if __name__ == '__main__':
    main()
