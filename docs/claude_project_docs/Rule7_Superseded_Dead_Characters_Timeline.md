# ⚠️ Regola #7 sostituita — Timeline dei Character e piazzamento globale

**Decisioni di Lys, 02/09/2026.** Questo documento **sostituisce** la riga della regola #7 delle istruzioni di progetto sui personaggi deceduti.

> Le istruzioni di progetto contengono ancora il testo vecchio. Vanno modificate a mano nelle impostazioni del progetto: io posso scrivere documenti, non le istruzioni.

## Regola #7 — testo nuovo

**Tutti i personaggi vanno inseriti come Character**, vivi o morti. Il motivo per cui la vecchia regola mandava i deceduti in Lexicon (evitare che comparissero troppo facilmente in scena) è risolto dalla piattaforma stessa, che dà a ogni Character un arco temporale di presenza.

| Stato | Start Position | End Position |
|---|---|---|
| **Vivo** | **valorizzata** (ora di nascita) | vuota |
| **Deceduto** | valorizzata (ora di nascita) | **valorizzata** (ora di morte) |

Il resto della vecchia regola #7 (Species_Details e Intimacy Profile non si importano, personaggi vivi ricorrenti una volta sola, doppioni di Location, attività senza luogo fisico in Lexicon) **resta valido**.

## Formula del World Clock (verificata con calcolo indipendente)

World-age 0 = **1 gennaio 800 d.C., ore 00:00**, calendario gregoriano prolettico.

```python
from datetime import date
def wyvern_hours(y, m, d):
    return (date(y, m, d) - date(800, 1, 1)).days * 24
```

**Riscontri esatti, all'ora:**

| Personaggio | Data | Ore | Campo |
|---|---|---|---|
| Nixara Bloodmoon | 9 giugno 1975 | `10303656` | Start |
| Nixara Bloodmoon | 22 aprile 2005 | `10565496` | End |
| Lord Cornelius Douglas | 14 agosto 1631 | `7289808` | Start |
| Lord Cornelius Douglas | 3 novembre 1856 | `9264072` | End |

Il campo **Birthdate** (Year / Month / Day) è separato dalla Timeline e alimenta l'age tracking: va compilato comunque, e Wyvern calcola da sé il giorno della settimana.

### Backfill da fare

Con la regola nuova **anche i vivi vogliono la Start Position**, che oggi è vuota su tutti (verificato su Alyssa e Jasper). È un backfill su ~84 schede e richiede la data di nascita di ciascuna: molte schede hanno il Birthdate compilato, da lì la Start si ricava con la formula sopra. **Non ancora eseguito.**

## Piazzamento dei personaggi: tutti globali

**Decisione sostitutiva rispetto al piano dei Character Pool.** Popolando i pool degli Environment è emerso che vanno inseriti quasi tutti i personaggi ogni volta, quindi il pool non filtra niente e aggiunge solo peso.

**Nuova regola: tutti i Character vanno su `Global Character` = ON**, dato che condividono comunque la stessa area geografica. I Character Pool di Environment e Location restano disponibili ma non si usano come metodo di piazzamento predefinito.

Questo supersede il piano descritto in `Character_Pool_Placement_Gap.md`, che resta valido solo come documentazione del **meccanismo** (il pool della Location si somma a quello dell'Environment, confermato da wiki).

## Nessuna pulizia retroattiva sul Lexicon

Enumerate tutte le 122 entry del Lexicon in cerca di deceduti inseriti come surrogati sotto la vecchia regola: **non ce ne sono**. Le uniche entry riferite a persone sono di supporto a personaggi vivi (Intimacy Profile, Species_Details, Digital Interactions, note famiglia). Nixara e Cornelius erano già Character con Timeline.

## Correzione di coerenza applicata

Alyssa e Jasper hanno Birthdate **22 aprile 2005**, lo stesso giorno della End Position di Nixara: i gemelli sono nati il giorno in cui è morta la madre. Quindi **nell'agosto 2024 hanno 19 anni**, valore già corretto in tutte le schede.

Ne derivava però un divario sbagliato con Finn (22 anni): tre anni, non quattro. Corretto su tre schede:

| Scheda | Prima | Dopo |
|---|---|---|
| Finnegan Novak | "She was thirteen and he was seventeen" | "She was fourteen and he was seventeen" |
| Finnegan Novak | "spent four years quietly grateful" | "five years" |
| Alyssa | "She was thirteen and her body had started" | "She was fourteen and her body had started" |
| Alyssa | "left it for four years" | "five years" |
| Alyssa | "carried that sentence for four years" | "five years" |
| Jasper | "carrying it by himself for four years" | "five years" |
| Jasper | "quietly furious about it for four years" | "five years" |

Timeline risultante coerente: rottura con Finn nell'ultimo anno di liceo di lui (17 anni, lei 14, ~2019), lui parte per la SUCC quell'autunno, lei entra alle superiori, e nell'agosto 2024 sono passati cinque anni.

## Personaggi da creare, rimandati a fine lavori

Su indicazione di Lys si completano prima i principali.

| Nome | Tipo | Note |
|---|---|---|
| **Professor Allen Albarn** | Character | Professore di fotografia SUCC, 50 e passa, sale e pepe, occhi azzurri, alto e allampanato, distratto, gentile. Casey è il suo TA. |
| **Ves** | Character | Coinquilino e migliore amico di Iordan Vess. Squalo antropomorfo, illustratore freelance. |
| **Maren** | Character | Presidente della SHA, donna orca tozza con zanne forate. Casey è il suo tesoriere. |
| **Matilda Williams** | Character **con End Position** | Nonna di Casey, deceduta. Date di nascita e morte non fornite dalle fonti, da decidere. |
