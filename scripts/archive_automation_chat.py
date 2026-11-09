#!/usr/bin/env python3
"""
scripts/archive_automation_chat.py

Archivia automaticamente le chat e i transcript delle Automazioni Antigravity
all'interno della cartella di progetto SvartulfrVerse:
- Salva il transcript grezzo in: logs/automations/transcripts/YYYY-MM-DD_HHmm_<automation>.jsonl
- Genera il verbale chat formattato e leggibile in: logs/automations/YYYY-MM-DD_HHmm_<automation>.md

Uso:
  python scripts/archive_automation_chat.py --automation daily-character-enrichment
  python scripts/archive_automation_chat.py --automation daily-wyvern-monitor
  python scripts/archive_automation_chat.py --automation daily-proxy-free-models
"""

import argparse
import datetime
import json
import os
import pathlib
import shutil
import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT / 'logs' / 'automations'
TRANSCRIPTS_DIR = LOGS_DIR / 'transcripts'
BRAIN_DIR = pathlib.Path(os.path.expanduser('~/.gemini/antigravity/brain'))

def get_latest_conversation(exclude_id: str = None) -> pathlib.Path:
    if not BRAIN_DIR.exists():
        return None
    convs = []
    for d in BRAIN_DIR.iterdir():
        if not d.is_dir():
            continue
        if exclude_id and d.name == exclude_id:
            continue
        transcript = d / '.system_generated' / 'logs' / 'transcript.jsonl'
        if transcript.exists() and transcript.stat().st_size > 0:
            convs.append((d, transcript.stat().st_mtime))
    if not convs:
        return None
    convs.sort(key=lambda x: x[1], reverse=True)
    return convs[0][0]

def parse_transcript(transcript_path: pathlib.Path):
    steps = []
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                steps.append(obj)
            except Exception:
                continue
    return steps

def format_markdown_chat(automation_name: str, conv_id: str, steps: list, timestamp_str: str) -> str:
    md = []
    md.append(f"# Registro Chat Automazione — {automation_name}\n")
    md.append(f"- **Data & Ora:** {timestamp_str}")
    md.append(f"- **Conversation ID:** `{conv_id}`")
    md.append(f"- **Totale Step Registrati:** {len(steps)}")
    md.append(f"- **Origine:** Svartulfr Verse Scheduled Automation\n")
    md.append("---\n")

    for s in steps:
        idx = s.get('step_index', 0)
        source = s.get('source', '')
        stype = s.get('type', '')
        created = s.get('created_at', '')

        if stype == 'USER_INPUT':
            content = s.get('content', '')
            md.append(f"### 👤 Input Pianificatore / Utente (Step {idx} - {created})\n")
            md.append(f"```text\n{content.strip()}\n```\n")

        elif stype == 'PLANNER_RESPONSE':
            thinking = s.get('thinking', '')
            content = s.get('content', '')
            tool_calls = s.get('tool_calls', [])

            md.append(f"### 🤖 Risposta Agente (Step {idx} - {created})\n")
            if thinking:
                md.append("<details><summary>Visualizza Ragionamento (Thinking)</summary>\n\n")
                md.append(f"{thinking.strip()}\n\n</details>\n")

            if content:
                md.append(f"{content.strip()}\n")

            if tool_calls:
                md.append("#### 🛠️ Tool Eseguiti:\n")
                for tc in tool_calls:
                    name = tc.get('name', 'tool')
                    args = tc.get('args', {})
                    md.append(f"- **`{name}`**:")
                    md.append(f"  ```json\n  {json.dumps(args, indent=2, ensure_ascii=False)}\n  ```\n")

        elif stype == 'GENERIC' and source == 'MODEL':
            content = s.get('content', '')
            if content:
                md.append(f"#### 📄 Output Esecuzione (Step {idx}):\n")
                # Truncate if gigantic
                if len(content) > 3000:
                    preview = content[:2000] + f"\n\n... [output troncato: {len(content)} byte totali]"
                else:
                    preview = content
                md.append(f"```text\n{preview.strip()}\n```\n")

    md.append("\n---\n*Archiviazione eseguita automaticamente da scripts/archive_automation_chat.py*\n")
    return "\n".join(md)

def archive(automation_name: str, conv_id: str = None):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.datetime.now()
    ts_file = now.strftime("%Y-%m-%d_%H%M%S")
    ts_human = now.strftime("%Y-%m-%d %H:%M:%S")

    # If conv_id specified, use it; otherwise pick latest
    if conv_id:
        target_dir = BRAIN_DIR / conv_id
    else:
        target_dir = get_latest_conversation()

    if not target_dir or not target_dir.exists():
        print(f"[ERROR] Nessuna directory di conversazione trovata in {BRAIN_DIR}")
        return False

    c_id = target_dir.name
    raw_transcript = target_dir / '.system_generated' / 'logs' / 'transcript.jsonl'
    if not raw_transcript.exists():
        print(f"[ERROR] Transcript non trovato in {raw_transcript}")
        return False

    # 1. Copy raw transcript
    safe_name = automation_name.replace(" ", "_").replace("/", "_")
    target_raw = TRANSCRIPTS_DIR / f"{ts_file}_{safe_name}_{c_id[:8]}.jsonl"
    shutil.copy2(raw_transcript, target_raw)
    print(f"[OK] Transcript grezzo archiviato in: {target_raw.relative_to(ROOT)}")

    # 2. Generate formatted markdown chat log
    steps = parse_transcript(raw_transcript)
    md_content = format_markdown_chat(automation_name, c_id, steps, ts_human)

    target_md = LOGS_DIR / f"{ts_file}_{safe_name}.md"
    target_md.write_text(md_content, encoding='utf-8')
    print(f"[OK] Chat formattata salvata in: {target_md.relative_to(ROOT)}")

    # 3. Update an INDEX file in logs/automations/README.md
    index_file = LOGS_DIR / 'README.md'
    entry_line = f"- **{ts_human}** | [{safe_name}]({target_md.name}) | ID `{c_id[:8]}` | {len(steps)} steps\n"
    if not index_file.exists():
        header = "# Archivio Chat Automazioni — Svartúlfr Verse\n\nRegistro storico delle sessioni eseguite automaticamente in background:\n\n"
        index_file.write_text(header + entry_line, encoding='utf-8')
    else:
        with open(index_file, 'a', encoding='utf-8') as f:
            f.write(entry_line)

    return True

def main():
    parser = argparse.ArgumentParser(description="Archive Automation Chat to Project Logs")
    parser.add_argument("--automation", default="unnamed-automation", help="Nome identificativo dell'automazione")
    parser.add_argument("--conv-id", default=None, help="Conversation ID specifico (opzionale)")
    args = parser.parse_args()

    success = archive(args.automation, args.conv_id)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
