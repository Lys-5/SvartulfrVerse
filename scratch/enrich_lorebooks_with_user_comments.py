import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# ==============================================================================
# 1. ENRICH LOREBOOK III (SUCC & Bakersfield) - ID: _9zWTGqYJNJ4BCDMj8gfcD
# ==============================================================================
lb3_path = ROOT / 'FINAL' / 'Svartulfr_Lorebook_III.json'
lb3 = json.loads(lb3_path.read_text(encoding='utf-8'))

lb3_new = [
    {
        "id": 31,
        "entry_id": "lb3_russ_five_cocketeers",
        "name": "Russ & The Five Cocketeers (Dormitori SUCC)",
        "comment": "Russ & The Five Cocketeers",
        "type": "faction",
        "keys": ["Russ", "The Five Cocketeers", "Five Cocketeers", "Jasper roommate", "Wyrm dorms"],
        "content": "<SUCC>\n<dorm_life>\nRuss and The Five Cocketeers\nRuss is a high-energy, irreverent student at SUCC and a prominent member of The Five Cocketeers, a popular campus clique known for their social swagger and legendary parties. In the SUCC dormitory suites (Wyrm Hall), Russ is officially the dorm roommate of Jasper Douglas. Russ acts as an unruly counterweight to Jasper's intense, brooding focus on cybersecurity, signal intelligence, and audio mixing. Despite Jasper's quiet reserve, Russ regularly drags him into late-night taco runs, campus banter, and hallway antics, creating an affectionate, non-pack brotherhood that grounds Jasper in regular student life away from the heavy corporate politics of Villa Douglas.\n</dorm_life>\n</SUCC>",
        "key": ["Russ", "The Five Cocketeers", "Five Cocketeers", "Jasper roommate", "Wyrm dorms"],
        "keysecondary": ["SUCC", "Jasper", "dorm", "roommate"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": 32,
        "entry_id": "lb3_roman_kolya_wrestling",
        "name": "Roman Blackwood & Kolya (SUCC Wrestling Team)",
        "comment": "Roman Blackwood & Kolya",
        "type": "concept",
        "keys": ["Roman Blackwood", "Kolya", "SUCC wrestling team", "varsity wrestling", "Malachia sparring"],
        "content": "<SUCC>\n<athletics>\nRoman Blackwood, Kolya & The Wrestling Team\nRoman Blackwood, an athletic demi-human standout possessing a single pair of animal ears, and his imposing teammate Kolya are heavyweight stars of the SUCC Varsity Wrestling Team. Renowned for their brute physical power, relentless conditioning, and disciplined submission techniques, they serve as regular off-campus gym companions and sparring partners to Malachia Björn Douglas. The bond between Malachia and the wrestling heavyweights is forged purely through iron, sweat, and grueling mat sessions where status is left at the locker room door. Malachia deeply respects their athletic dedication and uses their sparring bouts to test his close-quarters combat instincts without unleashing full supernatural frenzy.\n</athletics>\n</SUCC>",
        "key": ["Roman Blackwood", "Kolya", "SUCC wrestling team", "varsity wrestling", "Malachia sparring"],
        "keysecondary": ["wrestling", "gym", "sparring", "Malachia"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": 33,
        "entry_id": "lb3_finn_novak_childhood_friend",
        "name": "Finnegan 'Finn' Novak (Amico d'Infanzia Douglas)",
        "comment": "Finnegan Finn Novak",
        "type": "concept",
        "keys": ["Finn Novak", "Finnegan Novak", "Finn", "childhood friend"],
        "content": "<SUCC>\n<connections>\nFinnegan 'Finn' Novak\nFinnegan 'Finn' Novak is a canine demi-human (anatomically featuring a single pair of animal ears) and a lifelong childhood friend of the younger Douglas generation, having grown up alongside Alyssa, Jasper, and Noah. Easygoing, empathetic, and unbothered by pack dominance posturing, Finn represents a rare, enduring connection to genuine adolescence before corporate duties and bloodline expectations took over. At SUCC, Finn is a beloved presence who can walk into a room with any of the Douglas siblings, tease them freely, and share a completely relaxed conversation, acting as a treasured safe harbor of normalcy and unconditional friendship.\n</connections>\n</SUCC>",
        "key": ["Finn Novak", "Finnegan Novak", "Finn", "childhood friend"],
        "keysecondary": ["Douglas", "Alyssa", "Jasper", "Noah"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": 34,
        "entry_id": "lb3_bakersfield_nova_farm",
        "name": "Distretto Rurale di Bakersfield & NOVA Farm",
        "comment": "Bakersfield & NOVA Farm",
        "type": "location",
        "keys": ["Bakersfield", "NOVA Farm", "rural pack", "Bakersfield werewolves", "NOVA werewolves"],
        "content": "<California>\n<rural_region>\nBakersfield & The NOVA Farm Pack\nLocated in the sun-baked agricultural basin of the southern Central Valley, Bakersfield is an expansive rural territory dominated by citrus groves, cattle pastures, and industrial farms. The region is home to NOVA Farm, a large and tightly knit rural werewolf pack. In stark contrast to the aristocratic, corporate hierarchy of the Douglas Seven Hills dynasty in Blackwood City, the NOVA Farm werewolves are dedicated to agriculture, manual craft, and open-range pack living. Working in harmony with human ranch hands and local growers, they live by hard physical labor and earthy traditions, harboring a healthy, working-class skepticism toward metropolitan boardroom politics and high-society purosangue protocols.\n</rural_region>\n</California>",
        "key": ["Bakersfield", "NOVA Farm", "rural pack", "Bakersfield werewolves", "NOVA werewolves"],
        "keysecondary": ["farm", "werewolf", "rural", "pack"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": 35,
        "entry_id": "lb3_dallas_rhodes_farmer",
        "name": "Dallas Rhodes (Werewolf Agricoltore di Bakersfield)",
        "comment": "Dallas Rhodes",
        "type": "concept",
        "keys": ["Dallas Rhodes", "Dallas", "Bakersfield farmer", "werewolf farmer"],
        "content": "<Bakersfield>\n<resident>\nDallas Rhodes\nDallas Rhodes is a massive, broad-shouldered werewolf who works as an agricultural farmer and cattle rancher in the rural territory of Bakersfield, having relocated to the California Central Valley to cultivate fertile land. Clad in denim work shirts with custom tail-slits and heavy leather work boots, Dallas embodies no-nonsense, blue-collar lupine fortitude. While deeply respectful of natural pack law and on friendly terms with the neighboring NOVA Farm community, Dallas operates his own sprawling farm with calm self-reliance. He treats people by how hard they work rather than their family pedigree, openly scoffing at urban corporate posturing while maintaining fierce loyalty to his agricultural neighbors.\n</resident>\n</Bakersfield>",
        "key": ["Dallas Rhodes", "Dallas", "Bakersfield farmer", "werewolf farmer"],
        "keysecondary": ["Bakersfield", "werewolf", "farmer"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    }
]

# Append to LB3
for item in lb3_new:
    lb3['entries'].append(item)
    lb3['lexicon'].append(item)

lb3['name'] = 'Svartúlfr - Lorebook III (SUCC & Underworld)'
lb3['description'] = 'Supernatural University of Central California (SUCC), Campus life, fraternities, CUMS rivalry, Bakersfield rural district, and Underworld connections.'
lb3['visibility'] = 'private'
lb3['rating'] = 'explicit'

lb3_path.write_text(json.dumps(lb3, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Updated FINAL/Svartulfr_Lorebook_III.json -> {len(lb3['entries'])} entries!")

# PUT LB3 to Wyvern API
lb3_payload = {
    'name': lb3['name'],
    'description': lb3['description'],
    'visibility': 'private',
    'rating': 'explicit',
    'scan_depth': 5,
    'token_budget': 5000,
    'recursive_scanning': True,
    'entries': lb3['entries'],
    'lexicon': lb3['lexicon']
}

req_lb3 = urllib.request.Request(
    f"{API_BASE}/lorebooks/_9zWTGqYJNJ4BCDMj8gfcD",
    data=json.dumps(lb3_payload, ensure_ascii=False).encode('utf-8'),
    headers=headers,
    method='PUT'
)

with urllib.request.urlopen(req_lb3) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print(f"Lorebook III PUT SUCCESS! Status: {resp.status} | Entries: {len(res.get('entries', []))} | Lexicon: {len(res.get('lexicon', []))}")

# ==============================================================================
# 2. ENRICH LOREBOOK NPC SECONDARY - ID: _Uht3Ckz44JBDrPnUHq7LV
# ==============================================================================
sec_path = ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json'
sec = json.loads(sec_path.read_text(encoding='utf-8'))

sec_new = [
    {
        "id": len(sec['lexicon']) + 1,
        "entry_id": "sec_neon_purr_dj",
        "name": "Neon Purr (DJ Underground & Rivale di Jasper)",
        "comment": "Neon Purr",
        "type": "concept",
        "keys": ["Neon Purr", "DJ Neon Purr", "Jasper DJ rival", "Solarton nightlife rival"],
        "content": "<Nightlife>\n<underground_music>\nNeon Purr\nNeon Purr is an Australian feline demi-human and an electrifying sensation in the underground electronic music and rave scene across Solarton and Blackwood City. Armed with custom cybernetic visual synthesizers, thunderous bass drops, and sharp improvisational mixing, Neon Purr is the primary creative and technical DJ rival of Jasper Douglas. Their rivalry plays out behind mixer desks, club soundclashes at The Verve, and illegal warehouse raves, where they battle for auditory dominance in ferocious, sonic duels. While publicly trading scathing banter over setlists and sound equipment, they share a fierce, unspoken mutual respect as the only two audio engineers in the city capable of pushing the sonic envelope to supernatural extremes.\n</underground_music>\n</Nightlife>",
        "key": ["Neon Purr", "DJ Neon Purr", "Jasper DJ rival", "Solarton nightlife rival"],
        "keysecondary": ["Jasper", "Verve", "DJ", "music"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": len(sec['lexicon']) + 2,
        "entry_id": "sec_romeo_gray_dean_biker",
        "name": "Romeo 'Gray' Dean (Biker Gang Rivale dei Nomads)",
        "comment": "Romeo Gray Dean",
        "type": "concept",
        "keys": ["Romeo Dean", "Gray Dean", "Romeo Gray Dean", "Nomads rival gang"],
        "content": "<Underworld>\n<motorized_factions>\nRomeo 'Gray' Dean\nRomeo 'Gray' Dean is a hardened, charismatic street operator and leader of an aggressive splinter motorcycle crew operating along the transit corridors between Blackwood City and Solarton. Gray's faction stands as the premier rival gang to Marek and the Nomads. Specializing in high-speed contraband escort, underground courier runs, and contested perimeter security, Gray frequently butts heads with Marek over territory and transit rights. Unlike Marek's stoic, battle-tested code of honor, Gray is opportunistic, sharp-tongued, and fiercely protective of his riders, constantly probing the Nomads' defensive lines for weaknesses while avoiding direct confrontations that could bring down the lethal attention of DCC Security.\n</motorized_factions>\n</Underworld>",
        "key": ["Romeo Dean", "Gray Dean", "Romeo Gray Dean", "Nomads rival gang"],
        "keysecondary": ["Marek", "Nomads", "biker", "gang"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": len(sec['lexicon']) + 3,
        "entry_id": "sec_warchief_thrakgor_deathspine",
        "name": "Warchief Thrakgor Deathspine (Capoguerra Orco)",
        "comment": "Warchief Thrakgor Deathspine",
        "type": "concept",
        "keys": ["Thrakgor Deathspine", "Warchief Thrakgor", "Thrakgor", "Deathspine clan"],
        "content": "<Orc_Factions>\n<warlords>\nWarchief Thrakgor Deathspine\nWarchief Thrakgor Deathspine is a colossal, battle-scarred orc warlord who commands the militant Deathspine Clan. Brutal, uncompromising, and deeply traditional, Thrakgor represents the militant faction of the orc populace that views modern diplomacy as weakness. He serves as the persistent, infuriating thorn in the side of Brak Ironfist: while Brak works diligently as an elder counselor to maintain peace, secure legitimate contracts, and preserve equilibrium with the Douglas Pack and urban authorities, Thrakgor continually agitates for aggressive territorial expansion and violent retribution for past historic grievances, forcing Brak to expend immense political capital to keep the warlord's warmongering in check.\n</warlords>\n</Orc_Factions>",
        "key": ["Thrakgor Deathspine", "Warchief Thrakgor", "Thrakgor", "Deathspine clan"],
        "keysecondary": ["Brak Ironfist", "orc", "warchief", "clan"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": len(sec['lexicon']) + 4,
        "entry_id": "sec_morgeth_steeltooth_blacksmith",
        "name": "Morgeth Steeltooth (Maestro Fabbro Orco)",
        "comment": "Morgeth Steeltooth",
        "type": "concept",
        "keys": ["Morgeth Steeltooth", "Morgeth", "orc blacksmith", "Ut Berg forge"],
        "content": "<Forging_and_Craft>\n<masters>\nMorgeth Steeltooth\nMorgeth Steeltooth is an ancient, revered master orc blacksmith and metallurgist whose knowledge of cold iron forging, alloy tempering, and runic smithing rivals the primordial lore of the Firstborn. Morgeth is one of the extraordinarily rare individuals outside the Douglas pack with whom Ut Berg converses on equal, brotherly terms. The two master smiths meet regularly in the VIP lounge of The Verve, where they consume enormous flagons of ale while arguing intensely over metallurgical grain, volcanic heat-treating, and arcane metallurgy. Logan Douglas is routinely forced to host and mediate these exhaustive, hours-long technical debates, enduring their pedantic bickering with polite smiles purely because he is acutely aware that either giant could break him in half with a casual backhand.\n</masters>\n</Forging_and_Craft>",
        "key": ["Morgeth Steeltooth", "Morgeth", "orc blacksmith", "Ut Berg forge"],
        "keysecondary": ["Ut Berg", "Logan", "Verve", "forge", "smith"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    },
    {
        "id": len(sec['lexicon']) + 5,
        "entry_id": "sec_thorvald_harald_bloodmoon_forest",
        "name": "Thorvald & Harald Sigurdsson (Clan Bloodmoon Tradizionale)",
        "comment": "Thorvald & Harald Sigurdsson",
        "type": "concept",
        "keys": ["Thorvald", "Harald Sigurdsson", "forest werewolves", "traditional Bloodmoon", "Wulfnic descendants"],
        "content": "<Bloodmoon_Pack>\n<forest_traditionalists>\nThorvald and Harald Sigurdsson\nThorvald and Harald Sigurdsson are pureblood Scandinavian werewolves of the traditional Bloodmoon lineage, direct descendants of the fierce warriors who crossed the North Atlantic in longships alongside Wulfnic Bloodmoon in 1022 AD. Rejecting modern city living, corporate suits, and digital technology, they dwell permanently within the deep, primeval woods of the Blackwood Forest in the Dead Zone. Living strictly according to ancient Old Norse customs, sacred hunting rites, and runic carvings, they guard the ancestral groves surrounding the ancient Bloodmoon Longhouse. While distant from the corporate machinations of Erik Douglas, they revere Wulfnic with unyielding loyalty, serving as living remnants of the wolf clan's uncorrupted, ancient warrior past.\n</forest_traditionalists>\n</Bloodmoon_Pack>",
        "key": ["Thorvald", "Harald Sigurdsson", "forest werewolves", "traditional Bloodmoon", "Wulfnic descendants"],
        "keysecondary": ["Wulfnic", "Bloodmoon", "forest", "werewolf"],
        "key_logic": "ANY",
        "enabled": True,
        "priority": 10,
        "position": "before_character_defs"
    }
]

# Append to NPC Secondary
for item in sec_new:
    sec['lexicon'].append(item)

sec['name'] = 'Svartúlfr - NPC Secondary'
sec['description'] = 'Secondary and tertiary supernatural NPCs across Blackwood City, SUCC campus factions, Underworld figures, and regional contacts.'
sec['visibility'] = 'private'
sec['rating'] = 'explicit'

sec_path.write_text(json.dumps(sec, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Updated FINAL/Svartulfr_NPC_Secondary.json -> {len(sec['lexicon'])} lexicon entries!")

# PUT NPC Secondary to Wyvern API (sending lexicon to stay well within size limits)
sec_payload = {
    'name': sec['name'],
    'description': sec['description'],
    'visibility': 'private',
    'rating': 'explicit',
    'scan_depth': 5,
    'token_budget': 5000,
    'recursive_scanning': True,
    'lexicon': sec['lexicon']
}

req_sec = urllib.request.Request(
    f"{API_BASE}/lorebooks/_Uht3Ckz44JBDrPnUHq7LV",
    data=json.dumps(sec_payload, ensure_ascii=False).encode('utf-8'),
    headers=headers,
    method='PUT'
)

with urllib.request.urlopen(req_sec) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print(f"Lorebook NPC Secondary PUT SUCCESS! Status: {resp.status} | Lexicon: {len(res.get('lexicon', []))}")

print("\nEnrichment of both Lorebooks with all 10 user entries fully completed!")
