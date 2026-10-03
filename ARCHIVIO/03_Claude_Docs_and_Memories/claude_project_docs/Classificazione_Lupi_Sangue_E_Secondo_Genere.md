# Classificazione dei lupi: sangue e secondo genere

Aperto il 2026-09-08. Due cose: una regola chiusa e scritta nel World, e una
coda di lavoro su ventotto personaggi.

---

## 1. CHIUSA: la diluizione Pureblood verso Common è canon

Confermata dall'utente e **scritta nella entry Lexicon `LSE Blood
Classification`** (`_YXE9bXrzBjzz1L9a31Y66`). Non è più "in calibrazione": il
documento `Mac_Pureblood_E_Diluizione_In_Calibrazione.md` è superato su questo
punto e va letto solo per la costruzione del personaggio.

Aggiunte due righe alla lista INHERITANCE RULES, in posizione, subito dopo
`Pureblood + Pureblood = Pureblood`:

```
- Pureblood of the 1st or 2nd generation + Common = Pureblood.
- Pureblood of the 3rd generation or later + Common = Common Bloodline.
```

E una terza conseguenza in coda alle due che c'erano già: **Common non è un tipo
di lupo diverso, è una linea Pureblood diluita oltre il punto di non ritorno**, e
il conteggio funziona esattamente come un gradino sopra. È il motivo per cui i
Common sono la stragrande maggioranza e per cui la classificazione non è visibile
da fuori: il confine lo attraversa gente comune che sposa gente comune, di solito
senza che nessuno nella stanza sappia che ci fosse un confine.

La simmetria con la regola Founding è ora completa: due generazioni di grazia,
poi si scende e non si risale, a ogni gradino della scala.

---

## 2. La coda di lavoro

Scansione di tutte le 92 schede del World, filtrando i licantropi: **42
personaggi**, di cui **14 completi** e **28 da classificare**.

Completi (sangue e secondo genere entrambi dichiarati): Cornelius, Zefir, Ut,
Archer Wolfwood, Alyssa, Nixara, Edric, Jasper, Noah, Elizabeth, Magnus III,
Malachia, Erik, Logan. Cioè in pratica tutta e sola la famiglia, più i tre
vecchi e il Rettore.

### Manca tutto, sangue e secondo genere

Dullahan, Chase Anderson, Barkley Rover, Eris Davies, Stanley Davies Sr.,
Stanley Davies Jr., Allegra Lumsden, Luisa Sanchez-Rogers, Daniel "Danny" Boone.

Le ultime tre hanno `long_summary` a zero, quindi sono schede da scrivere, non da
integrare.

### Manca solo il sangue

Federico "Riki" Savini, Isobel Blackwater, Eclipse Noir, Dominic Chen, Cass
Harrow, Aurora Night, Bianca Rossi, Vito Marino, Warg, Marcus Thornfield,
Rafael Callaway, Kade Leavis, Miles Airhardt, Iordan R. Vess, Finnegan Novak,
Kaladin Nargathon, e **Wulfnic Bloodmoon**.

### Manca solo il secondo genere

Mackenzie Sanchez-Rogers, che è appena diventato Pureblood.

---

## 3. Tre avvertenze sulla scansione, prima di fidarsene

**La parola Alpha è ambigua in questo World e la scansione non può scioglierla.**
Vale come secondo genere, come ruolo di comando in un branco, e come titolo
civile nella forma "District Alpha" che portano quasi tutti i personaggi
dell'Underworld di Los Angeles. Ho filtrato le occorrenze esplicite di "District
Alpha", ma restano casi in cui "Alpha" nella scheda è un ruolo e non un sesso
secondario. **Ogni riga della lista va verificata aprendo la scheda**, ed è il
motivo per cui va deciso caso per caso e non a tappeto.

**Wulfnic compare fra chi manca il sangue.** È quasi certamente un buco reale
della sua scheda e non un errore della scansione: è Divine Blood per definizione,
essendo uno dei Nove, e la stringa non compare. Da verificare per primo, perché
se manca sulla sua manca probabilmente anche su altri dei Nove.

**Vincent Campbell è finito nella lista ed è un vampiro.** Falso positivo, la sua
scheda nomina i licantropi fra i dislike. Da ignorare.

---

## 4. La regola che fa risparmiare il lavoro

Non vanno decisi tutti da zero. `Cosa_Solarton_Sa_Delle_Case.md` dice già che **i
lupi di Solarton sono quasi tutti Common Bloodline**, con la linea Wolfwood come
unica eccezione conosciuta e adesso Mac come eccezione che nessuno conosce.

Quindi il default operativo:

- **Solarton e campus**: Common, salvo motivo esplicito. Chase, Iordan, Finnegan,
  i Davies, Allegra, Luisa, Barkley.
- **Los Angeles e Underworld**: da decidere, e qui il default non c'è. Un District
  Alpha che comanda un quartiere può benissimo essere Common, e probabilmente lo
  è, ma quel roster ha una sua struttura di potere che potrebbe volere qualche
  Pureblood in cima. È la decisione più interessante del gruppo e la terrei
  separata.
- **Dullahan** è un caso a sé e non va trattato con gli altri: la sua specie sul
  portale è "dog demi-human (?)" col punto interrogativo dell'autore, e le regole
  di sangue di Blackwood potrebbero semplicemente non applicarsi a lui.

Il secondo genere invece non ha default e va deciso davvero uno per uno. I valori
disponibili, dalla matrice del World: **Enigma, Alpha, Delta, Beta, Gamma,
Omega**.

---

## 5. Come procedere

Suggerito, non deciso: si fa un blocco alla volta per gruppo geografico, si
decide sangue e secondo genere insieme sullo stesso personaggio, e si scrive
subito nel blocco JED+ come campi espliciti, `BLOOD_CLASSIFICATION` e
`SECONDARY_SEX`, così la prossima scansione li trova senza ambiguità invece di
doverli indovinare dalla prosa. È esattamente il problema che ha reso questa
scansione poco affidabile.
