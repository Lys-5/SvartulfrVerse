# Audit completo delle 86 Character — 3 settembre 2026

Scansione fatta sull'intero dataset in un colpo solo, non aprendo le schede una per una: agganciando `window.fetch` e leggendo la risposta che l'app stessa riceve da `/api/worlds/characters/world/<id>`. Metodo riutilizzabile per i prossimi audit.

---

## Quadro generale

| Stato | Numero |
|---|---|
| **Completi** (description + outfit + RPG) | 35 |
| **Scritti ma grezzi** (description sì, outfit e RPG no) | 25 |
| **Vuoti** (segnaposto senza description) | 25 |
| Totale | 86 |

---

## 1. Regola 13 — `{{user}}` — LA REGOLA COME L'HO SCRITTA È SBAGLIATA

14 schede contengono `{{user}}`, ma **non sono tutte violazioni**. Ce ne sono due tipi completamente diversi, e la §13 che ti ho appena dato non li distingue. Il punto 5 ("verificare che non compaia più la stringa `{{user}}` in nessun campo") **è da correggere**, perché applicato alla lettera distruggerebbe le schede di famiglia.

### Tipo A — corretto, NON toccare (10 schede)

Sono schede scritte apposta per questo World, dove `{{user}}` **è** Alyssa per costruzione. Qui `{{user}}` è il modo giusto di scriverlo, e in diversi casi è addirittura la salvaguardia.

| Scheda | Uso |
|---|---|
| Erik Douglas | "NEVER: Pursue romantic or sexual involvement with `{{user}}`, hard-blocked" — è un blocco protettivo, va tenuto |
| Malachia | "`{{user}}`'s silent bodyguard", ammorbidimenti solo verso di lei |
| Noah | "NEVER write Noah into any romantic or sexual content involving `{{user}}`, siblings, non-negotiable" |
| Jasper | "`{{user}}`/Alyssa's twin brother", equivalenza esplicita |
| Alyssa | "`{{user}}`'s fixed identity in the first scenario", è la nota di design |
| Logan | "the only adult `{{user}}` can be around without feeling managed" |
| Wulfnic | "`{{user}}`'s 1199-year-old grandfather" + hard-block nonno |
| Nixara | "the twins Jasper and `{{user}}`/Alyssa" |
| Ut Berg | "calling `{{user}}` little wolf or pup" |
| Zefir | "guards `{{user}}` and Wulfnic's other descendants" |

### Tipo B — da correggere (4 schede)

| Scheda | Problema | Azione |
|---|---|---|
| **Fade Greymoor** | `"cooking for partner {{user}}"` | Import con `{{user}}` come **partner romantico**. Fade è uno studente della Class of 2024: così è fidanzato con Alyssa per default. Generalizzare o rimuovere |
| **Sullivan "Sully" Jones** | `"now protects {{user}}"`, `"protective, avuncular/teasing dynamic"` | Import da Los Angeles con `{{user}}` come assistito. Relazione fabbricata, Alyssa non c'entra nulla con lui. Generalizzare il ruolo |
| **Edric Douglas** | `"If {{user}} is male he mimics posture... if {{user}} is female he harbors a transparent, painfully obvious childhood crush"` | **Due problemi.** Primo: tratta `{{user}}` come di genere variabile, il che contraddice `{{user}}` = Alyssa, fissato ovunque altrove. Secondo: il ramo femminile dà a un dodicenne una cotta per la cugina. Da riscrivere collassando sul solo caso Alyssa e togliendo la cotta |
| **Scarlett Rose** | `"With {{user}}, depending on how the dynamic runs, she is either a..."` | Non è pericoloso, è solo scritto a metà: lascia la relazione indefinita invece di deciderla. Da chiudere |

### Correzione da fare alla §13

Il punto 5 va sostituito con:

> 5. **Distinguere i due usi di `{{user}}` prima di toccare qualcosa.** Nelle schede scritte per questo World `{{user}}` **è** Alyssa per costruzione, e va lasciato: è così che sono scritti i legami familiari e i blocchi protettivi ("NEVER pursue romantic or sexual involvement with `{{user}}`"). La regola vale solo sugli **import**, dove `{{user}}` arriva dalla card originale come partner, cotta o assistito di uno sconosciuto. La verifica finale non è "zero occorrenze di `{{user}}`", è "nessuna occorrenza che fabbrichi una relazione che nel World non esiste".

---

## 2. Regola 7 — Start / End Position

**82 schede su 86 non hanno Start Position.** Ne hanno solo quattro:

| Scheda | Start | End |
|---|---|---|
| Lord Cornelius Douglas | 7289808 | 9264072 ✅ deceduto |
| Nixara Bloodmoon | 10303656 | 10565496 ✅ deceduta |
| Dullahan | 8099616 | — |
| Barkley Rover | 10450560 | — |

I due deceduti sono già a norma. Il resto è backlog puro: serve la data di nascita di ognuno, e per molti non è nelle fonti. Suggerisco di farlo a blocchi, partendo da famiglia e branco dove le date le abbiamo.

**Global Character: tutte e 86 sono ON.** Questo è a posto, nulla da fare.

---

## 3. Regola 3 — em-dash residui

12 schede. Sono tutte precedenti all'adozione della regola.

