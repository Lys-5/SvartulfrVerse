import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

# 1. Fetch live scenario to get fresh revision
req_get = urllib.request.Request(
    'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4',
    headers=headers
)
with urllib.request.urlopen(req_get) as resp:
    live_data = json.loads(resp.read().decode('utf-8'))

current_rev = live_data.get('revision', 9)
print(f"Current live revision: {current_rev}")

# 2. Load local scenario
p = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.load(p.open(encoding='utf-8'))

# Name, Privacy, Rating, Revision
scen['name'] = 'Svartúlfr — Vita al Campus SUCC & Missioni di Gilda'
scen['visibility'] = 'private'
scen['rating'] = 'explicit'
scen['revision'] = current_rev

# Clean text in scenario
text = scen.get('scenario', '')
text = text.replace('Southern Union Monster College', 'Supernatural University of Central California')
text = text.replace('Solarton University', 'Supernatural University of Central California (SUCC)')

anti_ventriloquism = (
    "\n\n[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:\n"
    "1. Strict Anti-Ventriloquism: Never speak, think, emote, or act for {{user}}. Pause and wait for {{user}}'s input.\n"
    "2. Scene Balancing: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies.\n"
    "3. Format Discipline: Dialogue in quotes (\"...\"), actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only (*...*). Never use the em dash; use commas or periods instead.]"
)

if '[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:' not in text:
    text = text.strip() + anti_ventriloquism

scen['scenario'] = text

# Ensure slot marek is Kakihara's original card
for s in scen.get('slots', []):
    if s['key'] == 'marek':
        s['pool'] = [{'character_id': '_9AycMJGa4fjy6pn6kgxGj', 'weight': 100}]

# Greetings: link both personas and clean text
alyssa_pid = 'persona_1786335754946'
jasper_pid = '1792155173728'
for g in scen.get('greetings', []):
    g['linked_persona_ids'] = [alyssa_pid, jasper_pid]
    if 'content' in g:
        g['content'] = g['content'].replace('Southern Union Monster College', 'Supernatural University of Central California').replace('Solarton University', 'Supernatural University of Central California (SUCC)')
    if 'messages' in g:
        for m in g['messages']:
            if 'content' in m:
                m['content'] = m['content'].replace('Southern Union Monster College', 'Supernatural University of Central California').replace('Solarton University', 'Supernatural University of Central California (SUCC)')

# Save back to FINAL
p.write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
print("Saved cleaned scenario to FINAL/Svartulfr_Master_Scenario.json")

# 3. Deploy via PUT
payload = {
    'name': scen['name'],
    'display_description': scen.get('display_description', ''),
    'avatar': scen.get('avatar', ''),
    'tags': scen.get('tags', []),
    'visibility': scen['visibility'],
    'rating': scen['rating'],
    'revision': scen['revision'],
    'scenario': scen['scenario'],
    'startup_script': scen.get('startup_script', ''),
    'slots': scen['slots'],
    'greetings': scen['greetings'],
    'lorebook_ids': scen.get('lorebook_ids', [])
}

body = json.dumps(payload).encode('utf-8')
req_put = urllib.request.Request(
    'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4',
    data=body,
    headers=headers,
    method='PUT'
)

try:
    with urllib.request.urlopen(req_put) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"Scenario PUT Success! Status: {resp.status}")
        new_rev = res.get('scenario', res).get('revision')
        print(f"New revision: {new_rev}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8')
    print(f"Scenario PUT HTTPError: {e.code} - {err_body}")
except Exception as e:
    print(f"Scenario PUT Error: {e}")
