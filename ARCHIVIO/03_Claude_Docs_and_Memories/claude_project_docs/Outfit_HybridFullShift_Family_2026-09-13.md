# Outfit Hybrid Shift / Full Shift, cartella Family (2026-09-13)

Su richiesta dell'utente, dopo che ha aggiunto a mano i due outfit di trasformazione (Full Shift, Hybrid Shift / True Form) alla scheda di Alyssa, è stato replicato lo stesso trattamento su tutta la cartella Family. Corretto anche un em-dash trovato nel testo Full Shift di Alyssa stessa ("manifestation—the form venerated" -> "manifestation, the form venerated"), verificato via GET dopo il fix.

## Metodo

Per ognuno degli 11 personaggi della cartella Family: estrazione di HAIR/EYES/BUILD/HEIGHT esistenti dal `long_summary`, e di eventuali stub già presenti (`HYBRID_FORM:`, `FULL_SHIFT:`, `TRANSFORMATION_TRIGGERS:`). Dove lo stub esisteva già (Jasper, Noah, Erik, Logan, Malachia) è stato usato come ancora fattuale e sviluppato in prosa nello stile di Alyssa (~350-500 caratteri per outfit). Dove non esisteva (Wulfnic, Elizabeth, Magnus, Cornelius) la descrizione è stata costruita solo dai tratti fisici già scritti in scheda (colore capelli/pelo, occhi, altezza dove presente), senza inventare dettagli nuovi.

Scritto via API con PUT parziale sul campo `outfits` (array esistente + 2 nuove entry), verificato con reload completo della pagina e nuova GET: outfit count corretto, "Full Shift" e "Hybrid Shift" presenti, zero em-dash/`{{user}}`/markdown grassetto.

## Chi ha ricevuto i due outfit nella prima passata (9)

- **Jasper Douglas-Bloodmoon**: stesso manto caramello di Alyssa (sua gemella), ma SENZA il marchio a cuore/crescente color luna bianca, che appartiene solo a lei come White Moon. Su indicazione esplicita dell'utente, la sua forma da lupo è quasi doppia per stazza rispetto a quella di Alyssa pur restando la più veloce/snella dei fratelli (223cm hybrid, contro i 258-263cm di Malachia/Erik).
- **Noah Douglas-Bloodmoon**: manto biondo dorato, occhi che virano da blu a oro ambrato, 227cm hybrid. Usato lo stub HYBRID_FORM/FULL_SHIFT già presente in scheda.
- **Erik Douglas**: manto nero, occhi ambra che virano oro fuso, 263cm hybrid "riservato a esecuzioni o difesa del branco", coerente con lo stub esistente.
- **Logan Douglas**: manto nero brizzolato (coerente coi suoi capelli brizzolati alle tempie), occhi ambra, 228cm hybrid, usato solo per difendere garage/branco/Edric.
- **Malachia Douglas-Bloodmoon**: lupo nero con cicatrici bianche, 258cm hybrid, la forma che usa nel ring clandestino.
- **Wulfnic Bloodmoon**: qui la scheda aveva già un'altezza esplicita per la forma bipede primeva (300cm/9'10"), usata come Hybrid Shift; il Full Shift quadrupede è stato scritto in modo qualitativo (pelo bianco argento, occhi ghiaccio che virano blu argenteo) senza inventare una misura numerica non presente in fonte.
- **Elizabeth Duskwood**: pelo grigio cenere, occhi grigio tempesta, corporatura proporzionata alla sua statura umana ridotta (165cm) invece che alle taglie enormi dei maschi Douglas.
- **Magnus Douglas III**: pelo nero Douglas brizzolato alle tempie (coerente coi capelli), occhi ambra, forma ormai usata quasi solo per cerimonie di Casa.
- **Lord Cornelius Douglas**: pelo nero Douglas, occhi ambra, forma riservata alla disciplina di branco nella sua epoca, mai mostrata alla Corona inglese. Deceduto, ma la Character resta usabile in scenari storici/di flashback, quindi coerente aggiungere gli outfit.

## Edric e Nixara, aggiunti in un secondo momento su indicazione dell'utente

Inizialmente esclusi dalla prima passata (Edric perché non può ancora trasformarsi, Nixara perché la sua scheda non conteneva alcun dato fisico), sono stati poi inclusi anche loro dopo istruzioni dirette dell'utente:

- **Edric Douglas**: inserito con la macro temporale di Wyvern (`{{#beforeTimestamp}}` / `{{#afterTimestamp}}`, da `World Handlebars Macros` sulla WyvernWiki, aperta dall'utente nel browser interno). Compie 13 anni, età di presentazione coerente con Erik e Jasper, il 25 febbraio 2025, world-hour **10494288** (calcolato dall'epoca 21/12/827 con `birthdate`/`start_timeline_position` = 10380312; world_age attuale al momento della scrittura = 10486470). Prima di quell'ora entrambi gli outfit mostrano solo che non ha ancora presentato e non può accedere alla forma; dopo, mostrano una forma hybrid/full shift acerba e goffa (capelli/occhi Douglas neri/ambra, corporatura ancora da adolescente, incespica sui propri artigli). Nessuna contraddizione con il campo `FORM: Pre-presentation, currently unable to shift`: resta vero finché il World non supera quella data, poi la macro attiva il testo nuovo automaticamente.
- **Nixara Bloodmoon**: l'utente ha fornito il dettaglio mancante, tutti i Bloodmoon hanno capelli biondi, occhi azzurri e pelliccia bianca (Noah ha preso il colore da lei; Wulfnic era biondo in gioventù, poi diventato argenteo con l'età, coerente con la sua descrizione attuale). Scritti i due outfit su questa base: pelliccia bianca pura, occhi azzurri, senza il marchio a cuore/crescente che resta specifico di Alyssa come White Moon attuale, non ereditato automaticamente dal titolo.

Entrambi verificati dopo reload completo: outfit count corretto, testo presente, zero em-dash/`{{user}}`/markdown grassetto.

## Bilancio finale Family

Tutti e 11 i personaggi della cartella Family hanno ora gli outfit Full Shift e Hybrid Shift, Edric incluso (con gate temporale) e Nixara inclusa (con la colorazione Bloodmoon confermata dall'utente).

## Prossimo passo

Cartella Pack completata subito dopo (vedi `Outfit_HybridFullShift_Pack_2026-09-13.md`). Blackwood e Los Angeles restano in attesa di conferma esplicita dell'utente.
