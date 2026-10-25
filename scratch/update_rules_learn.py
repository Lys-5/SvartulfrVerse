import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

rule13_path = ROOT / '.agents' / 'rules' / '13_workflow_chat_di_gruppo_stand_alone.md'
content = rule13_path.read_text(encoding='utf-8')

section3 = """

---

## 3. Integrazione dei Chat Overrides con Scenari Stand-Alone e Chat di Gruppo

Nelle chat create da Character Scenarios o da bot stand-alone, l'esperienza di roleplay TTRPG raggiunge la massima coerenza combinando lo scenario con i Chat Overrides:

1. **Narrator Turn Collegato:**
   Impostare il narratore predefinito su `simple_assistant_xRfBnV7wq48QppqbPPpTM` (*"Svartúlfr — Game Master & World Engine"*). Questo assicura che tra un turno del bot e l'altro, o quando intervengono PNG non assegnati a uno slot primario, il Game Master gestisca la prosa ambientale in terza persona, mantenendo l'anti-puppeting assoluto per `{{user}}` e la privacy dei pensieri racchiusi in `*...*`.

2. **Master Prompt Assembly Attivo:**
   Collegare `pha_kWkWUAfTJTF9q72c2bC98` (*"Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)"*). Il prompt assembly inietta a runtime:
   - I blocchi di attributi XML formattati con `<special_stats>{{rpg_stats}}</special_stats>`.
   - Il floating prompt di guardrail al 4% di profondità per prevenire drift linguistici in inglese.
   - I blocchi post-history con ruolo HTTP `user` che forzano la risoluzione diegetica D20 + S.P.E.C.I.A.L. e i feed digitali solo su interazione fisica con schermi.

3. **Parametri di Campionamento:**
   Attivare *Easy Parameters* col profilo Storyteller (Temperature 0.95, Min-P 0.08, Repetition Penalty 1.05, Presence Penalty 0.05, Min Tokens 100), che garantisce la migliore risposta creativa evitando allucinazioni e ripetizioni di frasi fatte.
"""

if 'Integrazione dei Chat Overrides con Scenari' not in content:
    rule13_path.write_text(content.strip() + section3 + '\n', encoding='utf-8')
    print("Rule 13 updated successfully.")
else:
    print("Rule 13 already contains Section 3.")
