import glob, re

for f in glob.glob('scratch/*.js'):
    content = open(f, encoding='utf-8', errors='ignore').read()
    # Search for "Inventory" and "Party" and "Stats"
    if 'Inventory' in content and 'Stats' in content and 'Simulation' in content:
        matches = list(re.finditer(r'Party[^\n]{0,50}Stats[^\n]{0,50}Inventory', content))
        if matches:
            print(f"Match in {f}:")
            for m in matches:
                idx = m.start()
                print(" ", content[max(0, idx-100):min(len(content), idx+300)])
                print("-" * 50)
