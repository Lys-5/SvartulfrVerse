import re

content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()

# Find all occurrences of Switch or role="switch"
switches = re.findall(r'id:"([^"]+)"[^}]+Switch', content)
print(f"Total switch IDs found: {len(switches)}")
print("Switch IDs:", set(switches))

# Also search for "Party" or "Content" or "Creation" or "Auto" near switches
for m in re.finditer(r'Switch', content):
    idx = m.start()
    snippet = content[max(0, idx-100):min(len(content), idx+150)]
    for kw in ['party', 'scene', 'content', 'creation', 'auto', 'creation']:
        if kw in snippet.lower():
            print(f"Match for '{kw}' near Switch at {idx}:")
            print("  ", snippet.replace('\n', ' '))
            print("-" * 50)
            break
