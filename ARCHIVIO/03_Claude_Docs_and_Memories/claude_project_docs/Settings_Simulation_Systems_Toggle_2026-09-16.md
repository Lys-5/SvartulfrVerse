# Riattivazione toggle World Features — 16/09/2026

Fase 2 (Settings) del lavoro ordinato dall'utente il 16/09: dopo il fix/audit completo dei Content (vedi `Audit_SQL_Content_Fix_2026-09-16.md`), riattivati via UI Wyldfire i tre toggle esplicitamente richiesti.

## Cosa è stato fatto

- **Enable Relationships (Systems > Relationships): riattivato.** Era risultato OFF durante l'audit del 15/09 nonostante la canon precedente lo indicasse come l'unico sistema dovuto restare attivo dopo lo spegnimento della Simulation del 13/09. Sotto-impostazioni verificate intatte dopo la riattivazione: Persistent points ON, Moodlets ON, magnitudini Regular 5/8/24h e Severe 12/20/72h, tier ladder default a 14 livelli (Nemesis → Soulmate).
- **Inventory & Items e Currency & Economy (Simulation > World Features): riattivati.** Confermato che la configurazione preesistente non era andata persa durante lo spegnimento: 1 valuta (US Dollar), 5 marketplace (Administration, Bricklane Mall, Dockside, Medusa, The Verve, tutti a 0 listings), "AI-managed inventory" ON. La comparsa/scomparsa del tab "Economy" in sidebar segue il toggle ma non cancella i dati sottostanti, confermando lo stesso comportamento già documentato per le RPG Stats (§8/§15 istruzioni di progetto).
- **Non toccati:** RPG Stats (resta OFF, nessuna richiesta in merito), Combat System, Cross-World Ships, Creature Catcher.

## Nota di metodo — correzione di un mio errore nella stessa sessione

Durante la stesura di questa documentazione ho inizialmente scritto per errore un nuovo doc di Project chiamato `canon-decisions.md`, credendo di star aggiornando un file di canon già esistente con quel nome. In realtà il file di canon "Confirmed lore and system decisions" con quel nome vive nel filesystem di memoria personale (non nei doc di questo Project) ed è rimasto intatto e non toccato da questo errore: nessun contenuto è andato perso. Il doc spurio è stato rimosso e la nota sui toggle è stata invece aggiunta correttamente in coda al file di canon originale. Segnalato per trasparenza, nessuna azione ulteriore richiesta.
