import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/modernfantasy_portal_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

world_characters = {c['name'].lower(): c for c in world_data['world_characters'] if c.get('name')}
world_lexicon = {l['name'].lower(): l for l in world_data['world_lexicon_entries'] if l.get('name')}
world_locations = {loc['name'].lower(): loc for loc in world_data['world_locations'] if loc.get('name')}

detailed_roster = []

for sec_id, v in data['characters'].items():
    text = v['text']
    images = v['images']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # Try to extract structured data from lines
    info = {
        'sec_id': sec_id,
        'name': lines[0] if lines else sec_id,
        'species': None,
        'nationality': None,
        'age': None,
        'height': None,
        'occupation': None,
        'likes': None,
        'dislikes': None,
        'story': [],
        'related': [],
        'images': images,
        'world_match': None,
        'world_type': None
    }
    
    current_key = None
    collecting_story = False
    
    for idx, line in enumerate(lines):
        if line.lower() == 'story':
            collecting_story = True
            continue
        if line.lower() == 'related characters':
            if idx + 1 < len(lines):
                info['related'].append(lines[idx + 1])
            continue
            
        if ':' in line:
            parts = line.split(':', 1)
            k = parts[0].strip().lower()
            val = parts[1].strip()
            if 'species' in k: info['species'] = val
            elif 'nationality' in k: info['nationality'] = val
            elif 'age' in k: info['age'] = val
            elif 'height' in k: info['height'] = val
            elif 'occupation' in k or 'callsign' in k or 'abilities' in k: info['occupation'] = val
            elif 'likes' in k: info['likes'] = val
            elif 'dislikes' in k: info['dislikes'] = val
        elif collecting_story:
            info['story'].append(line)
        elif not collecting_story and len(line) > 60:
            info['story'].append(line)
            
    info['story_text'] = " ".join(info['story'])
    
    # Check match in World
    name_clean = info['name'].lower()
    for w_name, w_char in world_characters.items():
        if name_clean in w_name or w_name in name_clean:
            info['world_match'] = w_char['name']
            info['world_type'] = 'character'
            info['world_id'] = w_char['id']
            break
            
    if not info['world_match']:
        for l_name, l_entry in world_lexicon.items():
            if name_clean in l_name or l_name in name_clean:
                info['world_match'] = l_entry['name']
                info['world_type'] = 'lexicon'
                info['world_id'] = l_entry['id']
                break
                
    detailed_roster.append(info)

output_analysis = 'exports/modernfantasy_analyzed_roster.json'
with open(output_analysis, 'w', encoding='utf-8') as f:
    json.dump(detailed_roster, f, indent=2, ensure_ascii=False)

print(f"Analisi completata per {len(detailed_roster)} entità. Salvata in {output_analysis}.")

for item in detailed_roster:
    status_str = f"MATCH: [{item['world_type']}] {item['world_match']} ({item.get('world_id')})" if item['world_match'] else "DA INTEGRARE (Nuovo)"
    print(f"[{item['sec_id']}] {item['name']} | Sp: {item['species']} | Età: {item['age']} | Img: {len(item['images'])} | {status_str}")
