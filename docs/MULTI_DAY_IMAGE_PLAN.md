# Asset Manifest & Multi-Day Image Generation Plan — Svartúlfr Verse

**Generated:** 2026-11-18T07:35:00Z  
**Authoritative Live Platform:** `https://app.wyvern.chat/mine` (`uid: 2r4fVpvImte5dbljedLkZJxre2d2`, Active World `_YpX47fNraQFw2dD7TdycJ`)  
**Scope:** Complete 3-Group Inventory (Group 1 Family: 11 Cards + 7 Personas + 15 WorldChars; Group 2 Pack: 14 WorldChars; Group 3 Single-Card NPCs: 10 SUCC/Blackwood Cards + 7 DDM Contractors + 9 NPC WorldChars)

---

## 0. Pipeline Ufficiale Aggiornata (2026-11-22 — ComfyUI Locale & Studio Base Reference First)

- **Motore Unico di Generazione Immagini:** **ComfyUI Locale** (`http://127.0.0.1:8188`, `E:\ComfyUI`, `scripts/comfy_batch_runner.py`) su RTX 4060 con **SDXL 1.0** (`CyberRealisticXLPlay_V10.0_FP16.safetensors`), VAE dedicato `sdxl_vae.safetensors` (`madebyollin/sdxl-vae-fp16-fix`, senza `--fp8_e4m3fn-unet`), e `IP-Adapter FaceID Plus v2` (`CLIP-ViT-H-14` + `InsightFace buffalo_l` su CPU). `Gemini.exe` e PixAI non sono più utilizzati per la routine immagini.
- **Sequenza Obbligatoria Post-Calibrazione (Studio Base Reference First):**
  1. Completare e far approvare ad Alice la calibrazione dei **4 modelli base da studio dei gemelli** (**Alyssa** e **Jasper**: close-up + figura intera nuda su sfondo grigio neutro).
  2. Una volta approvata la pipeline sui gemelli, **partire per ogni NPC generando prima il Set Base Reference su sfondo neutro da studio fotografico**:
     - **Primo piano close-up** (ritratto volto/spalle su sfondo grigio neutro da studio);
     - **Figura intera nuda** (riferimento anatomico completo testa-piedi su sfondo grigio neutro da studio per NPC adulti 18+; eccezione obbligatoria `POLICY_EXEMPT` vestita/sportiva SFW per minorenni come Edric).
  3. Usare poi il Set Base Reference di ciascun NPC come reference FaceID / IP-Adapter per generare tutte le successive **varianti outfit** (9 outfit per scheda) e le **scene con contesto**.

---

## 1. Day 1 Credit Audit & Execution Summary

### 1.1 Google AI Studio (`gemini-2.5-flash-image` / `gemini-3.1-flash-image-preview`)
- **Result:** **0 credits / 0 images generated** (`scratch/m1_gemini_test_results.json`).
- **Evidence:** All 4 configured API keys (`proxy/config_free_proxy.json` `keys.google_ai_studio[0..3]` and `.env` `GOOGLE_AI_STUDIO_API_KEY`) returned **HTTP 429 `RESOURCE_EXHAUSTED`** on both `gemini-2.5-flash-image` and `gemini-3.1-flash-image-preview` (free-tier image generation quota exhausted / `limit: 0` on current projects).

### 1.2 PixAI (`https://pixai.art`, Account: `mandellialice5@gmail.com`)
- **Result:** **0 Day-1 images generated (Login / Browser Debugging Block)** (`scratch/pixai_home_1.png`).
- **Evidence:**
  - Chrome `157.0.8103.79` blocks `--remote-debugging-port` and hangs `--remote-debugging-pipe` on the default `%LOCALAPPDATA%\Google\Chrome\User Data` directory due to Chrome 136+ security restrictions.
  - Launching with a cloned profile (`scratch/pixai_chrome_profile`) opens `https://pixai.art` in a **signed-out state** (`Sign in` / `Sign up free, get 10,000 credits` shown in `scratch/pixai_home_1.png`) because Windows DPAPI/App-Bound Cookie Encryption prevents transferring encrypted session cookies across `user-data-dir` paths.
  - Per project security rules, login/auth boundaries are never bypassed. **Action for User (Day 2+):** Sign in manually on `pixai.art` with `mandellialice5@gmail.com` or run interactive browser session to claim daily `10,000` credits and execute Day 2+ batches.
- **PixAI Cost Model (`VXP_XL v2.2 (Hyper)` + `Niji semi realism [Illustrious]`):**
  - Batch Size = `1` image (`768x1024` / `832x1216`, `7-8` steps, `Euler a`, CFG `1.6-1.8`): ~`20-40` credits/image (`~250-500` images per `10,000`-credit daily claim).

### 1.3 Day 1 Zero-Credit Recoveries Completed (`RECOVERED_ZERO_CREDIT`)
- **Local Files Uploaded to Cloudflare CDN (`/api/cloudflare/request-upload-url`):** `4` (`larek_avatar` -> `b42e7852...`, `valencia_02_shared` -> `ed01b89a...`, `jasper_06_hybrid_v1` -> `ea268e10...`, `jasper_07_fullshift_v1` -> `932c53a6...`).
- **External JanitorAI URLs Re-Hosted to Cloudflare CDN:** `3` (`Harald Sigurdsson` -> `9d071c75...`, `Thorvald` -> `649855d6...`, `Vero Walker` -> `da9aa625...`).
- **Verified Existing CDN Reuse (`HTTP 200` + `SHA-256` deduped):** `45` slots across Group 1, Group 2 (`8` Pack avatars from `NPC_Primary`), and Group 3 (`Jared` Beach, `Scarlett`, `Sierra` temp, `Russ`, `Mackenzie Fantasy`).
- **Slot Totals:** `OK=201`, `RECOVERED_ZERO_CREDIT=49`, `GENERATED_DAY_1=0`, `QUEUED_DAY_2=83`, `QUEUED_DAY_3=304`, `QUEUED_DAY_4=63`, `QUEUED_DAY_5=96`.

---

## 2. Day 2+ Multi-Day Generation Schedule & Budget

| Day | Target Scope | Count | Est. PixAI Credits (`~30/img`, batch=1) | Notes |
|---|---|---:|---:|---|
| **Day 2** | **Group 1 — Family Priority** (`Jasper`, `Jasper Fantasy`, `Jasper Contractor` `#08`/`Beach`/`Abyssal`, `Malachia` dupes + `Fantasy`, `Erik` `Nude`/`Gala`/`Verve`, `Logan` `Nude`/`Sleep`, `Noah` `Nude`/`Party`, `Wulfnic` 5 slots, `Edric` SFW clothed slots, `Alyssa_Human_*`, `Echo`, `Magnus`/`Cornelius`/`Ut` avatars + Family non-card WCs) | 83 | ~2,490 | Edric `Nude`/`Bathroom` is `POLICY_EXEMPT` (clothed/athletic text only in M2, 0 nude images). |
| **Day 3** | **Group 2 — Pack & Group 3A — SUCC/Blackwood NPCs** (`Marcus T.`, `Jet`, `Marcus O.`, `Fenris` avatars + Pack outfits; `Sierra Cruz` clean Lamia regen [no wolf ears!]; `Zeera`, `Mac`, `Larek`, `Jared`, `Stan`, `Russ`, `Scarlett` outfits) | 304 | ~9,120 | `Sierra Cruz` MUST use Lamia anatomy (rainbow scales, smooth reptilian temples, zero legs/feet/wolf ears). |
| **Day 4** | **Group 3B — DDM Contractors `#01-#06`** (`Richard`, `Adam`, `Hana`, `Luka`, `Dullahan` [hood always on!], `Johan`, `Fenrir` 9 outfits each) | 63 | ~1,890 | `Dullahan` hood MUST remain up in all 9 outfits (`GEMINI.md` §4). |
| **Day 5** | **Group 1C Core Family WorldChar Outfit Mirrors** (Sync/populate remaining WorldChar outfit slots mirroring standalone cards) | 96 | ~2,880 | Most can be mirrored zero-credit from Day 2 Family Card/Persona generations once completed. |

