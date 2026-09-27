# Wyldfire desktop: verifica di cosa c'è davvero in una scheda

Verifica del 2026-09-07, in due passaggi: interrogazione diretta del database
locale, poi ispezione visiva dell'app aprendo una scheda reale.

**Conclusione: non manca quasi niente. Quello che sembrava perso c'è, ed è anche
visualizzato correttamente.** Il controllo precedente era quasi certamente stato
fatto mentre l'app stava ancora riscaricando il World: la sincronizzazione si è
chiusa alle **00:01 del 7 settembre**.

---

## Prova sul campo: scheda di Andrew Campbell aperta nell'app

Tutto quello che risultava sparito è presente e a schermo:

| Elemento | Stato nell'app |
|---|---|
| **Start Position** | `10538088`, esattamente il valore impostato |
| **Birthdate** | `-191280`, con la traduzione leggibile "March 7, 778" |
| **Pronomi** | presenti: he / him / his / his / himself |
| **Outfit** | tutti e cinque, con dettagli e Trigger Conditions |
| **Dialogue Examples** | 5 |
| **Attitudes / Relationships** | 5 |
| **RPG Stats** | abilitate, badge **Lv.22** |
| Nickname, titoli, keys, long_summary, summary | tutti presenti |

Il campo **Pronoun Set** in cima mostra "Select pronoun set" e sembra vuoto, ma
subito sotto la scheda elenca i pronomi correnti. È un preset non selezionato,
non un dato mancante: **quello è il falso allarme più facile da prendere**.

---

## Riscontro sul database, che conferma

I conteggi dei campi popolati combaciano con quello che sappiamo di aver
scritto, il che prova che il download è fedele:

| Campo | Presenti su 86 | Riscontro |
|---|---|---|
| `attitudes` | 36 | **identico all'audit del 3 settembre** |
| `outfits` | 39 | identico al censimento |
| `rpg_stats` | 38 | identico |
| `long_summary` | 61 | 86 meno le 25 schede grezze |
| `birthdate` | 44 | le schede lavorate |
| `pronouns` | 43 | idem |
| `summary` | 86 | completo |

Anche la configurazione del World è al suo posto: **star date**
(`human_start_date` = `0800-01-01`), **Stat Definitions** (2029 caratteri, tutte
e sei le stat), **Relationships** (enabled, persistent, moodlets, magnitudes),
Economy, InfoBoard, calendario, fasce orarie. Nulla di tutto questo è da rifare.

---

## Quello che manca davvero

**1. Global Character è spento su 85 schede su 86.** Confermato sia nel database
sia nell'app, dove il toggle di Andrew è visibilmente off. La regola di progetto
§7 dice che va **ON per tutti**: probabilmente era l'intenzione, non lo stato
effettivo. È la cosa più importante da sistemare, perché un Character non globale
è attivo solo dove è stato piazzato, e i Character Pool non li abbiamo popolati.

**2. Species e Occupation, 0 su 86.** È il bug di piattaforma già noto (§15): non
persistono nemmeno sul web. Non è un problema di download e non si risolve
reinserendoli.

**3. Writing Style & Tone.** `base_instructions` e `final_instructions` del World
sono vuoti. È quasi certamente il blocco che mancava in Simulation, e va scritto:
presente, terza persona, asterischi solo per i pensieri, backtick per i testi
scritti, virgolette per i dialoghi.

**4. Traits, Combat ruleset, Creature settings:** vuoti. Da capire se erano stati
compilati o se non li abbiamo mai fatti.

**5. Default Outfit non impostato.** Sulla scheda di Andrew l'app avvisa "Please
select a default outfit". Vale la pena controllarlo sulle 39 schede con outfit.

---

## Conseguenza pratica

**L'allarme rientra: non c'è niente da ricostruire da zero.** Le voci che
l'ispezione dava per "VOID da rifare completamente", cioè Relationships, Stat
Definitions ed Economy, sono popolate. Prima di rifare qualunque cosa conviene
riaprirla nell'app adesso che il download è concluso.

Resta valida una sola cautela: **l'app va ricontrollata dopo che la
sincronizzazione è finita**, non durante. Un controllo fatto a metà download
mostra esattamente il quadro che abbiamo visto stanotte, cioè campi vuoti che
vuoti non sono.
