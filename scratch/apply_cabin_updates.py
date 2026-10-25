import json
import shutil
import copy

# Paths
LOC_FINAL = 'FINAL/Svartulfr_Location.json'
LOC_OPT = 'lorebooks/optimized/Svartulfr_Location.json'
NPC_FINAL = 'FINAL/Svartulfr_NPC_Secondary.json'
NPC_OPT = 'lorebooks/optimized/Svartulfr_NPC_Secondary.json'

# Texts
MOONFLOWER_CONTENT = """Moonflower Cabin (G-01) e uno dei cottage residenziali da sei persone situato nella Girls Residential Zone di Camp Mystic, affacciato su una baia riparata del Lago Erie e illuminato da lanterne esterne a luminescenza violetta. Lo chalet in legno di cedro e travi runiche e strutturato su un unico livello con soppalco mansardato, progettato con sei alcove letto semi-private separate da pesanti tendaggi in lino fonoassorbente per garantire privacy e riposo anche a specie con abitudini circadiane opposte. L'ambiente include un salottino comune con camino in pietra, un angolo cottura provvisto di dispensa e doppio frigorifero (con scomparto schermato e sigillato per le razioni ematiche dei donatori e le conserve mediche), e due bagni completi dotati di estrattori d'aria potenziati. Il programma residenziale di Camp Mystic distribuisce appositamente una studentessa per ciascuno dei cinque anni di corso, a cui si aggiunge Alyssa Douglas-Bloodmoon come sesta occupante durante il soggiorno estivo.

Alyssa porta nello chalet una presenza rassicurante, dolce ma autorevole, intrisa del profumo naturale di miele selvatico, pioggia e moonflower. Come studentessa di medicina e guaritrice di branco, Alyssa e diventata rapidamente il punto di riferimento emotivo e sanitario della cabina: gestisce la cassetta di pronto soccorso, prepara tisane lenitive per calmare lo stress somatico e le fluttuazioni sensoriali, e offre ascolto senza giudizio. La sua indole protettiva si armonizza con le diverse nature delle compagne, creando un clima sereno che smussa le inevitabili tensioni tra predatori.

Roster delle compagne di stanza:

Year 1: Avery Lin Calder (Vampiro). 18 anni (nata il 1 gennaio 2008). Esile, bruna, sguardo scuro e penetrante. Trasformata di recente e discendente della stirpe dei Sette Originali, Avery sta affrontando il suo primo anno di adattamento con un misto di riserbo e timore di perdere il controllo della sete. Possiede il dono vampirico della fine lettura emotiva, che le permette di percepire le sottili sfumature interiori di chi le sta intorno: questo la rende diffidente ma anche profondamente legata alla genuina gentilezza di Alyssa, che non percepisce come finta. Avery etichetta meticolosamente ogni suo contenitore personale nel frigo e nella dispensa; Alyssa si assicura che nessuno tocchi le sue sacche di sangue conservato e la supporta nei momenti di stanchezza all'alba.

Year 2: Sofia Mae Rourke (Strega). 19 anni (nata l'8 febbraio 2007). Statura minuta, fisico atletico, capelli ramati rasati ai lati con ciuffo ribelle e occhi ambrati. Spigliata, creativa e dotata di un'ironia caustica che smorza qualsiasi litigio, Sofia e una specialista in barriere, trasmutazione elementale e contromagie. Riempie la sua alcova di candele d'argilla, gessetti runici e tomi spiegazzati. Sofia e Alyssa trascorrono lunghe serate a confrontare l'erboristeria magica con la farmacologia clinica, e Sofia usa spesso piccoli trucchi pirotecnici innocui per far sorridere le compagne dopo giornate di duro allenamento.

Year 3: Nadia Elise Voss (Licantropo). 20 anni (nata il 4 marzo 2006). Corporatura morbida e robusta, chioma biondo cenere e occhi dorati. Nadia appartiene alla famiglia Voss ed e imparentata con la direttrice Mara Voss. Tranquilla, leale e dotata di una forte empatia di branco, Nadia comprende d'istinto la natura lupina di Alyssa, verso la quale nutre un rispetto spontaneo privo di servilismo. Nadia e la compagna con cui Alyssa condivide le corse mattutine lungo il perimetro boschivo e la gestione dei turni di pulizia della cabina, garantendo stabilita quando la luna piena altera l'umore delle residenti.

Year 4: Talia June Mercer (Donna-Orso / Werebear). 21 anni (nata l'11 aprile 2005). Pelle scura, spalle forti, fisico compatto e atletico, sorella di Theo Mercer (alloggiato nella Ironwood Cabin con Jasper). Talia e la roccia dello chalet: dotata di una forza fisica colossale e di un potere di ancoraggio cinetico, ha un carattere schietto, silenzioso e profondamente protettivo. Non ama i fronzoli e parla poco, ma quando una discussione rischia di degenerare le basta un sospiro profondo o uno sguardo severo per ristabilire l'ordine. In Alyssa riconosce una coetanea seria e responsabile su cui poter sempre contare.

Year 5: Mina Rae Sato (Catwere Beastwere). 22 anni (nata il 7 maggio 2004). Flessuosa, agile come una ballerina, capelli castani ondulati e occhi grigio-argento. Mina e un Beastwere felino: il suo corpo originario e permanente e quello di un grande felino selvatico, mentre la forma umanoide e una costruzione magica temporanea. Essendo al quinto e ultimo anno, Mina e la veterana della Moonflower Cabin: conosce ogni sentiero della riserva, ogni scorciatoia e il programma dei custodi, guidando le compagne piu giovani con consigli pratici e un atteggiamento sornione e rilassato. Adora appollaiarsi sul parapetto della veranda al tramonto e apprezza la quiete che Alyssa sa mantenere nello spazio comune.

La convivenza nella Moonflower Cabin e regolata da un'intesa tacita e affiatata. I turni del bagno tengono conto dei ritmi circadiani opposti tra il sonno diurno di Avery e le sveglie all'alba dei licantropi e degli shifters. La ventilazione magica e i filtri agli ioni curati da Sofia neutralizzano i picchi feromonici durante i cicli lunari, mentre la cucina comune e il teatro di merende serali a base di pasticcini al miele di moonflower e tisane preparate da Alyssa."""

