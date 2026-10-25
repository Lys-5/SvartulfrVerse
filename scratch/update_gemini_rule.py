p = r'e:\repository\SvartulfrVerse\GEMINI.md'
content = open(p, encoding='utf-8').read()

section_snippet = """
### Soppressione Nativa Wyvern ("Don't Activate When Active"): `ignored_characters` & `ignored_personas`
Per impedire duplicazioni, allucinazioni e collisioni bot-giocatore (es. quando l'utente gioca nei panni di una Persona corrispondente a un NPC del Lorebook, come Alyssa o Jasper, o quando una Character Card esterna e gia presente nel party o nella chat), Wyvern gestisce a livello di schema due array dedicati:
- **`ignored_characters`: `string[]`**: Elenco di ID di Character Card. Se una delle card specificate e presente nella sessione attiva, Wyvern ignora e salta integralmente l'entry del Lorebook.
- **`ignored_personas`: `string[]`**: Elenco di ID di Persona (`{{user}}`). Se il giocatore seleziona una delle Persona specificate, Wyvern ignora e salta integralmente l'entry del Lorebook.
- **Superamento dei Workaround Artificiali**: Questo meccanismo nativo elimina qualsiasi necessita di limitare le schede con filtri restrittivi o keyword artificiali (`selective: true` con keyword 'Dossier'/'Scheda'). Consente a ogni entry NPC nei Lorebook di conservare `selective: false`, chiavi di attivazione naturali (nome, cognome, alias) e descrizioni JED+ narrative integrali (>2.000 fino a >16.000 caratteri) in totale sicurezza.
"""

target = "### Regole di Igiene Lorebook Obbligatorie:"
if target in content and 'ignored_characters' not in content:
    idx = content.find(target)
    # insert before target or inside Section 7
    content = content[:idx] + section_snippet + "\n" + content[idx:]
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("GEMINI.md updated successfully with native suppression documentation!")
else:
    print("GEMINI.md already contains ignored_characters or target not found.")
