import re

content = open('scratch/14685-a6f37bf36e7cf713.js', encoding='utf-8', errors='ignore').read()
for m in re.finditer(r'vnMode', content):
    idx = m.start()
    print("=== vnMode in 14685 ===")
    print(content[max(0, idx-400):min(len(content), idx+600)])
    print("=" * 60)
