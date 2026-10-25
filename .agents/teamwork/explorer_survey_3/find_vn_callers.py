import glob, re

js_files = glob.glob('scratch/*.js')
print("Searching for usage of 98043 or vnMode storage...")

for f in js_files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    if '98043' in content or 'vnAutoAdvance' in content or 'vnDirections' in content:
        print(f"=== Found in {f} ===")
        for kw in ['vnAutoAdvance', 'vnDirections', '98043', 'requestSection']:
            for m in re.finditer(kw, content):
                idx = m.start()
                print(f"[{kw}] at {idx}:")
                print(content[max(0, idx-150):min(len(content), idx+250)])
                print("-" * 50)
