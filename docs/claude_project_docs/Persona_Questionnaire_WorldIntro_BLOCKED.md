# Character Creation Questionnaire — World Introduction

## Stato aggiornato (31/08/2026 sera): World Introduction COMPLETO

Tutte e quattro le Start Questions (Character Name, Species, Occupation, Starting Items, Backstory) più il World intro opening greeting reattivo sono state ricostruite, salvate e verificate con reload completo. La sezione "Ancora da ricostruire" della versione precedente di questo file è quindi superata: Occupation, Starting Items e Backstory sono stati ricreati esattamente come specificato più sotto in "Contenuto confermato persistito", con una correzione: il campo "Grant currency" è stato rimosso dalla domanda Occupation (vedi sotto, sezione RPG Blueprints).

Il falso errore "Failed to save introduction" resta un problema noto della piattaforma (falso positivo, il salvataggio va sempre a buon fine); il workflow di verifica resta salvataggio singolo + reload completo prima di procedere al campo successivo.

---

## Contenuto confermato persistito dopo reload (31/08/2026)

**Start Question 1 — Character Name**
- Tipo: Text
- Label: Character Name
- Help text: "What's your character's name?"
- Required: ON
- What this choice does: Remember as variable → `player_name`
- Show this question only when: Character mode (persona/world character) — is empty

**Start Question 2 — Species**
- Tipo: Species Picker
- Label: Species
- Help text: "What species is your character?"
- Required: off
- What this choice does: Remember as variable → `player_species`
- Show this question only when: Character mode (persona/world character) — is empty

