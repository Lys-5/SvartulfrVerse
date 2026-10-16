import pathlib
import re

txt = pathlib.Path('scratch/inbox/wv_chunk.js').read_text(encoding='utf-8', errors='ignore')

# er is the entry object in the form component
matches = re.findall(r'\ber\.([a-zA-Z0-9_]+)', txt)
props = sorted(set(matches))
print(f"Total properties accessed on 'er': {len(props)}")
for p in props:
    print(f"  - {p}")
