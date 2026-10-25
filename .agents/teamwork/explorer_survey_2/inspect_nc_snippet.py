import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
content = open('scratch/nC_part2.js', encoding='utf-8', errors='ignore').read()
print(content[1400:2500])
