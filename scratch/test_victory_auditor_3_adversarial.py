import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

print("ADVERSARIAL STRESS TEST — Victory Auditor 3")

alyssa_data = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
jasper_data = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

# Inspect greetings specifically for macros
alyssa_greetings_str = json.dumps(alyssa_data.get('greetings', []))
alyssa_greeting_macros = set(re.findall(r'\{\{scenarioChar [^\}]+\}\}', alyssa_greetings_str))
print("Alyssa Route GREETINGS scenarioChar macros found:", alyssa_greeting_macros)
# In Alyssa route greetings, only twin (Jasper) and crush (Mac) are active cards!
for m in alyssa_greeting_macros:
    assert m in ['{{scenarioChar \\"twin\\"}}', '{{scenarioChar \\"crush\\"}}'], f"Unexpected macro in Alyssa greetings: {m}"

jasper_greetings_str = json.dumps(jasper_data.get('greetings', []))
jasper_greeting_macros = set(re.findall(r'\{\{scenarioChar [^\}]+\}\}', jasper_greetings_str))
print("Jasper Route GREETINGS scenarioChar macros found:", jasper_greeting_macros)
assert len(jasper_greeting_macros) == 0, f"Unexpected macros in Jasper Route greetings: {jasper_greeting_macros}"

# Inspect scenario overview field
print("Alyssa scenario overview field macros:", set(re.findall(r'\{\{scenarioChar [^\}]+\}\}', alyssa_data.get('scenario', ''))))
print("Jasper scenario overview field macros:", set(re.findall(r'\{\{scenarioChar [^\}]+\}\}', jasper_data.get('scenario', ''))))

# Check for residual {{age}} macros across all Lorebooks
for lb_path in (ROOT / 'FINAL').glob('Svartulfr_*.json'):
    content = lb_path.read_text(encoding='utf-8')
    age_matches = re.findall(r'\{\{age[^\}]*\}\}', content)
    assert len(age_matches) == 0, f"Found {{age}} macros in {lb_path.name}: {age_matches}"
print("Zero {{age}} macros across all FINAL Lorebooks.")

# Check the 6 NPC entries in Svartulfr_NPC_Primary.json
primary_data = json.loads((ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
lex = primary_data['lexicon']
target_ids = {
    '4NzXF4_0hYxmN7Idltzpw': 'Scarlett Rose',
    'ijy8vrlphNv19-p-gbYuY': 'Sierra Cruz',
    'YCxAqNoShpefVvk0_Pc7i': "Russell 'Russ' Sinclair",
    'ekdQjq63xP7HtNuaPQJQE': 'Stanley Davies Jr.',
    'RM6rcwv8MlY1XWaCTQp0M': 'Jared Thompson',
    'alyssa_world_dossier_2b54a223': 'Alyssa Hvit Douglas Bloodmoon'
}
for eid, name in target_ids.items():
    entry = next(e for e in lex if e.get('entry_id') == eid)
    content = entry['content']
    assert 'BACKSTORY:' in content, f"{name} missing BACKSTORY:"
    assert 'VOICE & BEHAVIOR:' in content or 'VOICE & MANNERISMS:' in content or 'BEHAVIOR:' in content, f"{name} missing VOICE section"
    assert len(content) > 2000, f"{name} description too short ({len(content)})"
    assert entry.get('selective') is False, f"{name} selective should be False under native suppression"
    print(f"[VERIFIED] {name}: {len(content)} chars, selective=False, ignored_chars={entry.get('ignored_characters')}, ignored_personas={entry.get('ignored_personas')}")

# Check 8 approved cards in FINAL
cards = list((ROOT / 'FINAL').glob('*_card.json'))
print(f"Verified {len(cards)} cards in FINAL:")
for c in sorted(cards):
    c_json = json.loads(c.read_text(encoding='utf-8'))
    char_name = c_json.get('name') or c_json.get('data', {}).get('name')
    print(f"  - {c.name}: {char_name}")
assert len(cards) == 8, f"Expected 8 cards in FINAL, found {len(cards)}"

# Check 6 archived cards in ARCHIVIO/cards_legacy
legacy_cards = list((ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*.json'))
print(f"Verified {len(legacy_cards)} cards in ARCHIVIO/cards_legacy:")
for c in sorted(legacy_cards):
    print(f"  - {c.name}")
assert len(legacy_cards) == 6, f"Expected 6 legacy cards, found {len(legacy_cards)}"

print("ADVERSARIAL STRESS TEST COMPLETE: 100% PASSED.")
