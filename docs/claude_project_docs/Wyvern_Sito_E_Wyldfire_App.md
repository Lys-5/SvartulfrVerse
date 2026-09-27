# Wyvern (sito) e Wyldfire (app desktop): cosa è cosa

Chiarito il 2026-09-07 leggendo la guida di StatuoTW
(`rentry.co/StatuoTWWyldfire`), che è una guida di community, non
documentazione ufficiale, ma è scritta da un beta tester ed è la fonte più
chiara in circolazione.

---

## Sono due prodotti, non due viste della stessa cosa

**Wyvern** (`app.wyvern.chat`) è **il sito**: sta nel cloud, ospita e pubblica
le card, i World e i lorebook, ha la community, l'Explore, i commenti, e ci si
chatta dal browser o dal telefono. È dove viviamo noi: il World
Svartúlfr | Urban è lì, e tutto quello che abbiamo costruito sta lì.

**Wyldfire** è **un'applicazione desktop che gira sulla macchina dell'utente**,
dello stesso sviluppatore (Nev). Nasce come sostituto di SillyTavern, che non
riceve più aggiornamenti. Punti che contano:

- Gira **in locale**. I dati stanno sul computer, non in rete.
- **Non serve un account Wyvern per usarla.** Si può averlo e integrarlo, ma non
  è necessario.
- Si connette **alle API che scegli tu** (Deepseek, Featherless, OpenRouter,
  modelli locali), con le tue chiavi.
- Ha funzioni pensate per il roleplay che il sito non ha allo stesso modo:
  Memory Scan, Director, Sidechat, Infoboard, Sprites, NPC con bolle di chat
  proprie.
- Importa quasi tutto da SillyTavern con qualche click. Le sole cose che non si
  importano sono le **chat di gruppo** e i **Chat Completion Preset**.

---

## Il ponte fra i due è il Sync, ed è opzionale

Sta in Wyldfire, in **Settings → Wyvern Account Sync**. Attivandolo si ottiene:

- scaricare card e World da Wyvern direttamente dentro l'app;
- ricevere le notifiche di Wyvern in Wyldfire e vedere il proprio feed;
- **pubblicare una card su Wyvern dall'app**, con il pulsante *Publish to
  Wyvern* sulla schermata della card;
- **sincronizzare le chat nei due sensi**, che è il motivo vero per attivarlo:
  si gioca su Wyldfire a casa e si continua la stessa chat su Wyvern dal
  telefono;
- far contare i messaggi con i bot pubblici nel totale del creatore.

**Il vincolo che conta:** per sincronizzare una chat **il personaggio deve già
esistere su Wyvern**. Quindi qualunque card si voglia usare in una chat
sincronizzata va caricata prima sul sito, anche in privato.

**Cosa il sync NON fa:** non pubblica le card automaticamente, e non rende
pubbliche le chat.

---

## Perché questo spiega la regola che avevamo già scritto

In `§15` delle istruzioni c'è la riga *"locale e sito sono entità separate,
modificare il locale non modifica il sito finché non si clicca su upload"*.
Adesso si capisce da dove viene: **Wyldfire ha un proprio database locale**, e
il caricamento verso Wyvern è sempre un gesto esplicito, o *Publish to Wyvern*
o il sync delle chat. Non c'è nessun salvataggio automatico verso l'alto.

**Conseguenza operativa per noi:** tutto il lavoro sul World che facciamo via
API passa dal sito, quindi è il sito la sorgente di verità. Se un giorno si
apre Wyldfire e si guarda lo stesso World, quello che si vede lì può essere una
copia più vecchia. In quel caso non si lavora sulla copia locale: si scarica di
nuovo.

---

## Cose della guida che ci riguardano direttamente

- **I Lexicon dei Lorebook non fanno niente**, dice la guida, mentre i Lexicon
  di Character e di Chat funzionano. È una nota su Wyldfire, non sul sito, dove
  il Lexicon del World funziona benissimo, ma va tenuta presente se un giorno si
  esporta materiale verso un lorebook.
- **Dopo un Memory Scan bisogna ricaricare la chat** perché le voci compaiano.
  Combacia con quello che abbiamo visto nei nostri test.
- **C'è una scheda Debug** che registra tutto quello che si fa nell'app, con
  timestamp. È il posto da cui prendere i log se un dev li chiede per una
  segnalazione.
- **Nelle impostazioni c'è una connessione a Claude Desktop.** Non l'abbiamo mai
  provata e potrebbe cambiare il modo in cui lavoriamo, perché darebbe accesso
  diretto ai dati locali di Wyldfire invece che al sito. Da esplorare quando ci
  sarà tempo.
- **I bug di Wyldfire hanno un canale Discord separato**,
  `wyldfire-bugs-and-support`, distinto da `bugs-and-support` che è del sito.
  I nostri sono tutti del sito.
