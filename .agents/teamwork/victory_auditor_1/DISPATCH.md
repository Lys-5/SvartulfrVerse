## 2026-10-24T20:45:00Z

Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\victory_auditor_1\
Please create your directory and keep all your metadata/progress/handoff files there.

Domain skill available for this task:
`e:\repository\SvartulfrVerse\.agents\skills\wyvern-card-lorebook-sync\SKILL.md`
Please consult and follow this skill.

<original_task>
This is a single self-contained fix; keep it small and focused.
Eseguire l'allineamento degli avatar delle 5 Character Card attive (`Erik`, `Logan`, `Malachia`, `Noah`, `Wulfnic`) con gli asset ufficiali della Gallery del Lorebook, effettuare il deploy live via Wyvern Web API (`PUT /api/characters/:id`) e validare la perfetta parità testuale (1:1 byte-for-byte), visiva e di esclusioni (`ignored_characters`) tra le 8 Character Card e le rispettive voci nei Lorebook Standalone.

Working directory: e:\repository\SvartulfrVerse
Integrity mode: development

## Requirements

### R1. Parità Testuale e Integrità Esclusioni
Verificare e certificare che:
- La descrizione narrativa JED+ delle 8 Character Card attive (`Edric`, `Erik`, `Jasper`, `Logan`, `Mackenzie`, `Malachia`, `Noah`, `Wulfnic`) sia identica byte-for-byte al campo `content` delle rispettive entry nei Lorebook (`Svartulfr - NPC Primary` e `Svartulfr - NPC Secondary`).
- L'array `ignored_characters` di ciascuna delle 8 voci NPC nei Lorebook contenga esattamente l'ID della rispettiva card attiva (`_TbRM3EdxDjHFgqztTbCpL`, `_QPea6g4Q1QfeYCVHCLMPR`, `_t4J9aQNJM36cUKAP4wB4U`, `_T8Ywcr9FEqNf9JxbK6eHP`, `_zn24784jfcchQ7EwCyAnm`, `_RDfz7XzTpM23LpPALVXHM`, `_zFLUjV8aVxQRAfQxGcAcY`, `_HEQQbbRFwKdG8QE2Fh1z1`).
- Le entry di tipo `memory` in Lorebook I e II rimangano attive senza `ignored_characters`.

### R2. Sincronizzazione Avatar Ufficiali Gallery
Aggiornare il campo `avatar` nei file locali `FINAL/*_card.json` e sui server di Wyvern per le 5 Character Card disallineate:
- `Erik Ulfr Douglas` (`_QPea6g4Q1QfeYCVHCLMPR`): `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public` (`erikMain`)
- `Logan Járn Douglas` (`_T8Ywcr9FEqNf9JxbK6eHP`): `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public` (`loganMain`)
- `Malachia Björn Douglas Bloodmoon` (`_RDfz7XzTpM23LpPALVXHM`): `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public` (`mailMain`)
- `Noah Loki Douglas Bloodmoon` (`_zFLUjV8aVxQRAfQxGcAcY`): `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public` (`noahMain`)
- `Wulfnic Bóleygr Bloodmoon` (`_HEQQbbRFwKdG8QE2Fh1z1`): `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public` (`mainWulfnic`)

### R3. Deploy Live e Collaudo Contratti
- Effettuare il salvataggio live via `PUT /api/characters/:id` con token aggiornato e verificare HTTP 200 su tutte le chiamate.
- Eseguire la suite di collaudo contratti `scripts/verify_npc_schema_contract.py --all` con esito 100% PASS.
- Eseguire lo script di verifica live `scratch/check_alignment_live.py` validando la piena parità testuale, visiva e di esclusioni su tutti gli 8 personaggi.

## Acceptance Criteria

### Criteri Oggettivi
- [ ] 8/8 Character Card hanno `description` 1:1 byte-for-byte identica a `content` delle entry nel Lorebook.
- [ ] 8/8 voci NPC nei Lorebook hanno `ignored_characters` popolato con l'ID della rispettiva card.
- [ ] 8/8 Character Card presentano l'avatar sincronizzato 1:1 con l'asset della Gallery del Lorebook.
- [ ] Wyvern Web API restituisce HTTP 200 su tutti gli aggiornamenti delle card.
- [ ] `python scripts/verify_npc_schema_contract.py --all` supera il 100% dei contratti.
</original_task>
