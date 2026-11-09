#!/usr/bin/env python3
"""
scripts/archive_mining_engine.py

Archive Lore Mining Engine for Svartulfr Verse.
Scans priority directories in ARCHIVIO/ (03_Claude_Docs_and_Memories -> 02_Drive_and_Raw_Sources -> 01_Drafts -> cards_legacy),
extracts lost lore, historical facts, relationship nuances, and saves structured staging notes in knowledge/Archive_Recoveries/.
"""

import os
import sys
import json
import re
import datetime
import pathlib
import argparse

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARCHIVIO = ROOT / 'ARCHIVIO'
SCRATCH = ROOT / 'scratch'
RECOVERIES_DIR = ROOT / 'knowledge' / 'Archive_Recoveries'
STATE_FILE = SCRATCH / 'archive_mining_state.json'
LOG_FILE = SCRATCH / 'archive_mining.log'

PRIORITY_DIRS = [
    ('03_Claude_Docs_and_Memories', 1),
    ('02_Drive_and_Raw_Sources', 2),
    ('01_Drafts', 3),
    ('cards_legacy', 4),
    ('janitor_sources', 5),
    ('04_Wyvern_Local_Legacy', 6)
]

# Canonical Entities / Keywords for Lore Extraction
KEYWORD_PATTERNS = {
    'institutions': [r'\bSt\.?\s*Brugge\b', r'\bSUCC\b', r'\bCUMS\b', r'\bDCC\b', r'\bDMHA\b', r'\bTheta Iota Theta\b', r'\bTIT\b', r'\bKSA\b', r'\bGilda\b', r'\bGuild\b'],
    'characters': [
        r'\bAlyssa\b', r'\bJasper\b', r'\bNoah\b', r'\bMalachia\b', r'\bErik\b', r'\bLogan\b', r'\bZeera\b',
        r'\bWulfnic\b', r'\bEdric\b', r'\bJared\b', r'\bSantiago\b', r'\bBailey\b', r'\bArcher\b', r'\bNarghaton\b',
        r'\bSierra\b', r'\bScarlett\b', r'\bZefir\b', r'\bRevazhael\b', r'\bMarcus\b', r'\bRoxy\b'
    ],
    'magic_and_tech': [
        r'\bcilindr[io]\b', r'\bcristall\w*\b', r'\bmatrice\b', r'\babissal\w*\b', r'\bvuoto\b', r'\bnecromanz\w*\b',
        r'\brunic\w*\b', r'\bdungeon\b', r'\bhunter\b', r'\bgebo\b', r'\bmani\b', r'\bsol\b', r'\bshift\b'
    ],
    'timeline_and_dates': [
        r'\b\d{3,4}\s*(?:CE|d\.C\.|BC|a\.C\.)\b', r'\bworld[-_]age\b', r'\b827\b', r'\b2024\b', r'\b2022\b'
    ]
}

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{ts}] {msg}"
    print(formatted)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(formatted + "\n")

def init_queue():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                state = json.load(f)
                if state.get('files'):
                    return state
        except Exception as e:
            log(f"Warning: Could not read existing state file, rebuilding: {e}")

    files_list = []
    for dir_name, prio in PRIORITY_DIRS:
        target_dir = ARCHIVIO / dir_name
        if not target_dir.exists():
            continue
        for root, _, files in os.walk(target_dir):
            for file in sorted(files):
                # Filter out binary or uninformative/system files
                if file.startswith('.') or file.lower().endswith(('.ini', '.png', '.jpg', '.jpeg', '.webp', '.avif', '.gif', '.zip', '.tar', '.gz')):
                    continue
                file_path = pathlib.Path(root) / file
                rel_path = file_path.relative_to(ARCHIVIO).as_posix()
                files_list.append({
                    "relative_path": rel_path,
                    "priority": prio,
                    "size_bytes": file_path.stat().st_size,
                    "status": "pending",
                    "processed_at": None,
                    "discoveries_count": 0,
                    "staging_file": None
                })

    state = {
        "created_at": datetime.datetime.now().isoformat(),
        "last_run": None,
        "total_files": len(files_list),
        "processed_files_count": 0,
        "files": files_list
    }
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    log(f"Initialized archive mining queue with {len(files_list)} files across {len(PRIORITY_DIRS)} priority tiers.")
    return state

def save_state(state):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def analyze_file_content(file_path):
    try:
        if file_path.suffix.lower() == '.json':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                data = json.load(f)
            raw_text = json.dumps(data, ensure_ascii=False, indent=1)
        else:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                raw_text = f.read()
    except Exception as e:
        return None, f"Read error: {e}"

    discoveries = {
        'institutions': set(),
        'characters': set(),
        'magic_and_tech': set(),
        'timeline_and_dates': set(),
        'highlight_passages': []
    }

    for category, patterns in KEYWORD_PATTERNS.items():
        for pat in patterns:
            matches = re.findall(pat, raw_text, re.IGNORECASE)
            if matches:
                for m in matches:
                    discoveries[category].add(m.strip().title() if len(m) > 4 else m.strip().upper())

    # Find compelling dialogue or narrative paragraphs
    lines = raw_text.splitlines()
    for line in lines:
        stripped = line.strip()
        if len(stripped) > 60 and any(k in stripped.lower() for k in ['douglas', 'svartulfr', 'abiss', 'cristal', 'revazhael', 'dungeon', 'hunter', 'logan', 'alyssa', 'jasper']):
            # Clean em-dashes
            sanitized = stripped.replace('—', ', ').replace('–', ', ')
            if len(discoveries['highlight_passages']) < 5 and sanitized not in discoveries['highlight_passages']:
                discoveries['highlight_passages'].append(sanitized[:300])

    # Convert sets to sorted lists
    for k in discoveries:
        if isinstance(discoveries[k], set):
            discoveries[k] = sorted(list(discoveries[k]))

    return discoveries, raw_text

