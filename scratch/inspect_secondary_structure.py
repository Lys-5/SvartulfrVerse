import json, re

sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

print("=== SAMPLE OF SECONDARY ENTRIES WITHOUT BACKSTORY ===")
count = 0
for e in sec['lexicon']:
    content = e.get('content', '')
    if 'BACKSTORY:' not in content and e.get('entry_id') != 'h-ttmlgJYeRXqyDvQjSX7':
        print(f"\n[{e.get('entry_id')}] {e.get('name')}:")
        print("Length:", len(content))
        headings = re.findall(r'^[A-Z0-9 &/\-\(\)]+:', content, re.M)
        print("Headings:", headings)
        print("First 300 chars:\n", content[:300])
        count += 1
        if count >= 5:
            break
