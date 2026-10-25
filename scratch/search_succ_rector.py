import json
import glob

for fpath in glob.glob('FINAL/*.json') + glob.glob('lorebooks/optimized/*.json'):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for e in d.get('entries', []):
            content = e.get('content', '')
            for term in ['chancellor', 'rector', 'rettore', 'dean', 'vance']:
                if term in content.lower():
                    print(f"Match in {fpath}: {e.get('name')} (term: {term})")
                    break
    except:
        pass
