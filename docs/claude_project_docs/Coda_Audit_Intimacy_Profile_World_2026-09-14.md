# Audit Intimacy Profile su tutto il World — Eseguito 2026-09-14

Task originariamente messo in coda, eseguito in questa sessione su richiesta esplicita dell'utente ("esegui tutti questi task in sequenza").

## Metodo

Scan programmatico via API su tutti i 100 Character del World: ricerca di sezioni `INTIMACY:` ancora presenti per intero in `long_summary` (non ridotte a una riga sobria), con controllo incrociato contro le entry Lexicon `Intimacy Profile - <Nome>` già esistenti per capire se si trattava di un gap vero (nessuna entry) o di un residuo duplicato (entry già esistente ma testo mai tolto dalla description).

## Risultati

**Nessuna azione necessaria:**
- **Venera Dolce**: `long_summary` già corretto, la riga sobria rimanda esplicitamente al Lexicon ("A fuller Intimacy Profile is filed separately in the Lexicon rather than spelled out here"). Nessuna modifica.

**Residuo duplicato, solo trim (entry Lexicon già esistente, paragrafo tolto da `long_summary`):**
- **Erik Douglas** (`_T3dPxjPxmHT4EDcfkba8M`): entry `Intimacy Profile - Erik` (`_8Q2GxtDA3XxG3JWj1Yhzz`) già copriva il materiale. Paragrafo completo su Rut/partner occasionali rimosso da `long_summary`, sostituito con riga sobria.
- **Stanley Davies Jr.** (`_pQ3yQbxftjhxUVWUk4m2Y`): entry `Intimacy Profile - Stanley Davies Jr.` (`_2GwpeqbErmVYgnM4NJMm4`) già copriva il materiale, incluse misure esplicite. Paragrafo completo rimosso da `long_summary`, sostituito con riga sobria.

**Gap veri, nuova entry Lexicon creata + trim di `long_summary` (8 personaggi):**
- **Ariadne Cirillo** (`_hXBqkLzmdXTyk6yYVHM6y`) → `_FCYPEx6BtFgtATNftac86`
- **Hank Thompson** (`_rVQar74BBgmFYmFCNAeW9`) → `_r6CnQ8N4YxKkwDdCLRRAU`
- **Janice Thompson** (`_dWMHLU3NXycVDDCtMHyrD`) → `_yghQCq1f22Vx2wLzU9TYb`
- **Jared Thompson** (`_1JhayQC7pzY6TC4qRHTx9`) → `_7xcyttCnBfBqc8bFYz7dy`
- **Nikolaj Jökull** (`_nLhHajTB2D1NAKwpGRT3g`) → `_QHWM9FkMA72phVpyzNmj7`
- **Oskar** (`_YtPgeD9TaQBxz9xjRdPyJ`) → `_zkqmEgMRr7Dmpg3rnGbGW`
- **Stanley Davies Sr.** (`_Ww6aaR4bVeB18RHjDHTKU`) → `_gJ1TKqyaqRhbj7dW6AHnp`
- **Tate** (`_DYmRyAw642RbzLF4EzPBL`) → `_n6mXzqTaNp1U446JpF8Df`

Tutte e 8 le nuove entry seguono il formato standard §13.3: `type: "memory"`, `is_global: true`, `keys` sul nome del personaggio, `secondary_keys` standard, `key_logic: "AND_ANY"`, `priority: 50`, `party_conditions` `has_any` sul proprietario, `attached_world_character_id` impostato. Contenuto in prosa, ricavato dal paragrafo `INTIMACY:` già presente in `long_summary` (nessun fatto nuovo inventato), con le misure anatomiche numeriche convertite in descrittori qualitativi per coerenza con il registro prosa (vedi §13.3, "senza misure anatomiche numeriche esplicite" per lo stile prosa), a differenza dello stile a blocchi (es. Stanley Davies Jr., Erik) dove le misure numeriche restano perché già presenti in quel formato.

Insieme a Eris Davies e Jasmin Thompson (fixati separatamente, vedi `Eris_Jasmin_Completamento_2026-09-13.md`), questo chiude tutti i casi rilevati dallo scan automatico di paragrafi `INTIMACY:` estesi (>300 caratteri) ancora incollati per intero in `long_summary`.

## Limiti dello scan

Lo scan si basa sulla stringa letterale `INTIMACY:` nel `long_summary`. Non copre:
- Personaggi con materiale intimo sostanziale scritto senza quell'etichetta esplicita (possibile ma non verificato in questa passata).
- Gli altri buchi sistemici già noti da audit precedenti (display_description, Start Position, format discipline, Default Outfit mancanti) su porzioni del roster mai auditate sistematicamente insieme a questo controllo.

Se in futuro serve un controllo più esteso, va fatta una lettura mirata (non solo grep su "INTIMACY:") dei personaggi ad alta frequenza di scena ancora non coperti da un Intimacy Profile esplicito, e un audit di completezza pipeline unificato su tutto il roster (modello: `Audit_Completezza_SUCC_2026-09-13.md`), non ancora fatto per Los Angeles/Blackwood/District Council nel loro complesso.

## Verifica

Tutte le 10 schede modificate verificate dopo GET fresca: paragrafo `INTIMACY:` esteso assente, riga sobria presente, zero `{{user}}`/em-dash/grassetto. Tutte le 8 nuove entry Lexicon verificate dopo GET fresca: `is_global: true`, `party_conditions` puntato al personaggio corretto, zero `{{user}}`/em-dash/grassetto.

## Stato

Chiuso per lo scope "paragrafi INTIMACY: ancora inline". Resta aperto, se richiesto in futuro, un audit di completezza pipeline più ampio su Los Angeles/Blackwood/Concilio (vedi limiti sopra).
