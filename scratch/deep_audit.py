import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'

print("=== A. MASTER SCENARIO DEEP AUDIT ===")
scen = json.loads((FINAL / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8'))
import urllib.request
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
req = urllib.request.Request(
    'https://api.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4',
    headers={'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(req, timeout=30) as resp:
    live_scen = json.loads(resp.read().decode('utf-8'))

print("Top-level keys in FINAL/Svartulfr_Master_Scenario.json:", list(scen.keys()))
print("Top-level keys in live_scen:", list(live_scen.keys()))
print("Does FINAL have 'personas'?", 'personas' in scen, "Does live have 'personas'?", 'personas' in live_scen)
if 'personas' in live_scen:
    print("live personas:", [p.get('id') if isinstance(p, dict) else p for p in live_scen['personas']])
if 'persona_ids' in live_scen:
    print("live persona_ids:", live_scen['persona_ids'])

for k in ['name', 'display_description', 'description', 'scenario', 'first_mes']:
    val = scen.get(k, '')
    if isinstance(val, str):
        if '*' in val:
            print(f"WARNING: '*' found in Master Scenario.{k}!")
        if '—' in val:
            print(f"WARNING: '—' found in Master Scenario.{k}!")
        if 'Southern Union Monster College' in val:
            print(f"WARNING: 'Southern Union Monster College' found in Master Scenario.{k}!")
        if '{{user}}' in val and k not in ('description', 'scenario', 'first_mes'):
            print(f"INFO: '{{user}}' in Master Scenario.{k}")

print("first_mes matches greetings[0].content?", scen.get('first_mes') == scen['greetings'][0]['content'])
print("alternate_greetings count:", len(scen.get('alternate_greetings', [])))
if 'alternate_greetings' in scen:
    ag = scen['alternate_greetings']
    g_contents = [g['content'] for g in scen['greetings'][1:]]
    print("alternate_greetings matches greetings[1:].content?", ag == g_contents)

# Check NPC regexes in NPC Primary & Secondary against all NPC prefixes used in the 29 greetings
npc_p = json.loads((FINAL / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))
npc_s = json.loads((FINAL / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))
all_npcs = [e for e in npc_p['entries'] + npc_s['entries'] if e.get('type') == 'npc']

prefixes_to_test = [
    "Zeera Darkfire:",
    "Santiago Herrera:",
    "Coach D:",
    "Roman Blackwood:",
    "Kolya Varenkov:",
    "Neon Purr:",
    "Elizabeth Duskwood:",
    "Magnus Douglas III:",
    "Kaladin Nargathon:",
    "Marek:"
]

print("\n=== B. TESTING NPC PREFIXES AGAINST AVATAR_ACTIVATION_REGEX ===")
for pref in prefixes_to_test:
    matched = []
    for e in all_npcs:
        rx = e.get('avatar_activation_regex', '')
        if rx:
            try:
                if re.search(rx, "\n" + pref + " \"Ciao\""):
                    matched.append((e['name'], rx))
            except Exception as ex:
                print(f"Regex error on {e['name']}: {ex}")
    print(f"Prefix '{pref}' -> matched NPCs: {matched}")

# Also scan all 29 greetings for any `Name:` at start of line
print("\n=== C. SCANNING ALL 29 GREETINGS FOR COLON-PREFIXED LINES ===")
for idx, g in enumerate(scen['greetings'], 1):
    for m_idx, m in enumerate(g.get('messages', [])):
        for line in m['content'].split('\n'):
            m_col = re.match(r'^\s*([A-Z][A-Za-z0-9\s\.\'\-]+):', line)
            if m_col:
                speaker_prefix = m_col.group(0).strip()
                # Check if it matches any NPC regex
                hits = [e['name'] for e in all_npcs if e.get('avatar_activation_regex') and re.search(e['avatar_activation_regex'], "\n" + line)]
                print(f"G{idx:02d} msg[{m_idx}] prefix '{speaker_prefix}' -> regex hits: {hits}")

# Check Camp Mystic in Lorebook III and Location
print("\n=== D. CHECKING CAMP MYSTIC IN LOREBOOK III AND LOCATION ===")
for fn in ['Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json']:
    lb = json.loads((FINAL / fn).read_text(encoding='utf-8'))
    hits = [e['name'] for e in lb['entries'] if 'mystic' in e.get('name', '').lower() or 'mystic' in e.get('content', '').lower() or any('mystic' in k.lower() for k in e.get('keys', []))]
    print(f"{fn} Camp Mystic hits:", hits)

# Check card.json from Downloads
card_dl = pathlib.Path(r'c:\Users\mande\Downloads\[WyvernChat] ✨️Camp Mystic✨️\card.json')
print("Camp Mystic card.json exists?", card_dl.exists())
