import json
import re
import os

with open(r'd:\SvartulfrVerse\ARCHIVIO\01_Drafts\Legacy_Janitor_Data\Douglas_Family_Profile.json', 'r', encoding='utf-8') as f:
    content = f.read()

chars_to_extract = ['Erik', 'Malachia', 'Jasper', 'Noah', 'Wulfnic', 'Logan']
results = {}

for char in chars_to_extract:
    match = re.search(f'<{char}>(.*?)</{char}>', content, re.DOTALL | re.IGNORECASE)
    if match:
        results[char] = match.group(1).strip()

def clean_text(text):
    if not text:
        return ''
    text = text.replace('—', ',').replace('**', '')
    return text.strip()

def extract_field(text, field):
    # Matches FIELD: value ending with ; or \n
    match = re.search(fr'{field}:\s*(.*?)(?:;|\n(?=[A-Z_]+:)|\n\]|$)', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ''

def process_char(name, raw_data):
    # Extract known prose fields
    backstory = extract_field(raw_data, 'BACKSTORY')
    if not backstory:
        backstory = extract_field(raw_data, 'ROLE')
        
    dynamic = extract_field(raw_data, 'DYNAMIC_WITH_USER')
    pack_role = extract_field(raw_data, 'PACK_ROLE')
    pack = extract_field(raw_data, 'PACK')
    
    family = []
    if dynamic: family.append(dynamic)
    if pack_role: family.append(f"Pack Role: {pack_role}.")
    if pack: family.append(f"Pack: {pack}.")
    family_text = ' '.join(family)
    
    personality = extract_field(raw_data, 'PERSONALITY')
    temperament = extract_field(raw_data, 'TEMPERAMENT')
    speech = extract_field(raw_data, 'SPEECH_AND_VOCALIZATIONS')
    if not speech: speech = extract_field(raw_data, 'SPEECH_BEHAVIOR')
    quirks = extract_field(raw_data, 'QUIRKS_AND_MANNERISMS')
    
    voice = []
    if personality: voice.append(personality)
    if temperament: voice.append(f"Temperament: {temperament}.")
    if speech: voice.append(speech)
    if quirks: voice.append(quirks)
    voice_text = ' '.join(voice)
    
    # Everything else goes into brackets, we can just extract everything that matches [A-Z_]+:
    fields_found = re.findall(r'([A-Z_]+):\s*(.*?)(?:;|\n(?=[A-Z_]+:)|\n\]|$)', raw_data, re.DOTALL)
    
    bracket_attrs = []
    skip_fields = ['BACKSTORY', 'DYNAMIC_WITH_USER', 'PACK_ROLE', 'PACK', 'PERSONALITY', 'TEMPERAMENT', 'SPEECH_AND_VOCALIZATIONS', 'SPEECH_BEHAVIOR', 'QUIRKS_AND_MANNERISMS', 'NAME', 'AGE', 'ROLE']
    
    name_val = f'{name} Douglas'
    
    for k, v in fields_found:
        k = k.strip()
        v = v.strip()
        if k == 'NAME':
            name_val = v
        if k not in skip_fields and v:
            # clean up v
            v = v.replace('\n', ' ')
            bracket_attrs.append(f'{k}: {v}')
            
    bracket_block = f'[NAME: {name_val}; AGE: {{{{age}}}}; ' + '; '.join(bracket_attrs) + ']'
    
    bracket_block = clean_text(bracket_block)
    backstory = clean_text(backstory)
    family_text = clean_text(family_text)
    voice_text = clean_text(voice_text)
    
    final_section = f'[THE TRUTH OF {name.upper()}]'
    
    out = f'## {name}\n\n'
    out += f'{bracket_block}\n\n'
    out += f'BACKSTORY: {backstory}\n\n'
    out += f'FAMILY & PACK: {family_text}\n\n'
    out += f'VOICE & BEHAVIOR: {voice_text}\n\n'
    out += f'{final_section}\n\n'
    
    return out

os.makedirs(r'd:\SvartulfrVerse\docs', exist_ok=True)
with open(r'd:\SvartulfrVerse\docs\Douglas_Family_JED_Proposal.md', 'w', encoding='utf-8') as f:
    f.write('# Douglas Family JED+ Conversion Proposal\n\n')
    for char in chars_to_extract:
        if char in results:
            f.write(process_char(char, results[char]))
        else:
            f.write(f'## {char}\n\nNot found.\n\n')
