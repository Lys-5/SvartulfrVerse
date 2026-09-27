# Regola 03 — Outfits, Accessori e Coerenza Visiva

## 1. Evitare Oggetti e Tratti "Sempre Visibili"

*Lezione empirica:* Qualunque accessorio o tratto scritto come "always on" o "never removed" nella description (es. le bende di Malachia, i tatuaggi di Logan, catena/anello/occhiali di Erik) induce l'LLM in loop rigidi, costringendolo a inserire l'elemento anche in scene prive di senso (piscina, doccia, cene formali, situazioni intime).

**Regola operativa:** Se un elemento visivo o un accessorio non è strutturalmente fuso con il corpo del personaggio, non deve essere descritto come costante. Adottare una delle due opzioni (in ordine di priorità):

1. **Sistema Outfit Nativo di Wyvern (Soluzione preferita):** Utilizzare la sezione *Appearance & Outfits* configurando outfit distinti e contestuali (es. Allenamento, Casa/Casual, Formale, Tattico, Notturno).
2. **Descrizione Contestuale:** Se il sistema Outfit non è ancora popolato per quella card, specificare il tratto come strettamente contestuale nella prosa della description:
   > *"X indossa Y solo quando si trova in Z; in altri contesti non è presente."*

**Eccezione Ammessa:** Un tratto può restare costante se e solo se la sua costanza è l'essenza stessa dell'identità del personaggio e la scheda lo dichiara apertamente (es. il cappuccio di Dullahan non scende mai, in nessun contesto, costituendo il fulcro della sua identità). In tal caso va dichiarato costante e ribadito in tutti gli outfit.

---

## 2. Coerenza Visiva della Famiglia Douglas

Scelta stilistica canonica approvata: i maschi della famiglia Douglas condividono un "family look" riconoscibile nelle generazioni e nei prompt visivi:
- Capelli scuri, lunghi e arruffati (conformazione necessaria ad accomodare le orecchie da lupo del Partial Shift);
- Palette calda al tramonto e sfondo/ambientazione di Blackwood City (palme, architettura costiera);
- Struttura facciale affine e marcata.

*Nota:* Mantenere comunque elementi distintivi propri per ciascun membro (motivi e stile dei tatuaggi, cicatrici, accessori contestuali, tonalità degli occhi). Rispettare questa coerenza visiva nella stesura dei campi `visual_description` e Shared Info.

---

## 3. Anatomia Demi-Umani: Orecchie Singole

**I demi-umani possiedono un solo paio di orecchie: quelle animali.**
Non hanno orecchie umane aggiuntive sotto la chioma. Questa regola anatomica è confermata dall'autore dell'ambientazione originale (che evidenzia come i generatori di immagini tendano costantemente a sbagliare generando quattro orecchie).

- Verificare tassativamente questa caratteristica su ogni immagine o descrizione anatomica prima dell'approvazione.
