import json
import pathlib
import urllib.request
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ChallengerBot/1.0',
    'Accept': 'application/json'
}

def api_get(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, None

print("=== CHECKING LOCAL VS REMOTE SCENARIOS ===")
status_alyssa, live_alyssa = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt')
status_jasper, live_jasper = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF')

local_alyssa = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
local_jasper = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

print(f"Live Alyssa revision: {live_alyssa.get('revision')}, Local Alyssa revision: {local_alyssa.get('revision')}")
print(f"Live Jasper revision: {live_jasper.get('revision')}, Local Jasper revision: {local_jasper.get('revision')}")

# Check key fields between local and remote
for name, live, local in [('Alyssa', live_alyssa, local_alyssa), ('Jasper', live_jasper, local_jasper)]:
    print(f"\n--- Comparing {name} ---")
    assert live.get('revision') == local.get('revision'), f"{name} revision mismatch!"
    assert len(live.get('slots', [])) == len(local.get('slots', [])), f"{name} slots count mismatch!"
    assert len(live.get('greetings', [])) == len(local.get('greetings', [])), f"{name} greetings count mismatch!"
    assert len(live.get('lorebook_ids', [])) == len(local.get('lorebook_ids', [])), f"{name} lorebook_ids count mismatch!"
    print(f"  Slots: {len(live['slots'])} match.")
    print(f"  Greetings: {len(live['greetings'])} match.")
    print(f"  Lorebook IDs: {len(live['lorebook_ids'])} match.")

    # Greeting by greeting comparison
    for idx, (lg, rg) in enumerate(zip(local['greetings'], live['greetings'])):
        assert lg['speaker_slot'] == rg['speaker_slot'], f"{name} G{idx} speaker_slot mismatch between local and live"
        assert lg['content'] == rg['content'], f"{name} G{idx} content mismatch between local and live"
        assert len(lg['messages']) == len(rg['messages']), f"{name} G{idx} messages count mismatch between local and live"
        for m_idx, (lm, rm) in enumerate(zip(lg['messages'], rg['messages'])):
            assert lm['speaker_slot'] == rm['speaker_slot'], f"{name} G{idx} M{m_idx} speaker_slot mismatch"
            assert lm['content'] == rm['content'], f"{name} G{idx} M{m_idx} content mismatch"
    print(f"  All greetings and messages perfectly identical between local and live!")

print("\n=== DETAIL ON ALYSSA GREETING 0 ===")
g0 = live_alyssa['greetings'][0]
print("Label:", g0.get('label'))
print("Speaker slot:", g0.get('speaker_slot'))
for i, m in enumerate(g0['messages']):
    print(f"Msg {i} [speaker_slot: {m.get('speaker_slot')}]: {m.get('content')[:140]}...")

print("\n=== LOCAL DIRECTORY AUDIT ===")
cards_final = list((ROOT / 'FINAL').glob('*_card.json'))
print(f"Cards in FINAL/: {len(cards_final)} files")
for c in cards_final:
    print(f"  FINAL: {c.name}")
assert len(cards_final) == 8, f"Expected 8 cards in FINAL, got {len(cards_final)}"

cards_legacy = list((ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*_card.json'))
print(f"Cards in ARCHIVIO/cards_legacy/: {len(cards_legacy)} files")
for c in cards_legacy:
    print(f"  ARCHIVIO: {c.name}")
assert len(cards_legacy) == 6, f"Expected 6 cards in ARCHIVIO/cards_legacy, got {len(cards_legacy)}"

scenarios_final = list((ROOT / 'FINAL' / 'scenarios').glob('*.json'))
print(f"Scenarios in FINAL/scenarios/: {len(scenarios_final)} files")
for s in scenarios_final:
    print(f"  FINAL scenario: {s.name}")
assert len(scenarios_final) == 2, f"Expected 2 scenarios in FINAL/scenarios, got {len(scenarios_final)}"

scenarios_arch = list((ROOT / 'ARCHIVIO' / 'scenarios').glob('*.json'))
print(f"Scenarios in ARCHIVIO/scenarios/: {len(scenarios_arch)} files")
for s in scenarios_arch:
    print(f"  ARCHIVIO scenario: {s.name}")
assert len(scenarios_arch) == 4, f"Expected 4 scenarios in ARCHIVIO/scenarios, got {len(scenarios_arch)}"

print("\n=== ALL DIRECTORY AND LIVE COMPARISONS PASSED ===")
