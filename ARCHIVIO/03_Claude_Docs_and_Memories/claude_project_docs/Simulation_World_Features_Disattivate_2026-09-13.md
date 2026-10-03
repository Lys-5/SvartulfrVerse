# Simulation: disattivati tutti i sistemi tranne Relationships (2026-09-13)

## Decisione dell'utente

Dopo test diretti sul World, l'utente ha riscontrato che il sistema di Simulation funziona male e ha deciso di disattivare tutto tranne Relationships:

- Inventory & Items: OFF
- Currency & Economy: OFF
- RPG Stats: OFF
- Combat System: OFF
- Cross-World Ships: OFF
- Creature Catcher: OFF
- Party Stats in Prompt: OFF
- Relationships: ON

## Verifica sul World via API

Letto `GET /api/worlds/<world_id>` e ispezionato il campo `world_features` (più `relationship_config.enabled`). Stato trovato, già coincidente con quanto richiesto:

```
world_features: {
  combat: false,
  currency: false,
  inventory: false,
  rpg_stats: false,
  ships: false,
  show_party_stats: false
}
relationship_config.enabled: true
```

Nessuna scrittura è stata necessaria: il World risultava già configurato esattamente come richiesto (l'utente lo aveva evidentemente già impostato dall'interfaccia durante i test, prima di scrivermi).

**Creature Catcher non esiste come campo nello schema di questo World** (nessuna occorrenza di "creature" nell'intero oggetto World restituito dall'API). Non c'è quindi nulla da disattivare per questa voce lato dati: o non è un feature applicabile a questo World, o non è ancora esposta su questo World nello schema attuale della piattaforma. Segnalato qui per tracciabilità, non è un problema aperto da risolvere.

## Implicazione per la pipeline di card (§8, §14.8)

Con `rpg_stats: false` a livello World, il sistema RPG Stats risulta disattivato globalmente, anche se i singoli Character continuano ad avere il proprio blocco `rpg_stats` (stat, livello, Species, Occupation) salvato e intatto sulla scheda. La pipeline standard §14 passo 8 (abilitare RPG Stats, distribuire i 25 punti, assegnare Species/Occupation via API) resta descritta nelle istruzioni di progetto, ma **il suo effetto in gioco è sospeso finché l'utente non riattiva `rpg_stats` a livello World**. I dati già scritti sulle card non vanno persi né rimossi: restano pronti per quando/se il sistema verrà riattivato.

## Decisione finale: passo RPG Stats in pausa

L'utente ha confermato: **il passo §14.8 (RPG Stats) va messo in pausa** sulle nuove card, finché non decide di riattivare il sistema a livello World. Da questo momento, nella pipeline standard §14 su nuovi personaggi:

- Si salta il passo 8 (distribuzione punti, Livello, Species/Occupation via API) finché non arriva indicazione contraria.
- Gli altri passi della pipeline restano invariati (JED+, outfit, Start/End Position, Dialogue Examples, Attitudes, Global Character, verifica finale).
- Le card già completate con RPG Stats popolate **non vengono toccate**: i dati restano sulla scheda, semplicemente inattivi lato gioco finché il toggle World resta OFF.
- Se in futuro l'utente riattiva `rpg_stats` a livello World, il passo 8 torna attivo per le card ancora da fare, e si può valutare se completare retroattivamente quelle saltate nel frattempo.

## Rilettura del 2026-09-14: regola ancora valida, ma non seguita per una sessione

Rifatto `GET /api/worlds/<world_id>` il 14 settembre: `world_features.rpg_stats` è ancora **false**. La regola sopra è quindi tuttora corretta e non necessitava aggiornamenti di contenuto, ma **non è stata seguita** durante il lavoro sul Concilio di Blackwood dello stesso giorno, perché questo documento non era stato riletto prima di iniziare: sono stati popolati RPG Stats (Livello, Species, e dove pertinente Occupation) su sei schede nuove o riviste in quella sessione, **Zeera**, **Harlan "Huck" Beaumont**, **Naomi Black**, **Darius Vale**, **Marcus "Mark" O'Connor**, e la revisione di **Vito Marino** (oltre a impostare per la prima volta i suoi RPG Stats, mai fatti nella build originale).

Come previsto da questo stesso documento, non è stato necessario disfare nulla: i dati restano sulle schede, semplicemente inattivi lato gioco finché il toggle resta OFF. Da questo punto in avanti, il passo §14.8 torna a essere saltato di default su ogni nuova scheda del Concilio ancora da fare, salvo diversa indicazione dell'utente.
