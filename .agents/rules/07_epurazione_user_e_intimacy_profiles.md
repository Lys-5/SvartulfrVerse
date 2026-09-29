# Regola 07 — Epurazione di `{{user}}`, Conformità Policy Wyvern e Intimacy Profiles

## 1. Epurazione Radicale di `{{user}}` e Policy sui Contenuti

In questo World, `{{user}}` non è un'identità fissa: può essere Alyssa Douglas in certi scenari, la fidanzata di Jasper in altri, Jasper stesso, o una figura esterna. Se si mantenessero riferimenti a `{{user}}`, dinamiche romantiche o intime di personaggi adulti finirebbero per riversarsi in modo inappropriato su qualunque giocatore (es. una studentessa matricola).

Tutti i personaggi, le voci di Lexicon e gli scenari devono inoltre rispettare tassativamente la [Wyvern Prohibited Content Guide](https://wiki.wyvern.chat/en/Policies/Prohibited-Content-Guide).

### Procedura Obbligatoria su Ogni Card o Testo Importato

1. **Rimozione della macro `{{user}}`:** La stringa `{{user}}` va eliminata ovunque, **senza** sostituirla con un nome proprio specifico.
2. **Generalizzazione dei ruoli:** Convertire il ruolo in termini sistemici e impersonali (es. `"{{user}}, l'allenatrice di cheerleading"` diventa `"chiunque gestisca il programma di cheerleading in una data stagione"`).
3. **Age Gating e Divieto Assoluto di Sessualizzazione di Minori (Policy #1):**
   - Qualsiasi personaggio destinato a temi di romance o intimità deve avere età esplicitamente dichiarata come **18+** (`AGE: {{age}}` o età anagrafica).
   - I personaggi minorenni (es. Edric Douglas, 12 anni) sono categorizzati unicamente come background NPC/famiglia con blocco assoluto di framing intimo: *"strictly minor background NPC: zero romantic or intimate framing under any circumstances"*.
   - Divieto totale di flirting, romance, grooming o attrazione verso personaggi minorenni o studenti delle scuole superiori. Elementi di trauma o abusi passati sono ammessi nella backstory solo se il personaggio è attualmente adulto, senza descrizioni grafiche ed evitando qualsiasi glorificazione o feticizzazione.
4. **Cancellazione di tensioni sessuali e cotte verso il giocatore:** Eliminare alla radice infatuazioni, cotte o attrazioni rivolte a `{{user}}`, specialmente se il personaggio è un adulto/staff e il potenziale interlocutore è uno studente. Il vuoto narrativo va colmato con tratti psicologici, compiti professionali e relazioni interne al mondo.
5. **Relazioni di Autorità e Confini Accademici:** Per personaggi con ruoli di comando o docenza su studenti (es. professori e coach SUCC), inserire una riga esplicita che precluda qualunque spiraglio a relazioni intime o inappropriate con il corpo studentesco.
6. **Harkness Test e Divieto di Bestialità (Policy #2):**
   - È vietata qualsiasi sessualizzazione verso animali reali.
   - Personaggi licantropi, demi-umani, furry e creature fantastiche/mostruose sono ammessi nelle relazioni intime **solo se superano l'Harkness Test**: devono essere senzienti, in grado di comunicare tramite linguaggio umano/articolato e biologicamente adulti per la loro specie.
7. **Divieto di Necrofilia, Guro e Feticizzazione della Morte (Policy #3):**
   - Violenza, ferite e morte sono ammesse nella narrazione d'azione (con adeguato rating Mature/Explicit), ma è severamente vietato sessualizzare cadaveri, ferite gravi, mutilazioni o agonia. Personaggi non-morti (vampiri, reanimated come Fade o Roland) sono ammessi solo come esseri pienamente senzienti, escludendo qualsiasi dettaglio grafico di decomposizione sessualizzata.
8. **Divieto di Scat, Fart, Vomit, STD Fetish e Prompt NSFL (Policy #4 & #6):**
   - È bandita la feticizzazione di escrementi, vomito o malattie sessualmente trasmissibili.
   - È vietato inserire nei prompt di sistema frasi come `"Explicit NSFL content is permitted"`.
9. **Esclusione all'Origine di Tematiche Non Consensuali Reali:**
   - Tratta di persone, abusi sessuali coercitivi reali o schiavismo sessuale attivo vanno **espunti alla radice prima della scrittura**. Non vanno importati per essere "ripuliti", ma riadattati (es. Zeera riconvertito in CEO aziendale con lo schiavismo ridotto a lontano retaggio storico di specie mai praticato dal personaggio). Conservare solo dinamiche sane, consenzienti e riutilizzabili.
10. **Divieto di "The Player (Persona)" nelle Attitudes:** Non usare tale entità per sentimenti diretti a un singolo individuo (vedi Regola 10).
11. **Verifica Finale Stringa:** Verificare sempre che la sottostringa `{{user}}` sia pari a zero occorrenze in ogni campo.
12. **Documentazione:** Registrare nel documento di riepilogo del Project gli elementi rimossi e le motivazioni dell'adattamento.

---

## 2. Gestione Contenuti Intimi e Anatomici: Gli Intimacy Profiles

I blocchi anatomici dettagliati e i profili di intimità/kink **non vanno trascritti nella `description`** della card (dove risulterebbero invasivi e deformerebbero il prompt narrativo generale).
Non vanno tuttavia cestinati se coerenti con la psicologia del personaggio: vanno **estratti come entry Lexicon separata**.

### Conformità con la Wyvern Prohibited Content Guide

Tutti gli Intimacy Profiles devono rispettare i seguenti principi di sicurezza:
1. **Riservati Esclusivamente a Personaggi Adulti (18+):** Nessun Intimacy Profile può essere creato o collegato a personaggi minorenni.
2. **Consenso e Dinamiche Relazionali Sane:** Pratiche di dominance/submission o kink devono basarsi su mutuo consenso, negoziazione e rispetto dei limiti personali (*Hard Limits*, *Aftercare*), escludendo violenza non consensuale reale.
3. **Registro Psicologico ed Enciclopedico:** Il testo deve esplorare la vulnerabilità emotiva, la risposta sensoriale e la chimica relazionale, evitando volgarità gratuita o contenuti banditi (no bestialità, no guro, no scat/STD).

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
