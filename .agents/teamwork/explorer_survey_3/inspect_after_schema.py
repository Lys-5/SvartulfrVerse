import re

content = open('scratch/14685-a6f37bf36e7cf713.js', encoding='utf-8', errors='ignore').read()
idx = content.find('version:V.z.literal(1)')
end = content.find(';', idx + 1000)
print("=== AFTER SCHEMA IN 14685 ===")
print(content[idx+500:idx+2500])
