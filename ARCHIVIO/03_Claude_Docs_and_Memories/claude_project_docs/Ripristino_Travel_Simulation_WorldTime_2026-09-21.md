# Ripristino dati World: Travel Routes, Simulation Toggles, World Time Span — 2026-09-21

Seguito diretto di `Audit_Ripristino_Dati_2026-09-21.md`. Lys ha risposto punto per punto ai 5 elementi segnalati nell'audit; questo documento chiude i tre che richiedevano un'azione (2, 4, 5) e registra perché gli altri due (1, 3) non ne richiedevano.

---

## 1. Environments (13→2): NESSUNA AZIONE

Confermato da Lys: non è una perdita di dati. I 13 Environment originali sono stati deliberatamente spostati in Location in una sessione precedente. Il contenuto di `Wyvern/environments.md` (fonte sincronizzata da GitHub) non va quindi ricreato come Environment: se serve, vive già dentro le Location corrispondenti sul World live.

## 2. Travel Routes: RIPRISTINATE (5 rotte)

La tab Travel era completamente vuota (0 rotte). Lys ha chiesto di ricreare la linea del traghetto **e in più** aggiungere delle rotte autostradali, non richieste nell'audit originale.

Scritte via UI (nessun accesso API diretto usato, come da regola §11 del progetto), verificate dopo reload completo della pagina:

| From | To | Ore | Mezzo | Note |
|---|---|---|---|---|
| Dockside Ferry Landing | Hex Valley Ferry Stop | 24 | water | Prima tratta del traghetto Passenger Ferry Solarton Line |
| Hex Valley Ferry Stop | Solarton Ferry Terminal | 24 | water | Seconda tratta, arrivo alla Bay Area alla foce dello Yarrow |
| Solarton | Blackwood City | 2 | land | Autostradale, la "corta guidata" già citata nel World Info |
| Solarton | Ventura / Route 101 | 1 | land | Tratto Solarton del corridoio 101 verso sud |
| Ventura / Route 101 | Los Angeles | 2 | land | Prosecuzione del corridoio 101 fino a LA |

**Fonti usate per il traghetto:** `World_Modifiche_Da_Applicare.md` (le 4 Location create per la linea, "un giorno pieno per tratta"), `Mappe_Style_Bible_E_Prompt.md` (geografia dello Yarrow che vincola il tracciato Dockside→Hex Valley→Solarton), `SUCC_Setting_Canon.md` (dettagli operativi dello scalo di Hex Valley).

**Decisione presa per le rotte autostradali (proposta, non esplicitamente confermata da Lys prima della scrittura — vedi §9.7 del progetto, segnalato qui per eventuale correzione):** Lys ha chiesto solo "quelle autostradali" senza specificare quali coppie di Location. Ho dedotto due tratte dal materiale già canon:

- **Solarton ↔ Blackwood City**: il World Info del World descrive esplicitamente Solarton come "a short drive away" da Blackwood, e `World_Modifiche_Da_Applicare.md` contrappone il traghetto lento alla "101" più veloce per lo stesso tragitto concettuale (Blackwood-Solarton). 2 ore è una stima ragionevole per una "corta guidata", non verificata a fonte.
- **Solarton ↔ Ventura/Route 101 ↔ Los Angeles**: la Location "Ventura / Route 101" esiste già nel World come lo snodo di transito costiero che "collega Solarton a Los Angeles" (fonte: `Wyvern/environments.md`). Ho spezzato il collegamento in due rotte passando per quella Location intermedia, invece di un salto diretto Solarton-LA, per rispettare la geografia già scritta. Tempi (1h e 2h) sono stime plausibili non verificate a fonte, coerenti con "a short drive"/corridoio costiero.

**Da confermare con Lys se le tratte o i tempi non sono quelli intesi.** Nessun altro dettaglio è stato inventato oltre a questi numeri di ore.

## 3. Relationships tier ladder: NESSUNA AZIONE (bassa priorità)

Confermato da Lys come a bassa priorità, lasciato con i valori di default della piattaforma (Nemesis/Enemy/Despised/.../Soulmate) invece della ladder LSE-themed. Resta un gap noto per un'eventuale sessione futura.

## 4. World Features toggles: RIPRISTINATI

Trovati accesi: Inventory & Items, Currency & Economy, Party Stats in Prompt, Relationships (oltre a Relationships, che doveva restare l'unico attivo per la decisione del 13/09).

Disattivati via UI: Inventory & Items, Currency & Economy, Party Stats in Prompt. Lasciato acceso solo **Relationships**, in linea con `Simulation_World_Features_Disattivate_2026-09-13.md`.

**Verificato dopo reload completo** (query DOM diretta sui checkbox, non solo `get_page_text`): degli 8 toggle, solo l'ultimo (Relationships) risulta `checked: true`, tutti gli altri `false`. Stato confermato persistito.

## 5. World Time Span: NESSUNA AZIONE, IL VALORE ERA GIÀ CORRETTO

Qui l'audit precedente aveva un errore da correggere, non il World.

Il campo mostrava "1197 years, 1 month, 1 day, 6 hours documented", segnalato come discrepanza contro un valore di "1249 years" verificato il 13/09. Ricalcolando il valore grezzo effettivamente salvato (`world_age: 10486470`) con l'epoca del World (0827-12-21T00:00:00Z, calendario gregoriano proletico), il risultato è **esattamente 2024-04-05T06:00:00Z**, cioè **5 aprile 2024, ore 06:00**: lo stesso valore che il progetto stesso documenta al §6 come "riconfermato via API il 14 settembre".

In altre parole: la riverifica del 14/09 (successiva e più autorevole di quella del 13/09) aveva già corretto il valore, e il World in vivo riflette correttamente quella riverifica. Il "1249 years" del 13/09 era il dato superato, non il "1197 years" attuale. **Non ho quindi toccato questo campo.** Se Lys ha in mente un valore diverso da 10486470 (5 aprile 2024), va chiarito esplicitamente, perché al momento il World è coerente con la propria stessa documentazione più recente.

---

## Riepilogo azioni

- Travel Routes: 5 rotte create e salvate, verificate dopo reload.
- Simulation → World Features: 3 toggle spenti, 1 lasciato acceso, verificato dopo reload.
- World Time Span: nessuna modifica, segnalato come falso allarme nell'audit precedente.
- Environments e Relationships tier ladder: nessuna azione, come da istruzione di Lys.

## Aperto

- Le rotte autostradali (tempi di percorrenza e scelta esatta delle coppie Solarton-Blackwood e Solarton-Ventura-LA) sono una proposta motivata ma non confermata parola per parola da Lys prima della scrittura. Da rivedere se non corrispondono a quanto intendeva.
