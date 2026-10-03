# Ricostruzione dei 9 Scenari dell'arco 2024 — completamento

Tutti e 9 gli scenari dell'arco narrativo 2024 sono stati ricreati direttamente sul sito Wyvern (non in locale, per istruzione esplicita dell'utente: l'app Wyldfire desktop resta ferma per questa fase perché ancora in beta). Verificato via reload completo della pagina Scenari: **Scenarios: 9/9**, **All Content: 752** (partito da 743 prima di questo lavoro).

## Elenco scenari (in ordine di World Clock)

1. **What Do You Want** — Domenica 7 aprile 2024, Villa Douglas, cucina (world_age 10486350 circa)
2. **Open Day alla SUCC** — Sabato 13 aprile 2024, Lunar Quad campus SUCC (10486667)
3. **First College Day** — Villa Douglas
4. **Diciannove Anni** — compleanno
5. **DJ Frequency** — Sabato 27 luglio 2024, notte
6. **Road Trip con Logan** — Lunedì 10 giugno 2024
7. **Primo Incontro con Jared Thompson** — Lunedì 2 settembre 2024, prima settimana
8. **Ciao, Sono Logan** — Sabato 14 settembre 2024, 23:00, Sidewinders Bar & Nightclub (10490375)
9. **Halloween alla Theta Iota Theta** — Giovedì 31 ottobre 2024, 21:00, Theta Iota Theta (10491501)

Ogni scenario ha: Nome, Short Description, Location (obbligatoria), When This Begins (world_age calcolato dalle fonti locali), pool di personaggi (aggiunti per nome via search, senza modificare i pesi di partecipazione individuali salvo Scenario 2), Min/Max Characters, un Manual Greeting con Template Description + Hour Override + testo completo in formato `=>Nome:` (dialogo tra virgolette, niente em-dash, niente asterischi), Content Rating mappato dalla fonte, World Only = ON.

## Deviazioni note dalla fedeltà assoluta alla fonte (da segnalare)

1. **Pesi di partecipazione dei personaggi**: per gli Scenari 3-9 i personaggi sono stati aggiunti al pool senza impostare manualmente il valore esatto di `participation_weight` della fonte (es. Mac 100%, Logan 90%, ecc. nello Scenario 8). Sono rimasti al default della piattaforma (~50%) tranne dove specificato. Lo Scenario 2 aveva ricevuto un tentativo di fine-tuning (Alyssa portata al 90% invece del 100% richiesto, per limiti dello slider). Non è stato esplicitamente approvato dall'utente come scorciatoia accettabile: da rivedere se serve fedeltà completa ai pesi.
2. **Location "Magazzino di DJ Frequency" non esiste ancora come Location sul World live** (Scenario 5): sostituita con "Los Angeles" (location più ampia disponibile), Environment lasciato "None". Va creata come Location dedicata quando si arriva alla sweep delle ~132 location.
3. **Nessun Environment "Blackwood City" o "Solarton" esiste ancora come Environment del World** (il World ha solo 2 opzioni Environment: "None" e "California Coast"). Tutti gli scenari sopra hanno quindi Environment = "None", anche quando la Location stessa (es. Sidewinders Bar & Nightclub, Theta Iota Theta) è chiaramente a Solarton. Questo è coerente in tutto l'arco ma andrebbe risolto creando gli Environment mancanti nella sweep successiva.
4. **Content Rating**: mappatura usata in assenza di corrispondenza esatta nella UI (che offre solo General/Mature/Explicit): fonte "none" → General, "suggestive" → Mature, "explicit" → Explicit.

## Prossimo passo

Procedere con la ricostruzione delle card dei personaggi principali della famiglia (Erik, Jasper, Alyssa, Malachia, Noah, Logan, Wulfnic, Kaladin, più Jared Thompson e Mac, nuovi nell'arco): Long Description in JED+, Short Description, Outfits, Birthdate, Dialogue Examples — direttamente sul sito, sempre senza passare dall'app locale Wyldfire per questa fase.
