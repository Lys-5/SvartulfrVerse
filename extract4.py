import json
import re

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
            raw_desc = desc_match.group(1)
        else:
            idx = matched_text.find('![Avatar]')
            if idx != -1:
                idx = matched_text.find('\n', idx)
                raw_desc = matched_text[idx:]
            else:
                raw_desc = matched_text
                
        desc = re.sub(r'<.*?>', ' ', raw_desc)
        desc = re.sub(r'\s+', ' ', desc).strip()
        
        clean_name = char
        if char == 'Rozalia': clean_name = 'Rozalia Tănase'
        if char == 'Henrey Cote': clean_name = 'Henrey Cote'
        
        jed = f"[NAME: {clean_name}; SPECIES: Unknown; AGE: Unknown]\n\nBACKSTORY: {desc}\n\nFAMILY & PACK: To be determined.\n\nVOICE & BEHAVIOR: To be determined.\n\n[CORE THEME]"
        results[clean_name] = jed

with open(r'd:\SvartulfrVerse\docs\GroupA_JED.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
