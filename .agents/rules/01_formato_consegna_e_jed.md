# Regola 01 - Formato di Consegna e Standard JED+ v2.0

## 1. Formato di Consegna: Testo, Non JSON

**Default assoluto:** Fornire sempre testo pronto da incollare nei campi del form dell'interfaccia Wyvern (`description`, `personality`, `first_mes`, `mes_example`, `system_prompt`, `post_history_instructions`, lorebook/NPC entries, outfit, tagline, shared info, ecc.), **NON** file JSON completi.

Il JSON va generato **esclusivamente** se:
1. L'utente lo richiede esplicitamente; oppure
2. Serve come riferimento tecnico per verificare la coerenza tra più campi complessi (in tal caso, chiedere prima conferma se l'utente preferisce il file JSON o solo il riepilogo testuale).

*Nota di sincronizzazione:* Il file JSON scaricato dall'utente **dopo** il salvataggio su Wyvern rappresenta il backup di archivio, non un artefatto che l'assistente deve mantenere sincronizzato in parallelo.

### Eccezioni Operative
- **Scrittura diretta sul World via API:** Quando l'assistente scrive direttamente sul World tramite API (vedi Regola 11), il testo non passa dalla chat campo per campo. In questo caso si consegna il **riepilogo** puntuale di cosa è stato scritto e dove, corredato dal documento di riepilogo nel Project con i valori precedenti dei campi modificati (snapshot di sicurezza).
- **Lavoro in locale su SQLite (sospeso dal 22/09):** Vale solo se l'utente riattiva esplicitamente il lavoro sul database locale di Wyldfire (vedi Regola 12). Il testo non passa dalla chat campo per campo, ma si consegna il riepilogo in un documento del Project.

## 1.1 Criterio Vincolante di Completezza: Live Platform Parity (https://app.wyvern.chat/mine)

**REGOLA SUPREMA DI RILASCIO:** Il lavoro svolto su Character Card, Lorebook, Scenari, Personas, Location, Setting o Parametri **NON VIENE MAI CONSIDERATO COMPLETO** finché non è effettivamente aggiornato, scritto e verificato a livello di piattaforma su **https://app.wyvern.chat/mine**.

1. **Divieto di Falso Completamento Locale:** La semplice modifica, correzione o validazione di un file locale (`FINAL/*.json`, `ARCHIVIO/19_exports_wyvern_ottobre2026/exports/`, script in `scratch/`) **NON costituisce completamento**.
2. **Dichiarazione di Stato Obbligatoria:** Se una modifica è pronta in locale o fornita come testo in chat ma non è ancora stata applicata sulla piattaforma web live (via Web API o intervento confermato dell'utente), il task **DEVE essere categoricamente classificato e dichiarato come "INCOMPLETO (In attesa di aggiornamento su piattaforma Wyvern)"**.
3. **Chiusura del Task:** Un task può essere marcato come "COMPLETATO" esclusivamente quando:
   - È stata eseguita con successo la chiamata API di scrittura/aggiornamento su Wyvern (con risposta HTTP 200/204 confermata); OPPURE
   - L'utente ha confermato esplicitamente di aver incollato e salvato il testo nell'interfaccia web di Wyvern.

---

## 2. JED+ v2.0 Come Formato Standard Universale delle Schede

Tutte le Character Card, User Personas, World Characters e voci NPC dei Lorebook adottano lo standard **JED+ v2.0 (Attention-First & Retrieval-Optimized)**, documentato integralmente in [docs/references/JED_PLUS_V2_UNIVERSAL_SCHEMA.md](../../docs/references/JED_PLUS_V2_UNIVERSAL_SCHEMA.md), che fonde:
- La sintassi PList/SBF di **SopakcoSauce (`soup`)** (`valore(dettaglio, causa)`, `SORE_SPOT`, `COPING`, `TRIGGER_RESPONSES`) e i **31 Non-Human Character Templates** ([SOPAKCOSAUCE_NON_HUMAN_CHARACTER_TEMPLATES.md](../../knowledge/External_References/SOPAKCOSAUCE_NON_HUMAN_CHARACTER_TEMPLATES.md));
- L'**Entity-Scoping** e gli obiettivi attivi (`GOALS`, `LOVES`, `HATES`) in stile **StatuoTW (`statuotw`)**;
- I **Micro-Tells Somatici ("Show, Don't Tell")** e la **Trust & Pacing Ladder (*Strangers -> Acquaintances -> Inner Circle*)** in stile **Iorveths / Veseii (`ioverse`), Nallak e bbcreature**.

### Topologia a U in 10 Slot Canonici Fissi (JED+ v2.0)

```text
[NAME: ...;
ALIASES: ...;
SPECIES: ...;
AGE: <età> (Born <Data esplicita>);
GENDER: ...;
HEIGHT: <cm> cm (<ft/in>);
BUILD: ...;
HAIR: ...;
EYES: ...;
ANATOMY: ...;
MARKS: ...;
SCENT: ...;
... <Chiavi Modulari Specie-Specifiche da SopakcoSauce 31> ...;
AFFILIATION: ...;
OCCUPATION: ...;
RESIDENCE: ...;
SOCIAL_STANDING: ...;
ARC_LEVEL: ...;
KNOWLEDGE_TIER: OPEN | HERMETIC_PACK | SECRET_FIRSTBORN | MINOR_LOCK]

KINSHIP & NON-KIN:
- PARENTS / SIBLINGS / GRANDPARENTS / EXTENDED: ...
- UNRELATED_HOMONYMS: ZERO kinship with ...
- POSSESSIVE_RULE (IT): ...

BACKSTORY: ...

RELATIONSHIPS & DYNAMICS: ... (include TRUST & PACING LADDER: Strangers / Acquaintances / Inner Circle)

POWERS, FORMS & GEAR: ... (opzionale se personaggio ordinario; mai vestiti fissi)

VOICE, TELLS & BEHAVIOR: ... (Vocal Register, Somatic Micro-Tells, Trigger Responses)

CORE PSYCHOLOGY [Sottotitolo Poetico Canonico]: ... (GOALS, SORE_SPOT, COPING, LOVES & HATES, FLAWS)

SEXUALITY & INTIMACY: ... (solo 18+, con 5 sotto-etichette fisse: Orientation & Role, Dynamics & Kinks, Anatomy & Physiology, Voice in Intimacy, Hard Limits & Aftermath; per minori <18 sostituire con AGE_POLICY: STRICTLY MINOR NPC)

GM SECRETS & EPISTEMIC BOUNDARIES: ...

RPG STATS & TRAITS:
[LEVEL: ...; ARC_LEVEL: ...; SPECIES: ...; OCCUPATION: ...; CLASS: ...]
[STATS: STR ..; PER ..; END ..; CHA ..; INT ..; AGI ..; LCK ..]
TRAITS:
- ...
```

### Regole Specifiche per i Campi
- **Blocco `[PList]` Multilinea (o Singola Riga Legacy durante la migrazione):** In **JED+ v2.0** il blocco iniziale `[...]` dispone **una chiave `UPPERCASE_KEY: valore;` per riga** per massimizzare la leggibilità umana e la scansione chiave-valore dell'LLM, combinando il **Core Universale (~16 chiavi)** con il **Modulo Specie-Specifico** dei 31 template SopakcoSauce (senza chiavi `N/A` inutili e senza `CLOTHING:` fisso). È tassativamente vietato annidare sezioni narrative lunghe (come `BACKSTORY:`) dentro le parentesi quadre `[...]`. Durante il rollout progressivo, il linter accetta sia il PList multilinea JED+ v2.0 sia il PList su singola riga legacy, purché ogni riga interna a `[...]` sia una coppia valida `CHIAVE: valore`.
- **Divieto di Header Duplicati nella Stessa Scheda:** Ogni intestazione di sezione (es. `VOICE & BEHAVIOR:` / `VOICE, TELLS & BEHAVIOR:`, `SEXUALITY & INTIMACY:`, `FAMILY & PACK:` / `RELATIONSHIPS & DYNAMICS:`) può comparire **una sola volta** per scheda.
- **Campo `personality` (`summary` nell'interfaccia Wyvern):** Usa un blocco compatto su **singola riga** tra parentesi quadre (`~450-650 caratteri`) in stile **SopakcoSauce SBF** (`TRAITS: trait(behavior, motive); FLAWS: flaw(manifestation, root);`), separato dalla `description` / `long_summary` estesa.
- **Budget Token a 3 Tier:**
  - **Tier 1 (Main Cast Cards & Personas):** `7.000 - 12.000 char` (`~1.750 - 3.000 tok`), tutti i 10 slot, 100% lossless sui fatti canonici.
  - **Tier 2 (World Characters & `NPC_Primary`):** `3.600 - 6.500 char` (`~900 - 1.600 tok`).
  - **Tier 3 (`NPC_Secondary`):** `1.800 - 3.200 char` (`~450 - 800 tok`), 6 slot essenziali (`[PList]`, `KINSHIP & NON-KIN`, `BACKSTORY`, `VOICE, TELLS & BEHAVIOR`, `CORE PSYCHOLOGY`, `RPG STATS & TRAITS`).
- **Età e Data di Nascita:** **Mai usare la macro `{{age}}`**. Indicare sempre `AGE: <età> (Born <Data>);`.
- **Parità `entries == lexicon`:** Nei file JSON locali dei Lorebook (`FINAL/` e `lorebooks/optimized/`), l'array `entries` e l'array `lexicon` devono essere mantenuti **100% identici byte-for-byte**.
- **Standardizzazione In-Chat Name (`chat_name`):** Tutte le Character Card (salvo esplicite omonimie) devono avere `chat_name` configurato con il solo nome proprio (`Firstname`), lasciando il nome completo in `name`.

### Invariante Outfits per Schede Giocabili vs User Personas
- **Character Cards Giocabili (`FINAL/*_card.json` e `/mine`):** Devono includere tassativamente **un minimo di 9 outfit contestuali completi**: `casual`, `campus / business`, `gala / formal`, `party / club`, `beach / terme`, `sleep`, `nude`, `hybrid shift / mutation`, `full shift / other`.
- **Outfit Nude Anatomico a 6 Sezioni:** Vietati placeholder brevi; deve seguire lo schema a 6 sezioni (Abbigliamento, Accessori, Scarpe, Gioielli, Trucco, Acconciatura).
- **User Personas (`FINAL/personas/*.json` e `/user-personas`):** Mantengono lo standard di **3 o più Appearances contestuali**.
