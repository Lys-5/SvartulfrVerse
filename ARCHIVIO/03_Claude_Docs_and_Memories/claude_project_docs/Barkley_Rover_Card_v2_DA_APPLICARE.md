# Barkley Rover — card v2 — APPLICATA E VERIFICATA

**Stato: applicata su Wyvern il 3 settembre 2026 e verificata dopo reload completo.** Questo documento resta come tracciamento dell'errore e delle scelte fatte. Il testo completo dei campi è ora sulla card, non serve tenerne una seconda copia qui.

---

## Perché la v1 è stata buttata

La v1 era stata scritta prima che arrivassero le fonti e aveva inventato quasi tutto. Le fonti sono due card janitorai (`veseii` e `Iorveths`), concordi su ogni punto sotto.

| Dettaglio | v1 (sbagliata) | Fonte, ora in card |
|---|---|---|
| Età | 34 | **32** |
| Altezza | 5'10" | **5'11"** |
| Capelli | "arruffato dorato" | **biondo dorato, mullet** |
| Occhi | marroni | **azzurri, da cucciolo** |
| Viso | non descritto | **barba bionda, sopracciglia folte, zanne** |
| Anni a SUCC | 11 | **5, tutti sotto Dullahan** |
| Carriera | "mai il migliore, sempre grato" | **football liceo e college, un infortunio gli ha chiuso la carriera** |
| Famiglia | due genitori, una sorella più brava | **figlio unico, molta pressione dai genitori** |
| Odore | erba tagliata, deodorante | **miele, sudore, fast food** |
| Personalità | competente e invisibile, "l'unico che tiene in piedi la squadra" | **Lovable Himbo: tonto, credulone, indeciso, pauroso, goffo, impulsivo, autostima a terra** |
| Gioco d'azzardo | nessuno lo sa | **va a Giocatori Anonimi ogni settimana, di nascosto** |
| Creditore | generico | **Sharky** |
| Casa | contratto rinnovato sei volte | **bachelor pad incasinato, a piedi dal campus** |

L'errore grave era il carattere: l'avevo scritto come il professionista silenzioso che regge tutto, ed è invece l'himbo adorabile. Riscritto da zero come himbo.

Roba nuova dalle fonti entrata in card: rut ogni sei mesi; permaloso sull'essere demiumano cane e detesta essere scambiato per un lupo mannaro; dimentica di avere la coda e rovescia le cose, con una classifica tenuta dai giocatori nella stanza attrezzi; insieme imbarazzato e a suo agio con la propria stazza; campionato vinto nel '09; parla con "right?" e "y'know?" in coda alle frasi.

---

## Epurazione `{{user}}` (Regola 1)

Entrambe le versioni sorgente mettono `{{user}}` come cotta o partner di Barkley, con contenuto sessuale esplicito e un blocco Intimacy dettagliato. In questo World `{{user}}` è Alyssa, matricola di diciannove anni, e Barkley è staff di trentadue anni. **Rimosso integralmente: nessuna cotta, nessuna relazione, nessun blocco intimità.** Il vuoto lo riempie il thread del debito, che regge da solo.

---

## Valori finali sulla card (verificati dopo reload)

| Campo | Valore |
|---|---|
| display_name | Barkley Rover |
| Nickname | Barks, Coach Barkley, Coach B |
| Titolo | Assistant Coach |
| long_summary (JED+) | 5.091 caratteri |
| summary (PList) | himbo, loyal, gullible, dim-witted, anxious, clumsy, low self-esteem, forgets he has a tail |
| Outfit | 5: Practice/Sideline, Game Day, At Home, Recruiting Visit, **Thursday Night** |
| Dialogue Examples | 5: Greeting, Nervous, Sad, Memory, **The line he will not cross** |
| Start Position | 10450560 = 12 marzo 1992 |
| RPG | **Lv.32** — MGT 8 / RES 7 / AGI 2 / WIT 2 / PRS 3 / SCT 9 (25/25) |
| Global Character | ON |
| Cartella | SOLARTON |

Verifica: zero `{{user}}`, zero em-dash, zero asterischi.

**Perché queste stat.** AGI 2 e WIT 2 sono deliberati: è goffo e non è sveglio, e la scheda deve dirlo. MGT 8 perché sotto il grasso c'è un ex giocatore vero. SCT 9 è il naso, l'opposto esatto di Dullahan, che è un cane da vista con SCT 1.

**"Thursday Night" e "The line he will not cross"** sono i due pezzi su cui poggia il personaggio. L'outfit è identico a nessun altro proprio perché è anonimo: felpa grigia, cappuccio sulle orecchie, parcheggia due strade prima della chiesa. E la battuta sul non scommettere sui propri ragazzi è l'unico momento in cui la coda si ferma. Insieme dicono che l'ottimismo a tutti i costi è una scelta che sta facendo, non un difetto di fabbrica.

---

## Nota operativa importante scoperta applicando questa card

**Le cartelle nella lista contenuti si espandono solo cliccando la chevron, che è il PRIMO button della riga della cartella.** Cliccare l'etichetta di testo, o il suo contenitore, non fa niente, nemmeno con un click di mouse reale. Se una scansione DOM restituisce zero righe, la cartella è collassata, non è sparito il personaggio.

Helper che funziona:

```js
EXPAND = async function(name){
  const c = [...document.querySelectorAll('*')]
    .find(e => e.children.length===0 && new RegExp('^'+name+'$','i').test(e.textContent.trim()));
  if(!c) return 'NOFOLDER';
  fc([...c.parentElement.querySelectorAll('button')][0]);  // chevron
  await sleep(3500);
  return rows().length;
};
```

Altra trappola: interrogare le API di Wyvern con un `fetch` scritto a mano restituisce `[]` o 401/403, perché l'app manda un header Authorization che il fetch nudo non ha. Un `[]` così **non è la prova che i dati siano spariti.** Verificare sempre dall'interfaccia.
