# Monitoraggio Test Massimo Chat — To-Do Attività di Domani (12/11/2026)

**Data Inizio Monitoraggio:** 11/11/2026, 21:18 CET  
**Sessione di Chat Target:** `chat_log_Tc4xL33mLdVCgr8fQJnkr` — *"Cylinders, Cookies, and a Feral Garden"* (241+ messaggi)  
**URL:** [https://app.wyvern.chat/sim/chat_log_Tc4xL33mLdVCgr8fQJnkr](https://app.wyvern.chat/sim/chat_log_Tc4xL33mLdVCgr8fQJnkr)  
**Party Attivo:** Lucan Rowland, Yuzuha Rowland, Mizuki Rowland, Dorian Rowland, Malachia, Jasper  
**Location:** Gola della Pietra del Falco, Camera Centrale (`_AqmQ2BTzeTYYdxpyrHe9G`)

---

## 1. Stato Integrazioni Eseguite Stasera (11/11/2026)

Tutte le componenti della pipeline narrativa e meccanica sono state aggiornate con la **tabella di conversione rigida anti-allucinazione (Stat 8–34+)** e la regola di pareggio ($\text{Totale} \ge \text{CD}$ è sempre un SUCCESSO pieno):

1. **Custom Prompt Assembly (`pha_kWkWUAfTJTF9q72c2bC98`)**:
   - Blocco `svartulfr_ttrpg_resolution` aggiornato con tabella completa fino a Stat 34+ (es. Jasper INT 32 = Mod +11).
   - Inserito promemoria matematico nel `floating_prompt_template` a Depth 4% per prevenire drift nei turni lunghi.
   - Sincronizzato con successo su Wyvern API (HTTP 200).
2. **World Svartúlfr (`_YpX47fNraQFw2dD7TdycJ`)**:
   - `system_prompt_override` aggiornato con il blocco `<ttrpg_mechanics>` esteso.
   - `final_instructions` aggiornato con la direttiva di accuratezza matematica.
   - Sincronizzato con successo su Wyvern API via PUT (HTTP 200).
3. **Game Master Assistant (`simple_assistant_EYQTtcgTQfwh2RH9RG8z3`)**:
   - Sincronizzato su Wyvern API con formula e tabella in `system_prompt` e `final_instructions` (HTTP 201/200).
4. **Micro-Proxy Locale (`proxy/free_tier_proxy.py`)**:
   - Implementata la fase automatica `enforce_ttrpg_math_guardrails` in `compact_request_payload`: inietta in modo trasparente la tabella di conversione ogni volta che nel payload compaiono `[STATS: ...]`, `TEST:` o `D20`.
   - Attivo e operativo su `http://0.0.0.0:5005`.

---

## 2. To-Do e Punti di Audit del 12/11/2026 — [COMPLETATI AL 100%]

- [x] **Audit Forense dei Tiri D20 nella Chat `chat_log_Tc4xL33mLdVCgr8fQJnkr`**:
  - **Esito:** Ispezionati tutti i 259 messaggi della sessione (fino al Day 3, 22:40). Rilevati 9 tiri formali in formato `> [TEST: ...]`.
  - **Accuratezza Aritmetica:** **100% esatta** ($14+5=19$, $17+4=21$, $15+11=26$, $7+9=16$, $16+7=23$, $13+6=19$, $14+8=22$, $16+8=24$, $12+7=19$).
  - **Aderenza alle Schede:** Jasper INT 32 ha ereditato `Mod: +11` (Msg #234); Alyssa INT ha ereditato `Mod: +7` (Msg #236); Yael PER ha ereditato `Mod: +8` (Msg #252, #254); Karshin PER ha ereditato `Mod: +7` (Msg #256).
  - **Regola Pareggi:** Confermata aderenza rigorosa: tutti i totali $\ge \text{CD}$ sono stati giudicati `SUCCESSO`. Nessun pareggio declassato.
- [x] **Ottimizzazione Failover e Upstream Direct Zhipu AI**:
  - **Esito:** Bonificata la lista modelli di `p1-glm-cloud` in `proxy/config_free_proxy.json` rimuovendo `z-ai/glm-5.3` e `~z-ai/glm-latest` a pagamento che generavano errori 402 su OpenRouter a credito zero. Verificata la piena disponibilità di `z-ai/glm-5.3-flash` su tutte le 3 chiavi di OpenRouter (HTTP 200).
  - Verificato l'endpoint Zhipu AI BigModel direct (`open.bigmodel.cn`): la chiave proprietaria restituisce codice 1113 (necessita pacchetto risorse per endpoint diretto), pertanto il routing prioritario converge sul Free Tier certificato di `z-ai/glm-5.3-flash` (zero 402, zero latenza).
- [x] **Standardizzazione Arrotondamento Statistiche Dispari (Floor vs Round)**:
  - **Esito:** Standardizzato ufficialmente il **Floor canonico D20** ($\lfloor(\text{Stat}-10)/2\rfloor$). Per statistiche dispari come PER 27 ($(27-10)/2 = 8.5$), il modificatore è tassativamente per difetto **`Mod: +8`** (vietato arrotondare a +9).
  - **Hardening Implementato:** Aggiornata la tabella sia in `proxy/free_tier_proxy.py` (fase `enforce_ttrpg_math_guardrails`) sia nel Custom Prompt Assembly `FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json`, sincronizzato live su Wyvern API (`pha_kWkWUAfTJTF9q72c2bC98`, HTTP 200).
- [x] **Verifica Disciplina di Formattazione & Zero Em-Dash**:
  - **Esito:** Scansione testuale su tutti i 259 messaggi: dall'indice 170 all'indice 258 (ultimi 89 turni consecutivi post-fix) **sono presenti ZERO em-dash (`—`)**, a fronte di 22 messaggi storici precedenti al fix. Dialoghi conformi al 100% con virgolette doppie standard (`"..."`). Zero allucinazioni anatomiche su orecchie/specie e zero reset temporali (Day 1 $\to$ Day 3, 22:40).
