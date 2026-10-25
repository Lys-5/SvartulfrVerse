import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

d = json.load(open('scratch/mod93312_dump.json', encoding='utf-8'))
text = d['content'][0]['text']

idx = text.find('1e4*t+n')
print(text[max(0, idx - 100):min(len(text), idx + 2000)])
