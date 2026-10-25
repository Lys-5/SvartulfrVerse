---
name: chrome-tabgroup-source-extractor
description: >
  Extracts saved Chrome tab groups, URLs, and titles directly from on-disk LevelDB Sync storage.
  Operates non-invasively without restarting Chrome, bypassing Chrome DevTools Protocol (CDP) port locks,
  single-client debugger limitations, and origin security policies.
---

# Chrome TabGroup Source Extractor

A robust, non-invasive skill to discover and extract active Saved Tab Groups, page titles, and URLs directly from Google Chrome's local synchronization storage (`Sync Data/LevelDB`).

## When to Use This Skill

- When the user asks to extract, inspect, or reference open tabs or saved tab groups from Chrome.
- When Chrome is running with Remote Debugging (`--remote-debugging-port=9222`) but CDP connections are locked by an existing debugger (e.g. IDE host process) under the **Single-Client CDP Rule**.
- When HTTP endpoints (`/json`, `/json/version`) return `404 Not Found` or `403 Forbidden` due to modern Chrome origin restrictions.
- When restarting or closing the user's browser is unacceptable because it would disrupt active workflows or lose unsaved state.

---

## Technical Architecture

```
Chrome Runtime (Unchanged)
   │
   ▼ writes asynchronously
%LOCALAPPDATA%\Google\Chrome\User Data\Default\Sync Data\LevelDB\
   ├── *.ldb (SSTable files containing protobuf sync entities)
   └── *.log (Write-ahead logs)
   │
   ▼ read-only binary scan (extract_tabgroup.py)
1. Match Tab Group Name (e.g. "RPG Source") -> Extract Group GUID
2. Correlate Sync Entities -> Resolve URLs & Titles
3. Output Structured JSON / Markdown Tables
```

---

## CLI Usage

The skill provides a self-contained helper script in `scripts/extract_tabgroup.py` requiring only standard Python 3:

```powershell
# List all discovered tab groups in the Chrome profile
python .agents/skills/chrome-tabgroup-source-extractor/scripts/extract_tabgroup.py --list-groups

# Extract a specific tab group as a Markdown table
python .agents/skills/chrome-tabgroup-source-extractor/scripts/extract_tabgroup.py --group "RPG Source" --format markdown

# Extract as structured JSON
python .agents/skills/chrome-tabgroup-source-extractor/scripts/extract_tabgroup.py --group "RPG Source" --format json

# Extract as plain URL list
python .agents/skills/chrome-tabgroup-source-extractor/scripts/extract_tabgroup.py --group "RPG Source" --format list
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--group`, `-g` | Name or case-insensitive substring of the tab group | `None` |
| `--guid` | Exact UUID string of the tab group entity | `None` |
| `--format`, `-f` | Output format: `table`, `markdown`, `json`, `list` | `table` |
| `--list-groups`, `-l` | Scans and lists all detected saved tab groups | `False` |
| `--sync-dir`, `-d` | Custom path to `Sync Data/LevelDB` directory | Auto-detected |

---

## Storage Locations by Operating System

| OS | Default LevelDB Sync Path |
|----|---------------------------|
| **Windows** | `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Sync Data\LevelDB` |
| **macOS** | `~/Library/Application Support/Google/Chrome/Default/Sync Data/LevelDB` |
| **Linux** | `~/.config/google-chrome/Default/Sync Data/LevelDB` |

---

## Best Practices & Safety

1. **Read-Only Access:** Never write or modify files within Chrome's `User Data` while Chrome is running. Always open with mode `rb`.
2. **Trailing Character Sanitization:** Sync protobuf entries often terminate string fields with length prefixes or delimiters; the script automatically strips trailing parenthesis or commas from URLs.
3. **Format Discipline:** When inserting extracted resources into project documentation (e.g., `EXTERNAL_RESOURCES_INDEX.md` or `CHANGELOG.md`), ensure compliance with project rules: wrap URLs in backticks and avoid em-dashes (`—`).