**Start Question 3 — Occupation**
- Tipo: Occupation Picker
- Label: Occupation
- Help text: "What does your character do to make a living?"
- What this choice does: Remember as variable → `player_occupation` (nessun Grant currency: rimosso su correzione esplicita dell'utente, i compensi differenziati per lavoro vanno dentro le singole Lexicon entry di tipo Job, non su questa domanda)
- Show this question only when: Character mode (persona/world character) — is empty

**Start Question 4 — Starting Items**
- Tipo: Item Picker
- Label: Starting Items
- Help text: "Pick a couple of everyday items your character starts with."
- Pool: Wireless Earbuds, Keys, Wallet, Lighter, Smartphone
- Max selections: 2
- What this choice does: Activate as lore + Remember as variable (`player_items`)
- Show this question only when: Character mode (persona/world character) — is empty

**Start Question 5 — Backstory**
- Tipo: Text area
- Label: Backstory
- Help text: "Tell us a bit about your character's background, personality, and how they ended up here."
- What this choice does: Activate as lore
- Match rule: keyword "fight, fighter, fighting, underground fighting" → Remember key `player_fighter_flag` = `true`
- Show this question only when: Character mode (persona/world character) — is empty

**World intro opening (greeting, Handlebars)**:
```
The neon haze of Blackwood City drifts in from the shoreline as you step out into the warm California night.

{{#memExists "player_species"}}As a {{memGet "player_species_name"}}, {{/memExists}}{{#memExists "player_occupation"}}you make your living {{memGet "player_occupation_name"}}, {{/memExists}}and tonight the city does not care who you are, only what you are willing to do to get by in it.

{{#memExists "player_items"}}You pat your pockets out of habit and find what you always carry: {{memGet "player_items_name"}}.{{/memExists}}

{{#ifEquals (memGet "player_fighter_flag") "true"}}Somewhere beneath the city, in rooms with no windows and no rules, people already know your name.{{/ifEquals}}

Whoever you are and whatever brought you here, Blackwood City is waiting.
```

**Include Choose Your Character**: ON, roster limitato a Alyssa Douglas Bloodmoon + Jasper Douglas Bloodmoon
**Include Build Your Stats**: ON
**Show "Begin here" to players**: ON

**Stat templates**
- **"Alyssa (Caretaker Omega)"** — "A gentle, empathic build focused on presence and wits, for a soft-spoken caretaker persona. Low physical stats, high social and perceptive ones." — Might 1, Resilience 3, Agility 4, Wits 8, Presence 10, Scent 5 (da RPG Stats reali di Alyssa, Lv.19, 25/25 punti, Condition 183 / Control 48)
- **"Jasper (Beta Hacker)"** — "A quick, sharp build built for evasion and cleverness over brute force, for an agile hacker persona balanced across the board." — Might 3, Resilience 5, Agility 7, Wits 9, Presence 4, Scent 3 (da RPG Stats reali di Jasper, Lv.19, 25/25 punti, Condition 183 / Control 48)

**Persona preset — terzo triplet Douglas**: Rowan Douglas-Bloodmoon (Third Triplet), He/Him. Vedi versione precedente di questo file per la description completa (non ripetuta qui per brevità, invariata).

---

## NUOVO (31/08/2026 sera): RPG Blueprints — Species e Occupations abilitati

Scoperta chiave della sessione: i campi Species Picker e Occupation Picker nelle Start Questions richiedono contenuto reale nel sistema **RPG Blueprints** (World Editor → tab RPG → "Enable Species" / "Enable Occupations"), che è **completamente separato dal Lexicon**. Non basta avere le entry Lexicon corrispondenti.

**Stato RPG tab**:
- "Enable Species": ON (salvato e verificato con reload)
- "Enable Occupations": ON (salvato e verificato con reload)
- "Enable Traits": OFF (non richiesto dall'utente)

**Species Blueprints create** (9 totali, budget punti confermato dall'utente: **3 punti totali per specie**, non più 2 come nella bozza iniziale):

| Specie | Modificatori | Note |
|---|---|---|
| Human | nessuno | baseline |
| Vampire | AGI +2, PRS +1 | |
| Weres/Shapeshifters | MGT +2, SCT +1 | ex "Werewolf", rinominata |
| Demi-humans | AGI +2, SCT +1 | |
| Demons | MGT +2, PRS +1 | |
| Fae | WIT +2, PRS +1 | |
| Hybrids | MGT +1, AGI +1, WIT +1 | unica a 3 stat diverse invece di 2+1 |
| Undead | MGT +1, RES +2 | |
| Magic-capable Humans | WIT +2, PRS +1 | |

Lista allineata alla pagina ufficiale SUCC (`https://io-succ.uwu.ai/#species`), come richiesto dall'utente, essendo SUCC l'ambientazione esterna con precedenza di lore sul proprio materiale (regola #10 delle istruzioni di progetto).

**Occupations**: sistema abilitato ma non ancora popolato con una lista deliberata; esiste solo un'entry preesistente "Student" (nessun modificatore) trovata già presente nel World, non creata in questa sessione. Nessuna lista di occupazioni né logica di modificatori è stata ancora discussa con l'utente.

---

## Da fare (prossima sessione)

1. **Lexicon cleanup richiesto esplicitamente dall'utente, non ancora eseguito**: le 4 entry Lexicon categoria SPECIES esistenti (Demihumans, Humans, Vampires, Werewolves) vanno rimosse o ricategorizzate, assicurandosi che non siano mai di tipo "Creature" (altrimenti compaiono come creature acquistabili nel sistema separato Wyvern Creatures). Queste sono entry Lexicon pre-esistenti, distinte dalle nuove RPG Species Blueprints appena create.
2. Decidere una lista di Occupation RPG Blueprints (nessuna guidance ancora data dall'utente su quali occupazioni includere o su eventuali modificatori).
3. Creare la Lexicon entry Job "Douglas Family Allowance" ($500/settimana) — task riportato da sessioni precedenti, ancora non fatto.
4. Creare un secondo Scenario ("Character Creation" o nome simile) che rispecchi lo stesso questionario del World Introduction, per soddisfare la risposta "Entrambi" data dall'utente in precedenza.
5. Valutare se promuovere Rowan a personaggio giocabile standalone con card JED+ completa (solo su richiesta futura, non pianificato).

---

## Nota tecnica UI (per sessioni future che lavorano sulla pagina RPG del World Editor)

La pagina RPG Blueprints (Species/Occupations) ha comportamenti poco affidabili nel browser automation:
- Gli screenshot risultano spesso "stale" (mostrano lo stato prima dell'ultima azione); il modo più affidabile per verificare lo stato reale è `find` per il testo atteso, o un reload completo della pagina.
- Il pulsante "+Add" a volte riapre in edit un'entry esistente invece di creare un form vuoto, o un form "Create" mantiene testo residuo da un tentativo precedente. Prima di premere "Create"/"Save", verificare sempre via screenshot/read_page che i campi Name/Description corrispondano davvero all'entry che si intende creare.
- Le icone accanto a ogni riga sono solo due: un'icona "Create lore entry" (crea/collega una entry Lexicon collegata, **non** un'icona di modifica) e un cestino di eliminazione. Cliccare la riga o il nome apre il form di modifica, che si apre **in cima alla lista**, non accanto alla riga cliccata.
- Dopo ogni "Create"/"Save" cliccare a vuoto non basta: confermare sempre con `find` sul nome appena creato prima di procedere all'elemento successivo, e fare un reload completo a fine sessione di modifiche per verificare la persistenza reale lato server.
