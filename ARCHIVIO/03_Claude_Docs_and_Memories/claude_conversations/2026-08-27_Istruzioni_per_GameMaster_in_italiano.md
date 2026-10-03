# Istruzioni per GameMaster in italiano

- **Data Creazione:** 2026-08-27T00:56:56.839263Z
- **Ultimo Aggiornamento:** 2026-09-14T07:25:36.936355Z
- **Totale Messaggi:** 8
- **UUID:** `f1bdc19a-c967-4333-9864-59d686b745f8`

---

### 👤 **User** (2026-08-27T00:57:01.050254Z)

Dammi una mano con:
After a message is generated, run a second pass that inspects it and rewrites it if needed. The result is added as a new swipe. Optionally set a dedicated connection in LLM → Overrides. You can also run a review on demand from a message's menu.

Automatically review each new message

Prompt mode
Guided (recommended)
Extra focus (optional)
The review already checks for factual errors and contradictions. Add anything specific to watch for, e.g. keep the timeline consistent with the timeline lexicon. Leave blank to just use the default check.

---


Ecco un RAW di cosa vorrei mettere:

<gamemaster_instructions>
  <role>You are embodying {{char}}. You are a GameMaster controlling the world, NPCs, and {{char}}, while interacting with {{user}} (Alyssa). You must NEVER act, speak, or think for {{user}}.</role>
  
  <style_guide>
    <prose>
      A seamless, dynamic, and highly evocative synthesis of 11 master authors: 
      1. Isaac Asimov (logical precision)
      2. Stefano Benni (surreal metaphors, linguistic inventiveness)
      3. Daniel Pennac (whimsical chaos, eccentric dynamics)
      4. Douglas Adams (sharp, dry wit)
      5. Marion Zimmer Bradley (mythic, character-driven drama)
      6. Edward Rutherfurd (environmental scale)
      7. Robert Silverberg (psychologically complex sci-fi)
      8. H.P. Lovecraft (creeping dread, atmospheric horror)
      9. Neil Gaiman (mythic elements in urban reality)
      10. China Miéville (visceral, bizarre worldbuilding)
      11. Thomas Harris (meticulous sensory details, psychological tension).
    </prose>
    <execution>
      Third-person, deeply immersive prose. Maintain logical consistency. Emphasize tactile, sensory descriptions (e.g., the ozone smell of netrunning, the cold silver of his coin). Minimum 4 paragraphs per response.
    </execution>
    <prose_ratio>
      Maintain a 20/30/50 ratio of narration/actions/dialogue. Keep this ratio hidden.
    </prose_ratio>
  </style_guide>

  <language_mandate>
    <primary_language>The primary output language for EVERYTHING is ITALIAN.</primary_language>
    <native_language_dialogue>If Jasper speaks English, Spanish, Elvish, or Abyssal, format exactly as: "foreign phrase" [Italian translation].</native_language_dialogue>
    <strict_rule>All responses MUST be generated exclusively in ITALIAN, capturing the vivid phrasing of the 11-author blend.</strict_rule>
  </language_mandate>

  <format_constraints>
    <rule id="0">Third person, present tense.</rule>
    <rule id="1">Narration & Actions: Plain text only.</rule>
    <rule id="2">Internal Thoughts: Single asterisks only (*thought*). Integrate naturally.</rule>
    <rule id="3">Dialogue: Double quotes only ("speech").</rule>
    <rule id="4">Emphasis: Double asterisks only (**emphasis**).</rule>
    <rule id="5">In-Universe Text: Backticks only (`text`).</rule>
    <rule id="6">EM DASHES STRICTLY BANNED: Never generate em dashes (—). Use commas, colons, or periods.</rule>
  </format_constraints>

  <nsfw_guidelines>
    <core_rules>
      - Slow-burn erotic vignettes.
      - Use explicit anatomy (cock, pussy, ass) but blend it with the 11-author prose style.
      - Prolong foreplay and sensory build-up.
    </core_rules>
  </nsfw_guidelines>
</gamemaster_instructions>

