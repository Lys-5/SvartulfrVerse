# Risoluzione delle 5 anomalie dello sweep Entry Type — 2026-09-22

Seguito diretto di `Lexicon_Entry_Type_Sweep_Completo_2026-09-22.md`. Lys ha chiesto di risolvere tutte e cinque le anomalie segnalate. Fatto via API, tutto verificato con GET fresca finale.

## 1. ZZ DEBUG PROBE — eliminata

`_BtDkQkyfbUJ3j6zddVL3c` cancellata (DELETE, 204). Era un'entry di test/debug marcata dallo stesso nome come da cancellare.

## 2. Duplicati fusi

- **Vax**: due entry con lo stesso nome. Tenuta `_j3Wbr6w8QeCWpdQ41eRNh` (la versione più ricca, su clan/cultura/decadenza demografica), arricchita con i dati fisici generali dell'altra (altezza, longevità, corno spezzato come marchio d'esilio) **senza** portare il dettaglio anatomico esplicito della copia eliminata: quel contenuto resta comunque coperto, in registro biologico non grafico, dalla entry dedicata "Vax - Reproduction and Compatibility" (§7). Eliminata `_FQp9r4NrLP4nJqpC1YcwF`.
- **The Roasted Bean**: due entry. Tenuta `_pFUMj4B4BBnLkfEqJBykg` (menu, aree, staff), aggiunto in coda il dettaglio unico dell'altra (i Douglas-Bloodmoon lì il primo giorno di scuola). Eliminata `_2b47cJ3UN8fRxPMNbwjk1`.

Verificato via GET fresca: una sola entry "Vax" e una sola "The Roasted Bean" nel World.

## 3. is_global corretto sulle meccaniche riproduttive esplicite

`LSE Reproduction & Bonding` (`_Ng3NHdfmDgd9enpHh8hLh`) e `Vax - Reproduction and Compatibility` (`_gbWtWqyLgadDA6QAkReCm`): `is_global` portato da `true` a `false`, coerente con §7 (il contenuto è esplicito, quindi non deve più "sparare ovunque nel World" via scansione globale a parole chiave; resta comunque accessibile includendola in Location/Environment/Scenario pertinenti se serve).

## 4. Species_Details trasferite nelle rispettive schede

Le tre entry "Species_Details - Malachia/Logan/Erik" erano stub JED+ vecchi e generici (blocco attributi grezzo tipo `[NAME: ...; TABOOS: killing pack, rejecting shift; ...]`). Confrontate con le card attuali dei tre personaggi: **quasi tutto il contenuto era già superato** dalle card vere, molto più specifiche (es. i TABOOS reali di Malachia riguardano Nixara e sua sorella, non il generico "killing pack" dello stub). L'unico dato genuinamente mancante era la fisiologia di specie generica (battito cardiaco doppio durante lo shift, soglia del dolore alta, guarigione accelerata sotto la luna, sensi iperacuti, andatura digitigrada) e la debolezza esplicita a argento/aconito, assenti dalle tre card.

Aggiunta a tutte e tre le card, in coda al blocco attributi `[...]` di `long_summary`, la stessa riga: `PHYSIOLOGY_SHIFT: dual-heart rate active during shift, high pain threshold, healing accelerates under moonlight, hyper-acute senses, digitigrade stance in hybrid form; WEAKNESSES: silver (burning, poisoning), wolfsbane`. Verificato via GET fresca su tutte e tre.

Le tre entry Lexicon "Species_Details - X" eliminate dopo il trasferimento (erano comunque una violazione di §7: "Species_Details del personaggio proprietario → Non importare, già parte della card collegata").

## 5. Vargus, Bartholomew and Madge, Angui convertiti in Character

Creati **quattro** nuovi Character (Bartholomew e Madge erano due persone in un'unica entry, quindi due schede separate, non una):

| Nome | id | Note |
|---|---|---|
| Vargus "The Red" | `_c9yC2E2TcPx6KLUQQXUnm` | Scheda volutamente compatta: la fonte era un solo paragrafo (membro degli Ironhorn Nomads, legame fraterno con Barrow). Non ho inventato dettagli mancanti (età, altezza, backstory estesa) per riempire, come da §9.4. |
| Bartholomew | `_egd2NVErGy86WFbyzRJfK` | ACE soulbound di Dullahan, maggiordomo a DDM Headquarters. |
| Madge | `_YpKdVLTX16pLrUDb6a1ra` | ACE soulbound di Dullahan, governante a DDM Headquarters. |
| Angui | `_RTVEcAQpeX94kV8QFtGGg` | Creatura di palude, isolata, nessun legame con Blackwood. **Attribuzione preservata**: la entry originale portava un credito esplicito ("character created by Oreo, io-modernfantasy/SUCC-U-Verse collective, posted under Iorveths/veseii") — riportato in una nota tra parentesi quadre in coda a `long_summary`, come richiesto da §10 per il materiale copiato alla lettera da un'altra ambientazione. |

Tutte e quattro: JED+ completo (blocco attributi + BACKSTORY + sezione famiglia/gruppo equivalente + VOICE & BEHAVIOR + chiusura tematica), `summary` in PList, `display_description`, `final_instructions` con la disciplina di formattazione di §3, `is_global: true`, `world_only: false`.

Le tre entry Lexicon originali (Vargus, Bartholomew and Madge, Angui) eliminate dopo la conversione, per evitare il doppione Character+Lexicon che §7 vieta esplicitamente.

**Non fatto oggi, pipeline incompleta per tutti e quattro** (stesso standard già segnalato per Marek): Outfit, Dialogue Examples, Attitudes verso Alyssa/Jasper (almeno stranger/15), pronomi, Start Position/Era (calcolata dal World Clock, §6, non ancora impostata), RPG Stats (in pausa di default, §8). Questi quattro personaggi sono minori/di contorno quindi la pipeline completa può aspettare una sessione dedicata se e quando servirà farli comparire attivamente in scena.

## Verifica finale

GET fresca su Lexicon e Character del World dopo tutte le operazioni:
- Lexicon: 253 → **244** (−9: debug probe, 2 duplicati fusi, 3 Species_Details, 3 NPC convertiti in Character)
- Character: 360 → **364** (+4: Vargus, Bartholomew, Madge, Angui)
- Una sola entry "Vax" e una sola "The Roasted Bean" rimaste
- Nessuna delle sette entry da eliminare/fondere/convertire risulta più presente in Lexicon
- Tutti e quattro i nuovi Character esistono con `is_global: true`

Nessun fallimento di scrittura o cancellazione su tutta l'operazione.
