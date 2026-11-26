# Pipeline Asset & Allineamento Canone Visivo — Log Sessione (26/11/2026)

**Data:** 2026-11-26  
**Workspace:** `E:\repository\SvartulfrVerse`  
**Obiettivo:** Ripresa della pipeline asset Gemini dopo dismissione ComfyUI, normalizzazione su griglia reale delle altezze (`1696x2528` RGBA, `FLOOR_Y=2500`, `PX_PER_CM=9.75`), aggiornamento canone visivo e anagrafico (`Edric`, `Kaladin`, `Ut`, `Wulfnic`, `Malachia`, `E.C.H.O.`), sincronizzazione Vault + Wyvern live, ed espansione del manifest a **85 item su 6 Wave**.

---

## 1. Allineamenti di Lore, Regole & Live Wyvern (`HTTP 200` + Read-Back)

Tutte le modifiche narrative/schede sono state applicate con **Pure Positive Framing** (zero `"no human ears"`/`"zero orecchie umane"` nelle schede), zero em-dash (`—`), zero markdown `**`, parità byte-for-byte `entries == lexicon` e backup in `scratch/backups_visual_lore_20261126/`:

- **Edric Douglas (`165 cm / 5'5"`):** aggiornata l'altezza canonica in [.agents/rules/05_precedenza_lore_e_discrepanze.md](../.agents/rules/05_precedenza_lore_e_discrepanze.md), [.agents/rules/03_outfits_e_coerenza_visiva.md](../.agents/rules/03_outfits_e_coerenza_visiva.md) e [scripts/vault_health_check.py](../scripts/vault_health_check.py).
- **Kaladin Blackwolf Nargathon (`_9YcrRj1BTHCL2e1Up3exz`):** aggiornato in [FINAL/Svartulfr_Characters.json](../FINAL/Svartulfr_Characters.json), [FINAL/Svartulfr_NPC_Primary.json](../FINAL/Svartulfr_NPC_Primary.json), [lorebooks/optimized/Svartulfr_NPC_Primary.json](../lorebooks/optimized/Svartulfr_NPC_Primary.json) e live su Wyvern (`PUT` + `GET` HTTP 200) per aderire al ritratto canonico: lunghi capelli neri in coda bassa con due ciocche frontali su fronte e tempie, occhi verde smeraldo-ottanio (rosso cremisi in ira/mutazione), pizzetto e baffi neri scolpiti lungo la mascella, cicatrici su fronte/sopracciglia/zigomi e 9 outfit ripuliti (`191 cm`).
- **Ut Berg (`_wMcYm8hBYH97fVVWG86nN`):** capelli e barba omogeneizzati in **rossiccio striato di grigio** (`reddish-auburn streaked with iron-grey`) e età apparente aggiornata a **quarantenne/45enne usurato dalle battaglie** (`battle-worn mid-40s`, arresto biologico a 45 anni nell'864 d.C.).
- **Wulfnic Báleygr Bloodmoon (`_P1HrVjkY9TGnymNaAWX1j` & `/mine` `_HEQQbbRFwKdG8QE2Fh1z1`):** capelli, treccia vichinga, barba, orecchie e coda aggiornati a **biondo dorato striato di bianco** (`golden-blonde streaked with snow-white`) ed età apparente **quarantenne usurato dalle battaglie** (`battle-worn 40s`, arresto biologico a 40 anni nell'864 d.C.) in [FINAL/Wulfnic_Bloodmoon_card.json](../FINAL/Wulfnic_Bloodmoon_card.json), `Svartulfr_Characters.json`, `Svartulfr_NPC_Primary.json`, [.agents/rules/06_invecchiamento_e_longevita.md](../.agents/rules/06_invecchiamento_e_longevita.md) e [GEMINI.md](../GEMINI.md).
- **Separazione Ruoli Asset (`03_outfits_e_coerenza_visiva.md` & `GEMINI.md`):**
  - **Default Avatar (`<name>_avatar.png`):** ritratto **a mezzo busto** con **outfit di default** su **sfondo urbano coerente** (campo `avatar` su Wyvern `/mine` e World Characters).
  - **Visual Novel Sprites (`<name>_neutral.png`, `1696x2528` RGBA su `FLOOR_Y=2500`):** **figure intere** destinate esclusivamente alla sezione **Sprites** della chat interface di Wyvern per le emozioni.
  - **Turnaround Reference (`<name>_reference.png` & `<name>_hybrid_reference.png`, `2730x1536` RGB `#C8C8C8`):** tavole tecniche 4-colonne base e forma ibrida.
- **Integrità Vault:** `scripts/vault_health_check.py` superato con **158/158 check** e **0 errori critici**.

---

## 2. Avanzamento Pipeline Asset (`scripts/asset_reference_pipeline.py`)

Copie di sicurezza di tutte le bozze e versioni sostituite archiviate in `scratch/backups_assets_20261126/`.

### Stato Manifest (`85` item totali su `6` Wave)
- **Wave 1A (8 Membri del Branco — base):**
  - **Reference Sheets (`8/8 DONE`):** `Jasper`, `Alyssa`, `Malachia` *(rigenerata 1:1 su ritratto canonico abbronzato con capelli spiky corti, pizzetto, cicatrice a X guancia/sopracciglio e lupo su avambraccio)*, `Noah`, `Erik`, `Logan`, `Edric`, `Wulfnic` *(rigenerata biondo striato bianco, 40s battle-worn)*.
  - **Visual Novel Sprites (`6/8 DONE`, `2 REGEN_QUEUED`):** `Jasper` (`192.7 cm`), `Alyssa` (`155.1 cm`), `Noah` (`197.1 cm`), `Erik` (`213.0 cm`), `Logan` (`198.1 cm`), `Edric` (`165.0 cm`). Restano da rigenerare: `Malachia` *(nuova ancora `malachia_body_2x3.png` già estratta a `207.0 cm`)* e `Wulfnic` *(nuova ancora `wulfnic_body_2x3.png` già estratta a `220.1 cm`)*.
- **Wave 1B (7 Membri del Branco / Cast Principale):**
  - **Reference Sheets (`7/7 DONE`):** `Magnus`, `Elizabeth`, `Ut` *(rigenerata rossiccio striato grigio, 45s battle-worn)*, `Zefir`, `Kaladin` *(rigenerata 1:1 da ritratto con coda bassa, 2 ciocche, occhi verde smeraldo-ottanio, pizzetto, dog tags e ZERO corna)*, `Nixara`, `Echo` *(rigenerata **100% NON-UMANO**: solo drone esagonale magitech 30 cm + ologramma onda audio smeraldo-ciano)*.
  - **Visual Novel Sprites (`3/7 DONE`, `4 PENDING/REGEN`):** `Magnus` (`205.0 cm`), `Elizabeth` (`165.0 cm`), `Nixara` (`165.0 cm`). Restano da generare: `Ut`, `Kaladin`, `Zefir` *(ancore `*_body_2x3.png` già pronte)* + `Echo` *(sprite drone+ologramma non-umano flottante, rimossa vecchia bozza umanoide)*.
- **Wave 2 (10 NPC Stand-Alone in `assets/NPC/<Name>/`):** `0/20` (`Mac`, `Larek`, `Zeera`, `Richard`, `Adam`, `Hana`, `Luka`, `Dullahan`, `Johan`, `Fenrir`).
- **Wave 3 (12 Varianti Alternate Timeline):** `0/24` (`Jasper` 4, `Alyssa` 5, `Malachia`, `Mac`, `Zeera`).
- **Wave `4_HYBRID` (23 Shifter Hybrid Form `16:9` Reference Cards):** `0/23` (`<name>_hybrid_reference.png` nella cartella di ciascuno dei 23 shifter canonici; esclusi `Echo` e `Zeera`).
- **Wave `5_AVATAR` (25 Default Half-Body Urban Avatars):** `0/25` (`<name>_avatar.png` `2:3` / `3:4` a mezzo busto con outfit di default su sfondo urbano, finalizzati con `finalize-avatar`).

---

## 3. Automazione Notturna & Ripartenza Domattina
- **Timer Notturno `image-generator` (`task-478`, ~`00:25 CET` 27/11/2026):** parte automaticamente al reset della finestra da 5 ore con priorità sui 6 neutral mancanti di Wave 1A/1B (`Malachia`, `Wulfnic`, `Ut`, `Kaladin`, `Zefir`, `Echo`), proseguendo poi con finestre `+5h02m` su Wave 2, Wave 3, Wave `4_HYBRID` e Wave `5_AVATAR`.
- **Timer API Key Probe (`task-215`, ~`09:03 CET` 27/11/2026):** verifica automatica crediti giornalieri Google AI Studio (`probe-keys`).
- **Lavoro manuale con Gemini Pro domattina:** usare rapporto **`3:4`** per tutti gli sprite VN (`neutral`) e per gli Avatar a mezzo busto, e **`16:9`** per le Reference Sheet (Wave 2/3/4). I prompt pronti per i 6 neutral rimanenti del Branco sono già allineati con le ancore `*_body_2x3.png` (e `echo_reference.png` per `Echo`).
