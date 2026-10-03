# Scenario "Ciao, Sono Logan"

Costruito il 2026-09-07. **Sostituisce la voce 1 di "Cosa manca ancora" in
`claude/Grave_Mistake_Band_Schede.md`**, che lo dava ancora da fare.

- **ID:** `_EyeRqnmmcc89mewWEMVLp`
- **Location:** Sidewinders Bar & Nightclub `_AnjWF2ECxBHFqDtyrzUDR`
- **Environment:** Solarton `_TF4E3geCQfWfeMgrdbXdn`
- **Insertion point:** `10490519`, cioè **venerdì 20 settembre 2024, 23:00**,
  quarta settimana di college
- **Personaggio giocabile:** Alyssa, che a quella data ha **diciannove anni**
- **Character select:** ON. **RPG build:** OFF

**Character pool e pesi:** Mac 100, Logan 90, Alyssa 0 (è la giocabile),
Scarlett Rose 70, Sierra 70, Fade 50, Via 50, Roland 30.

---

## La data: perché settembre e non aprile

Era stata valutata una collocazione fra il 13 e il 22 aprile 2024, come uscita
tra ragazze per festeggiare che Alyssa aveva accettato la proposta di Scarlett di
dividere la stanza. È stata scartata dopo aver controllato le date reali sul
World, ed è un caso da ricordare perché il controllo ha cambiato la decisione.

**Alyssa e Jasper sono nati il 22 aprile 2005** (`birthdate` 10320312 su
entrambi). Il 19 aprile 2024 Alyssa ha ancora **diciotto** anni. **Sierra è nata
l'8 settembre 2005**, quindi anche lei ne ha diciotto in aprile. Scarlett, nata
il 18 novembre 2004, ne ha diciannove.

La scena è un ventiquattrenne che si butta su una ragazza sola al bancone. In
aprile il bersaglio avrebbe avuto diciotto anni e tre giorni al compleanno. In
settembre ne ha diciannove ed è una matricola, che è esattamente lo scenario per
cui §13 esiste e che §13 governa: il puntamento è su Alyssa in quanto personaggio
giocabile dichiarato dallo scenario, non su `{{user}}`, quindi la regola è
rispettata, ma il margine in aprile era troppo stretto.

La cornice dell'uscita fra ragazze è stata tenuta lo stesso, adattata: sono
quattro settimane che Alyssa e Scarlett dividono la stanza, ed è la loro prima
uscita vera.

---

## Da dove viene

È il primo messaggio della variante di Mac Sanchez-Rogers dell'autore
`Iorveths`, ripreso nella struttura per scelta esplicita dell'utente e
riambientato nel World. Il locale è già quello dell'originale, il Sidewinders,
quindi non è stato spostato.

Sequenza mantenuta: pavimento appiccicoso, Mac che galleggia sull'adrenalina del
dopo concerto, il vanto interno sul set (Fade che per una volta non crepa sugli
acuti, Via che ha spaccato, e comunque la vera star era lui), la certezza di
essere stato guardato durante il secondo pezzo, i satiri urtati passando, l'odore
dolce sotto la birra, il bersaglio trovato da solo al bancone, l'incombere, il
gomito sul bancone, e le tre battute nell'ordine: "me lo dici che sono stato
pazzesco o devo indovinare", "ti ho beccata a fissarmi, tesoro, mi chiamo Mac",
"ce l'hai un nome".

## Le modifiche

1. **Il bersaglio è Alyssa, non `{{user}}`.** Lo scenario dichiara Alyssa come
   personaggio giocabile, quindi il puntamento è definito dallo scenario e non
   ricade su chiunque stia giocando. È il modo corretto di riusare materiale
   costruito su `{{user}}` senza violare §13.
2. **Scarlett e Sierra sono con lei** e sono andate in bagno cinque minuti prima.
   Serve a preservare l'unica cosa dell'originale che altrimenti non
   funzionerebbe, cioè "da sola, perfetto".
3. **Logan è l'accompagnatore, ed Erik ha detto di sì solo per quello.** A un
   concerto indie punk uno come Logan dà molto meno nell'occhio di Kaladin o di
   Malachia, e la scena lo dice esplicitamente.
4. **Logan è in scena dalla prima riga, a otto sgabelli di distanza**, con una
   birra quasi intatta. Il lettore lo sa e Mac no: è tutta lì la battuta.
5. **Il registro interno di Mac è stato abbassato.** L'originale lo scrive
   sull'appetito: caccia, bersaglio da acquisire, l'odore che scavalca la parte
   del cervello che ragiona, le pupille dilatate, il ginocchio contro la coscia.
   Quel registro funzionava con un `{{user}}` adulto non definito; puntato su una
   matricola nominata funziona male e non serve alla scena. Mac resta arrogante,
   invadente e convinto: incombe, le toglie mezzo locale dalla visuale, la chiude
   contro il bordo del bancone, dice tutte e tre le battute. La sgonfiata di
   Logan è più efficace contro l'arroganza che contro la fame.
6. **La chiusura.** Logan posa la birra senza sbatterla, si schiarisce la gola,
   arriva senza fretta e si mette **di fianco ad Alyssa, non fra i due**. Nessuna
   dimostrazione di forza, nessun ringhio. "Ciao. Sono Logan." Pausa. Sorso.
   "Suo zio." Coerente con la sua scheda, che chiede lento, ruvido, senza posa.

## Il dettaglio di canon aggiunto

Nell'originale Mac sente "qualcosa di dolce" sotto la birra e lo legge come
disponibilità. Qui il dettaglio resta ma la scena aggiunge una riga: **Mac non ha
la più pallida idea di cosa stia annusando, e ha deciso che vuol dire di sì.** È
coerente con §12, per cui nessun personaggio può dedurre il sangue di un altro, e
trasforma il passaggio più sgradevole dell'originale nella misura precisa di
quanto Mac stia sbagliando su ogni piano. Aggiunta anche la riga che non gli è
passato per la testa che una a quel concerto potesse guardare il palco e basta.

---

## Nota tecnica sul formato Scenario

Struttura di `premade_scenes`: array di `{id, description, scene_text,
time_override}`. Il `scene_text` usa blocchi `=>NomePersonaggio:` per assegnare
la voce, e il nome deve corrispondere a un personaggio del pool. Qui sono tre:
`=>Narrator:`, `=>Mac:`, `=>Logan:`.

**Divergenza deliberata dallo scenario esistente.** "First College Day" apre la
scena con una riga di intestazione in grassetto markdown, che viola §3 (niente
asterischi nei testi del World). Qui data e luogo sono in testo semplice.
Verificato dopo la scrittura: zero em-dash, zero asterischi, zero `{{user}}` nel
testo della scena. Resta da normalizzare "First College Day", che va nella stessa
coda dei trentotto em-dash e dei nomi delle Intimacy Profile vecchie.

Lingua: italiano, come "First College Day". Le quattro schede della band sono in
inglese, come tutte le altre character card. Lo split resta quello, ma prima o
poi va deciso davvero.
