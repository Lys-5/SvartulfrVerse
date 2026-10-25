import glob, re

keywords = [
    'auto-apply',
    'auto apply',
    'auto_apply',
    'content creation',
    'content_creation',
    'ai content',
    'scene',
    'party',
    'stats'
]

js_files = glob.glob('scratch/*.js')
print("Searching for sidebar flags...")

for f in js_files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    # Search for switch labels or settings in simulation
    for kw in ['Auto-apply', 'auto-apply', 'Auto Apply', 'Content creation', 'content creation', 'AI content']:
        for m in re.finditer(re.escape(kw), content, re.IGNORECASE):
            idx = m.start()
            print(f"[{f}] at {idx} for '{kw}':")
            print(content[max(0, idx-150):min(len(content), idx+250)])
            print("-" * 50)
