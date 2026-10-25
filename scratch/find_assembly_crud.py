import glob
import re

for f in glob.glob('e:/repository/SvartulfrVerse/scratch/*.js'):
    txt = open(f, encoding='utf-8').read()
    # Search for getAll and create and fork in the same function or object
    matches = re.finditer(r'(getAll|create|update|remove|fork)\s*:\s*async\s*function|\b(getAll|create|update|remove|fork)\s*:\s*async\s*\(|\b(getAll|create|update|remove|fork)\s*:\s*\(', txt)
    count = 0
    for m in matches:
        idx = m.start()
        snippet = txt[max(0, idx-50):min(len(txt), idx+200)]
        if 'assembly' in snippet or 'assemblies' in snippet or 'prompt' in snippet:
            print(f"Match in {f} at {idx}:")
            print(snippet)
            print("="*40)
            count += 1
            if count > 5:
                break
