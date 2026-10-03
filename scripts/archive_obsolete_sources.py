import os
import shutil
import json
from datetime import datetime

ROOT = r"d:\SvartulfrVerse"
ARCHIVE_ROOT = os.path.join(ROOT, "ARCHIVIO")

SUBDIRS = {
    "01_Drafts": os.path.join(ARCHIVE_ROOT, "01_Drafts"),
    "02_Drive_and_Raw_Sources": os.path.join(ARCHIVE_ROOT, "02_Drive_and_Raw_Sources"),
    "03_Claude_Docs_and_Memories": os.path.join(ARCHIVE_ROOT, "03_Claude_Docs_and_Memories"),
    "04_Wyvern_Local_Legacy": os.path.join(ARCHIVE_ROOT, "04_Wyvern_Local_Legacy"),
    "05_Snapshots_and_Extractions": os.path.join(ARCHIVE_ROOT, "05_Snapshots_and_Extractions"),
}

def move_safe(src, dst_dir):
    if not os.path.exists(src):
        print(f"  [SKIP] Non trovato: {src}")
        return
    os.makedirs(dst_dir, exist_ok=True)
    basename = os.path.basename(src)
    target = os.path.join(dst_dir, basename)
    if os.path.exists(target):
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)
    shutil.move(src, target)
    print(f"  [ARCHIVIATO] {src} -> {target}")