IRONWOOD_CONTENT = """Ironwood Cabin (B-01) e uno dei principali lodge residenziali da sei persone della Boys Residential Zone di Camp Mystic, situato su un promontorio roccioso circondato da pini neri e affacciato sulla riva settentrionale del lago, illuminato da lanterne esterne a luminescenza ambrata. Costruito con massicci tronchi di quercia e finiture in ferro battuto, lo chalet e dotato di sei cuccette rinforzate in legno massello distribuite in alcove schermate, progettate per sopportare il peso e l'impatto di mutaforma e licantropi di grossa taglia. La struttura comprende un'ampia sala comune riscaldata da una stufa in ghisa a legna, un grande tavolo da lavoro centrale equipaggiato con prese schermate e stazioni di ricarica per banchi ottici ed elettronici, una cucina comune e doppi servizi rinforzati. Originariamente assegnato a cinque studenti, lo chalet e stato riorganizzato a sei posti per consentire a Jasper Douglas-Bloodmoon di alloggiare insieme al cugino minore Edric, trasferendo il vampiro Year 1 Rylan Elias Cade presso la vicina B-07 Lake Wolf Cabin per ragioni di capienza.

Jasper occupa la postazione piu appartata della cabina, con laptop blindato, cuffie antirumore e apparecchiature radio per monitorare le frequenze del lago. Come Beta della Casata Douglas, Jasper governa l'ambiente con un'autorita calma, metodica e protettiva: non alza la voce ne impone ordini superflui, ma la sua mente strategica assicura disciplina e rispetto degli spazi. La sua attenzione primaria e rivolta a Edric, facendogli da fratello maggiore, mentore e punto fermo affinche il ragazzo canalizzi la sua esuberanza in modo costruttivo.

Roster dei compagni di stanza:

Year 1 (Junior Division): Edric Douglas (Cugino / Licantropo, Canis Lupus Svartulfr). 12 anni. Figlio del compianto Cornelius Douglas e cugino di Jasper, Alyssa, Malachia e Noah. Edric e un giovane licantropo Gamma purosangue di nobile lignaggio, leale, energico e orgoglioso delle tradizioni di famiglia. Ammesso al programma giovanile estivo di Camp Mystic per perfezionare la disciplina atletica e la resistenza, alloggia nella Ironwood Cabin sotto la custodia vigile di Jasper, che considera un mito vivente. Corre come running back nella squadra giovanile di Solarton, adora l'allenamento fisico e porta nella cabina un entusiasmo travolgente, tempestando Jasper di domande sui sistemi di sicurezza e sulle tattiche del branco.

Year 2: Theo James Mercer (Mago / Wizard). 19 anni (nato il 2 febbraio 2007). Fisico atletico, chioma ramata rasata sui lati, occhi castano dorati, fratello di Talia Mercer (alloggiata nella Moonflower Cabin con Alyssa). Theo e un mago sveglio, socievole e brillante, specializzato in costrutti runici, barriere protettive e circuiti ad assorbimento eterico. Tra Theo e Jasper e nata un'immediata intesa intellettuale: i due trascorrono intere serate al banco da lavoro comune a saldare componenti magitech, integrando i sensori digitali di Jasper con i sigilli difensivi di Theo.

Year 3: Jace Nolan Hart (Licantropo). 20 anni (nato il 9 marzo 2006). Fisico compatto e vigoroso, capelli biondo cenere e occhi ambrati. Jace e un lupo leale, serio e orientato al gioco di squadra, privo di complessi gerarchici verso la dinastia Douglas, di cui riconosce l'autorevolezza naturale. Funge da solido compagno di sparring all'aperto e affianca volentieri Jasper nel seguire Edric durante le corse campestri e i percorsi a ostacoli nei boschi, aiutando il ragazzino a perfezionare i riflessi.

Year 4: Evan Adrian Voss (Uomo-Cinghiale / Wereboar). 21 anni (nato il 2 aprile 2005). Corporatura massiccia e pesante, sguardo risoluto e carattere pragmatico, fratello di Nadia Voss e parente della direttrice Mara Voss. Evan e lo specialista della cabina per le barriere di schermatura cinetica e la manutenzione pesante: spacca la legna per la stufa, controlla i cardini e le travi del lodge e si esprime senza peli sulla lingua. E un ragazzo schietto che odia i drammi inutili e bilancia l'entusiasmo dei piu giovani con un sano realismo, nutrendo un forte rispetto per la fredda lucidita di Jasper.

Year 5: Nico Samuel Reed (Wolfwere Beastwere). 22 anni (nato il 1 maggio 2004). Flessuoso, scattante come un corridore, capelli castani e occhi grigio-argento. Nico e un Beastwere lupino: la sua forma permanente e originaria e quella di un vero lupo selvatico dei boschi, mentre l'aspetto umano e un costrutto magico temporaneo. Veterano del quinto anno, Nico offre alla cabina una saggezza singolare sulla convivenza tra istinto animale e coscienza razionale. Ha instaurato un legame istintivo con Jasper, Jace ed Edric, fungendo da guida esperta che conosce ogni anfratto della riserva lacustre.

Nota logistica su Rylan Elias Cade: Originariamente assegnato alla cabina come Year 1, Rylan e stato riassegnato alla B-07 Lake Wolf Cabin per fare spazio a Edric senza violare il limite di sei occupanti, mantenendo comunque ottimi rapporti con i compagni della Ironwood Cabin durante le attivita diurne e gli scambi al molo.

La vita nella Ironwood Cabin e vivace, operosa e cameratesca. Le mattinate partono presto con tuffi dal molo, sessioni di trazioni tra Jace, Evan ed Edric, e la messa a punto dei ricevitori radio di Jasper e Theo. La sera, attorno alla stufa in ghisa o sui gradini di quercia, le diverse nature lupine (il Beta Jasper, il giovane Gamma Edric, il lupo di branco Jace e il vero lupo Nico) creano un'intesa naturale e solida, armonizzata dalla concretezza di Evan e dalla vivacita magica di Theo."""