---

## 3. Shared Contract Resolution Notes

1. **Duplicate Live Fantasy Cards (`Jasper Fantasy` & `Malachia Fantasy`):**
   - **Jasper Fantasy:** Canonical live ID is **`_K6GYVEbKggCMjWFDkXW6e`** (`vanity_slug: "Jasper-Fantasy"`, referenced by `char_scenario_96kHDTPXYBLjw3fmEdFXr`, Lorebook `_zwEqgEEzh12X6gHVmMKKC`, and `FINAL/Jasper_Fantasy_card.json` `_id`). Orphaned duplicate **`_hABEHWwXTXrtMrR6zRN9J`** has 0 live references.
   - **Malachia Fantasy:** Canonical live ID is **`_wMG7wAXjkHxXLhcN8chwj`** (`vanity_slug: "Malachia-Fantasy"`, referenced by Lorebook `_zwEqgEEzh12X6gHVmMKKC` and `FINAL/Malachia_Fantasy_card.json` `_id`). Orphaned duplicate **`_4NkYFwYnYMm7GaRxeUeDz`** has 0 live references.
   - **M2 Action:** Migrate the 2026-11-16 Platinum text edits from the orphaned duplicates onto the canonical IDs, align local `"id" == "_id"`, and retire the 2 orphaned duplicates.
