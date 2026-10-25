import json
import hashlib

def verify_primary(filepath):
    print(f"=== Checking {filepath} ===")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        data = json.loads(content)
    
    # 1. Root gallery
    assert "gallery" in data, "Missing root gallery"
    assert isinstance(data["gallery"], list), "gallery is not list"
    assert len(data["gallery"]) == 0, f"gallery is not empty: {data['gallery']}"
    assert "gallery_count" in data, "Missing gallery_count"
    assert data["gallery_count"] == 0, f"gallery_count != 0: {data['gallery_count']}"
    assert not isinstance(data["gallery_count"], bool), "gallery_count is bool"
    assert data.get("enableEntryHighlighting") is True, "Missing or false root enableEntryHighlighting"
    assert data.get("token_budget") == 7500, f"Unexpected token_budget: {data.get('token_budget')}"
    
    # 2. Parity between entries and lexicon
    assert "entries" in data and "lexicon" in data, "Missing entries or lexicon"
    entries_json = json.dumps(data["entries"], ensure_ascii=False)
    lexicon_json = json.dumps(data["lexicon"], ensure_ascii=False)
    assert entries_json == lexicon_json, "entries and lexicon differ in content"
    assert len(data["entries"]) == 99, f"Count mismatch: {len(data['entries'])} != 99"
    assert len(data["lexicon"]) == 99, f"Count mismatch: {len(data['lexicon'])} != 99"
    
    # 3. Check every entry
    ignored_chars_all = []
    ignored_personas_all = []
    selective_entries = []
    
    for idx, e in enumerate(data["lexicon"]):
        name = e.get("name", f"idx_{idx}")
        # Check 3 toggles
        assert e.get("scan_persona") is True, f"[{idx}] {name} scan_persona not True"
        assert e.get("whole_words_only") is True, f"[{idx}] {name} whole_words_only not True"
        assert e.get("highlight_keys") is True, f"[{idx}] {name} highlight_keys not True"
        assert e.get("enable_highlighting") is True, f"[{idx}] {name} enable_highlighting not True"
        assert e.get("extensions", {}).get("highlight_keys") is True, f"[{idx}] {name} extensions.highlight_keys not True"
        
        # Check npc_info
        info = e.get("npc_info")
        assert isinstance(info, dict), f"[{idx}] {name} npc_info is not dict: {type(info)}"
        assert "first_name" in info and isinstance(info["first_name"], str) and info["first_name"].strip(), f"[{idx}] {name} invalid first_name"
        assert "middle_names" in info and isinstance(info["middle_names"], list), f"[{idx}] {name} invalid middle_names"
        assert all(isinstance(m, str) for m in info["middle_names"]), f"[{idx}] {name} non-string in middle_names"
        assert "last_name" in info and (info["last_name"] is None or isinstance(info["last_name"], str)), f"[{idx}] {name} invalid last_name"
        assert "nicknames" in info and isinstance(info["nicknames"], list), f"[{idx}] {name} invalid nicknames"
        assert all(isinstance(nk, str) for nk in info["nicknames"]), f"[{idx}] {name} non-string in nicknames"
        assert "titles" in info and isinstance(info["titles"], list), f"[{idx}] {name} invalid titles"
        assert all(isinstance(t, str) for t in info["titles"]), f"[{idx}] {name} non-string in titles"
        assert "npc_prefix" in info and isinstance(info["npc_prefix"], str), f"[{idx}] {name} invalid npc_prefix"
        
        # Check avatar
        avatar = e.get("avatar")
        assert isinstance(avatar, str) and avatar.startswith("https://"), f"[{idx}] {name} invalid avatar: {avatar}"
        
        # Anti-collision tracking
        ics = e.get("ignored_characters", [])
        if ics:
            ignored_chars_all.extend(ics)
        ips = e.get("ignored_personas", [])
        if ips:
            ignored_personas_all.extend(ips)
            
        if e.get("selective") is True:
            selective_entries.append((idx, name, e.get("secondary_keys"), e.get("key_logic")))
        else:
            # selective is False, ensure secondary_keys empty
            assert e.get("secondary_keys") == [], f"[{idx}] {name} has secondary_keys while selective is False: {e.get('secondary_keys')}"
            
    print(f"Checked 99 entries successfully.")
    print(f"Ignored characters count: {len(ignored_chars_all)} ({ignored_chars_all})")
    print(f"Ignored personas count: {len(ignored_personas_all)} ({ignored_personas_all})")
    print(f"Selective entries count: {len(selective_entries)} ({selective_entries})")
    
    assert len(ignored_chars_all) == 13, f"Expected 13 ignored_characters, got {len(ignored_chars_all)}"
    assert len(ignored_personas_all) == 2, f"Expected 2 ignored_personas, got {len(ignored_personas_all)}"
    assert len(selective_entries) == 2, f"Expected 2 selective entries, got {len(selective_entries)}"
    
    # Check that selective entries are Jasper and Alyssa with Dossier keys
    for idx, name, sec_keys, k_logic in selective_entries:
        assert "Jasper" in name or "Alyssa" in name, f"Unexpected selective entry: {name}"
        assert sec_keys == ["Dossier", "Scheda", "Archivio", "Database", "Profilo"], f"Invalid secondary_keys: {sec_keys}"
        assert k_logic == "AND_ANY", f"Invalid key_logic: {k_logic}"
        
    print(f"=== All contract invariants verified for {filepath} ===\n")

