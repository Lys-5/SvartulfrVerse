# Mappe del World: style bible e prompt

Aggiornato: 2026-09-06. Derivato dalle tre mappe esistenti (Blackwood City,
mappa regionale, SUCC Main Campus).

---

## 0. Decisioni prese

| Questione | Decisione |
|---|---|
| Tracciato dello Yarrow | **Passa dentro Hex Valley.** La valle e' scavata dal fiume, che le da' anche l'acqua per i vigneti |
| Modello di generazione | **Modello a forte aderenza al prompt** (Nano Banana / Gemini Image e simili) |
| Colore signature | **Giallo girasole `#FFC512`.** Il corallo e' ritirato. Vedi §10 |

Conseguenza sulla sintassi dei prompt: **prosa descrittiva lunga, non tag.**
Niente pesi tra parentesi, niente `--ar`, niente negative prompt separato. Le
esclusioni si scrivono dentro la frase ("with no text anywhere in the image").
Il formato si chiede a parole ("a wide landscape image"). Sono modelli che
reggono istruzioni condizionali complesse, quindi le regole strutturali del
World (le strade che si fermano al limite del bosco, il bordo delle ward dove
la luce cambia di colpo) vanno **dette esplicitamente come regole**, non
suggerite: e' esattamente quello in cui questi modelli sono piu' forti dei
diffusori a tag.

---

## 1. Il testo: regola corretta il 2026-09-06

**La versione precedente di questa sezione era sbagliata.** Diceva che nessun
modello di immagini scrive testo leggibile e che le etichette delle tre mappe
esistenti erano state messe in post con un editor. Non e' cosi': **le mappe sono
state generate integralmente da Nano Banana 2, etichette comprese**, e la
tipografia che si vede, nomi di distretto, descrittori su due righe, corsivi
lungo il fiume, e' uscita dal modello.

Quindi il testo si puo' generare, e in pratica regge: sulla mappa regionale ha
attraversato **cinque rigenerazioni** senza un errore, e alla sesta ha ceduto in
un punto solo.

**Conseguenze operative:**

1. **Non esiste una "base pulita" da ricolorare.** Ogni modifica di una mappa
   finita rimette in gioco le etichette, e non c'e' modo di aggirarlo lavorando
   su un livello separato. Il budget di rigenerazioni del §12 e' quindi un
   vincolo reale, non una precauzione.
2. **La difesa migliore non e' "non toccare il testo", e' dare il testo.** In
   ogni prompt di modifica va incollato **l'elenco completo e letterale di tutte
   le etichette**, dichiarato come ortografia autoritativa. Cosi' anche quando il
   modello le ridisegna, le ridisegna giuste. Chiedere solo di "conservarle
   identiche" lo lascia a copiare da un'immagine, che e' esattamente dove
   introduce refusi.
3. Un refuso gia' presente si corregge **nello stesso passaggio**, indicandolo
   esplicitamente. Esempio reale: sulla mappa di Blackwood il descrittore di The
   Dead Zone dice "denser, darter" invece di "denser, darker".
4. Per le mappe **nuove** resta valido chiedere l'immagine senza testo, ma per
   una ragione diversa da quella che avevo scritto: non perche' il modello non
   sappia scrivere, ma perche' una base neutra si puo' etichettare in italiano o
   in inglese senza rigenerare.

**Frase di chiusura per le mappe nuove, da tenere:**

```
Render the entire image with no text, no labels, no lettering, no numbers and
no typography of any kind anywhere, not even on signs or banners. Leave clean
empty space where labels would go, because they will be added later by hand.
```

---

## 2. Ci sono due stili, non uno

### Stile A, atlante notturno

Usato per **Blackwood City** e per la **mappa regionale**. E' il linguaggio
cartografico del World.

| Elemento | Come si comporta |
|---|---|
| Vista | Dall'alto, con una leggerissima inclinazione |
| Sfondo | Indaco profondo molto desaturato, quasi nero |
| Strade | Rete **girasole** luminosa, piu' spessa per le autostrade. E' la firma del World |
| Distretti | Campiture piatte traslucide tirate verso uno dei due poli, mai a meta' strada |
| Edifici | **Pochi e rappresentativi**: sei-quindici per distretto, line-art in vista tre quarti, tinti del colore del distretto, con molto vuoto attorno |
| Densita' | **La mappa e' un diagramma, non una pianta.** Nessuna griglia stradale, nessun tessuto di isolati, nessuna rete minore |
| Forma | Sagoma organica arrotondata su fondo scuro vuoto. La citta' **non riempie il fotogramma** |
| Foresta | Texture di conifere verde-teal molto scuro |
| Acqua | Indaco della rampa fredda. Mai grigio, il grigio non e' in palette |
| Etichette | Aggiunte in post, mai generate |

**Blocco di stile Stile A, da incollare in coda al soggetto.** Corretto il
2026-09-06 dopo il confronto con la mappa di Blackwood City: la versione
precedente diceva "richly detailed" e descriveva gli edifici senza limitarne il
numero, e il modello produceva **piante urbane densissime**, migliaia di
edifici e griglia stradale completa, cioe' un linguaggio completamente diverso
da quello delle mappe esistenti. La densita' va vincolata, non suggerita.

