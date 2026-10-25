import re

content = open('e:/repository/SvartulfrVerse/scratch/36457-688d656b1534b9f0.js', encoding='utf-8').read()

# Let's inspect where lore_template, floating_prompt, whisper_template, main_prompt_sections are defined and used
for term in ['lore_template', 'whisper_template', 'floating_prompt', 'F=[{value:"normal"', 'start_reply_with']:
    pos = 0
    while True:
        pos = content.find(term, pos)
        if pos == -1:
            break
        print(f"=== Found '{term}' at {pos} ===")
        print(content[max(0, pos-100):min(len(content), pos+500)])
        pos += len(term)
        if pos > 100000:
            break
