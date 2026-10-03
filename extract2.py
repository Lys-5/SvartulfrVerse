import json
import re
import os

def clean_text(html_text):
    text = re.sub(r'<.*?>', ' ', html_text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

with open(r'd:\SvartulfrVerse\ARCHIVIO\01_Drafts\Character_Cards_V1\Scraped_Characters.md', 'r', encoding='utf-8') as f:
    text = f.read()

chars_to_find = [
    'Rozalia', 'Ruby Valerius', 'Vesna',
    'Mikan', 'Ginger',
    'Orion and Sigrid Valois',
    'Henrey Cote', 'Aria Xenthon', 'Tori', 'River'
]

results = {}
for char in chars_to_find:
    pattern = r'## [^\n]*?' + re.escape(char) + r'.*?(?=## |\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        matched_text = match.group(0)
        desc_match = re.search(r'`(.*?)`', matched_text, re.DOTALL)
        if desc_match:
            desc = clean_text(desc_match.group(1))
        else:
            # Maybe it is directly HTML without codeblock
            # Try to grab anything after the image
            desc = clean_text(matched_text)
            # clean out the heading and image
            desc = re.sub(r'##.*?\n', '', desc)
            desc = re.sub(r'!\[Avatar\].*?\n', '', desc)
        
        clean_name = char
        if char == 'Rozalia': clean_name = 'Rozalia Tănase'
        
        jed = f"[NAME: {clean_name}; SPECIES: Unknown; AGE: Unknown]\n\nBACKSTORY: {desc}\n\nFAMILY & PACK: To be determined.\n\nVOICE & BEHAVIOR: To be determined.\n\n[CORE THEME]"
        results[clean_name] = jed

os.makedirs(r'd:\SvartulfrVerse\docs', exist_ok=True)
with open(r'd:\SvartulfrVerse\docs\GroupA_JED.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print('Saved json with keys:', list(results.keys()))
