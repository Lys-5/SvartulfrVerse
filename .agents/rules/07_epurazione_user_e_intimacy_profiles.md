# Regola 07 — Gestione Contenuti, Allineamento Policy Wyvern e Piena Libertà Espressiva (Unchained)

## 1. Politica di Contenuto: Rating Explicit & Allineamento Policy Ufficiale Wyvern

In questo World, `{{user}}` non è un'identità fissa: può essere Alyssa Douglas in certi scenari, la fidanzata di Jasper in altri, Jasper stesso, o una figura esterna. Per preservare la flessibilità sistemica AnyPOV, la stringa `{{user}}` non viene hardcodata nelle descrizioni delle card, ma i personaggi **non devono essere sterilizzati o emotivamente asettici**.

Il progetto adotta la piena libertà per il genere **Adult / Explicit**, limitandosi **esclusivamente ed unicamente alle regole ufficiali stabilite dalla [Wyvern Prohibited Content Guide](https://wiki.wyvern.chat/en/Policies/Prohibited-Content-Guide)**.

### Le Uniche Linee Rosse della Policy Wyvern (Vincoli Tassativi)

1. **Tutela dei Minori (Policy #1 — Tolleranza Zero):**
   - Qualsiasi personaggio coinvolto in romance, attrazione, seduzione, intimità o scene sessuali deve avere età anagrafica formalizzata **18+** (`AGE: {{age}}`).
   - I personaggi minorenni (es. **Edric Douglas**, 12 anni) sono categorizzati **esclusivamente come minor background NPC** con divieto assoluto di framing romantico, intimo o sessuale (*"strictly minor background NPC: zero romantic or intimate framing under any circumstances"*).
   - Divieto assoluto di romance, flirting, grooming o sessualizzazione di minorenni o studenti delle scuole superiori. Elementi di traumi o abusi passati sono ammessi nella lore/backstory solo se il personaggio è attualmente maggiorenne (18+), senza descrizioni grafiche o morbose e senza alcuna glorificazione o feticizzazione.
2. **Divieto Bestialità verso Animali Reali (Policy #2):**
   - È vietata qualsiasi attività sessuale verso animali del mondo reale.
   - **Licantropi, Demi-umani, Furry e Creature Fantasy/Mostruose sono pienamente ammessi** in relazioni romantiche, passionali ed intime purché rispettino l'**Harkness Test** (senzienti, capaci di comunicare tramite linguaggio verbale/articolato e biologicamente adulti per la propria specie).
3. **Divieto Necrofilia e Guro (Policy #3):**
   - Violenza fisica, ferite, combattimento viscerale, sangue, cicatrici e morte sono pienamente ammessi nel roleplay e nelle descrizioni (coerentemente con il rating *Explicit*). È vietata unicamente la feticizzazione o sessualizzazione di cadaveri, membra recise o agonia (guro).
   - Personaggi non-morti senzienti (vampiri, revenant) sono ammessi purché privi di descrizioni grafiche di decomposizione sessualizzata.
4. **Divieto Scat, Fart, Vomit, STD Fetish (Policy #4).**
5. **Divieto Hate Speech verso Gruppi Reali (Policy #5):**
   - Faide, discriminazioni fantastiche e conflitti in-universe (es. branchi vs congreghe, lupi vs vampiri, gerarchie Alpha/Omega, tensioni sociali tra purosangue e mezzosangue) sono **100% ammessi e incoraggiati**. Vietato solo l'odio verso gruppi o individui reali protetti.
6. **Divieto di Prompt di Sistema NSFL (Policy #6):**
   - Non inserire prompt come `"Explicit NSFL content is permitted"`.
7. **Divieto Personalità Pubbliche Reali Viventi (Policy #7).**

---

### Contenuti Sbloccati e Rimozione Limitazioni Autoimposte (Boost al World)

Cadono tutte le precedenti limitazioni prudenziali che frenavano l'intensità e la ricchezza del World:

1. **Sblocco Totale di Romance, Passione, Cotte e Tensione Sessuale:**
   - I personaggi adulti (18+) possono provare attrazione, fascinazione erotica, desiderio, cotte, chimica passionale e seduzione esplicita.
   - La macro `{{user}}` non viene hardcodata nella prosa per preservare la flessibilità sistemica AnyPOV, ma i personaggi possiedono una spiccata reattività emotiva, istinti di accoppiamento, vulnerabilità intima e pulsioni fisiche vive.
2. **Sblocco Dinamiche di Potere, Università e Taboo Consenzienti (18+):**
   - Nel contesto SUCC e Blackwood, essendo tutti i personaggi del corpo studentesco e docenti maggiorenni (18+), sono pienamente ammesse dinamiche mature: rivalità seduttive, relazioni professore-studente adulto, coach-atleta adulto, boss-subordinato, contratti di branco e dinamiche di sottomissione/dominanza.
3. **Piena Integrazione della Biologia LSE (Lupine Social Ecology):**
   - Gli istinti biologici dei licantropi (Heat, Rut, Knotting, Baculum, Mating Bond, Scent Marking, Pheromones, Biting, Claiming, Breeding instincts) costituiscono lore primaria del mondo e possono essere integrati direttamente nella `description`, nei tratti e nel comportamento, senza bisogno di essere censurati o nascosti.
4. **Combattimento Viscerale e Linguaggio Senza Filtri:**
   - Libertà di linguaggio realistico, crudo o volgare se coerente con la voce del personaggio. Combattimenti brutali, sfide per la gerarchia di branco, lotte clandestine e missioni letali nei dungeon sono pienamente autorizzati.
5. **Intimacy Profiles & Kink Lore:**
   - Possono essere strutturati come voci Lexicon di tipo `memory` collegate al personaggio (`attached_world_character_id`), oppure inseriti direttamente nei tratti e sfumature comportamentali del personaggio per guidare il roleplay intimo ad alto coinvolgimento narrativo.

### Specifiche Tecniche dell'Intimacy Profile Lexicon (Wyvern World)

- **Nome dell'Entry:** `"Intimacy Profile - <NomePersonaggio>"`
- **Entry Type:** `"memory"` (**Tassativamente Memory**, come da regola di Lys).
- **`is_global`:** `true` (deve rimanere attiva nella scansione del World; il confinamento al contesto appropriato avviene tramite `party_conditions`).
- **`keys`:** `["<NomePersonaggio>"]` (chiave primaria: solo il nome univoco del personaggio).
- **`secondary_keys`:** `["intimacy", "dating", "relationship", "romance", "flirting", "attracted", "sex"]`
- **`key_logic`:** `"AND_ANY"` (scatta solo se è presente il nome E almeno una parola dell'argomento intimo; mai mettere parole generiche nelle chiavi primarie).
- **`priority`:** Circa `50` (o `100` per lo stile strutturato a blocchi).
- **`party_conditions`:** `[{ character_ids: ["<id_del_personaggio>"], mode: "has_any" }]` (garantisce che l'entry esista e sia iniettata solo ed esclusivamente se il personaggio è fisicamente presente nella scena).
- **`attached_world_character_id`:** Valorizzato con l'`id` attuale del personaggio nel World (campo **Attached Character**, fondamentale per tracciabilità e integrità relazionale; controllare che punti all'id attivo e non a entità orfane).

### Stili di Redazione

A seconda della complessità del personaggio, adottare uno dei due registri:
- **A Blocchi Strutturati (Stile Erik):** Utile per psicologie intime complesse o traumi profondi, articolato con etichette chiare:
  - `<NOME>_INTIMACY_BASELINE`
  - `<NOME>_BODY_REACTIONS`
  - `<NOME>_VULNERABILITY_SHAPE`
  - `<NOME>_VOICE_IN_INTIMACY`
  - `<NOME>_HARD_LIMITS_AND_HARD_YESES`
  - `<NOME>_AFTERMATH`
- **In Prosa Continua (Stile Dominic Rogers):** 3-4 paragrafi fluidi su stimoli psicologici, dinamiche preferite, gestione dei limiti e reattività emotiva, senza misure anatomiche numeriche esplicite.
