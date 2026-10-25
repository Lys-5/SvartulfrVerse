import re
import glob

files = glob.glob('scratch/*.js')
for f in files:
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        for term in ['message', 'messages', 'swipe', 'chat-logs']:
            matches = re.findall(rf'["\'`]([^"\'`]*(?:chat-logs|messages|swipe)[^"\'`]*)["\'`]', content)
            if matches:
                endpoints = [m for m in matches if '/' in m or 'api' in m or 'PUT' in m or 'PATCH' in m]
                if endpoints:
                    print(f"File {f}:", set(endpoints[:10]))
                    break
    except Exception as e:
        pass
