# Censimento del secondo genere, e la scoperta che "Prime" è una fascia d'età

Lavorato il 2026-09-08 leggendo per la prima volta le fonti primarie in
`D:\SvartulfrVerse\Drafts\LSE`, indicate dall'utente e raggiungibili dal bridge.
**Da qui in avanti vanno consultate prima di dedurre**: hanno risposto da sole a
quattro domande che stavo per girare all'utente, e in due casi hanno smentito una
mia proposta.

---

## 1. La scoperta: `Prime` non è un rango né un sottogenere

`LSE_01_Species.md`, tabella del ciclo di vita:

```
| Prime | 40-60 | Peak authority and experience. Often in leadership positions. |
```

**È una fascia d'età**, nella stessa tabella che contiene Infant 0-2, Pup 2-12,
Juvenile 12-14, Adolescent 14-17, Young Adult 17-22, Adult 22-40, Prime 40-60,
Elder 60-100, Ancestor 100+.

Le designazioni della fonte hanno quindi la forma **`<fascia d'età> <sesso
secondario>`**:

| Nella fonte | Vuol dire |
|---|---|
| Erik "Prime Alpha" | Alpha, fascia Prime (55 anni) |
| Logan "Prime Beta" | Beta, fascia Prime (49) |
| Kaladin "Adult Alpha" | Alpha, fascia Adult (22-40) |
| Marcus "Prime Delta" | Delta |
| Erik "Prime Dominant Alpha" (World_Seed) | fascia Prime + sottogenere Dominant Alpha |

**Scrivere `SECONDARY_SEX: Prime Alpha` mescolava due assi**, cosa che il sistema
a sei assi del World vieta esplicitamente. Corretto su Erik e Cornelius.

La fascia d'età **non ha ancora un campo** nel blocco JED+. Se serve, va come
`LIFE_STAGE`, separato. Non l'ho creato.

## 2. Due miei errori, corretti

**Primo.** Avevo detto che "Prime Alpha e Dominant Omega sono usati sulle schede
ma non definiti da nessuna parte". Falso per Dominant e Submissive: i quattro
sottogeneri sono già scritti per esteso nella entry `LSE Secondary Sex
Physiology`. Era vero solo per `Prime`, e per il motivo qui sopra.

**Secondo.** Avevo proposto **Omega per Stanley Davies Jr.**, sulla base del
collare. Sbagliato, e la sua stessa scheda lo diceva già: fra le cose che odia
elenca *"full moons, ruts"*, e più sotto *"He also gets ruts, and hates those
considerably more."* **Il rut è dell'Alpha**, mensile e di 3-10 giorni; l'Omega
ha il calore ogni tre mesi, il Delta non ha rut e il Beta non ha ciclo. Stan è
Alpha, e non era una decisione da prendere ma un dato da leggere.

E il collare regge meglio così: un Alpha che porta un collare da cane e le
piastrine del padre che detesta, che odia i propri rut e si chiude dentro finché
passano, e che ha guardato più di una volta al wolfsbane per smussarli. Non è
sottomissione di natura, è un ragazzo che si mette il guinzaglio da solo perché
nessuno gli ha insegnato un altro modo di gestire quello che è.

---

## 3. Il censimento: 20 personaggi con il campo

| Personaggio | SECONDARY_SEX | Fonte |
|---|---|---|
| Wulfnic, Ut, Zefir | Enigma (Primordial) | Appendice |
| Alyssa | Dominant Omega (White Moon) | Appendice |
| Nixara | Dominant Omega (White Moon) | Appendice |
| Malachia | **Dominant Alpha** | Utente, 2026-09-08 |
| Noah | Delta | Appendice |
| Jasper | Beta | Appendice |
| Edric | Gamma (unpresented) | Appendice |
| Erik | **Dominant Alpha** | World_Seed, "new canon" |
| Logan | Beta | Appendice |
| Magnus III | Alpha | già sulla scheda |
| Cornelius | Alpha | corretto da "Prime Alpha" |
| Elizabeth | Omega | già sulla scheda |
| Archer Wolfwood | Alpha | già sulla scheda |
| Kaladin | Alpha | World_Seed |
| Marcus | Delta | World_Seed |
| Stanley Davies Sr. | Alpha | Utente |
| Stanley Davies Jr. | Alpha | dalla sua stessa scheda, i rut |
| Iordan R. Vess | Delta | Utente |

Famiglia, branco e i tre di Solarton sono completi.

### Discrepanza con la fonte da segnalare (§9.2)

**L'appendice dà Malachia come "Alpha" semplice**, riga 158 di
`LSE_Appendices.md`. L'utente ha stabilito il 2026-09-08 che è **Dominant
Alpha**. Vince l'utente; resta registrato che quel file dice altro e andrà
allineato se viene rigenerato.

Nota di coerenza: Dominant Alpha è definito come *"a mix of Enigma and standard
Alpha traits"*, che è **esattamente l'espressione meccanica della prossimità ai
Nove** scritta oggi in `LSE Secondary Sex Physiology`. Malachia Dominant Alpha
non è un potenziamento arbitrario, è la stessa regola vista da vicino, e spiega
perché a ventotto anni è più forte di suo padre pur essendo anche Erik un
Dominant Alpha: stesso sottogenere, distanza dai Nove diversa.

---

## 4. Kaladin Alpha e Marcus Delta, e cosa comporta

Erano la domanda che avevo lasciato aperta. La fonte risponde: Kaladin è Adult
Alpha, Marcus è Prime Delta.

Il dettaglio che ne esce è pesante. Il programma cercava di forzare lo stato
Enigma, che è la forma non diluita dell'Alpha. **Su Kaladin partiva da un Alpha.
Su Marcus partiva da un Delta**, cioè da un sesso secondario che non ha nessuna
capacità di Comando, per definizione e non per grado.

Il che dà un fondo meccanico alla riga già nella entry sigillata: *"Marcus has no
such quiet, and it is not because he is the more broken of the two. He believes
he is simply worse at being repaired. He is not."* Non era peggio riparato. **Era
il materiale sbagliato in partenza**, e nessuno gliel'ha mai detto.

Non l'ho scritto da nessuna parte: è una lettura, non una fonte, ed è materiale
per la entry sigillata se l'utente la vuole approfondire.

---

## 5. Restano

- Il roster di Los Angeles, rinviato per scelta a quando si lavorano quelle
  schede.
- **I demi-umani non rientrano**: Finn è Arctic Wolf demi-human, Barkley golden
  retriever demi-human, Dullahan "dog demi-human (?)". Il sistema dei sessi
  secondari è dei licantropi. Una mia scansione precedente li includeva ed era
  sbagliata.
- La fascia d'età come campo separato, se la si vuole.

## 6. Metodo, per la prossima volta

Le fonti in `D:\SvartulfrVerse\Drafts\` sono la sorgente più forte per la
biologia e per il cast, sopra qualunque deduzione dalle schede del World, e
finora non erano mai state aperte. In particolare: `Drafts/LSE/` per il sistema,
`Drafts/LSE/LSE_Appendices.md` per le tabelle del cast per Casa,
`Drafts/Core_Docs/World_Seed.md` per le designazioni aggiornate quando
l'appendice è vecchia.

Nota tecnica: la cartella Google Drive `G:\Il mio Drive\SvartúlfrVerse`, con
l'accento, **non si monta** in `device_bash` e va letta con `device_list_dir`.
`D:\SvartulfrVerse` si monta senza problemi.
