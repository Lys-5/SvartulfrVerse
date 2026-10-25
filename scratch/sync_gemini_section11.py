# -*- coding: utf-8 -*-
import sys

def main():
    with open('GEMINI.md', 'r', encoding='utf-8') as f:
        text = f.read()

    target = "- Campi annidati RPG: `species_id` e `occupation_id` risiedono dentro l'oggetto `rpg_stats`."
    if target not in text:
        print("Error: Target not found in GEMINI.md")
        sys.exit(1)

    new_section = """- Campi annidati RPG: `species_id` e `occupation_id` risiedono dentro l'oggetto `rpg_stats`.



### Estrazione Non-Invasiva Risorse Web da Chrome Sync LevelDB (Offline Tab Groups)

Quando Chrome è avviato con debugging remoto o in sessione attiva con l'IDE, l'accesso CDP/WebSocket diretto è frequentemente inibito dalla Single-Client Lock di Chrome o dalle restrizioni di sicurezza (`404/403` su `/json`). È fatto divieto assoluto di riavviare o terminare Chrome per forzare flag CLI, per prevenire la perdita dello stato di sessione dell'utente.

**Procedura di Estrazione Offline:**
1. **Database Locale Sync:** Chrome persiste schede e Saved Tab Groups nel database LevelDB di sincronizzazione locale in `%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default\\Sync Data\\LevelDB\\*.ldb`.
2. **Accesso Non-Invasivo:** Scansione in sola lettura (binaria `rb`) dei file `.ldb` e `.log` senza interagire con i processi attivi di Chrome.
3. **Correlazione GUID:** Ricerca del nome del gruppo (es. `"RPG Source"`), estrazione del GUID del gruppo tab e risoluzione delle entità tab sincronizzate contenenti URL e titoli.
4. **Tool Standardizzato:** Utilizzare la skill standard di repository `.agents/skills/chrome-tabgroup-source-extractor/` (`scripts/extract_tabgroup.py`).
5. **Integrazione Knowledge:** Censire le nuove risorse in `knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md` (aggiornando i conteggi in Sezione 2 e popolando la sottosezione in Sezione 3) e tracciare la voce in `CHANGELOG.md`."""

    if "### Estrazione Non-Invasiva Risorse Web da Chrome Sync LevelDB" in text:
        print("Section already present in GEMINI.md")
        return

    updated = text.replace(target, new_section, 1)

    with open('GEMINI.md', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(updated)
    print("Successfully updated GEMINI.md with Section 11 LevelDB subsection.")

if __name__ == '__main__':
    main()
