import json, re, time, requests, sys

FALLBACK_AVATAR = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"

COLLIDING_NAMES = {
    'jasper', 'noah', 'miles', 'silas', 'marcus', 'alistair', 'evan', 'adrian',
    'elizabeth', 'erik', 'malachia', 'logan', 'alyssa', 'wulfnic', 'edric',
    'stan', 'russ', 'jared', 'scarlett', 'sierra', 'mackenzie', 'jas', 'lys', 'mal', 'ed'
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
    is_staff = 'Staff' in raw_name or 'Counselor' in raw_name
    is_camper = 'Camper' in raw_name
    
    clean_name = raw_name
    clean_name = re.sub(r'^[\s\U00010000-\U0010ffff\u2600-\u27ff🧑👤\-\—]+\s*', '', clean_name)
    clean_name = re.sub(r'^(Camper|Staff)\s*[\—\-]\s*', '', clean_name).strip()
    
    full_name = clean_text(p.get('Name', clean_name))
    if not full_name: full_name = clean_name
    
    parts = full_name.split()
    first_name = parts[0] if parts else clean_name
    last_name = parts[-1] if len(parts) > 1 else ""
    
    nickname = clean_text(p.get('Alias/Nickname', ''))
    nicknames = [n.strip() for n in nickname.split(',') if n.strip()] if nickname else []
    
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
    
    # JED+ content
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
    
    rpg_block = f"RPG STATS & TRAITS:\n[LEVEL: {level_val}; SPECIES: {species}; OCCUPATION: Camp Mystic {role}]\n- Supernatural Gifts: {powers[:160]}\n- Innate Resilience: {unique_traits[:160] if unique_traits else 'Supernatural fortitude and resistance.'}\n- Camp Protocol & Conditioning: Rigorous supernatural control drills, first-aid fundamentals, and wilderness camp conditioning."
    content_blocks.append(rpg_block)
    
    final_content = "\n\n".join(content_blocks)
    
    # Keys sanitization
    raw_keys = entry.get('keys', [])
    clean_keys = []
    clean_keys.append(clean_name)
    if full_name and full_name != clean_name:
        clean_keys.append(full_name)
        
    for k in raw_keys:
        k_clean = clean_text(k).strip()
        if not k_clean: continue
        if k_clean.lower() in COLLIDING_NAMES:
            continue
        if ' ' not in k_clean and len(k_clean) < 5:
            continue
        if k_clean not in clean_keys:
            clean_keys.append(k_clean)
            
    prefix_key = f"{'Counselor' if is_staff else 'Camper'} {clean_name}"
    if prefix_key not in clean_keys:
        clean_keys.append(prefix_key)
        
    regex_names = [re.escape(clean_name)]
    if full_name and full_name != clean_name:
        regex_names.append(re.escape(full_name))
    for nk in nicknames:
        if nk.lower() not in COLLIDING_NAMES and len(nk) >= 3:
            regex_names.append(re.escape(nk))
    if is_staff:
        if first_name.lower() not in COLLIDING_NAMES:
            regex_names.append(re.escape(f"Counselor {first_name}"))
        if last_name:
            regex_names.append(re.escape(f"Counselor {last_name}"))
        
    regex_pattern = r"(?:^|\n)\s*(?:" + "|".join(regex_names) + r")\s*:"
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
        'nicknames': [nk for nk in nicknames if nk.lower() not in COLLIDING_NAMES],
        'titles': titles
    }
    return entry

def build_location_entry(entry):
    raw_name = entry.get('name', '')
    clean_name = re.sub(r'^[\s\U00010000-\U0010ffff\u2600-\u27ff🚐🌙🌲🧺🪟🛋💻🎨🤸🏀🏊🏢🧪🖥🩺🩸🛡🌊🛶🔥🎣🛖\-\—]+\s*', '', raw_name).strip()
    clean_name = clean_text(clean_name)
    
    # Refine cabin titles: 'G-01 Moonflower Cabin , Built-In Roster' -> 'G-01 Moonflower Cabin (Girls Zone)'
    if 'Cabin , Built-In Roster' in clean_name or 'Cabin - Built-In Roster' in clean_name:
        clean_name = clean_name.replace(' , Built-In Roster', '').replace(' - Built-In Roster', '').strip()
        if clean_name.startswith('G-'):
            clean_name = f"{clean_name} (Girls Zone)"
        elif clean_name.startswith('B-'):
            clean_name = f"{clean_name} (Boys Zone)"
    elif 'Rec Hall , Glass' in clean_name or 'Rec Hall - Glass' in clean_name:
        clean_name = "Rec Hall (Camp Mystic)"
    elif 'Feeding & Donor Center , Facility' in clean_name:
        clean_name = "Feeding & Donor Center"
        
    raw_content = entry.get('content', '')
    clean_content = clean_text(raw_content)
    
    raw_keys = entry.get('keys', [])
    clean_keys = []
    if clean_name not in clean_keys:
        clean_keys.append(clean_name)
        
    for k in raw_keys:
        k_clean = clean_text(k).strip()
        if not k_clean: continue
        if k_clean.lower() in COLLIDING_NAMES: continue
        if k_clean not in clean_keys:
            clean_keys.append(k_clean)
            
    entry['name'] = clean_name
    entry['type'] = 'location'
    entry['content'] = clean_content
    entry['keys'] = clean_keys
    return entry

