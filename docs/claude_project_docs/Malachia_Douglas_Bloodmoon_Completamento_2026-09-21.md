# Malachia Douglas Bloodmoon — Completamento scheda (2026-09-21)

## Stato di partenza

Corruzione dello stesso tipo già vista su Erik/Jasper/Alyssa, ma in una variante diversa: invece dello scambio Short↔Long Description, su Malachia era la **Long Description a essere vuota** e la **Short Description a contenere tutto il blocco JED+ grezzo non ripulito** (12929 caratteri, con blocco anatomico esplicito incluso). Mancavano inoltre: Name split (Middle Names/Nicknames/Titles), Tags, Timeline (Start Position/Birthdate), Pronomi (di default su "They/Them" invece di He/Him), Outfit (0 invece di 6), Default Outfit, "How many examples to show" (3 invece di 5), Dialogue Examples (0 invece di 5), Attitudes (0 invece di 8), Global Character (OFF), Writing Style & Tone (vuoto).

Riferimento pulito: riga completa dumpata da `live_delete2.db` (id `z1KHSz0a5BPgsFmwbQ7kO`).

## Lavoro svolto

**Name / Tags**: Middle Name "Björn", Nicknames "Mal", "Ghost", "King", Titolo "Heir to the Pack of Seven Hills", Tags (4, via modale). Aggiunti con il pulsante "+" esplicito (Invio non fa commit del chip in questi campi, comportamento confermato di nuovo).

