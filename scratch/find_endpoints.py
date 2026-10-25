import glob, re

for p in glob.glob('scripts/*.js') + glob.glob('scripts/*.py') + glob.glob('scratch/*.py'):
    try:
        content = open(p, encoding='utf-8', errors='ignore').read()
        if 'characters' in content and 'wyvern' in content:
            matches = re.findall(r'https?://[^\'\"\s]+characters[^\'\"\s]*', content)
            if matches:
                print(p, set(matches))
    except:
        pass
