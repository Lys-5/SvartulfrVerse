# Piano Parent Location + Folder — 2026-09-21

## Batch Parent Location (34 item) — ✅ COMPLETATO
Tutti i 34 item dell'istruzione originale di Lys sono stati assegnati. Creati in questo processo:
- Location "Storage & Supplies" (parent: Supernatural University of Central California / SUCC — confermato da Lys: "è un edificio del campus quindi parent succ")
- Location "Library Basement Meeting Room 005"
- Environment "DDM Inc. // Voidspace" — description scritta usando `https://io-ddm.uwu.ai/#ddm` (consultato via browser, non fetch diretto, per §11 istruzioni progetto), verificata persistita dopo reload (196 token).

## Task richiesto 2026-09-21: "continua con le folder creandole e spostando le voci"

**Esito: parzialmente bloccato dallo stesso bug di piattaforma già documentato in `claude/Import_Plan_AllContent.md` (Task #6), riverificato oggi con metodo più rigoroso. Creazione folder possibile, spostamento voci esistenti no.**

### Stato reale dei folder Location (confermato da Lys, 21/09)
- `claude/Audit_Content_Folders_Completo_2026-09-13.md` (8/9 settembre) dava le Location per 118/118 già classificate in una tassonomia (Blackwood District, Blackwood Location, SUCC Location, Solarton Location, CUMS Location, Los Angeles Location, Bakersfield Location, DDM), verificata allora via scrittura/lettura diretta API.
- **Lys conferma oggi: "non c'è nessuna folder".** Quella tassonomia non esiste più lato Location (rimossa in un intervento successivo, persa per un bug, o l'audit di settembre non era rappresentativo — non indagabile a ritroso senza accesso API). **Si riparte da zero: nessuna folder Location da riusare, vanno create ex novo.**
- Il totale Location è salito comunque da 118 (8/9) a **134** oggi (16 in più, probabile lavoro di altre sessioni + le 2 create in questo batch).
- Coerentemente con "nessuna folder", la UI (tab "Locations" e "All Content") mostra sempre una lista piatta senza righe/header di folder e senza alcun toggle "raggruppa per folder" funzionante (provati: ordinamento Name/Priority/Position/Date, Table/Gallery view — Gallery raggruppa solo alfabeticamente, filtro "All Types").

### Il bottone "Move to folder" è confermato non funzionante
Testato sistematicamente sull'icona "Move to folder" (icona folder-input) accanto a un item nella vista "All Content":
- Click reale via coordinate (screenshot) → nessun effetto visibile.
- Click via `ref` (accessibility tree) → nessun effetto visibile.
- `btn.click()` nativo via JS → nessun effetto.
- Sequenza completa di eventi sintetici (pointerdown/mousedown/pointerup/mouseup/click) dispatchati al centro reale del bounding rect del bottone → nessun effetto.
- **Verifica definitiva**: `MutationObserver` sul `document.body` durante il click → **zero mutazioni DOM, zero nodi aggiunti**. Il gestore del click non produce alcun cambiamento osservabile nella pagina, quindi non è un problema di targeting/coordinate da parte nostra: il bottone stesso non apre nulla, per nessun metodo di click provato.

Questo è lo stesso bug già documentato in `Import_Plan_AllContent.md` §Task #6 per il bulk "Move items…", ma oggi risulta rotto anche per lo spostamento di un **singolo** item (in precedenza il dialog singolo almeno si apriva, pur essendo inaffidabile nel salvataggio — vedi caso Bianca Rossi). Possibile regressione della piattaforma nel frattempo. Non escluso che valga la pena di un test manuale da parte di Lys stessa (nel suo browser, sessione sua) per confermare che non sia un problema isolato alla sessione automatizzata — la prova MutationObserver è comunque una forte indicazione che il gestore dell'evento non fa nulla lato client, indipendentemente da chi clicca.

### Cosa è possibile fare comunque
- **Creare le folder da zero funziona** (dialog "New folder" testato: si apre correttamente, campo nome + Save).
- **Popolare una folder al momento della creazione** di un nuovo item funziona (pattern "New [tipo] here" dal menu contestuale di una folder, già usato con successo nel Task #7/#3 di Import_Plan_AllContent.md) — ma questo aiuta solo per item creati da ora in poi, non per i 134 esistenti.
- **Non è possibile spostare via UI nessuna Location esistente in una folder** una volta creata, incluse le 2 nuove di questo batch (Storage & Supplies, Library Basement Meeting Room 005).
- Nessuna scrittura è stata tentata via API/token (vincolo di sicurezza rispettato).

### Proposta per Lys
1. Posso creare subito la tassonomia di folder da zero (stessi nomi di settembre: Blackwood District, Blackwood Location, SUCC Location, Solarton Location, CUMS Location, Los Angeles Location, Bakersfield Location, DDM — o un'altra struttura se preferisce), così è pronta e le nuove Location da qui in avanti nascono già filate correttamente con "New Location here".
2. Lo spostamento dei 134 item esistenti resta bloccato lato UI. Opzioni: aspettare che il bug venga corretto lato piattaforma, provare lei stessa il bottone "Move to folder" per escludere che sia un problema solo di questa sessione, oppure — se vuole e mi autorizza esplicitamente — valutare un'eccezione mirata al vincolo sulle scritture API (sconsigliato di default, resta la mia raccomandazione di non farlo).
3. Posso segnalare il bug nel forum Discord `wyldfire-bugs-and-support`/`bugs-and-support` (§15 del progetto) includendo la prova MutationObserver come evidenza.

## Prossimo passo
In attesa di indicazione di Lys: procedo a creare la tassonomia di folder vuota (punto 1) mentre aspetto conferma sul resto, oppure aspetto anche per quello se preferisce decidere i nomi delle folder insieme.
