import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# 1. Fetch live scenario to get current revision
req_get = urllib.request.Request(f"{API_BASE}/character-scenarios/{SCENARIO_ID}", headers=headers)
with urllib.request.urlopen(req_get) as resp:
    live = json.load(resp)
current_rev = live.get('revision', 13)
print(f"Current live scenario revision: {current_rev}")

# 2. Load local scenario
scen_path = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.loads(scen_path.read_text(encoding='utf-8'))

# 3. Define the 13 canonical slots covering all 14 characters
new_slots = [
    {
        "key": "maternal_grandfather",
        "label": "Maternal Grandfather",
        "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}] # Wulfnic
    },
    {
        "key": "father",
        "label": "Father",
        "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}] # Erik
    },
    {
        "key": "eldest_brother",
        "label": "Eldest Brother",
        "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}] # Malachia
    },
    {
        "key": "brother",
        "label": "Brother",
        "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}] # Noah
    },
    {
        "key": "twin",
        "label": "Twin",
        "pool": [
            {"character_id": "_t4J9aQNJM36cUKAP4wB4U", "weight": 100}, # Jasper
            {"character_id": "_6exg3yPfe2eCDK4hTftkh", "weight": 100}  # Alyssa
        ]
    },
    {
        "key": "uncle",
        "label": "Uncle",
        "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}] # Logan
    },
    {
        "key": "cousin",
        "label": "Cousin",
        "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}] # Edric
    },
    {
        "key": "quarterback",
        "label": "Quarterback",
        "pool": [{"character_id": "_xJVPtBLL3dxy69RLKL9X9", "weight": 100}] # Jared
    },
    {
        "key": "friend",
        "label": "Friend",
        "pool": [{"character_id": "_Xd3NhKnRJByMTtdb6PjxJ", "weight": 100}] # Stan
    },
    {
        "key": "crush",
        "label": "Crush",
        "pool": [{"character_id": "_zn24784jfcchQ7EwCyAnm", "weight": 100}] # Mac
    },
    {
        "key": "roommate",
        "label": "Roommate",
        "pool": [{"character_id": "_pnrXbkWqcgmFAf3meRWFY", "weight": 100}] # Sierra
    },
    {
        "key": "best_friend",
        "label": "Best Friend",
        "pool": [{"character_id": "_qXgBMbFYJfc84hbLHhe92", "weight": 100}] # Scarlett
    },
    {
        "key": "dorm_roommate",
        "label": "Dorm Roommate",
        "pool": [{"character_id": "_wn6DkCcg3Xqa2Xpx9ttnT", "weight": 100}] # Russ
    }
]

scen['slots'] = new_slots

# 4. Clean up the 4 greetings with obsolete speaker slots
for g in scen.get('greetings', []):
    gid = g.get('id')
    if gid == 'scene-alyssa-story-2-1':
        g['speaker_slot'] = 'twin'
        for m in g.get('messages', []):
            if m.get('speaker_slot') == 'boss':
                m['speaker_slot'] = 'twin'
    elif gid == 'scene-guild-1':
        g['speaker_slot'] = 'twin'
        for m in g.get('messages', []):
            if m.get('speaker_slot') == 'boss':
                m['speaker_slot'] = 'twin'
    elif gid == 'scene-alyssa-story-8-1':
        for m in g.get('messages', []):
            if m.get('speaker_slot') in ['paternal_grandfather', 'paternal_grandmother']:
                m['speaker_slot'] = 'maternal_grandfather'
    elif gid == 'scene-alyssa-story-9-1':
        for m in g.get('messages', []):
            if m.get('speaker_slot') == 'major':
                m['speaker_slot'] = 'father'

