import re

content = open('scratch/36457-688d656b1534b9f0.js', encoding='utf-8', errors='ignore').read()
print(f"File 36457 length: {len(content)}")

# Search for Switch or switches
matches = list(re.finditer(r'Switch|role="switch"', content))
print(f"Switches in 36457: {len(matches)}")
for m in matches[:15]:
    idx = m.start()
    print("=== Switch ===")
    print(content[max(0, idx-100):min(len(content), idx+200)].replace('\n', ' '))
