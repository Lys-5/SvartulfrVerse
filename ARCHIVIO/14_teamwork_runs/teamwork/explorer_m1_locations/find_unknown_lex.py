import json
import glob

unknowns = ['_xB6wzXC39XpCgVmD89Y2h', '_2JKA6UUf8DAzBFbADWAAJ', '_h1BaVYDMckXpgdaDCFNed', '_7H2Ve9Y7f33rTxNN9Ep91', '_GaQ8B1wLA7NCM1zP8JW6q', '_xYWFcMXnH7M8qac4rGmXW', '_CrpErFXTTJBRLrCR4hTeX', '_eDhC6hY41n7VtjTMxReP4']

found = {}
for path in glob.glob("FINAL/*.json") + glob.glob("ARCHIVIO/05_Snapshots_and_Extractions/**/*.json", recursive=True):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            entries = []
            if isinstance(data, dict):
                entries = data.get("entries") or data.get("lexicon") or data.get("world_lexicon_entries") or []
            elif isinstance(data, list):
                entries = data
            for e in entries:
                if isinstance(e, dict):
                    eid = e.get("id") or e.get("_id") or e.get("entry_id")
                    if eid in unknowns and eid not in found:
                        found[eid] = (e.get("name"), path)
    except Exception:
        pass

for u in unknowns:
    print(f"{u}: {found.get(u, 'STILL UNKNOWN')}")