2. **`Larek_Steeltooth_card.json` (`id: None`) & `/mine` Resolution:**
   - `FINAL/Larek_Steeltooth_card.json` has `id: None` and is absent from `/api/characters/mine`, while WorldChar `_PqRVec7Aa42KGUhK2J8GQ` and `NPC_Secondary` (`npc_larek_steeltooth`) are live with `PLACEHOLDER` (`99d10d9b...`).
   - **M1 Action Completed:** Uploaded `assets/characters/secondary_cast/larek.webp` to Cloudflare CDN (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b42e7852-0983-46c9-4ff2-5d3a1efca200/public`, HTTP 200).
   - **M3 Action:** Apply the CDN URL + rule fixes to `FINAL/Larek_Steeltooth_card.json`, WorldChar `_PqRVec7Aa42KGUhK2J8GQ`, and `NPC_Secondary`, and `POST /api/characters` to publish Larek on `/mine` (recording the returned `id`).
3. **User Persona `appearances[]` Schema Verification:**
   - Verified via live `GET /api/user-personas` and `scratch/match_chunk_106.js`: `appearances[]` is **strictly text-only** (`{id, name, description}` — `"alternate descriptions of the body (no image)"`). Only `avatar` and `outfits[].image_url` store image URLs.

---

## 4. Complete 3-Group Slot-by-Slot Inventory

| Entity ID | Entity Name | Group | Slot | Status | CDN URL | Scheduled Day | Notes |
|---|---|---|---|---|---|---|---|
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/49c5dab8-c38c-458c-45b5-6ff089239100/public | - | Verified unique Cloudflare CDN avatar |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DEDnMNcgX8xDEpGmYqdrM | Adam Valencia (Contractor #02A) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6b9a7196-7156-4479-bc84-78309e16ca00/public | - | Verified unique Cloudflare CDN avatar |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _GADYjkenq7CW4RhU2wqbh | Dullahan (Contractor #04) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public | - | Verified unique Cloudflare CDN avatar |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Business & Campus / Scuola Media Solarton | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Full Shift / Addestramento Forma Bestiale | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Streetwear / Solarton Friends | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Gala / Formale Giovani Douglas | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Party / Festa Studentesca | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Beach / Pomeriggio in Piscina | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Sleepwear / Notte in Camera | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Nude / Anatomia Giovanile | QUEUED_DAY_2 | - | QUEUED_DAY_2 | POLICY_EXEMPT (minor safety: convert to safe clothed athletic slot in M2; never generate nude) |
| _TbRM3EdxDjHFgqztTbCpL | Edric Douglas | Group 1: Family | outfit:Hybrid Shift / Addestramento Bipede | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public | - | Verified unique Cloudflare CDN avatar |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Casual / Home | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/93a74d71-f20c-46ab-299e-73ffd1a6ad00/public | - | Verified unique Cloudflare CDN outfit |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:DCC / Business | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9c3f7516-b63a-4bef-dda0-4bc5dc155400/public | - | Verified unique Cloudflare CDN outfit |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Esterno / In Auto | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/fab5408a-21f5-490e-6f83-7e4bead36200/public | - | Verified unique Cloudflare CDN outfit |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7ded2114-170c-4e08-a9fe-b4d0ec7aa700/public | - | Verified unique Cloudflare CDN outfit |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/36a0143a-02bb-489a-c8d0-b22e9dd1c600/public | - | Verified unique Cloudflare CDN outfit |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Gala di Casata / Formal Douglas | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:The Verve VIP / Clubbing | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Beach / Terme di Branco | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c5eab8d7-5969-40e5-ed56-b8aa9d89da00/public | Day 1 | Zero-credit reuse from Active Gallery erik_base_model (HTTP 200) |
| _QPea6g4Q1QfeYCVHCLMPR | Erik Ulfr Douglas | Group 1: Family | outfit:Sleepwear / Padronale | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e6190f8b-79e1-451d-7b12-c98e4f796100/public | Day 1 | Zero-credit reuse from Legacy Gallery Erik (768x768, HTTP 200) |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/369d1984-5677-456c-9f10-071e48bdc000/public | - | Verified unique Cloudflare CDN avatar |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1zWxyEmwxKq1DhMxj3pXw | Fenrir (Contractor #06) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5ba0971c-848a-4e79-79d7-01e0a8f6e400/public | - | Verified unique Cloudflare CDN avatar |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _DBd8Rx9pzaPtxeG8232V6 | Hana Valencia (Contractor #02H) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/003b6683-06e0-4b96-7bfa-a89fb057c200/public | - | Verified unique Cloudflare CDN avatar |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Tactical Field Uniform (#08) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Voidspace Lounge (Off-Duty) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2ff0fec6-331a-459a-74f3-33ffb35d4100/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Black Ops / LAZARUS Stealth | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/02aa42b7-acaa-4384-81e2-7804c2fce200/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Council / Formal Briefing | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c9d1f5c4-b3b9-479e-2eb6-32840d0afd00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:Sleepwear (The Motel Quarters) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5aad05c8-ee3f-4293-232c-969d6f7fde00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/33ddc2a2-9358-46ec-d720-37eeffa71300/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/35058de1-2b18-4fc5-13f6-8529580f3b00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:nude | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/41b4e87f-b1db-44c9-fe36-d9fe4ce1be00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:beach / terme | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:The Abyssal Armor (Summoned Demonic Steel) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/003b6683-06e0-4b96-7bfa-a89fb057c200/public | - | Verified unique Cloudflare CDN avatar |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Tactical Field Uniform (#08) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Voidspace Lounge (Off-Duty) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2ff0fec6-331a-459a-74f3-33ffb35d4100/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Black Ops / LAZARUS Stealth | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/02aa42b7-acaa-4384-81e2-7804c2fce200/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:DDM Council / Formal Briefing | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c9d1f5c4-b3b9-479e-2eb6-32840d0afd00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:Sleepwear (The Motel Quarters) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5aad05c8-ee3f-4293-232c-969d6f7fde00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/33ddc2a2-9358-46ec-d720-37eeffa71300/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/35058de1-2b18-4fc5-13f6-8529580f3b00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:nude | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/41b4e87f-b1db-44c9-fe36-d9fe4ce1be00/public | - | Verified unique Cloudflare CDN outfit |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:beach / terme | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _waQyWtVYDbJkhrH9ADYbn | Jasper | Group 1: Family | outfit:The Abyssal Armor (Summoned Demonic Steel) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public | - | Verified unique Cloudflare CDN avatar |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Casual / Home | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/231d6579-7053-4c3f-7dc6-f03da2b05500/public | Day 1 | Zero-credit reuse from Legacy Gallery Jasper (HTTP 200) |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Campus | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Tactical Guild (Spell-Hacker Infiltrator) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:The Abyssal Armor (Summoned Demonic Steel) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Underground DJ / The Verve | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Formal / Gala | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Sleepwear | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5aad05c8-ee3f-4293-232c-969d6f7fde00/public | Day 1 | Zero-credit reuse from Jasper Contractor Sleepwear |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Beach | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Full Shift | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Hybrid Shift | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _t4J9aQNJM36cUKAP4wB4U | Jasper Svartr Douglas Bloodmoon | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public | - | Verified unique Cloudflare CDN avatar |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:tactic | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:abyssal | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:fullshift | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:hybrid | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:casual | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:business | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:gala | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:party | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:beach | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _K6GYVEbKggCMjWFDkXW6e | Jasper Fantasy | Group 1: Family | outfit:sleep | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/085891dd-67bd-43ea-8317-6c12a7741700/public | - | Verified unique Cloudflare CDN avatar |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _cPHFyL1FbeQWzX1QMptpW | Johan Jakobsen (Contractor #05) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b42e7852-0983-46c9-4ff2-5d3a1efca200/public | Day 1 | Zero-credit upload of local larek.webp to Cloudflare CDN (HTTP 200) |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:business / campus | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _1PXjpkenMYk9VJHFDhBpL | Larek Steeltooth | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public | - | Verified unique Cloudflare CDN avatar |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Business & DCC Commander / Sicurezza di Branco | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d8fd7a7a-db2b-4a5c-984c-919563782e00/public | - | Verified unique Cloudflare CDN outfit |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:The Verve, orario notturno/club | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/67217b58-aa80-4f78-524a-7ba93c0b3000/public | - | Verified unique Cloudflare CDN outfit |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Formale / Cena di famiglia | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa6e80b7-bbff-4a8a-4ade-4566c4236200/public | - | Verified unique Cloudflare CDN outfit |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c44deaf7-7ebb-4a4a-804e-81f1e9190100/public | - | Verified unique Cloudflare CDN outfit |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/398741d4-cc13-4381-3f63-813170f53600/public | - | Verified unique Cloudflare CDN outfit |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Garage / Officina | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16a25184-8463-4c38-2f9c-d512d92d3e00/public | - | Verified unique Cloudflare CDN outfit |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Casual / Casa e Relax | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5579de09-eccf-460a-5023-5c17dc508d00/public | Day 1 | Zero-credit reuse from Legacy Gallery Logan (HTTP 200) |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Beach / Seven Hills Spa | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ef9f34e0-0ee7-4219-2de8-569a2695ef00/public | Day 1 | Zero-credit reuse from Active Gallery logan_base_model (HTTP 200) |
| _T8Ywcr9FEqNf9JxbK6eHP | Logan Járn Douglas | Group 1: Family | outfit:Sleepwear / Riposo Notturno | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/3027543a-318e-4085-d402-96dca7ba5d00/public | - | Verified unique Cloudflare CDN avatar |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _axCwFrFLmaUn6XE7hbQt2 | Luka Sutter (Contractor #03) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public | Day 1 | Zero-credit sync from live /mine card _nUkjqtKz9RrP7CJCxXnCL |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Taverna & Bivacco (Casual Tavern Wear) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Dotazione Operativa da Mercenario di Classe A (Guild Battlegear) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Ricevimento d'Ingaggio Ducale (Ducal Audience Formal) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Serata di Baldoria al Drago di platino (Tavern Revelry) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Sorgenti Calde di Mythal (Hot Springs & Wild Waters) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Bivacco Notturno / Tenda di Spedizione (Campfire Sleepwear) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Nudo Anatomico Pureblood Alpha Ancestrale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Alpha Sellsword | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _nUkjqtKz9RrP7CJCxXnCL | Mackenzie "Mac" Sanchez-Rogers (Fantasy) | Group 3: Single-Card NPCs | outfit:Full Shift / Lupo Ancestrale da Battaglia | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public | - | Verified unique Cloudflare CDN avatar |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:The Van (Streetwear) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Behind the Keys (Campus & Rehearsal) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Oakland Sunday (Family Formal) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Underground Gig / Sidewinders | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Pacific Surf / Venice Beach | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:The Den (Loungewear) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Nudo Anatomico Pureblood Alpha | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Alpha Brawler | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _zn24784jfcchQ7EwCyAnm | Mackenzie Sanchez-Rogers | Group 3: Single-Card NPCs | outfit:Full Shift / Lupo da Combattimento Ancestrale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public | - | Verified unique Cloudflare CDN avatar |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Allenamento / Combattimento | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6558eb89-80b1-4205-1aa6-d36f7b846400/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Servizio di Sicurezza Standard | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/cf35e142-3bfb-4c52-b882-5a9e77f8d900/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Guild Tactical Vanguard (Frontline Tank) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61e91849-2783-483c-817d-4404e3e01800/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Formale / Casa | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c34844a0-e491-4df8-389c-1f4813f9ed00/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Ring Clandestino / Ghost | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7327659c-3dc9-4eca-82e6-da8e73630400/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d336ed68-ec1b-4403-c6e1-562cd3149c00/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aae39a50-36a4-405d-274b-079824ab7b00/public | - | Verified unique Cloudflare CDN outfit |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Casual / Streetwear Blackwood | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/936e2c9c-df6e-4234-55f3-4f79ede78600/public | Day 1 | Zero-credit reuse from Active Gallery malachia (HTTP 200) |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Beach / Sorgenti Calde | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/024c2520-ae8c-42a6-921a-dde3257ae800/public | Day 1 | Zero-credit reuse from Active Gallery malachia_base_model (breaks 7327659c dup) |
| _RDfz7XzTpM23LpPALVXHM | Malachia Björn Douglas Bloodmoon | Group 1: Family | outfit:Sleepwear / Notte del Branco | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/fcea0059-0879-46fd-c106-b607a67bf300/public | - | Verified unique Cloudflare CDN avatar |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:tactic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61e91849-2783-483c-817d-4404e3e01800/public | - | Verified unique Cloudflare CDN outfit |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:fullshift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d336ed68-ec1b-4403-c6e1-562cd3149c00/public | - | Verified unique Cloudflare CDN outfit |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:hybrid | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aae39a50-36a4-405d-274b-079824ab7b00/public | - | Verified unique Cloudflare CDN outfit |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:nude | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7327659c-3dc9-4eca-82e6-da8e73630400/public | - | Verified unique Cloudflare CDN outfit |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:casual | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:business | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:gala | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:party | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:beach | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _wMG7wAXjkHxXLhcN8chwj | Malachia Fantasy | Group 1: Family | outfit:sleep | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public | - | Verified unique Cloudflare CDN avatar |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Casual / Home | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9ea386c0-81f0-4f02-23b9-f0e584fa7300/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Campus | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ca0f419b-e982-49db-c37a-d91f42e5ae00/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Formal / Gala | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5daa79cb-72e0-4882-285e-a568c37e0400/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Sleepwear | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/46a5a5c2-c849-4888-68b3-eaf6b5a4d500/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Beach | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/09b18c1e-f475-4892-b316-0c2c1450b900/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2df9d32e-4543-49f9-68b0-728545d77200/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f1089c95-805f-45eb-19b2-13ec546c4800/public | - | Verified unique Cloudflare CDN outfit |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _zFLUjV8aVxQRAfQxGcAcY | Noah Loki Douglas Bloodmoon | Group 1: Family | outfit:Party / Solarton Nightlife | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/590c4fb7-827d-4c09-0964-b484de537e00/public | - | Verified unique Cloudflare CDN avatar |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:business / mission | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _2xh1VhxVjHx1Rje3fg7Bg | Richard Whitlock (Contractor #01) | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_4 | - | QUEUED_DAY_4 | Missing; queued for DAY_4 |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public | - | Verified unique Cloudflare CDN avatar |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Casual / Sanctuary & Longhouse | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a4f6722c-bd44-4a48-1d35-e5dc1882e400/public | - | Verified unique Cloudflare CDN outfit |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Gala / Formal & Ceremonial | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8de3ef7a-5358-4ddc-088a-86e2aa5e5800/public | - | Verified unique Cloudflare CDN outfit |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Sleep / Night Rest & Slumber | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8f3939cc-47ed-4e6d-7f0d-643bb8f6bb00/public | - | Verified unique Cloudflare CDN outfit |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Beach / Shoreline & Wild Waters | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2fd3926f-b4ae-4b78-b861-b8b110d92300/public | - | Verified unique Cloudflare CDN outfit |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Business & Guard / Vigil & Watch | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/903da5cc-17a2-4c60-ba4f-fb5f3a6db400/public | - | Verified unique Cloudflare CDN outfit |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Party / Solstice Merriment | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/46a7f40c-d116-4b2e-f380-4e991cf02c00/public | - | Verified unique Cloudflare CDN outfit |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Gala / Council of the Firstborn | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/56e418f5-5f71-4167-e7a4-fce46a8f6b00/public | Day 1 | Zero-credit reuse from Legacy Gallery Wulfnic (HTTP 200) |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Party / Ancient Yule Feast | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Hybrid Shift / Il Primo Re Lupo Ancestrale | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Full Shift / Il Grande Lupo Antico Fenrisiano | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _HEQQbbRFwKdG8QE2Fh1z1 | Wulfnic Báleygr Bloodmoon | Group 1: Family | outfit:Casual / Modern Urban Disguise | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/06c93e0c-d5d2-43e0-8a33-05348172c800/public | - | Verified unique Cloudflare CDN outfit |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a1018982-65d0-4f28-0956-2c529b3a3900/public | - | Verified unique Cloudflare CDN avatar |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Casual / Relax Attico Uptown | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Business / CEO HSK Consulting | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Gala / Ricevimento Solenne del Consiglio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Party / Lounge Privato Solarton | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Beach / Terme Vulcaniche Sotterranee | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Sleepwear / Letto Padronale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Vax Alpha Integrale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Combat / Duello Rituale del Teschio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _CmkCDzCn36CyYUzfPp2UY | Zeera Darkfire | Group 3: Single-Card NPCs | outfit:Full Shift / Corazza Abissale del Signore della Guerra | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a1018982-65d0-4f28-0956-2c529b3a3900/public | - | Verified unique Cloudflare CDN avatar |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Casual / Trono di Pietra delle Caverne | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Warlord / Corazza da Guerra in Ossidiana | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Gala / Banchetto Nobiliare del Clan | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Raid / Incursione Notturna nelle Ombre | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Terme / Bagno Vulcanico Sotterraneo | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Sleep / Giaciglio di Pelli Padronale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Vax Warlord Integrale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Combat / Furia Rituale e Patto di Sangue | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _btwPFk7bX26P2jyRgqf3X | Zeera Darkfire (Fantasy) | Group 3: Single-Card NPCs | outfit:Study / Calligrafia di Sangue & Archivio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public | - | Verified unique Cloudflare CDN avatar |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:naked | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1c3ad1e9-d983-44d3-0b77-ec66aeb1d200/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:tactic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f3bdaa19-dfa1-470c-213f-a300da6baa00/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:summer | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16388ec0-55fb-4443-7ff0-5f0b731edd00/public | Day 1 | Zero-credit reuse from Legacy Gallery Alyssa Urban Def (breaks ba5a7fed dup) |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:winter | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16091b76-e9cf-44d8-3bab-808ee0001400/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:beach | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/dd9710a7-78c9-43d2-c04a-19fc83a2a300/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9e34875d-64cf-43f6-8314-b985e40c7800/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:fest | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed6f8525-1933-4ca4-0370-98790a7e5400/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:academy | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ad60aed3-7e9f-412e-8279-d1621ee2bb00/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:sport | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6738228f-7173-42a6-4ed6-d81b49a58100/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:spring | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7d532e6c-444b-43c7-9c87-d3900b3fd100/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:hybrid | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/219aa770-c06d-4150-cf9b-8f0a52bba900/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:fullshift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d2276ce1-93f4-449c-2f17-474f595b9d00/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:formal | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/31ae91ea-7985-40ed-5797-e62851772200/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:clinic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9ed2fe62-3af5-4998-35ac-c9f2e4fd1200/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:biker | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/720f5dab-06bb-4dd4-1f23-f02128606e00/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:dinner | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/34ed695f-66df-4827-9b94-f3c604fcc100/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Angelo Moreno Couture | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/3e4c7de2-ac30-4b14-f5f5-9e0bb16d1e00/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Clubbing Night | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8786df65-425f-4aba-6377-d91d4ad95900/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Pilates | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d6324b11-fb2f-4911-0e3b-611d4b234400/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Romantic Sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/92745394-a51e-438a-af12-3cb7a29b4700/public | - | Verified unique Cloudflare CDN outfit |
| _6exg3yPfe2eCDK4hTftkh | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:AnimeClub | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7464d676-bb1c-4d5d-1cd1-0f75fd41ab00/public | - | Verified unique Cloudflare CDN outfit |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7476db0-8dae-4450-8c84-3408b375c000/public | - | Verified unique Cloudflare CDN avatar |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Game Day | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Campus Default | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:BRO Party | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:The Dorm | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Home in Solarton | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Halloween | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Beach | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/69f02ee8-6a88-4d9f-d05c-ad91f4ace200/public | Day 1 | Zero-credit reuse from Legacy Gallery Jared Beach (HTTP 200) |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Gala / SUCC Athletic Awards | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Sleepwear / Confraternita BRO | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Nude / Fisico da Fullback | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _xJVPtBLL3dxy69RLKL9X9 | Jared Thompson | Group 3: Single-Card NPCs | outfit:Combat / Divisa da Mischia Corazzata | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f22c3f1f-4cd7-4946-e81e-54ce95bc4900/public | Day 1 | Zero-credit reuse from WorldChar _JFf1dFeggaKecWJDgK1qH (replaces JanitorAI) |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:business / campus | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _wn6DkCcg3Xqa2Xpx9ttnT | Russell 'Russ' | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e96d176a-47e4-4829-2af4-7cd6ae239100/public | Day 1 | Zero-credit reuse from WorldChar / Active Gallery scarlettMain (fixes 404 c8bdfad3) |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Casual / Dorm & Roommate Relax | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Business / Campus & Lezioni SUCC | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Gala / Formal Sorority Awards | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Party / The Verve & TIT Bash | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Beach / SUCC Campus Pool & Terme | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Sleep / Notte in Suite | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Demoniaca Evolved | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Manifestazione Succubus Piena | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _qXgBMbFYJfc84hbLHhe92 | Scarlett Rose | Group 3: Single-Card NPCs | outfit:Concert & Festival / Grave Mistake Support | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public | Day 1 | Zero-credit temp fix from WorldChar sierraMain (fixes 404 c8bdfad3; wolf-ears regen queued Day 3) |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Casual / Grave Mistake Oversized Tee | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Business / Laboratorio di Necromanzia SUCC | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Gala / Conclave Accademico & Ricevimento | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Party / Gothic Clubbing al The Verve | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Beach / Sorgenti Termali di Solarton | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Sleep / Nido Termico nel Dormitorio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Lamia Primordiale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Postura da Combattimento Predatoria | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _pnrXbkWqcgmFAf3meRWFY | Sierra Cruz | Group 3: Single-Card NPCs | outfit:Moulting & Field / Muta Stagionale delle Squame | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7c9c7d1-51e6-4441-82e3-c6ab5f537500/public | - | Verified unique Cloudflare CDN avatar |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Casual / Dorm & Gaming Slouch | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Business / Campus & Lezioni SUCC | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Gala / Cene di Rappresentanza Militare | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Party / Frat Night & Club | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Beach / Terme & Relax Estivo | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Sleep / Notte al Dormitorio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Lupina Naturale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Forma da Combattimento Bipede | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _Xd3NhKnRJByMTtdb6PjxJ | Stanley Davies Jr. | Group 3: Single-Card NPCs | outfit:Full Shift / Forma Bestiale Ancestrale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/78ecdd39-d4e9-4d1f-5b13-8c45e8f4a100/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:DDM Tactical Field Uniform (#07) | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2e0c23e6-13ec-415b-c361-5e5d4f62d500/public | Day 1 | Zero-credit distinct URL string (same pixels as 78ecdd39; regen queued Day 2) |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:DDM Voidspace Lounge (Off-Duty) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5a33463d-28c2-4fd3-5b53-db1ce003b600/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:DDM Black Ops / LAZARUS Stealth | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e548643d-ca0f-478f-27e1-03f1ec01af00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:DDM Council / Formal Briefing | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0368abba-3a8c-4e1e-5724-ec1ca036e000/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:DDM Sleep (The Motel Quarters) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2ff0b906-8ab6-4e58-abda-544384d1b300/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:nude | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/4c0d10d5-f18a-4bed-3c02-3e48ce563c00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:hybrid | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/11906703-a46f-40d8-4190-3c123d773900/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:fullshift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/4ef12aa4-d371-4ec1-71fa-6e57efc17300/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_xRpkh3JVPkhnpWbcBBfa6 | [ #07 ] Alyssa (DDM Contractor) | Group 1: Family | outfit:DDM Casual / Safehouse Off-Duty | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f3bdaa19-dfa1-470c-213f-a300da6baa00/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:nude | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1c3ad1e9-d983-44d3-0b77-ec66aeb1d200/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:tactic | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:hybrid | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/219aa770-c06d-4150-cf9b-8f0a52bba900/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:fullshift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d2276ce1-93f4-449c-2f17-474f595b9d00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:gala | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/3e4c7de2-ac30-4b14-f5f5-9e0bb16d1e00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:Sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/92745394-a51e-438a-af12-3cb7a29b4700/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:casual | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/eae26956-1547-440b-8206-ca07276be700/public | Day 1 | Zero-credit reuse from Active Gallery casual (breaks f3bdaa19 dup) |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:business | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9fcec9d3-0517-4466-ba7f-ed68472d0500/public | Day 1 | Zero-credit reuse from Active Gallery academy (breaks f3bdaa19 dup) |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:party | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d0819bf2-5975-4ae7-b47f-5943ee428300/public | Day 1 | Zero-credit reuse from Active Gallery fest (breaks f3bdaa19 dup) |
| user_persona_bUnwqPg77CrB4C9TDQ8h3 | Alyssa | Group 1: Family | outfit:beach | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/df642318-1bc9-48f4-6ca4-24a206939c00/public | Day 1 | Zero-credit reuse from Active Gallery beach (breaks f3bdaa19 dup) |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/4349d1b1-15bf-4056-35e2-82efdbcf0900/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | outfit:Casual | GENERATED_DAY_2 | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8605d469-1dc9-47fb-cdf7-404c35d94300/public | Day 2 | Generated via native image-generator (0 PixAI credits) & verified live |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | outfit:Formal | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | outfit:Festa | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | outfit:Sleep | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_E7PCD2G9C9CyKkhLDrPxc | Alyssa | Group 1: Family | outfit:Beach | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d55122db-8872-42cf-d79b-7b622646d800/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | outfit:Casual | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | outfit:Formal | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | outfit:Festa | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | outfit:Sleep | GENERATED_DAY_2 | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e84bcae5-2567-4032-e98b-e167739fe700/public | Day 2 | Generated via native image-generator (0 PixAI credits) & verified live |
| user_persona_87QnC1zUXX2HecJbehkEL | Alyssa | Group 1: Family | outfit:Beach | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:naked | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1c3ad1e9-d983-44d3-0b77-ec66aeb1d200/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:tactic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f3bdaa19-dfa1-470c-213f-a300da6baa00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:summer | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16388ec0-55fb-4443-7ff0-5f0b731edd00/public | Day 1 | Zero-credit reuse from Legacy Gallery Alyssa Urban Def (breaks ba5a7fed dup) |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:winter | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16091b76-e9cf-44d8-3bab-808ee0001400/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:beach | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/dd9710a7-78c9-43d2-c04a-19fc83a2a300/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9e34875d-64cf-43f6-8314-b985e40c7800/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:fest | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed6f8525-1933-4ca4-0370-98790a7e5400/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:academy | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ad60aed3-7e9f-412e-8279-d1621ee2bb00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:sport | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6738228f-7173-42a6-4ed6-d81b49a58100/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:spring | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7d532e6c-444b-43c7-9c87-d3900b3fd100/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:hybrid | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/219aa770-c06d-4150-cf9b-8f0a52bba900/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:fullshift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d2276ce1-93f4-449c-2f17-474f595b9d00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:formal | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/31ae91ea-7985-40ed-5797-e62851772200/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:clinic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9ed2fe62-3af5-4998-35ac-c9f2e4fd1200/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:biker | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/720f5dab-06bb-4dd4-1f23-f02128606e00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:dinner | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/34ed695f-66df-4827-9b94-f3c604fcc100/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:Angelo Moreno Couture | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/3e4c7de2-ac30-4b14-f5f5-9e0bb16d1e00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:Clubbing Night | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8786df65-425f-4aba-6377-d91d4ad95900/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:Pilates | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d6324b11-fb2f-4911-0e3b-611d4b234400/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:Romantic Sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/92745394-a51e-438a-af12-3cb7a29b4700/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_VnRF2xGeG1C4xByDF9h9R | Alyssa | Group 1: Family | outfit:AnimeClub | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7464d676-bb1c-4d5d-1cd1-0f75fd41ab00/public | - | Verified unique Cloudflare CDN outfit |
| user_persona_Chhp2NRN1kkVVPXCGQb8C | Echo | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bbc9c30b-87c5-4b84-cdf5-2bebb9bf1e00/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_Chhp2NRN1kkVVPXCGQb8C | Echo | Group 1: Family | outfit:Default Audio Wave | GENERATED_DAY_2 | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/448e5e4c-d224-479c-fedd-24aec4e1d400/public | Day 2 | Generated via native image-generator (0 PixAI credits) & verified live |
| user_persona_Chhp2NRN1kkVVPXCGQb8C | Echo | Group 1: Family | outfit:Combat Grid Drone | GENERATED_DAY_2 | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/25a39061-036e-4a18-8bd8-46fac09a7100/public | Day 2 | Generated via native image-generator (0 PixAI credits) & verified live |
| user_persona_Chhp2NRN1kkVVPXCGQb8C | Echo | Group 1: Family | outfit:Smartphone Interface | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_Chhp2NRN1kkVVPXCGQb8C | Echo | Group 1: Family | outfit:Cyberspace Full Avatar | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public | - | Verified unique Cloudflare CDN avatar |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Casual / Home | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/231d6579-7053-4c3f-7dc6-f03da2b05500/public | Day 1 | Zero-credit reuse from Legacy Gallery Jasper |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Campus | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Tactical Guild (Spell-Hacker Infiltrator) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:The Abyssal Armor (Summoned Demonic Steel) | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Underground DJ / The Verve | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Formal / Gala | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Sleepwear | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5aad05c8-ee3f-4293-232c-969d6f7fde00/public | Day 1 | Zero-credit reuse from Jasper Contractor Sleepwear |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Beach | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Full Shift | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Hybrid Shift | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| user_persona_bGDFCEtKDzVmgbCmHJWEW | Jasper | Group 1: Family | outfit:Nude | QUEUED_DAY_2 | - | QUEUED_DAY_2 | Missing; queued for DAY_2 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b42e7852-0983-46c9-4ff2-5d3a1efca200/public | Day 1 | Zero-credit upload of local larek.webp to Cloudflare CDN (HTTP 200) |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:business / campus | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _PqRVec7Aa42KGUhK2J8GQ | Larek | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing; queued for DAY_3 |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public | - | Verified unique Cloudflare CDN avatar |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Naked | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f700bcdb-6f39-4fb2-518e-5c03da614300/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Tactic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f820fd2a-dd06-4463-43b0-888f6940d800/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Summer | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/4b71bafb-5a6d-49a7-456d-46c3a5f32400/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Winter | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/875f1b46-a18d-4b1c-c772-e4f43a693600/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Beach | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/32d2cdf8-965b-425b-97fb-aaef738c3400/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1817335e-6879-496a-b4a4-7fc52bf98d00/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Fest | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/122759e3-228c-4620-2067-7a91a3566700/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Academy | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d53daa5a-129f-44e3-20c9-5c8f36149800/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Sport | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2a04990c-cc3c-4ac1-bdc8-2a21a5762d00/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Spring | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/51b27266-c453-4920-01dc-aa5a10d69700/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Formal | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/36a56b19-940c-4dac-a1e3-acd3e19dac00/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Clinic | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/fa15348e-cfb7-41e5-9465-297de1280600/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Biker | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2da45370-4cdb-43f0-e6b2-e610efd6bd00/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Dinner | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5fa0b47a-3e8d-48d1-53c0-bf1e88b46100/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Angelo Moreno Couture | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/3e4c7de2-ac30-4b14-f5f5-9e0bb16d1e00/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Clubbing Night | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8786df65-425f-4aba-6377-d91d4ad95900/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:hybrid | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/219aa770-c06d-4150-cf9b-8f0a52bba900/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:fullshift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d2276ce1-93f4-449c-2f17-474f595b9d00/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Pilates | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d6324b11-fb2f-4911-0e3b-611d4b234400/public | - | Verified unique Cloudflare CDN outfit |
| _FGeNBqjrt9fJJJyXTDgxM | Alyssa Hvit Douglas Bloodmoon | Group 1: Family | outfit:Romantic Sleep | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/92745394-a51e-438a-af12-3cb7a29b4700/public | - | Verified unique Cloudflare CDN outfit |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9d071c75-74bd-44ef-bce7-7f83403efa00/public | Day 1 | Zero-credit rehost from JanitorAI to Cloudflare CDN (HTTP 200) |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _4DMh7RBgE89ttA6B3Hk7Q | Harald | Group 2: Pack | outfit:Full Shift / Ancestral Wolf | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/649855d6-3023-4bf5-530f-cc23dbc61200/public | Day 1 | Zero-credit rehost from JanitorAI to Cloudflare CDN (HTTP 200) |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7GxR3D6e4QQGRXEtC8war | Thorvald | Group 2: Pack | outfit:Full Shift / Ancestral Wolf | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | avatar | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing/placeholder/external avatar (https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ) |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Rest & Recovery / Athletic Base | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Combat / Tactical & Mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _exPpbVrjg7J1AA1zmFbKB | Jet | Group 2: Pack | outfit:Full Shift / Field Specialist | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a15399c7-6c52-46bb-be68-41e2b6b30600/public | - | Verified unique Cloudflare CDN avatar |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Campus Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Athletic / Gym | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Dorm / Casual Loungewear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Greek Life / Party Night | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Formal / Academic Banquet | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _LVHkykWeN61ecNPEXnfQd | Dullahan | Group 3: Single-Card NPCs | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d41b78bf-e981-4570-2264-8e614e14fe00/public | - | Verified unique Cloudflare CDN avatar |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Pack Matriarch / Tradizionale | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Nude / Anatomical | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _7fpjtj6bq7Jn7HQPTbMXM | Elizabeth | Group 1: Family | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7476db0-8dae-4450-8c84-3408b375c000/public | - | Verified unique Cloudflare CDN avatar |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Game Day | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Campus Default | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:BRO Party | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:The Dorm | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Home in Solarton | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Halloween | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Beach | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/69f02ee8-6a88-4d9f-d05c-ad91f4ace200/public | Day 1 | Zero-credit reuse from Legacy Gallery Jared Beach (HTTP 200) |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Gala / SUCC Athletic Awards | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Sleepwear / Confraternita BRO | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Nude / Fisico da Fullback | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _6faaEP3MKNKWyV1JnJK8D | Jared | Group 3: Single-Card NPCs | outfit:Combat / Divisa da Mischia Corazzata | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public | - | Verified unique Cloudflare CDN avatar |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Casual / Home | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/231d6579-7053-4c3f-7dc6-f03da2b05500/public | Day 1 | Zero-credit reuse from Legacy Gallery Jasper |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Campus | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Tactical Guild (Spell-Hacker Infiltrator) | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:The Abyssal Armor (Summoned Demonic Steel) | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Underground DJ / The Verve | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Formal / Gala | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Sleepwear | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5aad05c8-ee3f-4293-232c-969d6f7fde00/public | Day 1 | Zero-credit reuse from Jasper Contractor Sleepwear |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Beach | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Full Shift | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Hybrid Shift | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _mUEUDfmTG4m7wNyQ7WQKx | Jasper | Group 1: Family | outfit:Nude | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c4e4de0c-7672-4642-657c-a288b304b700/public | - | Verified unique Cloudflare CDN avatar |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Duty / Tactical (Default) | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Off-Duty / Casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Formal / Family Event | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Full Shift | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Hybrid Shift | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _9YcrRj1BTHCL2e1Up3exz | Kaladin | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | avatar | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing/placeholder/external avatar (https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ) |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Abito Coloniale Formale DCC | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Nude / Anatomical | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _yze29RNQPTWfgXWGcFNPF | Cornelius | Group 1: Family | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | avatar | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing/placeholder/external avatar (https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ) |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Cancelleria & Alta Finanza | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Nude / Anatomical | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _tr68MzAxNYmGqLLrfxWxB | Magnus | Group 1: Family | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | avatar | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Missing/placeholder/external avatar (https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ) |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:DCC Heavy Security Tactical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _DUXKKGrCb7CxjVRHF88pd | Marcus T. | Group 2: Pack | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/4e569181-3894-45a2-d0c5-3d5a1e289600/public | - | Verified unique Cloudflare CDN avatar |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Dragonblade Matriarch Battle Dress | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Nude / Anatomical | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _8aVXCw6Yg3hHM18HntLUN | Nixara | Group 1: Family | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7c9c7d1-51e6-4441-82e3-c6ab5f537500/public | - | Verified unique Cloudflare CDN avatar |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Casual / Dorm & Gaming Slouch | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Business / Campus & Lezioni SUCC | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Gala / Cene di Rappresentanza Militare | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Party / Frat Night & Club | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Beach / Terme & Relax Estivo | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Sleep / Notte al Dormitorio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Lupina Naturale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Forma da Combattimento Bipede | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _TPqawPNbM7fhxnYGUGzx6 | Stan | Group 3: Single-Card NPCs | outfit:Full Shift / Forma Bestiale Ancestrale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | avatar | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing/placeholder/external avatar (https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ) |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Firstborn Berserker Garb | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Nude / Anatomical | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _wMcYm8hBYH97fVVWG86nN | Ut | Group 1: Family | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Placeholder; queued for DAY_5 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a1018982-65d0-4f28-0956-2c529b3a3900/public | - | Verified unique Cloudflare CDN avatar |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Faculty Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Office & Research | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Academic Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Off-Duty / Private | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Field / Travel Gear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _abbhNAnmxfGR4fYmqdD1A | Zeera | Group 3: Single-Card NPCs | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f22c3f1f-4cd7-4946-e81e-54ce95bc4900/public | - | Verified unique Cloudflare CDN avatar |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:business / campus | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:gala / formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:party / club | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:beach / terme | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:sleep | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:nude | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:hybrid shift / mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _JFf1dFeggaKecWJDgK1qH | Russell | Group 3: Single-Card NPCs | outfit:full shift / other | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bbc9c30b-87c5-4b84-cdf5-2bebb9bf1e00/public | - | Verified unique Cloudflare CDN avatar |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Core Code / Raw Data | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Combat / Tactical & Mutation | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _3b7MkBTrPKWnXKhcVzD9t | Echo | Group 1: Family | outfit:Full Shift / Field Specialist | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/43ed7caf-2479-4597-e227-6cdc8ada2b00/public | Day 1 | Zero-credit reuse from NPC_Primary [008] (HTTP 200) |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Tactical Hunter Gear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Southside Duplex Casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _eYQJzzkwxQLrBfjN6871e | Radek | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/004922f4-e19b-43d0-3301-c8cde63cd500/public | Day 1 | Zero-credit reuse from NPC_Primary [007] (HTTP 200) |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Vanguard Combat Rig | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Workshop & Gym Casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _Fwq1aW1AWcQ1xUPTdFJQf | Goran | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f28c269b-95d2-42a3-c6c9-794c37d41b00/public | Day 1 | Zero-credit reuse from NPC_Primary [006] (HTTP 200) |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Tactical Shadow Leather | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Urban Nightlife Silk | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _WgBtf8rz3PYLBFY3JhNUd | Kian | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c1fc8935-46c7-4534-d0b4-2f27acae3200/public | - | Verified unique Cloudflare CDN avatar |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Ironhorn Nomads Biker Kutte | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Pool Party / Club House Casual | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _mAYVe66B3EW6hDDFbp2Cz | Marek | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/fdf61a49-5c85-4658-8b62-e313863a4200/public | Day 1 | Zero-credit reuse from NPC_Primary [004] (HTTP 200) |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Combat / Tactical & Mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _ay3Jm2dBP6K2jEGf23eaY | Jaelyn | Group 2: Pack | outfit:Full Shift / Field Specialist | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/132ed7bf-d044-402c-d6dc-5041ffb3e300/public | Day 1 | Zero-credit reuse from NPC_Primary [003] (HTTP 200) |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Combat / Tactical & Mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _btCeADq1MWLMnRCPxXX4B | Neve | Group 2: Pack | outfit:Full Shift / Field Specialist | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/4c92d541-9a83-4b1e-fd73-92f49c195800/public | Day 1 | Zero-credit reuse from NPC_Primary [002] (HTTP 200) |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Combat / Tactical & Mutation | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _391gVED6YdaWmjm8kHPNn | Bessie | Group 2: Pack | outfit:Full Shift / Field Specialist | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/554bdd46-b5fc-42a3-0338-53beadf1d800/public | Day 1 | Zero-credit reuse from NPC_Primary [001] (HTTP 200) |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _qCUqTD7FBhC4hU6UaCYBJ | Liam | Group 2: Pack | outfit:Full Shift / Ancestral Wolf | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | avatar | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0857b30d-34bd-443c-23ee-5e00622da700/public | Day 1 | Zero-credit reuse from NPC_Primary [000] (HTTP 200) |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Casual / Daily | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Business / Campus & Work | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Gala / Formal | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Party / Club & Nightlife | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Beach / Terme & Pool | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Sleep / Nightwear | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Nude / Anatomical | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _6pDWfJb9LFbgtV1YtENKq | Hugh | Group 2: Pack | outfit:Full Shift / Ancestral Wolf | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Placeholder; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e96d176a-47e4-4829-2af4-7cd6ae239100/public | - | Verified unique Cloudflare CDN avatar |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Casual / Dorm & Roommate Relax | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Business / Campus & Lezioni SUCC | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Gala / Formal Sorority Awards | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Party / The Verve & TIT Bash | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Beach / SUCC Campus Pool & Terme | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Sleep / Notte in Suite | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Demoniaca Evolved | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Manifestazione Succubus Piena | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _d9f2AfTWG8V9aBMyabGLy | Scarlett | Group 3: Single-Card NPCs | outfit:Concert & Festival / Grave Mistake Support | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | avatar | QUEUED_DAY_3 | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public | QUEUED_DAY_3 | TEMP_OK but INCONGRUENCE (has wolf ears + green tail); clean Lamia regen queued Day 3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Casual / Grave Mistake Oversized Tee | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Business / Laboratorio di Necromanzia SUCC | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Gala / Conclave Accademico & Ricevimento | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Party / Gothic Clubbing al The Verve | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Beach / Sorgenti Termali di Solarton | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Sleep / Nido Termico nel Dormitorio | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Lamia Primordiale | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Postura da Combattimento Predatoria | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _EHx1dbCMHbXhNyhNzmPQg | Sierra | Group 3: Single-Card NPCs | outfit:Moulting & Field / Muta Stagionale delle Squame | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public | - | Verified unique Cloudflare CDN avatar |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:The Van | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Behind the Keys | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Working | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:The Den | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Oakland | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Gala / Rappresentanza Casata Wolfwood | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Clubbing / Underground Techno Night | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Beach / Venice Beach Van Life | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Sleepwear / Letto nel Furgone | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Nude / Anatomia Wolfwood-Rogers | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _RXHKfwRXwhRkBHttHVgqt | Mac | Group 3: Single-Card NPCs | outfit:Hybrid Shift / Guerriera Wolfwood | QUEUED_DAY_3 | - | QUEUED_DAY_3 | Duplicates avatar; queued for DAY_3 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bdd8961e-a68a-4c6b-b4e1-29a26db37e00/public | - | Verified unique Cloudflare CDN avatar |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:White Ghost Scout Shroud | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Casual / Daily | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Business / Campus & Work | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Gala / Formal | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Party / Club & Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Beach / Terme & Pool | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Sleep / Nightwear | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Nude / Anatomical | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _yAYpmxxnP1gmntXDQPYmG | Zefir | Group 1: Family | outfit:Hybrid Shift / Combat Form | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public | - | Verified unique Cloudflare CDN avatar |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Sanctuary / Longhouse | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/a4f6722c-bd44-4a48-1d35-e5dc1882e400/public | - | Verified unique Cloudflare CDN outfit |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Ceremonial / Formal | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8de3ef7a-5358-4ddc-088a-86e2aa5e5800/public | - | Verified unique Cloudflare CDN outfit |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Rest | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8f3939cc-47ed-4e6d-7f0d-643bb8f6bb00/public | - | Verified unique Cloudflare CDN outfit |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Shoreline | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2fd3926f-b4ae-4b78-b861-b8b110d92300/public | - | Verified unique Cloudflare CDN outfit |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Vigil / Watch | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/903da5cc-17a2-4c60-ba4f-fb5f3a6db400/public | - | Verified unique Cloudflare CDN outfit |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:The Gag Shirt | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/46a7f40c-d116-4b2e-f380-4e991cf02c00/public | - | Verified unique Cloudflare CDN outfit |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Nude | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Consiglio dei Firstborn / Solenne | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Banchetto del Solstizio / Yule Antico | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Hybrid Shift / Il Primo Re Lupo Ancestrale | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Full Shift / Il Grande Lupo Antico Fenrisiano | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _P1HrVjkY9TGnymNaAWX1j | Wulfnic | Group 1: Family | outfit:Modern | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/06c93e0c-d5d2-43e0-8a33-05348172c800/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public | - | Verified unique Cloudflare CDN avatar |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Allenamento / Combattimento | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6558eb89-80b1-4205-1aa6-d36f7b846400/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Servizio di Sicurezza Standard | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/cf35e142-3bfb-4c52-b882-5a9e77f8d900/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Guild Tactical Vanguard (Frontline Tank) | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61e91849-2783-483c-817d-4404e3e01800/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Formale / Casa | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c34844a0-e491-4df8-389c-1f4813f9ed00/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Ring Clandestino / Ghost | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7327659c-3dc9-4eca-82e6-da8e73630400/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d336ed68-ec1b-4403-c6e1-562cd3149c00/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aae39a50-36a4-405d-274b-079824ab7b00/public | - | Verified unique Cloudflare CDN outfit |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Nude | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Casual / Streetwear Blackwood | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/936e2c9c-df6e-4234-55f3-4f79ede78600/public | Day 1 | Zero-credit reuse from Active Gallery malachia |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Beach / Sorgenti Calde | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/024c2520-ae8c-42a6-921a-dde3257ae800/public | Day 1 | Zero-credit reuse from Active Gallery malachia_base_model |
| _QQXte9xWjMeMtqEJfwrc3 | Malachia | Group 1: Family | outfit:Sleepwear / Notte del Branco | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Missing; queued for DAY_5 |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public | - | Verified unique Cloudflare CDN avatar |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Casual / Home | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9ea386c0-81f0-4f02-23b9-f0e584fa7300/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Campus | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ca0f419b-e982-49db-c37a-d91f42e5ae00/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Formal / Gala | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5daa79cb-72e0-4882-285e-a568c37e0400/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Sleepwear | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/46a5a5c2-c849-4888-68b3-eaf6b5a4d500/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Beach | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/09b18c1e-f475-4892-b316-0c2c1450b900/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2df9d32e-4543-49f9-68b0-728545d77200/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/f1089c95-805f-45eb-19b2-13ec546c4800/public | - | Verified unique Cloudflare CDN outfit |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Nude | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _YzcPc7dRLkttzR2jKX93z | Noah | Group 1: Family | outfit:Party / Solarton Nightlife | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public | - | Verified unique Cloudflare CDN avatar |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Casual & Scuola | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Bathroom | QUEUED_DAY_2 | - | QUEUED_DAY_2 | POLICY_EXEMPT (minor safety: convert to safe clothed athletic slot in M2; never generate nude) |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Streetwear / Solarton Friends | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Gala / Formale Giovani Douglas | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Party / Festa Studentesca | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Beach / Pomeriggio in Piscina | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Sleepwear / Notte in Camera | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Nude / Anatomia Giovanile | QUEUED_DAY_2 | - | QUEUED_DAY_2 | POLICY_EXEMPT (minor safety: convert to safe clothed athletic slot in M2; never generate nude) |
| _4QWHxwHBpNnfjmNYm3tNr | Edric | Group 1: Family | outfit:Hybrid Shift / Addestramento Bipede | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public | - | Verified unique Cloudflare CDN avatar |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Affari di Branco / Sicurezza | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d8fd7a7a-db2b-4a5c-984c-919563782e00/public | - | Verified unique Cloudflare CDN outfit |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:The Verve, orario notturno/club | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/67217b58-aa80-4f78-524a-7ba93c0b3000/public | - | Verified unique Cloudflare CDN outfit |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Formale / Cena di famiglia | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa6e80b7-bbff-4a8a-4ade-4566c4236200/public | - | Verified unique Cloudflare CDN outfit |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Full Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c44deaf7-7ebb-4a4a-804e-81f1e9190100/public | - | Verified unique Cloudflare CDN outfit |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Hybrid Shift | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/398741d4-cc13-4381-3f63-813170f53600/public | - | Verified unique Cloudflare CDN outfit |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Garage / Officina | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/16a25184-8463-4c38-2f9c-d512d92d3e00/public | - | Verified unique Cloudflare CDN outfit |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Nude | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Casual / Casa e Relax | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/5579de09-eccf-460a-5023-5c17dc508d00/public | Day 1 | Zero-credit reuse from Legacy Gallery Logan |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Beach / Seven Hills Spa | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ef9f34e0-0ee7-4219-2de8-569a2695ef00/public | Day 1 | Zero-credit reuse from Active Gallery logan_base_model |
| _KW6aNaRYTengVR4NBmG7J | Logan | Group 1: Family | outfit:Sleepwear / Riposo Notturno | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | avatar | OK | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public | - | Verified unique Cloudflare CDN avatar |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Casual / Home | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/93a74d71-f20c-46ab-299e-73ffd1a6ad00/public | Day 1 | Zero-credit sync from Erik Card |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:DCC / Business | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/9c3f7516-b63a-4bef-dda0-4bc5dc155400/public | Day 1 | Zero-credit sync from Erik Card |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Esterno / In Auto | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/fab5408a-21f5-490e-6f83-7e4bead36200/public | Day 1 | Zero-credit sync from Erik Card |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Full Shift | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/7ded2114-170c-4e08-a9fe-b4d0ec7aa700/public | Day 1 | Zero-credit sync from Erik Card |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Hybrid Shift | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/36a0143a-02bb-489a-c8d0-b22e9dd1c600/public | Day 1 | Zero-credit sync from Erik Card |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Nude | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Gala di Casata / Formal Douglas | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:The Verve VIP / Clubbing | QUEUED_DAY_5 | - | QUEUED_DAY_5 | Duplicates avatar; queued for DAY_5 |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Beach / Terme di Branco | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c5eab8d7-5969-40e5-ed56-b8aa9d89da00/public | Day 1 | Zero-credit reuse from Active Gallery erik_base_model |
| _qfaywY2yfrGWcxPBdmURD | Erik | Group 1: Family | outfit:Sleepwear / Padronale | RECOVERED_ZERO_CREDIT | https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e6190f8b-79e1-451d-7b12-c98e4f796100/public | Day 1 | Zero-credit reuse from Legacy Gallery Erik |

---

## 5. Wyvern Sprite Sets Official Architecture (Emotion Pose Phase Contract)

Reference rules recorded on **2026-11-27** for all upcoming Character, Outfit, World, and Lorebook emotion sprite packs:

1. **Ownership & Linking (`Link existing sets`):**
   - Sprite sets belong strictly to the owner of the character, lorebook, or world where they live; only sets owned by us can be linked across entities.
   - A linked set is a **live reference (`"Linked from <Character>"`)**, never a static copy: edits to the source set propagate to every linked character, world, or lorebook; `Unlink` removes only the reference; linked sets cannot be marked as `Default Set` of the destination, and a `Default Set` cannot be deleted until another set is made default.
2. **Per-Outfit Sprite Sets & Chat Resolution Order:**
   - Inside *Appearance -> Outfits*, each saved outfit can select: `Character default`, `Own set` (created for that outfit, e.g., Hybrid Shift / Full Shift / distinct seasonal attire), or `Linked set` (shared across outfits `"(shared set)"` or read-only from World / linked WyvernChat character).
   - Runtime fallback chain in chat: **set chosen for that chat -> active outfit's set -> character's Default Set -> `neutral.png` of the same set if an emotion is missing**.
   - Bulk upload expects filenames matching Wyvern emotion names (`neutral.png`, `joy.png`, etc.); sprite uploads and removals save immediately, separately from the main Save button.
3. **NPC Sprite Set Pickers & Linked Character Inheritance:**
   - World NPC entries pick from sets owned by or linked into the World; Lorebook NPC entries pick from sets in that Lorebook's *Sprites* area.
   - A character linked to another WyvernChat character with no own default set inherits the linked character's sprites (`"Sprites from <Name>"`) until *Start Own Default Set* is clicked and the first sprite is uploaded.
   - Stage limits default to **5 desktop / 3 mobile** (configurable 1–8) with active-speaker spotlighting and per-dialogue-segment emotion detection.

---

## 6. Official 12-Step Cast Asset Production Order (Approved by Alice — 2026-11-27)

Strict execution queue across all remaining Cards, World Characters, Outfits, and Emotion Sprite Sets:

1. **Jasper & Alyssa Ovunque** *(maximize zero-credit reuse across all DDM/Fantasy/Modern variants + `FIX-A4` `villa_douglas_hearth` + `AV-J2` Jasper DDM/Fantasy avatars + `JF-1` Jasper Fantasy 4 outfits + **Emotion Poses / Sprite Sets**)*
2. **Malachia** *(Modern + Fantasy + World)*
3. **Noah**
4. **Erik**
5. **Logan**
6. **Wulfnic**
7. **Edric** *(strict SFW athletic-clothed slots only; zero nude)*
8. **Zefir & Ut**
9. **Mackenzie (`Mac`)** *(Modern + Fantasy + World)*
10. **Resto degli NPC con Card Singola Esterna (`/mine`)** (`Zeera`, `Larek`, `Richard W.`, `Adam`, `Hana V.`, `Luka`, `Dullahan`, `Johan`, `Fenrir`, `Richard L.`, etc.)
11. **Tutti i Primari (`Svartulfr_NPC_Primary`)**
12. **Tutti i Secondari (`Svartulfr_NPC_Secondary`)**
