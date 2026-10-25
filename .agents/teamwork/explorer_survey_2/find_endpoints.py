import re
import glob

files = glob.glob('scratch/*.js')
endpoints = set()

for f in files:
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        # Find string literals that look like endpoints: /api/... or chat-logs/...
        matches = re.findall(r'["\'`](/[a-zA-Z0-9_\-\/]+(?:chat-log|message)[a-zA-Z0-9_\-\/]*)["\'`]', content)
        endpoints.update(matches)
        
        matches2 = re.findall(r'["\'`](https://app\.wyvern\.chat/api/[^"\'`]+)["\'`]', content)
        endpoints.update(matches2)
    except Exception as e:
        pass

for ep in sorted(list(endpoints)):
    print(ep)
