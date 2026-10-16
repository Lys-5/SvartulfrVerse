import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'

req = urllib.request.Request(f'{API_BASE}/character-scenarios/{SCENARIO_ID}', headers={
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0'
})

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("=== SCENARIO VERIFICATION ===")
    print("ID:", data.get('id'))
    print("Name:", data.get('name'))
    print("Revision:", data.get('revision'))
    print("Slots count:", len(data.get('slots', [])))
    print("Greetings count:", len(data.get('greetings', [])))
    print("Lorebooks count:", len(data.get('lorebook_ids', [])))
    print("\nSlots detail:")
    for s in data.get('slots', []):
        pool_chars = [p.get('character_id') for p in s.get('pool', [])]
        print(f"  - Slot '{s.get('key')}' ({s.get('label')}): {len(pool_chars)} character(s) in pool: {pool_chars}")
    print("\nGreetings detail (all 26):")
    for idx, g in enumerate(data.get('greetings', []), 1):
        print(f"  {idx:02d}. [{g.get('id')}] {g.get('name')} | speaker: {g.get('speaker_slot')} | msgs: {len(g.get('messages', []))} | personas: {g.get('linked_persona_ids')}")