def verify_secondary(filepath):
    print(f"=== Checking {filepath} ===")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        data = json.loads(content)
    
    # 1. Root gallery
    assert "gallery" in data, "Missing root gallery"
    assert isinstance(data["gallery"], list), "gallery is not list"
    assert len(data["gallery"]) == 0, f"gallery is not empty: {data['gallery']}"
    assert "gallery_count" in data, "Missing gallery_count"
    assert data["gallery_count"] == 0, f"gallery_count != 0: {data['gallery_count']}"
    assert not isinstance(data["gallery_count"], bool), "gallery_count is bool"
    assert data.get("enableEntryHighlighting") is True, "Missing or false root enableEntryHighlighting"
    assert data.get("token_budget") == 5000, f"Unexpected token_budget: {data.get('token_budget')}"
    
    # 2. Parity between entries and lexicon
    assert "entries" in data and "lexicon" in data, "Missing entries or lexicon"
    entries_json = json.dumps(data["entries"], ensure_ascii=False)
    lexicon_json = json.dumps(data["lexicon"], ensure_ascii=False)
    assert entries_json == lexicon_json, "entries and lexicon differ in content"
    assert len(data["entries"]) == 211, f"Count mismatch: {len(data['entries'])} != 211"
    assert len(data["lexicon"]) == 211, f"Count mismatch: {len(data['lexicon'])} != 211"
    
    # 3. Check every entry
    ignored_chars_all = []
    
    for idx, e in enumerate(data["lexicon"]):
        name = e.get("name", f"idx_{idx}")
        # Check 3 toggles
        assert e.get("scan_persona") is True, f"[{idx}] {name} scan_persona not True"
        assert e.get("whole_words_only") is True, f"[{idx}] {name} whole_words_only not True"
        assert e.get("highlight_keys") is True, f"[{idx}] {name} highlight_keys not True"
        assert e.get("enable_highlighting") is True, f"[{idx}] {name} enable_highlighting not True"
        assert e.get("extensions", {}).get("highlight_keys") is True, f"[{idx}] {name} extensions.highlight_keys not True"
        
        # Check npc_info
        info = e.get("npc_info")
        assert isinstance(info, dict), f"[{idx}] {name} npc_info is not dict: {type(info)}"
        assert "first_name" in info and isinstance(info["first_name"], str) and info["first_name"].strip(), f"[{idx}] {name} invalid first_name"
        assert "middle_names" in info and isinstance(info["middle_names"], list), f"[{idx}] {name} invalid middle_names"
        assert all(isinstance(m, str) for m in info["middle_names"]), f"[{idx}] {name} non-string in middle_names"
        assert "last_name" in info and (info["last_name"] is None or isinstance(info["last_name"], str)), f"[{idx}] {name} invalid last_name"
        assert "nicknames" in info and isinstance(info["nicknames"], list), f"[{idx}] {name} invalid nicknames"
        assert all(isinstance(nk, str) for nk in info["nicknames"]), f"[{idx}] {name} non-string in nicknames"
        assert "titles" in info and isinstance(info["titles"], list), f"[{idx}] {name} invalid titles"
        assert all(isinstance(t, str) for t in info["titles"]), f"[{idx}] {name} non-string in titles"
        assert "npc_prefix" in info and isinstance(info["npc_prefix"], str), f"[{idx}] {name} invalid npc_prefix"
        
        # Check avatar
        avatar = e.get("avatar")
        assert isinstance(avatar, str) and avatar.startswith("https://"), f"[{idx}] {name} invalid avatar: {avatar}"
        
        # Anti-collision tracking
        ics = e.get("ignored_characters", [])
        if ics:
            ignored_chars_all.extend(ics)
            
        assert e.get("selective") is False, f"[{idx}] {name} has selective: True in Secondary Lorebook"
            
    print(f"Checked 211 entries successfully.")
    print(f"Ignored characters count: {len(ignored_chars_all)} ({ignored_chars_all})")
    assert ignored_chars_all == ["_TbRM3EdxDjHFgqztTbCpL"], f"Unexpected ignored_characters in Secondary: {ignored_chars_all}"
    print(f"=== All contract invariants verified for {filepath} ===\n")

if __name__ == "__main__":
    verify_primary("FINAL/Svartulfr_NPC_Primary.json")
    verify_primary("lorebooks/optimized/Svartulfr_NPC_Primary.json")

    with open("FINAL/Svartulfr_NPC_Primary.json", "rb") as f1, open("lorebooks/optimized/Svartulfr_NPC_Primary.json", "rb") as f2:
        b1 = f1.read()
        b2 = f2.read()
        assert b1 == b2, "FINAL and optimized Primary lorebooks differ byte-for-byte!"
        print(f"FINAL and optimized Primary files are 100% BYTE-FOR-BYTE IDENTICAL ({len(b1):,} bytes, SHA256: {hashlib.sha256(b1).hexdigest()})\n")

    verify_secondary("FINAL/Svartulfr_NPC_Secondary.json")
    verify_secondary("lorebooks/optimized/Svartulfr_NPC_Secondary.json")

    with open("FINAL/Svartulfr_NPC_Secondary.json", "rb") as f1, open("lorebooks/optimized/Svartulfr_NPC_Secondary.json", "rb") as f2:
        b1 = f1.read()
        b2 = f2.read()
        assert b1 == b2, "FINAL and optimized Secondary lorebooks differ byte-for-byte!"
        print(f"FINAL and optimized Secondary files are 100% BYTE-FOR-BYTE IDENTICAL ({len(b1):,} bytes, SHA256: {hashlib.sha256(b1).hexdigest()})\n")
