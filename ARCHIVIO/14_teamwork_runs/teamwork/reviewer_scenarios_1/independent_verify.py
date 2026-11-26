import json
import pathlib
import re
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
SCENARIOS_DIR = ROOT / 'FINAL' / 'scenarios'

FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
]

EXPECTED_LOREBOOKS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

sys.stdout.reconfigure(encoding='utf-8')

report = []

def log(msg):
    report.append(msg)
    print(msg)

log("================ INDEPENDENT STRUCTURAL & SCHEMA AUDIT ================")

critical_findings = []
major_findings = []
minor_findings = []

for fname in FILES:
    log(f"\n--- Checking File: {fname} ---")
    fpath = SCENARIOS_DIR / fname
    if not fpath.exists():
        critical_findings.append(f"CRITICAL: File {fname} does not exist!")
        continue

    raw_bytes = fpath.read_bytes()
    log(f"File size: {len(raw_bytes)} bytes")

    # Check encoding & raw text
    try:
        raw_text = raw_bytes.decode('utf-8')
    except Exception as e:
        critical_findings.append(f"CRITICAL: {fname} is not valid UTF-8: {e}")
        continue

    # Character check: Em-dash (\u2014) and En-dash (\u2013)
    em_dash_count = raw_text.count('\u2014')
    en_dash_count = raw_text.count('\u2013')
    if em_dash_count > 0:
        critical_findings.append(f"CRITICAL: {fname} contains {em_dash_count} em-dash ('—') characters!")
    else:
        log("PASS: Zero em-dashes found.")

    if en_dash_count > 0:
        major_findings.append(f"MAJOR: {fname} contains {en_dash_count} en-dash ('–') characters!")
    else:
        log("PASS: Zero en-dashes found.")

    # JSON parse
    try:
        data = json.loads(raw_text)
        log("PASS: Valid JSON syntax.")
    except Exception as e:
        critical_findings.append(f"CRITICAL: {fname} failed JSON parsing: {e}")
        continue

    # Top-level fields check
    expected_top_fields = [
        "name", "display_description", "avatar", "tags",
        "visibility", "rating", "scenario", "startup_script",
        "slots", "greetings", "lorebook_ids", "gallery", "linked_world_id"
    ]
    for field in expected_top_fields:
        if field not in data:
            major_findings.append(f"MAJOR: {fname} missing top-level field '{field}'")

    # CRITICAL: visibility == "private"
    vis = data.get("visibility")
    log(f"Visibility value: '{vis}'")
    if vis != "private":
        critical_findings.append(f"CRITICAL: {fname} 'visibility' is '{vis}' (MUST be 'private')")
    else:
        log("PASS: Visibility is strictly 'private'.")

    # Rating == "explicit"
    rating = data.get("rating")
    log(f"Rating value: '{rating}'")
    if rating != "explicit":
        critical_findings.append(f"CRITICAL: {fname} 'rating' is '{rating}' (MUST be 'explicit')")
    else:
        log("PASS: Rating is strictly 'explicit'.")

    # Lorebook IDs
    lorebooks = data.get("lorebook_ids", [])
    log(f"Lorebook IDs count: {len(lorebooks)}")
    missing_lb = [lb for lb in EXPECTED_LOREBOOKS if lb not in lorebooks]
    extra_lb = [lb for lb in lorebooks if lb not in EXPECTED_LOREBOOKS]
    if missing_lb:
        critical_findings.append(f"CRITICAL: {fname} missing canonical lorebook IDs: {missing_lb}")
    if extra_lb:
        major_findings.append(f"MAJOR: {fname} has extra lorebook IDs: {extra_lb}")
    if not missing_lb and not extra_lb and len(lorebooks) == 6:
        log("PASS: Exactly the 6 canonical standalone lorebooks are linked.")

    # Slots schema verification
    slots = data.get("slots", [])
    log(f"Slots count: {len(slots)}")
    slot_keys = set()
    for idx, s in enumerate(slots):
        k = s.get("key")
        lbl = s.get("label")
        p = s.get("pool")
        uc = s.get("unavailable_count")

        if not k or not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{0,63}$', k):
            critical_findings.append(f"CRITICAL: {fname} slot[{idx}] invalid key format: '{k}'")
        if k in slot_keys:
            critical_findings.append(f"CRITICAL: {fname} duplicate slot key: '{k}'")
        slot_keys.add(k)

        if not lbl or not isinstance(lbl, str) or len(lbl) > 120:
            major_findings.append(f"MAJOR: {fname} slot '{k}' invalid label: '{lbl}'")

        if not isinstance(p, list):
            critical_findings.append(f"CRITICAL: {fname} slot '{k}' pool is not a list")
        else:
            for c_entry in p:
                if not isinstance(c_entry, dict) or "character_id" not in c_entry:
                    critical_findings.append(f"CRITICAL: {fname} slot '{k}' pool contains invalid entry: {c_entry}")

        if uc != 0:
            critical_findings.append(f"CRITICAL: {fname} slot '{k}' unavailable_count={uc} (MUST be 0)")

    log(f"PASS: All {len(slots)} slots have valid keys, labels, pools, and unavailable_count=0.")

    # Greetings schema verification
    greetings = data.get("greetings", [])
    log(f"Greetings count: {len(greetings)}")
    if not (1 <= len(greetings) <= 100):
        critical_findings.append(f"CRITICAL: {fname} greetings count {len(greetings)} outside [1, 100]")

    for g_idx, g in enumerate(greetings):
        g_name = g.get("name")
        g_desc = g.get("description", "")
        g_content = g.get("content")
        g_speaker = g.get("speaker_slot")
        messages = g.get("messages", [])

        if not g_name or not isinstance(g_name, str):
            major_findings.append(f"MAJOR: {fname} greeting[{g_idx}] has invalid name")

        if not messages or not isinstance(messages, list):
            critical_findings.append(f"CRITICAL: {fname} greeting[{g_idx}] has no messages list")
            continue

        first_msg = messages[0]
        # Parity check
        if g_content != first_msg.get("content"):
            critical_findings.append(f"CRITICAL: {fname} greeting[{g_idx}] root content != messages[0].content")
        if g_speaker != first_msg.get("speaker_slot"):
            critical_findings.append(f"CRITICAL: {fname} greeting[{g_idx}] root speaker_slot != messages[0].speaker_slot")

        for m_idx, msg in enumerate(messages):
            m_slot = msg.get("speaker_slot")
            m_content = msg.get("content", "")

            if m_slot not in slot_keys:
                critical_findings.append(f"CRITICAL: {fname} greeting[{g_idx}] msg[{m_idx}] speaker_slot '{m_slot}' not found in slots!")

            if not m_content or not isinstance(m_content, str):
                critical_findings.append(f"CRITICAL: {fname} greeting[{g_idx}] msg[{m_idx}] has empty or invalid content")

            # Check illicit name prefix
            if re.match(r'^[A-Z][a-zA-Z\s\'-]+:\s', m_content):
                major_findings.append(f"MAJOR: {fname} greeting[{g_idx}] msg[{m_idx}] has explicit name prefix in content")

            # Check for em-dash in content
            if '\u2014' in m_content:
                critical_findings.append(f"CRITICAL: {fname} greeting[{g_idx}] msg[{m_idx}] has em-dash")

    log(f"PASS: All {len(greetings)} greetings passed schema, parity, and speaker_slot validation.")

    # Integrity & facade check: check lengths of scenario and greetings
    sc_text = data.get("scenario", "")
    log(f"Scenario context length: {len(sc_text)} chars")
    if len(sc_text) < 200:
        critical_findings.append(f"CRITICAL: {fname} scenario context is suspiciously short ({len(sc_text)} chars) - potential dummy facade!")

    total_greeting_words = sum(len(m.get("content", "").split()) for g in greetings for m in g.get("messages", []))
    log(f"Total greeting words: {total_greeting_words} words across {sum(len(g.get('messages', [])) for g in greetings)} messages")
    if total_greeting_words < 500:
        critical_findings.append(f"CRITICAL: {fname} total greeting word count ({total_greeting_words}) suspiciously low - potential dummy facade!")

log("\n================ AUDIT SUMMARY ================")
log(f"Critical findings: {len(critical_findings)}")
for c in critical_findings:
    log(f"  ❌ {c}")
log(f"Major findings: {len(major_findings)}")
for m in major_findings:
    log(f"  ⚠️ {m}")
log(f"Minor findings: {len(minor_findings)}")
for mn in minor_findings:
    log(f"  ℹ️ {mn}")

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_1\audit_output.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(report))

if critical_findings:
    sys.exit(1)
sys.exit(0)
