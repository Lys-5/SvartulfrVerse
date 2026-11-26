## 2026-10-31T06:32:17Z

Allineamento delle altezze canoniche nelle schede, nei prompt visivi e nelle descrizioni di gruppo dell'universo Svartúlfr, progettazione e generazione delle reference visive dei marchi runici e divini del branco, e ottimizzazione non distruttiva del micro-proxy locale per la sanitizzazione e compattazione dei payload di contesto inviati ai modelli LLM per l'integrazione stabile in produzione nel repository.

Integrity mode: development

## Requirements

### R1. Allineamento altezze canoniche e riferimenti proporzionali
Allineare le altezze nei file locali del repository (Character Card in `FINAL/`, Personas, Lorebooks/NPC e prompt visivi/descrizioni di gruppo) ai valori canonici accertati:
- Alyssa: 155 cm (5' 1")
- Jasper: 193 cm (6' 4")
- Noah: 197 cm (6' 5.6")
- Malachia: 208 cm (6' 9.9")
- Erik: 213 cm (6' 11.9")
- Wulfnic: 220 cm (7' 2.6")

Includere esplicitamente nelle descrizioni di gruppo e nei prompt visivi le seguenti reference proporzionali dirette:
- Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).
- Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.
- Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno).

Preservare rigorosamente la parità byte-for-byte (`entries == lexicon`) nei Lorebook, la formattazione JED+ e la coerenza delle schede.

### R2. Generazione e progettazione reference visive marchi runici e divini
Progettare e generare le immagini di reference e i prompt per i marchi runici e divini del branco, salvando i file immagine generati e le specifiche documentali in una cartella dedicata del repository (es. `assets/references/` o `docs/references/`):
- Tatuaggio Gebo al polso sinistro dei gemelli (inchiostro di ferro freddo)
- Marchio runico di Máni (mezzaluna argentata con glifi lunari sub-dermici) unicamente sull'anca sinistra di Alyssa (Hvít Mániúlfr)
- Marchio runico di Sól (sole nero radioso con glifi fiammeggianti sub-dermici) unicamente sull'anca destra di Jasper (Svartr Sólúlfr)
- Marchi e tatuaggi degli altri membri del branco come Logan, Malachia, Erik, Wulfnic)

### R3. Ottimizzazione non distruttiva del micro-proxy
Ottimizzare `proxy/free_tier_proxy.py` e `proxy/config_free_proxy.json` per intercettare, sanitizzare e compattare i payload di sistema e i dati di lexicon/lorebook inviati ai modelli LLM, riducendo l'overhead di token e ottimizzando il flusso verso il provider. L'ottimizzazione deve essere non distruttiva, preservando l'integrità dei contenuti semantici (eliminazione di spaziature e newline ridondanti, deduplicazione entry e pulizia di campi o commenti non necessari). L'ambiente di esecuzione locale è standard su `127.0.0.1`.

## Acceptance Criteria

### Allineamento altezze canoniche e proporzioni
- [ ] Tutte le occorrenze delle altezze dei sei personaggi nei file target locali in `FINAL/` (Character Card, Personas, Lorebook NPC) e nei prompt/descrizioni visive corrispondono esattamente ai valori canonici accertati in cm e piedi/pollici.
- [ ] Le descrizioni di gruppo e i prompt visivi contengono le reference proporzionali dirette specificate (Alyssa alla spalla di Jasper; Malachia che supera Alyssa di oltre 50 cm con la testa di lei a metà torace; Erik e Wulfnic che sovrastano Alyssa di 58-65 cm con altezza al basso petto/sterno).
- [ ] Uno script di verifica programmatico convalida la correttezza di tutte le altezze aggiornate e conferma la parità `entries == lexicon` nei file Lorebook modificati senza errori.

### Reference visive marchi runici e divini
- [ ] I file immagine generati per ciascun marchio (Gebo polso sx, Máni anca sx Alyssa, Sól anca dx Jasper, e marchi di Logan, Malachia, Erik, Wulfnic) sono presenti nel repository nel percorso designato.
- [ ] È presente un documento di specifica contenente i prompt visivi completi, il posizionamento anatomico e le descrizioni estetiche canoniche di ciascun marchio.

### Ottimizzazione micro-proxy
- [ ] `proxy/free_tier_proxy.py` e `proxy/config_free_proxy.json` implementano la logica di compattazione e sanitizzazione non distruttiva dei payload JSON.
- [ ] Una suite di test automatizzata verifica che il micro-proxy si avvii su `127.0.0.1`, esegua la compattazione riducendo il conteggio token/lunghezza dei payload di test rispetto all'input grezzo, e preservi inalterato il contenuto informativo essenziale.
