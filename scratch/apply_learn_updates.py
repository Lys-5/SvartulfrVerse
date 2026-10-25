import re

# 1. Update .agents/rules/05_precedenza_lore_e_discrepanze.md
path_rule05 = '.agents/rules/05_precedenza_lore_e_discrepanze.md'
with open(path_rule05, 'r', encoding='utf-8') as f:
    r05 = f.read()

# Add to table
old_table = """| **Blackwood / Douglas** | Lys | Blackwood City, famiglia e branco Douglas |
| **DDM Inc.** | Autore esterno (*io wuvs soap*) | Voidspace (universo separato) |"""

new_table = """| **Blackwood / Douglas** | Lys | Blackwood City, famiglia e branco Douglas |
| **DDM Inc.** | Autore esterno (*io wuvs soap*) | Voidspace (universo separato) |
| **Fabule Urbane / La Frattura** | Groviglio Prinz | Europa continentale, bacino del Mediterraneo, Dungeon europei, agenzia EXO, Le Furie (Teatro europeo dello Squarcio del Velo / Voidspace) |"""

if old_table in r05 and new_table not in r05:
    r05 = r05.replace(old_table, new_table)

# Add Section 7 and 8 to rule 05
new_sections_r05 = """
---

## 7. Ponte Canonico: La Frattura, lo Squarcio del Velo e i Dungeon Europei

1. **Identificazione Cosmologica:** Nel canone di Svartúlfr Verse, "La Frattura" (ambientazione *Fabule Urbane* di Groviglio Prinz) corrisponde storicamente all'evento dello **Squarcio del Velo** (classificato dai terminali DDM come *Reality Tear Primaria*) nel teatro continentale europeo e mediterraneo.
2. **Fenomenologia dei Dungeon Europei:** Il collasso dimensionale del Velo ha inondato catacombe, cripte e reti ipogee di miasma arcanico grezzo, convertendole in Dungeon labirintici governati da distorsioni gravitazionali, nuclei di mana (*Dungeon Cores*) e dando origine alla *Fascia Desolata*. L'evento ha risvegliato il bestiario folkloristico mediterraneo e dantesco (*Alichini, Coblynau, Drakaina, Alseidi Corrotte, Variaghi*).
3. **Agenzie di Contenimento Continentali:** La *European Xenological Operations (EXO)* e la squadra speciale d'assalto rapido *Le Furie* operano come controparti/partner europee di DDM Inc. e PERSEUS nella bonifica dei Dungeon urbani, nel contenimento di brecce critiche e nella gestione dei civili *Cambiati*.

---

## 8. Quadro Giuridico e Tecnologico Vincolante Modern Fantasy

In tutti gli scenari e testi relativi a Solarton, SUCC e al Modern Fantasy in generale vigono le seguenti invarianti legali e di setting:
- **Divieto di Matrimonio Misto:** Il matrimonio tra esseri umani e creature soprannaturali è formalmente illegale e privo di validità civile nella quasi totalità dei paesi e delle giurisdizioni.
- **Registro Obbligatorio dei Demoni:** Le entità infernali, succubi, incubi e specie ematofaghe o a nutrizione energetica umana sono sottoposte a schedatura e monitoraggio periodico obbligatorio federale.
- **Supernatural Harm Act (2001):** Tutele legali, pensioni compensative e status di non-morto riconosciuto per le vittime di necromanzia, resurrezione forzata o mutazione occulta non consensuale (es. Roland Vickers).
- **Livello Tecnologico e Divieto Assoluto di Androidi:** Tecnologia ancorata al 2023-2024 con integrazioni magiche; divieto assoluto di robotica avanzata, androidi senzienti o cyborg.
"""

if "## 7. Ponte Canonico: La Frattura" not in r05:
    r05 = r05.strip() + "\n" + new_sections_r05

with open(path_rule05, 'w', encoding='utf-8') as f:
    f.write(r05)

