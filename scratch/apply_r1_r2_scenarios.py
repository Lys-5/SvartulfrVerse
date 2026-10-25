import json
import pathlib
import shutil
import urllib.request
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_scenarios_dir = ROOT / 'FINAL' / 'scenarios'
archivio_scenarios_dir = ROOT / 'ARCHIVIO' / 'scenarios'

# 1. Create ARCHIVIO/scenarios/ and move the 4 retired scenarios
archivio_scenarios_dir.mkdir(parents=True, exist_ok=True)
retired_scenarios = [
    'Svartulfr_Scenario_Camp_Mystic.json',
    'Svartulfr_Scenario_DMHA_Dungeons.json',
    'Svartulfr_Scenario_Underworld_Sindacato.json',
    'Svartulfr_Scenario_Villa_Douglas.json'
]

for sc in retired_scenarios:
    src = final_scenarios_dir / sc
    dst = archivio_scenarios_dir / sc
    if src.exists():
        shutil.move(str(src), str(dst))
        print(f"Moved {sc} -> ARCHIVIO/scenarios/")
    else:
        print(f"File {sc} not in FINAL/scenarios/, check ARCHIVIO: {dst.exists()}")

# Verify remaining in FINAL/scenarios/
remaining = [f.name for f in final_scenarios_dir.glob('*.json')]
print(f"Remaining in FINAL/scenarios/: {remaining}")
assert set(remaining) == {'Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'Svartulfr_Scenario_SUCC_Route_Jasper.json'}, f"Unexpected files: {remaining}"

# 2. Update Alyssa Route
alyssa_path = final_scenarios_dir / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'
alyssa_data = json.loads(alyssa_path.read_text(encoding='utf-8'))

# Clean slots
# twin Jasper and crush Mac retained; best_friend, roommate, childhood_friend, quarterback, friend, sports_rival emptied
for slot in alyssa_data.get('slots', []):
    slot['unavailable_count'] = 0
    k = slot.get('key')
    if k in ['best_friend', 'roommate', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']:
        slot['pool'] = []
    elif k == 'twin':
        slot['pool'] = [{'character_id': '_t4J9aQNJM36cUKAP4wB4U', 'weight': 100}]
    elif k == 'crush':
        slot['pool'] = [{'character_id': '_zn24784jfcchQ7EwCyAnm', 'weight': 100}]

# Replace macros in greetings and messages
alyssa_macro_replacements = {
    'best_friend': 'Scarlett Rose',
    'roommate': 'Sierra Cruz',
    'friend': 'Stanley Davies Jr.',
    'quarterback': 'Jared Thompson',
    'childhood_friend': 'Finnegan Novak',
    'sports_rival': 'Vincent Campbell'
}

def replace_macros_in_text(text, mapping):
    for key, repl in mapping.items():
        text = text.replace(f'{{{{scenarioChar "{key}"}}}}', repl)
    return text

for g in alyssa_data.get('greetings', []):
    g['content'] = replace_macros_in_text(g.get('content', ''), alyssa_macro_replacements)
    for m in g.get('messages', []):
        m['content'] = replace_macros_in_text(m.get('content', ''), alyssa_macro_replacements)
    # Enforce invariant: greeting.speaker_slot == messages[0].speaker_slot and greeting.content == messages[0].content
    if g.get('messages'):
        g['speaker_slot'] = g['messages'][0]['speaker_slot']
        g['content'] = g['messages'][0]['content']

# Set live revision 10
alyssa_data['revision'] = 10
alyssa_data['visibility'] = 'private'

alyssa_path.write_text(json.dumps(alyssa_data, indent=2, ensure_ascii=False), encoding='utf-8')
print("Alyssa Route scenario updated locally!")

# 3. Update Jasper Route
jasper_path = final_scenarios_dir / 'Svartulfr_Scenario_SUCC_Route_Jasper.json'
jasper_data = json.loads(jasper_path.read_text(encoding='utf-8'))

# Clean slots: all 8 slots emptied
for slot in jasper_data.get('slots', []):
    slot['unavailable_count'] = 0
    slot['pool'] = []

# Replace macros in greetings and messages
jasper_macro_replacements = {
    'crush': 'Scarlett Rose',
    'male_roommate': 'Russell Sinclair',
    'quarterback': 'Jared Thompson',
    'friend': 'Stanley Davies Jr.',
    'childhood_friend': 'Finnegan Novak',
    'sports_rival': 'Vincent Campbell',
    'twin': 'Alyssa Hvit Douglas Bloodmoon'
}

for g in jasper_data.get('greetings', []):
    g['content'] = replace_macros_in_text(g.get('content', ''), jasper_macro_replacements)
    for m in g.get('messages', []):
        m['content'] = replace_macros_in_text(m.get('content', ''), jasper_macro_replacements)
    # Enforce invariant
    if g.get('messages'):
        g['speaker_slot'] = g['messages'][0]['speaker_slot']
        g['content'] = g['messages'][0]['content']

jasper_data['revision'] = 4
jasper_data['visibility'] = 'private'

jasper_path.write_text(json.dumps(jasper_data, indent=2, ensure_ascii=False), encoding='utf-8')
print("Jasper Route scenario updated locally!")

# Check invariants on both local files
for s_name, s_data in [('Alyssa', alyssa_data), ('Jasper', jasper_data)]:
    for i, g in enumerate(s_data.get('greetings', [])):
        assert g['speaker_slot'] == g['messages'][0]['speaker_slot'], f"{s_name} G{i} speaker_slot mismatch"
        assert g['content'] == g['messages'][0]['content'], f"{s_name} G{i} content mismatch"
        assert '\u2014' not in g['content'], f"{s_name} G{i} em-dash in content"
        for j, m in enumerate(g['messages']):
            assert '\u2014' not in m['content'], f"{s_name} G{i} M{j} em-dash in content"
            # verify no retired macros remain
            for ret in ['best_friend', 'roommate', 'friend', 'quarterback', 'childhood_friend', 'sports_rival', 'male_roommate']:
                assert f'{{{{scenarioChar "{ret}"}}}}' not in m['content'], f"{s_name} G{i} M{j} still has {ret}"
    print(f"All invariants passed for {s_name} Route!")

# 4. Deploy both scenarios via PUT to Wyvern API
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

def deploy_scenario(scenario_id, payload):
    data_bytes = json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(
        f'https://app.wyvern.chat/api/character-scenarios/{scenario_id}',
        data=data_bytes,
        headers=headers,
        method='PUT'
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"PUT {scenario_id} ({payload.get('name')}) -> HTTP {resp.status}, new rev: {res.get('revision')}")
        return res

deploy_scenario('char_scenario_CKgwq246DyCj1NNTBV9rt', alyssa_data)
deploy_scenario('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', jasper_data)

print("\nTask 2 finished successfully!")
