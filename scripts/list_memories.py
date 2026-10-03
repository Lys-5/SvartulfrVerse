import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
memories = [l for l in d['world_lexicon_entries'] if l.get('type') == 'memory']

print(f"Total memory entries: {len(memories)}")
for m in memories:
    name = m['name'].encode('ascii', 'replace').decode('ascii')
    cnt = m.get('content', '').replace('\n', ' ')[:140].encode('ascii', 'replace').decode('ascii')
    print(f"ID: {m['id']} | Name: {name}")
    print(f"  Attached: {m.get('attached_world_character_id')}")
    print(f"  Content: {cnt}\n")
