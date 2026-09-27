# Audit completo content_folders, tutti i tipi (2026-09-13)

Su richiesta dell'utente, dopo aver confermato che il move delle voci Lexicon funziona (vedi `Bug_Wyvern_Stato_Segnalazioni_E_Workaround_Species.md` §0), controllo esteso a **tutti i tipi di contenuto del World**, non solo Lexicon: presenza in una cartella (nessun elemento orfano/non classificato) e correttezza della cartella assegnata (nessun elemento nella cartella sbagliata).

## Metodo

Per ogni tipo (`characters`, `locations`, `environments`, `lexicon`, `scenarios`):

1. Confronto fra la lista completa via `GET /api/worlds/<tipo>/world/<world_id>` e gli `entry_ids` di tutte le cartelle di quel tipo in `content_folders`, per trovare elementi non presenti in nessuna cartella.
2. Ricerca di **id orfani**: id presenti in una cartella ma che non corrispondono a nessun elemento realmente esistente (probabile residuo di elementi cancellati senza pulizia del riferimento).
3. Ricerca di **duplicati**: stesso id presente in più cartelle dello stesso tipo.
4. Per i tipi con cartelle a base geografica/di ambientazione (Lexicon: Houses & Bloodlines/Blackwood City/SUCC Campus/DDM; Locations: Blackwood District/Blackwood Location/SUCC Location/Solarton Location/CUMS Location/Los Angeles Location/Bakersfield Location/DDM; Characters: Family/Pack/Blackwood/Solarton/Los Angeles), scansione euristica per parole chiave di dominio (Douglas/Blackwood/Bloodmoon vs SUCC/Solarton vs CUMS vs Los Angeles/Underworld vs DDM/Voidspace) per trovare elementi il cui contenuto non menziona affatto il dominio della cartella in cui si trovano ma menziona chiaramente un dominio diverso.

## Risultati

**Elementi non classificati (prima dell'intervento):** solo le 22 voci Lexicon "Uncategorized" già trattate in precedenza, di cui 21 riclassificate e 1 lasciata fuori di proposito (DEBUG PROBE, da cancellare). Nessun elemento non classificato trovato in Characters (92/92), Locations (118/118), Environments (13/13), Scenarios (3/3): erano già tutti in una cartella.

**Id orfani trovati e rimossi** (residui di elementi cancellati, riferimenti rimasti nelle cartelle):

- Characters → cartella "Solarton": 1 id orfano rimosso.
- Locations → cartelle "Blackwood District" e "Blackwood Location": 1 id orfano ciascuna, 2 in totale, rimossi.
- Scenarios → cartella "Canon": 1 id orfano rimosso.

Nessun orfano in Lexicon o Environments.

**Duplicati (stesso elemento in più cartelle dello stesso tipo):** nessuno trovato, in nessun tipo.

**Errori di classificazione trovati con la scansione euristica:** **1**, in Lexicon.

- **"Anti-Vampire Legislation"** era in **Blackwood City** ma il contenuto parla esclusivamente di Solarton, SUCC, CUMS e della Vampire/Undead Alliance, zero menzioni di Blackwood o dei Douglas. **Spostata in SUCC Campus.**

Nessuna anomalia di dominio trovata in Locations (118 elementi scansionati) né in Characters (92 elementi scansionati, cartelle Family/Pack/Blackwood trattate come un unico dominio Blackwood/Douglas contro Solarton e Los Angeles).

## Scritture effettuate

Tre PUT parziali su `content_folders` del World (rimozione dei 4 id orfani, spostamento di "Anti-Vampire Legislation"), tutte via API. **Verificato dopo reload completo della pagina**: 0 non classificati (a parte il DEBUG PROBE lasciato apposta), 0 orfani, 0 duplicati su tutti e cinque i tipi, "Anti-Vampire Legislation" confermata dentro "SUCC Campus".

## Nota sul metodo di rilevamento

La scansione per parole chiave è euristica: individua solo i casi in cui un elemento non menziona affatto il dominio della propria cartella mentre menziona chiaramente un dominio diverso. Non è una garanzia assoluta di correttezza tematica fine (per esempio non rileva un elemento messo nella sotto-cartella sbagliata all'interno dello stesso dominio, tipo Blackwood District vs Blackwood Location), ma è un controllo ragionevole per gli errori più grossi, cioè un contenuto finito nel dominio geografico sbagliato. Nessun'altra anomalia di questo tipo oltre a quella corretta.
