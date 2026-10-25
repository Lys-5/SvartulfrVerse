with open('.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md', 'r', encoding='utf-8') as f:
    text = f.read()

old_personas = """   - **Personas Proposte (`linked_persona_ids`):**
     - **Alyssa** (`["persona_1786335754946"]`) per le aperture `[FemPOV]`;
     - **Jasper** (`["1792155173728"]`, ID interno `user_persona_bGDFCEtKDzVmgbCmHJWEW`) per le aperture `[MalePOV]`;
     - **`[]` (Scelta libera del giocatore)** per le aperture Dual giocabili da entrambi i gemelli;
     - **Echo** (`1791389790053`) disponibile come Persona alternativa tecnomanziale.
     - **Requisito Obbligatorio `can_fork: true`:** Qualsiasi Persona collegata a uno Scenario in `linked_persona_ids` deve avere tassativamente `can_fork: true` per essere accettata da Wyvern (in caso contrario l'API restituisce `HTTP 400: Only your own forkable personas can be offered`)."""

new_personas = """   - **Personas Proposte (`linked_persona_ids`):**
     - **Alyssa** (`["persona_1786335754946"]`) per le aperture `[FemPOV]` e per tutti i greeting della rotta specifica `SUCC Route Alyssa`;
     - **Jasper** (`["1792155173728"]`, ID interno `user_persona_bGDFCEtKDzVmgbCmHJWEW`) per le aperture `[MalePOV]` e per tutti i greeting della rotta specifica `SUCC Route Jasper`;
     - **Entrambi i Gemelli** (`["persona_1786335754946", "1792155173728"]`) per tutti i greeting degli scenari Dual (*Villa Douglas*, *Camp Mystic*, *DMHA Dungeons*, *Underworld Sindacato*) e per le aperture condivise/neutrali del Master Scenario;
     - **Echo** (`1791389790053`) disponibile come Persona alternativa tecnomanziale;
     - **Requisito Obbligatorio `can_fork: true`:** Qualsiasi Persona collegata a uno Scenario in `linked_persona_ids` deve avere tassativamente `can_fork: true` per essere accettata da Wyvern (in caso contrario l'API restituisce `HTTP 400: Only your own forkable personas can be offered`)."""

old_dual_pov = """     - Le aperture Dual giocabili indifferentemente da entrambi i gemelli lasciano `linked_persona_ids: []` e usano `{{user}}` + `{{scenarioChar "twin"}}`."""
new_dual_pov = """     - Le aperture Dual giocabili indifferentemente da entrambi i gemelli offrono entrambe le Persona (`["persona_1786335754946", "1792155173728"]`) e usano `{{user}}` + `{{scenarioChar "twin"}}`."""

old_section3 = """Oltre al Master Scenario Omnibus (`char_scenario_1DC43ggb6mB8YLJDJKrU4`), il Verse dispone di 6 Character Scenarios dedicati e focalizzati per specifiche linee narrative, tutti configurati con `visibility: "private"`, `unavailable_count: 0`, e con i 6 Lorebook Standalone collegati (`lorebook_ids`):"""
new_section3 = """Oltre al Master Scenario Omnibus (`char_scenario_1DC43ggb6mB8YLJDJKrU4`), il Verse dispone di 6 Character Scenarios dedicati e focalizzati per specifiche linee narrative, tutti configurati con `visibility: "private"`, `unavailable_count: 0`, e con la Suite Completa dei **15 Lorebook** (`lorebook_ids` per un totale di 1.173 voci) e Personas offerte (`linked_persona_ids`):"""

text = text.replace(old_personas, new_personas)
text = text.replace(old_dual_pov, new_dual_pov)
text = text.replace(old_section3, new_section3)

with open('.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated rule 13 successfully.")
