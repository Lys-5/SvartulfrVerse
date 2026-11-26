import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
content = open('scratch/nC_part2.js', encoding='utf-8', errors='ignore').read()

# Find where speaker/avatar matching happens
idx = content.find('unregisteredNpcName')
print(content[max(0, idx - 200):min(len(content), idx + 800)])
