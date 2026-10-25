import json
import re

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    prim_data = json.load(f)
with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec_data = json.load(f)

cm_card = json.load(open('scratch/campmystic_full_card.json', 'r', encoding='utf-8'))
cm_lb = [lb for lb in cm_card['lorebooks'] if lb['name'] == 'Camp Mystic'][0]['entries']

raw_cm_map = {}
for e in cm_lb:
    rname = e.get('name', '')
    if 'Camper' in rname or 'Staff' in rname or 'Counselor' in rname:
        if 'Boundaries' in rname or 'Roster' in rname or 'Population' in rname:
            continue
        cname = re.sub(r'^[\s\U00010000-\U0010ffff\u2600-\u27ff🧑👤🚐🌙🌲🧺🪟🛋💻🎨🤸🏀🏊🏢🧪🖥🩺🩸🛡🌊🛶🔥🎣🛖\-\—]+\s*', '', rname)
        cname = re.sub(r'^(Camper|Staff)\s*[\—\-]\s*', '', cname).strip()
        raw_cm_map[cname] = e

def clean_text(t):
    if not t:
        return ""
    t = t.replace('—', ', ').replace('–', '-')
    t = t.replace('**', '').replace('*', '')
    t = re.sub(r' +', ' ', t)
    return t.strip().rstrip('.').strip()

