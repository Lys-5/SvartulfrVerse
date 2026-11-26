import glob, re

js_files = glob.glob('scratch/*.js')
for f in js_files:
    content = open(f, encoding='utf-8', errors='ignore').read()
    matches = list(re.finditer(r'\b[a-zA-Z0-9_\$]*\(98043\)', content))
    if matches:
        print(f"=== Found s(98043) in {f} ===")
        for m in matches:
            idx = m.start()
            print(content[max(0, idx-100):min(len(content), idx+300)])
            print("-" * 50)
