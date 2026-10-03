# Sweep completo Entry Type su tutto il Lexicon del World — 2026-09-22

Su richiesta di Lys ("rivedessi tramite API ogni lexicon una per una e assegnassi ad ognuna la giusta Entry Type"), rivista **ogni singola entry Lexicon del World** (253 totali) e assegnato l'Entry Type corretto via API (partial PUT su `type` + `attached_world_character_id` dove pertinente), tutto verificato con GET fresca finale.

## Fonte di riferimento

Il campo Entry Type del **World Lexicon** (Content area → Lexicon, quello con cui lavoriamo su questo Project) è documentato in `wiki.wyvern.chat/en/Features/Worlds/Lexicon`, **non** nella pagina generica `wiki.wyvern.chat/en/Advanced/Lexicon` (quella copre Chat Lexicon e Character Lexicon, una feature diversa con una tassonomia diversa — NPC/Item/Location/Event/Concept/Memory/Other — che non è quella usata dal World Lexicon).

Tassonomia reale del World Lexicon, confermata sia dal testo della pagina sia dai valori raw già presenti via API:
- **No specific type** (default)
- **lore/concept** — testo puro, lore generica/astratta
- **organization/faction** — testo puro, gruppi/organizzazioni
- **memory** — testo puro, ricordi/fatti specifici di un personaggio o di un evento
- **Item**, **Furniture**, **Creature**, **Move**, **Nature**, **Ability** — sbloccano pannelli di configurazione aggiuntivi (RPG/oggetti), coperti in altri capitoli della wiki

## Metodo

