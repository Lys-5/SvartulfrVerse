# Bakersfield — Garrett Locke e Dallas Rhodes (2026-09-15)

Primo gruppetto della lista "official NPC" mandata dall'utente il 14/09 sera (vedi riepilogo completo, ancora da salvare come indice a parte se richiesto). Scritti **solo in locale** (Wyldfire), World online ancora quello rotto. Nuovo totale locale: **119 personaggi**.

## Garrett Locke

Fonte: scheda originale fornita dall'utente, con Relationships che includeva `{{user}}` come "lover" (una riga sola, non un arco narrativo esteso come nel caso Atlas/Zeera/Huck). Rimossa quella riga per §13 (nessuna relazione fissa possibile con `{{user}}`), mantenuto tutto il resto: vampiro che si nutre di sangue animale per senso di colpa, ranch fuori Bakersfield (adattato da "Montana" del sorgente per calzare sul dominio richiesto), il trauma dell'incendio a 14 anni, gli animali del ranch (Rain, Bandit, King, tenuti nella prosa perché propri del personaggio, non creati come entry separate).

**Scoperta di continuity importante**: il blocco NPC allegato nominava esplicitamente "Adrian Locke, fratello minore di Garrett, ranger a Grand Teton, morso e trasformato in licantropo, di nascosto da tutti, contatti persi con Garrett da anni". **Adrian Locke esiste già nel World** (Blackwood, completato il 14/09) e la sua scheda conteneva **già** esattamente questo aggancio, fratello maggiore Garrett, incendio, licantropia nascosta, persino un tatuaggio con le iniziali "G.L." in suo onore. Nessuna correzione necessaria sul lato Adrian: solo aggiunta la voce Attitude reciproca verso Garrett (`romantic_interest`, intensity 90, usato come da convenzione del World per i legami familiari profondi, non solo romantici, vedi Wulfnic/Nixara e Alyssa/famiglia).

Intimacy Profile scritto come entry Lexicon separata, generalizzato dai tratti propri di Garrett (lento, protettivo, si scioglie con le lodi, cede il controllo con la persona giusta) invece che centrato su `{{user}}`.

## Dallas Rhodes

Fonte: scheda in formato PList/prosa mista fornita dall'utente, più uno scenario di primo incontro (farmer's market) scritto con `{{user}}` come chiunque lo incontri per la prima volta, non come relazione fissata: mantenuto come Dialogue Example (non esiste un campo `first_mes` separato nello schema locale `world_characters`, i World Character usano `speech_examples` come unico meccanismo di esempio), ripulito da un doppio trattino non conforme e normalizzato alla disciplina §3.

**Scartato deliberatamente** il blocco "Setting" allegato alla fonte (Terra moderna 2023, matrimoni misti umano/non-umano illegali nella maggior parte dei paesi): è lore di un'ambientazione esterna non dichiarata, potenzialmente in conflitto con lo status civile dei sovrannaturali già stabilito per Blackwood. Non importato, per §10 (un dominio non dichiarato non ha voce su regole già stabilite altrove nel World).

Intimacy Profile scritto come entry Lexicon separata dal blocco Sex/Other della fonte (già scritto con `{{char}}`, quindi già generico e portabile senza modifiche sostanziali): pulsione a marcare/mordere, biologia del nodo, desiderio di legame serio più che di casualità.

## Verifica

`PRAGMA integrity_check` ok, 119/119 personaggi, zero `{{user}}`/em-dash/grassetto markdown su entrambe le nuove schede, Attitudes risolte correttamente (incluse quelle obbligatorie verso Alyssa/Jasper, entrambi "mai incontrati" essendo Garrett e Dallas fuori dal territorio Douglas). Scritto sul PC solo dopo conferma che Wyldfire fosse chiuso.

## Stato pipeline "official NPC"

Dei 92 nomi mandati dall'utente il 14/09, 61 già presenti (incluse varianti di scrittura confermate: Loewe/Davies/Jökull/Gray), **31 nuovi** individuati, di cui **2 completati** in questo batch (Garrett Locke, Dallas Rhodes). Restano 29: Bakersfield (2: Bram Beaumont, Lennox McKay), Solarton (7: Kai Monroe, Roman Blackwood, Kolya Varenkov, Dean, Russ, Eric, Raymond), Los Angeles (5: Emlyn Danes, Vero Walker, August Reed, Maverick Varon, Jack Briar), Blackwood (15: Milo Grayson, Emil, Levi Graham, Rhatt, Jayce, Julian Bieri, Gianni Luciano, Vale Roberts, Cyrus Camden, Nic Lucero, Angui, Gabriel Landon, Justin Campbell, Neon Purr, Arturo Cardona). L'utente manderà il materiale a gruppetti.
