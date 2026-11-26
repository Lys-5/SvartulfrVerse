import json
import os
import glob

files = [
    "Svartulfr_Lorebook_I.json",
    "Svartulfr_Lorebook_II.json",
    "Svartulfr_Lorebook_III.json",
    "Svartulfr_Location.json",
    "Svartulfr_NPC_Primary.json",
    "Svartulfr_NPC_Secondary.json"
]

expected_ids = {
    "Svartulfr_Lorebook_I.json": "_gwwCxCfQ6PQaLEjAQVpJL",
    "Svartulfr_Lorebook_II.json": "_HfG7TeV6MJyj6bxMwxkpt",
    "Svartulfr_Lorebook_III.json": "_9zWTGqYJNJ4BCDMj8gfcD",
    "Svartulfr_Location.json": "_EjXxkmPVhpCXg8xABpFkK",
    "Svartulfr_NPC_Primary.json": "_zwEqgEEzh12X6gHVmMKKC",
    "Svartulfr_NPC_Secondary.json": "_Uht3Ckz44JBDrPnUHq7LV"
}

results = []
total_entries = 0
total_lexicon = 0

for fname in files:
    fpath = os.path.join(r"e:\repository\SvartulfrVerse\FINAL", fname)
    if not os.path.exists(fpath):
        results.append(f"MISSING: {fname}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    lb_id = data.get("id") or data.get("lorebook_id") or data.get("_id")
    name = data.get("name") or data.get("title")
    entries = data.get("entries", [])
    lexicon = data.get("lexicon", [])
    
    entries_count = len(entries) if isinstance(entries, list) else (len(entries) if isinstance(entries, dict) else "N/A")
    lexicon_count = len(lexicon) if isinstance(lexicon, list) else (len(lexicon) if isinstance(lexicon, dict) else "N/A")
    
    total_entries += entries_count if isinstance(entries_count, int) else 0
    total_lexicon += lexicon_count if isinstance(lexicon_count, int) else 0
    
    # Check top-level keys
    top_keys = list(data.keys())
    
    results.append({
        "file": fname,
        "id": lb_id,
        "expected_id": expected_ids.get(fname),
        "id_matches": lb_id == expected_ids.get(fname),
        "name": name,
        "entries_count": entries_count,
        "lexicon_count": lexicon_count,
        "counts_equal": entries_count == lexicon_count,
        "top_keys": top_keys[:10]
    })

print(json.dumps({
    "files": results,
    "total_entries": total_entries,
    "total_lexicon": total_lexicon
}, indent=2))