print("Updated .agents/rules/05_precedenza_lore_e_discrepanze.md")

# 2. Update .agents/rules/11_wyvern_api_sicurezza_e_bug.md
path_rule11 = '.agents/rules/11_wyvern_api_sicurezza_e_bug.md'
with open(path_rule11, 'r', encoding='utf-8') as f:
    r11 = f.read()

# Add row to bug table
old_table_end = """| **Attivazione Involontaria Dossier Lorebook** | Un World Dossier enciclopedico si attiva in chat parlando del personaggio già presente come card/slot | Impostare tassativamente `selective: true` sui World Dossier del cast principale con `secondary_keys` dedicate archivistiche (`['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`), e bonificare le chiavi trigger isolate mono-parola (es. `'Alyssa'` -> `'Alyssa Telegram'`). |"""

new_table_row = """| **Attivazione Involontaria Dossier Lorebook** | Un World Dossier enciclopedico si attiva in chat parlando del personaggio già presente come card/slot | Impostare tassativamente `selective: true` sui World Dossier del cast principale con `secondary_keys` dedicate archivistiche (`['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`), e bonificare le chiavi trigger isolate mono-parola (es. `'Alyssa'` -> `'Alyssa Telegram'`). |
| **HTTP 500 Unauthorized (Token Scaduto)** | Wyvern risponde con HTTP 500 e body `{"message": "Unauthorized", "code": "INTERNAL_ERROR"}` | Il Bearer token in `scratch/wyvern_token.txt` è scaduto. Eseguire automaticamente `python scratch/refresh_token.py` (scambio con Google Firebase Secure Token API) per rigenerare il token e ripetere la chiamata. Non interrompere il flusso né chiedere token all'utente. |"""

if old_table_end in r11 and new_table_row not in r11:
    r11 = r11.replace(old_table_end, new_table_row)

new_section_r11 = """
---

## 8. Protocollo Obbligatorio di Auto-Refresh Token Firebase (HTTP 500 Unauthorized)

- **Sintomo del Bug:** Quando il Bearer token di autenticazione scade, la Web API di Wyvern non risponde con HTTP 401, ma genera un ingannevole `HTTP 500 Internal Server Error` con payload:
  `{"error":"Internal Server Error","message":"Unauthorized","details":{"message":"Unauthorized","code":"INTERNAL_ERROR"}}`
- **Protocollo Automatico di Ripristino:**
  1. È tassativamente vietato interrompere l'operazione o chiedere all'utente un nuovo token manuale.
  2. L'assistente deve eseguire tempestivamente lo script `python scratch/refresh_token.py`.
  3. Lo script contatta la Google Firebase Secure Token API (`https://securetoken.googleapis.com/v1/token`) utilizzando il `refresh_token` permanente in `scratch/refresh_token.txt` e aggiorna silenziosamente `scratch/wyvern_token.txt` con un id_token fresco valido per un'altra ora.
  4. L'assistente ripete immediatamente la chiamata API interrotta.
- **Host Ufficiale Endpoints:** Utilizzare sempre `https://app.wyvern.chat/api/` (es. `/lorebooks/{id}`, `/character-scenarios/{id}`) e non `api.wyvern.chat`.
"""

if "## 8. Protocollo Obbligatorio di Auto-Refresh Token Firebase" not in r11:
    r11 = r11.strip() + "\n" + new_section_r11

with open(path_rule11, 'w', encoding='utf-8') as f:
    f.write(r11)

print("Updated .agents/rules/11_wyvern_api_sicurezza_e_bug.md")

# 3. Update GEMINI.md
path_gemini = 'GEMINI.md'
with open(path_gemini, 'r', encoding='utf-8') as f:
    gem = f.read()

# Update table in Section 10
if old_table in gem and new_table not in gem:
    gem = gem.replace(old_table, new_table)

