# Atlas Teague — Completamento Scheda (2026-09-14)

Chiude l'incidente documentato in `Atlas_Teague_Bug_Character_Bloccato_2026-09-14.md` e prosegue `Migrazione_Locale_Wyldfire_116_Personaggi_2026-09-14.md`. Personaggio scritto **solo in locale** (Wyldfire, `world_characters`), il World online resta quello rotto: l'utente pubblicherà da Wyldfire a lavoro finito. Nuovo totale locale: **117 personaggi**.

## Fonte e triage

L'utente ha fornito la scheda sorgente originale (pre-modifiche), costruita quasi interamente attorno a `{{user}}`: adozione di Atlas come "cane randagio" da parte di `{{user}}`, convivenza in casa sua, relazione romantica di un anno, tutto il blocco Intimacy scritto in funzione di quel rapporto specifico.

Applicata l'estensione del 14/09 a §13: **l'intero arco narrativo/romantico legato a `{{user}}` è stato escluso fin dalla lettura**, non ripulito riga per riga. Portato avanti solo ciò che regge senza: trauma dell'attacco di branco a 16 anni, addestramento nelle arti marziali, fight club clandestino, raid della polizia, homelessness, aspetto fisico, tratti di personalità, voce, insicurezze (paura del rifiuto, timore di valere solo per i pugni che sa tirare).

Al posto della trama con `{{user}}`, la scheda è stata agganciata al dato già confermato in altri documenti del Project: **compagno/rivale di lotta clandestina di Malachia Douglas Bloodmoon, incontrati sul ring illegale di Blackwood**. Da lì sono state costruite le scelte di continuity mancanti nella fonte (proposte all'utente e confermate prima di scrivere):

- **Età/data di nascita**: 28 anni confermati dalla fonte, data scelta 19 febbraio 1996 (non 1° gennaio, per §9.6), `birthdate` = `start_timeline_position` = **10239912** ore-World (calcolato dall'epoch 827-12-21T00:00 con calendario gregoriano proletico).
- **Stato attuale**: lupo solitario, non registrato presso la città, nessun pack, nessun handler umano. Coerente col lore di base fornito dall'utente in chat (licantropi con handler per gestire aggressività/calore, registrazione obbligatoria dei sovrannaturali, branco raro ma stabilizzante). La sua natura non registrata diventa il punto di tensione con la Douglas Pack che controlla il territorio di Blackwood, riservato via Attitude generica (vedi sotto).

## Contenuto scritto

- **JED+ completo** (BACKSTORY, FAMILY & PACK, VOICE & BEHAVIOR, THE WEIGHT HE CARRIES) e `summary` PList, presentati e confermati dall'utente prima della scrittura.
- **5 Outfit contestuali**: Street Casual (default), Ring Night, Hired Muscle, Full Shift (lupo, stile Husky ingigantito), Full Moon / Heat. Nessun accessorio scritto come costante non giustificata: tatuaggi e piercing sono tratti fisici fissi (non un "accessorio" soggetto al problema §4), coerenti in ogni outfit.
- **5 Dialogue Examples**, riscritti allontanando ogni scena dal contesto `{{user}}`: primo incontro sul ring, la domanda sul perché non è registrato, il riflesso protettivo, il ricordo del raid (il suo momento più esposto), l'opinione su Malachia. Disciplina di formattazione §3 rispettata (verificato programmaticamente: zero em-dash, zero asterischi fuori dai pensieri, zero `{{user}}`, zero grassetto markdown).
- **Attitudes**: Malachia Douglas Bloodmoon (`rival`, intensity 75, con **voce reciproca aggiunta anche sulla scheda di Malachia** per §16), Alyssa e Jasper Douglas Bloodmoon (`stranger`, intensity 15, mai incontrati, come da regola §16 sui due personaggi giocabili), più due Attitudes di tipo Generic/text: "Local Law Enforcement / City Registration" (`disliked`, 55) e "Douglas Pack" (`wary`, 40), per rendere esplicita la sua posizione di lupo non registrato in territorio Douglas senza inventare un nuovo personaggio nominato.
- **Intimacy Profile** come entry Lexicon separata (`Intimacy Profile - Atlas Teague`, tipo `memory`, `is_global: true`, keys sul nome, secondary_keys standard, `attached_world_character_id` sull'id locale di Atlas), stile prosa (precedente Dominic Rogers), contenuto generalizzato come tratti propri del personaggio (dominanza, praise kink, biologia del nodo, paura del rifiuto) invece che scene legate a `{{user}}`.
- **`final_instructions`** chiude con la riga di disciplina di formattazione richiesta da §3.
- `Global Character`: `is_global = 1`.

## Nota tecnica sulla scrittura locale

Personaggio inserito direttamente nella tabella `world_characters` del database Wyldfire locale (id locale generato in stile coerente con gli altri, `platform_id` sintetico dato che non esiste ancora online). Applicata la lezione della correzione dello stesso giorno (vedi doc di migrazione): `attitudes[].target_id` scritto fin da subito con gli **id locali** di Malachia/Alyssa/Jasper, non platform_id, per evitare lo stesso bug di risoluzione già trovato e corretto sugli altri 116 personaggi. Verificato dopo scrittura: `PRAGMA integrity_check` ok, tutti gli Attitudes risolvono al nome giusto, nessun riferimento orfano.

Scritto sul PC dell'utente solo dopo conferma esplicita che Wyldfire fosse chiuso.

## Stato

Scheda completa lato locale. Resta sospesa la scrittura sul World online (corrotto, in attesa di pubblicazione da Wyldfire a lavoro finito) e qualunque `birthdate` futuro andrà passato come numero, mai come stringa ISO, quando si tornerà a scrivere via API.
