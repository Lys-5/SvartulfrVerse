import json

for path in ["FINAL/Svartulfr_NPC_Primary.json", "FINAL/Svartulfr_NPC_Secondary.json"]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"=== {path} ===")
    has_entries = "entries" in data
    has_lexicon = "lexicon" in data
    entries_len = len(data.get("entries", [])) if has_entries else 0
    lexicon_len = len(data.get("lexicon", [])) if has_lexicon else 0
    print(f"has entries: {has_entries} (len {entries_len})")
    print(f"has lexicon: {has_lexicon} (len {lexicon_len})")
    
    # Check if entries and lexicon have same IDs
    if has_entries and has_lexicon:
        e_ids = [e.get("entry_id") or e.get("id") for e in data["entries"]]
        l_ids = [e.get("entry_id") or e.get("id") for e in data["lexicon"]]
        same_ids = (e_ids == l_ids)
        print(f"Are IDs identical in order? {same_ids}")
        if not same_ids:
            print(f"Difference: set(entries) - set(lexicon) = {set(e_ids) - set(l_ids)}")
            print(f"Difference: set(lexicon) - set(entries) = {set(l_ids) - set(e_ids)}")
