# Archivio Storico: Voci Disattivate Purificate dai Lorebook (223 Voci)

> **Data Operazione**: 18 Ottobre 2026  
> **Oggetto**: Purga e alleggerimento strutturale dei 6 Lorebook Standalone Svartúlfr su Wyvern.  
> **File Manifest Completo**: [`purged_disabled_entries_manifest.json`](./purged_disabled_entries_manifest.json)

---

## 1. Motivazione Architetturale

Nell'ambito dell'ottimizzazione del context budget e della pulizia sistematica del database Wyvern, tutte le voci impostate con `enabled: false` (disattivate) all'interno dei file Lorebook sono state rimosse dai file operativi (`FINAL/` e `lorebooks/optimized/`) e sincronizzate sui corrispettivi remoti via Wyvern Web API.

Questo intervento ha rimosso **223 voci disattivate**, liberando **oltre 360.000 caratteri** di payload inutile e velocizzando significativamente i tempi di scansione dei trigger durante le sessioni di roleplay.

---

## 2. Dettaglio Quantitativo per Lorebook

| Lorebook | ID Wyvern | Voci Iniziali | Voci Mantenute (Attive) | Voci Purigate (OFF) | Note |
|---|---|---|---|---|---|
| **Svartúlfr - Location** | `_EjXxkmPVhpCXg8xABpFkK` | 196 | **188** | 8 | Purificate location dismesse (The Hothouse, Seedpod, Narcissus, Taproot, Digitalis, The Ovary, Nectary, Graft). |
| **Svartúlfr - Lorebook I** | `_gwwCxCfQ6PQaLEjAQVpJL` | 219 | **219** | 0 | 100% delle voci erano già attive. |
| **Svartúlfr - Lorebook II** | `_HfG7TeV6MJyj6bxMwxkpt` | 143 | **139** | 4 | Purificate voci off-world disattivate (Jun's Coping Mechanism, Hemlock Biosciences, Cameras, Rules). |
| **Svartúlfr - Lorebook III** | `_9zWTGqYJNJ4BCDMj8gfcD` | 35 | **35** | 0 | 100% delle voci erano già attive. |
| **Svartúlfr - NPC Primary** | `_zwEqgEEzh12X6gHVmMKKC` | 107 | **100** | 7 | Purificate figure disattivate (Mei, Bao, The Gardener, Wen Guo, Dr Negin Tabasi, Rene Legaspi, Aikawa Keisuke). |
| **Svartúlfr - NPC Secondary** | `_Uht3Ckz44JBDrPnUHq7LV` | 315 | **111** | 204 | Bonifica massiva di 204 comparse disattivate da vecchi dump, preservando tutti i 111 personaggi attivi. |
| **TOTALE** | — | **1.015** | **792** | **223** | **-360.548 caratteri di context bloat eliminati** |

---

## 3. Garanzia di Reversibilità

Tutte le 223 voci purgate, con i loro oggetti JSON integrali (`entry_id`, `keys`, `content`, `avatar`, `type`, ecc.), sono conservate fedelmente nel file [`purged_disabled_entries_manifest.json`](./purged_disabled_entries_manifest.json) per qualsiasi eventuale ripristino o consultazione futura.
