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
    'Rozalia TÄƒnase', 'Ruby Valerius', 'Vesna | A long day',
    'Mikan | Runaway Catgirl raids your fridge', 'Ginger | Sniper Situation',
    'Orion and Sigrid Valois || Pack Enforcer & Strategic Guard , Pack Sentinel & Lore-Keeper of The Triune Moon Pack',
    'Fairy Ecologist â€” Henrey Cote', 'Aria Xenthon', 'Tori', 'River | Daddy Wolf'
]

results = {}
for char in chars_to_find:
    pattern = r'## ' + re.escape(char) + r'\s+.*?(?=## |\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        desc_match = re.search(r'`(.*?)`', match.group(0), re.DOTALL)
        if desc_match:
            desc = clean_text(desc_match.group(1))
        else:
            desc = 'No description'
        
        clean_name = char.split('|')[0].strip().replace('TÄƒnase', 'Tănase').replace('Fairy Ecologist â€” ', '').replace('Fairy Ecologist — ', '')
        if 'Henrey Cote' in clean_name:
            clean_name = 'Henrey Cote'
            
        jed = f"[NAME: {clean_name}; SPECIES: Unknown; AGE: Unknown]\n\nBACKSTORY: {desc}\n\nFAMILY & PACK: To be determined.\n\nVOICE & BEHAVIOR: To be determined.\n\n[CORE THEME]"
        results[clean_name] = jed

os.makedirs(r'd:\SvartulfrVerse\docs', exist_ok=True)
with open(r'd:\SvartulfrVerse\docs\GroupA_JED.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print('Saved json with keys:', list(results.keys()))
