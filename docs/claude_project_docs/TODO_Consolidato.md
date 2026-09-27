# TODO consolidato — Svartúlfr | Urban

Rilevato il **7 settembre 2026**, aggiornato lo stesso giorno dopo il round di
decisioni di canon (vedi `Decisioni_Canon_2026-09-07.md`). Raccoglie i todo
sparsi in dodici documenti del Project e li **riconcilia con lo stato reale del
World letto via API**, perché diversi conteggi nei doc vecchi erano superati.

Numeri di riferimento: **88 Character**, 149 Lexicon, 12 Environment, 79
Location, 2 Scenario.

---

## 0. Chiuso, da non riaprire

- **`{{user}}` è a zero** su tutte le schede, in ogni campo. Il todo sui quattro
  casi "Tipo B" è superato: Edric ha la riga `Strictly non-applicable, Edric is a
  minor and a background NPC`; Scarlett dice `With Alyssa she is a fiercely loyal
  wingwoman and nothing else`; Fade e Sullivan hanno la scheda ancora vuota.
- **Global Character = ON su tutte.** Vincent, Jared e Finn non sono più a OFF.
- **Macro `{{age}}`** estesa ai `summary` e tolta ogni età scritta a mano dai
  `display_description`.
- **Fondazione SUCC**: 1908 ufficiale, apertura agli umani 1992 come adattamento.
- **Rory's Estate**: Los Angeles, chiusa.
- **V.U.A.**: una sola organizzazione, sezione SUCC aperta dopo l'abolizione.
- **Regina e Madre dei Lupi**: stessa figura, Hvit e le sue White Moon.
- **Wulfnic nonno**: scritto, l'affetto resta.
- **La domanda ai tre**: resta sospesa per scelta, gli NPC non la sollevano.
- **L'orologio del sangue**: confermato per Alyssa, Jasper, Malachia e Noah.
- **Omega, Pack Mom, poliamore e monogamia**: scritti in tre entry LSE.

---

## 1. Blocchi grossi di lavoro sulle schede

Ordine per volume, non per priorità.

| Lavoro | Quante schede | Note |
|---|---|---|
| **Schede vuote da scrivere da zero** | **25** | Mackenzie e Luisa Sanchez Rogers, Allegra Lumsden, Viola Carter, Dominic Rogers, Fade Greymoor, Roland Vickers, Everett Rottmore, Damien Bishop, Cato, Vasile Ionescu, Alistair DeVille, Sullivan Jones, Daniel Boone, Harper Aries, Ruaraidh Ballantine, Alicia Virtuoso, **Elizabeth Duskwood**, e i **sette Peccati** |
| **Schede grezze da passare in pipeline §14** | **25** | Aris Thorne, Talia Grimwood, Javier Sinclair, Jake Thompson, Brittany Willow, Archer Wolfwood, Federico Savini, Isobel Blackwater, Eclipse, Dominic Chen, Cass Harrow, Aurora Night, Bianca Rossi, Vito Marino, Warg, Tomas Matthews, Chase Anderson, Angelo Moreno, Sierra Cruz, Scarlett Rose, Revazhael, Graham Purcell, Santiago Herrera, Andrew e **Vincent Campbell** |
| **Schede stub nuove da scrivere** | **2** | **Hideo Reid** e **Venera Dolce**, create il 7 settembre con le sole informazioni ufficiali e una riga che vieta al modello di improvvisarne il resto |
| **Dialogue Examples mancanti** | **70** | passo 8 della pipeline |
| **Start Position mancante** | **78** | vedi §3, c'è una contraddizione da sciogliere |
| **RPG Stats non abilitate** | **48** | |
| **Outfit assenti** | **47** | priorità: Bailey, Chase, Stanley Jr., Iordan, i sette Peccati, Rory. Anche **Ut e Zefir** non ne hanno |
| **Attitudes verso Alyssa e Jasper mancanti** | **50** | obbligatorie per §16, anche solo a Unknown Scent |
| **Birthdate mancante** | **42** | vedi §2 |
| **Em-dash residui** | **8 schede** | Santiago Herrera 4, Bailey Rogers 3, PRIDE 2, Elizabeth Duskwood 2, e una a testa Mackenzie, Fade, Roland, Magnus. Nel Lexicon sono a zero |

