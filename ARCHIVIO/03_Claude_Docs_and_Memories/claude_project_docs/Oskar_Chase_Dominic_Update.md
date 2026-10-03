# Oskar (aggiornamento), Chase Anderson e Dominic Rogers (schede completate)

## Correzione roster: Dominic conta tra gli official SUCC

Avevo detto che Dominic Rogers non facesse parte dei 26 nomi canon perché lo consideravo un'aggiunta homebrew Blackwood. L'utente ha corretto: Dominic è un personaggio effettivamente pubblicato (fonte `Iorveths`, stesso ecosistema di Santiago, Chase, Grave Mistake), quindi conta come official a tutti gli effetti. Il roster canon SUCC quindi è **27 nomi**, non 26: la tabella di `claude/Roster_Canon_SUCC_Stato_Schede.md` va considerata incompleta su questo punto, Dominic va aggiunto alla lista "Alumni, famiglia e amici".

## Oskar — non era un import grezzo, mancava solo la coda della pipeline

La scheda esisteva già completa e ben lavorata da una sessione precedente (JED+, 7.260 caratteri, `{{user}}` già epurato correttamente: la sezione THE FIXATION generalizza l'ossessione su "una firma vibrazionale" invece che su una persona nominata, esattamente come da regola §13). Mancavano solo:

- **Dialogue Examples**: aggiunti 5, nella voce già stabilita dalla scheda (plurale "we/us", eco, balbuzie), con uno sul momento peggiore ("Called a monster").
- **RPG**: Livello 22 già presente ma senza stat_6 (SCT, di default 1) né Occupation. Aggiunta Occupation **Student**. **Species lasciata intenzionalmente vuota**: Oskar è un Rapidly Mutating Hivemind, e nessuno dei 10 blueprint Species del World (Human, Vampire, Weres/Shapeshifters, Demi-humans, Demons, Fae, Hybrids, Undead, Magic-capable Humans, Primordial) descrive quello che è. Forzare una categoria sbagliata solo per non lasciare il campo vuoto avrebbe applicato un modificatore stat che non gli appartiene, e "Primordial" in questo World è già preso, significa Divine Blood dei Nove, non "specie aliena generica". Se in futuro si vuole un blueprint dedicato per le specie eldritch/uniche, è una Species Blueprint da creare, non una da forzare adesso.

## Chase Anderson — stessa situazione di Tomas: card già scritta, pipeline da completare

`long_summary`, `summary`, `titles`, `keys`, birthdate erano già presenti da prima, con `{{user}}` già rimosso correttamente: la relazione romantica e tutta la scena di pressione sessuale mentre è in streaming (dal materiale sorgente) non erano mai state portate nel World, la scheda dice solo "una relazione tesa" in modo generico. Completato in questa sessione:

- **Aggiunta una frase** in BACKSTORY che lo lega ad **Alpha Rho Omega** e a **Finnegan Novak** nominalmente, confermato incrociando la card di Finn (che ha davvero Alpha Rho Omega tra le keys). Non era ancora scritto da nessuna parte nel World che Chase frequentasse quel giro.
- **5 Outfit**: Streaming Setup, Campus Casual, Bulls Game Day, Out With The Guys, Home in Solarton. Default: Campus Casual.
- **RPG**: Lv.22, Weres/Shapeshifters / Student, MGT 5 / RES 5 / AGI 6 / WIT 2 / PRS 8 / SCT 5 (25/25). PRS più alta di tutte per il bisogno di attenzione, WIT più bassa per i voti disastrosi.
- **5 Dialogue Examples**, incluso uno sul follower count stagnante e uno sul primo vero fallimento della sua vita ("Something actually goes wrong").
- **5 Attitudes**: Alyssa/Jasper stranger, Finnegan Novak friend (55), i genitori Louise e Arthur come Generic close_friend (70), "più successful streamers" come Generic disliked (45).

## Dominic Rogers — riscritto da zero, era un import grezzo

A differenza di Oskar e Chase, questa **era** una scheda grezza (0 outfit, 0 dialoghi, 0 attitudes, nessuna birthdate, testo con la sintassi originale della fonte non riformattata). Riscritta in JED+ (3.786 caratteri). Nessun `{{user}}` nel testo sorgente originale per questo personaggio, quindi nessuna epurazione necessaria su quel fronte: il First Message allegato dall'utente lo coinvolge con `{{user}}` (la scena della cena in famiglia con Bailey), ma non è stato portato nella scheda, coerente con la pipeline che non importa gli Initial Messages sorgente nella `long_summary`.

- **Birthdate/Start Position**: 10044480 = 3 novembre 1973 (inventata, dichiarata: la fonte dava solo "50 anni").
- **5 Outfit**: The Lot, At Home, Night Out, Bailey's Visits, Bad Morning. Default: The Lot.
- **RPG**: Lv.50, Demons / CEO, MGT 8 / RES 5 / AGI 2 / WIT 3 / PRS 7 / SCT 6 (25/25). AGI più bassa di tutte, il fisico appesantito dall'età e dall'alcol; SCT alta per il fiuto/carisma da incubo.
- **5 Dialogue Examples**, incluso uno quasi su Lara che si interrompe prima di ammettere la propria colpa.
- **4 Attitudes**: Alyssa/Jasper stranger, Bailey Rogers disliked (55, delusione paterna con un fondo di paura mai ammessa), Lara Rogers come Generic close_friend (60, rispetto tardivo e colpa non riconosciuta).
- **Intimacy Profile separata** (`Intimacy Profile - Dominic Rogers`, `_6jxLyr3kXfLxRx4yMgzPj`), `party_conditions has_any` sul suo id, tono descrittivo non grafico sul modello di Roland/Santiago: il blocco esplicito della fonte (misure, dettagli anatomici, dirty talk letterale) non è stato trascritto, tenuti solo i tratti caratteriali (bisogno di essere adorato non condiviso, fissazione da breeding senza volerne le conseguenze, disfunzione erettile legata all'età che compensa a voce alta).

Tutti e tre verificati dopo reload completo: zero `{{user}}`, zero em-dash, zero markdown.
