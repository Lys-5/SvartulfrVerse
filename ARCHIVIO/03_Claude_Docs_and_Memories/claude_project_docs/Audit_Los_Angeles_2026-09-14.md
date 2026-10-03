# Audit cartella Los Angeles (21 personaggi) — 2026-09-14

Stato di partenza, verificato via GET diretto su tutti e 21 gli ID della cartella "Los Angeles".

## 4 personaggi con pipeline parzialmente avviata

**Rafael Callaway, Kade Leavis, Graham Purcell, Miles Airhardt**: hanno già `long_summary` in JED+ inglese e alcuni outfit (4-5), ma mancano `display_description`, `speech_examples` (0 per tutti e 4), `final_instructions`, e `attitudes` (0 tranne Miles Airhardt che ne ha 4). Miles Airhardt ha inoltre residui di italiano nel `long_summary` da ripulire. Servono solo completamento pipeline, non riscrittura.

## 17 personaggi: solo import grezzo JanitorAI, mai lavorati

Tutti e 17 hanno **zero** `long_summary`: il campo `summary` contiene ancora il testo grezzo di importazione in stile JanitorAI (blocco `Name/Class/Demographics/Appearance/Personality/Background/Relationships/Dialogue`, in alcuni casi ancora dentro tag `<nome>...</nome>`), esattamente il caso descritto in §2 ("una scheda importata grezza... non è una scheda lavorata"). Nessuno ha outfit, dialogue examples, attitudes, o final_instructions.

Elenco e nucleo narrativo di ciascuno, dal testo grezzo:

**Famiglia DeVille / entourage:**
- **Alistair DeVille**: umano, art collector e crime lord, 63 anni, gestisce una galleria a NYC come copertura per traffico di reperti, cerca il "Dawnstar" (gemma dell'immortalità). Speciesista dichiarato verso i non umani ma con inclinazioni Dom/kink proprio verso tratti non umani (corna/code). Figlio Charles, ex moglie Amelia, bodyguard Cato.
- **Cato**: demiumano alligatore, ex mercenario, bodyguard di Alistair, lealtà puramente transazionale.

**Sindacato "The Sinners" (i Sette Peccati, rivali di Rory Ballantine):**
- **PRIDE - Jean-Luc Virtuoso**: telepate, leader dei Sinners, produce e distribuisce Ambrosia (narcotico magico), odio personale verso Rory Ballantine.
- **Alicia Virtuoso**: moglie di Jean-Luc, ex modella, matrimonio di convenienza, indifferente al crimine del marito.
- **SLOTH - Arthur**: chimera/chimico, cuoco dell'Ambrosia, esausto e cinico.
- **GLUTTONY - Kevin**: umano, hacker, 22 anni, tratteggiato con tropi "incel" pesanti (dipendenza da porno/videogiochi, tre "fidanzate" soprannaturali che lo sfruttano economicamente).
- **WRATH - Zero**: coyote shifter, sicario, infanzia abusiva, odio primordiale verso Danny Boone.
- **ENVY - Siobhan**: vampira, spymaster, manipolatrice, tratteggiata con satira pesante su attivismo performativo ("social justice warrior" che odia gli umani ma se ne serve).
- **GREED - Roxie**: demiumana iena, trafficante d'armi, caotica e violenta.
- **LUST - Dante**: incubo, gestisce un locale/bordello, iper-sessuale e bisognoso di validazione.

**Cerchia di Rory Ballantine (rivale dei Sinners):**
- **Ruaraidh "Rory" Ballantine**: demiumano drago, crime lord, CEO di un'importazione, cresciuto a Glasgow, sterile, ha "adottato" Sully/Harper/Danny come famiglia scelta.
- **Sullivan "Sully" Jones**: umano, ex braccio destro di Rory, autista/bodyguard, tre divorzi, cane St. Bernard.
- **Daniel "Danny" Boone**: licantropo enforcer, salvato da Rory da un ring di combattimento, dislessico/analfabeta, orecchie e coda sempre visibili (nota: da verificare con §5, "un solo paio di orecchie" per i demiumani).
- **Harper Aries**: dhampir, spacciatrice, dipendente da Ambrosia per sopprimere gli istinti, orfana adottata da Rory.

**Indipendenti:**
- **Everett Rottmore**: umano maledetto, fixer/becchino, maschera scheletrica sempre indossata (da valutare secondo §4 se costante ammessa o da rendere contestuale), disperato per una cura.
- **Damien Bishop**: demone, detective privato, nasconde gli occhi da demone con occhiali da sole.
- **Vasile Ionescu**: umano, cacciatore di criptidi, vende esemplari vivi a collezionisti, gestisce uno "zoo" di mostri in gabbia, temi Dom/bondage con framing possessivo ("appartieni a me, nessun altro ti tocca, mai").

## Punti che richiedono una decisione prima di procedere

1. **Scala**: 17 personaggi da costruire da zero (non completare, costruire), lo stesso volume di lavoro degli "8 fully custom" più i "6 cross-reference" della sessione precedente messi insieme, ma qui senza schede già in buono stato da cui partire.
2. **Materiale sensibile**: diversi personaggi hanno tratti che il §13 tratta già per altri casi (Alistair è esplicitamente speciesista/suprematista verso i non umani; Vasile ha framing dubcon-adjacent di possesso; Kevin è scritto con tropi incel/misoginia satirica; Siobhan con satira su attivismo). Questi tratti sono caratterizzazione del personaggio (un antagonista scritto per essere un antagonista), non contenuto rivolto a `{{user}}`, quindi §13 non si applica direttamente, ma vanno scritti con lo stesso criterio già usato altrove nel World: la caratterizzazione resta, i blocchi anatomici/kink espliciti vanno isolati in un Intimacy Profile separato (§7) con `party_conditions` sul proprietario, non nella description.
3. **Attitudes incrociate interne**: il testo grezzo descrive già una fitta rete di rapporti tra questi 17 (Jean-Luc-Siobhan, Zero-Danny odio reciproco, Roxie-Kevin, Dante-Siobhan, Rory-Sully-Harper-Danny come famiglia scelta, Alistair-Cato, DeVille-Ballantine rivalità di fondo). Andranno tutte incrociate e scritte reciprocamente, non solo verso Alyssa/Jasper.
4. **Everett Rottmore, maschera sempre indossata**: possibile eccezione ammessa per §4 (come il cappuccio di Dullahan) se la scheda lo rende esplicito, da confermare.

## Stato

Nessuna scrittura ancora effettuata su questi 17. In attesa di indicazioni dell'utente su ordine di lavorazione e gestione dei contenuti sensibili prima di procedere, data la scala del lavoro.
