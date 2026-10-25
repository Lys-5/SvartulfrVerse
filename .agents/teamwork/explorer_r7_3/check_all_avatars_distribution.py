import json
from collections import Counter

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    prim = json.load(f)
with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec = json.load(f)

all_entries = prim.get('entries', []) + sec.get('entries', [])
avatar_counts = Counter(e.get('avatar') for e in all_entries)

print(f"Total entries inspected: {len(all_entries)}")
print(f"Total unique avatar URLs: {len(avatar_counts)}")

print("\nDistribution of avatar occurrences:")
occurrence_dist = Counter(avatar_counts.values())
for count, num_urls in sorted(occurrence_dist.items()):
    print(f"  URLs appearing {count} times: {num_urls}")

print("\nAll URLs appearing more than once:")
for url, count in avatar_counts.most_common():
    if count > 1:
        print(f"  [{count}] {url}")
