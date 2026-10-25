import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(r"e:\repository\SvartulfrVerse")
TOKEN_PATH = ROOT / "scratch" / "wyvern_token.txt"

with open(TOKEN_PATH, "r", encoding="utf-8") as f:
    token = f.read().strip()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "AuditorBot/1.0",
    "Accept": "application/json"
}

CANONICAL_BROAD_KEYS = {
    "solarton", "succ", "blackwood", "losangeles", "underworld",
    "vampire", "werewolf", "human", "demihuman", "demi-human",
    "demon", "college", "student", "alpha", "beta", "omega", "pack"
}

def audit_dataset(name, root_data, entries, is_live=False):
    print(f"\n==================================================================")
    print(f"AUDITING DATASET: {name} (Total Entries: {len(entries)})")
    print(f"==================================================================")
    violations = []

    # 1. Root Level Checks
    if not is_live:
        if root_data.get("gallery") != []:
            violations.append(f"Root gallery is not empty list: {root_data.get('gallery')}")
        if root_data.get("gallery_count") != 0:
            violations.append(f"Root gallery_count is not 0: {root_data.get('gallery_count')}")
        if root_data.get("enableEntryHighlighting") is not True:
            violations.append(f"Root enableEntryHighlighting is not True: {root_data.get('enableEntryHighlighting')}")

    # 2. Entries Level Checks
    for idx, e in enumerate(entries):
        ename = e.get("name", f"Entry_{idx}")

        # Schema: npc_info
        info = e.get("npc_info")
        if not isinstance(info, dict):
            violations.append(f"[{idx}] {ename}: npc_info is not a dict")
        else:
            fn = info.get("first_name")
            if not isinstance(fn, str) or not fn.strip():
                violations.append(f"[{idx}] {ename}: invalid first_name '{fn}'")
            mn = info.get("middle_names")
            if not isinstance(mn, list) or any(not isinstance(m, str) for m in mn):
                violations.append(f"[{idx}] {ename}: invalid middle_names '{mn}'")
            ln = info.get("last_name")
            if ln is not None and not isinstance(ln, str):
                violations.append(f"[{idx}] {ename}: invalid last_name '{ln}'")
            nicks = info.get("nicknames")
            if not isinstance(nicks, list) or any(not isinstance(n, str) for n in nicks):
                violations.append(f"[{idx}] {ename}: invalid nicknames '{nicks}'")
            titles = info.get("titles")
            if not isinstance(titles, list) or any(not isinstance(t, str) for t in titles):
                violations.append(f"[{idx}] {ename}: invalid titles '{titles}'")
            np = info.get("npc_prefix")
            if np is not None and not isinstance(np, str):
                violations.append(f"[{idx}] {ename}: invalid npc_prefix '{np}'")

        # Toggles
        if e.get("scan_persona") is not True:
            violations.append(f"[{idx}] {ename}: scan_persona is not True")
        if e.get("whole_words_only") is not True:
            violations.append(f"[{idx}] {ename}: whole_words_only is not True")
        if e.get("highlight_keys") is not True:
            violations.append(f"[{idx}] {ename}: highlight_keys is not True")
        if e.get("enable_highlighting") is not True:
            violations.append(f"[{idx}] {ename}: enable_highlighting is not True")
        ext = e.get("extensions")
        if not isinstance(ext, dict) or ext.get("highlight_keys") is not True:
            violations.append(f"[{idx}] {ename}: extensions.highlight_keys is not True")

        # Avatar URL
        avatar = e.get("avatar")
        if not isinstance(avatar, str) or not avatar.startswith("https://") or "." not in avatar:
            violations.append(f"[{idx}] {ename}: invalid avatar URL '{avatar}'")

        # Regex parsing flags
        if e.get("custom_avatar_regex") is not True:
            violations.append(f"[{idx}] {ename}: custom_avatar_regex is not True")
        if e.get("lines_parsed") != 1:
            violations.append(f"[{idx}] {ename}: lines_parsed is not 1 ({e.get('lines_parsed')})")

        # Duplicate surname detection
        regex = e.get("avatar_activation_regex", "")
        # Normalize regex
        norm_regex = re.sub(r'\\+\s+', ' ', regex)
        norm_regex = re.sub(r'\\+s[+*]?', ' ', norm_regex)
        for dupe in ["Rivers Rivers", "Rogers Rogers", "Boone Boone", "Black Black", "O'Connor O'Connor",
                     "Virtuoso Virtuoso", "Cirillo Cirillo", "Bishop Bishop", "Thompson Thompson", "DeVille DeVille"]:
            if dupe.lower() in norm_regex.lower():
                violations.append(f"[{idx}] {ename}: duplicate surname defect '{dupe}' in regex")

        # Keyword hygiene
        keys = e.get("keys", [])
        for k in keys:
            if isinstance(k, str) and k.strip().lower() in CANONICAL_BROAD_KEYS:
                violations.append(f"[{idx}] {ename}: prohibited broad key '{k}' in keys")
        sec_keys = e.get("secondary_keys", [])
        for sk in sec_keys:
            if isinstance(sk, str) and sk.strip().lower() in CANONICAL_BROAD_KEYS:
                violations.append(f"[{idx}] {ename}: prohibited broad key '{sk}' in secondary_keys")
        if isinstance(info, dict) and isinstance(info.get("nicknames"), list):
            for nick in info["nicknames"]:
                if isinstance(nick, str) and nick.strip().lower() in CANONICAL_BROAD_KEYS:
                    violations.append(f"[{idx}] {ename}: prohibited broad key '{nick}' in npc_info.nicknames")

        # Selective rule
        selective = e.get("selective", False)
        if selective and len(sec_keys) == 0:
            violations.append(f"[{idx}] {ename}: selective is true but secondary_keys is empty")

        # Content checks
        content = e.get("content", "")
        if "{{age}}" in content.lower():
            violations.append(f"[{idx}] {ename}: residual {{age}} macro found in content")
        if "—" in content:
            violations.append(f"[{idx}] {ename}: em-dash found in content")

    print(f"Total violations found: {len(violations)}")
    if violations:
        for v in violations[:20]:
            print(f"  [FAIL] {v}")
    else:
        print("  [CLEAN] All checks passed with 0 violations!")
    return len(violations) == 0

