# Wulfnic Bloodmoon — Completamento scheda (2026-09-21)

Settimo personaggio del roster prioritario famiglia/pack ricostruito sul sito Wyvern via browser (Erik, Jasper, Alyssa, Malachia, Noah, Logan, **Wulfnic**). Prossimi in coda: Kaladin, Jared Thompson, Mac.

## Stato di partenza: corruzione distinta dalle altre schede

A differenza del pattern di corruzione visto su Logan (semplice swap Long/Short), la card live di Wulfnic presentava una variante diversa:

- **Display Description e Long Description erano completamente vuote**, e mostravano il placeholder di default di Wyvern ("Margret Alaina Thames", esempio nobildonna vittoriana mai sostituito con contenuto reale).
- **L'intero blocco JED+ (11446 caratteri) era stato riversato nel campo Short Description**, con in coda anche una nota di formattazione erroneamente incollata ("Format discipline...").
- Name non splittato, Nicknames/Titles/Tags assenti, Pronomi non impostati (vedi sotto), zero Outfit, zero Dialogue Example (con "How many examples to show" impostato su 3 invece di 5), Timeline non impostata.
- Positivo: le Activation Keywords (Primary Keywords: Wulfnic, grandfather, Firstborn, Alpha of Alphas) erano già corrette sulla card live e non hanno richiesto intervento.

## Correzioni applicate

