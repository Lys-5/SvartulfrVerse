import json
import re
from collections import Counter

sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))
s_lex = sec.get('lexicon', [])

print(f"Total entries in Secondary: {len(s_lex)}")

# Let's inspect what different categories of entries exist
patterns = Counter()
for e in s_lex:
    content = e.get('content', '')
    # Extract all top-level section headers
    headers = [line.split(':')[0].strip() for line in content.split('\n') if re.match(r'^[A-Z0-9\s&/\-]+:', line.strip()) and not line.strip().startswith('[')]
    header_sig = " -> ".join(headers[:4])
    patterns[header_sig] += 1

print("\nTop 10 header structures in Secondary:")
for sig, cnt in patterns.most_common(10):
    print(f"Count: {cnt}\n  Structure: {sig}\n")
