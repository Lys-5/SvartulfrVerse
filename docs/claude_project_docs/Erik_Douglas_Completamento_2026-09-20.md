# Erik Douglas — Completamento Scheda (2026-09-20)

Ricostruzione completa della card di Erik Douglas su Wyvern (sito live), a seguito della corruzione causata da un publish difettoso dall'app locale Wyldfire. Lavorazione svolta interamente via browser UI (Claude Browser), niente API diretta e niente app locale, come da istruzione permanente dell'utente.

## Campi ricostruiti/verificati

- **Long Description**: 15165 caratteri, JED+ completo (blocco attributi + BACKSTORY + FAMILY & PACK + VOICE & BEHAVIOR + sezione tematica finale). Verificato pulito: zero `{{user}}`, zero em-dash, zero doppio trattino, zero grassetto markdown. Il sospetto "--" vicino a "Noah" segnalato in una sessione precedente non è mai esistito nel campo Long Description: era uno stale duplicate nel campo Short Description, già superato.
- **Short Description**: 749 caratteri, riscritta da zero con la tecnica JS (nativeSetter su HTMLTextAreaElement + dispatch evento `input`), perché `ctrl+a` non seleziona in modo affidabile nei textarea React di Wyvern.
- **Display Description**: 170 caratteri, già corretta, non toccata.
- **Outfits**: 5 (Casa/Rilassato, DCC/Business, Esterno/In Auto, Full Shift, Hybrid Shift), aggiunti uno alla volta con salvataggio individuale. Default Outfit impostato su "Casa / Rilassato".
- **Dialogue Examples**: 5, riscritti con la disciplina di formattazione del progetto (niente asterischi per la narrazione, solo per pensieri interni; niente em-dash).
- **Attitudes**: 10 totali (Alyssa, Logan, Wulfnic, Kaladin, Magnus III, Malachia, Jasper, Noah come World Character; Court of the Night e Rival Pureblood Houses come Generic).
- **Writing Style & Tone** (= `final_instructions`/post_history_instructions nei termini del progetto): 1274 caratteri, termina con il paragrafo obbligatorio di format discipline.
- **Timeline**: Start Position e Birthdate entrambi = 10009344 (coerenti, come richiesto dal sanity check del World Clock).
- **Pronomi**: corretti da they/them (difettoso) a he/him/his/his/himself.
- **Global Character**: acceso (era spento).

Verifica finale eseguita dopo reload completo della pagina (non solo controllo post-salvataggio), come da §14.12.

## Decisione presa in autonomia: correzione tier Attitudes

Nella fonte locale (`erik_full.json`, dump da `live_delete2.db`), le Attitudes di **Alyssa, Malachia, Jasper e Noah verso Erik** erano taggate `romantic_interest`. Si tratta chiaramente di un artefatto di data-entry di una sessione precedente: sono rapporti padre-figli, non romantici.

Wyvern non ha un tier dedicato per i legami familiari. La scheda di Erik aveva già "Best Friend" (`best_friend`) usato correttamente per Logan (fratello/Beta) e Wulfnic (suocero/figura paterna), cioè legami stretti non romantici. Per coerenza è stato applicato lo stesso tier "Best Friend" ai quattro rapporti padre-figli, mantenendo intensità e reasoning originali:

- Alyssa → Erik: Best Friend, 100
- Malachia → Erik: Best Friend, 90
- Jasper → Erik: Best Friend, 82
- Noah → Erik: Best Friend, 80

Questa è una correzione di dato palesemente errato (non un giudizio soggettivo), fatta in autonomia sotto istruzione "procedi". Da tenere presente: se in futuro Wyvern introducesse un tier familiare dedicato (es. "Parent/Child"), queste quattro Attitudes andrebbero rimappate.

## Nota aperta, non ancora decisa

Il campo Short Description di Erik usa un formato prosa ALWAYS/NEVER/REMEMBER invece del blocco PList puro previsto da §2 delle istruzioni di progetto per il campo `personality`/`summary`. È stato mantenuto così com'era nella fonte (dato pre-esistente, già rivisto in sessioni precedenti), non riformattato d'ufficio. Da chiedere all'utente se va uniformato al formato PList in una passata successiva, per Erik e per altre schede pre-esistenti con lo stesso pattern.

## Stato pipeline

Erik Douglas: **completo**, tutti i passi di §14 verificati dopo reload. Prossimo personaggio nell'ordine di priorità approvato: **Jasper Douglas Bloodmoon**.
