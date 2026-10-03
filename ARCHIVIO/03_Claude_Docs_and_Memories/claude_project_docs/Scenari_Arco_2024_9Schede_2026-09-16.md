# Revisione completa degli scenari (arco 2024) — 16/09/2026

Su richiesta dell'utente: "gli scenari sono tutti da rivedere post modifiche alla lore", seguita dall'arco completo di 9 eventi datati da costruire/correggere. Lavoro fatto in locale sul database Wyldfire (§17), world_id `6cfuc64QBr1Flf9nKndFy`.

## L'arco completo, in ordine cronologico

| # | Data | Evento | Scenario | Stato |
|---|---|---|---|---|
| 1 | Dom 7 apr 2024 | Erik chiede ai gemelli cosa vogliono fare | **What Do You Want To Do** | Corretto (era 5 apr, venerdì) |
| 2 | Sab 13 apr 2024 | Open Day alla SUCC | **Open Day alla SUCC** | Nuovo |
| 3 | Lun 22 apr 2024 | Compleanno 19 anni | **Diciannove Anni** | Nuovo |
| 4 | Lun 10 - dom 23 giu 2024 | Road Trip con Logan | **Road Trip con Logan** | Nuovo (scena di partenza) |
| 5 | Sab 27 lug 2024 | DJ Frequency | **DJ Frequency** | Nuovo, ricostruito da zero dopo il materiale fonte di Jasper |
| 6 | Lun 26 ago 2024 | Primo giorno di college | **First College Day** | Invariato, data già corretta |
| 7 | Lun 2 set 2024 | Primo incontro con Jared Thompson | **Primo Incontro con Jared Thompson** | Nuovo, riscritto sulla voce autentica di Jared fornita dall'utente |
| 8 | Sab 14 set 2024 | Concerto Grave Mistake / primo incontro con Mac | **Ciao, Sono Logan** | Corretto (era 20 set, venerdì; tolta l'ambiguità sul "primo incontro") |
| 9 | Gio 31 ott 2024 | Halloween | **Halloween alla Theta Iota Theta** | Nuovo, con l'aggancio di Jared integrato |

## Correzioni sugli scenari esistenti

**"What Do You Want To Do"**: spostato dal 5 al 7 aprile (venerdì → domenica). Effetto a catena nel testo: "fra diciassette giorni" (compleanno) corretto in "quindici giorni", "fra ventisei giorni" (scadenza del primo maggio) corretto in "ventiquattro giorni". Il `world_age` attuale del World (10486470, cioè 5 aprile 2024 06:00) resta quindi due giorni prima di questo scenario: già così per First College Day e Ciao Sono Logan, quindi coerente con come il World gestisce gli scenari come "avanti" rispetto al puntatore corrente.

**"Ciao, Sono Logan"**: spostato dal 20 al 14 settembre (venerdì → sabato), "quattro settimane" di college corretto in "tre settimane" (19 giorni da lunedì 26 agosto). **Correzione più profonda, chiarita dall'utente durante la sessione**: questo scenario non è mai stato il primo incontro con Logan, ma il primo incontro con **Mac (Mackenzie Sanchez-Rogers)**. La battuta di chiusura di Logan ("Ciao. Sono Logan. Suo zio.") era scritta come una rivelazione, il che contraddiceva il Road Trip di giugno dove i gemelli passano tredici giorni con lui. Riscritta come una battuta di routine ("Logan. Suo zio. Sì, ancora io.") che presume familiarità pregressa, non una prima presentazione. Mac resta l'unico vero "primo incontro" della serata.

## Il caso DJ Frequency: cambio di scenario completo

La lista originale dell'utente descriveva l'evento del 27-28 luglio come "rave in spiaggia". La prima versione che ho scritto seguiva quella lettura: famiglia/amici (Alyssa, Jasper, Noah, Logan) sulla spiaggia pubblica di Solarton.

L'utente ha poi fornito il materiale fonte reale del personaggio di Jasper per questa scena, che descrive tutt'altro: Jasper si intrufola da solo in un rave underground in un **magazzino a Los Angeles**, in tenuta da incognito, usando un terminale di hacking fatto in casa per falsificare la sua posizione GPS e aggirare la rete di sicurezza di suo padre, che stava per mandare una squadra a "salvarlo". Nessuno al rave sa chi sia davvero.

Confermato con l'utente prima di scrivere: **vale la versione del magazzino**, non la spiaggia. La persona che Jasper incontra nel vicolo alla fine della scena non è stata identificata: lasciata generica, senza nome, per non inventare un'identità che l'utente non ha specificato. Creata una nuova Location, "Magazzino di DJ Frequency" (ambiente Los Angeles), visto che non esisteva ancora una Location per un rave underground in un magazzino. Lo scenario ha `playable_character_ids` vuoto (nessuno dei due gemelli forzato come protagonista giocabile: qui il personaggio guidato dall'IA è Jasper stesso).

