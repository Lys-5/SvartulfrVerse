import re
import json

content = open('e:/repository/SvartulfrVerse/scratch/36457-688d656b1534b9f0.js', encoding='utf-8').read()

# Let's search for the default prompt assembly or initial state or props
patterns = [
    r'defaultPromptAssembly',
    r'main_prompt_sections',
    r'floating_prompt_sections',
    r'lore_template',
    r'whisper_template',
    r'post_history',
    r'prompt_template',
    r'default_prompt',
    r'exportPrompt',
    r'importPrompt'
]

print("=== SEARCHING PATTERNS IN 36457 ===")
for p in patterns:
    matches = [m.start() for m in re.finditer(p, content, re.IGNORECASE)]
    print(f"Pattern {p}: {len(matches)} matches")

# Let's find where main_prompt_sections, floating_prompt_sections, blocks, etc. are defined
idx = content.find("main_prompt_sections")
while idx != -1:
    print("\n--- Context around main_prompt_sections at", idx, "---")
    print(content[max(0, idx-200):min(len(content), idx+400)])
    idx = content.find("main_prompt_sections", idx+1)
    if idx > 20000: # just first few
        break
