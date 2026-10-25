import json

live_npc = json.load(open('scratch/live_raw_npc_secondary.json', encoding='utf-8'))['lexicon']
live_loc = json.load(open('scratch/live_raw_location.json', encoding='utf-8'))['lexicon']

out = []
def log(s=""): out.append(str(s))

# Look at sample camper (Avery Calder)
camper_1 = live_npc[111] # first new one
log("=== SAMPLE CAMPER (index 111) ===")
log(f"Name: {camper_1.get('name')}")
log(f"Keys: {camper_1.get('keys')}")
log(f"Avatar: {camper_1.get('avatar')}")
log(f"Type: {camper_1.get('type')}")
log(f"Custom regex: {camper_1.get('custom_avatar_regex')}")
log(f"Avatar regex: {camper_1.get('avatar_activation_regex')}")
log(f"Lines parsed: {camper_1.get('lines_parsed')}")
log(f"NPC info: {camper_1.get('npc_info')}")
log("Content:")
log(camper_1.get('content', ''))

# Look at sample staff (Mara Voss)
staff_1 = live_npc[191] # Mara Voss
log("\n=== SAMPLE STAFF (Mara Voss) ===")
log(f"Name: {staff_1.get('name')}")
log(f"Keys: {staff_1.get('keys')}")
log(f"Avatar: {staff_1.get('avatar')}")
log(f"Type: {staff_1.get('type')}")
log("Content:")
log(staff_1.get('content', ''))

# Look at sample location (Arrival Gate)
loc_1 = live_loc[188]
log("\n=== SAMPLE LOCATION (Arrival Gate) ===")
log(f"Name: {loc_1.get('name')}")
log(f"Keys: {loc_1.get('keys')}")
log(f"Type: {loc_1.get('type')}")
log("Content:")
log(loc_1.get('content', ''))

loc_cabin = live_loc[209]
log("\n=== SAMPLE CABIN (Moonflower) ===")
log(f"Name: {loc_cabin.get('name')}")
log(f"Keys: {loc_cabin.get('keys')}")
log(f"Type: {loc_cabin.get('type')}")
log("Content:")
log(loc_cabin.get('content', ''))

with open('scratch/sample_mystic_dump.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Dumped to scratch/sample_mystic_dump.txt")