## Il caso Jared Thompson: voce riscritta sulla fonte autentica

L'utente ha fornito il materiale fonte originale della card di Jared per il primo incontro (2 settembre) e per Halloween (31 ottobre), in inglese, con `{{user}}` e contenuto esplicito/anatomico. Ho riscritto entrambe le scene in italiano seguendo §13 e §3:

- `{{user}}` sostituito con **Alyssa** per nome, non generalizzato: qui è legittimo perché lo scenario ha un cast fisso e specifico (a differenza dei campi di scheda di Jared, che restano scritti in modo generico per qualunque giocatore).
- Tolto il contenuto anatomico esplicito ("dodici pollici", il "lil' Jared" che si eccita) e il "panty-dropping smile": la battuta corny resta ("Sei una ciotola di caramelle... hai un'aria che si mangia volentieri"), il contenuto grafico no. Se in futuro serve un Intimacy Profile per Jared, quel materiale è il punto di partenza corretto per spostarcelo, non per la scena stessa.
- Mantenuta la voce originale del personaggio: rozzo, da bullo sportivo, mezzo minotauro, diretto. Adattata in italiano con un registro equivalente (qualche "cazzo", niente di più greve del tono già presente altrove nel World, es. Noah in "Rave in Spiaggia"/Mac in "Ciao Sono Logan").
- Mai usato l'em-dash, presente più volte nel testo originale inglese.
- Integrato Jared come presenza fissa nello scenario di Halloween (non solo nel primo incontro), coerente con l'arco: si sono già conosciuti il 2 settembre, quindi ad Halloween la scena è un secondo approccio, non un'altra prima volta.

## Dettagli tecnici comuni a tutti i 9 scenari

- Nessun `{{user}}`, em-dash, asterisco o grassetto markdown residuo (verificato via script, un giro di pulizia ha tolto il grassetto `**data**` che era già presente per convenzione nell'intestazione di ogni scena, incluse le due scritte prima di questa sessione).
- `insertion_point` calcolato con la formula del World Clock (§6, epoca 21 dicembre 827), coerente ora e data della scena.
- Location ed Environment scelti fra quelli già esistenti nel World dove possibile (Villa Douglas, Lunar Quad, The Verve, Bulls Stadium, Theta Iota Theta, Sidewinders); creata una sola Location nuova (il magazzino di Los Angeles per DJ Frequency).
- RPG Build non incluso (`include_rpg_build: 0`), coerente con il toggle RPG Stats ancora spento (§8).
- Cast verificato contro il World: nessun personaggio purgato nella pulizia 404/401 di questa sessione compare in questi scenari.

## Verifica e sync

Backup pre-scrittura: `wyldfire.db.backup7-prescenari-<timestamp>`. Scrittura via script Python/sqlite3 (mai a mano). Verifica mirata (non `PRAGMA integrity_check`, che fallisce per la corruzione preesistente non correlata di `app_settings`): conteggio scenari 3 → 9, conteggio location 119 → 120, controllo programmatico dell'assenza di em-dash/asterischi/`{{user}}`/markdown su tutti i `premade_scenes`. Sincronizzazione sul dispositivo confermata con l'utente (app chiusa) prima del trasferimento.
