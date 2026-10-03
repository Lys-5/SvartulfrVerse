import re

with open(r'C:\Users\mande\.gemini\antigravity\brain\95b23a44-2346-44a1-a18b-40523986cca3\.tempmediaStorage\snapshot_full_1790663016000.txt', 'r', encoding='utf-8') as f:
    text = f.read()

links = re.findall(r'https://wiki\.wyvern\.chat[^\s\"\'\<\>]+', text)
for l in sorted(set(links)):
    if any(k in l.lower() for k in ['time', 'world', 'calendar', 'clock', 'date']):
        print(l)
