# Allineamento dei capi distretto Blackwood alla gerarchia LSE (Pack Leader) — 2026-09-14

Su richiesta dell'utente: rivedere il gruppo dei "District Alpha" di Blackwood per allinearli alla gerarchia di `LSE_04_Governance.md`, dove il titolo corretto per chi guida un branco è **Pack Leader**, non "Alpha". Nel documento fonte: *"At the top of the pack's chain of command... Does not need to be an Alpha — can be any secondary sex."* "Alpha" nel canon LSE è una classifica di secondo sesso, un asse separato dall'autorità di branco, esattamente come già stabilito per la famiglia Douglas in `Ruoli_Branco_E_Casa_E_Pulizia_Formato.md` (Erik è Pack Leader, non "Alpha" come titolo).

## Chi è stato toccato

Dei 9 personaggi della cartella Blackwood, **7 sono effettivamente capi di distretto** e rientravano nel problema: Vito Marino, Bianca Rossi, Aurora Night, Cass Harrow, Eclipse Noir, Isobel Blackwater, Dominic Chen. Angelo Moreno (imprenditore vampiro, non governa un distretto) e Riki Savini (rappresentante dei lupi solitari, non un capo di branco) sono rimasti invariati, correttamente fuori da questo gruppo.

## Cosa è cambiato, per ciascuno dei 7

- **`long_summary`**: aggiunto un campo `PACK_ROLE: Pack Leader` nel blocco JED+, subito dopo `SPECIES`, con lo stesso pattern già usato per Erik, Malachia, Wulfnic eccetera. La riga `ROLE:` è stata riscritta da "District Alpha of X" a "Pack Leader of X" (mantenendo il resto della frase, es. "Fashion negotiator and Pack Leader of Paradise East"). Anche i riferimenti in prosa nel corpo del testo ("Like every District Alpha of Blackwood City...") sono stati aggiornati a "Pack Leader".
- **`summary`**: stesso trattamento sul blocco compatto.
- **`display_description`**: "Alpha of X" era usato come scorciatoia per "capo di X", che rinforzava proprio la confusione fra il titolo di governo e la classe di secondo sesso. Riscritto in "Pack Leader of X" per tutti e 7.
- **`titles`**: da `["District Alpha, X"]` a `["Pack Leader, X"]`.
- **`keys`**: la keyword `District Alpha` è stata sostituita con `Pack Leader`.
- **`outfits`**: due nomi di outfit erano letteralmente "District Alpha Summit" (Aurora, Eclipse) e "District Alpha Mediation" (Dominic), rinominati "Pack Leader Summit" / "Pack Leader Mediation"; le descrizioni che menzionavano "other District Alphas" sono state corrette.
- **`speech_examples`**: tre `prompt` di scena menzionavano "District Alpha" (Dominic, Eclipse, Isobel), corretti allo stesso modo. Le `response` in-character non contenevano il termine.

**Cosa non è stato toccato**: `SPECIES: Werewolf, Alpha (Pureblood)` resta invariato ovunque, perché lì "Alpha" è correttamente la classificazione di secondo sesso del personaggio, un asse distinto da `PACK_ROLE`, esattamente come vuole il canon LSE (i due assi non vanno confusi, ma nemmeno entrambi cancellati).

## Nota su Cass Harrow

Cass co-regge Uptown North con Naomi Black, che non esiste come Character nel World (già annotato nella sessione precedente). Non essendoci una seconda scheda a cui assegnare un ruolo di branco, il `PACK_ROLE: Pack Leader` di Cass resta scritto al singolare con la co-reggenza spiegata in prosa nella riga `ROLE`, senza inventare una struttura Right Hand/Left Hand per una persona che non è ancora una entry del World.

## Verifica

GET diretto su tutti e 7 dopo un reload completo di pagina: zero occorrenze residue della stringa "District Alpha" in qualunque campo, `PACK_ROLE: Pack Leader` presente nel `long_summary` di tutti e 7, `titles` aggiornati, outfit ancora a 5 con default valido, zero em-dash, zero grassetto markdown.

## Nota canon aggiuntiva (2026-09-14, precisazione dell'utente)

Il Pack Leader **non deve** essere un Alpha per LSE (asse di secondo sesso separato, vedi sopra), **ma nel 95% dei casi lo è**. Non è quindi un errore che tutti e 7 i Pack Leader di distretto finora costruiti abbiano `SPECIES: ..., Alpha` — è la norma statistica, non un'incoerenza da correggere. Resta però aperto uno spazio narrativo legittimo per un Pack Leader di distretto che non sia un Alpha (il 5% eccezionale): se emergerà un personaggio così tra i quattro ancora da creare (Naomi Black, Darius Vale, Marcus O'Connor) o tra futuri sviluppi, non va scartato come errore ma trattato come la rara eccezione prevista dal canon.

## Stato

Punto aperto chiuso su richiesta esplicita dell'utente. La cartella Los Angeles resta in attesa di materiale sorgente aggiuntivo da parte dell'utente per i 17 personaggi ancora da costruire (vedi `Audit_Los_Angeles_2026-09-14.md`), quindi il lavoro si è spostato su questo allineamento di Blackwood nel frattempo.
