import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('FINAL/scenarios/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    print(f"\nChecking {f}:")
    for g_i, g in enumerate(d.get('greetings', [])):
        for m_i, m in enumerate(g.get('messages', [])):
            c = m.get('content', '')
            # Match 1 to 3 capitalized words followed immediately by a colon
            m_prefix = re.match(r'^([A-Z][a-zA-Z\'-]+(?:\s+[A-Z][a-zA-Z\'-]+){0,2})\s*:', c)
            if m_prefix:
                print(f"  g[{g_i}] m[{m_i}] matched prefix: '{m_prefix.group(0)}' -> Full content: {c[:120]}")

print("\n--- Check complete ---")
