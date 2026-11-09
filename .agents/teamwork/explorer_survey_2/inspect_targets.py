import json

def inspect_entry(path, target_id):
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for e in d.get('entries', []):
        if (e.get('entry_id') or e.get('id')) == target_id:
            return e
    return None

targets = [
    ('lorebooks/optimized/Svartulfr_Location.json', 'ulTwlYo2jqObA7l_bFoa5', 'St. Brugge Location'),
    ('lorebooks/optimized/Svartulfr_Location.json', 'UmuOEDRDjliMuEpyMbeRo', 'La Dimora del Rifugio Location'),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'jmh0MajEsRwrm4UYU14mY', 'Rev in NPC Secondary'),
    ('FINAL/Svartulfr_NPC_Secondary.json', '1TnBSs1poc0mTNG8R0OTx', 'Kobal in NPC Secondary'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'alyssa_world_dossier_2b54a223', 'Alyssa in NPC Primary'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'Vcj4h2TL4Usola2A4OOl6', 'Jasper in NPC Primary'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'RVmhUtNzKvHow_AExX-LR', 'Kaladin Nargathon in NPC Primary'),
    ('FINAL/Svartulfr_NPC_Primary.json', 'fQHJanwGPD5nX-5jIpqym', 'Archer Wolfwood in NPC Primary'),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'bunD_crPBoA7FFi-QNTzw', 'Warg in NPC Secondary'),
    ('FINAL/Svartulfr_NPC_Secondary.json', 'gyZ3SOAsx3M7l42RDqSeZ', 'Adelin Coso in NPC Secondary')
]

with open('e:/repository/SvartulfrVerse/.agents/teamwork/explorer_survey_2/target_entries_inspection.txt', 'w', encoding='utf-8') as out:
    for path, eid, label in targets:
        e = inspect_entry(path, eid)
        out.write(f'=== {label} (ID: {eid}) ===\n')
        if not e:
            out.write('NOT FOUND!\n\n')
            continue
        out.write(f'Name: {e.get("name")}\n')
        out.write(f'Type: {e.get("type")}\n')
        out.write(f'Keys: {e.get("keys")}\n')
        out.write(f'Secondary Keys: {e.get("secondary_keys")}\n')
        out.write(f'Selective: {e.get("selective")}\n')
        out.write(f'Key Logic: {e.get("key_logic")}\n')
        out.write(f'Constant: {e.get("constant")}\n')
        out.write(f'Scan Persona: {e.get("scan_persona")}\n')
        out.write(f'Whole Words Only: {e.get("whole_words_only")}\n')
        out.write(f'Highlight Keys: {e.get("highlight_keys")}\n')
        out.write(f'Ignored Characters: {e.get("ignored_characters")}\n')
        out.write(f'Ignored Personas: {e.get("ignored_personas")}\n')
        out.write(f'Avatar: {e.get("avatar")}\n')
        out.write(f'NPC Info: {e.get("npc_info")}\n')
        out.write(f'Content Length: {len(e.get("content", ""))}\n')
        out.write(f'Content Full:\n{e.get("content", "")}\n\n')

print('Dumped inspection to target_entries_inspection.txt')
