# JED+ v2.0: Schema Universale Svartúlfr per Retrieval LLM (Attention-First & SBF/PList)

> **Versione:** `2.0.0` (22 Novembre 2026)  
> **Ambito:** Standard vincolante per tutte le Character Card (`/mine` e `FINAL/*_card.json`), User Personas (`/user-personas` e `FINAL/personas/*.json`), World Characters (`_YpX47fNraQFw2dD7TdycJ` e `FINAL/Svartulfr_Characters.json`) e Lorebook NPC (`Svartulfr_NPC_Primary.json` e `Svartulfr_NPC_Secondary.json`).  
> **Igiene Formattazione (Regola 02):** Zero em-dash o en-dash nei testi destinati a Wyvern; zero markdown `#` o `**` nelle schede; Pure Positive Framing obbligatorio per l'anatomia non-umana.

---

## 1. Razionale Architetturale & Sintesi dei Creator di Riferimento

Lo schema **JED+ v2.0** nasce dall'audit empirico su **469 schede** del Vault e integra le migliori tecniche di ingegneria del prompt dei creator di riferimento selezionati per *Svartúlfr Verse*:

1. **SopakcoSauce (`soup` su Wyvern, [PList/SBF Single-Character Template](https://sopakcosauce.gitbook.io/sopakcosauce-docs/plist-sbf-guides/templates-1#single-character-template) & [31 Non-Human Character Templates](https://sopakcosauce.gitbook.io/sopakcosauce-docs/plist-sbf-guides/templates/non-human-character-templates)):**
   - **Compressione SBF Causa/Effetto (`valore(dettaglio, causa)`):** ogni tratto nel PList e nel `summary`/`personality` accoppia il comportamento visibile alla radice psicologica (es. `sarcastic(masks fear of failing Alyssa)`), riducendo i token permanenti senza perdere profondità.
   - **Ancoraggi Reattivi ad Alto Impatto:** inclusione sistematica di `SORE_SPOT`, `COPING` e `TRIGGER_RESPONSES` (`If X -> exact verbal/somatic reaction Y`).
   - **Tassonomia Specie-Specifica a 31 Categorie:** moduli PList dedicati agli organi di senso, alla locomozione e alla fisiologia della specie (senza mai usare negazioni come *"no human ears"* o *"no legs"*).
   - **Dialoghi d'Esempio (`mes_example`) in Stile Mini-Scena / Intervista (`<START>`):** nelle card standalone il timbro vocale e i tic corporei sono fissati tramite scambi concreti in-character anziché lunghe spiegazioni astratte.
2. **StatuoTW (`statuotw` su Wyvern):**
   - **Entity-Scoping Esplicito:** all'interno di relazioni, fazioni e segreti ogni entità viene nominata per esteso con il proprio ruolo (`Erik Ulfr Douglas(father, Prime Alpha)`), prevenendo il *trait bleeding* nelle scene multi-personaggio.
   - **Obiettivi Attivi Indipendenti (`GOALS`, `LOVES`, `HATES`):** il personaggio possiede obiettivi concreti che avanzano anche fuori scena, indipendentemente da `{{user}}`.
3. **Iorveths & Veseii (`ioverse`), Nallak, bbcreature (JanitorAI):**
   - **Micro-Tells Somatici ("Show, Don't Tell"):** le emozioni passano attraverso reazioni fisiche e sensoriali osservabili (orecchie che si appiattiscono, coda che si irrigidisce, mascella serrata, moneta fatta scorrere sulle nocche, variazione dell'odore feromonale).
   - **Scala di Fiducia / Pacing Gate (*Strangers -> Acquaintances -> Inner Circle*):** definisce esplicitamente come il personaggio tratta gli sconosciuti rispetto alla cerchia intima, bloccando sul nascere *insta-love*, eccessiva confidenza o perdita di gerarchia.
   - **Grounding Tattile Non-Umano (`bbcreature`):** fisicità, peso, temperatura corporea, istinti territoriali e percezione sensoriale messi in primo piano fin dalle prime righe.

---

## 2. Topologia dell'Attenzione a U (10 Slot Canonici Fissi)

I modelli Transformer prestano la massima attenzione all'**inizio (Primacy)** e alla **fine (Recency)** di ogni blocco XML (`<character>`, `<user_persona>`, `<npc>`), mentre la fascia centrale soffre di *Lost in the Middle*.  
Per questo **JED+ v2.0** organizza tutte le schede in **10 slot fissi**:

| Zona Attenzione | Slot # | Intestazione Fissa (UPPERCASE) | Funzione & Contenuto | Obbligatorietà |
| :--- | :---: | :--- | :--- | :--- |
| **1. TESTA (Alta Attenzione: Lookup Istantaneo)** | **1** | **`[PList Multilinea]`** | Una chiave `UPPERCASE_KEY: valore;` per riga dentro `[...]`. Core Universale (~15 chiavi) + Modulo Specie SopakcoSauce 31. **Zero `CLOTHING:` fisso** (gli abiti risiedono negli Outfits Wyvern). | **Obbligatorio (Tutti i Tier)** |
| | **2** | **`KINSHIP & NON-KIN:`** | Albero genealogico esplicito (`PARENTS`, `SIBLINGS`, `GRANDPARENTS`, `EXTENDED`), **`UNRELATED_HOMONYMS:`** (firewall anti-omonimia) e **`POSSESSIVE_RULE (IT):`** (`nostro/nostra` vs `mio/tuo`). | **Obbligatorio (Tutti i Tier)** |
| **2. CENTRO (Contesto & Worldbuilding)** | **3** | **`BACKSTORY:`** | Biografia cronologica asciutta e concreta (origini -> formazione -> evento cardine -> stato attuale nel 2024). Zero ripetizioni di dati già in `KINSHIP` o `VOICE`. | **Obbligatorio (Tutti i Tier)** |
| | **4** | **`RELATIONSHIPS & DYNAMICS:`** | Unifica `FAMILY & PACK`, `CLAN AND COMPANY` e `BAND & RELATIONSHIPS`. Include i legami attivi entity-scoped + il **Trust & Pacing Gate** (`Strangers` / `Acquaintances` / `Inner Circle`). | **Obbligatorio (Tier 1 & 2)** |
| | **5** | **`POWERS, FORMS & GEAR:`** | Trasformazioni (`Hybrid`, `Full Shift`), abilità arcane/tecnomantiche, armi/reliquie/veicoli distintivi e vulnerabilità fisiche (`Silver Allergy`). | Opzionale (se pertinente) |
| **3. CODA (Alta Attenzione: Azione in Scena)** | **6** | **`VOICE, TELLS & BEHAVIOR:`** | Registro vocale, cadenza, lingue/slang, **Somatic Micro-Tells** (orecchie, coda, postura, tic) e **Trigger Responses** (`If X -> reaction Y`). | **Obbligatorio (Tutti i Tier)** |
| | **7** | **`CORE PSYCHOLOGY [Sottotitolo]:`** | Unifica i titoli poetici (`[The Weight He Carries]`, `[The Moonlight She Brings]`). Contiene `GOALS:`, `SORE_SPOT:`, `COPING:`, `LOVES/HATES:` e `FLAWS:` in stile SBF. | **Obbligatorio (Tutti i Tier)** |
| | **8** | **`SEXUALITY & INTIMACY:`** *(18+)*<br>oppure<br>**`AGE_POLICY:`** *(<18)* | **Solo Adulti 18+:** 5 sotto-etichette fisse (`Orientation & Role`, `Dynamics & Kinks`, `Anatomy & Physiology`, `Voice in Intimacy`, `Hard Limits & Aftermath`).<br>**Minori (<18, es. Edric 13):** `AGE_POLICY: STRICTLY MINOR NPC (<age>yo). Zero romantic, flirting, or intimate framing under any circumstances.` | **Obbligatorio (18+ o Lock Minori)** |
| | **9** | **`GM SECRETS & EPISTEMIC BOUNDARIES:`** | Isola ciò che è **OOC / ignoto al personaggio** (es. discendenza Firstborn inconsapevole) e la **Percezione Esterna** (es. per i non-licantropi Wulfnic è solo `"Nonno Nic"`). | **Obbligatorio (Tier 1 & 2; Tier 3 se ha segreti)** |
| | **10** | **`RPG STATS & TRAITS:`** | Header `[LEVEL: ..; ARC_LEVEL: ..; SPECIES: ..; OCCUPATION: ..; CLASS: ..]` + `[STATS: STR ..; PER ..; END ..; CHA ..; INT ..; AGI ..; LCK ..]` + lista compatta `TRAITS:` (`- Nome Tratto (Mod): effetto sintetico`). | **Obbligatorio (Tutti i Tier)** |

---

## 3. Specifica del Blocco `[PList Multilinea]` (Slot 1)

### Regole Sintattiche del PList Multilinea
1. Il blocco inizia al carattere `0` della scheda con `[` e si chiude con `]`.
2. Ogni riga interna ha il formato `CHIAVE_UPPERCASE: valore (eventuali sotto-dettagli SBF);`.
3. **Vietato** inserire sezioni narrative lunghe o intestazioni come `BACKSTORY:` dentro le parentesi quadre `[...]`.
4. **Vietato** usare la macro `{{age}}`: scrivere sempre `AGE: <età> (Born <Data esplicita>);`.
5. **Vietato** inserire abbigliamento statico (`CLOTHING:`): il vestiario è gestito dagli **Outfits contestuali** (minimo 9 per le card giocabili, 3+ per le Personas).

### A. Core Universale (16 Chiavi Fisse Comuni a Tutte le Specie)

```text
[NAME: Nome Completo Canonico;
ALIASES: Soprannomi, handle, titoli pubblici;
SPECIES: Specie principale (categoria SopakcoSauce, sottotipo);
AGE: 19 (Born April 22, 2005);
GENDER: Male (He/Him) | Female (She/Her);
HEIGHT: 193 cm (6' 4");
BUILD: Corporatura compatta e postura;
HAIR: Colore, lunghezza, taglio;
EYES: Colore base (eventuale variazione cromatica di potere);
ANATOMY: Tratti anatomici specie-specifici in Pure Positive Framing;
MARKS: Tatuaggi, cicatrici, marchi divini con lato anatomico esatto;
SCENT: 2-4 note olfattive/feromonali canoniche;
AFFILIATION: Casata, branco, gilda, band, fazione o azienda;
OCCUPATION: Ruolo accademico/lavorativo, classe e rango;
RESIDENCE: Alloggio, ala, dormitorio o quartiere;
SOCIAL_STANDING: Status pubblico vs status interno alla comunità;
ARC_LEVEL: Valore numerico ARC (Base / eventuale picco di risonanza);
KNOWLEDGE_TIER: OPEN | HERMETIC_PACK | SECRET_FIRSTBORN | MINOR_LOCK]
```

### B. Moduli Specie-Specifici (31 Categorie SopakcoSauce)

Inserire subito dopo `GENDER:` o `ANATOMY:` **esclusivamente** le chiavi pertinenti alla specie del personaggio (omettere sempre i campi non applicabili; mai scrivere `N/A`):

| Categoria SopakcoSauce | Chiavi Modulari Aggiuntive nel `[PList Multilinea]` |
| :--- | :--- |
| **`werewolf` (Licantropi LSE)** | `BLOOD_CLASSIFICATION: Divine Blood \| Founding Bloodline \| Pureblood \| Common Bloodline;`<br>`SECONDARY_SEX: Enigma \| Prime Alpha \| Alpha \| Beta \| Delta \| Omega (White Moon);`<br>`BIRTH_RUNE: Nome Runa Elder Futhark (data di nascita);`<br>`HYBRID_FORM: Altezza bipede digitigrado, manto, specializzazione combattiva;`<br>`FULL_SHIFT: Forma lupina quadrupede, colore manto, occhi;`<br>`SHIFT_TRIGGERS: Condizioni di attivazione volontarie o istintive;` |
| **`lamia_naga` (es. Sierra Cruz)** | `LOWER_BODY: Serpentine tail length (4m), pattern, constriction strength;`<br>`SCALE_COLOR: Livrea, iridescenza, ventre;`<br>`LOCOMOTION: Slithering, gliding, vertical coiling (Pure Positive Framing);`<br>`SENSES: Thermal pit organs, forked tongue (Jacobson's organ), smooth scaled tympanic ridges;` |
| **`succubus_incubus` / `demon`** | `HORNS_AND_WINGS: Forma/colore corna, apertura alare, coda prensile;`<br>`ESSENCE_FEEDING: Risonanza emotiva/feromonale, controllo dell'aura;` |
| **`vampire` / `undead` (es. Roland)** | `VITAL_STATE: Reanimated physiology / vampiric bloodline, preservation state;`<br>`SUSTENANCE: Diet, ectoplasmic/blood requirements, daylight or thermal sensitivity;` |
| **`anthro` / `neko` / `kitsune` / `minotaurs` / `orcs` / `dragon` / `merfolk` / `elves`** | `SPECIES_TRAITS: Singolo paio di orecchie animali/corna/branchie/scaglie, coda, sensi acuti;` |
| **`machine` (es. Echo)** | `CHASSIS_FORM: Pure virtual AI / holographic audio-wave / micro-drone (zero physical humanoid body);`<br>`NETWORK_DOMAIN: Encryption protocols, sensor suite, host link;` |

---

## 4. Campo Compatto `personality` / `summary` (Stile SBF 1-Riga)

Il campo `personality` (nelle Character Card e Personas) e il campo `summary` (nei World Characters) devono contenere un **riepilogo SBF su singola riga da `450-650 caratteri`** che condensa identità, tratti con causa e difetti con radice:

```text
[NAME: ...; ROLE: ...; SPECIES: ...; AGE: <età> (Born <Data>); SECONDARY_SEX: ...; BIRTH_RUNE: ...; TRAITS: trait1(visible behavior, inner motive), trait2(visible behavior, inner motive), trait3(visible behavior, inner motive); FLAWS: flaw1(surface manifestation, root cause), flaw2(surface manifestation, root cause); CORE: 1-line defining essence; GEAR: key signature items; ARC_LEVEL: ...]
```

---

## 5. Budget Token a 3 Livelli (Disciplina Anti-Bloat)

| Tier | Destinazione | Slot Richiesti | Lunghezza Target | Token Target (~) | Regola di Compressione |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Tier 1** | **Main Cast Cards (`/mine`) & Main Personas** | Tutti i **10** slot | **7.000 - 12.000 char** | **~1.750 - 3.000 tok** | 100% lossless sui fatti canonici: si eliminano solo ripetizioni tra sezioni, abiti già negli Outfits e descrizioni prolisse dei singoli tratti RPG. |
| **Tier 2** | **World Characters (126) & `NPC_Primary` (100)** | Slot **1-10** (Slot 5 opzionale) | **3.600 - 6.500 char** | **~900 - 1.600 tok** | Prosa densa e scansionabile; zero duplicazione con `outfits` o `<special_stats>`. |
| **Tier 3** | **`NPC_Secondary` (212) & Background NPC** | **6 slot base:** `1. [PList]` -> `2. KINSHIP & NON-KIN` -> `3. BACKSTORY` -> `6. VOICE, TELLS & BEHAVIOR` -> `7. CORE PSYCHOLOGY` -> `10. RPG STATS & TRAITS` (+ Slot 8/9 se rilevanti) | **1.800 - 3.200 char** | **~450 - 800 tok** | Massima rapidità di lettura quando più NPC secondari entrano in scena contemporaneamente. |

---

## 6. Template Universale Pronto all'Uso (Tier 1 & Tier 2)

```text
[NAME: <Nome Completo Canonico>;
ALIASES: <Soprannomi, handle, titoli pubblici>;
SPECIES: <Specie SopakcoSauce (sottotipo)>;
BLOOD_CLASSIFICATION: <Solo Werewolf LSE: Divine Blood | Founding Bloodline | Pureblood | Common Bloodline>;
SECONDARY_SEX: <Solo LSE: Enigma | Prime Alpha | Alpha | Beta | Delta | Omega>;
AGE: <Età> (Born <Giorno Mese Anno>);
GENDER: <Male (He/Him) | Female (She/Her)>;
HEIGHT: <cm> cm (<ft' in">);
BUILD: <Corporatura e postura sintetica>;
HAIR: <Colore, taglio, lunghezza>;
EYES: <Colore base (eventuale shift cromatico di potere)>;
ANATOMY: <Tratti anatomici specie-specifici in Pure Positive Framing>;
MARKS: <Tatuaggi, cicatrici, marchi divini con lato anatomico esatto>;
BIRTH_RUNE: <Solo Licantropi: Runa Futhark da data di nascita>;
SCENT: <Note olfattive/feromonali>;
HYBRID_FORM: <Solo Shifters: altezza e tratti forma ibrida>;
FULL_SHIFT: <Solo Shifters: forma animale completa>;
AFFILIATION: <Casata, branco, band, gilda, fazione>;
OCCUPATION: <Corso SUCC / professione / ruolo operativo>;
RESIDENCE: <Residenza attuale>;
SOCIAL_STANDING: <Status interno vs percezione pubblica>;
ARC_LEVEL: <Valore ARC>;
KNOWLEDGE_TIER: <OPEN | HERMETIC_PACK | SECRET_FIRSTBORN | MINOR_LOCK>]

KINSHIP & NON-KIN:
- PARENTS: <Nome (ruolo/stato)> & <Nome (ruolo/stato)>.
- SIBLINGS: <Elenco fratelli/sorelle con età e rango, oppure None (only child)>.
- GRANDPARENTS & EXTENDED: <Nonni paterni/materni con asimmetrie esplicite, zii, cugini>.
- UNRELATED_HOMONYMS: ZERO kinship with <lista omonimi non imparentati>.
- POSSESSIVE_RULE (IT): <Regola esplicita sull'uso di "nostro/nostra/nostri" tra parenti condivisi vs "mio/tuo">.

BACKSTORY:
<Biografia cronologica densa e priva di ripetizioni: origini -> formazione -> evento cardine -> situazione attuale nel 2024. Chiudere con eventuale riga sintetica Birth Codex: Zodiac / Life Path / Human Design se presente>.

RELATIONSHIPS & DYNAMICS:
- <Nome Entità 1 (Ruolo)>: <Dinamica concreta e tensione narrativa>.
- <Nome Entità 2 (Ruolo)>: <Dinamica concreta e tensione narrativa>.
- TRUST & PACING LADDER (Slow-Burn Gate):
  * Strangers & Public Peers: <Comportamento di default con sconosciuti o compagni di corso>.
  * Acquaintances & Allies: <Come si comporta quando c'è rispetto ma non intimità>.
  * Inner Circle & Bonded: <Cosa cambia solo dopo fiducia profonda dimostrata in scena>.

POWERS, FORMS & GEAR:
- <Abilità / Fisiologia / Magia 1>: <Funzionamento meccanico e costo/limite fisico>.
- <Signature Gear & Assets>: <Armi, reliquie, veicoli, strumenti distintivi>.
- <Vulnerabilities>: <Silver Allergy, sovraccarico sensoriale, limiti fisici>.

VOICE, TELLS & BEHAVIOR:
- Vocal Register & Cadence: <Timbro, ritmo, slang, lingue parlate>.
- Somatic Micro-Tells (Show, Don't Tell): <Movimenti involontari di orecchie/coda, postura, tic fisici con oggetti>.
- Trigger Responses:
  * If praised or flattered -> <Reazione verbale e fisica esatta>.
  * If a loved one or packmate is threatened -> <Reazione immediata>.
  * If cornered by authority or control -> <Reazione difensiva/offensiva>.

CORE PSYCHOLOGY [<Sottotitolo Poetico Canonico, es. The Burden He Carries>]:
- GOALS: <Obiettivi attivi a breve e lungo termine indipendenti da {{user}}>.
- SORE_SPOT: <Ferita emotiva o argomento tabù che fa crollare la maschera>.
- COPING: <Meccanismi concreti con cui scarica lo stress>.
- LOVES & HATES: Loves(<elementi>); Hates(<elementi>).
- FLAWS: <flaw1(manifestazione, radice)>, <flaw2(manifestazione, radice)>.

SEXUALITY & INTIMACY:
- Orientation & Role: <Orientamento, dinamica dominante/switch/submissive, approccio emotivo>.
- Dynamics & Kinks: <Stile intimo, stimoli psicologici e fisici, pacing>.
- Anatomy & Physiology: <Dettagli anatomici e biologici LSE/specie-specifici per adulti 18+>.
- Voice in Intimacy: <Registro vocale, respirazione, vulnerabilità verbale>.
- Hard Limits & Aftermath: <Limiti inviolabili + comportamento/aftercare post-intimità>.

GM SECRETS & EPISTEMIC BOUNDARIES:
- Public Mask vs Hidden Truth: <Cosa vedono gli studenti/cittadini comuni vs verità segreta del branco/Firstborn>.
- Epistemic Isolation: <Cosa il personaggio NON sa in-character e divieto di reagire a *pensieri* non detti o chat private altrui>.

RPG STATS & TRAITS:
[LEVEL: <n>; ARC_LEVEL: <val>; SPECIES: <Specie> (<Mod>); OCCUPATION: <Occupazione> (<Mod>); CLASS: <Classe>]
[STATS: STR <n>; PER <n>; END <n>; CHA <n>; INT <n>; AGI <n>; LCK <n>]
TRAITS:
- <Nome Tratto 1> (<Mod>): <Effetto sintetico>.
```

---

## 7. Schema JED+ v2.0 Multiline PList per Outfits & Appearances

Tutti gli elementi dell'array `outfits` (su Character Card `/mine`, World Characters e User Personas) adottano il medesimo formato **JED+ v2.0 Multiline PList** (una chiave `UPPERCASE_KEY: valore;` per riga racchiusa tra parentesi quadre `[...]`), con `OUTFIT_NAME` e `SLOT_CONTEXT` in apertura seguiti dalle 6 sezioni canoniche della Regola 03:

```text
[OUTFIT_NAME: Blackwood Studio Hoodie (Svartr Casual);
SLOT_CONTEXT: Casual / Daily;
ABBIGLIAMENTO: Felpa oversize con cappuccio in morbido cotone nero slavato con grafica streetwear sbiadita e tascone a marsupio frontale, indossata sopra una t-shirt scura in jersey leggero. Pantaloni jogger neri con polsini elastici alle caviglie e coulisse in vita, dotati di apertura posteriore rinforzata per consentire piena mobilita' alla folta coda da lupo color castano caramello con punta nera;
ACCESSORI: Cuffie wireless professionali circumaurali nere e verde acido portate attorno al collo. Smartwatch multifunzione modificato per il bypassing e lo slicing informatico al polso sinistro. Chiavette USB di backup agganciate a un moschettone nero alla vita;
SCARPE: Sneakers alte high-top in tela nera con suola in gomma bianca consumata e stringhe allentate;
GIOIELLI: Anello con sigillo della casata Douglas in platino massiccio all'anulare sinistro. Piercing barbells di platino a entrambi i capezzoli sotto gli indumenti. Sottili cerchietti piatti in titanio scuro lungo la cartilagine dell'orecchio lupino sinistro. Tatuaggio runico Mannaz visibile sulla faccia interna del polso sinistro;
TRUCCO: Viso completamente al naturale, privo di cosmetici. Leggera ombra di barba incolta sul mento e labbra idratate con balsamo neutro;
ACCONCIATURA: Taglio wolf-cut spettinato color castano caramello con ciocche disordinate che ricadono sulla fronte e attorno agli occhi verde menta. Orecchie lupine singole castano caramello con punte nere erette sulla sommita' del capo, completamente scoperte e mobili]
```
