# Audit completezza dati World + outfit Shift/Hybrid (2026-09-15)

Verifica sistematica su tutti i 134 personaggi del World, su richiesta esplicita dell'utente ("verifica che le schede abbiano tutti i dati e tutti i campi compilati correttamente, con gli outfit per shift e hybrid per werewolf e shifter"). Corretto tutto ciò che era derivabile in sicurezza da materiale già in scheda, senza inventare nulla di nuovo; segnalato ciò che richiede materiale sorgente non disponibile.

## Metodo

Script di audit programmatico su tutta la tabella `world_characters`: completezza dei campi core (`long_summary`, `summary`, `display_description`, `final_instructions`), presenza della riga di format discipline, conteggio outfit (minimo 5) e validità del `default_outfit`, conteggio Dialogue Examples (minimo 5), presenza delle Attitudes obbligatorie verso Alyssa e Jasper, coerenza `birthdate`/`start_timeline_position`, `keys` non vuote, `is_global` attivo. Poi, specificamente per la richiesta sugli outfit Shift/Hybrid: estratta la specie di ogni personaggio dal campo `SPECIES:` del blocco JED+, isolati i 51 personaggi Werewolf/Warg e l'unico altro shifter puro del World (Professor Loewe, leone), verificato per ciascuno se possiede un outfit dedicato alla forma trasformata.

## Cosa è risultato già a posto

**49 dei 51 personaggi Werewolf/Warg avevano già gli outfit Hybrid Shift e Full Shift** (o equivalenti nominati diversamente: Full Wolf Shift, Wolf Form, Shifted, Full Moon), frutto del lavoro sistematico già fatto su Family, Pack e Solarton nelle sessioni precedenti (`Outfit_HybridFullShift_*`). Nessun gap strutturale trovato lì.

## Cosa è stato corretto in questa sessione

**Outfit Shift/Hybrid mancanti (3 personaggi):**
- **Allegra Lumsden** (Werewolf, Solarton): aggiunti Hybrid Shift e Full Shift, manto pink-blonde coerente con i capelli.
- **Roger "Rocky" Mackenzie** (Werewolf Common, Solarton): aggiunti Hybrid Shift e Full Shift, manto nero coerente.
- **Professor Loewe** (Shapeshifter, lion, unico non-licantropo con un vero shift nel World oltre a Coach Mithers/Hideo Reid/Arran Parker/Zero che ce l'avevano già): aggiunta Lion Form, forma singola coerente col sistema a uno stadio già usato per gli altri shifter non licantropi del World (manticora, kitsune, volpe, coyote).

**Campi core mancanti, corretti sintetizzando solo materiale già presente sulla scheda, nessuna invenzione nuova:**
- **Lord Cornelius Douglas, Zefir Hvitskog, Ut Berg**: `final_instructions` vuoto, aggiunta la sola riga di format discipline standard (nessun preambolo specifico inventato, coerente con lo stile già usato su Marlowe Voss/Cassian Aralas/Abel Vilas/Harrison Black).
- **Erik Douglas**: `final_instructions` presente ma privo della riga di format discipline, aggiunta in coda al testo esistente senza toccare il resto.
- **Marcus Thornfield**: mancavano `keys`, `display_description` e `final_instructions` per intero. Tutti e tre ricostruiti dal materiale già scritto nel suo stesso `long_summary` (il rapporto con Kaladin, Gamma-7, l'umorismo come muro, il tell degli occhi rossi), nessun fatto nuovo introdotto.
- **Kaladin Nargathon, Magnus Douglas III**: mancava solo `display_description`, scritta sintetizzando materiale già presente in `long_summary`.
- **Marlowe Voss, Cassian Aralas, Abel Vilas, Harrison Black, Marcus Thornfield**: `keys` vuoto, popolato con nome e varianti già usate altrove nella scheda.
- **Alyssa Douglas Bloodmoon**: aveva solo 3 Dialogue Examples invece di 5. Aggiunti due nuovi esempi coerenti con la voce già stabilita (una scena in cui si fa valere con calma, un momento vulnerabile con Malachia sulla paura di diventare Pack Mom), nessun fatto biografico nuovo introdotto.

## Cosa resta aperto, segnalato senza correggere

**6 schede completamente vuote, stub grezzi mai lavorati**, senza `long_summary`, `display_description`, `final_instructions`, outfit, Dialogue Examples o Attitudes: **Everett Rottmore, Damien Bishop, GLUTTONY - Kevin, ENVY - Siobhan, GREED - Roxie, Alicia Virtuoso**. Non corretti perché non esiste materiale sorgente da cui derivarli senza inventare per riempire un buco (§9.4). Kevin, Siobhan e Roxie sembrano appartenere al gruppo dei Sette Peccati Capitali (Gluttony/Envy/Greed, accanto a Jean-Luc Virtuoso/Lust, Dante/Wrath, Zero/Sloth già lavorati), e Alicia Virtuoso è probabilmente collegata a Jean-Luc Virtuoso: da chiarire con l'utente se esiste materiale sorgente per queste sei schede prima di poterle completare.

**Nota su un campo `avatar` mancante sugli outfit di gran parte del World (355 occorrenze su schede pre-esistenti a questa sessione).** Verificato che è una omissione diffusa e sistemica su tutto il World precedente a questa sessione, non un'anomalia isolata: probabilmente il campo è opzionale lato piattaforma e la sua assenza equivale a un avatar vuoto, non una scheda rotta. Non corretto in blocco per evitare centinaia di scritture a basso valore su un'ipotesi non verificata: da chiarire con l'utente se conviene una verifica diretta sull'interfaccia Wyvern prima di decidere se vale la pena sistemarlo ovunque.

**Dullahan**, `birthdate` diverso da `start_timeline_position`: già documentato e intenzionale (Immortal Contractor, Start Position anticipata al 1724 per coprire gli scenari fuori epoca già previsti), non un errore.

## Verifica

`PRAGMA integrity_check` ok, conteggio World invariato a 134 (solo modifiche di campo, nessun personaggio aggiunto o rimosso), tutti i 51 Werewolf/Warg più Professor Loewe ora con outfit di trasformazione, zero `{{user}}`/em-dash/markdown grassetto introdotti dalle correzioni. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.