LAKE_WOLF_CONTENT = """Lake Wolf Cabin (B-07) is one of the residential cabins in the Boys Residential Zone of Camp Mystic, situated near the wooded shoreline. Camp Mystic deliberately mixes program years so each cabin contains one first-year through one fifth-year rather than isolating newcomers together. In addition, Rylan Elias Cade (Vampire, Year 1) was reassigned here from B-01 Ironwood Cabin to accommodate Edric Douglas under Jasper's custody.

 Year 1: Soren Hale Navarro , Zombie
 Year 1 (Transfer): Rylan Elias Cade , Vampire (reassigned from B-01 Ironwood Cabin)
 Year 2: Damian Cole Wynn , Gorgon
 Year 3: Julian Ash Mercer , Avian Beastfolk
 Year 4: Kellan Reid Novak , True Dragon
 Year 5: Micah Owen Cross , Merman

The fifth-year is expected to model camp navigation and basic routines, not act as unpaid staff. Cabinmates share a living room, kitchenette, bathrooms, refrigerator, chores, and enough proximity to learn exactly which habits annoy one another. The cabin can become family-like, hostile, competitive, protective, or simply practical depending on who is having a good week."""

# 1. Update Location
with open(LOC_FINAL, 'r', encoding='utf-8') as f:
    loc_data = json.load(f)

