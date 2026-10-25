import os

insert_text = """### Integrazione dei Chat Overrides di Sessione (`Overrides & Extras`)
Per unire Character Scenarios, Assistant e Prompt Assembly in un flusso di roleplay coeso:
- **Default Narrator**: configurato su `simple_assistant_xRfBnV7wq48QppqbPPpTM` (*"Svartúlfr — Game Master & World Engine"*), narrazione in terza persona, switch `narratorShowNpcThoughtsToggle` attivo.
- **Prompt Assembly**: collegato al preset `pha_kWkWUAfTJTF9q72c2bC98` (*"Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)"*) con `advancedPostHistoryToggle` attivo.
- **Easy Parameters**: abilitato con profilo Storyteller / Balanced Roleplay (Temp: 0.95, Min-P: 0.08, RepPen: 1.05, PresencePen: 0.05, Min Tokens: 100).
- **Protocollo CDP Single-Client**: Chrome ammette un unico client debugger attivo per sessione; tutti gli script di ispezione esterna devono chiudere esplicitamente la connessione WebSocket (`ws.close()`, `process.exit(0)`) per evitare blocchi del browser o dell'agente.

"""

with open('GEMINI.md', 'r', encoding='utf-8') as f:
    content = f.read()

target = '## 19. Standard Operativo di Sessione e Skill Integrate'
if target in content and 'Integrazione dei Chat Overrides di Sessione' not in content:
    idx = content.find(target)
    new_content = content[:idx] + insert_text + content[idx:]
    with open('GEMINI.md.tmp', 'w', encoding='utf-8', newline='\r\n') as f_out:
        f_out.write(new_content)
    os.replace('GEMINI.md.tmp', 'GEMINI.md')
    print('GEMINI.md updated successfully!')
else:
    print('Target not found or already updated!')