**Elizabeth Duskwood è il caso peggiore singolo:** `long_summary` vuoto, niente
birthdate, età scritta a mano (76), due em-dash. Vive solo di `summary` e cinque
outfit, ed è la moglie di Magnus e madre di Erik e Logan.

---

## 2. Età e macro

**Fatto.** `{{age}}` sta in `long_summary` su **40 schede** e in `summary` su
**13**. Nessun `display_description` contiene più un'età scritta a mano. La
conversione ha corretto sei numeri stantii (Wulfnic 1199→1196, Magnus 357→355,
Ut 1201→1200, Angelo 540→539, Noah 25→24, e Sierra e Scarlett che semplicemente
non avevano ancora compiuto gli anni).

**Da fare:**

- **8 schede hanno ancora l'età scritta a mano nel `summary`** perché manca la
  birthdate: Eris Davies, Jasmin Thompson, Stanley Davies Sr. e Jr., Hank
  Thompson, Janice e Jared Thompson, Elizabeth Duskwood.
- **42 schede senza birthdate.** Per le 15 già in checklist si usa il criterio
  del trittico zodiacale quando la fonte tace.
- **5 birthdate segnaposto al 1° gennaio**, contro la preferenza registrata:
  Tomas Matthews, Chase Anderson, Revazhael, Graham Purcell, Marcus Thornfield.
  **Marcus è confermato al 1985**, quindi 39 anni: resta solo da variare il
  giorno.
- **Macro di livello 2, non ancora usate.** `{{#beforeTimestamp}}` /
  `{{#afterTimestamp}}` sul timestamp del rush (26 agosto 2024) per la sezione
  KSA di Jasper e per lo status "senza confraternita" dei gemelli.

---

## 3. La contraddizione sulle Start Position (aperta)

Due regole in conflitto, entrambe scritte:

- La **convenzione vecchia**, verificata su Logan: Start ed End **vuote per i
  vivi**, si compilano solo per i deceduti.
- La **§7 riscritta**: i **vivi** hanno la sola **Start Position**; i deceduti
  Start e End.

Oggi solo **8 schede su 88** hanno una Start Position. Se vale la §7 c'è un
backlog di 78 schede; se vale la convenzione vecchia non c'è backlog.

---

## 4. Contenuti che mancano nel World

**Personaggi da creare:** Professor Allen Albarn, Ves, Maren, **Matilda
Williams** (deceduta, serve Start + End), Elio Warren, Dr. Henry Ross, **Sharky**
(basta un Lexicon), **Elice Campbell** (19 anni, capo della VUA). **Maria e
Leonard Campbell**: una entry per la coppia o due Character?

**Bulls, i tre rimandati:** Cris Hicks, Brad Grimsley, Ethan Primrose. Da vedere
insieme agli altri NPC mancanti. Non sono stati messi nemmeno come nomi dentro la
entry, per non dare al modello tre nomi da riempire a caso.

**Fratelli Thompson:** presenti Hank, Jasmin, Janice, Jared, Jake; mancano
Jaiden, Jason, Jeremy, Jet, Jerry, Julie. Verificare quale sia la lista giusta.

**Huin Douglas**: verificare se è parente Douglas o omonimia.

**Item.** Nessun item base: zaino, cuffie, blocco da disegno, laptop, borraccia,
tessera universitaria, chiavi della confraternita. Nessun Key Item firma: ascia
di Dullahan, macchina fotografica di Casey, fischietto di Barkley, sacca da
hockey di Finn. **Categoria Creature a zero**, servono almeno i gatti di
Dullahan. Inventario vuoto su ~20 NPC.

