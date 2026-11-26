import json
import os
import re

FINAL_DIR = r"e:\repository\SvartulfrVerse\FINAL"

lorebooks = [
    {"id": "_gwwCxCfQ6PQaLEjAQVpJL", "file": "Svartulfr_Lorebook_I.json", "name": "Lorebook I"},
    {"id": "_HfG7TeV6MJyj6bxMwxkpt", "file": "Svartulfr_Lorebook_II.json", "name": "Lorebook II"},
    {"id": "_9zWTGqYJNJ4BCDMj8gfcD", "file": "Svartulfr_Lorebook_III.json", "name": "Lorebook III"},
    {"id": "_EjXxkmPVhpCXg8xABpFkK", "file": "Svartulfr_Location.json", "name": "Location"},
    {"id": "_zwEqgEEzh12X6gHVmMKKC", "file": "Svartulfr_NPC_Primary.json", "name": "NPC Primary"},
    {"id": "_Uht3Ckz44JBDrPnUHq7LV", "file": "Svartulfr_NPC_Secondary.json", "name": "NPC Secondary"}
]

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "vampire", "werewolf", 
    "college", "student", "alpha", "omega"
}

npc_spurious_fields = ["npc_info", "custom_avatar_regex", "lines_parsed"]

report = {
    "pillar1_spurious_non_npc": {},
    "pillar2_broad_keys_npc": {},
    "pillar3_age_macros": {},
    "pillar4_npc_avatar_regex": {}
}

for lb in lorebooks:
    path = os.path.join(FINAL_DIR, lb["file"])
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # We inspect lexicon and entries
    # For reporting, let's analyze lexicon items, but also check entries
    lexicon = data.get("lexicon", [])
    entries = data.get("entries", [])
    
    lb_name = lb["name"]
    report["pillar1_spurious_non_npc"][lb_name] = []
    report["pillar2_broad_keys_npc"][lb_name] = []
    report["pillar3_age_macros"][lb_name] = []
    report["pillar4_npc_avatar_regex"][lb_name] = []
    
    for idx, e in enumerate(lexicon):
        entry_id = e.get("entry_id") or e.get("uid") or str(idx)
        name = e.get("name") or e.get("comment") or f"Entry_{idx}"
        etype = e.get("type", "unknown")
        
        # Pillar 1: Spurious NPC metadata on non-NPC entries
        is_npc = (etype == "npc") or (lb_name in ["NPC Primary", "NPC Secondary"])
        found_spurious = {}
        for sf in npc_spurious_fields:
            if sf in e:
                # If non-npc has it
                if not is_npc:
                    found_spurious[sf] = e[sf]
        if found_spurious:
            report["pillar1_spurious_non_npc"][lb_name].append({
                "index": idx,
                "id": entry_id,
                "name": name,
                "type": etype,
                "spurious_fields": list(found_spurious.keys())
            })
            
        # Pillar 2: Broad keys on NPC entries
        if is_npc:
            keys = [k.lower().strip() for k in e.get("keys", [])]
            sec_keys = [k.lower().strip() for k in e.get("secondary_keys", [])]
            all_keys = set(keys + sec_keys)
            broad_found = all_keys.intersection(BROAD_KEYS)
            if broad_found:
                report["pillar2_broad_keys_npc"][lb_name].append({
                    "index": idx,
                    "id": entry_id,
                    "name": name,
                    "broad_keys": list(broad_found),
                    "selective": e.get("selective", False),
                    "has_secondary": bool(e.get("secondary_keys"))
                })
                
        # Pillar 3: {{age}} macros in any field
        entry_str = json.dumps(e, ensure_ascii=False)
        age_matches = re.findall(r"\{\{age(?:::.*?)?\}\}", entry_str, flags=re.IGNORECASE)
        if age_matches:
            report["pillar3_age_macros"][lb_name].append({
                "index": idx,
                "id": entry_id,
                "name": name,
                "matches": age_matches
            })
            
        # Pillar 4: NPC avatar and regex splitting
        if is_npc:
            avatar = e.get("avatar", "")
            car = e.get("custom_avatar_regex", False)
            lp = e.get("lines_parsed")
            regex = e.get("avatar_activation_regex", "")
            
            issues = []
            if not avatar or avatar.strip() == "":
                issues.append("missing_avatar")
            if not car:
                issues.append("custom_avatar_regex_not_true")
            if lp != 1:
                issues.append(f"lines_parsed_{lp}")
            if not regex or "(?:^|\\n)" not in regex:
                issues.append("invalid_or_missing_multiline_regex")
                
            if issues:
                report["pillar4_npc_avatar_regex"][lb_name].append({
                    "index": idx,
                    "id": entry_id,
                    "name": name,
                    "avatar": avatar,
                    "issues": issues
                })

# Summary counts
summary = {}
for pillar, pdata in report.items():
    summary[pillar] = {lb: len(items) for lb, items in pdata.items()}
    summary[pillar]["TOTAL"] = sum(len(items) for items in pdata.values())

out_path = r"e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_1\audit_summary.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "summary": summary,
        "details": report
    }, f, indent=2, ensure_ascii=False)

print(json.dumps(summary, indent=2))
