# Regola 07 — Epurazione di `{{user}}` e Creazione Intimacy Profiles

## 1. Epurazione Radicale di `{{user}}`

In questo World, `{{user}}` non è un'identità fissa: può essere Alyssa Douglas in certi scenari, la fidanzata di Jasper in altri, Jasper stesso, o una figura esterna. Se si mantenessero riferimenti a `{{user}}`, dinamiche romantiche o intime di personaggi adulti finirebbero per riversarsi in modo inappropriato su qualunque giocatore (es. una studentessa matricola).

### Procedura Obbligatoria su Ogni Card o Testo Importato

1. **Rimozione della macro `{{user}}`:** La stringa `{{user}}` va eliminata ovunque, **senza** sostituirla con un nome proprio specifico.
2. **Generalizzazione dei ruoli:** Convertire il ruolo in termini sistemici e impersonali (es. `"{{user}}, l'allenatrice di cheerleading"` diventa `"chiunque gestisca il programma di cheerleading in una data stagione"`).
3. **Cancellazione di tensioni sessuali e cotte verso il giocatore:** Eliminare alla radice infatuazioni, cotte o attrazioni rivolte a `{{user}}`, specialmente se il personaggio è un adulto/staff e il potenziale interlocutore è uno studente. Il vuoto narrativo va colmato con tratti psicologici, compiti professionali e relazioni interne al mondo.
4. **Relazioni di Autorità:** Per personaggi con ruoli di comando o docenza su studenti, inserire una riga esplicita che chiuda espressamente qualunque spiraglio a relazioni inappropriate con il corpo studentesco.
5. **Divieto di "The Player (Persona)" nelle Attitudes:** Non usare tale entità per sentimenti diretti a un singolo individuo (vedi Regola 10).
6. **Esclusione all'Origine di Tematiche Non Consensuali:** Quando una card sorgente include tratta di persone, abusi sessuali, rapporti coercitivi o archi romantici ossessivi incentrati su `{{user}}` (casi: Zeera, Huck, Marek, ecc.), **questo materiale va espunto alla radice prima della scrittura**. Non va importato né trascritto per essere poi "ripulito". Riconvertire il personaggio (es. Zeera riconvertito in CEO aziendale con il passato di schiavismo trattato solo come lontano retaggio di specie e non pratica personale) conservando unicamente aspetto fisico sobrio, voce e dinamiche sane riutilizzabili.
7. **Verifica Finale Stringa:** Verificare sempre che la sottostringa `{{user}}` sia pari a zero occorrenze in ogni campo.
8. **Documentazione:** Registrare nel documento di riepilogo del Project gli elementi rimossi e le motivazioni dell'adattamento.

---

## 2. Gestione Contenuti Intimi e Anatomici: Gli Intimacy Profiles

I blocchi anatomici dettagliati e i profili di intimità/kink **non vanno trascritti nella `description`** della card (dove risulterebbero invasivi e deformerebbero il prompt narrativo generale).
Non vanno tuttavia cestinati se coerenti con la psicologia del personaggio: vanno **estratti come entry Lexicon separata**.

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
