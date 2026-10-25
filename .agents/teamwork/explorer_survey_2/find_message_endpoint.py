import re
import glob

for f in glob.glob('scratch/*.js'):
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
        if '/new/chat-logs/message' in content:
            matches = re.findall(r'.{0,150}/new/chat-logs/message.{0,150}', content)
            print(f"File {f}:")
            for m in matches:
                print("  ", m.strip())
    except Exception as e:
        pass
