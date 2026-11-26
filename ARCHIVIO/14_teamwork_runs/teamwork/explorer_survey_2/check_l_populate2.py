import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
content = open('scratch/nC_part2.js', encoding='utf-8', errors='ignore').read()

idx = content.find('l.forEach(e=>n.push(e))')
print(content[max(0, idx - 3000):max(0, idx - 1000)])
