p = r'e:\repository\SvartulfrVerse\GEMINI.md'
content = open(p, encoding='utf-8').read()

inventory = """
### Inventario Ufficiale delle Skill di Progetto (`.agents/skills/`)
1. **`auto-loop`**: Pipeline evolutiva completa a 4 stadi (Allineamento, Web Research, Plan/Boost, Esecuzione, Debug e Self-Learning).
2. **`chrome-tabgroup-source-extractor`**: Estrazione diretta e non invasiva di sessioni, tab group e URL da LevelDB Sync di Chrome senza riavvio del browser.
3. **`wyvern-ttrpg-master-deployer`**: Progettazione, compilazione Handlebars/XML e deploy via Wyvern Web API di AI Game Master, Custom Prompt Assembly e Scenari con motore D20 + S.P.E.C.I.A.L.
4. **`wyvern-card-lorebook-sync`**: Sincronizzazione Card/Lorebook, conversione di card in NPC con descrizioni JED+ piene, adozione della soppressione nativa anti-collisione (`ignored_characters` & `ignored_personas`), bonifica slot inaccessibili degli Scenari (`unavailable_count: 0`) e deployment via Wyvern Web API.
"""

target = "5. **Audit Post-Esecuzione (`/boost`):** ogni scrittura va verificata con GET fresche e controlli di integrit indipendenti."
# find in content
if 'wyvern-card-lorebook-sync' not in content:
    # find where Section 19 ends or append at end of Section 19
    idx = content.find('## 19. Standard Operativo')
    if idx != -1:
        content = content + "\n" + inventory
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print("GEMINI.md updated with skill inventory!")
else:
    print("Already updated.")
