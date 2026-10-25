with open('.agents/rules/05_precedenza_lore_e_discrepanze.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = """## 4. Canone Ufficiale SUCC (`io-succ.uwu.ai`) e Divieto Assoluto di "Solarton University"

Per l'ateneo principale dell'ambientazione universitaria in Solarton, California:
1. **Nome Istituzionale Corretto:** **Supernatural University of Central California (SUCC)**.
2. **Divieto Assoluto:** Il termine "Solarton University" (o "Southern Union Monster College") è errato ed apocrifo. È tassativamente vietato impiegarlo in descrizioni, lorebook, scenari, schede o dialoghi.
3. **Fondazione e Rettorato:** Fondata nel **2002** dal **Dean Archer Wolfwood**, che per la prima volta aprì l'istituto agli studenti umani creando il modello di educazione mista umano-soprannaturale.
4. **Istituzione Rivale:** **CUMS** (*California University of Magical Sciences*), situata a Hex Valley, strettamente segregata e riservata ai soli esseri soprannaturali.
5. **Facoltà Canoniche:** Alchemy, Necromancy, Applied Divination, Paranormal Psychology, Astral Studies, Potions, Cryptozoology, Supernatural/Human Relations, Environmental Magic, Vampiric Studies, Lycanthropy Studies."""

replacement = """## 4. Canone Ufficiale SUCC (`io-succ.uwu.ai`) e Divieto Assoluto di Varianti Apocrife

1. **Denominazione Istituzionale Unica ed Ufficiale:**
   - **Nome Completo:** **Supernatural University of Central California**
   - **Acronimo Ufficiale:** **SUCC**
   - **Sede:** Solarton, California (Central California / Hex Valley).
   - **Mascotte & Squadra Atletica:** **Bulls** (SUCC Bulls).
2. **Divieto Tassativo di Nomi Inventati o Apocrifi:**
   È rigorosamente vietato utilizzare qualsiasi nome alternativo o surrogato, tra cui:
   - ❌ *"Solarton University"*
   - ❌ *"Solarton University of the Occult"*
   - ❌ *"Solarton Collegiate University"*
   - ❌ *"Southern Union Monster College"*
3. **Gestione Prompt Grafici per Argon / Imagen 3:**
   Poiché l'acronimo isolato `"SUCC"` può attivare falsi positivi nei filtri di moderazione semantica in lingua inglese (in quanto scambiato per slang fonetico lewd), nei prompt di generazione immagine è obbligatorio usare per esteso la dicitura ufficiale:
   - ✅ `"Supernatural University of Central California"`
   È fatto esplicito divieto di alterare il nome dell'ateneo per aggirare i filtri: la dicitura per esteso è neutrale, istituzionale e priva di trigger di policy.
4. **Fondazione e Rettorato:** Fondata nel **2002** dal **Dean Archer Wolfwood**, che per la prima volta aprì l'istituto agli studenti umani creando il modello di educazione mista umano-soprannaturale.
5. **Istituzione Rivale:** **CUMS** (*California University of Magical Sciences*), situata a Hex Valley, strettamente segregata e riservata ai soli esseri soprannaturali.
6. **Facoltà Canoniche:** Alchemy, Necromancy, Applied Divination, Paranormal Psychology, Astral Studies, Potions, Cryptozoology, Supernatural/Human Relations, Environmental Magic, Vampiric Studies, Lycanthropy Studies."""

assert target in text, "target not found in rule 05"
text = text.replace(target, replacement)
with open('.agents/rules/05_precedenza_lore_e_discrepanze.md', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated .agents/rules/05_precedenza_lore_e_discrepanze.md")

# Now update GEMINI.md
with open('GEMINI.md', 'r', encoding='utf-8') as f:
    g_text = f.read()

g_target = """- **Canone Ufficiale SUCC (`io-succ.uwu.ai`):**
  - **Nome Ufficiale:** **Supernatural University of Central California (SUCC)** a Solarton, CA.
  - **Divieto del termine "Solarton University":** Il nome "Solarton University" è apocrifo e bandito da ogni testo o scheda.
  - **Fondazione (2002):** Fondata dal **Dean Archer Wolfwood**, pioniere dell'integrazione accademica umano-soprannaturale.
  - **Istituzione Rivale:** **CUMS** (*California University of Magical Sciences*), situata a Hex Valley."""

g_replacement = """- **Canone Ufficiale SUCC (`io-succ.uwu.ai`) & Divieto Varianti Apocrife:**
  - **Nome Istituzionale Unico ed Ufficiale:** **Supernatural University of Central California** (acronimo: **SUCC**), situata a Solarton, California. Mascotte e squadra: **Bulls** (SUCC Bulls).
  - **Divieto Assoluto di Termini Apocrifi:** È bandito qualsiasi nome alternativo ("Solarton University", "Solarton University of the Occult", "Solarton Collegiate University", "Southern Union Monster College").
  - **Regola Prompt Grafici (Argon / Imagen 3):** Poiché l'acronimo "SUCC" attiva falsi positivi nei filtri semantici come slang lewd, nei prompt di generazione immagine è obbligatorio usare per esteso il nome canonico: `"Supernatural University of Central California"`. Vietato inventare nomi surrogati.
  - **Fondazione (2002):** Fondata dal **Dean Archer Wolfwood**, pioniere dell'integrazione accademica umano-soprannaturale.
  - **Istituzione Rivale:** **CUMS** (*California University of Magical Sciences*), situata a Hex Valley."""

assert g_target in g_text, "g_target not found in GEMINI.md"
g_text = g_text.replace(g_target, g_replacement)
with open('GEMINI.md', 'w', encoding='utf-8') as f:
    f.write(g_text)
print("Updated GEMINI.md")
