# Regola 01 — Formato di Consegna e Standard JED+

## 1. Formato di Consegna: Testo, Non JSON

**Default assoluto:** Fornire sempre testo pronto da incollare nei campi del form dell'interfaccia Wyvern (`description`, `personality`, `first_mes`, `mes_example`, `system_prompt`, `post_history_instructions`, lorebook/NPC entries, outfit, tagline, shared info, ecc.), **NON** file JSON completi.

Il JSON va generato **esclusivamente** se:
1. L'utente lo richiede esplicitamente; oppure
2. Serve come riferimento tecnico per verificare la coerenza tra più campi complessi (in tal caso, chiedere prima conferma se l'utente preferisce il file JSON o solo il riepilogo testuale).

*Nota di sincronizzazione:* Il file JSON scaricato dall'utente **dopo** il salvataggio su Wyvern rappresenta il backup di archivio, non un artefatto che l'assistente deve mantenere sincronizzato in parallelo.

### Eccezioni Operative
- **Scrittura diretta sul World via API:** Quando l'assistente scrive direttamente sul World tramite API (vedi Regola 11), il testo non passa dalla chat campo per campo. In questo caso si consegna il **riepilogo** puntuale di cosa è stato scritto e dove, corredato dal documento di riepilogo nel Project con i valori precedenti dei campi modificati (snapshot di sicurezza).
- **Lavoro in locale su SQLite (sospeso dal 22/09):** Vale solo se l'utente riattiva esplicitamente il lavoro sul database locale di Wyldfire (vedi Regola 12). Il testo non passa dalla chat campo per campo, ma si consegna il riepilogo in un documento del Project.

---

## 2. JED+ Come Formato Standard delle Schede

Tutte le character card devono adottare rigorosamente il formato **JED+**:
1. Un blocco di attributi tra parentesi quadre, separati da punto e virgola (stile bracket/PList);
2. Seguito da sezioni in prosa per backstory, dinamiche familiari/di gruppo, voce/comportamento;
3. Chiusura con una sezione tematica centrale del personaggio.

### Struttura Standard JED+

```text
[NAME: ...; SPECIES: ...; AGE: ...; HEIGHT: ...; ... ]

BACKSTORY: ...

FAMILY & PACK: ...

VOICE & BEHAVIOR: ...

[sezione tematica finale, es. CORE TRAGEDY / THE WEIGHT HE CARRIES / THE SECRET HE CARRIES]
```

### Regole Specifiche per i Campi

- **Personaggi senza legame di branco:** Per figure aziendali, indipendenti o civili, la sezione `FAMILY & PACK:` si sostituisce con l'equivalente pertinente (es. `CLAN AND COMPANY:` per Zeera), mantenendo invariata la struttura a quattro blocchi più la chiusura tematica finale.
- **Campo `personality` (`summary` nell'interfaccia Wyvern):** Usa un blocco compatto di soli tratti tra parentesi quadre (stile PList puro), come riepilogo rapido e condensato, separato dalla `description` estesa.
- **Import Grezzi:** Una card importata grezza con il blocco `<nome_personaggio>` incollato tale e quale dalla fonte **NON è una scheda lavorata**. Va riscritta integralmente in JED+, non semplicemente ritoccata.
- **Età e Macro `{{age}}`:** Usare obbligatoriamente la macro `{{age}}` nel campo `AGE` del blocco JED+ di ogni personaggio che possiede una data di nascita, anziché il numero statico in chiaro (il numero statico invecchia e richiede correzioni a ogni avanzamento del World Clock). `summary` e `display_description` mantengono per ora l'età in chiaro per convenzione (coda aperta).
