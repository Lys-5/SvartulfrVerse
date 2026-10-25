p = r'e:\repository\SvartulfrVerse\GEMINI.md'
content = open(p, encoding='utf-8').read()

bullet = """  - **Soppressione Nativa Wyvern ("Don't Activate When Active"): `ignored_characters` & `ignored_personas`:**
    Per impedire duplicazioni, allucinazioni e collisioni bot-giocatore (es. quando l'utente gioca nei panni di una Persona corrispondente a un NPC del Lorebook, come Alyssa o Jasper, o quando una Character Card esterna e gia presente nel party o nella chat), Wyvern gestisce a livello di schema due array dedicati:
    - `ignored_characters: string[]`: Elenco di ID di Character Card. Se una delle card specificate e presente nella sessione attiva, Wyvern ignora e salta integralmente l'entry del Lorebook.
    - `ignored_personas: string[]`: Elenco di ID di Persona (`{{user}}`). Se il giocatore seleziona una delle Persona specificate, Wyvern ignora e salta integralmente l'entry del Lorebook.
    - Questo meccanismo nativo elimina la necessita di ricorrere a workaround artificiali (come `selective: true` con keyword fittizie 'Dossier'/'Scheda'), consentendo a ogni entry NPC nei Lorebook di conservare `selective: false`, chiavi di attivazione naturali (nome, cognome, alias) e descrizioni JED+ narrative integrali (>2.000 fino a >16.000 caratteri) in totale sicurezza.
"""

target = "- **Personaggi Stand-Alone (`/mine`):**"
if target in content and 'ignored_characters' not in content:
    idx = content.find(target)
    content = content[:idx] + bullet + content[idx:]
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("GEMINI.md updated successfully with native suppression bullet!")
else:
    print("Target not found or already updated.")
