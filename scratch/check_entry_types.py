import pathlib
import re

txt = pathlib.Path('scratch/inbox/wv_chunk.js').read_text(encoding='utf-8', errors='ignore')

# Find all comparisons against .type
pattern = re.compile(r'(\w+\.type\s*===?\s*["\']([^"\']+)["\']|["\']([^"\']+)["\']\s*===?\s*\w+\.type)')
matches = pattern.findall(txt)
print(f"Total type comparisons: {len(matches)}")

found_types = set()
for full, t1, t2 in matches:
    val = t1 or t2
    found_types.add(val)
    print(f"Match: {full} -> value: {val}")

print("\nDistinct type values found:")
for t in sorted(found_types):
    print(f" - {t}")
