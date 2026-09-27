# Verifica fonti Janitor AI per gli stub Fan OC — 16/09/2026

Su richiesta esplicita dell'utente ("tutti i personaggi"), applicata la nuova regola sui link 404 (vedi `Fonti_Aggiuntive_e_Regola_Char_404_2026-09-16.md`) all'intero roster Fan OC di `iofan.uwu.ai` (Students + Staff), cioè la fonte dei 313 stub creati in `Stub_FanOC_Creazione_313Schede_2026-09-15.md`.

## Metodo

Contrariamente a quanto documentato nel 15/09 (si pensava che la sezione Students non avesse link individuali), la rilettura via browser locale con estrazione DOM ha mostrato che **ogni nome sulla pagina ha in realtà un link Janitor AI reale** (attributo `href` su un tag `<a>` all'interno del blocco immagine di ciascuna card), per un totale di **318 link univoci** (Students + Staff insieme, deduplicati per UUID).

Verifica fatta con l'endpoint interno di Janitor (`GET /hampter/characters/<uuid>`, chiamato via `fetch` same-origin dalla pagina di janitorai.com per evitare il blocco CORS), che risponde in modo pulito:
- **200** con i dati del personaggio: scheda esistente.
- **404** `{"message":"cannot find character"}`: scheda non trovata. Verificato anche visitando direttamente una pagina 404 (title "Not Found", testo del sito: *"Oops. Can not find this character. It might be deleted or set to private. Status: 404"*), quindi il 404 copre sia la cancellazione sia l'impostazione a privato da parte dell'autore, i due casi non sono distinguibili dall'esterno.
- **401**: NON significa cancellato. Verificato su un caso reale (Kore Savariophai): la pagina carica normalmente con titolo e dati visibili, solo la sezione "Character Definition" risulta nascosta perché richiede autenticazione/età per contenuto ristretto. Questi casi sono stati esclusi dalla lista di cancellazione.

## Risultato

Dei 318 link verificati: **224 rispondono 200** (scheda esistente), **16 rispondono 401** (scheda esistente ma con contenuto ristretto, non è un candidato alla cancellazione), **78 rispondono 404**.

Dei 78 nomi in 404, **71 corrispondono a stub già creati nel World** (tag `["Stub", "Fan OC", "SUCC", "Students"]`, status `pending`), quindi sono **candidati alla cancellazione dal World** secondo la nuova regola:

Gary Newton Rogers, Ezekiel "Zeke" Azok, Damien Holt, Trip Vasiliadis, Ezra "Ez" Veyne, Dean Primrose, Seven, Carden Lewis Jr, Dustin Wagner, Kieran Lancaster, Chidori Hare, Adrian Wolfmoon, Gary Tucker, Chad Wagner, Crispin Hicks, Dakota Hunt, Devin, Kai Marino, Kian Nouri, Percy Moore, Tullio Ruzsa, Vendalath Rel'vos, Xanethar Rel'vos, Zahan Nouri, Max Halloway, Ellie Baker, Miron Romans, Ethan Primrose, Quinn Primrose, Silas Primrose, Emily Primrose, Melody Moore, Maddison Sanders, Lucian Scavis, Alo Leok, Marcus Bailey, Adrian 'Ari' Snowbanks, Emiliano 'Emilio' Sanchez, Harleen, Beatriz C. Silvester, Amir Hassan, Antonio Ricci, August, Elijah 'Eli' Snowbanks, Ember Knight, Calira Vireline, Taliah 'Tali' Rynor, Tyler Ito, Vornak Halton, Pom Clovis, Lior 'Lio' Halcyon, Chloe Rezal, Arlen Dove, Thera Veyne, Jake Reyonds, Han Doyun, Salum Azazel Crowe, Aya Seren, Mizuki Thoru, Maru, Daisy Lehto, Rusty Gardener, Domingo Escobar, Giselle Beaumont, Aster Hara, Nyx Belmont, Ryan Gallagher, Rose Fieran, Harlow Shea, Gethrir Holota, Monica VanAster-Sequoia.

Gli altri **7 nomi in 404 non hanno mai avuto uno stub nel World** (Professor Tipton, Rania Vega, Adonis Ness, Professor Vulkan, Kolvin Loughlin, Mowy "Moss" Movoud, Marcus Jacobs): comparivano nella sezione Staff della fonte ma non risultano fra i 23 stub Staff creati il 15/09, quindi con ogni probabilità sono nomi aggiunti alla pagina fan dopo quell'import, oggi già rimossi dall'autore. Nessuna azione necessaria, sono solo segnalati per completezza.

Confermato inoltre che i due casi di corrispondenza già noti restano intatti (non in 404): "Professor Reid" → Hideo Reid (200) e "Coach Coso" → Adelin Coso (200), entrambi già completi nel World, e "Professor Blackwood" (200, distinto da Roman Blackwood).

## Cosa NON è stato fatto

Nessuna cancellazione eseguita sul World. La regola dice di segnalare i candidati, non di eliminarli in automatico: trattandosi di un'azione distruttiva su 71 schede, resta da confermare con l'utente prima di procedere (backup + DELETE via script sul database locale Wyldfire, secondo §17).

## Nota sui 12 personaggi SUCC-U-Verse canon e sugli altri non-canon staff

Non ancora verificati in questo giro (fuori dallo scope di iofan.uwu.ai): i 12 Character con tag `SUCC-U-Verse` (Gabriel, Gianni Luciano, Nic Lucero, Levi Graham, Milo Grayson, Cyrus Camden, Vale Roberts, Julian Bieri, Rhett Moore, Jayce Collins, Emil, August Reed) provengono da `io-succ-char.uwu.ai`, non da iofan, e richiedono un controllo separato con lo stesso metodo se l'utente lo richiede.