```
Draw this as a stylized fantasy atlas DIAGRAM seen from directly above with a
very slight three-quarter tilt. The settlement is a single rounded organic shape
floating on empty dark ground and does not fill the frame. It is divided into a
handful of large districts, each a big flat translucent block of one colour with
soft irregular boundaries, separated by a few thick glowing arterial roads and
nothing else: there is no street grid, no block pattern and no minor street
network. Inside each district there are only six to fifteen individual
buildings, small hand-drawn line-art volumes in three-quarter view, tinted with
that district's colour and scattered with generous empty space around them; they
are representative samples, not a complete city, and most of each district's
area stays flat colour with nothing on it. A few notable places are marked with
a teardrop pin containing a small symbol. Leave clear empty space inside every
district for a name to be written later. Use a strict two-pole complementary palette and pull every element towards one
of the two poles, with nothing sitting halfway between them. The warm pole is
sunflower yellow: #FFE9A3 for highlights, #FFC614 for the full tone, #AB840D for
its deep shade. The cool pole is its exact complement: #6086FB for lit water,
#1245E2 for the full tone, #16275A for deep ocean, #0F1629 for the ground and
the night land. The two poles govern hue only: value stays free and is what
carries the terrain, so keep the ocean the darkest and most saturated blue, the
forest dark and shifted slightly towards green, the open land mid dark, the
valley the lightest of the cool areas, and rivers lighter than any land they
cross, with differences large enough to read at a glance. Everything inhabited and modern takes the warm pole: the road
network glows sunflower yellow against the dark ground, with thicker strokes for
highways and thin capillaries for local streets, and settlements and cultivated
land take warm translucent washes. Everything natural and nocturnal takes the
cool pole: ocean, land, forest, ridges and shadows. Do not use grey, do not use
teal, do not use coral or salmon, and introduce no colour outside these two
ramps. The overall mood is nocturnal supernatural noir cartography, crisp and
vector-like, A wide landscape image.
```

### Stile B, campus dipinto

Usato per il **SUCC Main Campus**. Illustrazione isometrica pittorica, non
cartografia.

**Blocco di stile Stile B:**

```
Draw this as a high-angle three-quarter isometric painterly illustration, the
kind used for a storybook game map. Architectural volumes are hand-painted with
soft directional shadows, rooftops are detailed, tree clusters are dense and
painted rather than drawn, footpaths and quads are clearly readable between the
buildings. Rich warm autumn palette, golden hour light, long soft shadows, high
detail. A landscape image slightly wider than tall.
```

---

## 3. Correzione alla mappa regionale: lo Yarrow River

Canon dal Lexicon, vincola il tracciato:

- **nasce nella Blackwood Forest**;
- scende fino a **Blackwood City**, dove alimenta **Dockside**, che e' traffico
  fluviale via chiatta e non un porto marittimo, perche' **Blackwood e'
  entroterra**;
