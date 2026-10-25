with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = """  - Verifica indipendente al 100% positiva tramite script automated GET e asserzione di parità strutturale (`scratch/independent_verify_15lb.py`)."""

replacement = """  - Verifica indipendente al 100% positiva tramite script automated GET e asserzione di parità strutturale (`scratch/independent_verify_15lb.py`).
- **Consolidamento Regole e Distillazione Skill (/learn + /workflow-skill-creator)**:
  - Aggiornata la Regola 11 (`.agents/rules/11_wyvern_api_sicurezza_e_bug.md`) con la Sezione 11 sulle specifiche tecniche dei Character Scenarios (suite 15 Lorebook, per-greeting `linked_persona_ids`, requisito `can_fork: true` anti-HTTP 400 e gestione incrementale `revision` anti-HTTP 409).
  - Aggiornata la Regola 13 (`.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md`) con la mappatura ufficiale delle Persona offerte (Dual su Villa Douglas, Camp Mystic, DMHA, Underworld; Singolo su rotte SUCC; Misto sul Master Scenario).
  - Sincronizzato `GEMINI.md` (§ 7 e § 18) per riflettere stabilmente la nuova architettura a 15 Lorebook.
  - Estesa la skill `.agents/skills/wyvern-ttrpg-master-deployer/` integrando il modulo `scripts/sync_scenarios_suite.py` per l'aggiornamento e la validazione di massa dei Character Scenarios."""

assert target in text, "target not found in CHANGELOG.md"
text = text.replace(target, replacement)

with open('CHANGELOG.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("CHANGELOG.md updated successfully!")
