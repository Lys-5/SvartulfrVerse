import re

content = open('scratch/webpack_dumped_modules.json', encoding='utf-8', errors='ignore').read()

# Search for calls to edit message, update message, or HTTP methods like put/patch on message
matches = re.findall(r'.{0,100}(?:updateMessage|editMessage|chat-logs/message|message_swipe|swipe_id).{0,100}', content)
print("Found matches:", len(matches))
for m in matches[:15]:
    print("---", m.strip())
