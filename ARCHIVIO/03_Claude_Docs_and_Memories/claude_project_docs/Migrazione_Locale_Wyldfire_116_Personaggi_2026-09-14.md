# Migrazione Locale Wyldfire — Recupero Completo 116 Personaggi (2026-09-14)

Prosecuzione di `Atlas_Teague_Bug_Character_Bloccato_2026-09-14.md`. Documenta la soluzione trovata dopo che lo staff Wyvern ha confermato che il World online **non è riparabile** (database criptato per privacy) e che l'unica via è ricostruire il locale Wyldfire e ripubblicarlo.

## Il problema di partenza

Il database locale di Wyldfire (`wyldfire.db`) risultava congelato a un'istantanea del **7 settembre**, quindi non utilizzabile come fonte affidabile per l'intera settimana di lavoro fatta dopo quella data direttamente sul sito. Il backup markdown `Svartulfr.md` copre Lexicon/Locations/Environments/Scenarios ma **non i Character**. I backup JSON individuali in `D:\SvartulfrVerse\Wyvern\characters\` sono solo 9, risalenti a metà agosto, insufficienti.

## La scoperta che ha sbloccato tutto

L'endpoint di lista Character (`GET /api/worlds/characters/world/<world_id>`) è quello rotto dal bug di Atlas Teague, ma:

- **Il GET su un singolo Character funziona perfettamente per tutti gli altri 115/116 personaggi.**
- L'oggetto World stesso (`GET /api/worlds/<world_id>`) contiene `content_folders.characters`, un array di cartelle (Family, Pack, Blackwood, Solarton, Los Angeles) con gli `entry_ids` di ogni personaggio: **116 ID completi e autoritativi**, aggirando del tutto l'endpoint corrotto.

Con questi 116 ID ho scaricato via browser (autenticato, mai fetch diretto) il record completo di ogni personaggio, confrontato con `platform_id` contro gli 86 presenti in locale, e calcolato:

- **30 personaggi completamente assenti in locale**: Marlowe Voss, Cassian Aralas, Abel Vilas, Barrow, Harrison Black, Brak Ironfist, Harlan Beaumont, Helena Weiss, Marcus O'Connor, Darius Vale, Naomi Black, Roger "Rocky" Mackenzie, Arthur Grey, Harlow MacGregor, Sawyer Shephard, Adrian Locke, Zeera, Rue, Venera Dolce, Kai Mitchell, Coach Mithers, Hideo Reid, Romeo "Gray" Dean, Adelin Coso, Rifle Maddox, Amelia DeVille, Charles "Charlie" DeVille, Park Jae-Sung, Arran Parker, Siebren Dijkstra.
- **80 presenti ma non aggiornati** (toccati sul sito dopo la sincronizzazione locale del 7/9).
- **6 già allineati.**

## Mappatura dei campi (API live → colonna locale `world_characters`)

Verificata riga per riga prima di scrivere, per evitare di ripetere l'errore di tipo che ha causato il bug originale (§ del documento precedente):

- **`rpg_stats` vive come campo di primo livello nell'oggetto Character live**, non dentro `entity_statistics` (che è solo analytics: like, messaggi, viste). Contiene `base_stats`, `enabled`, `experience`, `level`, e talvolta `species_id`/`occupation_id` annidati. Copiato as-is nella colonna locale `rpg_stats` (JSON compatto). Le colonne locali separate `species_id`/`occupation_id` restano `NULL`, coerente con la convenzione già osservata su ogni riga locale esistente (mai popolate, anche quando `rpg_stats` è pieno).
- **`attitudes[].target_id`** e **`default_inventory[].lexicon_entry_id`**: qui la prima versione di questo documento riportava "nessuna traduzione necessaria" perché sia l'API live sia lo snapshot locale pre-esistente del 7/9 avevano già lo stesso valore (il platform_id). **Correzione, vedi sezione successiva**: quel valore condiviso era comunque sbagliato per l'app Wyldfire, che risolve questi riferimenti contro l'**id locale**, non il platform_id. Il fatto che combaciassero prima e dopo la migrazione ha mascherato per un momento che fosse comunque un dato non risolvibile dall'interfaccia.
- **`home_location_id`** è l'unico campo che richiede traduzione: localmente punta all'**id locale** della Location (non al platform_id). Costruita una mappa `platform_id → id locale` da `world_locations` per tradurre.
- **`avatar` (personaggio e per-outfit)**: preservato il percorso file locale già scaricato quando presente (`C:\Users\...\files\avatars\...`), altrimenti usato l'URL remoto CDN dall'API. Evita di perdere la cache locale delle immagini già sincronizzate.
- Campi senza equivalente nell'API (`base_character_id`, `base_world_character_id`, `actioned_by_id`, `battle_rewards`, `voice_profile`) lasciati al valore locale esistente sugli update, `NULL` sui nuovi insert.

## Esecuzione

Script Python diretto su una copia locale di `wyldfire.db` (mai toccato l'originale prima della verifica):

1. Backup della copia pre-migrazione.
2. 86 `UPDATE` + 30 `INSERT` in un'unica transazione sulla tabella `world_characters`, `world_id = 6cfuc64QBr1Flf9nKndFy`.
3. `PRAGMA wal_checkpoint(TRUNCATE)` per ottenere un file `.db` autocontenuto (il locale gira in `journal_mode=wal`).
4. Verifica: `PRAGMA integrity_check` → `ok`; conteggio righe World → **116/116**; zero campi JSON malformati su tutte le colonne array/oggetto; spot-check su Wulfnic (avatar locale preservato, `home_location_id` tradotto correttamente), Vito Marino (RPG stats/species_id post-promozione Pureblood recuperati), Zeera (nuovo insert, tutti i campi popolati).
5. Scritto sul PC dell'utente **solo dopo conferma che l'app Wyldfire fosse chiusa**, per evitare conflitti di scrittura sul file SQLite. Backup dell'originale scritto accanto come `wyldfire.backup-pre-migration.db`. Verificato che non restassero file `-wal`/`-shm` residui che avrebbero potuto sovrascrivere la migrazione al riavvio dell'app.

## Stato a fine intervento

`wyldfire.db` locale aggiornato e verificato con tutti i 116 personaggi del World. Prossimi passi (a carico dell'utente): riaprire Wyldfire, controllo visivo, eventuali correzioni puntuali via UI (opzione 2), poi pubblicazione del World pulito da Wyldfire e cancellazione manuale del World online rotto.

## Nota per la pipeline futura

Questo intervento conferma inoltre, per riferimento §11 del workflow: il campo `rpg_stats` è la fonte autoritativa anche per `species_id`/`occupation_id` quando presenti nell'oggetto live, non serve più cercarli altrove.

## Correzione successiva: Attitudes e Default Inventory "senza personaggio assegnato" (2026-09-14, stesso giorno)

Dopo la prima migrazione l'utente ha segnalato, riaprendo Wyldfire: nelle Attitudes di ogni scheda il campo "World Character" risultava vuoto/non assegnato pur con reasoning e tier compilati, e gli item del Default Inventory mostravano un'icona "?" col solo ID grezzo al posto del nome.

**Causa reale**: l'app Wyldfire risolve `attitudes[].target_id` e `default_inventory[].lexicon_entry_id` cercando una corrispondenza contro l'**id locale** (colonna `id`, chiave primaria) delle rispettive tabelle (`world_characters`, `world_lexicon_entries`), non contro il `platform_id`. L'oggetto scaricato dall'API live usa invece sempre il platform_id in questi due campi. **Questo non è un errore introdotto dalla migrazione**: verificato che lo snapshot locale originale del 7 settembre (mai toccato prima della mia scrittura) aveva già gli stessi valori platform_id in questi campi, quindi il problema esisteva già nel sync originale sito → Wyldfire, semplicemente non era stato notato prima perché l'utente non aveva ancora ispezionato queste schede nel dettaglio dentro l'app.

**Fix applicato**: script separato che, per tutti i 116 personaggi, ricostruisce le mappe `platform_id → id locale` per `world_characters` e `world_lexicon_entries`, poi traduce ogni `attitudes[].target_id` (dove `target_type == "world_character"`) e ogni `default_inventory[].lexicon_entry_id` dal platform_id all'id locale corrispondente. Il campo `default_creatures` è risultato vuoto su tutti i 116 personaggi live, quindi non richiede lo stesso trattamento (per ora).

**Risultato**: 110 schede su 116 avevano almeno un riferimento da tradurre; **0 riferimenti rimasti irrisolti** (ogni target_id/lexicon_entry_id trovava una corrispondenza locale). Verificato a campione: Wulfnic → Nixara (Attitude, tier `romantic_interest`) ora risolve correttamente, così come i due item del suo Default Inventory (Rolls-Royce, Keys); Alyssa Douglas Bloodmoon → Erik/Malachia/Jasper/Edric (tutti `romantic_interest`) risolvono tutti al nome giusto.

Scritto sul PC solo dopo nuova conferma che Wyldfire fosse chiuso, backup della versione intermedia salvato accanto (`wyldfire.db.backup2-<timestamp>`, lato container, non ancora portato sul PC dell'utente perché il backup pre-migrazione originale è già lì come rete di sicurezza più a monte).

**Nota per la pipeline futura, integrazione a §11 e §14**: quando in futuro si scriverà di nuovo dal locale Wyldfire verso il sito o viceversa, **qualunque campo che referenzia un'altra entità del World per ID va controllato per la direzione della traduzione**: l'API pubblica di Wyvern usa sempre il platform_id, mentre il database locale di Wyldfire usa l'id locale della riga referenziata (confermato ora per `home_location_id`, `attitudes[].target_id`, `default_inventory[].lexicon_entry_id`; `attitudes[].target_id` quando `target_type` non è `world_character` resta una stringa libera, non va tradotto). Non dare per scontato che un valore identico tra le due fonti sia "già corretto": può semplicemente significare che il sync originale aveva lo stesso bug.