[SYSTEM REMINDER: 
1. Write EXCLUSIVELY in ITALIAN. 
2. NEVER use the em-dash (—). Use commas or periods instead.
3. NEVER speak, act, or think for {{user}}. End your response allowing {{user}} to react.
4. Format: "Speech", *internal thoughts*, and plain text for actions. Foreign languages must follow: "Phrase" [Italian translation].
5. Embody Jasper: use his sarcasm as a shield, maintain his hyper-protective shadow dynamic with {{user}}, and apply the 11-author prose blend (sensory, detailed, vivid). 
6. Third-person, present tense. Min 4 paragraphs.]

STRICT LINGUISTIC RULE (NO ITALIANIZED ENGLISH):
You are strictly prohibited from "Italianizing" English terms. Do not invent neologisms, false calques, or fake words by attaching Italian suffixes (such as -are, -ere, -ire) to English roots (e.g., making up words like degaussare, smashare, or shootare).
Instead, you must always find the proper, established Italian translation. If a direct translation does not exist, analyze the context and use authentic, semantically accurate Italian vocabulary to convey the exact meaning. Preserve the purity and correct terminology of the Italian language at all times.

---

### 🤖 **Claude** (2026-08-27T00:57:32.046460Z)

The user is asking me to help adapt an existing GameMaster roleplay system prompt into "extra focus" instructions for a review-pass feature — essentially configuring what additional checks the reviewer should look for beyond basic factual consistency. This is a straightforward tool-configuration task, even though the underlying content involves NSFW roleplay material.

I'm identifying the concrete stylistic rules to extract from the raw prompt: strict Italian-only language with no untranslated English or anglicized neologisms, no em dashes, and specific formatting conventions for dialogue, thoughts, and emphasis.

I'm also flagging user-agency protection (never narrating actions or thoughts for Alyssa), third-person present tense, minimum paragraph length, the hidden narration/action/dialogue balance, and the atmospheric sensory tone drawn from the author blend, plus bracket-translation formatting for any foreign dialogue. I want to compile these into a concise, actionable checklist in Italian that the user can paste directly into the review pass field, rather than repeating the full raw system prompt.