def fix_they_grammar(t):
    replacements = {
        'they assumes': 'they assume',
        'they confuses': 'they confuse',
        'they expects': 'they expect',
        'they forgets': 'they forget',
        'they gets': 'they get',
        'they hides': 'they hide',
        'they manipulates': 'they manipulate',
        'they misses': 'they miss',
        'they needs': 'they need',
        'they overthinks': 'they overthink',
        'they resists': 'they resist',
        'they spirals': 'they spiral',
        'they suppresses': 'they suppress',
        'they takes': 'they take',
        'they treats': 'they treat',
        'they turns': 'they turn',
        'they underestimates': 'they underestimate',
        'they uses': 'they use',
        'they withdraws': 'they withdraw',
        'They assumes': 'They assume',
        'They confuses': 'They confuse',
        'They expects': 'They expect',
        'They forgets': 'They forget',
        'They gets': 'They get',
        'They hides': 'They hide',
        'They manipulates': 'They manipulate',
        'They misses': 'They miss',
        'They needs': 'They need',
        'They overthinks': 'They overthink',
        'They resists': 'They resist',
        'They spirals': 'They spiral',
        'They suppresses': 'They suppress',
        'They takes': 'They take',
        'They treats': 'They treat',
        'They turns': 'They turn',
        'They underestimates': 'They underestimate',
        'They uses': 'They use',
        'They withdraws': 'They withdraw',
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t

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

def rebuild_camp_mystic_content(clean_name, raw_entry):
    raw_content = raw_entry.get('content', '')
    p = parse_raw_npc_content(raw_content)
    rname = raw_entry.get('name', '')
    is_staff = 'Staff' in rname or 'Counselor' in rname
    
    full_name = clean_text(p.get('Name', clean_name)) or clean_name
    parts = clean_name.split()
    first_name = parts[0] if parts else clean_name
    
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
    
    # Shift camper birthdates by -2 years so Age 18-22 aligns with 2024 World Clock, and avoid Jan 1 / 1st of month
    for y_old, y_new in [('2008', '2006'), ('2007', '2005'), ('2006', '2004'), ('2005', '2003'), ('2004', '2002')]:
        if y_old in birthdate:
            birthdate = birthdate.replace(y_old, y_new)
            break
    # Replace 1st of month (Rule 9.6) with varied realistic days
    day_offsets = {
        'Avery Calder': '14',
        'Yasmin Nadir': '17',
        'Dahlia Cross': '19',
        'Ember Hale': '12',
        'Nico Reed': '16',
        'Orin Bell': '22',
        'Emmett Cole': '15',
        'Jasper Rowan': '18',
        'Oona Hart': '14',
        'Ren Amari': '19',
    }
    if re.search(r'\b1,', birthdate):
        new_day = day_offsets.get(clean_name, '14')
        birthdate = re.sub(r'\b1,', f'{new_day},', birthdate)

    birthplace = clean_text(p.get('Place of Birth', 'Unknown'))
    origin = clean_text(p.get('Origin', ''))
    powers = clean_text(p.get('Powers', 'Supernatural physiology'))
    unique_traits = clean_text(p.get('Unique Triats') or p.get('Unique Traits', ''))
    
    role = "Counselor / Staff" if is_staff else "Camper"
    edu = clean_text(p.get('Education', 'Camp Mystic Residential Program'))
    past_role = clean_text(p.get('Past Occupation/Role', ''))
    cabin_match = re.search(r'[GB]-\d+\s+[A-Za-z\s]+Cabin', edu)
    cabin_info = cabin_match.group().strip() if cabin_match else ("Staff Lodge" if is_staff else "Residential Zone")
    
    personality = fix_they_grammar(clean_text(p.get('Personality', '')))
    strengths = fix_they_grammar(clean_text(p.get('Strengths', '')))
    weaknesses = fix_they_grammar(clean_text(p.get('Weaknesses', '')))
    # Fix lowercase or mismatched first name in 'recurring weak point is that <name>'
    weaknesses = re.sub(
        r'recurring weak point is that [a-zA-Z]+',
        f'recurring weak point is that {first_name}',
        weaknesses
    )
    flaws = fix_they_grammar(clean_text(p.get('Flaws', '')))
    fears = fix_they_grammar(clean_text(p.get('Fears', '')))
    quirks = fix_they_grammar(clean_text(p.get('Quirks', '')))
    habits = fix_they_grammar(clean_text(p.get('Habits', '')))
    pet_peeves = fix_they_grammar(clean_text(p.get('Pet Peeves', '')))
    favorite_things = fix_they_grammar(clean_text(p.get('Favorite Things', '')))
    fun_fact = fix_they_grammar(clean_text(p.get('Fun Fact', '')))
    secret = fix_they_grammar(clean_text(p.get('Secret', '')))
    secret = secret.replace("Vesper his true Anchor", "Vesper's true Anchor")
    philosophy = fix_they_grammar(clean_text(p.get('Philosophy', ''))).strip('"').strip("'")
    motivation = fix_they_grammar(clean_text(p.get('Motivation', '')))
    backstory = fix_they_grammar(clean_text(p.get('Backstory', '')))
    training = fix_they_grammar(clean_text(p.get('Training', '')))
    physical_skills = fix_they_grammar(clean_text(p.get('Physical Skills', '')))
    items = fix_they_grammar(clean_text(p.get('Personal Items of Note', '')))

    header_block = (
        f"[NAME: {clean_name}; ALIASES: {', '.join([full_name] + nicknames)}; "
        f"SPECIES: {species}; AGE: {age_str} (Born {birthdate}); GENDER: {gender}; "
        f"HEIGHT: {height}; BUILD: {build}; HAIR: {hair}; EYES: {eyes}; SKIN: {skin}; "
        f"SCARS: {scars}.; AFFILIATION: Camp Mystic ({cabin_info}); OCCUPATION: {role}; "
        f"ORIGIN: {birthplace}; POWERS: {powers}.]"
    )

    bg_parts = [f"BACKSTORY: {backstory}."]
    if origin:
        bg_parts.append(f"Origin: {origin}.")
    if past_role:
        bg_parts.append(f"Background & Role: {past_role}.")
    if motivation:
        bg_parts.append(f"Motivation: {motivation}.")
    if secret:
        bg_parts.append(f"Secret: {secret}.")
    if philosophy:
        bg_parts.append(f'Philosophy: "{philosophy}".')
    bg_block = " ".join(bg_parts)

    cc_parts = [f"CLAN AND COMPANY: Affiliated with Camp Mystic ({cabin_info}) as a {role}."]
    if edu:
        cc_parts.append(f"Education & Placement: {edu}.")
    if training:
        cc_parts.append(f"Training: {training}.")
    if physical_skills:
        cc_parts.append(f"Physical Skills: {physical_skills}.")
    if items:
        cc_parts.append(f"Personal Items: {items}.")
    cc_block = " ".join(cc_parts)

    vb_parts = [f"VOICE & BEHAVIOR: {personality}."]
    if quirks:
        vb_parts.append(f"Quirks: {quirks}.")
    if habits:
        vb_parts.append(f"Habits: {habits}.")
    if pet_peeves:
        vb_parts.append(f"Pet Peeves: {pet_peeves}.")
    if favorite_things:
        vb_parts.append(f"Favorite Things: {favorite_things}.")
    if fun_fact:
        vb_parts.append(f"Fun Fact: {fun_fact}.")
    vb_block = " ".join(vb_parts)

    sw_parts = ["STRENGTHS & WEAKNESSES:"]
    if strengths:
        sw_parts.append(f"Strengths: {strengths}.")
    if weaknesses:
        sw_parts.append(f"Weaknesses: {weaknesses}.")
    if flaws:
        sw_parts.append(f"Flaws: {flaws}.")
    if fears:
        sw_parts.append(f"Fears: {fears}.")
    sw_block = " ".join(sw_parts)

    rpg_block = (
        f"RPG STATS & TRAITS:\n"
        f"[LEVEL: {level_val}; SPECIES: {species}; OCCUPATION: Camp Mystic {role}]\n"
        f"- Supernatural Gifts: {powers}.\n"
        f"- Innate Resilience: {unique_traits if unique_traits else 'Supernatural fortitude and resistance'}.\n"
        f"- Camp Protocol & Conditioning: Rigorous supernatural control drills, first-aid fundamentals, and wilderness camp conditioning."
    )

    return "\n\n".join([header_block, bg_block, cc_block, vb_block, sw_block, rpg_block])

# 1. Process Primary
prim_entries = prim_data['entries']
for idx, e in enumerate(prim_entries):
    c = e['content']
    name = e['name']
    if name == 'Marek':
        c = c.replace('TERRITORIAL INSTINCTS & Alyssa:', 'CLAN AND COMPANY:')
    elif name in ('Kian', 'Goran', 'Radek'):
        c = c.replace('SQUAD & BROTHERHOOD:', 'CLAN AND COMPANY:')
    elif name == 'Echo':
        c = c.replace('CORE FUNCTIONS & CYBERSPACE WARFARE:', 'BACKSTORY:')
        c = c.replace('MONITORING SYSTEM & FAMILIAR PROTOCOLS:', 'FAMILY & PACK:')
        c = c.replace('PERSONALITY & HUMOR:', 'VOICE & BEHAVIOR:')
    elif name == 'Dominic Rogers':
        c = c.replace('\nFAMILY:', '\nFAMILY & PACK:')
    elif name in ('Scarlett Rose', 'Sierra Cruz'):
        c = c.replace('DORM DYNAMICS & ROOMMATES:', 'CLAN AND COMPANY:')
    elif name == "Russell 'Russ' Sinclair":
        if 'CLAN AND COMPANY:' not in c:
            c = c.replace(
                '\nVOICE & BEHAVIOR:',
                '\nCLAN AND COMPANY: Russ splits his life between Sacred Needle Tattoo, where he works as an apprentice artist, and Wyrm Hall Room 304 on the SUCC campus, which he shares with his best friend Jasper Douglas Bloodmoon. He is a founding member of The Five Cocketeers alongside Jasper, Jared Thompson, Stanislas Kowalski, and Finn Novak, serving as the grounded, deadpan voice of reason whenever supernatural chaos erupts.\n\nVOICE & BEHAVIOR:'
            )
    elif name == 'Daniel "Danny" Boone':
        c = c.replace('THE BALLANTINE FAMILY:', 'FAMILY & PACK:')
        if 'VOICE & BEHAVIOR:' not in c:
            c += '\n\nVOICE & BEHAVIOR: Rough, working-class English accent, blunt and unpretentious. He speaks with his fists first when threatened, wears his heart on his sleeve around the people he trusts, and cannot hide his emotions when his wolf tail starts wagging.'
    elif name == 'Zero':
        c = c.replace('LIFE IN THE SINNERS:', 'CLAN AND COMPANY:')
        c = c.replace('a target rather than a person\n', 'a target rather than a person.\n')
        c = c.replace('before he can have sex\n', 'before he can have sex.\n')
        if c.endswith('before he can have sex'):
            c += '.'
    e['content'] = c

# 2. Process Secondary
sec_entries = sec_data['entries']

# Mapping of non-Camp-Mystic Secondary headers to FAMILY & PACK: or CLAN AND COMPANY:
sec_header_map = {
    'Jet Thompson': ('FAMILY & CONNECTIONS:', 'FAMILY & PACK:'),
    'Alicia Virtuoso': ('THE VIRTUOSO NAME:', 'CLAN AND COMPANY:'),
    'Allegra Lumsden': ('THE REGRET SHE HIDES:', 'CLAN AND COMPANY:'),
    'Ariadne Cirillo': ('THE NURSE:', 'CLAN AND COMPANY:'),
    'Luisa Sanchez Rogers': ('FAMILY & BROTHERHOOD:', 'FAMILY & PACK:'),
    'Alistair Ambrose DeVille': ('FAMILY & SYNDICATE:', 'CLAN AND COMPANY:'),
    'Adelin Coso': ('\nFAMILY:', '\nFAMILY & PACK:'),
    'Brittany Willow': ('HER PLACE IN BLACKWOOD:', 'CLAN AND COMPANY:'),
    'Hideo Reid': ('LIFE AT SUCC:', 'CLAN AND COMPANY:'),
    'Professor Marit Christiansen': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Professor Mollusk Moreau': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Rev': ('WHAT HE PROTECTS:', 'CLAN AND COMPANY:'),
    'Fenris': ('THE CHILDREN AND THE FAITH:', 'CLAN AND COMPANY:'),
    'Yael': ('CLAN AND LOYALTY:', 'CLAN AND COMPANY:'),
    "Eithne Dal'Kereth": ('SYNDICATE & ALLIANCES:', 'CLAN AND COMPANY:'),
    'Ren': ('CLAN & SOCIAL CIRCLE:', 'CLAN AND COMPANY:'),
    'Aiden Anderson': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Alad C.': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Aris Thorne': ('HIS PLACE IN BLACKWOOD:', 'CLAN AND COMPANY:'),
    'Arturo Cardona': ('RELATIONSHIPS:', 'CLAN AND COMPANY:'),
    'August Reed': ('CURRENT LIFE:', 'CLAN AND COMPANY:'),
    'Bram Beaumont': ('FAMILY & FARM:', 'FAMILY & PACK:'),
    'Caim Morningstar': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Cyrus Camden': ('\nFAMILY:', '\nFAMILY & PACK:'),
    'Emil': ('\nFAMILY:', '\nFAMILY & PACK:'),
    'Eric Grey': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Gabriel': ('FAMILY & POD:', 'FAMILY & PACK:'),
    'Gianni Luciano': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Jake Thompson': ('FAMILY ROLE:', 'FAMILY & PACK:'),
    'Jayce Collins': ('FAMILY & FRIENDSHIP:', 'CLAN AND COMPANY:'),
    'Julian Bieri': ('\nFAMILY:', '\nFAMILY & PACK:'),
    'Kade Leavis': ('THE OTHERS:', 'CLAN AND COMPANY:'),
    'Lennox McKay': ('FAMILY & FARM:', 'FAMILY & PACK:'),
    'Levi Graham': ('FAMILY & CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Neon Purr': ('CREW AND COMPANY:', 'CLAN AND COMPANY:'),
    'Nic Lucero': ('CURRENT LIFE:', 'CLAN AND COMPANY:'),
    'Nickolas Wolffe': ('FAMILY & CONNECTIONS:', 'FAMILY & PACK:'),
    'Professor Dryden Kiwetin': ('ORIGIN & NATURE:', 'CLAN AND COMPANY:'),
    'Rafael Callaway': ('THE SQUAD:', 'CLAN AND COMPANY:'),
    'Rhett Moore': ('FAMILY & FRIENDSHIP:', 'CLAN AND COMPANY:'),
    'Rue': ('\nFAMILY:', '\nFAMILY & PACK:'),
    'Sawyer Shephard': ('THE HACK HE NEVER FORGOT:', 'CLAN AND COMPANY:'),
    'Siebren Dijkstra': ('DIJKSTRA RISK SOLUTIONS:', 'CLAN AND COMPANY:'),
    'Vale Roberts': ('CONNECTIONS:', 'CLAN AND COMPANY:'),
    'Vargus "The Red"': ('CLUB AND CREW:', 'CLAN AND COMPANY:'),
    'Bartholomew': ('THE HOUSEHOLD:', 'CLAN AND COMPANY:'),
    'Madge': ('THE HOUSEHOLD:', 'CLAN AND COMPANY:'),
    'Angui': ('ISOLATION:', 'CLAN AND COMPANY:'),
    'Finn the Satyr': ('COMMUNITY & TIES:', 'CLAN AND COMPANY:'),
    'Wren Lark': ('ALLIES & HORNS COMMUNITY:', 'CLAN AND COMPANY:'),
    'Zaire Ziisis': ('CLAN AND ACADEMY:', 'CLAN AND COMPANY:'),
    'Xaiden Nershatar': ('ACADEMY AND FACULTY:', 'CLAN AND COMPANY:'),
    'Lestat Oreven': ('ACADEMY AND PEERS:', 'CLAN AND COMPANY:'),
    'Caien Vaelion': ('ACADEMY AND STUDIES:', 'CLAN AND COMPANY:'),
    'Aeril Royen': ('ACADEMY AND RIVALRIES:', 'CLAN AND COMPANY:'),
    'Amerian de Vian': ('ACADEMY AND LABS:', 'CLAN AND COMPANY:'),
    'Ashton Crowley': ('ACADEMY AND RIVALRIES:', 'CLAN AND COMPANY:'),
    'Thrakgor Deathspine': ('CLAN AND ALLIANCES:', 'CLAN AND COMPANY:'),
    'Crowe': ('CREW AND CONTRACTS:', 'CLAN AND COMPANY:'),
    'Morgeth Steeltooth': ('FORGE AND FRIENDS:', 'CLAN AND COMPANY:'),
    'Thorvald': ('PACK AND SOVEREIGNTY:', 'FAMILY & PACK:'),
    'Harald Sigurdsson': ('CLAN AND COMMAND:', 'CLAN AND COMPANY:'),
}

for idx, e in enumerate(sec_entries):
    name = e['name']
    c = e['content']
    if idx >= 111:
        raw_e = raw_cm_map[name]
        e['content'] = rebuild_camp_mystic_content(name, raw_e)
        continue

    if name in sec_header_map:
        old_h, new_h = sec_header_map[name]
        c = c.replace(old_h, new_h, 1)
    elif name == 'Coach Mithers':
        c = c.replace('WHAT THE SOURCES SAY:', 'BACKSTORY:')
        c = c.replace('HOW SHE READS:', 'VOICE & BEHAVIOR:')
        c = c.replace('USE HER FOR:', 'CLAN AND COMPANY:')
    elif name == 'Kobal':
        c = c.replace('BEHAVIOR & DUTIES:', 'BACKSTORY:')
        c = c.replace('DEFENSE & LOYALTY:', 'FAMILY & PACK:')
        c += '\n\nVOICE & BEHAVIOR: Silent, immaculate, and frictionless in motion. Kobal communicates through understated gestures and quiet, formal deference, enforcing sanctuary boundaries with icy supernatural decorum.'
    elif name == 'Kai Mitchell':
        c = c.replace('WHO HE IS:', 'BACKSTORY:')
        c = c.replace('HOW HE COMES ACROSS:', 'VOICE & BEHAVIOR:')
        c = c.replace('USE HIM FOR:', 'CLAN AND COMPANY:')
    elif name == 'Miles Airhardt':
        c = c.replace('COMMAND STYLE:', 'VOICE & BEHAVIOR:')
        c = c.replace('HIS SQUAD:', 'CLAN AND COMPANY:')
    elif name == 'Coach Mack':
        c = c.replace('\nVOICE & BEHAVIOR:', '\nCLAN AND COMPANY: Assistant Head Coach and Offensive Coordinator of the SUCC Bulls Football Team, working alongside Head Coach Dullahan and mentoring quarterback Jared Thompson.\n\nVOICE & BEHAVIOR:')
    elif name == 'Rick Howell':
        c = c.replace('\nVOICE & BEHAVIOR:', '\nCLAN AND COMPANY: Member of the Beta Rho Omega (BRO) Fraternity and backup quarterback for the SUCC Bulls, sharing locker room camaraderie and friendly rivalry with starter Jared Thompson.\n\nVOICE & BEHAVIOR:')
    elif name == 'Ilya Volkov':
        c = c.replace('\nVOICE & BEHAVIOR:', '\nCLAN AND COMPANY: Independent mercenary and heavy muscle operating in the Paradise District underworld, frequently contracted by Ruaraidh Ballantine and the Ballantine Crime Syndicate for high-risk enforcement.\n\nVOICE & BEHAVIOR:')
    elif name in ('Julie Thompson', 'Jerry Thompson', 'Jeremy Thompson', 'Jason Thompson', 'Jaiden Thompson'):
        c = c.replace('\nVOICE & BEHAVIOR:', '\nFAMILY & PACK: Member of the tight-knit Thompson family of Solarton, raised by parents Hank and Jasmin Thompson alongside seven brothers and two sisters in a boisterous, fiercely protective household.\n\nVOICE & BEHAVIOR:')
    elif name == 'Venera Dolce':
        c = c.replace('\nVOICE & BEHAVIOR:', '\nCLAN AND COMPANY: Archaeology major at SUCC, member of the gold-uniformed SUCC Cheerleading Squad alongside Janice Thompson, and active sister in the Chi Omicron Omega Mu sorority.\n\nVOICE & BEHAVIOR:')

    e['content'] = c

prim_data['lexicon'] = prim_data['entries']
sec_data['lexicon'] = sec_data['entries']

with open('FINAL/Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
    json.dump(prim_data, f, ensure_ascii=False, indent=2)
with open('FINAL/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
    json.dump(sec_data, f, ensure_ascii=False, indent=2)

with open('lorebooks/optimized/Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
    json.dump(prim_data, f, ensure_ascii=False, indent=2)
with open('lorebooks/optimized/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
    json.dump(sec_data, f, ensure_ascii=False, indent=2)

print("Successfully remediated and synchronized all 310 entries in FINAL/ and lorebooks/optimized/!")