def main():
    print("=== STARTING CAMP MYSTIC REMEDIATION & STANDARDIZATION ===")
    
    # 1. NPC SECONDARY
    print("\n--- 1. Processing Svartulfr_NPC_Secondary.json ---")
    live_npc_raw = json.load(open('scratch/live_raw_npc_secondary.json', encoding='utf-8'))
    lexicon_npc = live_npc_raw['lexicon']
    print(f"Total entries in live: {len(lexicon_npc)}")
    
    remediated_npc = []
    # keep first 111 intact
    for i in range(111):
        remediated_npc.append(lexicon_npc[i])
        
    # standardize 111 through 210 (100 entries)
    for i in range(111, len(lexicon_npc)):
        remediated_npc.append(build_npc_entry(lexicon_npc[i]))
        
    print(f"Processed NPC Secondary lexicon: {len(remediated_npc)} entries (111 original + {len(remediated_npc)-111} standardized)")
    
    live_npc_raw['lexicon'] = remediated_npc
    live_npc_raw['entries'] = remediated_npc # keep both in local file
    
    with open('FINAL/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
        json.dump(live_npc_raw, f, indent=2, ensure_ascii=False)
    with open('lorebooks/optimized/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
        json.dump(live_npc_raw, f, indent=2, ensure_ascii=False)
    print("Saved to FINAL/ and lorebooks/optimized/ for NPC Secondary.")

    # 2. LOCATION
    print("\n--- 2. Processing Svartulfr_Location.json ---")
    live_loc_raw = json.load(open('scratch/live_raw_location.json', encoding='utf-8'))
    lexicon_loc = live_loc_raw['lexicon']
    print(f"Total entries in live: {len(lexicon_loc)}")
    
    remediated_loc = []
    # keep first 188 intact
    for i in range(188):
        remediated_loc.append(lexicon_loc[i])
        
    # standardize 188 through 224 (37 entries)
    for i in range(188, len(lexicon_loc)):
        remediated_loc.append(build_location_entry(lexicon_loc[i]))
        
    print(f"Processed Location lexicon: {len(remediated_loc)} entries (188 original + {len(remediated_loc)-188} standardized)")
    
    live_loc_raw['lexicon'] = remediated_loc
    live_loc_raw['entries'] = remediated_loc
    
    with open('FINAL/Svartulfr_Location.json', 'w', encoding='utf-8') as f:
        json.dump(live_loc_raw, f, indent=2, ensure_ascii=False)
    with open('lorebooks/optimized/Svartulfr_Location.json', 'w', encoding='utf-8') as f:
        json.dump(live_loc_raw, f, indent=2, ensure_ascii=False)
    print("Saved to FINAL/ and lorebooks/optimized/ for Location.")

    # 3. WYVERN API DEPLOYMENT
    print("\n--- 3. Deploying to Wyvern Web API ---")
    token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    # Deploy NPC Secondary: _Uht3Ckz44JBDrPnUHq7LV
    payload_npc = {
        'name': live_npc_raw.get('name', 'Svartúlfr - NPC Secondary'),
        'description': live_npc_raw.get('description', ''),
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'lexicon': remediated_npc
    }
    print("Sending PUT for NPC Secondary (_Uht3Ckz44JBDrPnUHq7LV)...")
    r_put_npc = requests.put('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers, json=payload_npc)
    print("PUT NPC Secondary response:", r_put_npc.status_code)
    if r_put_npc.status_code != 200:
        print("Error details:", r_put_npc.text[:300])
        sys.exit(1)
        
    time.sleep(2.5)
    
    # Deploy Location: _EjXxkmPVhpCXg8xABpFkK
    payload_loc = {
        'name': live_loc_raw.get('name', 'Svartúlfr - Location'),
        'description': live_loc_raw.get('description', ''),
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'lexicon': remediated_loc
    }
    print("Sending PUT for Location (_EjXxkmPVhpCXg8xABpFkK)...")
    r_put_loc = requests.put('https://app.wyvern.chat/api/lorebooks/_EjXxkmPVhpCXg8xABpFkK', headers=headers, json=payload_loc)
    print("PUT Location response:", r_put_loc.status_code)
    if r_put_loc.status_code != 200:
        print("Error details:", r_put_loc.text[:300])
        sys.exit(1)
        
    time.sleep(2.5)

    # 4. Deploy Master Scenario: char_scenario_1DC43ggb6mB8YLJDJKrU4
    print("Deploying updated Master Scenario...")
    r_scen_get = requests.get('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=headers)
    if r_scen_get.status_code == 200:
        live_scen_data = r_scen_get.json()
        current_rev = live_scen_data.get('revision', 0)
        print(f"Current live Scenario revision: {current_rev}")
        
        local_scen = json.load(open('FINAL/Svartulfr_Master_Scenario.json', encoding='utf-8'))
        local_scen['revision'] = current_rev
        
        r_scen_put = requests.put('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=headers, json=local_scen)
        print("PUT Scenario response:", r_scen_put.status_code)
        if r_scen_put.status_code == 200:
            new_rev = r_scen_put.json().get('revision')
            print(f"Scenario updated to revision: {new_rev}")
            local_scen['revision'] = new_rev
            json.dump(local_scen, open('FINAL/Svartulfr_Master_Scenario.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
            json.dump(local_scen, open('exports/Master_Scenario_Export.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
            
    time.sleep(2.5)

    # 5. POST-DEPLOY VERIFICATION VIA GET
    print("\n--- 4. Post-Deploy GET Verification ---")
    v_npc = requests.get('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers).json()
    v_loc = requests.get('https://app.wyvern.chat/api/lorebooks/_EjXxkmPVhpCXg8xABpFkK', headers=headers).json()
    
    print(f"Verified Live NPC Secondary count: {len(v_npc.get('lexicon', []))} (Expected: 211)")
    print(f"Verified Live Location count: {len(v_loc.get('lexicon', []))} (Expected: 225)")
    
    print("\n=== SUCCESS: ALL REMEDIATIONS DEPLOYED & VERIFIED ===")

if __name__ == '__main__':
    main()
