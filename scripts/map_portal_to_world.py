import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/modernfantasy_portal_raw.json', 'r', encoding='utf-8') as f:
    portal_data = json.load(f)

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

existing_chars = { (c.get('name') or c.get('display_name') or '').lower(): c for c in world_data['world_characters'] }
existing_lex = { (l.get('name') or '').lower(): l for l in world_data['world_lexicon_entries'] }
existing_locs = { (loc.get('name') or '').lower(): loc for loc in world_data['world_locations'] }

print(f"Loaded {len(portal_data['characters'])} portal sections.")
print(f"Existing in World: {len(existing_chars)} characters, {len(existing_lex)} lexicon, {len(existing_locs)} locations.\n")

parsed_entries = []

for sec_id, data in portal_data['characters'].items():
    text = data['text']
    images = data['images']
    
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Try to extract key details
    entry = {
        'sec_id': sec_id,
        'title': lines[0] if lines else sec_id,
        'species': '',
        'age': '',
        'height': '',
        'nationality': '',
        'likes': '',
        'dislikes': '',
        'occupation': '',
        'story': '',
        'images': images,
        'raw_lines': lines
    }
    
    # Parse Quick Info lines
    for i, line in enumerate(lines):
        m_sp = re.search(r'Species\s*:\s*([^|]+)', line, re.I)
        if m_sp: entry['species'] = m_sp.group(1).strip()
        m_age = re.search(r'Age\s*:\s*([^|]+)', line, re.I)
        if m_age: entry['age'] = m_age.group(1).strip()
        m_h = re.search(r'Height\s*:\s*([^|]+)', line, re.I)
        if m_h: entry['height'] = m_h.group(1).strip()
        m_nat = re.search(r'Nationality\s*:\s*([^|]+)', line, re.I)
        if m_nat: entry['nationality'] = m_nat.group(1).strip()
        m_occ = re.search(r'Occupation\s*:\s*([^|]+)', line, re.I)
        if m_occ: entry['occupation'] = m_occ.group(1).strip()
        m_lk = re.search(r'Likes\s*:\s*([^|]+)', line, re.I)
        if m_lk: entry['likes'] = m_lk.group(1).strip()
        m_dlk = re.search(r'Dislikes\s*:\s*([^|]+)', line, re.I)
        if m_dlk: entry['dislikes'] = m_dlk.group(1).strip()

    # Find story
    if 'story' in [l.lower() for l in lines]:
        idx = [l.lower() for l in lines].index('story')
        entry['story'] = " ".join(lines[idx+1:idx+6])
    else:
        # Just grab middle lines
        entry['story'] = " ".join(lines[1:6])
        
    parsed_entries.append(entry)

print("=== DETTAGLIO COMPLETO DI TUTTE LE SEZIONI E MAPPATURA NEL VERSE ===\n")
for p in parsed_entries:
    title = p['title']
    clean_name = title.split()[0].capitalize()
    
    # Check if exists in characters, lexicon or locations
    match_char = None
    for k, c in existing_chars.items():
        if clean_name.lower() in k:
            match_char = c.get('name') or c.get('display_name')
            break
            
    match_lex = None
    for k, l in existing_lex.items():
        if clean_name.lower() in k:
            match_lex = l.get('name')
            break

    print(f"■ {p['title'].upper()} ({p['sec_id']})")
    print(f"  Specie: {p['species'] or 'N/A'} | Età: {p['age'] or 'N/A'} | Altezza: {p['height'] or 'N/A'} | Ruolo: {p['occupation'] or 'N/A'}")
    print(f"  Nazionalità: {p['nationality'] or 'N/A'}")
    if p['likes']: print(f"  Likes: {p['likes']}")
    if p['dislikes']: print(f"  Dislikes: {p['dislikes']}")
    print(f"  Immagini disponibili: {len(p['images'])}")
    for img in p['images']:
        print(f"    * [{img['alt']}] {img['url']}")
    print(f"  Story snippet: {p['story'][:180]}...")
    
    status = "NUOVO (Da inserire)"
    if match_char:
        status = f"PRESENTE COME CHARACTER: {match_char}"
    elif match_lex:
        status = f"PRESENTE COME LEXICON: {match_lex}"
    print(f"  >>> STATO NEL WORLD: {status}\n")
