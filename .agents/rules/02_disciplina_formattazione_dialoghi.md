# Regola 02 — Disciplina di Formattazione per Dialoghi ed Esempi

Applicare sempre questa disciplina a `first_mes`, `mes_example`, `alternate_greetings`, Dialogue Examples e a qualunque testo di esempio in-character o narrativo:

1. **Divieto dell'Em-Dash:** Mai usare l'em-dash (`—`). Usare virgole (`,`) o punti (`.`) al suo posto.
2. **Dialogo tra virgolette:** I dialoghi parlati vanno sempre racchiusi tra virgolette inglesi doppie standard (`"..."`).
3. **Azioni e narrazione in testo semplice:** Le azioni, i movimenti e la prosa descrittiva vanno scritti in testo semplice, **SENZA asterischi**.
4. **Uso esclusivo degli asterischi:** Gli asterischi (`*...*`) sono riservati **esclusivamente** ai pensieri interni del personaggio (uso attualmente non ancora sfruttato, riservato per sviluppi futuri).
5. **Lingue straniere:** Riportare la frase originale tra virgolette seguita dalla traduzione tra parentesi: `"Frase originale"` `([traduzione])`.
6. **Divieto di Markdown nei testi del World:** Niente markdown dentro i testi del World. L'uso del grassetto con `**` viola espressamente la regola sugli asterischi. Questo divieto si applica tassativamente anche alle entry Lexicon e alle description di Location ed Environment, non solo ai dialoghi dei personaggi.
7. **Prefisso Dialoghi Secondari / ACE su Nuova Riga (`Firstname:`):** Nei contesti multi-character e negli scenari corali, i cognomi restano ammessi nella prosa narrativa delle scene, ma i dialoghi e le azioni dei personaggi secondari devono iniziare su una nuova riga con il prefisso `'Firstname:'` (es. `Bartholomew: [dialogue/action]`, `Luka: [dialogue/action]`) per attivare lo splitting automatico dei balloon e degli avatar nel client Wyvern.

---

## Istruzione Obbligatoria in `post_history_instructions`

Questa regola va inclusa esplicitamente in coda a `post_history_instructions` (campo `final_instructions` via API) di ogni character card, affinché sia attiva e vincolante durante la chat attiva e non solo negli esempi:

> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. When secondary NPCs or ACEs speak or take action, always output their dialogue on a new line prefixed with 'Firstname:' (e.g., Bartholomew: [dialogue/action], Luka: [dialogue/action]) to trigger avatar headers in chat. Demi-human anatomical discipline: treat species-specific animal traits (e.g. single animal ears for mammals, smooth reptilian hearing and scales for lamias) as the natural norm; never mix species traits (never give wolf ears to lamias or reptiles); never mention, describe, or reiterate the presence, absence, or type of human ears or human anatomy in narrative descriptions."
