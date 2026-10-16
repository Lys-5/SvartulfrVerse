import os
import json
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = r"e:\repository\SvartulfrVerse"
BACKUP_DIR = os.path.join(PROJECT_ROOT, "scratch", "backup_pre_audit_lorebooks")
FINAL_DIR = os.path.join(PROJECT_ROOT, "FINAL")
LOG_PATH = os.path.join(PROJECT_ROOT, "scratch", "missing_npc_avatars.json")

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

log_data = json.load(open(LOG_PATH, encoding="utf-8"))
logged_entries = log_data["entries"]

print(f"Log total: {len(logged_entries)}")
logged_ids = {e["entry_id"]: e for e in logged_entries}

# Check Primary and Secondary
files = ["Svartulfr_NPC_Primary.json", "Svartulfr_NPC_Secondary.json"]

total_checked = 0
valid_preserved = 0
fallback_assigned = 0

for fname in files:
    b_data = json.load(open(os.path.join(BACKUP_DIR, fname), encoding="utf-8"))["lexicon"]
    f_data = json.load(open(os.path.join(FINAL_DIR, fname), encoding="utf-8"))["lexicon"]
    
    for idx, (b_entry, f_entry) in enumerate(zip(b_data, f_data)):
        total_checked += 1
        eid = f_entry["entry_id"]
        name = f_entry["name"]
        
        b_av = b_entry.get("avatar", "")
        f_av = f_entry.get("avatar", "")
        
        if b_av and b_av.strip().startswith("http"):
            # Should NOT be in logged_ids
            assert eid not in logged_ids, f"Entry {eid} was valid in backup but in missing log!"
            # Should be untouched in FINAL
            assert b_av == f_av, f"Entry {eid} avatar mutated! Pre: '{b_av}' != Post: '{f_av}'"
            valid_preserved += 1
        else:
            # Must be in logged_ids
            assert eid in logged_ids, f"Entry {eid} had missing avatar in backup but NOT in missing log!"
            log_item = logged_ids[eid]
            assert log_item["lorebook"] == fname, f"Log lorebook mismatch: {log_item['lorebook']} vs {fname}"
            assert log_item["index"] == idx, f"Log index mismatch: {log_item['index']} vs {idx}"
            assert log_item["name"] == name, f"Log name mismatch: {log_item['name']} vs {name}"
            assert log_item["applied_avatar"] == FALLBACK_AVATAR, f"Log applied_avatar mismatch: {log_item['applied_avatar']}"
            assert f_av == FALLBACK_AVATAR, f"Final avatar is not fallback: '{f_av}'"
            fallback_assigned += 1

print(f"Total checked: {total_checked}")
print(f"Valid preserved: {valid_preserved} (Expected 114)")
print(f"Fallback assigned: {fallback_assigned} (Expected 302)")
print("ALL AVATAR CHECKS PASSED WITH 100% MATHEMATICAL PRECISION!")
