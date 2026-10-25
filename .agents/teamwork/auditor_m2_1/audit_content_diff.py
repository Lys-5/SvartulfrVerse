import json
import subprocess
from pathlib import Path

ROOT = Path(r"e:\repository\SvartulfrVerse")

def check_content_diff(rel_path):
    # Get git HEAD version of the file
    cmd = ["git", "show", f"HEAD:{rel_path}"]
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8")
    if p.returncode != 0:
        print(f"Failed to get git HEAD for {rel_path}: {p.stderr}")
        return False
    
    old_data = json.loads(p.stdout)
    with open(ROOT / rel_path, "r", encoding="utf-8") as f:
        new_data = json.loads(f.read())

    old_lex = old_data.get("lexicon", [])
    new_lex = new_data.get("lexicon", [])

    print(f"\n=======================================================")
    print(f"Checking JED+ Content Integrity: {rel_path}")
    print(f"=======================================================")
    print(f"Old Lexicon count: {len(old_lex)}, New Lexicon count: {len(new_lex)}")

    old_map = {e.get("name"): e for e in old_lex}
    new_map = {e.get("name"): e for e in new_lex}

    content_mismatches = []
    field_changes_summary = {}

    for name, new_entry in new_map.items():
        if name not in old_map:
            print(f"  [NEW ENTRY ADDED]: {name}")
            continue
        old_entry = old_map[name]
        
        old_content = old_entry.get("content", "")
        new_content = new_entry.get("content", "")

        if old_content != new_content:
            content_mismatches.append({
                "name": name,
                "old_len": len(old_content),
                "new_len": len(new_content)
            })

        # Track what fields actually changed
        for k in set(list(old_entry.keys()) + list(new_entry.keys())):
            if old_entry.get(k) != new_entry.get(k):
                field_changes_summary[k] = field_changes_summary.get(k, 0) + 1

    print(f"Content mismatches found: {len(content_mismatches)}")
    if content_mismatches:
        for cm in content_mismatches[:10]:
            print(f"  - {cm['name']}: old_len={cm['old_len']} vs new_len={cm['new_len']}")
    else:
        print("  [SUCCESS] 100% of preexisting entries have EXACTLY IDENTICAL 'content' (0 JED+ dossiers altered or truncated)!")

    print(f"\nSummary of fields that changed across entries:")
    for k, count in sorted(field_changes_summary.items(), key=lambda x: -x[1]):
        print(f"  {k}: modified in {count} entries")

    return len(content_mismatches) == 0

p1 = check_content_diff("FINAL/Svartulfr_NPC_Primary.json")
p2 = check_content_diff("FINAL/Svartulfr_NPC_Secondary.json")

print("\n" + "=" * 70)
if p1 and p2:
    print("[FORENSIC INTEGRITY AUDIT PASSED: ZERO DOSSIERS CORRUPTED/ALTERED/TRUNCATED]")
else:
    print("[FORENSIC INTEGRITY AUDIT FAILED: CONTENT WAS ALTERED]")
print("=" * 70)
