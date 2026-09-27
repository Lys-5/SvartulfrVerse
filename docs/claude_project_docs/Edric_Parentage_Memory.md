# Il segreto di Edric come Memory di Logan

Data: 2026-09-03. Stato: **applicato e verificato dopo reload completo.**

## Decisione

La parentela reale di Edric (figlio biologico di Erik, non di Logan) non è più
un dato di World globale. È una **Lexicon entry di tipo Memory agganciata a
Logan Douglas**, quindi entra in contesto **solo quando Logan è in scena**. Se
Logan non c'è, il segreto non esiste per il modello, ed è esattamente il
comportamento voluto: è un segreto che solo lui può decidere di far uscire.

## Cosa è stato creato

**Lexicon → `Edric's Parentage (Logan's Secret)`**

- Type: `memory`
- Attached Character: **Logan Douglas** (`_gYwk8EbFrtwPatB9CgC3D`)
- Content: 2.659 caratteri
- Keys: `Edric's parentage`, `Edric's father`, `Edric secret`, `Logan's secret`
- Cartella al momento: UNCATEGORIZED (spostamento a cura dell'utente)

Copre: cosa sa Logan esattamente, perché ha scelto di mentire, cosa gli costa,
e le tre circostanze strette in cui la cosa potrebbe venire fuori.

## Cosa è stato ripulito

Il segreto era leggibile in tre punti che lo rendevano di fatto pubblico:

| Dove | Prima | Dopo |
|---|---|---|
| Card **Edric Douglas** | `display_description`, `summary`, `long_summary` (BACKSTORY + sezione `THE SECRET HE CARRIES`) e un campo Attitude dicevano che Erik è suo padre | Riscritti sulla cover story che Edric conosce davvero; la sezione è diventata `WHAT HE IS ACTUALLY AFRAID OF`. `long_summary` 3.310 caratteri |
| Lexicon **House Genealogies Summary** (globale, `concept`) | "- Edric Douglas: Pureblood, Gamma (unpresented). Publicly Logan's son; secretly Erik's illegitimate child." | "- Edric Douglas: Pureblood, Gamma (unpresented). Logan's son, raised at the garage in Seven Hills." 4.055 caratteri |
| Card **Erik Douglas**, `long_summary` | "...Logan, his Beta brother and Head of Security, is his trusted shield - and unknowingly hides the secret that Edric, Erik's 'nephew,' is actually Erik's own illegitimate son." | "...Logan, his Beta brother and Head of Security, is his trusted shield, and Logan's son Edric is the nephew Erik micromanages from a distance, insisting on wellness protocols and scheduled drop-offs the boy never asked for." 14.730 caratteri |

Il caso di Erik era il più grave: Erik **non sa**, e la sua stessa scheda lo
diceva al modello.

## Verifica finale (dopo reload completo, dati letti dal server)

- Lexicon: 138 entries. `Edric's Parentage` presente, `type: memory`,
  `attached_world_character_id` = Logan.
- Scansione di tutte le 138 Lexicon entries su
  `illegitimate|secretly Erik|Erik's biological|true parentage`: **zero
  occorrenze** oltre alla Memory stessa.
- Scansione di tutte le 86 Character card sugli stessi pattern: **solo Logan
  Douglas**, che è corretto.

## Nota di metodo (combobox lunghi)

Il campo Attached Character è una combobox con 87 opzioni. Non risponde né a
eventi sintetici né a Invio da tastiera. Sequenza che ha funzionato:

1. click di mouse reale sul trigger, con coordinate calcolate dal
   `getBoundingClientRect` CSS convertite nel frame dello strumento
   (`x * 800 / innerWidth`, `y * 538 / innerHeight`);
2. tasto **End** per portare l'evidenziazione sull'ultima opzione (o le frecce
   per le altre), che ha anche l'effetto di scrollarla dentro il viewport;
3. lettura del rect di `document.activeElement` e **click di mouse reale** su
   quelle coordinate. Invio, in questo punto, non commit-a il valore.

Il campo Search della lista non filtra dentro le cartelle collassate: per
trovare una entry va prima espansa la cartella dalla chevron.
