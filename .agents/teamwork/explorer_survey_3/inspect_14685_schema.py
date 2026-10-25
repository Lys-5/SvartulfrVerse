import re

content = open('scratch/14685-a6f37bf36e7cf713.js', encoding='utf-8', errors='ignore').read()
idx = content.find('version:V.z.literal(1)')
if idx != -1:
    print("=== SCHEMA FOUND ===")
    print(content[max(0, idx-200):min(len(content), idx+1500)])
