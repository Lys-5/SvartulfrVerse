p = r'e:\repository\SvartulfrVerse\.agents\rules\08_triage_lorebook_e_lexicon.md'
content = open(p, encoding='utf-8').read()

rule_6 = """
6. **Soppressione Nativa Wyvern ("Don't Activate When Active"): `ignored_characters` & `ignored_personas`:**
   Per impedire duplicazioni, allucinazioni e collisioni bot-giocatore (es. quando l'utente gioca nei panni di una Persona corrispondente a un NPC del Lorebook, come Alyssa o Jasper, o quando una Character Card esterna e gia presente nel party o nella chat), Wyvern gestisce a livello di schema due array dedicati:
   - **`ignored_characters`: `string[]`**: Elenco di ID di Character Card. Se una delle card specificate e presente nella sessione attiva, Wyvern ignora e salta integralmente l'entry del Lorebook.
   - **`ignored_personas`: `string[]`**: Elenco di ID di Persona (`{{user}}`). Se il giocatore seleziona una delle Persona specificate, Wyvern ignora e salta integralmente l'entry del Lorebook.
   - **Superamento dei Workaround Artificiali**: Questo meccanismo nativo elimina qualsiasi necessita di limitare le schede con filtri restrittivi o keyword artificiali (`selective: true` con keyword 'Dossier'/'Scheda'). Consente a ogni entry NPC nei Lorebook di conservare `selective: false`, chiavi di attivazione naturali (nome, cognome, alias) e descrizioni JED+ narrative integrali (>2.000 fino a >16.000 caratteri) in totale sicurezza.
"""

if 'ignored_characters' not in content:
    with open(p, 'a', encoding='utf-8') as f:
        f.write(rule_6)
    print('Rule 08 updated successfully!')
else:
    print('Rule 08 already contains ignored_characters.')