| Scheda | Occorrenze |
|---|---|
| **Erik Douglas** | **15** |
| Santiago Herrera | 4 |
| Bailey Rogers | 3 |
| PRIDE - Jean-Luc Virtuoso | 2 |
| Elizabeth Duskwood | 2 |
| Logan Douglas | 2 |
| Mackenzie Sanchez Rogers, Fade Greymoor, Roland Vickers, Andrew Campbell, Vincent Campbell, Magnus Douglas III | 1 ciascuna |

Sono sostituzioni meccaniche, si fanno in blocco con Search & Replace.

---

## 4. Item e veicoli

**Esistono 7 Item e 7 Vehicle. Zero Creature, zero Furniture.**

| Tipo | Presenti |
|---|---|
| Item | Zefir's Blade, Ut's Warhammer, Wireless Earbuds, Keys, Wallet, Lighter, Smartphone |
| Vehicle | Jasper's Porsche, Noah's Sedan, Logan's Harley, Wulfnic's Rolls-Royce, Erik's SUV, Malachia's Motorcycle, Alyssa's Yellow Beetle |

**Solo 14 personaggi su 86 hanno un inventario**, e sono tutti famiglia e branco: Erik, Logan, Malachia, Noah, Jasper, Alyssa, Edric, Wulfnic, Ut, Zefir, Magnus, Elizabeth, Kaladin, Marcus Thornfield.

**Tutti i ~20 NPC scritti in questa sessione hanno inventario vuoto:** Finn, Bailey, Loewe, Iordan, Casey, Nikolaj, Tate, Oskar, Miles, Rafael, Kade, Ariadne, Dullahan, Barkley, più i Thompson e i Davies.

### Da creare per coprire il registro

- **Item base mancanti**: zaino, cuffie over-ear, blocco da disegno, laptop, borraccia, tessera universitaria, mazzo di chiavi della confraternita.
- **Item firma mancanti** (Key Item, senza prezzo): ascia a uncino di Dullahan, macchina fotografica di Casey, fischietto di Barkley, sacca da hockey di Finn.
- **Creature**: la categoria è a zero, e ci servono almeno i gatti di Dullahan.
- **Furniture**: a zero, per ora non urgente.

---

## 5. NPC da aggiungere alla to-do

### Confermati mancanti dal World

| Nome | Da dove | Note |
|---|---|---|
| **Professor Allen Albarn** | scheda Casey | Professore di fotografia SUCC, suo capo |
| **Ves** | scheda Iordan | Squalo antropomorfo, coinquilino |
| **Maren** | scheda Iordan | Presidente della SHA, donna orca con zanne forate |
| **Matilda Williams** | scheda Casey | Nonna di Casey, **deceduta: Start + End Position** |
| **Elio Warren** | scheda Tate | Demihuman cane, l'unico amico di Tate |
| **Dr. Henry Ross** | scheda Oskar | Centauro, medico e terapeuta di Oskar |
| **Sharky** | scheda Barkley | Il creditore. Non serve una card piena, può bastare un Lexicon: funziona meglio come minaccia fuori campo |

### Già presenti ma da lavorare

Andrew Campbell (3.434 car. grezzi) e **Vincent Campbell (5.317 car. grezzi)**. Vincent è il fratello e il capitano dei Bears: conviene farlo subito dopo Andrew, i due si reggono a vicenda.

### Fratelli Thompson

Presenti: Hank, Jasmin, Janice, Jared, **Jake**. Mancano quindi cinque dei sei che avevamo in lista: **Jaiden, Jason, Jeremy, Jet, Jerry, Julie** meno Jake che c'è già. Da verificare quale sia la lista giusta.

---

## 6. Le 25 schede vuote

Segnaposto senza description, tutti da scrivere quando serviranno:

Mackenzie Sanchez Rogers, Allegra Lumsden, Luisa Sanchez Rogers, Viola Carter, Dominic Rogers, Fade Greymoor, Roland Vickers, Everett Rottmore, Damien Bishop, Cato, Vasile Ionescu, Alistair DeVille, Sullivan "Sully" Jones, Daniel "Danny" Boone, Harper Aries, Ruaraidh "Rory" Ballantine, Alicia Virtuoso, Elizabeth Duskwood, e i sette Peccati (SLOTH Arthur, GLUTTONY Kevin, WRATH Zero, ENVY Siobhan, GREED Roxie, LUST Dante, PRIDE Jean-Luc Virtuoso).

Nota: **Fade Greymoor e Sullivan Jones sono in questa lista e sono anche fra i Tipo B della regola 13.** Nel loro caso il `{{user}}` sta nel campo `summary`, che è pieno mentre la description è vuota. Si sistemano quando si scrivono, non serve un passaggio dedicato.

---

## 7. Le 25 schede grezze da lavorare

Hanno description ma niente outfit né RPG. Sono import mai passati in pipeline:

Aris Thorne, Talia Grimwood, Javier Sinclair, Jake Thompson, Brittany Willow, Archer Wolfwood, Federico "Riki" Savini, Isobel Blackwater, Eclipse Noir, Dominic Chen, Cass Harrow, Aurora Night, Bianca Rossi, Vito Marino, Warg, Tomas Matthews, Chase Anderson, Angelo Moreno, Sierra, Scarlett Rose, Rev, Graham Purcell, Santiago Herrera, **Andrew Campbell**, **Vincent Campbell**.

Graham Purcell è uno dei quattro sopravvissuti Gamma-7 con Miles, Rafael e Kade: gli altri tre sono già completi, lui no.
