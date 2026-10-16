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

# 1. Fetch live scenario
req_get = urllib.request.Request(
    'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4',
    headers=headers
)
with urllib.request.urlopen(req_get) as resp:
    live = json.loads(resp.read().decode('utf-8'))

rev = live.get('revision', 10)
print(f"Current live revision: {rev}")

# 2. Build 13 role-based slots
slots = [
    {
        "key": "maternal_grandfather",
        "label": "Maternal Grandfather",
        "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}]
    },
    {
        "key": "paternal_grandfather",
        "label": "Paternal Grandfather",
        "pool": [{"character_id": "_dJ7nRMQEbcUgdWG96MqLz", "weight": 100}]
    },
    {
        "key": "paternal_grandmother",
        "label": "Paternal Grandmother",
        "pool": [{"character_id": "_zBD6rWUkJBAjLfXnja4xh", "weight": 100}]
    },
    {
        "key": "father",
        "label": "Father",
        "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}]
    },
    {
        "key": "twin",
        "label": "Twin",
        "pool": [
            {"character_id": "_t4J9aQNJM36cUKAP4wB4U", "weight": 100},
            {"character_id": "_6exg3yPfe2eCDK4hTftkh", "weight": 100}
        ]
    },
    {
        "key": "brother",
        "label": "Brother",
        "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}]
    },
    {
        "key": "eldest_brother",
        "label": "Eldest Brother",
        "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}]
    },
    {
        "key": "uncle",
        "label": "Uncle",
        "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}]
    },
    {
        "key": "cousin",
        "label": "Cousin",
        "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}]
    },
    {
        "key": "boss",
        "label": "Boss",
        "pool": [{"character_id": "_3tMk6cRAFewRnKMkdJ4XU", "weight": 100}]
    },
    {
        "key": "quarterback",
        "label": "Quarterback",
        "pool": [{"character_id": "_xJVPtBLL3dxy69RLKL9X9", "weight": 100}]
    },
    {
        "key": "crush",
        "label": "Crush",
        "pool": [{"character_id": "_zn24784jfcchQ7EwCyAnm", "weight": 100}]
    },
    {
        "key": "major",
        "label": "Major",
        "pool": [{"character_id": "_EnRGd1jfbjTTGmz4EFJdd", "weight": 100}]
    }
]

slot_key_map = {
    'grandfather': 'maternal_grandfather',
    'magnus': 'paternal_grandfather',
    'elizabeth': 'paternal_grandmother',
    'zeera': 'boss',
    'jared': 'quarterback',
    'mac': 'crush',
    'kaladin': 'major',
    'marek': 'twin'
}

# 3. Load local scenario
p = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.load(p.open(encoding='utf-8'))

scen['name'] = 'Svartúlfr — Vita al Campus SUCC & Missioni di Gilda'
scen['visibility'] = 'private'
scen['rating'] = 'explicit'
scen['revision'] = rev
scen['slots'] = slots

# Remap macros in scenario text
s_text = scen.get('scenario', '')
for old_k, new_k in slot_key_map.items():
    s_text = s_text.replace(f'{{{{scenarioChar "{old_k}"}}}}', f'{{{{scenarioChar "{new_k}"}}}}')

s_text = s_text.replace('Southern Union Monster College', 'Supernatural University of Central California')
s_text = s_text.replace('Solarton University', 'Supernatural University of Central California (SUCC)')

anti_ventriloquism = (
    "\n\n[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:\n"
    "1. Strict Anti-Ventriloquism: Never speak, think, emote, or act for {{user}}. Pause and wait for {{user}}'s input.\n"
    "2. Scene Balancing: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies.\n"
    "3. Format Discipline: Dialogue in quotes (\"...\"), actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only (*...*). Never use the em dash; use commas or periods instead.]"
)

if '[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:' not in s_text:
    s_text = s_text.strip() + anti_ventriloquism

scen['scenario'] = s_text

# 4. Remap greetings
alyssa_pid = 'persona_1786335754946'
jasper_pid = '1792155173728'

for i, g in enumerate(scen.get('greetings', [])):
    g['linked_persona_ids'] = [alyssa_pid, jasper_pid]
    
    # Map speaker_slot
    old_slot = g.get('speaker_slot')
    if old_slot in slot_key_map:
        g['speaker_slot'] = slot_key_map[old_slot]
    
    # Remap text
    c = g.get('content', '')
    for old_k, new_k in slot_key_map.items():
        c = c.replace(f'{{{{scenarioChar "{old_k}"}}}}', f'{{{{scenarioChar "{new_k}"}}}}')
    c = c.replace('Southern Union Monster College', 'Supernatural University of Central California').replace('Solarton University', 'Supernatural University of Central California (SUCC)')
    g['content'] = c
    
    # Remap messages
    for m in g.get('messages', []):
        m_slot = m.get('speaker_slot')
        if m_slot in slot_key_map:
            m['speaker_slot'] = slot_key_map[m_slot]
        mc = m.get('content', '')
        for old_k, new_k in slot_key_map.items():
            mc = mc.replace(f'{{{{scenarioChar "{old_k}"}}}}', f'{{{{scenarioChar "{new_k}"}}}}')
        mc = mc.replace('Southern Union Monster College', 'Supernatural University of Central California').replace('Solarton University', 'Supernatural University of Central California (SUCC)')
        m['content'] = mc

# Ensure Cap 11 top-level speaker matches messages[0]
cap11 = scen['greetings'][25]
cap11['speaker_slot'] = 'twin'
for m in cap11.get('messages', []):
    m['speaker_slot'] = 'twin'

# Save to FINAL
p.write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
print("Successfully updated FINAL/Svartulfr_Master_Scenario.json with 13 role slots and 26 greetings!")

# 5. PUT to Wyvern
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
        print(f"Scenario PUT Success! Status: {resp.status}, New Revision: {res.get('revision')}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8')
    print(f"Scenario PUT HTTPError: {e.code} - {err_body}")
except Exception as e:
    print(f"Scenario PUT Error: {e}")
