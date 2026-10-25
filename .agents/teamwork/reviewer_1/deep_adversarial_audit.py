import json
import requests
from pathlib import Path

ROOT = Path(r"e:\repository\SvartulfrVerse")
WT_PATH = ROOT / "scratch" / "wyvern_token.txt"
token = WT_PATH.read_text(encoding="utf-8").strip()
headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "AuditorBot/1.0"
}

TARGET_CHARACTERS = [
    {
        "name": "Edric Douglas",
        "cid": "_TbRM3EdxDjHFgqztTbCpL",
        "file": "FINAL/Edric_Douglas_card.json",
        "lb_id": "_Uht3Ckz44JBDrPnUHq7LV",
        "lb_name": "Secondary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public"
    },
    {
        "name": "Erik Ulfr Douglas",
        "cid": "_QPea6g4Q1QfeYCVHCLMPR",
        "file": "FINAL/Erik_Douglas_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public"
    },
    {
        "name": "Jasper Svartr Douglas Bloodmoon",
        "cid": "_t4J9aQNJM36cUKAP4wB4U",
        "file": "FINAL/Jasper_Douglas_Bloodmoon_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public"
    },
    {
        "name": "Logan Járn Douglas",
        "cid": "_T8Ywcr9FEqNf9JxbK6eHP",
        "file": "FINAL/Logan_Douglas_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public"
    },
    {
        "name": "Mackenzie Sanchez-Rogers",
        "cid": "_zn24784jfcchQ7EwCyAnm",
        "file": "FINAL/Mackenzie_Sanchez_Rogers_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public"
    },
    {
        "name": "Malachia Björn Douglas Bloodmoon",
        "cid": "_RDfz7XzTpM23LpPALVXHM",
        "file": "FINAL/Malachia_Douglas_Bloodmoon_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public"
    },
    {
        "name": "Noah Loki Douglas Bloodmoon",
        "cid": "_zFLUjV8aVxQRAfQxGcAcY",
        "file": "FINAL/Noah_Douglas_Bloodmoon_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public"
    },
    {
        "name": "Wulfnic Bóleygr Bloodmoon",
        "cid": "_HEQQbbRFwKdG8QE2Fh1z1",
        "file": "FINAL/Wulfnic_Bloodmoon_card.json",
        "lb_id": "_zwEqgEEzh12X6gHVmMKKC",
        "lb_name": "Primary",
        "expected_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public"
    }
]

print("=" * 80)
print("DEEP ADVERSARIAL AUDIT - INDEPENDENT VERIFICATION")
print("=" * 80)

# Fetch mine
r_mine = requests.get("https://app.wyvern.chat/api/characters/mine", headers=headers)
assert r_mine.status_code == 200, f"Failed /api/characters/mine: {r_mine.status_code}"
mine_chars = {c["id"]: c for c in r_mine.json().get("characters", [])}
print(f"Total active characters in /characters/mine: {len(mine_chars)}")
assert len(mine_chars) == 8, f"Expected 8 characters, found {len(mine_chars)}"

# Fetch Live Lorebooks
r_prim = requests.get("https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC", headers=headers)
assert r_prim.status_code == 200, f"Failed Live LB Primary: {r_prim.status_code}"
live_lb_prim = r_prim.json()

r_sec = requests.get("https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV", headers=headers)
assert r_sec.status_code == 200, f"Failed Live LB Secondary: {r_sec.status_code}"
live_lb_sec = r_sec.json()

