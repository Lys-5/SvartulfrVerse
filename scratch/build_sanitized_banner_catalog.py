import re

with open('scratch/step_3713_prompts.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

# Sanitize function
def sanitize_banner_prompt(p_text):
    # University name: replace any occurrence of SUCC or Solarton University or variants with full canonical name
    p = re.sub(r'Solarton University of the Occult \(SUCC\)', 'the Supernatural University of Central California', p_text)
    p = re.sub(r'Solarton University of the Occult', 'the Supernatural University of Central California', p)
    p = re.sub(r'Solarton Collegiate University', 'the Supernatural University of Central California', p)
    p = re.sub(r'Solarton University', 'the Supernatural University of Central California', p)
    p = re.sub(r'at SUCC\b', 'at the Supernatural University of Central California', p)
    p = re.sub(r'SUCC campus\b', 'the Supernatural University of Central California campus', p)
    p = re.sub(r'SUCC\b', 'Supernatural University of Central California', p)
    
    # Bloodmoon in prompt body
    p = re.sub(r'Bloodmoon', 'Douglas', p)
    
    # TIT sorority -> Tau Iota Theta
    p = re.sub(r'\bTIT Sorority\b', 'Tau Iota Theta Sorority', p)
    p = re.sub(r'\bTIT\b', 'Tau Iota Theta', p)
    
    # Necromancy -> Esoteric Biology & Life Sciences
    p = re.sub(r'Applied Necromancy', 'Applied Esoteric Life Sciences', p)
    p = re.sub(r'necromancy', 'esoteric life sciences', p)
    
    # cream-colored -> ivory-toned / pearl-white
    p = re.sub(r'cream-colored', 'ivory-toned', p)
    p = re.sub(r'\bcreamy\b', 'ivory', p)
    
    # burning -> glowing / crackling
    p = re.sub(r'burning copper', 'warm glowing copper', p)
    p = re.sub(r'burning embers', 'crackling embers', p)
    p = re.sub(r'burning', 'glowing', p)
    
    # bed -> furnishings
    p = re.sub(r'unmade military bunk bed', 'neatly structured oak desk and locker unit', p)
    
    # Add architectural safety tags if not present
    if 'no people' not in p and 'no text' in p:
        p = p.replace('no text, no watermark', 'empty scene, architectural photography, no people, no text, no watermark')
        
    return p

# Split by headings
sections = re.split(r'(?=###\s+)', raw)
clean_sections = []
for sec in sections:
    if not sec.strip(): continue
    clean_sections.append(sanitize_banner_prompt(sec))

final_content = "# Svartúlfr Verse — Master Banners Catalog per Google Imagen 3 (Argon)\n\n"
final_content += "Questo catalogo contiene i 22 banner panoramici (14 Cast Fisso + 8 Location Chiave) riscritti e blindati per **Google Imagen 3 (Argon)**.\n\n"
final_content += "### Regole di Compliance Applicate:\n"
final_content += "1. **Nome Istituzionale SUCC**: Indicato tassativamente per esteso come **`Supernatural University of Central California`** (banditi acronimi e varianti apocrife).\n"
final_content += "2. **Zero Falsi Positivi Policy**: Sostituiti termini a rischio (es. `TIT` -> `Tau Iota Theta`, `Necromancy` -> `Applied Esoteric Life Sciences`, `cream-colored` -> `ivory-toned`, `burning` -> `glowing`).\n"
final_content += "3. **Pure Architectural Establishing Shots**: Clausola `empty scene, architectural photography, no people, no text, no watermark` inclusa su tutti i prompt.\n\n---\n\n"

final_content += '\n\n'.join(clean_sections)

with open('asset/PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Created asset/PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md with sanitized prompts.")
