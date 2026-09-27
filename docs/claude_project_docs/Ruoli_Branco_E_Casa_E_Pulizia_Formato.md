# Ruoli di branco e status di Casa, e la pulizia del formato

2026-09-08, con una correzione importante del 2026-09-13. Fonti:
`LSE_04_Governance.md` e le matrici B e C dell'appendice.

---

## 1. Casa e branco sono entità separate

Canon dell'utente, e correggeva un mio errore. Avevo messo Erik come House Head.

> **Erik ha preso il controllo del branco, non della casata. Erik è Pack Leader,
> Magnus è House Head.**

Il principio della fonte che regge tutto: l'autorità di branco *"is earned,
assigned, and maintained through trust and competence, NOT determined by
secondary sex"*, e il Pack Leader **non deve essere un Alpha**.

---

## 2. CORREZIONE 2026-09-13: Patriarch non è House Head, e il World lo diceva già

Avevo segnalato come contraddizione il fatto che Erik venga chiamato "Patriarch"
mentre Magnus è House Head, appoggiandomi alla riga del glossario
`LSE Naming Conventions & Titles` che dice *"Patriarch / Matriarch: House Head"*.
Su richiesta dell'utente avevo poi tolto il titolo a Erik.

**Era sbagliato, ed è stato annullato.** Il World contiene una entry dedicata,
`Patriarch`, che dice:

> *"The office is often confused with House Head and is not identical: House Head
> is a legal and continental designation, while Patriarch is what the family
> itself calls the man it will actually obey. When the two are the same person,
> which is usual, nobody notices the distinction. When they are not, everybody
> does."*

Quell'ultima frase è scritta esattamente per la situazione attuale. **Erik
Patriarch e Magnus House Head non è un conflitto: è il caso raro che la entry
prevede**, ed è materiale narrativo invece che un errore da sanare.

### Cosa è stato fatto, alla fine

- **Erik**: `ALIAS: The Prime Alpha, The Patriarch` ripristinato, e "Patriarch"
  rimesso fra i suoi nickname.
- **`House Genealogies Summary`**: la riga di Erik adesso dice *"Patriarch of
  House Douglas and Pack Leader of the Seven Hills Pack, CEO of the DCC. The
  House Head is still his father Magnus, and the two offices being held by
  different men is the uncommon case the Patriarch entry describes."* E su
  Magnus è stato aggiunto che **è tuttora House Head**.
- **`LSE Naming Conventions & Titles`**: la riga che appiattiva i due titoli è
  stata corretta in *"usually the House Head, but the two offices are distinct
  and can be held by different people"*, con rinvio alle entry dedicate.

### La lezione, che è §9.5 esatta

Una riga di glossario importata da una tabella non batte una entry dedicata
scritta apposta. **Prima di trattare qualcosa come contraddizione, cercare se il
World ha già una voce su quel termine.** Qui la voce c'era, conteneva la
risoluzione, e non l'avevo cercata.

Nota: `Core_Docs/World_Seed.md` riga 221 dice *"House Head (Erik)"*. Alla luce di
questo resta impreciso ma è secondario, ed è un file sorgente dell'utente (§9.3).
Non modificato.

---

## 3. Assegnazioni applicate

| | PACK_ROLE | SOCIAL_STATUS |
|---|---|---|
| Magnus III | Pack elder, nessun ruolo operativo | House Head |
| Erik | Pack Leader dei Seven Hills | Lord |
| Elizabeth | Pack Mom, tenuta in trust | Lord |
| Logan | nessuno, ha lasciato il branco | Lord |
| Malachia | Left Hand, e Pack Leader designate | Citizen |
| Noah | Caretaker, e Right Hand designate a Malachia | Citizen |
| Jasper | Caretaker, e Left Hand designate a Malachia | Citizen |
| Alyssa | Whitemoon, Caretaker, Pack Mom designate | Citizen |
| Edric | Pup | Citizen |
| Kaladin | Left Hand | Knight |
| Marcus | Left Hand | Knight |
| Cornelius | Pack Leader ai suoi tempi | House Head, fondatore |
| Nixara | Pack Mom fino alla morte | Lord |
| Wulfnic | Pack Leader dei Bloodmoon, Alpha of Alphas | House Head di Casa Bloodmoon |
| Ut | Right Hand di Wulfnic | Lord |
| Zefir | Left Hand di Wulfnic | Lord |

**Il chiarimento sui fratelli.** Le schede dicevano che Noah e Jasper sono Right
e Left Hand *di Malachia*, che non tornava. L'utente ha sciolto il nodo: **sono
designati**, e prenderanno quei ruoli quando Malachia succederà a Erik. Oggi sono
Caretaker, che la matrice descrive come il posto dei giovani adulti usciti da
Pup.

Il branco ha quindi **tre successioni scritte e nessuna avvenuta**: Malachia a
Pack Leader, i suoi due fratelli come Hands, Alyssa a Pack Mom ai ventuno anni.

### Assi separati, campi separati

Tre schede avevano `SOCIAL_STATUS` riempito con la **professione**. Corretto: il
campo porta solo il valore della scala, e il contenuto precedente è stato
conservato in `STUDIES:` per Alyssa e `AFFILIATION:` per Noah e Jasper.

### Fascia d'età: esclusa

`Prime`, `Adult`, `Elder` non avranno un campo: sono derivabili dalla data di
nascita, e scriverle a mano crea un dato che invecchia da solo. È lo stesso
motivo per cui §2 impone la macro `{{age}}`.

---

## 4. Il backlog §3 è chiuso

Era registrato come "38 em-dash su circa 8 schede". Il conteggio reale era molto
più piccolo e adesso è **zero**.

- **Dieci em-dash** su quattro schede: Bailey (3), Santiago (4), Jean-Luc (2),
  Magnus (1). Sostituiti uno per uno con la punteggiatura giusta per la frase.
- **Markdown `**`**: `frat-bro` sulla scheda di Noah e ventidue coppie di
  grassetto nella entry `Supernatural Degrees`. Rimossi.
- **Ventidue entry Lexicon avevano l'em-dash nel nome**, non solo le undici
  Intimacy Profile. Tutte rinominate col trattino semplice.

Verifica su tutto il World: zero em-dash in nomi di entry, contenuti Lexicon,
schede personaggio, Location e Scenari.

---

## 5. Avviso sulle matrici dell'appendice

La matrice E dà i **Common Bloodlines a 80-150 anni**. Il World li ha a **60-80**
per una scelta deliberata del 2026-09-06 registrata in
`Longevita_Common_Bloodline.md`. **Non è una svista da riallineare.**

---

## 6. Nota tecnica: device_bash non funziona più

Dal 2026-09-13 la shell sul computer dell'utente risponde *"Workspace
unavailable... A Windows update released September 8 prevents Claude's workspace
from reaching your files."*

Conseguenza pratica: **le fonti in `D:\SvartulfrVerse\Drafts\` non sono più
leggibili via shell**. Restano raggiungibili con `device_list_dir` per esplorare
e `device_stage_files` per portarne su una copia da leggere. Va tenuto presente,
perché quelle fonti sono diventate il riferimento più forte per biologia e cast.