# 5. Update scenario narrative prompt to reflect the 14-character cast
clean_scenario_text = (
    "Setting: Contemporary Supernatural California (2024–2025) — Blackwood City (Seven Hills, Villa Douglas, Uptown, Dockside, Ironworks) "
    "and Solarton (Supernatural University of Central California / SUCC Campus, Greek Row, DMHA Guild Hall, Camp Mystic).\n\n"
    "Protagonists & Douglas-Bloodmoon Pack Family:\n"
    "- {{user}} and {{scenarioChar \"twin\"}} are the 19-year-old Douglas-Bloodmoon twins (Alyssa Hvit, Dominant Omega Pre-Med Healer, and Jasper Svartr, Beta Technomancer & DJ Frequency), starting their freshman year at SUCC.\n"
    "- {{scenarioChar \"father\"}} (Erik Ulfr Douglas): Prime Alpha Pack Leader of House Douglas and CEO of the Douglas Commercial Coalition (DCC).\n"
    "- {{scenarioChar \"eldest_brother\"}} (Malachia Björn): 26-year-old Dominant Alpha, undefeated heavyweight fighter, and silent protective shield of the twins.\n"
    "- {{scenarioChar \"brother\"}} (Noah Loki): 25-year-old Delta diplomat, corporate strategist, and charming socialite.\n"
    "- {{scenarioChar \"uncle\"}} (Logan Járn Douglas): Erik's Beta brother, mechanic at The Verve, and grounded confidant.\n"
    "- {{scenarioChar \"cousin\"}} (Edric Douglas): Logan's 20-year-old son and loyal campus companion.\n"
    "- {{scenarioChar \"maternal_grandfather\"}} (Wulfnic Báleygr Bloodmoon): 1,197-year-old Primordial Firstborn Alpha of the Sacred Forest.\n\n"
    "SUCC Campus Circle & Inner Circle:\n"
    "- {{scenarioChar \"quarterback\"}} (Jared Thompson): 21-year-old Minotaur, star quarterback for the SUCC Bulls, BRO fraternity member.\n"
    "- {{scenarioChar \"friend\"}} (Stanley Davies Jr.): 20-year-old Golden Retriever Demihuman, chemistry undergraduate, loyal friend and roommate.\n"
    "- {{scenarioChar \"crush\"}} (Mackenzie 'Mac' Sanchez-Rogers): 20-year-old Coyote shifter, talented synth musician and mechanic at Rogers' Motors.\n"
    "- {{scenarioChar \"roommate\"}} (Sierra Cruz): 18-year-old Lamia / Serpentine Demihuman, varsity track athlete, Alyssa's dorm roommate.\n"
    "- {{scenarioChar \"best_friend\"}} (Scarlett Rose): 19-year-old Succubus, social coordinator and Alyssa's closest confidante.\n"
    "- {{scenarioChar \"dorm_roommate\"}} (Russell 'Russ'): 21-year-old Human, tattoo apprentice, Jasper's sharp-tongued dorm roommate at Wyrm Hall and member of the Five Cocketeers.\n\n"
    "Core Rules:\n"
    "- Demi-humans and Werewolves in Partial Shift possess ONLY ONE PAIR OF EARS (their animal ears on top of the head, no human ears).\n"
    "- Respect familial boundaries between Douglas/Bloodmoon relatives (deep pack warmth, teasing, and protective loyalty; no romantic or sexual framing between blood relatives).\n"
    "- Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.\n\n"
    "[NARRATION GUIDELINES & ANTI-VENTRILOQUISM:\n"
    "1. Strict Anti-Ventriloquism: Never speak, think, emote, or act for {{user}}. Pause and wait for {{user}}'s input.\n"
    "2. Scene Balancing: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies.\n"
    "3. Format Discipline: Dialogue in quotes (\"...\"), actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only (*...*). Never use the em dash; use commas or periods instead.]\n\n"
    "[NPC FORMATTING DISCIPLINE]: When secondary NPCs or background characters speak or take action, always output their dialogue on a new line prefixed with their exact full name and a colon (e.g., 'Santiago Herrera: [dialogue/action]'). Never blend NPC dialogue anonymously into narration."
)

scen['scenario'] = clean_scenario_text

# 6. Save updated JSON locally
scen_path.write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
print("Saved updated FINAL/Svartulfr_Master_Scenario.json")

# 7. Deploy via PUT /api/character-scenarios/{SCENARIO_ID}
put_payload = {
    'name': scen.get('name'),
    'display_description': scen.get('display_description', ''),
    'avatar': scen.get('avatar', ''),
    'tags': scen.get('tags', []),
    'visibility': scen.get('visibility', 'private'),
    'rating': scen.get('rating', 'explicit'),
    'revision': current_rev,
    'linked_world_id': scen.get('linked_world_id', ''),
    'scenario': scen.get('scenario', ''),
    'startup_script': scen.get('startup_script', ''),
    'slots': scen.get('slots', []),
    'greetings': scen.get('greetings', []),
    'lorebook_ids': scen.get('lorebook_ids', []),
    'gallery': scen.get('gallery', [])
}

req_put = urllib.request.Request(
    f"{API_BASE}/character-scenarios/{SCENARIO_ID}",
    data=json.dumps(put_payload, ensure_ascii=False).encode('utf-8'),
    headers=headers,
    method='PUT'
)

try:
    with urllib.request.urlopen(req_put, timeout=60) as resp:
        res = json.load(resp)
        print(f"Master Scenario PUT SUCCESS! Status: {resp.status} | New revision: {res.get('revision')} | Slots count: {len(res.get('slots', []))} | Greetings count: {len(res.get('greetings', []))}")
        print("\nUpdated live slots:")
        for s in res.get('slots', []):
            p_chars = [p.get('character_id') for p in s.get('pool', [])]
            print(f"  - Key: '{s.get('key')}' | Label: '{s.get('label')}' | Pool: {p_chars}")
except urllib.error.HTTPError as e:
    err_body = e.read().decode('utf-8', errors='ignore')
    print(f"Master Scenario PUT HTTPError {e.code}: {err_body}")
