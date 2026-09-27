# Logan Douglas — Completamento scheda (2026-09-21)

Sesto personaggio della priority list core family/pack (dopo Erik, Jasper, Alyssa, Malachia, Noah). Lavorazione completata direttamente sul sito Wyvern via browser automation (nessun uso del Wyldfire locale, nessuna estrazione di token Firebase), in continuazione da una sessione precedente compattata.

## Pipeline §14 completata

- Timeline: Start Position + Birthdate = 10054920 (World Clock, coincidono, entrambi ≤ world_age 10486470 → sanity check §6 passato)
- Pronomi: He/Him
- Outfit: 6 totali (inclusi da fonte), Default Outfit impostato su "Garage / Officina"
- Dialogue Examples: 5 (corretto da 3 nel campo "How many examples to show")
- Attitudes: 10 totali, con 2 correzioni di tier (vedi sotto)
- Global Character: ON (era OFF, non ancora toccato in questa lavorazione)
- Writing Style & Tone (Advanced Parameters / `final_instructions`): popolato dalla fonte (1354 caratteri → 288 token), era completamente vuoto

## Bug scoperto e corretto: scambio Long/Short Description

Lo script di batch-injection originale (pre-compattazione) assumeva l'ordine dei textarea `[display, short, long]`, ma l'ordine reale visivo/DOM sulla pagina di modifica personaggio è `[display, long, short]`. Risultato: il campo Long Description conteneva il breve blocco ALWAYS/NEVER, e il campo Short Description conteneva l'intero blocco JED+.

**Non è un pattern di corruzione preesistente del sito**, è un artefatto del mio stesso script di questa lavorazione. Corretto scambiando i due valori via JS e risalvato; verificato con un secondo reload che lo scambio è persistito (Long = 7250 caratteri, inizia con "[NAME: Logan Dominic Douglas...", Short = 621 caratteri, inizia con "Logan Douglas - 49, Pureblood Beta...").

**Rischio aperto non ancora verificato**: Erik, Jasper, Alyssa, Malachia e Noah potrebbero avere lo stesso bug se le loro schede sono state popolate con lo stesso script di batch-injection con la stessa assunzione di ordine errata. Da controllare in una sessione futura, non ancora fatto.

## Scoperta tecnica: campo Context dei Dialogue Example

Il campo "Context" di un Dialogue Example è un `<input>` (placeholder "What situation triggers this response..."), non un `<textarea>` come il campo "Response" (placeholder "This character's dialogue response..."). Un primo tentativo che filtrava solo `textarea` per placeholder ha mancato il campo Context, causando un disallineamento contenuto/campo sul primo Dialogue Example, poi corretto.

## Correzioni tier Attitude

Seguendo il precedente stabilito su Noah (vedi `claude/Noah_Douglas_Bloodmoon_Completamento_2026-09-21.md`): due Attitude corrotte con tier `romantic_interest` corrette a `best_friend`, perché si tratta di relazioni familiari/platoniche, non romantiche:

- **Edric** (il "figlio" che Logan protegge, in realtà figlio biologico di Erik): `romantic_interest` → `best_friend`
- **Alyssa Douglas**: `romantic_interest` → `best_friend`

## Intimacy Profile - Logan: audit e correzione §13.3

L'entry Lexicon esistente non era conforme al formato standard del progetto. Correzioni applicate:

| Campo | Prima | Dopo |
|---|---|---|
| Entry Type | No specific type | **Memory** |
| Attached Character (comparso dopo aver impostato Entry Type = Memory) | (campo non presente) | **Logan Douglas** |
| Priority | 10 | **100** (convenzione per Intimacy Profile in stile a blocchi, come Erik) |
| Primary Keywords | Logan, intimacy, mate, partner | **Logan** (solo) |
| Secondary Keywords | (vuoto) | **intimacy, dating, relationship, romance, flirting, attracted, sex** |
| Party Conditions | Nessuna | **Has ANY of → Logan Douglas** |
| Global Entry | ON | ON (invariato, corretto) |

Contenuto (stile a blocchi: `Logan_INTIMACY_BASELINE`, `Logan_TRAUMA_MAP`, `Logan_BODY_REACTIONS`, `Logan_VULNERABILITY_SHAPE`, `Logan_VOICE_IN_INTIMACY`, `Logan_HARD_LIMITS_AND_HARD_YESES`, `Logan_AFTERMATH`) verificato programmaticamente via JS: zero `{{user}}`, zero em-dash, zero doppio trattino, zero asterischi, zero grassetto markdown.

Salvato e riverificato dopo reload completo: tutte le correzioni (Entry Type, Attached Character, Priority, Primary/Secondary Keywords, Party Condition) confermate persistenti.

## Verifica finale §14.12

Dopo reload completo della card principale: zero `{{user}}`/em-dash/doppio-trattino/asterischi/grassetto markdown su tutti i campi description (display=186, long=7250, short=621 caratteri, valori corretti dopo il fix dello scambio). Timeline, Pronomi, Outfit (6, Default impostato), Dialogue Examples (5), tutte e 10 le Attitude con intensità e tier corretti, Global Character ON, Writing Style & Tone persistito (288 token) tutti confermati. RPG Stats non toccato (sistema in pausa, `world_features.rpg_stats: false`).

## Stato pipeline core family

Completati: Erik, Jasper, Alyssa, Malachia, Noah, **Logan**.

Prossimi in coda secondo l'ordine di priorità approvato: **Wulfnic, Kaladin**, poi **Jared Thompson e Mac**.