# Find entries by comment/title or index
for idx in range(len(loc_data['entries'])):
    e = loc_data['entries'][idx]
    c = e.get('comment', '')
    
    # Moonflower
    if 'G-01' in c or 'Moonflower' in c:
        print(f"Updating Moonflower at entries[{idx}]")
        e['comment'] = "🛖 G-01 Moonflower Cabin: Compagne di Stanza di Alyssa"
        e['name'] = "G-01 Moonflower Cabin: Compagne di Stanza di Alyssa"
        e['keys'] = ["G-01 Moonflower Cabin (Girls Zone)", "Moonflower Cabin", "Moonflower", "compagne Alyssa", "Alyssa roommates", "Alyssa cabin", "Avery Calder", "Sofia Rourke", "Nadia Voss", "Talia Mercer", "Mina Sato", "G-01"]
        e['secondary_keys'] = ["Camp Mystic", "chalet", "camper", "dormitorio", "stanza", "compagne", "turno", "convivenza"]
        e['key_logic'] = "AND_ANY"
        e['position'] = "before_char"
        e['priority'] = 2
        e['type'] = "location"
        e['content'] = MOONFLOWER_CONTENT
        if 'wyvern' in e.get('extensions', {}):
            e['extensions']['wyvern']['priority'] = 2
            e['extensions']['wyvern']['position'] = 'before_char'
            
    # Ironwood
    if 'B-01' in c or 'Ironwood' in c:
        print(f"Updating Ironwood at entries[{idx}]")
        e['comment'] = "🛖 B-01 Ironwood Cabin: Compagni di Stanza di Jasper"
        e['name'] = "B-01 Ironwood Cabin: Compagni di Stanza di Jasper"
        e['keys'] = ["B-01 Ironwood Cabin (Boys Zone)", "Ironwood Cabin", "Ironwood", "compagni Jasper", "Jasper roommates", "Jasper cabin", "Edric Douglas", "Theo Mercer", "Jace Hart", "Evan Voss", "Nico Reed", "B-01"]
        e['secondary_keys'] = ["Camp Mystic", "chalet", "camper", "dormitorio", "stanza", "compagni", "turno", "convivenza", "Rylan Cade"]
        e['key_logic'] = "AND_ANY"
        e['position'] = "before_char"
        e['priority'] = 2
        e['type'] = "location"
        e['content'] = IRONWOOD_CONTENT
        if 'wyvern' in e.get('extensions', {}):
            e['extensions']['wyvern']['priority'] = 2
            e['extensions']['wyvern']['position'] = 'before_char'

    # Lake Wolf
    if 'B-07' in c or 'Lake Wolf' in c:
        print(f"Updating Lake Wolf at entries[{idx}]")
        e['content'] = LAKE_WOLF_CONTENT
        if 'Rylan Cade' not in e['keys']:
            e['keys'].extend(['Rylan Cade', 'Rylan Elias Cade'])

# Synchronize lexicon with entries
loc_data['lexicon'] = copy.deepcopy(loc_data['entries'])

with open(LOC_FINAL, 'w', encoding='utf-8') as f:
    json.dump(loc_data, f, ensure_ascii=False, indent=2)

shutil.copyfile(LOC_FINAL, LOC_OPT)
print("Saved Svartulfr_Location.json to FINAL and lorebooks/optimized/")

# 2. Update NPC Secondary (Rylan Cade)
with open(NPC_FINAL, 'r', encoding='utf-8') as f:
    npc_data = json.load(f)

for idx in range(len(npc_data['entries'])):
    e = npc_data['entries'][idx]
    c = e.get('comment', '')
    if 'Rylan' in c or 'Cade' in c:
        print(f"Updating Rylan Cade at entries[{idx}]")
        content = e['content']
        # Replace affiliation
        content = content.replace("AFFILIATION: Camp Mystic (B-01 Ironwood Cabin);", "AFFILIATION: Camp Mystic (B-07 Lake Wolf Cabin);")
        # Replace background mention of Ironwood Cabin
        content = content.replace("They entered Ironwood Cabin expecting Camp Mystic to feel like exile.", "Originally assigned to Ironwood Cabin before being reassigned to B-07 Lake Wolf Cabin for capacity reasons to accommodate Edric Douglas under Jasper's custody, Rylan entered Camp Mystic expecting it to feel like exile.")
        e['content'] = content
        if 'B-07 Lake Wolf Cabin' not in e.get('keys', []):
            e['keys'].append('B-07 Lake Wolf Cabin')

# Synchronize lexicon with entries
npc_data['lexicon'] = copy.deepcopy(npc_data['entries'])

with open(NPC_FINAL, 'w', encoding='utf-8') as f:
    json.dump(npc_data, f, ensure_ascii=False, indent=2)

shutil.copyfile(NPC_FINAL, NPC_OPT)
print("Saved Svartulfr_NPC_Secondary.json to FINAL and lorebooks/optimized/")