# Load Local Lorebooks
with open(ROOT / "FINAL" / "Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    local_lb_prim = json.load(f)
with open(ROOT / "FINAL" / "Svartulfr_NPC_Secondary.json", "r", encoding="utf-8") as f:
    local_lb_sec = json.load(f)

# Audit each target character
failures = []
for tc in TARGET_CHARACTERS:
    name = tc["name"]
    cid = tc["cid"]
    cfile = ROOT / tc["file"]
    lb_live = live_lb_prim if tc["lb_name"] == "Primary" else live_lb_sec
    lb_local = local_lb_prim if tc["lb_name"] == "Primary" else local_lb_sec

    print(f"\n--- Auditing: {name} ({cid}) ---")

    # 1. Local Card checks
    if not cfile.exists():
        failures.append(f"Local file missing: {cfile}")
        continue
    with open(cfile, "r", encoding="utf-8") as f:
        loc_card = json.load(f)

    loc_desc = loc_card.get("description", "")
    loc_avatar = loc_card.get("avatar", "")
    loc_outfits = loc_card.get("outfits", [])

    print(f"  Local Card: desc_len={len(loc_desc)}, avatar={loc_avatar}, outfits={len(loc_outfits)}")
    if loc_avatar != tc["expected_avatar"]:
        failures.append(f"{name} local avatar mismatch: {loc_avatar} != {tc['expected_avatar']}")
    if len(loc_outfits) < 9:
        failures.append(f"{name} has fewer than 9 outfits: {len(loc_outfits)}")
    if "—" in loc_desc:
        failures.append(f"{name} local description contains forbidden em-dash ('—')")

    # 2. Remote Card checks
    if cid not in mine_chars:
        failures.append(f"{name} ({cid}) NOT in /characters/mine!")
        continue
    rem_card = mine_chars[cid]
    rem_desc = rem_card.get("description", "")
    rem_avatar = rem_card.get("avatar", "")

    print(f"  Remote Card: desc_len={len(rem_desc)}, avatar={rem_avatar}")
    if rem_avatar != tc["expected_avatar"]:
        failures.append(f"{name} remote avatar mismatch: {rem_avatar} != {tc['expected_avatar']}")
    if rem_desc != loc_desc:
        failures.append(f"{name} local vs remote card description mismatch (diff={len(rem_desc) - len(loc_desc)})")

    # 3. Local Lorebook entry checks
    found_local_entry = None
    for e in lb_local.get("lexicon", []):
        if cid in e.get("ignored_characters", []) or e.get("name") == name:
            found_local_entry = e
            break
    if not found_local_entry:
        failures.append(f"{name} entry not found in local {tc['lb_name']}")
    else:
        e_desc = found_local_entry.get("content", "")
        e_avatar = found_local_entry.get("avatar", "")
        e_ignored = found_local_entry.get("ignored_characters", [])
        if e_desc != loc_desc:
            failures.append(f"{name} local entry content != card description (diff={len(e_desc) - len(loc_desc)})")
        if e_avatar != tc["expected_avatar"]:
            failures.append(f"{name} local entry avatar mismatch: {e_avatar} != {tc['expected_avatar']}")
        if cid not in e_ignored:
            failures.append(f"{name} local entry ignored_characters missing {cid}: {e_ignored}")
        if "—" in e_desc:
            failures.append(f"{name} local entry content contains forbidden em-dash ('—')")

    # 4. Live Lorebook entry checks
    found_live_entry = None
    for e in lb_live.get("lexicon", []):
        if cid in e.get("ignored_characters", []) or e.get("name") == name:
            found_live_entry = e
            break
    if not found_live_entry:
        failures.append(f"{name} entry not found in LIVE {tc['lb_name']}")
    else:
        live_e_desc = found_live_entry.get("content", "")
        live_e_avatar = found_live_entry.get("avatar", "")
        live_e_ignored = found_live_entry.get("ignored_characters", [])
        live_e_personas = found_live_entry.get("ignored_personas", [])
        if live_e_desc != rem_desc:
            failures.append(f"{name} LIVE entry content != LIVE card description (diff={len(live_e_desc) - len(rem_desc)})")
        if live_e_avatar != tc["expected_avatar"]:
            failures.append(f"{name} LIVE entry avatar mismatch: {live_e_avatar} != {tc['expected_avatar']}")
        if cid not in live_e_ignored:
            failures.append(f"{name} LIVE entry ignored_characters missing {cid}: {live_e_ignored}")
        if name == "Jasper Svartr Douglas Bloodmoon":
            if "1792155173728" not in live_e_personas:
                failures.append("Jasper LIVE entry missing Jasper persona in ignored_personas!")

# 5. Check Memory entries in LB1 and LB2
print("\n--- Auditing Memory entries in Lorebook I & II ---")
for lb_fname, lbid in [("Svartulfr_Lorebook_I.json", "_gwwCxCfQ6PQaLEjAQVpJL"), ("Svartulfr_Lorebook_II.json", "_HfG7TeV6MJyj6bxMwxkpt")]:
    with open(ROOT / "FINAL" / lb_fname, "r", encoding="utf-8") as f:
        loc_lb = json.load(f)
    r_live = requests.get(f"https://app.wyvern.chat/api/lorebooks/{lbid}", headers=headers)
    assert r_live.status_code == 200, f"Failed {lb_fname} live GET: {r_live.status_code}"
    live_lb = r_live.json()

    # Local check
    memories_local = [e for e in loc_lb.get("lexicon", []) if e.get("type") == "memory"]
    print(f"Local {lb_fname}: {len(memories_local)} memory entries")
    for m in memories_local:
        ign = m.get("ignored_characters", [])
        if ign:
            failures.append(f"Local {lb_fname} memory '{m.get('name')}' has non-empty ignored_characters: {ign}")

    # Live check
    memories_live = [e for e in live_lb.get("lexicon", []) if e.get("type") == "memory"]
    print(f"Live {lb_fname}: {len(memories_live)} memory entries")
    for m in memories_live:
        ign = m.get("ignored_characters", [])
        if ign:
            failures.append(f"Live {lb_fname} memory '{m.get('name')}' has non-empty ignored_characters: {ign}")

# 6. Check Zod Parity: entries == lexicon in all files
print("\n--- Auditing entries == lexicon parity in all local files ---")
for fpath in [
    ROOT / "FINAL" / "Svartulfr_NPC_Primary.json",
    ROOT / "FINAL" / "Svartulfr_NPC_Secondary.json",
    ROOT / "lorebooks" / "optimized" / "Svartulfr_NPC_Primary.json",
    ROOT / "lorebooks" / "optimized" / "Svartulfr_NPC_Secondary.json",
]:
    with open(fpath, "r", encoding="utf-8") as f:
        d = json.load(f)
    e_str = json.dumps(d.get("entries", []), sort_keys=True)
    l_str = json.dumps(d.get("lexicon", []), sort_keys=True)
    if e_str != l_str:
        failures.append(f"entries != lexicon in {fpath.name} (len diff: {len(e_str)} vs {len(l_str)})")
    else:
        print(f"  Parity OK: {fpath.name}")

print("\n" + "=" * 80)
if failures:
    print(f"AUDIT FAILED WITH {len(failures)} DEFECT(S):")
    for idx, fail in enumerate(failures, 1):
        print(f"  [{idx}] {fail}")
    exit(1)
else:
    print("ALL 6 AUDIT PHASES PASSED WITH ZERO DEFECTS (100% SUCCESS)!")
    print("=" * 80)