def write_staging_note(rel_path, discoveries, sample_text):
    RECOVERIES_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r'[^a-zA-Z0-9_\-]+', '_', pathlib.Path(rel_path).stem)[:50]
    note_filename = f"{today}_{slug}.md"
    note_path = RECOVERIES_DIR / note_filename

    total_hits = sum(len(discoveries[k]) for k in ['institutions', 'characters', 'magic_and_tech', 'timeline_and_dates'])

    content = f"""---
title: "Archive Recovery: {pathlib.Path(rel_path).name}"
source_file: "ARCHIVIO/{rel_path}"
extracted_date: "{today}"
status: "staging_candidate"
total_key_matches: {total_hits}
---

# Archive Recovery Report: `{pathlib.Path(rel_path).name}`

## Provenienza
- **Percorso Archivio:** `ARCHIVIO/{rel_path}`
- **Data Scansione:** {today}

## Entita e Vettori di Lore Rilevati

### Istituzioni & Fazioni
{chr(10).join(f"- {item}" for item in discoveries['institutions']) if discoveries['institutions'] else "- Nessuna istituzione esplicita rilevata."}

### Personaggi Menzionati
{chr(10).join(f"- {item}" for item in discoveries['characters']) if discoveries['characters'] else "- Nessun personaggio principale rilevato."}

### Magia, Tecnologia & Artefatti
{chr(10).join(f"- {item}" for item in discoveries['magic_and_tech']) if discoveries['magic_and_tech'] else "- Nessun tratto magico peculiare rilevato."}

### Riferimenti Cronologici & Date
{chr(10).join(f"- {item}" for item in discoveries['timeline_and_dates']) if discoveries['timeline_and_dates'] else "- Nessun riferimento temporale rilevato."}

## Passaggi Salienti Estratti
{chr(10).join(f"> {p}" for p in discoveries['highlight_passages']) if discoveries['highlight_passages'] else "*Nessun passaggio saliente isolato.*"}

## Valutazione per Promozione a Canone
- Verificare la coerenza con i canoni attuali (Timeline 2024, JED+, assenza di em-dash, Single Source of Truth).
- Se contiene lore originale utile (es. dettagli di infanzia, nomi di professori o accordi di casata), promuovere nel rispettivo Lorebook Standalone o Scheda Personaggio.
"""
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return note_path

def run_archive_mining_batch(batch_size=2, dry_run=False):
    state = init_queue()
    pending = [f for f in state['files'] if f['status'] == 'pending']
    
    if not pending:
        log("Tutti i file dell'archivio sono stati processati! Resetto la coda per un nuovo ciclo di audit.")
        for f in state['files']:
            f['status'] = 'pending'
        pending = state['files']

    batch = pending[:batch_size]
    log(f"Avvio mining archivio: batch di {len(batch)} file su {len(pending)} in attesa.")

    if dry_run:
        print(f"[DRY-RUN] File selezionati per il batch: {[b['relative_path'] for b in batch]}")
        return {"batch": batch, "dry_run": True}

    processed_results = []
    for item in batch:
        rel_p = item['relative_path']
        full_path = ARCHIVIO / rel_p
        log(f"--- Elaborazione file: {rel_p} (Priorita {item['priority']}) ---")
        
        discoveries, raw_text = analyze_file_content(full_path)
        if discoveries is None:
            log(f"  [Errore] Impossibile analizzare {rel_p}: {raw_text}")
            item['status'] = 'error'
            item['error'] = raw_text
            continue

        hits = sum(len(discoveries[k]) for k in ['institutions', 'characters', 'magic_and_tech', 'timeline_and_dates'])
        note_path = write_staging_note(rel_p, discoveries, raw_text)
        
        item['status'] = 'processed'
        item['processed_at'] = datetime.datetime.now().isoformat()
        item['discoveries_count'] = hits
        item['staging_file'] = note_path.relative_to(ROOT).as_posix()
        state['processed_files_count'] += 1
        
        log(f"  -> Generata nota di staging: {item['staging_file']} ({hits} entita identificate)")
        processed_results.append(item)

    state['last_run'] = datetime.datetime.now().isoformat()
    save_state(state)
    log(f"Batch completato. Progresso totale: {state['processed_files_count']}/{state['total_files']} file elaborati.")
    return {
        "status": "success",
        "processed_count": len(processed_results),
        "total_processed": state['processed_files_count'],
        "total_files": state['total_files'],
        "results": processed_results
    }

def main():
    parser = argparse.ArgumentParser(description="Archive Lore Mining Engine")
    parser.add_argument('--batch-size', type=int, default=2, help="Numero di file da elaborare (default 2)")
    parser.add_argument('--dry-run', action='store_true', help="Esegue la selezione della coda senza generare file")
    args = parser.parse_args()
    
    run_archive_mining_batch(batch_size=args.batch_size, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
