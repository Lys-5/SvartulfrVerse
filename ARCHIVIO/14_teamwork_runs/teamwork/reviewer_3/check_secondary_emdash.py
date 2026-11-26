import json

data = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))
entries = data.get('entries', [])

edric_entry = None
found_entries = []

for idx, e in enumerate(entries):
    name = e.get('name', '')
    content = e.get('content', '')
    comment = e.get('comment', '')
    keys = e.get('keys', [])
    em_in_content = content.count('—')
    em_in_comment = comment.count('—')
    if name == 'Edric Douglas':
        edric_entry = e
        print(f"Edric Douglas: content em-dashes: {em_in_content}, comment: {em_in_comment}")
    if em_in_content > 0 or em_in_comment > 0:
        found_entries.append((name, em_in_content, em_in_comment))

print(f"Total entries in Secondary with em-dashes: {len(found_entries)}")
for name, c_cnt, com_cnt in found_entries[:15]:
    print(f"  {name:30} | content: {c_cnt} | comment: {com_cnt}")
