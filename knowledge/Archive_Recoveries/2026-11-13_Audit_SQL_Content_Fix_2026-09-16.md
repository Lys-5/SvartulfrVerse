---
title: "Archive Recovery: Audit_SQL_Content_Fix_2026-09-16.md"
source_file: "ARCHIVIO/03_Claude_Docs_and_Memories/claude_project_docs/Audit_SQL_Content_Fix_2026-09-16.md"
extracted_date: "2026-11-13"
status: "staging_candidate"
total_key_matches: 13
---

# Archive Recovery Report: `Audit_SQL_Content_Fix_2026-09-16.md`

## Provenienza
- **Percorso Archivio:** `ARCHIVIO/03_Claude_Docs_and_Memories/claude_project_docs/Audit_SQL_Content_Fix_2026-09-16.md`
- **Data Scansione:** 2026-11-13

## Entita e Vettori di Lore Rilevati

### Istituzioni & Fazioni
- DCC
- SUCC

### Personaggi Menzionati
- Alyssa
- ERIK
- Jasper
- Logan
- Malachia
- NOAH
- Wulfnic
- Zefir

### Magia, Tecnologia & Artefatti
- Vuoto

### Riferimenti Cronologici & Date
- 2024
- World_Age

## Passaggi Salienti Estratti
> - Tutte le 152 schede lavorate (esclusi Alyssa e Jasper stessi) hanno l'Attitude verso **sia** Alyssa che Jasper Douglas Bloodmoon, come richiesto da §16.
> - **Fix applicato:** 9 entry item/vehicle (le "auto/moto/armi" dei personaggi: Zefir's Blade, Ut's Warhammer, Jasper's Porsche, Noah's Sedan, Logan's Harley, Wulfnic's Rolls-Royce, Erik's SUV, Malachia's Motorcycle, Alyssa's Yellow Beetle) avevano `is_global: true` ma **nessuna keys e constant: fals
> - Confermato che i tag `<Nome_Entry>` che avvolgono ~60 entry (inclusi tutti gli Intimacy Profile) sono un formato strutturale intenzionale e coerente (stesso pattern usato in `<Villa_Douglas>[LOCATION_ID: ...]` e `<Blackwood_City>[LOCATION_ID: ...]`), non residuo di import grezzo: non toccato.
> - "First College Day" aveva la Short Description vuota: aggiunta una riga derivata dal proprio setup già esistente (Villa Douglas, Blackwood City, roster personaggi).

## Valutazione per Promozione a Canone
- Verificare la coerenza con i canoni attuali (Timeline 2024, JED+, assenza di em-dash, Single Source of Truth).
- Se contiene lore originale utile (es. dettagli di infanzia, nomi di professori o accordi di casata), promuovere nel rispettivo Lorebook Standalone o Scheda Personaggio.
