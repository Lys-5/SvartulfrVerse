import json

with open('lorebooks/source/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    source_data = json.load(f)

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    final_data = json.load(f)

final_by_name = {e.get('name'): e for e in final_data['entries']}

print("Comparing entries with {{age}} in source vs FINAL:")
count = 0
entries = source_data['entries']
entry_list = entries.values() if isinstance(entries, dict) else entries

for e in entry_list:
    content = e.get('content', '')
    if '{{age}}' in content:
        name = e.get('comment') or (e.get('key', [''])[0] if isinstance(e.get('key'), list) and e.get('key') else '')
        f_entry = final_by_name.get(name)
        if f_entry:
            count += 1
            if count <= 5:
                print(f"\n--- NPC: {name} ---")
                for line in content.split('\n'):
                    if '{{age}}' in line or 'AGE:' in line:
                        print(f"  SOURCE: {line.strip()[:100]}")
                f_content = f_entry.get('content', '')
                for line in f_content.split('\n'):
                    if 'AGE:' in line:
                        print(f"  FINAL:  {line.strip()[:100]}")

print(f"\nTotal source entries with {{{{age}}}} checked: {count}")
