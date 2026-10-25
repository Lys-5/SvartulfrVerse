import glob
import re

keywords = [
    'visual novel',
    'vn_mode',
    'display settings',
    'auto-apply',
    'auto_apply',
    'content creation',
    'content_creation',
    'character sheet',
    'auto-scene',
    'auto_scene',
    'auto_party',
    'auto-party',
    'chat_display',
    'display_mode'
]

js_files = glob.glob('scratch/*.js')
print(f'Scanning {len(js_files)} JS chunk files in scratch/...')

found = 0
for f in js_files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    for kw in keywords:
        pattern = re.compile(re.escape(kw), re.IGNORECASE)
        for m in pattern.finditer(content):
            found += 1
            start = max(0, m.start() - 120)
            end = min(len(content), m.end() + 120)
            snippet = content[start:end].replace('\n', ' ')
            print(f'[{f}] Matched "{kw}":')
            print(f'  ...{snippet}...\n')

print(f'Total matches found: {found}')
