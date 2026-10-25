import os

with open('GEMINI.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = """### Regola di Lys per Entry Monopersonaggio
Ogni voce di Lexicon focalizzata su un singolo personaggio (Intimacy Profiles, Digital Interactions, ricordi personali, note comportamentali):
1. **Entry Type = Memory** (`type: "memory"`);
2. Collegata all'id attuale del personaggio tramite **Attached Character** (`attached_world_character_id`).
3. Le memorie corali (eventi collettivi, log di gruppo) rimangono senza Attached Character."""

replacement = """### Regola di Lys per Entry Monopersonaggio
Ogni voce di Lexicon focalizzata su un singolo personaggio (Intimacy Profiles, Digital Interactions, ricordi personali, note comportamentali):
1. **Entry Type = Memory** (`type: "memory"`);
2. **Vincolo `attached_world_character_id` nei World con Linked Characters:** Se il World adotta i **Linked Characters** collegati da `/characters/mine` (Single Source of Truth), il campo `attached_world_character_id` deve essere impostato **TASSATIVAMENTE a `null` / `None`**. È vietato inserire ID di Character Card esterne in questo campo, poiché il backend Mongoose di Wyvern accetta esclusivamente ID di `WorldCharacter` embedded nel medesimo World (pena errore `HTTP 500: attached_world_character_id must reference a WorldCharacter in the same world`). La soppressione di collisione bot/giocatore si attua esclusivamente tramite gli array nativi `ignored_characters` e `ignored_personas`. Nei World con personaggi interni embedded, rimane valido il collegamento all'id del `WorldCharacter`.
3. Le memorie corali (eventi collettivi, log di gruppo) rimangono senza Attached Character."""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('GEMINI.md', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(text)
    print("GEMINI.md updated successfully!")
else:
    print("Target not found in GEMINI.md")

rule_path = os.path.join('.agents', 'rules', '08_triage_lorebook_e_lexicon.md')
with open(rule_path, 'r', encoding='utf-8') as f:
    rule_text = f.read()

target_rule = """### Regola di Lys (Entry Monopersonaggio)
Ogni entry Lexicon che gravita attorno a un singolo personaggio (Intimacy Profiles, Digital Interactions, dinamiche personali, memorie biografiche):
1. Deve avere **Entry Type = Memory** (`type: "memory"`);
2. Deve essere associata al personaggio tramite il campo **Attached Character** (`attached_world_character_id`).
3. Le memorie che coinvolgono coralmente più personaggi (eventi collettivi, rituali, log di gruppo) restano senza Attached Character."""

replacement_rule = """### Regola di Lys (Entry Monopersonaggio)
Ogni entry Lexicon che gravita attorno a un singolo personaggio (Intimacy Profiles, Digital Interactions, dinamiche personali, memorie biografiche):
1. Deve avere **Entry Type = Memory** (`type: "memory"`);
2. **Vincolo `attached_world_character_id` nei World con Linked Characters:** Se il World adotta i **Linked Characters** collegati da `/characters/mine` (Single Source of Truth), il campo `attached_world_character_id` deve essere impostato **TASSATIVAMENTE a `null` / `None`**. È vietato inserire ID di Character Card esterne in questo campo, poiché il backend Mongoose di Wyvern accetta esclusivamente ID di `WorldCharacter` embedded nel medesimo World (pena errore `HTTP 500: attached_world_character_id must reference a WorldCharacter in the same world`). La soppressione di collisione bot/giocatore si attua esclusivamente tramite gli array nativi `ignored_characters` e `ignored_personas`. Nei World con personaggi interni embedded, rimane valido il collegamento all'id del `WorldCharacter`.
3. Le memorie che coinvolgono coralmente più personaggi (eventi collettivi, rituali, log di gruppo) restano senza Attached Character."""

if target_rule in rule_text:
    rule_text = rule_text.replace(target_rule, replacement_rule, 1)
    with open(rule_path, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(rule_text)
    print("08_triage_lorebook_e_lexicon.md updated successfully!")
else:
    print("Target not found in 08_triage_lorebook_e_lexicon.md")
