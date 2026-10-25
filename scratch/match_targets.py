import json
import pathlib

for fname, path in [
    ("FINAL", pathlib.Path(r'e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Primary.json')),
    ("LIVE", pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\live_primary_lorebook.json'))
]:
    print(f"\n=================== {fname} ===================")
    data = json.load(open(path, 'r', encoding='utf-8'))
    entries = data.get('lexicon', data.get('entries', []))
    print(f"Total entries: {len(entries)}")
    
    target_names = [
        "Scarlett Rose", "Sierra Cruz", "Russell", "Russ", "Sinclair", 
        "Stanley", "Stan", "Davies", "Jared", "Thompson", "Alyssa", "Jasper"
    ]
    
    target_ids = [
        "4NzXF4_0hYxmN7Idltzpw", "ijy8vrlphNv19-p-gbYuY", "YCxAqNoShpefVvk0_Pc7i",
        "ekdQjq63xP7HtNuaPQJQE", "RM6rcwv8MlY1XWaCTQp0M", "alyssa_world_dossier_2b54a223",
        "Vcj4h2TL4Usola2A4OOl6"
    ]
    
    found_entries = []
    for idx, e in enumerate(entries):
        eid = e.get('entry_id') or e.get('id')
        name = e.get('name', '')
        keys = e.get('keys', [])
        
        match_id = eid in target_ids
        match_name = any(tn.lower() in name.lower() for tn in target_names) or any(any(tn.lower() in str(k).lower() for tn in target_names) for k in keys)
        
        if match_id or match_name:
            found_entries.append((idx, eid, name, e))
            
    print(f"Matched entries count: {len(found_entries)}")
    for idx, eid, name, e in found_entries:
        print(f"\n[{idx}] entry_id: {eid} | name: {name}")
        print(f"     type: {e.get('type')}")
        print(f"     keys: {e.get('keys')}")
        print(f"     secondary_keys: {e.get('secondary_keys')}")
        print(f"     selective: {e.get('selective')}")
        print(f"     key_logic: {e.get('key_logic')}")
        print(f"     avatar: {e.get('avatar')}")
        print(f"     custom_avatar_regex: {e.get('custom_avatar_regex')}")
        print(f"     avatar_activation_regex: {repr(e.get('avatar_activation_regex'))}")
        print(f"     lines_parsed: {e.get('lines_parsed')}")
        print(f"     npc_info: {e.get('npc_info')}")
        content = e.get('content', '')
        print(f"     content len: {len(content)}")
        print(f"     content preview: {repr(content[:100])}")
