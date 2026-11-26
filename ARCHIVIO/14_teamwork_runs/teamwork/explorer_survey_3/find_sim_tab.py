import glob, re

for f in glob.glob('scratch/*.js'):
    content = open(f, encoding='utf-8', errors='ignore').read()
    if 'Simulation' in content:
        for m in re.finditer(r'label:"Simulation"|title:"Simulation"|children:"Simulation"', content):
            idx = m.start()
            print(f"[{f}] at {idx}:")
            print(content[max(0, idx-100):min(len(content), idx+300)])
            print("-" * 50)
