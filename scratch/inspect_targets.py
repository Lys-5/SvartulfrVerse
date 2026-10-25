import json

def inspect_lorebook(path, target_ids):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"=== LOREBOOK: {path} ===")
    print("Top-level keys:", list(data.keys()))
    print("ID:", data.get("id"))
    print("Name:", data.get("name"))
    print("Token budget:", data.get("token_budget"))
    print("photoURL:", data.get("photoURL"))
    
    entries = data.get("entries", [])
    lexicon = data.get("lexicon", [])
    print(f"Entries count: {len(entries)}, Lexicon count: {len(lexicon)}")
    
    for tid in target_ids:
        print(f"\n==========================================")
        print(f"--- Target ID: {tid} ---")
        
        # Check by entry_id, id, or name
        found_lex = [e for e in lexicon if e.get("entry_id") == tid or e.get("id") == tid]
        found_ent = [e for e in entries if e.get("entry_id") == tid or e.get("id") == tid]
        
        if not found_lex and not found_ent:
            print(f"NOT FOUND by ID: {tid}")
            # Try searching by name in lexicon
            continue
            
        rec = found_lex[0] if found_lex else found_ent[0]
        for k in ['entry_id', 'id', 'name', 'title', 'type', 'selective', 'enabled', 'constant', 'exclude_from_recursion', 'keys', 'secondary_keys', 'key_logic', 'avatar', 'custom_avatar_regex', 'avatar_activation_regex', 'lines_parsed', 'npc_info', 'ignored_characters', 'ignored_personas']:
            print(f"{k}: {rec.get(k)}")
            
        content = rec.get("content") or rec.get("description") or ""
        print(f"Content Length: {len(content)} characters")
        print(f"Content preview (first 250 chars):\n{content[:250]}")
        print(f"Content preview (last 250 chars):\n{content[-250:]}")

print("INSPECTING PRIMARY:")
inspect_lorebook("FINAL/Svartulfr_NPC_Primary.json", [
    "C-JisFj8qA1tsFEqZKevk", # Erik
    "jDuJtzirlEZC3K_ArIufh", # Malachia
    "H2JX-NkHRiJ2FzoekC5ZZ", # Noah
    "tAcrWLtWSDGf3xJJRwUOM", # Logan
    "HhuMluMmIIENUei3bX6ed", # Wulfnic
    "BXi3sENAVYB8OKF80Q9Su"  # Mackenzie
])

print("\n\nINSPECTING SECONDARY:")
inspect_lorebook("FINAL/Svartulfr_NPC_Secondary.json", [
    "h-ttmlgJYeRXqyDvQjSX7"  # Edric
])