- **attraversa Hex Valley** (decisione presa: la valle e' scavata dal fiume, e i
  vigneti delle famiglie vampiriche bevono da li');
- **sfocia in mare vicino a Solarton**, dove un **traghetto turistico** percorre
  l'ultimo tratto;
- il nome e' la storpiatura anglosassone del norreno **Yra**, "fiume del tasso",
  dato da Wulfnic intorno al 1022 quando risali' il fiume dalla costa fino alla
  radura dove pianto' il tasso della Bloodmoon Longhouse.

Senza il fiume, il traghetto Dockside-Solarton non ha senso geografico.

**Prompt (Stile A):**

```
A regional map of a stretch of coastal and inland California. Deep indigo ocean
along the western edge, dark plum landmass inland. A glowing sunflower-yellow highway
network links the settlements. Dark teal forest covers the mountainous north. A
tan upland valley sits in the centre of the map. One single navigable river
runs through the whole region: it rises from a spring high in the northern
forest, descends south to the walled inland city, continues south-west and cuts
directly through the middle of the upland valley, then widens into a river
mouth where it reaches the coastal town on the ocean. Long curving rows of
vineyard terraces sit on the valley slopes on both banks of the river, close
enough that the river clearly waters them. The river is desaturated blue-grey
with faint mist along its banks, and its final stretch before the sea is wide
enough for a small boat.
```
piu' il blocco di Stile A e la frase di chiusura del §1.

Sulla base finita vanno aggiunti in post l'icona del **traghetto** sul tratto
finale e lo spillo della **foce**, per coerenza con la mappa cittadina che il
traghetto ce l'ha gia'.

---

## 4. Mappe da fare, in ordine di utilita'

### 4.1 Solarton (Stile A), priorita' alta

La controparte solare di Blackwood, e il posto dove si gioca di piu'. Canon:
cittadina universitaria **costiera**, 35.621 abitanti, melting pot inclusivo,
brezza marina e vita studentesca, **Full Moon Market mensile** e **Solar
Festival**, il campus SUCC dentro di essa, la **foce dello Yarrow** e il
terminal del traghetto.

L'idea forte: stessa grammatica e stesso fondo di Blackwood, ma **molto piu'
caldo per quantita'**. Blackwood e' la notte, Solarton e' il giorno, e si vede al
primo colpo d'occhio da quanto giallo c'e'.

```
A map of a small coastal university town on the Pacific, drawn as a city-scale
zoom of the same atlas as the regional map, in the same drawing language. A
curving beach runs along the western edge, with the ocean beyond it. At one end
of the town a river reaches the sea through a wide mouth, with a small passenger
ferry pier beside it. A large university campus quarter with quads and sports
fields sits inland from the beach. The rest is low-rise seaside housing on a
relaxed grid, a wooden boardwalk along the shore, and an open market square near
the centre. Palm trees line the main avenues.

This town is the sunlit counterpart of the dark inland city, and that contrast
is carried by how much of it is warm, not by changing the background. Keep the
dark indigo ground and the deep ocean of the atlas, then make this town far
warmer than any other place on the map: a dense sunflower street network covering
the whole town, the beach strip rendered as the lightest warm tone on the map,
and warm translucent washes over the campus, the market square and the housing
districts, so the eye reads warmth and daylight from the sheer amount of yellow
rather than from a pale background.
```
piu' il blocco di Stile A e la frase di chiusura del §1.

**Vincoli di scala e di impianto, imparati al primo tentativo.** Il modello ha
disegnato un campus piu' grande della citta' e una decina di campi sportivi.
Vanno detti come numeri:

- **Solarton ha 35.621 abitanti e SUCC circa dodicimila studenti.** Il campus e'
  un distretto importante ma non e' la citta': **il tessuto urbano ordinario
  deve coprire dai quattro ai cinque volte l'area dell'intero campus**, fra
  griglie residenziali, downtown, fronte porto e piazza del mercato.
- **Gli stadi sono due, e sono diversi fra loro.** Il **Bulls Stadium** e' football
  americano, quindi campo rettangolare dentro un anello continuo di gradinate,
  a cielo aperto, con parcheggio accanto: e' il piu' grande e il piu' visibile.
  Il **St. Neptune Stadium** e' hockey su ghiaccio, piscine e spa, quindi e' un
  **edificio chiuso con il tetto**, non un campo: dall'alto si legge come
  architettura, non come impianto sportivo. Confonderli e' l'errore piu' facile.
- **Oltre a quei due, un solo gruppetto di due o tre campi da allenamento**, tutti
  insieme in un punto solo ai margini del campus. Nessun altro campo, campetto,
  pista o pitch da nessun'altra parte, ne' in campus ne' in citta'.
- Il campus si organizza **intorno ai quad**, cortili di edifici che chiudono
  prati, collegati da vialetti, con il **Griffin Clocktower** e la **Basilica
  Library** fra i blocchi e gli alloggi studenteschi su un lato. Deve leggersi
  come un quartiere pedonale denso, non come un centro sportivo con degli
  edifici attaccati.

**Decisione:** Solarton NON inverte il fondo. La versione precedente di questo
documento prevedeva uno sfondo chiaro di sabbia e crema per contrapporla alla
Blackwood notturna. Con la palette a due poli quella scelta spezzerebbe la
serie: le mappe del World devono leggersi come un unico atlante, e un fondo
chiaro le farebbe sembrare di due progetti diversi. Il contrasto giorno/notte si
ottiene con la **densita' del caldo**, non con il fondo. Se un giorno si volesse
davvero la versione diurna, andrebbe fatta per tutte le mappe insieme o per
nessuna.

---

### 4.2 Hex Valley (Stile A), priorita' alta

Canon dell'Environment: enclave vampirica ricca a venti minuti da Solarton,
**ward antiche che allungano il crepuscolo** al punto che la luce vera dura sei
ore in piena estate e praticamente zero d'inverno, **vigneti** delle famiglie
vampiriche, CUMS al centro, e **chi e' soggetto alla luna piena fatica a
viverci**.

L'elemento visivo che deve reggere tutta la mappa e' **il bordo delle ward**: un
perimetro dove la luce cambia di colpo. Su un modello ad aderenza va detto come
una regola, non come un'atmosfera.

```
A map of a small wealthy valley town held in permanent twilight. Terraced
vineyards in long curving rows cover both slopes of the valley. Grand estate
houses and wine cellars are scattered among the vines. A gothic university
campus stands at the centre of the valley floor. A river threads along the
valley floor and waters the vineyards.

The most important feature of this image is a visible circular boundary drawn
around the whole valley. Follow this rule strictly: outside that circle the
land is rendered in ordinary cold night colours, dark blue and grey; inside
that circle the land is rendered in a perpetual violet and amber dusk, warmer
and lighter than the outside. The change happens abruptly exactly at the line,
with no gradient across it. Along the line itself runs a faint luminous runic
shimmer, like a thin ring of pale light worked into the ground.

District fills inside the valley are deep purple, amber and wine red.
```
piu' il blocco di Stile A e la frase di chiusura del §1.

### 4.3 CUMS Main Campus (Stile B), priorita' alta

Va fatta **in coppia con la SUCC**, stesso stile e stessa inquadratura, cosi' le
due si leggono come rivali. Canon: ammette solo soprannaturali, corpo studentesco
in maggioranza vampirica, arti arcane, piu' formale e tradizionale di SUCC, sta
dentro Hex Valley.

Il contrasto: **SUCC e' autunno caldo, CUMS e' crepuscolo freddo.**

```
An old gothic arcane university campus in permanent twilight, seen from the
same high angle and the same three-quarter isometric viewpoint as a warm autumn
campus map, so the two read as a matched pair. Tall pointed spires and
buttressed stone halls, cloistered courtyards, an observatory dome on the
highest building, a walled ritual garden at the back. Black iron lanterns
burning with violet flame line every path. The trees are dark cypress and yew,
not autumn foliage.

Replace the warm autumn palette with a cold one: deep indigo, violet, slate and
tarnished silver, with small warm yellow window lights as the only warm notes.
Low blue dusk light, long cold shadows. The whole place should read as severe,
formal and much older than the town around it.
```
piu' il blocco di Stile B **sostituendo** la frase sulla palette autunnale, e la
frase di chiusura del §1.

### 4.4 Bloodmoon Pack Territory / The Dead Zone (Stile A, ma rotto apposta)

Canon: **la tecnologia non funziona** perche' la magia e' troppo densa, niente
luci artificiali, niente strade moderne, la **Longhouse norrena sotto il grande
tasso**, zero sorveglianza.

**L'idea:** la mappa deve *rompere* la grammatica delle altre. La rete stradale
girasole, che su ogni altra mappa e' ovunque, qui **si interrompe al confine e non
entra**. Dentro non ci sono campiture di distretto, non c'e' una sola luce
artificiale, e il disegno stesso cambia mano: invece che tratto vettoriale
pulito, inchiostro su pelle. E' il World che ti dice che li' la modernita' non
arriva.

Questa e' la mappa che guadagna di piu' dal modello scelto, perche' e' tutta
costruita su un divieto e i modelli a tag i divieti non li rispettano.

```
A map of a dense ancient mountain forest, divided by one clear boundary: the
tree line.

Outside the tree line, at the edges of the image, draw modern cartography: a
glowing sunflower-yellow highway network, small clean line-art buildings, flat coloured
district washes. Follow this rule strictly: every road stops dead at the tree
line and none of them crosses it. No road, no power line, no building, no
artificial light and nothing modern of any kind appears anywhere inside the
forest.

Inside the tree line there are only narrow game trails, a river, and one single
structure: an enormous ancient yew tree with a long norse timber hall standing
beneath its canopy.

Change the drawing technique at the boundary as well. Outside it is clean crisp
vector-like cartography. Inside it is hand-inked lines drawn on dark tanned
hide, with visible ink and charcoal texture and no grid and no icons. The only
light inside is a faint red-tinged moonlight.
```
piu' la frase di chiusura del §1. **Il blocco di Stile A qui non va messo per
intero**, perche' descrive proprio le cose che dentro il confine non devono
esserci.

### 4.5 Blackwood Forest (Stile A), la macro-regione contenitore

E' il livello sopra Blackwood City e Bloodmoon Territory, e serve soprattutto a
mostrare **dove nasce lo Yarrow** e come le tre aree stanno una dentro l'altra.

```
A map of an ancient mountainous forest region covered in dense dark teal
conifer forest, with ridgelines and rocky outcrops. A river rises from a spring
high in the northern hills and descends through the whole region, leaving the
map at the southern edge. A walled dark city occupies a cleared basin at the
southern edge of the forest, and the river runs through it. The north-eastern
quadrant is an unlit roadless wilderness with no buildings at all. Thin sunflower-yellow
roads reach the city from the south but stop before the wilderness and never
enter it.
```
piu' il blocco di Stile A e la frase di chiusura del §1.

### 4.6 Los Angeles (Stile A), dominio Underworld

Stessa grammatica, **scala metropolitana**: griglia enorme, sprawl a perdita
d'occhio, il DDC Tower come unico segnaposto verticale, gia' presente sulla mappa
regionale. Nota di progetto §10: LA e' dominio Underworld, quindi la mappa va
disegnata sul loro materiale, non inventata qui. **Da fare solo dopo aver
recuperato le fonti Underworld.**

```
A map of an enormous sprawling coastal metropolis. A vast rectangular street
grid covers most of the image, dense and fine-grained, with a few very wide
sunflower-yellow freeways cutting across it diagonally and interchanges where they meet.
Low sprawl everywhere, one cluster of taller towers downtown, hills on the
northern edge breaking the grid, and the ocean along the south-west with a
harbour. One single black skyscraper stands taller than everything else and
reads as a landmark.
```
piu' il blocco di Stile A e la frase di chiusura del §1.

### 4.7 Bakersfield, Simi Valley, Ventura, corridoio 101

Sono comprimari. Consiglio di **non fare tre mappe separate** ma una sola
tavola del corridoio, con le tre localita' come nodi lungo la 101 e la 5. Rende
di piu' e costa un terzo.

```
A long horizontal corridor map showing three small towns strung along two
highways that meet near the coast. On the left an inland agricultural town on a
flat plain of field patterns. In the middle a suburban valley town between low
brown hills. On the right a coastal town on the ocean. The two sunflower-yellow highways
are the spine of the image and everything else is arranged along them. Between
the towns there is mostly empty land: dry hills, farmland, the occasional
service stop.
```
piu' il blocco di Stile A e la frase di chiusura del §1.

### 4.8 Zone di Transito e Confine, non e' una mappa

Sono aree liminali e strade fra gli hub. Non ha una geografia propria: funziona
molto meglio come **overlay sulla mappa regionale**, cioe' i tratti di strada
gia' disegnati evidenziati in un colore diverso, con due o tre spilli di sosta.
Si fa in post, non si genera.

### 4.9 DDM Inc. // Voidspace, non e' una mappa

Non e' un posto della California e non ha una geografia. Forzarla in Stile A
sarebbe sbagliato. Funziona come **schema**, non come cartografia: i
dipartimenti della Company come blocchi collegati, il Dead Dog Motel come unico
punto di contatto con questo universo, le reality tears come strappi nel
supporto stesso del disegno.

---

## 5. Cose da tenere coerenti fra tutte le mappe

- **Le strade girasole sono la firma del World.** Dove ci sono, c'e' modernita' e
  sorveglianza. Dove si interrompono, non c'e'.
- **Blackwood e' fredda e notturna, Solarton e' calda e diurna, Hex Valley e'
  viola-ambra crepuscolare.** Le tre chiavi cromatiche vanno tenute distinte,
  perche' e' cosi' che si capisce dove si e' senza leggere una riga.
- Le icone a spillo con simbolo (casa, ospedale, libro, traghetto, quadrifoglio)
  sono gia' uno standard: vanno riusate identiche in post, non ridisegnate.
- **Lo Yarrow deve comparire su tutte le mappe che lo attraversano**: regionale,
  Blackwood City (gia' c'e'), Blackwood Forest, Hex Valley e Solarton alla foce.

---

## 6. Ordine di lavorazione consigliato

1. **Regionale corretta** con lo Yarrow, perche' fissa la geografia di tutte le
   altre e va guardata prima di disegnare i pezzi.
2. **Solarton**, il posto dove si gioca di piu'.
3. **Hex Valley**, che deve essere coerente col tracciato del fiume deciso al
   punto 1.
4. **CUMS**, subito dopo Hex Valley perche' ci sta dentro.
5. **Bloodmoon Territory**, la piu' rischiosa e la piu' interessante.
6. **Blackwood Forest**, che le contiene.
7. Los Angeles e il corridoio 101, quando servono davvero.

---

## 7. Lezioni dalla generazione, da applicare a tutti i prompt

Raccolte lavorando la regionale su Nano Banana 2. Sono errori del prompt, non
del modello, e si ripeterebbero identici su Solarton e Hex Valley.

**Mai scrivere "mist", "haze" o "fog" come dettaglio di un elemento.** Nel primo
tentativo `faint mist along its banks` e' stato preso come soggetto: al posto del
fiume e' comparso un banco di nebbia largo quanto una citta', senza sponde. La
nebbia sull'acqua, se la si vuole, va aggiunta in post. Nel blocco di Stile A la
frase "soft fog drifting over water" va quindi **tolta** quando nel soggetto c'e'
un corso d'acqua da disegnare.

**Mai scrivere "navigable".** Suggerisce una scala fluviale enorme. Il fiume va
dimensionato per confronto con qualcosa che gia' esiste nell'immagine: "largo
come le linee delle strade girasole, mai piu' largo della citta'".

**Mai scrivere "long curving rows" per i vigneti.** Diventano anelli
concentrici, cioe' curve di livello. La formulazione che funziona e' "small
elongated rectangular field patches arranged in neat parallel strips", con il
divieto esplicito di cerchi, pattern radiali e isoipse.

**Mai scrivere "walled city".** Ha prodotto un esagono bastionato in stile
fortezza medievale. **Blackwood City e' una citta' coloniale seicentesca
cresciuta fino a diventare moderna, non ha mura e non le ha mai avute.** Va
descritta come "an open street grid with no defensive perimeter", con il divieto
esplicito di bastioni, cinte, porte e cittadelle. Vale per ogni mappa in cui
compare.

**Ogni elemento lineare va chiesto "continuo".** La prima resa aveva il fiume
spezzato in due tronconi scollegati. Serve "one single continuous unbroken line
from its spring to the sea, with clearly defined banks along its whole length".

**Le strade vanno protette esplicitamente.** Senza istruzione, il nuovo elemento
ci passa sopra e le interrompe. Serve "the existing roads must remain fully
visible and unbroken; where a road meets the river it passes over it on a small
bridge".

### Strategia di iterazione

- Se il risultato e' **sbagliato in modo strutturale**, non correggerlo:
  ripartire **dall'immagine originale** dicendo esplicitamente di scartare
  l'ultimo output. I difetti grossi non si tolgono per sottrazione, si
  ereditano.
- Se il risultato e' **giusto tranne un dettaglio**, iterare **sull'ultimo
  output** chiedendo una sola modifica e ripetendo che tutto il resto non deve
  cambiare.
- Se lo stesso elemento va storto **due volte di fila**, la terza va storta
  uguale: si genera quell'elemento separatamente e lo si compone in post.

---

## 8. Palette: SvartulfrVerse Urban

Le mappe usano la **palette del template visivo 06 URBAN FANTASY**, la stessa
dei ritratti Urban, non una palette cartografica separata. E' una scelta
azzeccata e va tenuta: e' quello che fa leggere mappe e personaggi come un unico
mondo.

Ancore dichiarate dal template:

- **Catppuccin Yellow**, il sole vibrante
- **Catppuccin Blue**, oceano e denim

La mappa regionale esistente e' gia' sostanzialmente Catppuccin: il fondo prugna
scuro sta nella famiglia di Base e Mantle, le strade girasole in quella di Peach,
l'oceano in quella di Blue. Quindi **non va convertita, va rispettata**.

**Regola operativa:** ogni elemento aggiunto a una mappa esistente deve prendere
il colore da quelli gia' presenti nell'immagine, non da una descrizione
autonoma. Nel prompt conviene sia nominare la famiglia ("lo stesso blu denim
dell'oceano") sia dare il codice, perche' i modelli ad aderenza li usano
entrambi, e va aggiunto il divieto esplicito di introdurre colori che nella
mappa non ci sono.

Applicato allo Yarrow: il fiume e' **blu periwinkle intorno a #89b4fa**,
schiarito quel tanto che serve per staccare dalla terra scura, e piu' profondo
verso la foce dove si avvicina al tono dell'oceano. **Non grigio**, che era
l'errore dei prompt precedenti: il grigio non e' in questa palette.

---

## 9. Altre due lezioni

**Nominare le parti di un elemento ne cambia la scala.** Scrivere "citta' fatta
di piccoli edifici line-art" su una mappa regionale ha prodotto una citta' larga
cinquanta chilometri, disegnata edificio per edificio. La formulazione sicura
non e' descrivere l'elemento da zero ma **agganciarlo a qualcosa di gia'
presente nell'immagine**: "come gli altri insediamenti di questa mappa". Vale
per la scala come per il colore.

**Quando si edita una mappa gia' etichettata, la regola sul testo si
capovolge.** I prompt di generazione vietano il testo perche' le etichette si
mettono dopo. I prompt di modifica di una mappa finita devono invece **ordinare
di conservare ogni etichetta identica**, posizione, font, corpo e colore, scudi
autostradali e icone a spillo compresi, e vietare l'aggiunta di testo nuovo.

**Corollario onesto:** i modelli di immagini degradano il testo ogni volta che
rigenerano, anche con l'istruzione esplicita. Per una modifica che consiste in
**un solo elemento lineare** su una mappa gia' etichettata, disegnarlo a mano in
post e' piu' veloce, da' il controllo esatto del tracciato e ha **rischio zero
sulle etichette**. Se il primo tentativo sporca anche una sola scritta, si
chiude li' e si passa al post.

---

## 10. Grading complementare: girasole e il suo opposto

Direzione richiesta: l'effetto **teal and orange** del cinema, ma ruotato
sull'asse **giallo girasole / suo complementare**.

**Funziona, e non e' una deviazione dalla palette Urban: e' la sua descrizione
esatta.** Catppuccin Yellow sta a 41 gradi di tinta e Catppuccin Blue a 217:
sono 176 gradi di distanza, cioe' gia' una coppia complementare. Il template 06
URBAN FANTASY, dichiarando "Yellow, sole vibrante" e "Blue, oceano e denim",
stava gia' descrivendo un teal-and-orange spostato di un quadrante. Quindi
questa non e' una palette nuova da imporre, e' quella che c'e' gia', portata
alle sue conseguenze.

**Asse:** girasole `#FFC512`, tinta 45. Complementare esatto, tinta 225.

### Le due rampe

**Polo caldo (girasole, tinta 45)**

| Ruolo | Colore |
|---|---|
| Luce alta, sole | `#FFE9A3` |
| Girasole pieno | `#FFC614` |
| Ambra profonda | `#AB840D` |

**Polo freddo (complementare, tinta 225)**

| Ruolo | Colore |
|---|---|
| Blu chiaro, acqua illuminata | `#6086FB` |
| Indaco pieno | `#1245E2` |
| Indaco profondo, oceano | `#16275A` |
| Ombra di fondo, terra notturna | `#0F1629` |

### Come si distribuiscono

La grammatica del teal-and-orange e' che **ogni cosa viene tirata verso uno dei
due poli**, senza colori a meta' strada. Sulla mappa la divisione naturale e'
gia' scritta nel contenuto:

- **Polo caldo:** tutto cio' che e' abitato e moderno. Strade, autostrade, scudi
  autostradali, insediamenti, icone a spillo, etichette, la valle coltivata.
- **Polo freddo:** tutto cio' che e' naturale e notturno. Oceano, terra, foresta,
  rilievi, ombre.

**Decisione presa: il girasole e' il colore signature del World.** Il corallo e'
ritirato, non e' piu' un'opzione, e la variante morbida che lo conservava e'
scartata. La regola di §5 resta identica nella sostanza e cambia colore: dove
c'e' la rete gialla c'e' modernita' e sorveglianza, dove si interrompe non c'e'.
Ogni prompt e ogni mappa futura usa il girasole; il corallo va trattato come un
colore fuori palette al pari del grigio e del teal.

### Come si applica, che non e' come si genera

- **Sulle mappe gia' finite ed etichettate**, il grading e' una
  **post-produzione**: curve o gradient map in un editor. E' l'operazione per cui
  il post esiste, e' reversibile, e non tocca le etichette. Rigenerare l'intera
  mappa per cambiarle il colore significa rimettere in gioco ogni scritta, ogni
  scudo e ogni spillo per un risultato che si ottiene meglio in cinque minuti.
- **Sulle mappe ancora da generare** (Solarton, Hex Valley, CUMS, Bloodmoon,
  Blackwood Forest), va invece scritto nel prompt fin dall'inizio, sostituendo
  nel blocco di Stile A la frase sulla palette con i due poli qui sopra.
- **Un'operazione per volta.** Aggiungere lo Yarrow e ribilanciare i colori nello
  stesso passaggio e' il modo piu' rapido per non capire quale delle due cose ha
  rotto l'altra. Prima il fiume, poi il grading.

### Correzione al grading: i due poli governano la tinta, non il valore

Primo test reale del girasole sulla mappa regionale. La ricolorazione ha
funzionato, il giallo su indaco stacca molto piu' del corallo su prugna, e le
etichette sono sopravvissute alla rigenerazione. Ma **la regola "ogni cosa
tirata verso uno dei due poli, niente a meta' strada" e' stata applicata anche
al valore**, e il risultato e' che oceano, terra, foresta e valle sono diventati
quasi lo stesso blu: la mappa ha perso la distinzione dei terreni e non si capiva
piu' dov'era la foresta senza leggere l'etichetta.

**Regola corretta: i due poli governano la TINTA. Il VALORE resta libero, ed e'
il valore che porta l'informazione geografica.** E' anche il modo in cui
funziona il teal-and-orange al cinema, che non e' due colori piatti ma due
famiglie con l'intera gamma di luminosita'.

Scala di valore dentro la famiglia fredda, dal piu' scuro al piu' chiaro:

| Area | Valore |
|---|---|
| Oceano | il piu' scuro e il piu' saturo, cosi' la costa e' un bordo netto |
| Foresta | scura, con una leggera virata al verde, cosi' si riconosce senza etichetta |
| Terra aperta | medio scuro |
| Valle | il piu' chiaro delle aree fredde, si legge come conca aperta |
| Fiume e acque interne | chiaro e luminoso, piu' chiaro di qualunque terra attraversi |

Gli scarti fra un livello e l'altro devono essere **visibili a colpo d'occhio**,
non sfumature. Questa scala va aggiunta al blocco di Stile A di ogni mappa
futura, altrimenti l'errore si ripete identico.

**Nota sul fiume:** dargli il colore "della rampa fredda" non basta, perche' lo
fa sparire dentro la terra che e' della stessa famiglia. Va chiesto
esplicitamente **piu' chiaro di ogni area che attraversa**. E la sorgente va
chiesta **dentro** la foresta: senza quella precisazione il fiume e' entrato dal
bordo superiore dell'immagine, leggendosi come una strada o un confine.

### Il budget di rigenerazioni, e quando fermarsi

Dato dal ciclo reale sulla mappa regionale, sei rigenerazioni in sequenza.

- Le **etichette hanno retto fino alla quinta**. Alla sesta e' comparso il primo
  danno: il sottotitolo della SUCC, "Supernatural University of Central
  California", e' diventato "Supernatural University at Contral California".
  Nessun altro elemento e' peggiorato, ma il degrado del testo **non torna
  indietro** e da li' in poi peggiora a ogni giro.
- La **sorgente del fiume dentro il bosco e' stata chiesta tre volte e non e'
  mai stata eseguita.** Il fiume ha continuato a entrare dal bordo superiore
  dell'immagine. Conferma la regola: se un elemento sbaglia due volte di fila,
  la terza sbaglia uguale, e la quarta richiesta e' tempo buttato piu' un giro
  di degrado gratis.

**Regola pratica:** su una mappa gia' etichettata si ha un budget di **quattro o
cinque rigenerazioni**, non di piu'. Vanno spese sulle cose che il modello sa
fare, cioe' colore, valore, aree, reti stradali. Le linee singole e le
correzioni chirurgiche non valgono un giro: costano quanto un ritocco di due
minuti in un editor e mettono a rischio la tipografia, che e' la parte
insostituibile.

**Corollario operativo:** salvare ogni versione intermedia. La sesta e' la
migliore per contenuto ma ha il sottotitolo rotto, la quinta ha il sottotitolo
giusto: la versione finale si ottiene componendo, non rigenerando.
---

## 11. La lezione piu' importante: il livello di astrazione

Emersa confrontando le rese di Solarton con la mappa di **Blackwood City**, che
fino a quel momento non avevo esaminato.

**Le mappe del World sono diagrammi, non piante urbane.** Blackwood City e' fatta
di sette-otto **distretti a campitura piatta** (Seven Hills, Uptown, Paradise,
Bluemoon, Oldtown, Dockside, Ironworks, Arcadia), ognuno di un colore diverso,
separati da **poche arterie spesse**, con dentro **una manciata di edifici
rappresentativi** e molto vuoto intorno, piu' qualche spillo per i luoghi
notevoli. Non c'e' una griglia stradale. Non c'e' il tessuto degli isolati. La
citta' e' una **sagoma organica arrotondata su fondo scuro vuoto** e non riempie
il fotogramma.

Le rese di Solarton erano invece piante urbane letterali: griglia completa,
migliaia di edifici minuscoli, nessuna zonizzazione a colore, nessuno spazio
vuoto. Graficamente non brutte, ma **di un altro atlante**.

**Causa: il mio blocco di Stile A.** Diceva "richly detailed" e descriveva gli
edifici senza mai dire quanti. Un modello che legge "atlante dettagliato" e non
ha un tetto alla densita' disegna tutto.

**Regole che ne seguono, da mettere in ogni prompt di mappa cittadina:**

1. Dichiarare esplicitamente che **e' un diagramma e non una pianta**.
2. **Vietare la griglia stradale**: solo arterie spesse fra i distretti, nessuna
   strada minore.
3. **Dare il numero degli edifici**: sei-quindici per distretto, con vuoto
   intorno, dichiarati come campioni rappresentativi.
4. Dire che **la maggior parte dell'area di ogni distretto resta campitura
   piatta senza niente sopra**.
5. Chiedere la **sagoma organica su fondo vuoto**, non un'immagine al vivo.
6. Riservare **spazio vuoto dentro ogni distretto** per il nome, che si aggiunge
   in post.

**E il riferimento di stile da allegare non e' la mappa regionale ma quella di
Blackwood City**, perche' e' la mappa cittadina alla scala giusta. La regionale
serve solo come riferimento per altre mappe regionali.

### Dato di lore raccolto dalla mappa di Blackwood

**Eidolon Creative ha sede a Blackwood, nel distretto Paradise** (moda e
intrattenimento), dove la mappa la segna con uno spillo. Quindi la boutique di
Angelo Moreno a Solarton non e' la sede: e' un **avamposto**, il che rende ancora
piu' deliberata la scelta di aprirla in una citta' a scarsita' vampirica.


---

## 12. Il viola non se ne andava perche' glielo dicevo io

Errore di vocabolario, costato tre rigenerazioni su Blackwood.

Il complementare esatto del girasole cade a tinta 225, che a rigore e' un
**blu-violetto**. Nei prompt lo avevo chiamato cosi', "a blue-violet family", e
avevo assegnato al distretto della vita notturna un "dusty violet". Risultato:
il modello teneva viola, prugna, malva e lilla in mezza mappa, e ogni giro glielo
riautorizzavo con le mie stesse parole mentre gli chiedevo di toglierlo.

**Regola: nei prompt questa palette si chiama GIALLO E BLU, e basta.** Le parole
violet, purple, mauve, lilac non vanno mai scritte, nemmeno per descrivere il
polo freddo, nemmeno come sfumatura di un singolo distretto. I codici esadecimali
restano gli stessi, cambia solo come li si nomina.

**Formulazione che funziona:** dichiarare due sole famiglie ammesse, dare i sei
codici, e poi scrivere il filtro come test binario: *se un pixel non e' giallo,
non e' blu e non e' il verde-blu scuro del bosco, e' sbagliato*. Seguito
dall'elenco esplicito dei colori vietati, viola e malva compresi.

**Corollario sui distretti:** con un solo blu e un solo giallo, otto distretti si
distinguono per **valore**, non per tinta. Sei blu a profondita' diverse e due
gialli.

**E un caso in cui il vincolo ha migliorato il risultato:** il distretto della
vita notturna si chiama **Bluemoon**. Da viola era un colore qualunque; da **blu
piu' brillante e saturo della mappa** e' il suo nome scritto in colore. Il
vincolo di palette ha trovato la soluzione giusta al posto mio.

---

## 13. Mappa del campus SUCC: specifica

Riferimento di genere scelto dall'utente: le **mappe di orientamento
universitarie** tipo UCLA, quelle che si danno alle matricole. Non l'isometrica
pittorica dello Stile B, che va in pensione.

**Cosa si prende da quel genere:** la **completezza**. Quelle mappe non
inquadrano solo il nucleo accademico, mostrano tutta la proprieta', parcheggi
periferici, residenze e impianti sportivi compresi, con le strade intorno
disegnate e nominate, un riquadro di legenda in un angolo e una rosa dei venti.

**Errore da non rifare:** la prima versione era **tagliata sul nucleo** e
lasciava fuori Bulls Stadium, Sports Fields, Parking Lot B, Main Parking Lot e
Additional Student Housing, che sulla vecchia mappa esistevano solo come frecce
con una lista. Vanno **tutti dentro il fotogramma**. Fuori campo escono solo le
strade.

**Impianto complessivo:**

- **nucleo accademico** al centro, con la pianta della vecchia mappa;
- a **nord-ovest** Main Parking Lot e Additional Student Housing, e da li' la
  strada che se ne va verso Solarton;
- a **sud-est** Parking Lot B, i campi d'allenamento come rettangoli d'erba
  lisci, e il **Bulls Stadium**;
- **strada perimetrale** che gira intorno a tutta la proprieta'.

**Colore come informazione, non come decorazione:** codifica per funzione.
Didattica in sabbia e ambra (famiglia gialla), residenze, sport, servizi e
amministrazione in blu a profondita' diverse. Il **Griffin Clocktower** e' il
giallo piu' chiaro della mappa, cosi' l'occhio ci va per primo. Vialetti come
ragnatela gialla sottile e pallida, strade carrabili in giallo pieno.

**Procedura in due passaggi, per il testo.** Qui la base pulita possiamo
costruircela, a differenza di Blackwood:

1. **primo passaggio**: base senza una parola, con spazio vuoto accanto a ogni
   edificio, il riquadro di legenda vuoto e la rosa dei venti;
2. **secondo passaggio**, su una base salvata e approvata: solo le etichette, con
   l'elenco autoritativo dei nomi.

Cosi' un fallimento tipografico costa un passaggio e non tutta la mappa.

**Da aggiungere nel passaggio etichette**, oltre ai nomi della vecchia mappa:
**TIT House** (Theta Iota Theta, la sorority di Alyssa, sulla Fraternity &
Sorority Row) e **Dragon's Shortcut** (il sentiero alberato dalla Row al Lunar
Quad). Sono i due punti del campus che un giocatore usa davvero, e sulla vecchia
mappa non c'erano.

---

## 14. Mappa del campus: decisione finale

Dopo due tentativi di generare da zero una mappa piatta in stile wayfinding, con
esiti scadenti sulla pianta, la strada scelta e' la stessa che ha funzionato su
Blackwood: **si ricolora la mappa esistente e la si allarga**, non se ne genera
una nuova.

**Perche' la generazione da zero non funzionava.** Chiedevo in un colpo solo una
**pianta precisa da venticinque edifici** e uno **stile nuovo**. Il modello non
regge le due cose insieme: teneva lo stile e inventava la pianta. Nella resa
generata gli edifici erano generici, mancavano torre e biblioteca col chiostro,
lo stadio aveva di nuovo la pista di atletica, comparivano due campi marcati, e
nella griglia il modello ha scritto lettere da solo sbagliando la sequenza
(A B B C D E E F G H) nonostante l'ordine di non scrivere niente.

**Regola generale:** quando esiste gia' un'immagine con la disposizione giusta,
**ricolorare batte rigenerare**. La pianta e le etichette sono la parte costosa;
il colore e' la parte facile.

**Cosa comprende la lavorazione, in un unico passaggio:**

1. **Allargamento dell'inquadratura.** La mappa attuale e' tagliata sul nucleo
   accademico e rimanda i luoghi esterni a due liste negli angoli. Vanno
   **disegnati**: a nord-ovest Main Parking Lot e Additional Student Housing, a
   sud-est Parking Lot B, i campi d'allenamento e il **Bulls Stadium**, piu' una
   strada perimetrale. Le due liste negli angoli si cancellano, resta solo una
   freccia verso **Solarton**.
2. **Ricolorazione su navy e oro**, i colori d'ateneo confermati dal portale
   ufficiale, con le stesse due rampe di tutto il World. Quattro edifici in oro
   come punti di riferimento: torre, biblioteca, arena coperta, stadio.
3. **Elenco autoritativo delle etichette** nel prompt, ventotto voci con le loro
   righe di dettaglio, piu' il blocco del titolo. E' la difesa che ha funzionato
   su Blackwood.

**Refuso corretto nel passaggio:** la mappa originale scrive "quadrapeds" per
Unicorn Hall. Il termine giusto e' **quadrupeds**.

**Riferimento di inquadratura:** la mappa "Explore UCLA", non per i colori ma per
come e' composta: tutta la proprieta' dentro un foglio, parcheggi e impianti
disegnati invece che citati, strade perimetrali, e piccole frecce ai bordi verso
cio' che sta fuori.
