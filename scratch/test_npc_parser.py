import json, re

def parse_raw_npc_content(raw_text):
    data = {}
    lines = raw_text.splitlines()
    current_key = None
    current_val = []
    
    for line in lines:
        if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
            parts = line.split(':', 1)
            k = parts[0].strip()
            # check if it looks like a known field
            known_fields = ['Name', 'Alias/Nickname', 'Age', 'Gender', 'Species/Race', 'Height', 'Build', 
                            'Hair', 'Eyes', 'Skin', 'Scars', 'Origin', 'Place of Birth', 'Birthdate', 
                            'Personality', 'Strengths', 'Weaknesses', 'Flaws', 'Fears', 'Quirks', 
                            'Habits', 'Powers', 'Unique Triats', 'Unique Traits', 'Education', 'Training', 
                            'Past Occupation/Role', 'Physical Skills', 'Personal Items of Note', 
                            'Favorite Things', 'Pet Peeves', 'Fun Fact', 'Secret', 'Philosophy', 
                            'Motivation', 'Backstory']
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

def clean_text(t):
    if not t: return ""
    # replace em-dashes
    t = t.replace('—', ', ').replace('–', '-')
    # remove markdown bold/italics
    t = t.replace('**', '').replace('*', '')
    # replace double spaces
    t = re.sub(r' +', ' ', t)
    return t.strip()

# Test on index 111 (Avery Calder) and index 191 (Mara Voss)
live_npc = json.load(open('scratch/live_raw_npc_secondary.json', encoding='utf-8'))['lexicon']
camper_data = parse_raw_npc_content(live_npc[111]['content'])
staff_data = parse_raw_npc_content(live_npc[191]['content'])

print("Camper parsed keys:", list(camper_data.keys()))
print("Camper Name:", camper_data.get('Name'))
print("Camper Age:", camper_data.get('Age'))
print("Camper Powers:", camper_data.get('Powers')[:80])

print("\nStaff parsed keys:", list(staff_data.keys()))
print("Staff Name:", staff_data.get('Name'))
print("Staff Age:", staff_data.get('Age'))