**Description**: Display/Long/Short scritte via JS (native setter + evento `input`) dopo verifica preventiva indice-per-indice delle tre textarea (per evitare l'errore di scambio già capitato su Alyssa). Dal blocco JED+ grezzo è stato **rimosso il blocco anatomico esplicito** (CHEST/NIPPLES/PENIS/BALLS/ANUS con misure numeriche) per §13.3, e la riga MATING_AND_KINKS è stata sostituita con una versione non grafica ("Dominant, protective, and intense, requiring deep trust to let his guard down"). Tutti i doppi trattini "--" residui sono stati sostituiti con virgole/punti. Lunghezza finale Long Description: 11445 caratteri.

**Timeline**: Start Position = Birthdate = 10244064 (world_age attuale 10486470, coerente). Nessun End Position (personaggio vivo).

**Pronomi**: preset "He/Him" selezionato dal menu nativo (il pronome sorgente era he/him/his/his/himself; il valore di default del form era erroneamente "They/Them").

**Outfit**: 6 outfit ricreati dal campo `outfits` della fonte (Allenamento/Combattimento, Servizio di Sicurezza Standard, Formale/Casa, Ring Clandestino/Ghost, Full Shift, Hybrid Shift), riempiti in batch via JS. Un settimo slot vuoto aggiunto per errore da un doppio click su "Add Outfit" è stato individuato e cancellato prima del salvataggio. Default Outfit impostato su "Servizio di Sicurezza Standard".

**Dialogue Examples**: "How many examples to show" portato da 3 a 5, 5 esempi riempiti in batch via JS.

**Attitudes (8)**: Alyssa (Best Friend, 100), Erik (Best Friend, 70), Wulfnic (Best Friend, 92), Logan (Friend, 68), Kaladin (Acquaintance, 55), "underground fighting circuit" (Generic, Friend, 60), Jasper (Best Friend, 78), Atlas Teague (vedi discrepanza sotto).

**Global Character**: era OFF, portato ON.

**Writing Style & Tone**: applicato il testo sorgente (1029 caratteri, già comprensivo della frase di disciplina di formato), verificato pulito (zero em-dash, zero doppio trattino, zero asterischi).

## Discrepanza: nessun tier "Rival" nella Relationship Tier ladder

Come già segnalato per Jasper e Alyssa, la ladder live mostra tier in inglese semplice, non quella LSE-tematica descritta nelle istruzioni di progetto (§16). Elenco completo osservato per Malachia: Nemesis, Enemy, Despised, Hated, Disliked, Stranger, Acquaintance, Friend, Close Friend, Best Friend, Romantic Interest, Lover, Partner, Soulmate.

**Non esiste un tier "Rival".** Per Atlas Teague, la fonte prevedeva "Rival". In assenza di un tier equivalente, è stato scelto **Acquaintance** come il più vicino disponibile (dinamica di rispetto competitivo, non ostile), con **Intensity 75** per riflettere il peso reale della relazione nonostante il tier tecnicamente "basso" nella convenzione di progetto (che assocerebbe Acquaintance a 20-25). Scelta segnalata qui come discrepanza aperta, non normalizzata silenziosamente. Reasoning scritto: "An unregistered lone wolf who keeps turning up on Blackwood's illegal fighting circuit. Malachia has beaten him and been beaten by him in close to equal measure, and has quietly chosen not to report him, which is as close as Malachia gets to admitting he respects the man."

Questa è la terza scheda di fila (dopo Jasper e Alyssa) con la stessa incongruenza fra la ladder documentata in §16 e quella osservata live. Resta da portare all'attenzione dell'utente a un checkpoint naturale, o da correggere direttamente nelle istruzioni di progetto se si conferma che la ladder LSE non è mai stata effettivamente implementata lato piattaforma.

## Intimacy Profile - Malachia: trovata già esistente, corretta per conformità a §13.3

A differenza di quanto risultava nel riepilogo pre-compattazione (contenuto anatomico rimosso dalla description ma non ancora spostato in un'entry separata), **l'entry Lexicon "Intimacy Profile - Malachia" esisteva già** nel World (probabilmente creata in una sessione precedente non coperta dal riepilogo disponibile). È stata trovata non pienamente conforme al formato standard di §13.3 e corretta:

- **Doppio trattino "--"** in due punti del testo (Primary Content) sostituito con virgola, per la disciplina di formattazione.
- **Entry Type**: era "No specific type", portato a **"Memory"** come da convenzione.
- **Attached Character**: era "None — global memory", impostato su **Malachia Douglas Bloodmoon** (campo apparso solo dopo aver impostato Entry Type a Memory).
- **Priority**: era 10, portato a **100** (registro a blocchi, coerente con lo stile Erik: `Malachia_INTIMACY_BASELINE`, `_TRAUMA_MAP`, `_BODY_REACTIONS`, `_VULNERABILITY_SHAPE`, `_VOICE_IN_INTIMACY`, `_HARD_LIMITS_AND_HARD_YESES`, `_AFTERMATH`).
- **Primary Keywords**: erano `["Malachia", "intimacy", "mate", "partner"]` con `key_logic: AND_ANY`, cioè l'entry si sarebbe attivata anche solo per "mate" o "partner" senza che Malachia fosse coinvolto. Corretto a **solo `["Malachia"]`**.
- **Secondary Keywords**: erano vuote. Popolate con `["intimacy","dating","relationship","romance","flirting","attracted","sex","mate","partner"]`, spostando lì "intimacy"/"mate"/"partner" tolte dalle primarie e aggiungendo il set standard di §13.3.
- **Party Conditions**: erano assenti del tutto ("No party conditions. Entry activation is unaffected by party composition."), il che significa che l'entry sarebbe stata idonea in qualunque scena purché le keyword combaciassero, indipendentemente dalla presenza di Malachia nel party. Aggiunta condizione **Has ANY of: Malachia Douglas Bloodmoon**, come richiesto da §7/§13.3.

Global Entry era già ON (`is_global: true`), corretto secondo la nota di §7 (non è l'is_global a restringere, ma le party_conditions, ora presenti).

Non toccato: il campo "Regex patterns" contiene solo il placeholder di esempio `\bdoors?\b` (non un valore salvato), verificato via JS che non è un valore reale di input, quindi nessuna azione necessaria lì.

**Nota di continuità per le schede future**: la scoperta che questa entry esisteva già ma con un formato imperfetto suggerisce di aggiungere un controllo esplicito "verificare se un Intimacy Profile esiste già per questo personaggio, anche se non citato nel riepilogo di sessione" come passo della pipeline standard, non solo "crearne uno se manca".

## Content Rating

Non toccato, lasciato su "General" nonostante la fonte indicasse `rating: "explicit"` (giustificato dal blocco anatomico ora rimosso dalla description e spostato nell'Intimacy Profile). Stessa scelta già presa per Alyssa: non modificare senza indicazione esplicita dell'utente, segnalato qui come discrepanza nota.

## Verifica finale (§14.12)

Eseguita dopo reload completo della pagina (via `window.location.reload()`, la navigazione automatica torna alla lista contenuti del World, da lì si è riaperta la scheda cercando "Malachia"):

- Display/Long/Short Description: lunghezze confermate (201/11445/613 caratteri), zero doppio trattino nel Long.
- Middle Name/Nicknames/Titles: confermati.
- 6 Outfit + Default Outfit "Servizio di Sicurezza Standard": confermati.
- Dialogue Examples: 5 confermati.
- Attitudes: tutte le 8 confermate nell'ordine corretto (Alyssa, Erik, Wulfnic, Logan, Kaladin, underground fighting circuit, Jasper, Atlas Teague).
- Global Character: ON confermato.
- Writing Style & Tone: 213 token, testo confermato.
- Intimacy Profile - Malachia: Entry Type Memory, Attached Character Malachia, Priority 100, Primary Keywords solo "Malachia", 9 Secondary Keywords, Party Condition Has ANY of Malachia, tutti confermati persistenti dopo reload.

Scheda considerata completa secondo la pipeline di §14, incluso il passo Intimacy Profile di §13.3.

## Prossimo personaggio

Prossimo nella lista di priorità concordata: **Noah**, poi Logan, Wulfnic, Kaladin, Jared Thompson, Mac.
