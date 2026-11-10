# Directory Asset Multimediali — Svartúlfr Verse (`assets/`)

Questa directory raccoglie e indicizza tutti gli asset grafici, i riferimenti anatomici/visivi e i prompt master generativi ufficiali dell'ambientazione **Svartúlfr (Blackwood-Douglas / Modern Fantasy)**.

---

## 1. Struttura delle Cartelle

```text
assets/
├── characters/
│   ├── avatars_legacy/       # Avatar storici e icone a risoluzione compatta
│   ├── group_shots/          # Illustrazioni di gruppo e scene corali
│   ├── main_cast/            # Cartelle dedicate al cast principale (Alyssa, Jasper, Noah, Malachia, Erik, ecc.)
│   └── secondary_cast/       # NPC e figure ricorrenti della casata e del campus
├── environments/             # Visual di Solarton, Campus SUCC, The Verve Club, Docks e scorci urbani
├── lore_and_gods/            # Emblemi runici, araldica della Casata Douglas e divinità celesti (Máni, Sól, Fenris)
├── NEW_IMAGE/                # Render ad altissima risoluzione per banner di Scenari e ambientazioni chiave
└── references/               # Reference canoniche ufficiali per i Marchi Runici e le polarità gemellari
```

---

## 2. Documentazione e Prompt Master Integrati

- [divine_marks_and_heights.md](divine_marks_and_heights.md):
  - **Specifiche dei Marchi Divini:**
    - Marchio di Máni (mezzaluna argentata con glifi lunari sub-dermici esclusivamente su anca sinistra di Alyssa — *Mániúlfr*).
    - Marchio di Sól (sole nero radioso con glifi solari sub-dermici esclusivamente su anca destra di Jasper — *Sólúlfr*).
    - Marchio Gebo (runa $\mathcal{X}$ a inchiostro di ferro freddo su polso sinistro interno di entrambi i gemelli).
  - **Griglia Proporzioni e Altezze:** Alyssa (193 cm), Jasper (193 cm), Noah (197 cm), Malachia (208 cm), Erik (213 cm), Wulfnic (220 cm).
  - **Suite di Prompt:** Midjourney v6, SDXL / Pony XL (con sintassi `BREAK` e tag Danbooru), NovelAI V3 e vincoli rigorosi di locomozione lamia per Sierra Cruz (4 metri di coda iridescente, zero gambe).
- [PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md](PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md):
  - Suite di prompt master calibrati su **Argon** per il cast completo, strutturati secondo lo schema a 6 sezioni (Abbigliamento con apertura lombare per la coda, Accessori, Scarpe, Gioielli, Trucco, Acconciatura).
- [PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md](PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md):
  - Prompt master per la generazione dei banner panoramici e delle ambientazioni dei Character Scenarios.

---

## 3. Regole di Conformità Visiva

1. **Demi-Umani (Orecchie Singole):** I demi-umani possiedono unicamente il paio di orecchie animali sulla sommità del capo. È tassativamente vietato rappresentare orecchie umane laterali (zero 4 orecchie).
2. **Sierra Cruz (Lamia):** Coda da serpente lunga 4 metri con scaglie arcobaleno iridescenti. Nessun uso di termini riferiti a gambe, ginocchia, piedi o camminata.
3. **Coerenza Douglas:** Tratti somatici condivisi tra i maschi della famiglia (mascella decisa, capelli scuri arruffati, palette calda al tramonto) pur preservando l'individualità di cicatrici e corporature.
