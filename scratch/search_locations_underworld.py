import json

targets = ['harbor', 'sinclair', 'lab', 'estate', 'ambrosia', 'sinner', 'hideout']

for path in ['FINAL/Svartulfr_Location.json', 'FINAL/Svartulfr_Lorebook_II.json', 'FINAL/Svartulfr_Lorebook_III.json']:
    d = json.load(open(path, 'r', encoding='utf-8'))
    for e in d.get('entries', []):
        name = e.get('name', '')
        content = e.get('content', '')
        for t in targets:
            if t.lower() in name.lower() or t.lower() in content.lower():
                print(f"{path} | entry_id: {e.get('entry_id')} | name: {name} | matched '{t}'")
                break