1. Estratta via API la lista completa (253 entry) con nome, `type`, `is_global`, `party_conditions`, `attached_world_character_id`, contenuto.
2. Classificate per pattern di nome + lettura di un campione di contenuto per ogni cluster ambiguo (tutte le ~40 entry "LSE ...", "Species_Details - X", "Digital Interactions - X", gli "Intimacy Profile - X" residui, le occupazioni generiche tipo "Teacher"/"Bartender", gli oggetti personali, le entry segrete DDM/Firstborn, ecc.), prima di scrivere qualunque valore.
3. Per le entry `memory` legate a un singolo personaggio, risolto `attached_world_character_id` incrociando `party_conditions` esistenti (quando validi) o il nome esatto/nickname contro la lista Character attuale del World — **mai indovinato**: 7 nomi non risolti automaticamente (Arthur, Sullivan Jones, Rory Ballantine, Romeo Gray Dean, Mac Sanchez-Rogers, Dryden Kîwêtin, Danny Boone) sono stati risolti a mano controllando manualmente la lista Character (es. "Mac Sanchez-Rogers" → Mackenzie Sanchez-Rogers, nickname "Mac"; "Arthur" → Dr. Arthur Sinclair, per distinguerlo da "Arthur Grey" che ha già una propria entry separata).
4. Scritto via PUT parziale (solo i campi che cambiano, mai l'oggetto intero, come da §11) a lotti di 25 per rispettare i limiti di tempo del browser tool, con verifica incrementale.
5. **Verifica finale**: GET fresca dell'intera lista Lexicon del World dopo tutte le scritture.

## Risultato

| Entry Type | Conteggio |
|---|---|
| memory | 112 |
| lore/concept | 108 |
| item | 16 |
| organization/faction | 15 |
| creature | 1 |
| (nessuno, intenzionalmente) | 1 |
| **Totale** | **253** |

Delle 112 `memory`: 92 hanno un `attached_world_character_id` valido (personaggio singolo proprietario), 20 sono correttamente **senza** Attached Character perché coinvolgono più personaggi contemporaneamente (es. eventi datati dell'arco 2024, la chat di famiglia Pack-Family, la gara di costumi dei Cocketeers) o sono meccaniche riproduttive a livello di intera specie (LSE Reproduction & Bonding, Vax - Reproduction and Compatibility) — coerente con la regola di Lys per cui l'Attached Character si usa solo quando l'entry fa riferimento a **un unico personaggio**.

### Le 73 "Intimacy Profile - X" pendenti dalla sessione precedente

Tutte portate a `type: memory` + `attached_world_character_id` risolto sul personaggio corretto, stesso trattamento delle 10 già fatte in precedenza.

### Item (16)
Oggetti posseduti da un personaggio o gruppo: veicoli (Rolls-Royce di Wulfnic, Sedan di Noah, Harley di Logan, Moto di Malachia, SUV di Erik, Maggiolino di Alyssa, Porsche di Jasper), armi (Lama di Zefir, Martello di Ut), oggetti personali (auricolari, portafoglio, accendino, chiavi, smartphone), il trofeo Gerald il Gallo Dorato, e Ambrosia (la sostanza illecita dei Sinners, trattata come oggetto/consumabile).

### Organization/faction (15)
SRF, The Council and The Cause, The Other Contractors, The Five Cocketeers, SERAPHIM, DDM Inc. (The Company), DDM Inc. Departments, BLOODHOUND PMC, Douglas Commercial Coalition (DCC), Ballantine Family, The Sinners, SUCC BULLS, SUCC BEARS, Humans First, Grave Mistake (la band, trattata come collettivo).

### Creature (1)
Asag Beast (unico vero "mostro"/mob della lore, coerente con la definizione wiki "mobs and enemies"; non ha ancora stat/moveset configurati dato che l'RPG è in pausa, §8, ma la categorizzazione resta corretta indipendentemente dal pannello).

### Lore/concept (108)
Tutto il resto: le ~40 entry di riferimento enciclopedico "LSE ..." (biologia, cultura, storia, leggi, glossario del Common Bloodline), le specie generiche (Vax, Sarrow, Weres/Shapeshifters, Vampire, Undead, Fae, Demons, Human, Hybrids, Demi-humans, Primordial, Magic-capable Humans), i miti fondativi e segreti di lore (La Guerra di Fenris, Vélhati e Vélsköll, Project BlackWolf, L'origine vera dei Nove, La Legge di Wulfnic, La casa della Longhouse, Cosa Solarton sa delle Case), il sistema di occupazioni generiche (Teacher, Bartender, CEO, ecc. — confermato via lettura contenuto: sono testo descrittivo del ruolo nel setting, non stub del blueprint RPG Occupation), luoghi non ancora mappati come Location (Dragon's Shortcut, Lunar Quad, Horned Skull Caverns), e i riferimenti di sistema/società (SUCCbook & social media, Supernatural Civil Status, Supernatural Degrees, Frats & Sororities, ecc.).

## Anomalie trovate durante lo sweep (segnalate, non corrette d'ufficio)

1. **"ZZ DEBUG PROBE (temporanea, da cancellare)"** (`_BtDkQkyfbUJ3j6zddVL3c`): unica entry rimasta senza Entry Type, di proposito. È un'entry di debug/test che lo stesso nome dice essere da cancellare. Non l'ho toccata né cancellata: solo Lys decide se eliminarla.

2. **Due coppie di entry duplicate per nome**: "Vax" (`_FQp9r4NrLP4nJqpC1YcwF` e `_j3Wbr6w8QeCWpdQ41eRNh`) e "The Roasted Bean" (`_pFUMj4B4BBnLkfEqJBykg` e `_2b47cJ3UN8fRxPMNbwjk1`), con contenuto molto simile ma non identico tra i due membri di ogni coppia. Entrambe tipizzate `lore/concept` (coerente in entrambi i casi), ma non ho unificato/cancellato nessuna delle due copie: stesso principio già visto con gli orfani Zeera/Ariadne la sessione scorsa, da valutare se meritano un merge.

3. **`is_global: true` su entrambe le entry di meccanica riproduttiva esplicita** ("LSE Reproduction & Bonding" e "Vax - Reproduction and Compatibility"). Il contenuto di "LSE Reproduction & Bonding" in particolare è esplicito (cicli di calore, istinto di accoppiamento, "decisions made during heat are non-consensual"), lo stesso tipo di contenuto che §7 del Project dice dovrebbe essere `is_global: false` per non "sparare ovunque nel World" come già successo con gli Intimacy Profile orfani. Non ho toccato `is_global` oggi (fuori dallo scope esplicito di "assegna il type"), ma è un flag da valutare a parte.

4. **Le tre entry "Species_Details - Malachia/Logan/Erik"** esistono come Lexicon separate nonostante §7 dica esplicitamente di non importarle mai come tali ("già parte della card collegata"). Tipizzate `memory` + Attached Character sul personaggio corretto per coerenza con la richiesta di oggi, ma la loro stessa esistenza come entry indipendenti resta un'anomalia da riconciliare con la card in un secondo momento.

5. **NPC secondari senza una propria Character card**: Vargus, Bartholomew and Madge, Angui esistono solo come Lexicon (tipizzate `lore/concept`) pur essendo personaggi nominati con una loro voce/psicologia. Candidati a diventare Character veri in futuro, non convertiti oggi.

## Verifica

GET fresca finale su tutte le 253 entry dopo le scritture: 252/253 hanno un `type` valido, la sola eccezione è la entry di debug lasciata intenzionalmente intatta. Nessun fallimento di scrittura (0 PUT falliti su 242 scritture totali di questa fase, più le 6 della fase precedente).
