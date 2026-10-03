# Barrow — Demi-human Representative, Blackwood Council (completato 2026-09-14)

Terzo dei sette rappresentanti delle specie minoritarie del Concilio a essere completato (dopo Zeera per i Demoni e Brak Ironfist per gli Orchi). Character ID Wyvern: `_eJQEGWzj2tyVHfbf7d7B1`. Entry Lexicon Intimacy Profile collegata: `_92VBcqq2Wt8bLYD7H4mMn`.

## Origine e riscrittura

Barrow nasce da una character card fornita dall'utente ("Barrow | Ukiyo Series", ambientazione Chicago moderna, razza Minotauro), il primo personaggio del progetto ad attivare formalmente la nuova regola generale sull'Intimacy Profile (vedi sotto). Scelto per il seggio Demi-human perché il minotauro, pur avendo un aspetto da predatore imponente, è biologicamente un erbivoro (bovino): rompe lo stereotipo richiesto dalla categoria (§Concilio, punto 4) senza bisogno di un coniglio o una capra.

Come da §13, l'intero arco protettivo/romantico costruito specificamente attorno a `{{user}}` (inclusa la scena della rissa nel vicolo con i gnoll, scritta come salvataggio di `{{user}}` in pericolo) **non è stato portato nella scheda nuova**. Al suo posto resta solo il tratto generale, senza destinatario fisso: Barrow protegge chiunque viva nel suo quartiere.

Quello che è stato portato avanti dal materiale originale: aspetto fisico (minotauro 7'4", pelliccia nera corta, barba curata, occhi ambra, corna con una tacca, anello al setto, cicatrice da arma da fuoco, tatuaggi sbiaditi di un vecchio gruppo), personalità (stoico, protettivo, disciplinato, di poche parole, mostra affetto con gesti pratici), il passato da "muscolo" di un gruppo di fuorilegge itineranti (reso generico, senza legami con Los Angeles/Underworld per non invadere quel dominio), l'episodio della sparatoria e dell'infermiera umana che lo ha trattato da persona, le abilità (forza sovrumana, master builder/carpentiere), gli amici Vargus (Oni) e Finn (Satyr) citati come contatti di sfondo, la passione per il jazz e il caffè nero, l'abitudine di sedersi all'alba sul portico a sorvegliare il quartiere.

## Concept sviluppato in chat con l'utente

- **Riambientazione**: da Southside Chicago a **The Horns**, un'enclave demi-human dentro il distretto di **Dockside** a Blackwood (nome dell'enclave originale mantenuto come omaggio). Non Ironworks, per non sovrapporsi a Vito Marino e Brak Ironfist già lì.
- **Occupazione**: manovale/carpentiere nei magazzini di Dockside di giorno, "sceriffo" informale del quartiere la sera. Deliberatamente non un imprenditore come Zeera o Brak Ironfist, per differenziare il suo profilo economico all'interno del Concilio.
- **Età**: 42 nella fonte, trattata come età reale (nessuna convenzione di longevità per i Minotauri ancora stabilita, stesso approccio "umano-simile" adottato per Brak Ironfist). Birthdate/start_timeline_position: 10117494 (3 marzo 1982), coincidenti, età 42 al world_age corrente (10486470 = 5 aprile 2024).

## Nuova regola generale sull'Intimacy Profile (decisione 14/09)

**L'utente ha modificato la regola del progetto in chat**: il contenuto anatomico/di kink esplicito e consensuale (non i casi di tratta/non consenso/arco `{{user}}`-specifico, quelli restano esclusi per intero secondo l'estensione già in vigore) **non va più scartato, va spostato come Intimacy Profile separato, come regola generale per qualunque personaggio**, non solo su richiesta caso per caso.

In fase di scrittura si è scoperto che questo pattern **esiste già ed è ampiamente in uso sul World** (Erik, Logan, Malachia, Bailey, Dominic, Venera, Santiago, Roland, Mac, Fade, Adelin, Chase, Stanley, Zero, Jean-Luc, Dante, Arthur ce l'hanno già), solo non era stato applicato alle schede riscritte da materiale importato in questa sessione (Zeera, Huck, Brak Ironfist, dove il contenuto è stato scartato del tutto). Formato confermato via API e ora codificato nelle regole di progetto: `is_global: true` (non `false`), `party_conditions` con `has_any` sull'id del personaggio proprietario, `keys: [nome]`, `secondary_keys` su intimacy/dating/relationship/romance/flirting/attracted/sex, due registri di scrittura osservati (a blocchi tipo Erik, o in prosa tipo Dominic).

## Cosa è stato scritto su Wyvern

Pipeline completa (§14) via API browser-driven, verificata con GET diretto (scanner automatico: zero `{{user}}`, zero em-dash, zero grassetto markdown su entrambe le entry).

- `long_summary` in JED+ con sezioni BACKSTORY, THE HORNS AND THE ROAD (equivalente di FAMILY & PACK), VOICE AND BEHAVIOR, chiusura tematica "WHAT HE BUILT TO REPLACE THE VIOLENCE".
- `summary` in blocco PList compatto.
- `display_description`, `titles` (Demi-human Representative Blackwood Council), `nicknames` (The Bull of The Horns), `keys`, pronomi he/him.
- **Outfit, cinque, contestuali**: Dockside Shift (default), Council Session, The Stoop, Off the Clock, Trouble.
- **RPG Stats: non impostate**, come da pausa del sistema (§8).
- **Dialogue Examples, cinque**: saluto a un nuovo vicino, un vicino che lo ringrazia per una riparazione, una minaccia in arrivo sul quartiere, qualcuno che gli chiede della vecchia vita, un momento esposto in solitudine sull'infermiera che lo ha aiutato.
- **Attitudes**: Alyssa e Jasper a tier "stranger" (mai incontrati), Erik Douglas a tier "acknowledged" (stesso schema di Zeera e Brak Ironfist).
- **Intimacy Profile separato** (entry Lexicon `_92VBcqq2Wt8bLYD7H4mMn`): registro in prosa (stile Dominic Rogers), copre taglia/contenimento, dominanza protettiva, apprezzamento per gli elogi alla sua disciplina invece che alla forza, il "ronzio" vocale in eccitazione, scent-marking involontario, il limite invalicabile (perdere il controllo) e il consenso più profondo (un partner che si fida abbastanza da abbandonarsi del tutto). Nessuna misura anatomica numerica riportata, nessun riferimento a `{{user}}`.
- **Global Character**: ON su entrambe le entry.

## Note aperte

Restano da assegnare quattro seggi del Concilio: Fatati, Umano con capacità magiche, Ibrido/Naga, Non-morto non vampirico.

Le regole di progetto (`Istruzioni di Workflow`) sono state aggiornate in locale per riflettere la nuova regola generale sull'Intimacy Profile; l'utente ha già l'ultima versione completa consegnata in chat, da incollare nelle istruzioni custom del Project quando vuole.
