# Wyvern_Superseded — aggiornamento 30/08/2026 (notte)

Aggiunto in questo giro, in esecuzione dell'istruzione "in `D:\SvartulfrVerse\Wyvern` deve trovarsi solo
il materiale effettivamente caricato o pronto per essere caricato sulla piattaforma, tutto il resto va
spostato in draft":

## Lexicon_TypeBased_Superseded/ (nuovo)
Vecchia struttura locale del Lexicon organizzata per Entry Type (Concept.md, Creature.md, Event.md,
Furniture.md, Item.md, Job.md, Location.md, Memory.md, Mob.md, Move.md, NPC.md, Other.md, Vehicle.md).
Era incompleta/non allineata alle 39 entry reali attualmente su Wyvern (conteneva solo pochi entry
placeholder per file). **Sostituita interamente da `Wyvern/lexicon/by_folder/`**, il mirror 1:1 corretto
organizzato per folder Wyvern reale (Uncategorized, Chars Details, Underworld Concept, Item, Species,
History, Job & Business, SUCC Concept), generato dall'export nativo "Export as Markdown" del 30/08.

## world_info_legacy.md (nuovo, ex `Wyvern/world_info.md`, 2325 righe)
File di lavoro storico che mescolava World Description/Context Description con contenuto di Location
(es. Villa Douglas) e Dialogue Examples di personaggio (es. Logan) in un unico documento non strutturato.
Tutto il contenuto è ormai superato: il World Description/Context vive sulla piattaforma, Villa Douglas
è in `locations.md` (ancora attivo in `Wyvern/`, task Location non ancora completato), e i Dialogue
Examples dei personaggi sono nelle rispettive card JSON già in `Wyvern/characters/` o negli export
`*_card.json`/`*_world.json`. Conservato solo come riferimento storico.

## Core_Docs/Personas_Mechanism_Notes.md (nuovo, ex `Wyvern/personas/README.md`)
Nota di lavoro su come funziona realmente il meccanismo "Personas" su Wyvern (non una feature World-level
separata, ma Persona Preset + Playable Characters dentro l'editor di uno Scenario). Contenuto di
pianificazione/riferimento, non testo pronto da incollare — spostato in Core_Docs insieme agli altri
documenti di design. Riguarda in particolare la futura card standalone di Alyssa (in coda, dopo Noah e
Jasper), vedi anche `claude/Alyssa_Status_Note.md` nel progetto Cowork.

## Cosa resta in Wyvern/ (materiale attivo: già caricato o pronto per caricare)
- `characters/` — 9 cartelle (Edric, Erik, Jasper, Logan, Malachia, Noah, Ut, Wulfnic, Zefir), ciascuna
  con `*_card.json`/`*_world.json`: backup di archivio dei personaggi già live sulla piattaforma
  (Regola #1 del progetto: JSON scaricato dopo il salvataggio = backup, non un artefatto da sincronizzare
  in parallelo, ma resta utile come riferimento diretto di cosa è live).
- `lexicon/by_folder/` — mirror 1:1 corrente del Lexicon (39 entry, per folder reale).
- `locations.md` — master list Location, task ancora "in pausa" (~54 location mancanti): materiale
  pronto per essere caricato.
- `gerarchia_location.txt` — schema di classificazione Environment/Location/Internal usato attivamente
  per decidere dove va ogni nuova location.
- `environments.md` — riepilogo dei 12 Environment attualmente live sulla piattaforma (task completato,
  tenuto come riferimento diretto, stesso criterio dei backup Character).
- `scenarios/`, `scripts/` — cartelle vuote, nessuna azione (nessun contenuto da smistare).

---

## Aggiornamento 30/08/2026 (notte, seconda sessione) — stretta ulteriore della regola 1:1

Lys ha richiesto un criterio più stringente: in `Wyvern/` deve restare **solo** materiale che rispecchia
1:1 lo stato reale della piattaforma in questo momento, non più anche "materiale pronto per essere
caricato" o strumenti di lavoro. Spostati di conseguenza:

- **`Svartulfr_Urban_FullExport_30-08.md`** (nuovo qui, ex `Wyvern/Svartúlfr_Urban.md`, 416KB) — export
  grezzo completo del World fatto con "Export as Markdown" (World Description/Context/Base Instructions/
  Final Instructions + presumibilmente Characters/Lexicon/Locations/Environments/Scenarios in un unico
  documento non strutturato). Superato dalla struttura organizzata: `Wyvern/lexicon/by_folder/` per il
  Lexicon, `Wyvern/characters/*/` per i Character. Conservato come riferimento storico/fonte grezza,
  stesso trattamento di `world_info_legacy.md`.
- **`Drafts/Core_Docs/locations.md`** (spostato da `Wyvern/locations.md`) — non è un mirror 1:1: contiene
  61 location in prosa ma il conteggio Location live sulla piattaforma è 79, e non c'è modo di distinguere
  da questo file solo quali delle 61 sono già live e quali sono ancora "da creare" (~54 mancanti secondo
  la nota precedente). È materiale di pianificazione per il task Location ancora "in pausa", non uno
  specchio dello stato attuale.
- **`Drafts/Core_Docs/gerarchia_location.txt`** (spostato da `Wyvern/gerarchia_location.txt`) — schema di
  classificazione/metodologia di lavoro (Environment/Location/Internal), non contenuto della piattaforma:
  è uno strumento per decidere dove va una nuova location, non una entry esistente da rispecchiare.

## Cosa resta in Wyvern/ ora (aggiornato)

- `characters/` — 9 cartelle, backup 1:1 dei personaggi già live (Regola #1 progetto).
- `lexicon/by_folder/` — mirror 1:1 corrente del Lexicon (45 entry dopo la sessione del 30/08 notte).
- `environments.md` — riepilogo dei 12 Environment live sulla piattaforma (11 voci nel file: da
  verificare in futuro se manca 1 Environment non ancora annotato qui, discrepanza minore non ancora
  investigata).
- `personas/`, `scenarios/`, `scripts/` — cartelle vuote, nessuna azione.

`locations.md` e `gerarchia_location.txt` restano disponibili in `Drafts/Core_Docs/` per quando si
riprende il task Location; verranno ricreati in `Wyvern/` solo nella forma di un vero mirror 1:1 (es.
`Wyvern/lexicon/by_folder/`-style, organizzato per Environment reale) quando quel lavoro riparte.