# In GEMINI.md Section 10, add bridge and MF laws
marker_sec10 = "- **Canone Ufficiale SUCC (`io-succ.uwu.ai`) & Divieto Varianti Apocrife:**"
new_sec10_block = """- **Ponte Canonico "La Frattura" <-> "Squarcio del Velo / Voidspace / Dungeons":**
  - **Identificazione Cosmologica:** Nel canone di Svartúlfr Verse, "La Frattura" (ambientazione *Fabule Urbane* di Groviglio Prinz) corrisponde storicamente all'evento dello **Squarcio del Velo** (Reality Tear Primaria nei registri DDM) nel teatro continentale europeo e mediterraneo.
  - **Fenomenologia dei Dungeon Europei:** Il collasso del Velo ha inondato catacombe, cripte e reti ipogee di miasma arcanico grezzo, convertendole in Dungeon labirintici governati da distorsioni gravitazionali e nuclei di mana (*Dungeon Cores*), dando origine alla *Fascia Desolata* e risvegliando il bestiario folkloristico mediterraneo e dantesco (*Alichini, Coblynau, Drakaina, Alseidi Corrotte, Variaghi*).
  - **Agenzie di Contenimento Continentali:** La *European Xenological Operations (EXO)* e la squadra speciale d'assalto rapido *Le Furie* operano come controparti/partner europee di DDM Inc. e PERSEUS nella bonifica dei Dungeon urbani e nella gestione dei civili *Cambiati*.
- **Quadro Giuridico e Tecnologico Vincolante Modern Fantasy:**
  - **Divieto di Matrimonio Misto:** Il matrimonio tra umani e sovrannaturali è formalmente illegale e privo di validità civile nella quasi totalità dei paesi.
  - **Registro Obbligatorio dei Demoni:** Le specie infernali, succubi, incubi e specie ematofaghe o a nutrizione energetica umana sono sottoposte a schedatura obbligatoria federale.
  - **Supernatural Harm Act (2001):** Tutele legali, pensioni compensative e status di non-morto riconosciuto per le vittime di necromanzia o resurrezione forzata (es. Roland Vickers).
  - **Livello Tecnologico e Divieto Androidi:** Tecnologia ancorata al 2023-2024; totale assenza di robotica avanzata, androidi senzienti o cyborg.
- **Canone Ufficiale SUCC (`io-succ.uwu.ai`) & Divieto Varianti Apocrife:**"""

if marker_sec10 in gem and "Ponte Canonico \"La Frattura\"" not in gem:
    gem = gem.replace(marker_sec10, new_sec10_block)

# In GEMINI.md Section 15, update bug table and add auto-refresh protocol
if old_table_end in gem and new_table_row not in gem:
    gem = gem.replace(old_table_end, new_table_row)

marker_sec15_end = "### Standard Minimo 9 Outfits Obbligatori per Scheda"
# In Section 15, let's find the end of the bug section or table
sec15_sub = """- **Errore HTTP 500 "Unauthorized" & Protocollo di Auto-Refresh Token Firebase:**
  Quando il Bearer token di Wyvern scade, l'API restituisce un ingannevole `HTTP 500 Internal Server Error` con corpo `{"message": "Unauthorized", "code": "INTERNAL_ERROR"}`. È fatto divieto di interrompere il lavoro o chiedere un nuovo token all'utente: l'assistente deve eseguire automaticamente `python scratch/refresh_token.py` (che scambia il refresh token su Google Firebase Secure Token API `https://securetoken.googleapis.com/v1/token` aggiornando `scratch/wyvern_token.txt`) e ripetere immediatamente la richiesta sull'host `https://app.wyvern.chat/api/`.
"""

if "- **Errore HTTP 500 \"Unauthorized\"" not in gem:
    # Insert right before ## 16. Disciplina delle Attitudes
    gem = gem.replace("## 16. Disciplina delle Attitudes", sec15_sub + "\n---\n\n## 16. Disciplina delle Attitudes")

with open(path_gemini, 'w', encoding='utf-8') as f:
    f.write(gem)

print("Updated GEMINI.md")
