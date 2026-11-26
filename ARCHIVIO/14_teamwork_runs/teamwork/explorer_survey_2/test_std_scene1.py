import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

scene_1_std = """=>Narrator:
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
"Devo ammettere che lo stile da vichingo ribelle ti dona in modo pericoloso, Zefir," mormora Scarlett inclinando la testa così che i suoi capelli rosa confetto sfiorino le corna scarlatte che spuntano sopra le tempie, un lampo malizioso e civettuolo nei suoi occhi rosa confetto mentre flirta con lui prima di lanciare uno sguardo complice a {{user}}. "Se tuo cugino avesse bisogno di una mano per decifrare i manuali in inglese, Jasper, sai dove trovarmi. Dai, venite a sedervi con noi sul prato sud prima che Wolfwood inizi il discorso.\""""

print("Scene 1 check:")
print("  Em-dash:", scene_1_std.count('—'))
print("  Asterisk:", scene_1_std.count('*'))
print("  Length:", len(scene_1_std))
