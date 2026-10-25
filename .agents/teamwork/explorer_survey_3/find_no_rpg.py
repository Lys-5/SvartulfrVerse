import glob

for f in glob.glob('scratch/*.js'):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    if 'No RPG-enabled characters' in txt:
        print(f"FOUND 'No RPG-enabled characters' in {f}!")
        idx = txt.find('No RPG-enabled characters')
        print(txt[max(0, idx-300):min(len(txt), idx+500)])
        print("="*60)
