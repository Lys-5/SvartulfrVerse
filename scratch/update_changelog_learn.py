import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
cl_path = ROOT / 'CHANGELOG.md'
lines = cl_path.read_text(encoding='utf-8').splitlines(keepends=True)

new_entry = """## [20-21 Ottobre 2026] - Deploy Wyvern Game Master & Prompt Assembly, Chat Overrides & Validazione CDP (/learn)

- **Verifica e Collegamento Game Master & Custom Prompt Assembly**:
  - Assistant `simple_assistant_xRfBnV7wq48QppqbPPpTM` (*"Svartúlfr — Game Master & World Engine"*) verificato attivo su cloud Wyvern (`kind: "narrator"`, `visibility: "private"`).
  - Prompt Assembly `pha_kWkWUAfTJTF9q72c2bC98` (*"Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)"*) verificato con architettura a 4 livelli, XML polimorfico, floating prompt a profondità 4% (ruolo `user`), e 5 blocchi post-history (ruolo `user`).

- **Configurazione e Persistenza Chat Overrides su `chat_log_qUdWrgx232YGtwDE2318a`**:
  - *Narrator Turn*: Selezionato come narratore predefinito `simple_assistant_xRfBnV7wq48QppqbPPpTM` con prospettiva *Third person* e switch `#narratorShowNpcThoughtsToggle` attivo (`data-state="checked"`).
  - *Prompt Assembly*: Collegato al preset `pha_kWkWUAfTJTF9q72c2bC98` con switch `#advancedPostHistoryToggle` attivo (`data-state="checked"`).
  - *Easy Parameters*: Attivato con profilo *Storyteller / Balanced Roleplay* (Temperature: 0.95, Min-P: 0.08, Repetition Penalty: 1.05, Presence Penalty: 0.05, Min Tokens: 100).

- **Validazione Live Chrome DevTools Protocol (CDP)**:
  - Ispezionato il DOM e verificata la conformità degli stati attivi dei controlli (badges "On", toggles `data-state="checked"`, zero errori JavaScript runtime).
  - Identificata e formalizzata la **Regola del Single-Client CDP**: l'istanza Chrome con remote debugging ammette un solo client debugger WebSocket per sessione; scoperto che il processo host Antigravity mantiene una connessione attiva, richiedendo disconnessioni esplicite (`ws.close()`) per evitare accodamenti di processo.

- **Aggiornamento Regole e Nuova Skill di Dominio (`/learn` + `/workflow-skill-creator`)**:
  - Aggiornata la Regola 11 (`.agents/rules/11_wyvern_api_sicurezza_e_bug.md`) con la Sezione 10 su Chat Overrides e protocollo CDP.
  - Aggiornata la Regola 13 (`.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md`) con la Sezione 3 sull'integrazione degli overrides con gli scenari.
  - Sincronizzato `GEMINI.md` con i nuovi standard operativi.
  - Consolidata la skill `.agents/skills/wyvern-ttrpg-master-deployer/` con utility script `scripts/verify_chat_overrides.py` (CLI multi-comando per token refresh, verifica assistant, assembly e chat) e `scripts/inspect_chrome_cdp.js`.

---

"""

# Insert right before the first '## ['
first_h2 = -1
for i, line in enumerate(lines):
    if line.startswith('## ['):
        first_h2 = i
        break

if first_h2 != -1:
    lines.insert(first_h2, new_entry)
    cl_path.write_text(''.join(lines), encoding='utf-8')
    print("CHANGELOG.md updated successfully at line", first_h2)
else:
    print("Could not find first H2 section")