# 1. Local Primary
with open(ROOT / "FINAL" / "Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    local_prim = json.load(f)
ok_lp = audit_dataset("Local Primary (FINAL)", local_prim, local_prim.get("lexicon", []))

# 2. Local Secondary
with open(ROOT / "FINAL" / "Svartulfr_NPC_Secondary.json", "r", encoding="utf-8") as f:
    local_sec = json.load(f)
ok_ls = audit_dataset("Local Secondary (FINAL)", local_sec, local_sec.get("lexicon", []))

# 3. Live Primary
url_p = f"https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC"
req_p = urllib.request.Request(url_p, headers=headers)
with urllib.request.urlopen(req_p) as resp:
    live_prim = json.loads(resp.read().decode("utf-8"))
ok_live_p = audit_dataset("Live Cloud Primary (_zwEqgEEzh12X6gHVmMKKC)", live_prim, live_prim.get("lexicon", []), is_live=True)

# 4. Live Secondary
url_s = f"https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV"
req_s = urllib.request.Request(url_s, headers=headers)
with urllib.request.urlopen(req_s) as resp:
    live_sec = json.loads(resp.read().decode("utf-8"))
ok_live_s = audit_dataset("Live Cloud Secondary (_Uht3Ckz44JBDrPnUHq7LV)", live_sec, live_sec.get("lexicon", []), is_live=True)

print("\n" + "=" * 70)
if ok_lp and ok_ls and ok_live_p and ok_live_s:
    print("OVERALL FORENSIC AUDIT RESULT: CLEAN (100% PASS)")
else:
    print("OVERALL FORENSIC AUDIT RESULT: INTEGRITY VIOLATION")
print("=" * 70)
