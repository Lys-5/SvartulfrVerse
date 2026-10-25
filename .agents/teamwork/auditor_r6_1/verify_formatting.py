import json
import re
import os

print("=== CHECK 5: FORMATTING & KEYWORD HYGIENE AUDIT ===")

violations = []

# 1. Em-Dash Audit
files_to_check_emdash = [
    'FINAL/Svartulfr_NPC_Primary.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json',
    'lorebooks/optimized/Svartulfr_NPC_Primary.json'
]

em_dash_char = '\u2014'

for fpath in files_to_check_emdash:
    if not os.path.exists(fpath):
        violations.append(f"File missing for em-dash check: {fpath}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    count = text.count(em_dash_char)
    print(f"Em-dash check in {fpath}: {count} occurrences found")
    if count > 0:
        violations.append(f"Em-dash violation: {count} em-dashes found in {fpath}")

# Check CHANGELOG.md recent entries for em-dashes
if os.path.exists('CHANGELOG.md'):
    with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
        cl_text = f.read()
    # Check lines after the latest section header
    latest_section = cl_text.split('## [')[1] if '## [' in cl_text else cl_text
    # Grab the top entry
    top_entry = latest_section.split('## [')[0] if '## [' in latest_section else latest_section
    cl_emdash_count = top_entry.count(em_dash_char)
    print(f"Em-dash check in latest CHANGELOG.md entry: {cl_emdash_count} occurrences found")
    if cl_emdash_count > 0:
        violations.append(f"Em-dash violation in CHANGELOG.md latest entry: {cl_emdash_count} found")

# 2. Action Asterisks in Greetings
scenario_files = [
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json'
]

for sf in scenario_files:
    with open(sf, 'r', encoding='utf-8') as f:
        sdata = json.load(f)
    greetings = sdata.get('greetings', [])
    for gi, g in enumerate(greetings):
        msgs = g.get('messages', [])
        # Check greeting level content
        g_content = g.get('content', '')
        if '*' in g_content:
            violations.append(f"Asterisk in greeting {gi} content of {sf}")
        for mi, m in enumerate(msgs):
            m_content = m.get('content', '')
            if '*' in m_content:
                violations.append(f"Asterisk in greeting {gi} msg {mi} of {sf}")
            # Check for orphan {{scenarioChar macros
            if '{{scenarioChar' in m_content:
                violations.append(f"Orphan macro {{scenarioChar in greeting {gi} msg {mi} of {sf}: {m_content[:60]}")
    print(f"Asterisk & macro check in {sf}: {len(greetings)} greetings checked cleanly")

# 3. Umbrella Keywords (BROAD_KEYS) in NPC entries
BROAD_KEYS = {
    'solarton', 'succ', 'blackwood', 'vampire', 'werewolf',
    'college', 'student', 'alpha', 'omega'
}

def check_umbrella_keys(lb_path):
    with open(lb_path, 'r', encoding='utf-8') as f:
        lb = json.load(f)
    entries = lb.get('entries', [])
    flagged = []
    for e in entries:
        e_type = e.get('type')
        if e_type == 'npc':
            keys = [k.strip().lower() for k in e.get('keys', [])]
            for bk in BROAD_KEYS:
                if bk in keys:
                    flagged.append((e.get('name'), bk))
    return flagged

flagged_primary = check_umbrella_keys('FINAL/Svartulfr_NPC_Primary.json')
print(f"Umbrella keywords on NPCs in Svartulfr_NPC_Primary.json: {len(flagged_primary)} found")
for name, bk in flagged_primary:
    violations.append(f"Umbrella key violation in Primary: NPC '{name}' has broad key '{bk}'")

flagged_secondary = check_umbrella_keys('FINAL/Svartulfr_NPC_Secondary.json')
print(f"Umbrella keywords on NPCs in Svartulfr_NPC_Secondary.json: {len(flagged_secondary)} found")
for name, bk in flagged_secondary:
    violations.append(f"Umbrella key violation in Secondary: NPC '{name}' has broad key '{bk}'")

# 4. File counts check
final_cards = [f for f in os.listdir('FINAL') if f.endswith('_card.json')]
legacy_cards = [f for f in os.listdir('ARCHIVIO/cards_legacy') if f.endswith('_card.json')]
final_scenarios = [f for f in os.listdir('FINAL/scenarios') if f.endswith('.json')]
legacy_scenarios = [f for f in os.listdir('ARCHIVIO/scenarios') if f.endswith('.json')]

print(f"\nFile Counts Check:")
print(f"  FINAL cards: {len(final_cards)} (Expected 8)")
print(f"  ARCHIVIO legacy cards: {len(legacy_cards)} (Expected 6)")
print(f"  FINAL scenarios: {len(final_scenarios)} (Expected 2)")
print(f"  ARCHIVIO legacy scenarios: {len(legacy_scenarios)} (Expected 4)")

if len(final_cards) != 8:
    violations.append(f"FINAL cards count is {len(final_cards)}, expected 8")
if len(legacy_cards) != 6:
    violations.append(f"ARCHIVIO legacy cards count is {len(legacy_cards)}, expected 6")
if len(final_scenarios) != 2:
    violations.append(f"FINAL scenarios count is {len(final_scenarios)}, expected 2")
if len(legacy_scenarios) != 4:
    violations.append(f"ARCHIVIO legacy scenarios count is {len(legacy_scenarios)}, expected 4")

print(f"\nFinal Check 5 Result: {'ALL FORMATTING & HYGIENE CHECKS PASSED' if len(violations) == 0 else 'VIOLATIONS FOUND: ' + str(violations)}")
