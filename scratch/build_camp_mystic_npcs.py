import json, re

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

COLLIDING_NAMES = {
    'jasper': 'Jasper Rowan',
    'noah': 'Noah Grant',
    'miles': 'Miles Black',
    'silas': 'Silas Thorne',
    'marcus': 'Marcus Vale',
    'alistair': 'Alistair Grant',
    'evan': 'Evan Voss',
    'adrian': 'Adrian Quinn',
    'elizabeth': 'Elizabeth',
    'erik': 'Erik',
    'malachia': 'Malachia',
    'logan': 'Logan',
    'alyssa': 'Alyssa',
    'wulfnic': 'Wulfnic',
    'edric': 'Edric',
    'stan': 'Stan',
    'russ': 'Russ',
    'jared': 'Jared',
    'scarlett': 'Scarlett',
    'sierra': 'Sierra',
    'mackenzie': 'Mackenzie'
}

def clean_text(t):
    if not t: return ""
    t = t.replace('—', ', ').replace('–', '-')
    t = t.replace('**', '').replace('*', '')
    t = re.sub(r' +', ' ', t)
    return t.strip()

def parse_raw_npc_content(raw_text):
    data = {}
    lines = raw_text.splitlines()
    current_key = None
    current_val = []
    
    known_fields = ['Name', 'Alias/Nickname', 'Age', 'Gender', 'Species/Race', 'Height', 'Build', 
                    'Hair', 'Eyes', 'Skin', 'Scars', 'Origin', 'Place of Birth', 'Birthdate', 
                    'Personality', 'Strengths', 'Weaknesses', 'Flaws', 'Fears', 'Quirks', 
                    'Habits', 'Powers', 'Unique Triats', 'Unique Traits', 'Education', 'Training', 
                    'Past Occupation/Role', 'Physical Skills', 'Personal Items of Note', 
                    'Favorite Things', 'Pet Peeves', 'Fun Fact', 'Secret', 'Philosophy', 
                    'Motivation', 'Backstory']
    
    for line in lines:
        if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
            parts = line.split(':', 1)
            k = parts[0].strip()
            if any(k.lower() == kf.lower() for kf in known_fields):
                if current_key:
                    data[current_key] = ' '.join(current_val).strip().rstrip(';')
                current_key = k
                current_val = [parts[1].strip()]
                continue
        if current_key:
            current_val.append(line.strip())
            
    if current_key:
        data[current_key] = ' '.join(current_val).strip().rstrip(';')
        
    return data

