import os
import re

TARGET_DIRS = ['scratch', '.agents/teamwork', 'knowledge']

total_replacements = 0
files_updated = []

for td in TARGET_DIRS:
    for root, dirs, files in os.walk(td):
        for f in files:
            if f.endswith(('.json', '.txt', '.md')):
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                        content = fp.read()
                    
                    c1 = content.count('Sunday, August 26')
                    c2 = content.count('Monday, August 27')
                    
                    if c1 > 0 or c2 > 0:
                        new_content = content.replace('Sunday, August 26', 'Monday, August 26')
                        new_content = new_content.replace('Monday, August 27', 'Tuesday, August 27')
                        with open(p, 'w', encoding='utf-8') as fp:
                            fp.write(new_content)
                        count = c1 + c2
                        total_replacements += count
                        files_updated.append((p, count))
                        print(f"Updated {p}: {count} replacements")
                except Exception as e:
                    print(f"Error reading {p}: {e}")

print("\n==========================================")
print(f"Total files updated: {len(files_updated)}")
print(f"Total string replacements: {total_replacements}")
print("==========================================")