def generate_live_world_doc():
    export_path = os.path.join(ROOT, "exports", "Svartulfr_Export.json")
    if not os.path.exists(export_path):
        print("  [ERRORE] Svartulfr_Export.json non trovato!")
        return

    with open(export_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    world = data.get("world", {})
    chars = data.get("world_characters", [])
    locs = data.get("world_locations", [])
    envs = data.get("world_environments", [])
    lexs = data.get("world_lexicon_entries", [])
    scens = data.get("world_scenarios", [])
    eras = data.get("world_eras", [])
    maps = data.get("world_maps", [])

    doc_lines = []
    doc_lines.append("# Svartulfr Verse — Documentazione Ufficiale Sincronizzata con World Web API")
    doc_lines.append(f"\n*Generato il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    doc_lines.append(f"*Sorgente Dati: exports/Svartulfr_Export.json (Sincronizzazione Live Wyvern World `_CgYT8fHXpDC4crjmegQF7`)*\n")

    doc_lines.append("## 1. Parametri Generali del World")
    doc_lines.append(f"- **World ID**: `{world.get('id') or world.get('_id')}`")
    doc_lines.append(f"- **Nome World**: {world.get('name')}")
    doc_lines.append(f"- **World Clock**: `{world.get('world_age')}` ore assolute")
    doc_lines.append(f"- **Data Corrente (UTC)**: 28 Agosto 2024, 08:00 UTC (Anno 2024)")
    doc_lines.append(f"- **Epoca di Riferimento (World-Age 0)**: {world.get('human_start_date')} (21 Dicembre 827 UTC)")
    doc_lines.append(f"- **Personaggi Attivi**: {len(chars)}")
    doc_lines.append(f"- **Location Registrate**: {len(locs)}")
    doc_lines.append(f"- **Ambienti Globali**: {len(envs)}")
    doc_lines.append(f"- **Voci Lexicon**: {len(lexs)}")
    doc_lines.append(f"- **Scenari Giocabili**: {len(scens)}")
    doc_lines.append(f"- **Ere Storiche**: {len(eras)}")
    doc_lines.append(f"- **Mappe del Mondo**: {len(maps)}\n")

    doc_lines.append("### Descrizione del Mondo (`description`)")
    doc_lines.append(f"{world.get('description', '')}\n")

    doc_lines.append("### Contesto Globale (`context_description`)")
    doc_lines.append(f"{world.get('context_description', '')}\n")

    doc_lines.append("### Direttive e Istruzioni Finali (`final_instructions`)")
    doc_lines.append(f"{world.get('final_instructions', '')}\n")

    doc_lines.append("---")
    doc_lines.append("## 2. Ere Storiche Configurate (`world_eras`)")
    for era in eras:
        doc_lines.append(f"- **{era.get('name')}** (ID: `{era.get('id') or era.get('_id')}`): Inizio ore `{era.get('start_position')}` - Fine ore `{era.get('end_position')}`")
        if era.get('description'):
            doc_lines.append(f"  *{era.get('description')}*")

    doc_lines.append("\n---")
    doc_lines.append("## 3. Scenari Giocabili Ufficiali (`world_scenarios`)")
    for sc in scens:
        doc_lines.append(f"### {sc.get('name')} (ID: `{sc.get('id') or sc.get('_id')}`)")
        doc_lines.append(f"- **Tagline**: {sc.get('tagline', 'Nessuna')}")
        doc_lines.append(f"- **Posizione Temporale Iniziale**: `{sc.get('start_timeline_position')}` ore")
        doc_lines.append(f"- **Location Iniziale**: `{sc.get('start_location_id', 'Default')}`")
        doc_lines.append(f"- **Primi Messaggi / Alternate Greetings**: {len(sc.get('alternate_greetings', [])) + (1 if sc.get('first_mes') else 0)}")
        if sc.get('catch_hook'):
            doc_lines.append(f"- **Catch Hook**: {sc.get('catch_hook')}")
        doc_lines.append("")

    doc_lines.append("---")
    doc_lines.append("## 4. Catalogo Completo Personaggi (`world_characters`)")
    doc_lines.append(f"Totale schede attive: **{len(chars)}**\n")
    doc_lines.append("| Nome Personaggio | Specie | Età | Genere / Ruolo | ID Wyvern |")
    doc_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for c in sorted(chars, key=lambda x: x.get('display_name') or x.get('name') or ''):
        name = c.get('display_name') or c.get('name')
        cid = c.get('id') or c.get('_id')
        summary = c.get('summary', '')
        rpg = c.get('rpg_stats') or {}
        species = rpg.get('species_id') or 'N/D'
        level = rpg.get('level', 'N/D')
        
        # Try parse bracket PList
        sp = species
        age_str = str(level)
        if '[' in summary and ']' in summary:
            parts = summary.replace('[', '').replace(']', '').split(';')
            for p in parts:
                if 'SPECIES:' in p.upper():
                    sp = p.split(':', 1)[1].strip()
                if 'AGE:' in p.upper():
                    age_str = p.split(':', 1)[1].strip()
        doc_lines.append(f"| **{name}** | {sp} | {age_str} | Level {level} | `{cid}` |")

    doc_lines.append("\n---")
    doc_lines.append("## 5. Catalogo Completo Location (`world_locations`)")
    doc_lines.append(f"Totale location registrate: **{len(locs)}**\n")
    for loc in sorted(locs, key=lambda x: x.get('name') or ''):
        lid = loc.get('id') or loc.get('_id')
        lname = loc.get('name')
        ldesc = loc.get('context_description') or loc.get('description') or ''
        doc_lines.append(f"### {lname} (`{lid}`)")
        doc_lines.append(f"{ldesc}\n")

    doc_lines.append("---")
    doc_lines.append("## 6. Struttura del Lexicon (`world_lexicon_entries`)")
    doc_lines.append(f"Totale voci di Lexicon: **{len(lexs)}**\n")
    
    # Categorizzazione
    categories = {}
    for lx in lexs:
        t = lx.get('type') or 'uncategorized'
        categories.setdefault(t, []).append(lx)

    for cat_name, entries in sorted(categories.items()):
        doc_lines.append(f"### Tipologia: `{cat_name}` ({len(entries)} voci)")
        for entry in sorted(entries, key=lambda x: x.get('name') or ''):
            eid = entry.get('id') or entry.get('_id')
            ename = entry.get('name') or entry.get('title')
            is_glob = "Globale" if entry.get('is_global') else "Locale / Memory"
            keys = ", ".join(entry.get('keys', [])[:4])
            doc_lines.append(f"- **{ename}** (`{eid}`) [{is_glob}] — *Keys: {keys}*")
        doc_lines.append("")

    out_file = os.path.join(ROOT, "docs", "Svartulfr_World_Doc.md")
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(doc_lines))
    print(f"  [OK] Documentazione sincronizzata generata: {out_file} ({len(doc_lines)} righe)")

def main():
    print("==================================================================")
    print("      OPERAZIONE ARCHIVIAZIONE FONTI OBSOLETE & SYNC DOCUMENTI     ")
    print("==================================================================")

    # 1. Spostamento 01_Drafts
    print("\n--- 1. ARCHIVIAZIONE DRAFTS OBSOLETI ---")
    drafts_src = os.path.join(ROOT, "Drafts")
    if os.path.exists(drafts_src):
        for item in os.listdir(drafts_src):
            move_safe(os.path.join(drafts_src, item), SUBDIRS["01_Drafts"])
        try:
            os.rmdir(drafts_src)
            print(f"  [PULIZIA] Cartella vuota rimossa: {drafts_src}")
        except Exception:
            pass

    # 2. Spostamento 02_Drive_and_Raw_Sources
    print("\n--- 2. ARCHIVIAZIONE DRIVE & SORGENTI GREZZE ---")
    drive_src = os.path.join(ROOT, "drive")
    if os.path.exists(drive_src):
        for item in os.listdir(drive_src):
            move_safe(os.path.join(drive_src, item), SUBDIRS["02_Drive_and_Raw_Sources"])
        try:
            os.rmdir(drive_src)
            print(f"  [PULIZIA] Cartella vuota rimossa: {drive_src}")
        except Exception:
            pass

    # 3. Spostamento 03_Claude_Docs_and_Memories
    print("\n--- 3. ARCHIVIAZIONE DOCUMENTAZIONE STORICA CLAUDE & VECCHI DOCS ---")
    docs_dir = os.path.join(ROOT, "docs")
    for item in ["claude_conversations", "claude_memories", "claude_project_docs", "legacy"]:
        src_path = os.path.join(docs_dir, item)
        if os.path.exists(src_path):
            move_safe(src_path, SUBDIRS["03_Claude_Docs_and_Memories"])
    
    # Vecchio Svartulfr_World_Doc.md (pre-sync)
    old_world_doc = os.path.join(docs_dir, "Svartulfr_World_Doc.md")
    if os.path.exists(old_world_doc):
        # Sposta e rinomina come pre_sync
        target_pre = os.path.join(SUBDIRS["03_Claude_Docs_and_Memories"], "Svartulfr_World_Doc_pre_sync.md")
        os.makedirs(SUBDIRS["03_Claude_Docs_and_Memories"], exist_ok=True)
        if os.path.exists(target_pre):
            os.remove(target_pre)
        shutil.move(old_world_doc, target_pre)
        print(f"  [ARCHIVIATO] Vecchio Svartulfr_World_Doc.md -> {target_pre}")

    # 4. Spostamento 04_Wyvern_Local_Legacy
    print("\n--- 4. ARCHIVIAZIONE WYVERN LOCAL LEGACY (SCHEDE E MARKDOWN DI AGOSTO) ---")
    wyvern_src = os.path.join(ROOT, "Wyvern")
    if os.path.exists(wyvern_src):
        for item in os.listdir(wyvern_src):
            move_safe(os.path.join(wyvern_src, item), SUBDIRS["04_Wyvern_Local_Legacy"])
        try:
            os.rmdir(wyvern_src)
            print(f"  [PULIZIA] Cartella vuota rimossa: {wyvern_src}")
        except Exception:
            pass

    # 5. Spostamento 05_Snapshots_and_Extractions
    print("\n--- 5. ARCHIVIAZIONE VECCHI SNAPSHOTS & DUMP INTERMEDI ---")
    # File in root
    snap_root = os.path.join(ROOT, "scenarios_pre_academic_rework_snapshot.json")
    if os.path.exists(snap_root):
        move_safe(snap_root, SUBDIRS["05_Snapshots_and_Extractions"])

    # File e cartelle in exports/ tranne Svartulfr_Export.json
    exports_dir = os.path.join(ROOT, "exports")
    if os.path.exists(exports_dir):
        for item in os.listdir(exports_dir):
            if item == "Svartulfr_Export.json":
                continue # PRESERVA IL MASTER EXPORT LIVE!
            src_path = os.path.join(exports_dir, item)
            move_safe(src_path, SUBDIRS["05_Snapshots_and_Extractions"])

    # 6. Generazione Documentazione Sincronizzata Attiva
    print("\n--- 6. GENERAZIONE DOCUMENTAZIONE SINCRONIZZATA DAL MASTER EXPORT LIVE ---")
    generate_live_world_doc()

    print("\n==================================================================")
    print("                    OPERAZIONE COMPLETATA CON SUCCESSO!           ")
    print("==================================================================")

if __name__ == "__main__":
    main()
