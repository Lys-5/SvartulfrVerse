import json

targets = [
    'Ruaraidh "Rory" Ballantine',
    'Sullivan "Sully" Jones',
    'Jean-Luc Virtuoso',
    'Alicia Virtuoso',
    'Dr. Arthur Sinclair',
    'Ilya Volkov',
    'Vasile Ionescu'
]

for path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    d = json.load(open(path, 'r', encoding='utf-8'))
    for e in d.get('entries', []):
        name = e.get('name', '')
        if any(t.lower() == name.lower() or t.lower() in name.lower() for t in targets):
            print("="*70)
            print("FILE:", path)
            print("ENTRY_ID:", e.get('entry_id'))
            print("NAME:", name)
            print("KEYS:", e.get('keys'))
            print("SECONDARY_KEYS:", e.get('secondary_keys'))
            print("AVATAR:", e.get('avatar'))
            print("NPC_INFO:", json.dumps(e.get('npc_info', {}), indent=2))
            print("CONTENT PREVIEW:\n", e.get('content', '')[:1200])
