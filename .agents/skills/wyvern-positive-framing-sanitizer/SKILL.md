---
name: wyvern-positive-framing-sanitizer
description: >-
  Pipeline per la bonifica da negative constraint echoing ("Pink Elephant Problem")
  nei contesti di roleplay LLM (Character Cards, Outfits, Scenari, Lorebook)
  mediante Positive Framing puro, iniezione di vincoli di stile in post_history_instructions
  e sincronizzazione sicura via Wyvern Web API.
---

# Wyvern Positive Framing & Anti-Echoing Sanitizer

Questa skill codifica e standardizza la pipeline metodologica e tecnica per eliminare l'echoing narrativo dei vincoli negativi (il cosiddetto *"Pink Elephant Problem"*) nelle Character Card, negli Outfits, nei Lorebook e negli Scenari di Wyvern, assicurando una narrazione organica e un deployment privo di regressioni via Web API.

---

## 1. Analisi del Fenomeno: Il "Pink Elephant Problem" negli LLM

### 1.1 Perché le Negazioni nel Contesto Falliscono
I Large Language Models operano probabilisticamente sulla base dell'attivazione dei token all'interno della matrice di attenzione (self-attention mechanism), non tramite inferenza logica o esclusione simbolica booleana.
Quando un autore o un compilatore inserisce clausole negative all'interno dei campi di contesto letti dal bot durante la chat:
- `"No orecchie umane"`
- `"(nessun orecchio umano visibile)"`
- `"senza orecchie umane ai lati"`
- `"prive di qualsiasi orecchio umano ai lati del volto"`

I token semantici `orecchio`, `umano`, `prive`, `senza`, `volto` rimangono costantemente ad alta probabilità nel contesto operativo. Durante i turni di narrazione o roleplay, il modello tenta di riflettere e giustificare questi concetti estratti, trasformandoli in frasi narrative ridondanti e innaturali ripetute all'infinito.

### 1.2 La Regola della Separazione Funzionale
- **Contesto Narrativo LLM (Schede JED+, Outfits, Scenari, Lorebook):** Deve contenere **esclusivamente descrizioni positive pure** (ciò che è fisicamente presente e come interagisce). Mai inserire negazioni anatomiche.
- **Parametri Image Generation (Argon / Gemini Imagen / Midjourney):** Le clausole negative (`--no human ears`, `No orecchie umane`) appartengono **esclusivamente** ai prompt tecnici e ai parametri negativi del generatore visivo.

---

## 2. Architettura della Soluzione: Replacement Framing

### 2.1 Tabella di Trasformazione (Negative $\to$ Positive Framing)

| Negazione da Eliminare ❌ | Formula Positiva Sostitutiva ✅ | Ambito di Applicazione |
| :--- | :--- | :--- |
| `No orecchie umane` / `(nessun orecchio umano visibile)` | `Orecchie lupine singole [colore], erette e mobili sulla sommità del capo, perfettamente integrate tra i capelli.` | Acconciatura / Outfits |
| `senza orecchie umane ai lati` / `senza alcuna orecchia umana ai lati della testa` | `Il suo unico paio di orecchie da lupo [colore] sulla sommità del capo si piega / si drizza all'erta.` | Greeting / Premade Scenes Scenari |
| `(nessun orecchio umano laterale)` | `Singolo paio di orecchie da lupo mobili e soffici situate sulla sommità del capo.` | User Persona / Schede JED+ |
| `tempie umane` | `tempie` (o `zona temporale coperta dai capelli`) | Acconciature e Outfits |

### 2.2 Vincolo di Stile di Sistema (`post_history_instructions`)
Per blindare a livello di architettura di generazione che l'LLM non introduca autonomamente spiegazioni anatomiche non richieste, ogni scheda e prompt di sistema deve includere in coda:

```text
Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Demi-human anatomical discipline: treat single animal ears as the natural norm; never mention, describe, or reiterate the absence or lack of human ears in narrative descriptions.
```

---

## 3. Protocolli di Deployment su Wyvern Web API

### 3.1 Aggiornamento Character Cards Standalone (`/api/characters/{id}`)
> [!CAUTION] **Trappola del Payload Annidato:** Inviare `{'character': { ... }}` all'endpoint `PUT /api/characters/{id}` causa il fallimento silenzioso dell'aggiornamento per `outfits` e `post_history_instructions`.

Il payload deve essere rigorosamente **flat a livello root**:

```python
payload = {
    'description': local_card.get('description', ''),
    'outfits': local_card.get('outfits', []),
    'post_history_instructions': local_card.get('post_history_instructions', ''),
    'final_instructions': local_card.get('post_history_instructions', ''),
    'visibility': 'private',
    'rating': 'explicit'
}
resp = requests.put(f"https://app.wyvern.chat/api/characters/{char_id}", headers=headers, json=payload)
assert resp.status_code == 200
```

### 3.2 Aggiornamento Scenari del World (`/api/worlds/scenarios/{id}`)
> [!WARNING] **Trappola del MongoDB Cast Error:** Quando si effettua un `GET` su uno scenario di World, il campo `world` viene restituito come oggetto popolato (`{'_id': '...', 'name': '...'}`). Se reinviato tale e quale in un `PUT`, il backend risponde con `HTTP 500: Argument passed in must be a string of 12 bytes or a string of 24 hex characters or an integer`.

**Procedura di Bonifica del Payload Scenario:**
1. Sostituire `cleaned['world'] = WORLD_ID` (stringa ID, es. `_YpX47fNraQFw2dD7TdycJ`).
2. Sostituire `cleaned['world_id'] = WORLD_ID`.
3. Se presenti oggetti per `location` o `environment`, estrarre solo `location_id` / `environment_id` e rimuovere gli oggetti.
4. Rimuovere i campi read-only del DB: `_id`, `id`, `created_at`, `updated_at`, `approval_date`, `rejection_date`, `entity_statistics`, `resolved_characters`.

---

## 4. Checklist di Validazione End-to-End

Prima di considerare conclusa qualsiasi bonifica di positive framing:

1. **Scansione Regex Locale Rigorosa:**
   ```bash
   python -c "import re, glob; pattern = re.compile(r'\b(no orecchie umane|nessun orecchio umano|senza (?:alcuna )?orecchi[ae] uman[ae]|prive di (?:qualsiasi )?orecchi[ae] uman[ae])\b', re.I); [print(p) for p in glob.glob('FINAL/**/*.json', recursive=True) if pattern.search(open(p, encoding='utf-8').read())]"
   ```
   *Esito atteso:* Zero righe restituite.

2. **Verifica Live API Wyvern:**
   Interrogare `GET /api/characters/{id}` e `GET /api/worlds/scenarios/world/{world_id}` verificando che il conteggio delle occorrenze sia 0 e che `Demi-human anatomical discipline` sia presente.

3. **Ispezione Headless Chrome DevTools / Playwright:**
   - Navigazione a `https://app.wyvern.chat/characters/mine` con sessione copiata.
   - Verifica di 0 errori in Console e 0 risposte di errore di rete (4xx/5xx).
   - Verifica di assenza delle frasi negative nel DOM (`document.body.innerText`).