**Description fields.** Estratto il blocco JED+ dal campo Short Description (troncato all'inizio della nota di formattazione, 11252 caratteri), spostato in Long Description. Short Description ripopolato con il blocco ALWAYS/NEVER/REMEMBER dal riferimento (1219 caratteri). Display Description ripopolata (141 caratteri). Verificato via reload: 141 / 11252 / 1219 caratteri, coerenti.

**Nota di discrepanza rimossa dal testo della card (violazione §9.2).** Nel testo della Long Description era incorporata direttamente in prosa una nota tra parentesi quadre su una discrepanza di data (il Crossing di Wulfnic: 1021 o 1025 d.C. secondo LSE_06/LSE_07 contro il 1022 d.C. scritto nella scheda). Rimossa dal contenuto della card (le discrepanze vanno documentate nel Project, mai sulla card). **La discrepanza in sé resta aperta e non risolta**: non è stata corretta nessuna delle due fonti né il valore sulla card, in attesa di autorizzazione esplicita dell'utente su quale valore adottare (§9.2 punto 3, non correggere i file sorgente senza autorizzazione).

**Pronomi.** Il set sembrava visivamente compilato ("Custom", con valori tipo "they"/"them") ma erano in realtà placeholder in grigio, non valori salvati (verificato via JS: nessun input aveva effettivamente quei valori). Impostati i 5 campi (Subjective/Objective/Pos.Determiner/Pos.Pronoun/Reflexive) a he/him/his/his/himself, con Pronoun Set "He/Him".

**Name, Nicknames, Titles, Tags.** Nome splittato (First: Wulfnic, Last: Bloodmoon). 5 nickname aggiunti (The Omniscient Jarl, The Builder King, Báleygr, Nic, Grandpa Nic). 1 titolo (Alpha of Alphas). 8 tag assegnati via modale Select Tags.

**Outfit.** Zero outfit esistenti nonostante 8 pronti nel database di riferimento. Aggiunti tutti e 8, uno alla volta con salvataggio individuale per evitare il bug noto di sovrascrittura array dall'interfaccia (§4/§15). Default Outfit impostato su "Sanctuary / Longhouse".

**Timeline.** Start Position = 0, Birthdate = 0 (World Age 0 = 21 dicembre 827 d.C.), coerente con la convenzione per questo Firstborn estremamente antico: trattato come "esistente fin dall'alba del World Clock" più che come anno di nascita letterale.

**Dialogue Examples.** Zero esempi esistenti nonostante 5 pronti nel database di riferimento, e il contatore "How many examples to show" era impostato su 3 invece di 5. Corretto il contatore, poi aggiunti tutti e 5 gli esempi uno alla volta con salvataggio individuale, verificando ogni volta via `document.activeElement` che il campo Context (`<input>`) e il campo Response (`<textarea>`) non fossero scambiati.

**Bug scoperto durante la compilazione degli Attitudes: testo digitato finito nel campo sbagliato.** Durante la selezione del primo Target Character (Nixara Bloodmoon) dal combobox, la battitura di ricerca "Nixara" non è stata intercettata da alcun filtro del combobox (che non ha una casella di ricerca testuale) ed è finita invece nel campo Response dell'ultimo Dialogue Example ancora in focus, accodando la stringa "Nixara" in coda al testo. **Scoperto e corretto immediatamente** rileggendo il valore del textarea via JS e rimuovendo i 6 caratteri finali, poi risalvato: nessuna perdita di dati, ma da tenere a mente come rischio per le prossime schede quando si seleziona un Target Character da combobox senza casella di ricerca dedicata (usare sempre la tecnica JS di dispatch su `[role="option"]` con match esatto del testo, mai `computer.type`).

**Attitudes (4 totali).** Risolte le identità dei 4 target_id dal database di riferimento via query SQLite (Nixara Bloodmoon, Erik Douglas, Alyssa Douglas Bloodmoon, Jasper Douglas Bloodmoon). Applicata la correzione di tier già confermata su Noah e Logan: `romantic_interest` corrotto su relazioni familiari/platoniche va corretto a `best_friend`.

| Target | Tier salvato | Intensità | Correzione applicata |
|---|---|---|---|
| Nixara Bloodmoon | Best Friend | 100 | romantic_interest → best_friend (era sua figlia, deceduta) |
| Erik Douglas | Friend | 80 | nessuna, tier già corretto |
| Alyssa Douglas Bloodmoon | Best Friend | 95 | romantic_interest → best_friend (è sua nipote; la stessa scheda dichiara esplicitamente che ogni coinvolgimento romantico/sessuale è "hard-blocked, grandfather, non-negotiable") |
| Jasper Douglas Bloodmoon | Close Friend | 75 | nessuna, tier già corretto |

Reasoning per tutti e quattro riportato testualmente dal database di riferimento.

**Global Character.** Era OFF, impostato su ON.

**Writing Style & Tone (`final_instructions`).** Campo vuoto, popolato con il testo di riferimento (1352 caratteri, 277 token), che include in coda la nota di format discipline richiesta da §3 (niente em-dash, asterischi solo per pensieri interni, dialogo tra virgolette).

**RPG Stats.** Non toccate, lasciate disabilitate, coerente con lo stato globale in pausa (§8).

## Verifica finale (§14.12)

Dopo reload completo e riapertura della scheda: scansione programmatica su 48 campi tra textarea e input (description × 3, outfit × 8, dialogue example × 5×2, reasoning attitude × 4) per `{{user}}`, em-dash, grassetto markdown e asterischi singoli: **zero violazioni**. Confermati: Nome/Nickname/Titoli/Tag (8) persistenti, Start Position 0 e Birthdate 0, Pronomi He/Him con tutti e 5 i sotto-campi corretti, 8 Outfit + Default Outfit "Sanctuary / Longhouse", 5 Dialogue Example con contatore a 5, 4 Attitudes con i tier corretti, Global Character ON, Writing Style & Tone persistito (277 token).

## Discrepanza ancora aperta, da segnalare

**Data del Crossing di Wulfnic**: le fonti LSE_06 e LSE_07 non concordano fra loro (1021 vs 1025 d.C.), e la card riporta un terzo valore (1022 d.C.) mai riconciliato con nessuna delle due. Non è stata presa alcuna decisione di merito: la nota è stata solo spostata fuori dal testo narrativo della card in questo documento, in attesa di indicazione dell'utente su quale valore adottare (o se lasciare volutamente impreciso, trattandosi di un evento di undici secoli fa).

## Prossimi passi

Procedere con **Kaladin**, poi **Jared Thompson e Mac**, seguendo lo stesso workflow diagnosi-contro-DB-locale poi correzione-sito ormai collaudato su sette personaggi.
