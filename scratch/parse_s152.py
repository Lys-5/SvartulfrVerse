import re
import json

with open('scratch/campmystic_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
s152 = scripts[152]

# Let's search for character id in s152
# In Wyvern/Next.js/React hydration streams, data often looks like self.__next_f.push([1,"..."])
# Let's find all occurrences of campmystic or character fields
chunks = re.findall(r'self\.__next_f\.push\(\[\d+,\s*"(.*?)"\]\)', s152)
print(f'Total chunks in s152: {len(chunks)}')

full_unquoted = ''
for c in chunks:
    # replace escaped quotes
    unq = c.encode('utf-8').decode('unicode_escape', errors='ignore')
    full_unquoted += unq

print(f'Unquoted length: {len(full_unquoted)}')
with open('scratch/campmystic_stream.txt', 'w', encoding='utf-8') as f:
    f.write(full_unquoted)

# Now search for character object in stream
m = re.findall(r'\{"id":"([^"]+)","name":"([^"]+)",.*?"slug":"campmystic"', full_unquoted)
print('Matches with slug campmystic:', m)

m2 = re.findall(r'"character":(\{.*?"name":"Camp Mystic".*?\})', full_unquoted)
print('Matches "character":', len(m2))

# Search for the id of campmystic
for line in full_unquoted.split('\n'):
    if 'campmystic' in line:
        print('Line with campmystic:', line[:300])
