import glob, re

for f in glob.glob('scratch/*.js'):
    content = open(f, encoding='utf-8', errors='ignore').read()
    if 'Lexicon & Summaries' in content:
        idx = content.find('Lexicon & Summaries')
        print(f"Found 'Lexicon & Summaries' in {f} at {idx}:")
        print(content[max(0, idx-200):min(len(content), idx+500)])
        print("="*60)
