import re

with open('scratch/campmystic_stream.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for id preceding campmystic or nearby
pos = 0
while True:
    idx = text.find('campmystic', pos)
    if idx == -1:
        break
    start = max(0, idx - 400)
    end = min(len(text), idx + 400)
    snippet = text[start:end]
    print('--- SNIPPET AT', idx, '---')
    print(snippet.encode('ascii', errors='replace').decode('ascii'))
    pos = idx + 10