def build_npc_entry(entry):
    raw_content = entry.get('content', '')
    p = parse_raw_npc_content(raw_content)
    
    raw_name = entry.get('name', '')
    # clean name from emojis
    is_staff = 'Staff' in raw_name or 'Counselor' in raw_name
    is_camper = 'Camper' in raw_name
    
    clean_name = raw_name
    clean_name = re.sub(r'^[\s\U00010000-\U0010ffff\u2600-\u27ff🧑👤🚐🌙🌲🧺🪟🛋💻🎨🤸🏀🏊🏢🧪🖥🩺🩸🛡🌊🛶🔥🎣🛖\-\—]+\s*', '', clean_name)
    clean_name = re.sub(r'^(Camper|Staff)\s*[\—\-]\s*', '', clean_name).strip()
    
    full_name = clean_text(p.get('Name', clean_name))
    if not full_name: full_name = clean_name
    
    # Names split
    parts = full_name.split()
    first_name = parts[0] if parts else clean_name
    last_name = parts[-1] if len(parts) > 1 else ""
    
    nickname = clean_text(p.get('Alias/Nickname', ''))
    nicknames = [n.strip() for n in nickname.split(',') if n.strip()] if nickname else []
    
    # Age
    age_str = clean_text(p.get('Age', '18'))
    m_age = re.search(r'\d+', age_str)
    age_val = int(m_age.group()) if m_age else 18
    level_val = min(age_val, 99)
    
    species = clean_text(p.get('Species/Race', 'Supernatural'))
    gender = clean_text(p.get('Gender', 'Unknown'))
    height = clean_text(p.get('Height', '5\'8"'))
    build = clean_text(p.get('Build', 'Athletic'))
    hair = clean_text(p.get('Hair', 'Dark'))
    eyes = clean_text(p.get('Eyes', 'Dark'))
    skin = clean_text(p.get('Skin', 'Fair'))
    scars = clean_text(p.get('Scars', 'None'))
    birthdate = clean_text(p.get('Birthdate', 'Unknown'))
    birthplace = clean_text(p.get('Place of Birth', 'Unknown'))
    origin = clean_text(p.get('Origin', ''))
    
    powers = clean_text(p.get('Powers', 'Supernatural physiology'))
    unique_traits = clean_text(p.get('Unique Triats') or p.get('Unique Traits', ''))
    
    role = "Counselor / Staff" if is_staff else "Camper"
    edu = clean_text(p.get('Education', 'Camp Mystic Residential Program'))
    cabin_match = re.search(r'[GB]-\d+\s+[A-Za-z\s]+Cabin', edu)
    cabin_info = cabin_match.group().strip() if cabin_match else ("Staff Lodge" if is_staff else "Residential Zone")
    
    personality = clean_text(p.get('Personality', ''))
    strengths = clean_text(p.get('Strengths', ''))
    weaknesses = clean_text(p.get('Weaknesses', ''))
    flaws = clean_text(p.get('Flaws', ''))
    fears = clean_text(p.get('Fears', ''))
    quirks = clean_text(p.get('Quirks', ''))
    habits = clean_text(p.get('Habits', ''))
    pet_peeves = clean_text(p.get('Pet Peeves', ''))
    favorite_things = clean_text(p.get('Favorite Things', ''))
    secret = clean_text(p.get('Secret', ''))
    philosophy = clean_text(p.get('Philosophy', ''))
    motivation = clean_text(p.get('Motivation', ''))
    backstory = clean_text(p.get('Backstory', ''))
    training = clean_text(p.get('Training', ''))
    physical_skills = clean_text(p.get('Physical Skills', ''))
    items = clean_text(p.get('Personal Items of Note', ''))
    
    # Build clean JED+ content
    content_blocks = []
    header_block = f"[NAME: {clean_name}; ALIASES: {', '.join([full_name] + nicknames)}; SPECIES: {species}; AGE: {age_str} (Born {birthdate}); GENDER: {gender}; HEIGHT: {height}; BUILD: {build}; HAIR: {hair}; EYES: {eyes}; SKIN: {skin}; SCARS: {scars}; AFFILIATION: Camp Mystic ({cabin_info}); OCCUPATION: {role}; ORIGIN: {birthplace}; POWERS: {powers}]"
    content_blocks.append(header_block)
    
    if personality:
        p_block = f"PERSONALITY: {personality}"
        if quirks: p_block += f" Quirks: {quirks}."
        if habits: p_block += f" Habits: {habits}."
        if pet_peeves: p_block += f" Pet Peeves: {pet_peeves}."
        if favorite_things: p_block += f" Favorite Things: {favorite_things}."
        content_blocks.append(p_block)
        
    if strengths or weaknesses or flaws or fears:
        sw_block = f"STRENGTHS & WEAKNESSES: Strengths: {strengths} Weaknesses: {weaknesses} Flaws: {flaws} Fears: {fears}"
        content_blocks.append(sw_block)
        
    bg_block = f"CAMP MYSTIC BACKGROUND & ROLE: {backstory}"
    if training: bg_block += f" Training: {training}."
    if physical_skills: bg_block += f" Physical Skills: {physical_skills}."
    if items: bg_block += f" Personal Items: {items}."
    if secret: bg_block += f" Secret: {secret}."
    if motivation: bg_block += f" Motivation: {motivation}."
    if philosophy: bg_block += f' Philosophy: "{philosophy}".'
    content_blocks.append(bg_block)
    
    # RPG stats
    rpg_block = f"RPG STATS & TRAITS:\n[LEVEL: {level_val}; SPECIES: {species}; OCCUPATION: Camp Mystic {role}]\n- Supernatural Gifts: {powers[:160]}\n- Innate Resilience: {unique_traits[:160] if unique_traits else 'Supernatural fortitude and resistance.'}\n- Camp Protocol & Conditioning: Rigorous supernatural control drills, first-aid fundamentals, and wilderness camp conditioning."
    content_blocks.append(rpg_block)
    
    final_content = "\n\n".join(content_blocks)
    
    # Keys sanitization
    raw_keys = entry.get('keys', [])
    clean_keys = []
    
    # always include full clean name
    clean_keys.append(clean_name)
    if full_name and full_name != clean_name:
        clean_keys.append(full_name)
        
    for k in raw_keys:
        k_clean = clean_text(k).strip()
        if not k_clean: continue
        # CHECK COLLISION: if k_clean matches any single colliding name exactly, SKIP IT!
        if k_clean.lower() in COLLIDING_NAMES:
            continue
        # If key is single word first name and is very common, only keep if not colliding
        if ' ' not in k_clean and len(k_clean) < 5:
            # check if too short/generic
            continue
        if k_clean not in clean_keys:
            clean_keys.append(k_clean)
            
    # Add prefixed role key
    prefix_key = f"{'Counselor' if is_staff else 'Camper'} {clean_name}"
    if prefix_key not in clean_keys:
        clean_keys.append(prefix_key)
        
    # Avatar activation regex
    regex_names = [re.escape(clean_name)]
    if full_name and full_name != clean_name:
        regex_names.append(re.escape(full_name))
    for nk in nicknames:
        if nk.lower() not in COLLIDING_NAMES and len(nk) >= 3:
            regex_names.append(re.escape(nk))
    if is_staff:
        regex_names.append(re.escape(f"Counselor {clean_name.split()[0]}"))
        regex_names.append(re.escape(f"Counselor {last_name}"))
        
    regex_pattern = r"(?:^|\n)\s*(?:" + "|".join(regex_names) + r")\s*:"
    
    # titles
    titles = [f"Camp Mystic {'Counselor' if is_staff else 'Camper'}"]
    
    entry['name'] = clean_name
    entry['type'] = 'npc'
    entry['keys'] = clean_keys
    entry['content'] = final_content
    entry['avatar'] = entry.get('avatar') or FALLBACK_AVATAR
    entry['custom_avatar_regex'] = True
    entry['lines_parsed'] = 1
    entry['avatar_activation_regex'] = regex_pattern
    entry['npc_info'] = {
        'first_name': first_name,
        'last_name': last_name,
        'nicknames': nicknames,
        'titles': titles
    }
    return entry

if __name__ == '__main__':
    live = json.load(open('scratch/live_raw_npc_secondary.json', encoding='utf-8'))['lexicon']
    sample_indices = [111, 150, 188, 191, 210]

    for idx in sample_indices:
        e = live[idx]
        built = build_npc_entry(e)
        print(f"=== INDEX {idx}: {built['name']} ===")
        print("Type:", built['type'])
        print("Keys:", built['keys'])
        print("Avatar regex:", built['avatar_activation_regex'])
        print("NPC info:", built['npc_info'])
        print("Content preview:")
        for line in built['content'].splitlines()[:6]:
            print(" ", line[:120])
        print()
