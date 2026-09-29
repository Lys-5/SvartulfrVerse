import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    world = json.load(f)

chars_by_id = {c['id']: c for c in world['world_characters']}

# Check each G2 character's full description / long_summary
print("Checking age text inside long_summary and personality:")
for item in g2_list:
    cid = item['id']
    name = item['name']
    c = chars_by_id[cid]
    ls = c.get('long_summary') or ''
    p = c.get('personality') or ''
    s = c.get('summary') or ''
    dd = c.get('display_description') or ''
    full_text = f"{ls}\n{p}\n{s}\n{dd}"
    
    # search for age patterns
    # e.g. "AGE: ..." or "(\d+) years old" or "born ..."
    m_age = re.findall(r'(?:age|età)\s*[:=]?\s*([^\n;\]]+)', full_text, re.I)
    m_born = re.findall(r'(?:born|nascit[ao]|birth)\s*[:=]?\s*([^\n;\]\.\,]+)', full_text, re.I)
    
    # print if something interesting
    age_str = ", ".join(m_age[:2]) if m_age else "None"
    born_str = ", ".join(m_born[:2]) if m_born else "None"
    if '{{age}}' not in age_str or born_str != "None":
        print(f"{name:30s} | age: {age_str[:35]:35s} | born: {born_str[:30]}")