**Lexicon e sistema:** entry Job **"Douglas Family Allowance"** ($500/settimana);
lista di **Occupation RPG Blueprints** (oggi c'è solo "Student"); **secondo
Scenario "Character Creation"**.

**KSA House** non ha residenti oltre a Noah presidente: o si popola o si decide
che è chiusa.

**Mappe mancanti:** campus SUCC, Solarton, Hex Valley, Bloodmoon Territory. Sulla
mappa del campus c'è il refuso **"quadrapeds"**, che sta solo nell'immagine.

**Scheda di Mac:** non nomina Directions & Dragons né l'appartamento sopra la
libreria.

---

## 5. Pulizie

- **61 elementi UNCATEGORIZED** (51 Location + 10 Lexicon) da spostare a mano.
- **Doppioni:** "Ironworks" e "Bloodmoon Longhouse" compaiono due volte.
- **Lexicon "Archer Wolfwood Hall"**: probabile doppione della Location omonima.
- **4 entry Lexicon categoria SPECIES** da rimuovere o ricategorizzare.
- **Rinominare `Barkley_Rover_Card_v2_DA_APPLICARE.md`**, ormai fuorviante.

---

## 6. Decisioni ancora aperte

**Nuove, dal round del 7 settembre:**

- **Zefir**: l'harem condiviso della longhouse è storico per lui o attuale? La
  scheda lo dà asessuale al presente e non l'ho toccata.
- **13 aprile contro 1 maggio**: l'Admitted Student Days presuppone una lettera
  già in mano, la scadenza del 1° maggio è scritta come termine per formalizzare.
  Se intendevi la domanda iniziale, il 13 aprile va riscritto.
- **Le 20 entry Memory**: procedere col test per togliere Global alle diciannove
  agganciate? Vedi `Decisioni_Canon_2026-09-07.md` §12.

**Dal registro precedente:**

- **"L'Omega è del branco"** è risolto come regola, ma resta da decidere quanto i
  Bloodmoon la praticano **oggi** in concreto, e cosa vuol dire per le scene.
- **I sei Firstborn senza nome**, **Sköll e Sól**, **le compagne di Magnus prima
  di Elizabeth**, **il ramo ducale inglese**: filoni lasciati aperti apposta.
- **Character Pool contro §7**: un doc decide di popolare i pool per Environment,
  la §7 dice che è inutile. Oggi vale la §7 e i pool sono vuoti.

---

## 7. Istruzioni di progetto da aggiornare (le incolli tu)

| Sezione | Cosa cambia | Testo pronto in |
|---|---|---|
| **§6 World Clock** | ora 0 = **21 dicembre 827**, nascita di Wulfnic; start del World 5 aprile 2024 | `World_Clock_Eras_E_Start_Positions.md` |
| **§10 Precedenza di lore** | sostituita dalla **Golden Rule** | `Golden_Rule_Canon_Blackwood.md` |
| **§12 Invecchiamento** | i **Common** (60-80 anni, aspetto rallentato), il fermo immagine del **Divine Blood**, e l'età di Zefir a **1019** | `Longevita_Common_Bloodline.md` |
| **§13 punto 5** | distinguere `{{user}}` di **Tipo A** da **Tipo B** | `Audit_Schede_2026-09-03.md` |
| **§7 / Character Pool** | sciogliere la contraddizione sui pool e sulle Start Position dei vivi | questo doc, §3 |

---

## 8. Bug da segnalare a Wyvern

1. **Save appeso** su "Saving..." mentre il contenuto si salva davvero.
2. **Species e Occupation non persistono** dopo il reload.
3. **Livello RPG oltre ~100** fa fallire in silenzio l'intero blocco RPG.
4. **`linked-characters` restituisce 500** costantemente.
5. **`PUT /api/worlds/<world_id>` restituisce 500 "Maximum call stack size
   exceeded"** pur scrivendo correttamente.
6. **Disallineamento fra la tab Simulation e il date-picker.**

---

## 9. Lavoro in sospeso di questa sessione

- **Quattro thread Discord ancora da leggere**: il secondo canale
  Solarton/Underworld, i due canali DDM, e il canale general.
- **Ripresa del lavoro sugli NPC**, il filone rinviato più volte.
- **Roster NPC da 300+ nomi**: da affrontare a piccoli gruppi, deduplicando prima
  contro i Character già esistenti.
