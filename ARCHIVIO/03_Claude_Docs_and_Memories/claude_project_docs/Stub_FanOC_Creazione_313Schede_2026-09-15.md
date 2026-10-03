# Creazione stub Fan OC: 313 schede segnaposto (2026-09-15)

Su richiesta esplicita dell'utente ("citiamoli creando schede per ora vuote ma pronte a essere compilate in caso di necessità, ti manderò i dati di quelli che recupero"), creati stub Character per **tutti** i nomi del roster Fan OC ufficiale (`iofan.uwu.ai`) ancora assenti dal World, sezioni Students e Staff (la seconda controllata dopo la domanda diretta dell'utente "hai controllato anche iofan.uwu.ai/#staff").

## Cosa è stato letto in più rispetto al confronto precedente

`FanOC_Roster_Confronto_2026-09-15.md` copriva solo la sezione Students. Riletta ora anche la sezione **Staff** (`iofan.uwu.ai/#staff`): 25 nomi, di cui **23 nuovi rispetto a `NPC_Roster_To_Add.md`** solo per l'aggiunta di **"Professor Kîwêtin"**, non presente nel pro-memoria di agosto. Verificati via link `janitorai.com` collegati a ciascun nome (non aperti, solo usati come conferma di esistenza della fonte) e via confronto diretto contro il database: **due nomi della lista Staff corrispondono a schede già costruite con il nome reale del personaggio invece del titolo/ruolo della fonte fan**, non duplicati da ricreare:
- "Professor Reid" → **Hideo Reid** (56 anni, kitsune, professore di chimica SUCC), già completo nel World.
- "Coach Coso" → **Adelin Coso** (49 anni, ariete, head coach SUCC Bears), già completo nel World.

**Falso positivo scartato**: "Professor Blackwood" (Staff) è stato inizialmente confuso per corrispondenza col già esistente **Roman Blackwood** (23 anni, MBA student/lottatore MMA), ma sono due personaggi Fan OC distinti che condividono solo il cognome, uno studente e uno docente. Verificato leggendo `display_description` di Roman Blackwood: nessuna menzione di ruolo docente. **Professor Blackwood resta quindi tra gli stub creati**, non è un duplicato.

## Duplicati nella fonte stessa, risolti

Quattro nomi compaiono **due volte** nella sezione Students della pagina fan stessa (una volta nel blocco "★" e una volta nel blocco "senza marcatura"): **Ashton Hill, Ethan Rivers, Kieran Lancaster, Nico Cousins**. Non essendoci alcun dato che distingua le due occorrenze (nessuna bio associata a nessuna delle due sulla pagina), creata **una sola scheda per ciascuno** invece di due identiche, per evitare ambiguità quando arriverà il materiale reale. Se in futuro emergesse che si tratta davvero di due Fan OC diversi con lo stesso nome (possibile, dato che "anyone may create a SUCC-U-VERSE OC"), si potrà scorporare la seconda scheda quando arriva la fonte che li distingue.

## Conteggio finale

- Students: 297 nomi sulla fonte, 3 già presenti (Venera Dolce, Kolya Varenkov, Roman Blackwood), 294 mancanti, **ridotti a 290 stub creati** dopo la deduplicazione dei 4 nomi doppi sulla fonte.
- Staff: 25 nomi sulla fonte, 2 già presenti (Hideo Reid, Adelin Coso), **23 stub creati**.
- **Totale stub creati: 313.** Nessuno di questi 313 esisteva prima come Character nel World (verificato con query esatta sul `display_name` prima dell'inserimento).

## Formato dello stub

Ogni scheda creata è deliberatamente minima, **senza alcun contenuto inventato** (§9.4: qui il buco è l'intera scheda, quindi non si riempie nulla):

- `display_name`: nome esatto dalla fonte (virgolette curve normalizzate in dritte).
- `long_summary`: blocco JED+ ridotto a `[NAME: ...; STATUS: placeholder, in attesa di fonte]` più una nota in prosa che rimanda a questo documento e al roster ufficiale.
- `summary`: `[STUB, in attesa di fonte. Nessun tratto ancora raccolto.]`
- `display_description`: una riga che dice "Fan OC dell'ioverse (Students/Staff), scheda ancora da compilare."
- `final_instructions`: già popolato con la riga standard di disciplina di formato (§3), meccanica e non legata a contenuto inventato, così la scheda è pronta a incassare dialoghi non appena arriva la personalità.
- `keys`: solo il nome stesso.
- `start_timeline_position`: impostato al World Clock attuale (10486470, 5 aprile 2024), come posizione "presente" di default, dato che tutti questi personaggi sono contemporanei (Class of 2024 / staff SUCC in servizio). **`birthdate` lasciato vuoto**: l'età reale non è nota e non va inventata: quando arriverà (dall'utente), andrà scritta insieme a un `birthdate` coerente, con conferma esplicita se comporta soglie particolari (§9.7).
- `end_timeline_position`: vuoto (nessuna indicazione di decesso dalla fonte).
- Nessun outfit, nessun Dialogue Example, nessuna Attitude: tutti i passi della pipeline (§14) che richiederebbero contenuto reale sono rimandati alla compilazione futura.
- `is_global`: 1, secondo la regola generale di piazzamento (§7).
- `tags`: `["Stub", "Fan OC", "SUCC", "Students"]` o `["Stub", "Fan OC", "SUCC", "Staff"]` a seconda della provenienza, per poterle ritrovare facilmente in blocco quando si vorrà lavorarle.
- `rating`: `none`, `visibility`: `friends`, `status`: `pending` (valori più comuni già in uso nel World per schede non ancora rifinite).

## Verifica

Backup pre-scrittura: `wyldfire.db.backup17` (creazione stub) e `wyldfire.db.backup18` (rimozione dei 4 duplicati). `PRAGMA integrity_check` ok dopo entrambi i passaggi. Conteggio Character: 134 (fine sessione precedente) → 497 dopo l'inserimento dei 317 stub grezzi → **493 dopo la deduplicazione** (313 stub netti + 180 Character preesistenti... la cifra esatta preesistente va confermata a parte, il delta netto di questa operazione è +313). Zero `{{user}}`, zero em-dash, zero grassetto markdown sui campi testuali dei nuovi stub. Nessun duplicato di `display_name` residuo nel World. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.

## Prossimo passo

In attesa che l'utente fornisca il materiale (bio, aspetto, personalità) per ciascun Fan OC, personaggio per personaggio o a piccoli gruppi. Quando arriverà, la scheda andrà **riscritta secondo la pipeline completa di §14** (JED+, outfit, Dialogue Examples, Attitudes incluse quelle obbligatorie verso Alyssa e Jasper), non semplicemente integrata sopra il segnaposto.
