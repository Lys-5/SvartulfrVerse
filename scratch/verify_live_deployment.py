import json
import re
import urllib.request

with open("scratch/wyvern_token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "User-Agent": "AuditorBot/1.0"
}

EMBLEM_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"
PLACEHOLDER_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"
OLD_PLACEHOLDER = "6f8b7c78-2c7b-4f87-c98b-8a0d27f32c00"

BROAD_KEYS = {"solarton", "succ", "blackwood", "vampire", "werewolf", "college", "student", "alpha", "omega"}

CORE_7 = {
    "Erik Ulfr Douglas": "_QPea6g4Q1QfeYCVHCLMPR",
    "Malachia Björn Douglas Bloodmoon": "_RDfz7XzTpM23LpPALVXHM",
    "Noah Loki Douglas Bloodmoon": "_zFLUjV8aVxQRAfQxGcAcY",
    "Logan Dominic Járn Douglas": "_T8Ywcr9FEqNf9JxbK6eHP",
    "Wulfnic Báleygr Bloodmoon": "_HEQQbbRFwKdG8QE2Fh1z1",
    "Mackenzie Sanchez-Rogers": "_zn24784jfcchQ7EwCyAnm",
    "Edric Douglas": "_TbRM3EdxDjHFgqztTbCpL"
}

def audit_live_lorebook(lb_id, expected_count, expected_budget):
    req = urllib.request.Request(f"https://api.wyvern.chat/lorebooks/{lb_id}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        status = resp.status
    lex = data.get("lexicon", [])
    assert status == 200, f"Status {status}"
    assert len(lex) == expected_count, f"Expected {expected_count}, got {len(lex)}"
    assert data.get("token_budget") == expected_budget, f"Budget {data.get('token_budget')}"
    assert data.get("photoURL") == EMBLEM_URL, f"photoURL {data.get('photoURL')}"

    errors = []
    for idx, e in enumerate(lex):
        name = e.get("name", "")
        c = e.get("content", "")
        if e.get("type") != "npc":
            errors.append(f"[{idx}] {name}: type={e.get('type')}")
        if bool(e.get("selective")):
            errors.append(f"[{idx}] {name}: selective={e.get('selective')}")
        if e.get("exclude_from_recursion") is not True:
            errors.append(f"[{idx}] {name}: exclude_from_recursion={e.get('exclude_from_recursion')}")
        av = e.get("avatar", "")
        if not av or not av.startswith("https://") or OLD_PLACEHOLDER in av:
            errors.append(f"[{idx}] {name}: bad avatar={av}")
        if not e.get("custom_avatar_regex") or not e.get("avatar_activation_regex"):
            errors.append(f"[{idx}] {name}: missing avatar regex")
        if not c.lstrip().startswith("["):
            errors.append(f"[{idx}] {name}: missing initial bracket block")
        if "BACKSTORY:" not in c:
            errors.append(f"[{idx}] {name}: missing BACKSTORY:")
        if ("FAMILY & PACK:" not in c) and ("CLAN AND COMPANY:" not in c):
            errors.append(f"[{idx}] {name}: missing FAMILY & PACK: / CLAN AND COMPANY:")
        if "VOICE & BEHAVIOR:" not in c:
            errors.append(f"[{idx}] {name}: missing VOICE & BEHAVIOR:")
        if "—" in c or "*" in c or "{{age}}" in c:
            errors.append(f"[{idx}] {name}: formatting violation (em-dash/asterisk/age macro)")
        if re.search(r'(?<!\.)\.\.(?!\.)', c) or '""' in c:
            errors.append(f"[{idx}] {name}: double dot or double quote")
        for k in e.get("keys", []):
            if k.lower().strip() in BROAD_KEYS:
                errors.append(f"[{idx}] {name}: broad key '{k}'")
        if name in CORE_7:
            exp_card = CORE_7[name]
            if exp_card not in (e.get("ignored_characters") or []):
                errors.append(f"[{idx}] {name}: missing ignored_characters {exp_card}")
            if len(c) < 7000:
                errors.append(f"[{idx}] {name}: content too short ({len(c)} chars)")

    print(f"LIVE AUDIT {lb_id} ({data.get('name')}): HTTP {status} | entries={len(lex)} | budget={data.get('token_budget')} | errors={len(errors)}")
    for err in errors:
        print("  ERROR:", err)
    return len(errors)

e1 = audit_live_lorebook("_zwEqgEEzh12X6gHVmMKKC", 99, 7500)
e2 = audit_live_lorebook("_Uht3Ckz44JBDrPnUHq7LV", 211, 5000)

# Also verify covers on the other 4 lorebooks
for lb_id in ["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK"]:
    req = urllib.request.Request(f"https://api.wyvern.chat/lorebooks/{lb_id}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    print(f"LIVE COVER CHECK {lb_id} ({d.get('name')}): photoURL == EMBLEM_URL -> {d.get('photoURL') == EMBLEM_URL}")