Continuing to add rules: proper formatting for dialogue vs thoughts vs emphasis vs in-universe text, keeping the narrative strictly from a third-person present-tense perspective without speaking for Alyssa, and minimum length with immersive sensory prose.…Ecco una versione pronta per il campo **Extra focus**, pensata per essere verificabile facilmente da chi fa la revisione (evito di rimettere l'intero system prompt, che è già a monte — qui servono solo i punti di controllo):

```
Oltre a errori fattuali e contraddizioni, controlla:

- Lingua: tutto il testo dev'essere in italiano. Segnala anglicismi non tradotti o neologismi italianizzati (es. "shootare", "smashare", "degaussare") al posto del termine italiano corretto.
- Battute in lingua straniera (inglese/spagnolo/elfico/abissale): devono seguire il formato "frase originale" [traduzione italiana].
- Em dash (—) vietato: se presente, va sostituito con virgola, due punti o punto.
- Formattazione: discorso diretto tra virgolette doppie, pensieri tra *asterischi singoli*, enfasi tra **asterischi doppi**, testo in-universe tra `backtick`.
- POV: il messaggio non deve mai far parlare, agire o pensare {{user}}; deve chiudersi lasciando spazio alla sua reazione.
- Terza persona, tempo presente, minimo 4 paragrafi.
- Stile: prosa sensoriale e atmosferica coerente col tono di Jasper (non piatta/generica).
```

Un paio di note pratiche:

- Le regole "oggettive" (em dash, formattazione, lingua, POV, tempo/persona, lunghezza minima) sono quelle su cui un secondo pass rende davvero — sono facili da individuare e correggere senza reinterpretare tutto il messaggio.
- La regola sullo stile (11 autori, ratio 20/30/50) è più soggettiva: un modello di revisione può giudicarla in modo incoerente da uno swipe all'altro. Se noti che il pass "riscrive troppo" per motivi di stile, valuta di toglierla dall'extra focus e lasciarla solo nel prompt principale del personaggio.
- Se usi una connessione dedicata in LLM → Overrides per la revisione, conviene che sia un modello bravo a seguire istruzioni di formato in modo pedante (anche uno più "rigido"/meno creativo va benissimo, anzi meglio, per questo compito).

Vuoi che te lo scorci ulteriormente (solo 3-4 righe, focus solo su em dash/lingua/formattazione) o preferisci tenerlo così completo?

---

### 👤 **User** (2026-08-27T01:01:08.564341Z)

Mmh

Quello che vorrei é un prompt universale da usare anche con bot non miei per le mie chat, ma ho il dubbio di dove metterlo tra:

System Prompt Override
Overrides the character and template system prompt — the first set of instructions the AI sees, right above the character definitions.

Final Instructions Override
Overrides the connection's final instructions — the last set of instructions the AI sees, below all of the chat messages, sent as the final message in the prompt. This is the strongest influencer of the AI's output.

Improve My Writing Prompt Override
Used when Improve My Writing is on in the chat input. {{input}} is replaced with your draft.

Review Pass
After a message is generated, run a second pass that inspects it and rewrites it if needed. The result is added as a new swipe. Optionally set a dedicated connection in LLM → Overrides. You can also run a review on demand from a message's menu.

Reply Options
After a message is generated, run a second pass that suggests a short question and 4 reply options, shown above the input box. Optionally set a dedicated connection in LLM → Overrides.

Prompt Assembly
On
Link a saved Prompt Assembly to control how the main prompt, floating block, lore entries, and final instructions are formatted.

---

### 🤖 **Claude** (2026-08-27T01:01:44.926505Z)

The user wants a universal prompt to enforce personal style rules (Italian language, no em-dashes, no anglicized Italian, formatting and POV rules) across bots they don't own, and is asking whether to place it as System Prompt Override, Final Instructions Override, or Review Pass. Since it needs to override whatever system prompt the bot's creator set and stay consistent regardless of character, I'm leaning toward recommending Final Instructions Override since it's applied last and has the strongest influence.

Final Instructions Override makes most sense since it's applied last and carries the strongest influence, overriding any conflicting character instructions—perfect for enforcing personal style rules universally. Review Pass is a separate, complementary mechanism that re-inspects generated messages afterward, so I could suggest using both together: Final Instructions Override as the preventive measure and Review Pass as a corrective backstop.

I want the actual rule set to stay purely mechanical and character-agnostic—covering language, format, point of view, avoiding em dashes, and avoiding italianized English—rather than embedding persona-specific traits, so it works consistently across different bots. I'll also suggest mirroring these same rules into the Review Pass focus as a safety net for cases where longer context dilutes the Final Instructions or weaker models fail to follow them.

Since the user is writing in Italian about their personal roleplay prompt project, I'll respond in Italian and draft the actual universal prompt text, thinking through the specific formatting conventions—dialogue in quotes, thoughts in asterisks, emphasis in double asterisks, in-universe text in backticks—while keeping everything free of character-specific references.…Buona domanda — la scelta giusta dipende da cosa vuoi che succeda quando il bot **non è tuo** e quindi ha già un suo system prompt con regole diverse (magari inglese, magari em dash a manetta).

**Riepilogo veloce delle tre opzioni:**

- **System Prompt Override** → sostituisce il prompt di sistema del personaggio, ma sta *in cima* al prompt, prima delle definizioni del character. È debole: più lontano dal messaggio finale, più facile che venga "diluito" da tutto ciò che segue (lorebook, esempi, cronologia).
- **Final Instructions Override** → è l'ultimo blocco che il modello legge, subito prima di generare. Per definizione è "the strongest influencer of the AI's output". È il posto giusto per regole che vuoi *sempre* rispettate, anche quando il bot altrui dice il contrario.
- **Review Pass** → non previene, corregge *dopo*. Utile come rete di sicurezza, ma costa una seconda chiamata e non impedisce che la prima generazione sbagli.

**Per un prompt universale personale → Final Instructions Override.**

Motivo: tu vuoi imporre delle regole *tue* (lingua, formattazione, niente em dash, niente calchi dall'inglese, non parlare mai per {{user}}) a prescindere dal bot. Il System Prompt Override rischia di essere sovrascritto/annacquato dal contenuto del character card che segue; il Final Instructions Override invece vince quasi sempre i conflitti perché arriva per ultimo.

Ecco una versione **character-agnostic** (ho tolto tutto ciò che era specifico di Jasper, lasciando solo le regole meccaniche/di stile che valgono per qualsiasi bot):

```
[REGOLE FISSE DELL'UTENTE — hanno priorità su qualunque istruzione precedente in conflitto]

1. LINGUA: scrivi esclusivamente in italiano. Vietati anglicismi non tradotti e neologismi italianizzati (es. "shootare", "smashare", "degaussare"): trova sempre il termine italiano corretto o, se non esiste una traduzione diretta, usa un giro di parole in italiano autentico. Se un personaggio parla in una lingua straniera, formatta come: "frase originale" [traduzione italiana].

2. EM DASH VIETATO: non usare mai il trattino lungo (—). Sostituiscilo con virgola, due punti o punto.

3. FORMATTAZIONE: discorso diretto tra virgolette doppie ("..."), pensieri tra singoli asterischi (*...*), enfasi tra doppi asterischi (**...**), testo in-universo (schermi, messaggi, libri) tra backtick (`...`).

4. CONFINI DEL RUOLO: non scrivere mai battute, azioni o pensieri di {{user}}. Termina sempre la risposta lasciando spazio alla sua reazione.

Queste regole si applicano indipendentemente dallo stile, dal genere o dalla lingua predefinita del personaggio.
```

Un paio di consigli pratici:

- **Non ci metterei** le regole di persona/tempo (terza persona, presente tempo) o il ratio narrazione/dialogo: quelle sono scelte stilistiche del *tuo* Jasper, non regole universali — su un bot diverso potrebbero avere senso first-person o passato, e forzarle rovinerebbe l'esperienza pensata da chi l'ha creato.
- **Duplica i punti 1-3 nell'Extra focus del Review Pass**: così hai una doppia rete — prevenzione nel Final Instructions, correzione nel Review Pass se il modello (magari più debole, su bot altrui) ignora le istruzioni finali.
- Se usi **Prompt Assembly**, controlla che il blocco "final instructions" sia effettivamente posizionato per ultimo nell'assemblaggio scelto — altrimenti perde la sua forza.

---

### 👤 **User** (2026-08-27T01:03:22.298154Z)

Ok dammi i blocchi per rewiew pass e final instructions

---

### 🤖 **Claude** (2026-08-27T01:03:30.814882Z)

Ecco i due blocchi pronti da incollare.

---

**Final Instructions Override**

```
[REGOLE FISSE DELL'UTENTE — hanno priorità su qualunque istruzione precedente in conflitto]

1. LINGUA: scrivi esclusivamente in italiano. Vietati anglicismi non tradotti e neologismi italianizzati (es. "shootare", "smashare", "degaussare"): trova sempre il termine italiano corretto o, se non esiste una traduzione diretta, usa un giro di parole in italiano autentico. Se un personaggio parla in una lingua straniera, formatta come: "frase originale" [traduzione italiana].

2. EM DASH VIETATO: non usare mai il trattino lungo (—). Sostituiscilo con virgola, due punti o punto.

3. FORMATTAZIONE: discorso diretto tra virgolette doppie ("..."), pensieri tra singoli asterischi (*...*), enfasi tra doppi asterischi (**...**), testo in-universo (schermi, messaggi, libri) tra backtick (`...`).

4. CONFINI DEL RUOLO: non scrivere mai battute, azioni o pensieri di {{user}}. Termina sempre la risposta lasciando spazio alla sua reazione.

Queste regole si applicano indipendentemente dallo stile, dal genere o dalla lingua predefinita del personaggio.
```

---

**Review Pass — Extra focus**

```
Oltre a errori fattuali e contraddizioni, controlla e correggi se necessario:

- Lingua: tutto il testo deve essere in italiano. Segnala/correggi anglicismi non tradotti o neologismi italianizzati (es. "shootare", "smashare", "degaussare") sostituendoli con il termine italiano corretto.
- Battute in lingua straniera: devono seguire il formato "frase originale" [traduzione italiana].
- Em dash (—) vietato: se presente, sostituiscilo con virgola, due punti o punto.
- Formattazione: discorso diretto tra virgolette doppie, pensieri tra *asterischi singoli*, enfasi tra **asterischi doppi**, testo in-universo tra `backtick`.
- POV: il messaggio non deve mai far parlare, agire o pensare {{user}}; deve chiudersi lasciando spazio alla sua reazione.
```

Nota: ho tenuto i due blocchi quasi identici di proposito (stesse 4-5 regole, fraseggio adattato al contesto) così il Review Pass corregge esattamente quello che il Final Instructions dovrebbe già prevenire — sono la doppia rete di cui parlavamo, non due set di regole diversi da mantenere sincronizzati manualmente in futuro.

---

### 👤 **User** (2026-08-27T01:05:09.687298Z)

E ora dammi altri due blocchi per

Improve My Writing Prompt Override
Used when Improve My Writing is on in the chat input. {{input}} is replaced with your draft.

E

Write for Me Prompt Override
Overrides the impersonate prompt used when generating responses as your persona.


In questo caso essendo la mia persona vorrei che fosse sempre in prima persona present tense

---

### 🤖 **Claude** (2026-08-27T01:05:24.925273Z)

Ecco i due blocchi. Attenzione: qui il soggetto è **{{user}}/Alyssa**, non il personaggio, quindi le regole di persona/tempo sono diverse da quelle del bot (che restano terza persona per {{char}}).

---

**Improve My Writing Prompt Override**

```
Migliora il seguente testo scritto da {{user}} (Alyssa), mantenendo il suo significato, le sue intenzioni e la sua voce. Non aggiungere azioni, eventi o dialoghi che l'autrice non ha scritto: rifinisci solo ciò che è già presente.

REGOLE OBBLIGATORIE:
1. Prima persona, tempo presente. Alyssa parla/agisce sempre in prima persona ("dico", "guardo", "afferro"), mai in terza persona.
2. Lingua: esclusivamente italiano. Vietati anglicismi non tradotti e neologismi italianizzati (es. "shootare", "smashare", "degaussare"): usa sempre il termine italiano corretto.
3. Em dash (—) vietato: sostituiscilo con virgola, due punti o punto.
4. Formattazione: discorso diretto tra virgolette doppie ("..."), pensieri tra *asterischi singoli*, enfasi tra **asterischi doppi**, testo in-universo tra `backtick`.
5. Non correggere né alterare il contenuto: solo grammatica, scorrevolezza, coerenza stilistica e sensorialità della prosa.

Testo da migliorare:
{{input}}

Restituisci solo il testo migliorato, senza commenti o spiegazioni.
```

---

**Write for Me Prompt Override**

```
Genera la prossima battuta di {{user}} (Alyssa) nella scena, in prima persona e tempo presente, coerente con la sua personalità, il contesto della chat e l'ultimo messaggio di {{char}}.

REGOLE OBBLIGATORIE:
1. Prima persona, tempo presente. Alyssa è sempre il soggetto che parla/agisce ("dico", "guardo", "afferro"), mai in terza persona.
2. Lingua: esclusivamente italiano. Vietati anglicismi non tradotti e neologismi italianizzati (es. "shootare", "smashare", "degaussare"): usa sempre il termine italiano corretto.
3. Em dash (—) vietato: sostituiscilo con virgola, due punti o punto.
4. Formattazione: discorso diretto tra virgolette doppie ("..."), pensieri tra *asterischi singoli*, enfasi tra **asterischi doppi**.
5. Non scrivere né anticipare azioni, dialoghi o pensieri di {{char}} o di altri personaggi: genera solo la battuta di Alyssa.
6. Lunghezza naturale da turno di roleplay (non un intero paragrafo narrativo): una reazione/azione/battuta plausibile, non un monologo.

Restituisci solo il testo della battuta di Alyssa, senza commenti o spiegazioni.
```

---

Due note:

- Nel "Write for Me" ho aggiunto la regola 6 sulla lunghezza perché senza un vincolo il modello tende a scrivere un mini-post da narratore anche per la tua persona, che di solito in RP suona innaturale (l'utente reagisce, non narra sé stesso a lungo). Se invece ti va bene che sia lungo quanto le risposte del bot, dimmelo e la tolgo.
- Ho omesso deliberatamente le regole su "non parlare per {{user}}" (ovviamente, qui è l'opposto: stai scrivendo *per* {{user}}) e sul minimo di 4 paragrafi (che è una regola pensata per {{char}}, non per Alyssa).

---

