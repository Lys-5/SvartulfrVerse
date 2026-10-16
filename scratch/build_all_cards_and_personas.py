import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
PERSONAS_DIR = FINAL_DIR / 'personas'
PERSONAS_DIR.mkdir(parents=True, exist_ok=True)

computed_rpg = json.loads((ROOT / 'scratch' / 'computed_final_rpg_stats.json').read_text(encoding='utf-8'))
live_7 = json.loads((ROOT / 'scratch' / 'live_wyvern_snapshot_oct16' / 'mine_7_characters_live.json').read_text(encoding='utf-8'))
live_personas = json.loads((ROOT / 'scratch' / 'live_wyvern_snapshot_oct16' / 'personas_live.json').read_text(encoding='utf-8'))
snap_dir = ROOT / 'scratch' / 'backup_consolidated_snapshot'
mine_snap = json.loads((snap_dir / 'mine_standalone_characters.json').read_text(encoding='utf-8'))
wc_snap = json.loads((snap_dir / 'world_characters.json').read_text(encoding='utf-8'))
pa_snap = json.loads((snap_dir / 'persona_alyssa.json').read_text(encoding='utf-8'))

FORMAT_RULE = "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."

def update_rpg_in_text(text: str, rpg_key: str) -> str:
    rpg_block = computed_rpg[rpg_key]['rpg_block']
    # Remove any existing RPG STATS & TRAITS block up to ATTITUDES or [INSTRUCTIONS or end of string
    pattern = re.compile(r'RPG STATS & TRAITS:\s*\[LEVEL:.*?(?=\n\nATTITUDES|\n\n\[INSTRUCTIONS|\Z)', re.DOTALL)
    if pattern.search(text):
        return pattern.sub(rpg_block, text)
    else:
        return text.rstrip() + '\n\n' + rpg_block

def clean_phi(phi: str) -> str:
    if not phi:
        return FORMAT_RULE
    # Remove duplicate Format discipline sentences
    lines = [l.strip() for l in phi.splitlines() if l.strip()]
    cleaned = []
    seen_format = False
    for l in lines:
        if 'format discipline:' in l.lower():
            if not seen_format:
                cleaned.append(l)
                seen_format = True
        else:
            cleaned.append(l)
    res = '\n\n'.join(cleaned)
    if 'format discipline:' not in res.lower():
        res = (res + '\n\n' + FORMAT_RULE).strip()
    return res

# 1. Update the 7 Live /mine Character Cards
ID_TO_FILE_AND_KEY = {
    '_HEQQbbRFwKdG8QE2Fh1z1': ('Wulfnic_Bloodmoon_card.json', 'wulfnic'),
    '_QPea6g4Q1QfeYCVHCLMPR': ('Erik_Douglas_card.json', 'erik'),
    '_t4J9aQNJM36cUKAP4wB4U': ('Jasper_Douglas_Bloodmoon_card.json', 'jasper'),
    '_zFLUjV8aVxQRAfQxGcAcY': ('Noah_Douglas_Bloodmoon_card.json', 'noah'),
    '_RDfz7XzTpM23LpPALVXHM': ('Malachia_Douglas_Bloodmoon_card.json', 'malachia'),
    '_T8Ywcr9FEqNf9JxbK6eHP': ('Logan_Douglas_card.json', 'logan'),
    '_TbRM3EdxDjHFgqztTbCpL': ('Edric_Douglas_card.json', 'edric'),
}

updated_7_cards = {}
for cid, c in (live_7.items() if isinstance(live_7, dict) else [(x.get('_id') or x.get('id'), x) for x in live_7]):
    if cid not in ID_TO_FILE_AND_KEY:
        continue
    fname, rpg_key = ID_TO_FILE_AND_KEY[cid]
    c['description'] = update_rpg_in_text(c.get('description', ''), rpg_key).replace('—', ', ')
    c['post_history_instructions'] = clean_phi(c.get('post_history_instructions', '')).replace('—', ', ')
    if c.get('personality'):
        if rpg_key == 'wulfnic':
            c['personality'] = c['personality'].replace('{{age}}', '1197')
        elif rpg_key == 'noah':
            c['personality'] = c['personality'].replace('{{age}}', '25')
        c['personality'] = c['personality'].replace('—', ', ')
    if not c.get('character_note'):
        if rpg_key == 'wulfnic':
            c['character_note'] = (
                "Wulfnic Báleygr Bloodmoon is the 1,197-year-old Primordial Firstborn Alpha, grandfather to Malachia, Noah, Jasper, and Alyssa. "
                "He speaks in a deep, unhurried, archaic cadence, struggles with modern technology, and fiercely reveres the Lupine Blood Moon and his grandchildren. "
                + FORMAT_RULE
            )
        elif rpg_key == 'edric':
            c['character_note'] = (
                "Edric Douglas is Logan's 20-year-old son and cousin to Malachia, Noah, Jasper, and Alyssa. "
                "Warm, observant, grounded, and protective without Alpha arrogance, he acts as a loyal confidant and steady anchor on campus and at home. "
                + FORMAT_RULE
            )
    out_path = FINAL_DIR / fname
    out_path.write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding='utf-8')
    updated_7_cards[cid] = c
    print(f'Updated existing /mine card: {fname} ({cid}) | outfits={len(c.get("outfits", []))} | desc_len={len(c["description"])}')

# 2. Build the 8 New / Resurrected /mine Character Cards (Alyssa + 7 External NPCs)
# Map mine_snap by name
mine_by_name = {c['name']: c for c in mine_snap}
wc_by_id = {c['id']: c for c in wc_snap}

# 2a. Alyssa Hvit Douglas Bloodmoon Card (for twin slot pool)
alyssa_wc = wc_by_id['_MXcEC8Y6B3BNm3b1ttHj6']
alyssa_persona_live = next(p for p in live_personas if p.get('persona_id') == 'persona_1786335754946')
# Extract ATTITUDES block from pa_snap if present
attitudes_match = re.search(r'(ATTITUDES & PACK RELATIONSHIPS:.*)', pa_snap.get('description', ''), re.DOTALL)
attitudes_block = attitudes_match.group(1).strip() if attitudes_match else ''

alyssa_desc = update_rpg_in_text(alyssa_wc.get('long_summary', ''), 'alyssa')
if attitudes_block and 'ATTITUDES & PACK RELATIONSHIPS:' not in alyssa_desc:
    alyssa_desc = alyssa_desc.rstrip() + '\n\n' + attitudes_block
alyssa_desc = alyssa_desc.replace('—', ', ')

alyssa_card = {
    "name": "Alyssa Hvit Douglas Bloodmoon",
    "chat_name": "Alyssa",
    "tagline": "Dominant Omega Twin of House Douglas-Bloodmoon & SUCC Pre-Med Healer",
    "avatar": alyssa_persona_live.get('avatar') or alyssa_wc.get('avatar'),
    "description": alyssa_desc,
    "personality": (alyssa_wc.get('summary') or "[NAME: Alyssa Hvit Douglas Bloodmoon; SPECIES: Werewolf (Founding Bloodline & Pureblood Dominant Omega); AGE: 19 (Born 5 April 2005); ROLE: Twin Sister of Jasper, SUCC Pre-Med Healer]").replace('—', ', '),
    "visual_description": "19-year-old petite (165 cm) curvy hourglass young woman with waist-length snow-white hair, vivid emerald-green eyes, and in Partial Shift a single pair of snow-white wolf ears on top of her head (no human ears) and a fluffy snow-white wolf tail.",
    "first_mes": "\"Jay, se tocchi di nuovo i miei appunti di anatomia per farci girare sopra i benchmark di Echo, giuro che uso i tuoi cavi in fibra ottica come laccio emostatico.\" Alyssa alza lo sguardo dal divano con un mezzo sorriso complice, le orecchie da lupo bianco-neve che fremono appena mentre incrocia le gambe.",
    "mes_example": "",
    "scenario": "Blackwood City & Southern Union Monster College (SUCC), California, 2024.",
    "pre_history_instructions": "Play Alyssa Hvit Douglas Bloodmoon, 19-year-old Dominant Omega twin sister of Jasper Douglas Bloodmoon. She is sunny, sharp-tongued when teased by her brothers, fiercely empathetic, and studying Pre-Med and healing magic at SUCC.",
    "post_history_instructions": FORMAT_RULE,
    "character_note": "Alyssa Hvit Douglas Bloodmoon (19, Dominant Omega, White Moon). Twin sister to Jasper, younger sister to Malachia and Noah, daughter of Erik Douglas. " + FORMAT_RULE,
    "creator_notes": "Official SvartúlfrVerse Character Card for Alyssa Hvit Douglas Bloodmoon (Twin Pool / MalePOV & Group Scenarios).",
    "visibility": "private",
    "rating": "mature",
    "pronouns": "she/her",
    "tags": ["Svartulfr", "Werewolf", "Omega", "Douglas", "Bloodmoon", "SUCC"],
    "outfits": alyssa_persona_live.get('outfits', []),
    "default_outfit": alyssa_persona_live.get('default_outfit'),
}
(FINAL_DIR / 'Alyssa_Douglas_Bloodmoon_card.json').write_text(json.dumps(alyssa_card, indent=2, ensure_ascii=False), encoding='utf-8')
print('Built Alyssa_Douglas_Bloodmoon_card.json | outfits:', len(alyssa_card['outfits']))

# 2b. Zeera, Jared, Mackenzie from mine_standalone_characters.json
for name, fname, rpg_key in [
    ('Zeera Darkfire', 'Zeera_Darkfire_card.json', 'zeera'),
    ('Jared Thompson', 'Jared_Thompson_card.json', 'jared'),
    ('Mackenzie Sanchez-Rogers', 'Mackenzie_Sanchez_Rogers_card.json', 'mackenzie'),
]:
    c = dict(mine_by_name[name])
    c['description'] = update_rpg_in_text(c.get('description', ''), rpg_key).replace('—', ', ')
    c['post_history_instructions'] = clean_phi(c.get('post_history_instructions', '')).replace('—', ', ')
    if c.get('personality'):
        c['personality'] = c['personality'].replace('—', ', ')
    if not c.get('character_note'):
        c['character_note'] = f"{name} — SvartúlfrVerse Official Character Card. {FORMAT_RULE}"
    (FINAL_DIR / fname).write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Built {fname} (from mine_standalone_characters {c.get("_id")}) | outfits={len(c.get("outfits", []))}')

# 2c. Kaladin, Elizabeth, Magnus, Marek from world_characters.json
NPC_WC_SPECS = [
    {
        'wc_id': '_b7QqV43D8pU1tewx4qenY',
        'fname': 'Kaladin_Nargathon_card.json',
        'rpg_key': 'kaladin',
        'name': 'Major Kaladin Blackwolf Nargathon',
        'chat_name': 'Kaladin',
        'tagline': 'Commander of DCC Security Division & Former S.R.F. Special Forces Alpha',
        'pronouns': 'he/him',
        'first_mes': 'Kaladin checks the tactical tablet in his scarred hand before glancing up with a steady, Assessing gaze. "Perimeter is clear. Tell Erik the convoy is ready when he is."',
    },
    {
        'wc_id': '_EwPN1te7qtUKYEx4NLgag',
        'fname': 'Elizabeth_Duskwood_card.json',
        'rpg_key': 'elizabeth',
        'name': 'Elizabeth Duskwood',
        'chat_name': 'Elizabeth',
        'tagline': 'Lady Duskwood, Pureblood Omega Matriarch of Seven Hills & Mother of Erik and Logan',
        'pronouns': 'she/her',
        'first_mes': 'Elizabeth sets her porcelain teacup down without a sound, her warm amber eyes softening as she looks toward the doorway. "Come in, darling. You look like you have been carrying the weight of the whole city on your shoulders."',
    },
    {
        'wc_id': '_jeJTbxLcrYWXNWYPDx4ph',
        'fname': 'Magnus_Douglas_III_card.json',
        'rpg_key': 'magnus',
        'name': 'Magnus Douglas III',
        'chat_name': 'Magnus',
        'tagline': 'Elder Lord of House Douglas, Former Patriarch & Master of Seven Hills Estate',
        'pronouns': 'he/him',
        'first_mes': 'Magnus stands by the tall library windows of Seven Hills, hands clasped behind his back, his silver-streaked gaze cool and exacting. "Punctuality is the first courtesy of a leader. Sit. We have matters of the House to discuss."',
    },
    {
        'wc_id': '_DNaUEjdBpeYph6pMYAkrt',
        'fname': 'Marek_card.json',
        'rpg_key': 'marek',
        'name': 'Marek',
        'chat_name': 'Marek',
        'tagline': 'Ironhorn Nomads MC Enforcer & Heavy Chopper Builder at Cable District Garages',
        'pronouns': 'he/him',
        'first_mes': 'Marek wipes a streak of motor oil from his massive furred forearm with a shop rag, the steel tips of his horns glinting under the garage neon. "Engine is solid. You treat her right on the highway, she will bring you back alive."',
    },
]

for spec in NPC_WC_SPECS:
    wc_obj = wc_by_id[spec['wc_id']]
    desc = update_rpg_in_text(wc_obj.get('long_summary', ''), spec['rpg_key']).replace('—', ', ')
    pers = (wc_obj.get('summary') or '').replace('—', ', ')
    card = {
        'name': spec['name'],
        'chat_name': spec['chat_name'],
        'tagline': spec['tagline'],
        'avatar': wc_obj.get('avatar') or '',
        'description': desc,
        'personality': pers,
        'visual_description': '',
        'first_mes': spec['first_mes'],
        'mes_example': '',
        'scenario': 'Blackwood City & Solarton, California, 2024.',
        'pre_history_instructions': f"Play {spec['name']} faithfully according to their JED+ profile and RPG stats.",
        'post_history_instructions': FORMAT_RULE,
        'character_note': f"{spec['name']} — {spec['tagline']}. {FORMAT_RULE}",
        'creator_notes': f"Converted from Svartúlfr World Character {spec['wc_id']}.",
        'visibility': 'private',
        'rating': 'mature',
        'pronouns': spec['pronouns'],
        'tags': ['Svartulfr', 'Blackwood'],
        'outfits': wc_obj.get('outfits', []),
    }
    (FINAL_DIR / spec['fname']).write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Built {spec['fname']} | outfits={len(card['outfits'])} | desc_len={len(desc)}")

# 3. Build the 3 User Personas in FINAL/personas/
# 3a. Alyssa Persona
alyssa_p = dict(alyssa_persona_live)
alyssa_p['description'] = update_rpg_in_text(alyssa_p.get('description', ''), 'alyssa')
if attitudes_block and 'ATTITUDES & PACK RELATIONSHIPS:' not in alyssa_p['description']:
    alyssa_p['description'] = alyssa_p['description'].rstrip() + '\n\n' + attitudes_block
alyssa_p['description'] = alyssa_p['description'].replace('—', ', ')
(PERSONAS_DIR / 'Alyssa_Persona.json').write_text(json.dumps(alyssa_p, indent=2, ensure_ascii=False), encoding='utf-8')
print('Built FINAL/personas/Alyssa_Persona.json | outfits:', len(alyssa_p.get('outfits', [])), 'appearances:', len(alyssa_p.get('appearances', [])))

# 3b. Echo Persona
echo_persona_live = next(p for p in live_personas if p.get('persona_id') == '1791389790053')
echo_p = dict(echo_persona_live)
echo_p['description'] = update_rpg_in_text(echo_p.get('description', ''), 'echo').replace('—', ', ')
(PERSONAS_DIR / 'Echo_Persona.json').write_text(json.dumps(echo_p, indent=2, ensure_ascii=False), encoding='utf-8')
print('Built FINAL/personas/Echo_Persona.json | outfits:', len(echo_p.get('outfits', [])), 'appearances:', len(echo_p.get('appearances', [])))

# 3c. Jasper Persona (New User Persona mirroring Jasper's Card _t4J9aQNJM36cUKAP4wB4U)
jasper_card = updated_7_cards['_t4J9aQNJM36cUKAP4wB4U']
jasper_appearances = [
    {
        "id": "appearance_jasper_human",
        "name": "Human Form (Glamour / Public / SUCC Campus)",
        "description": "Jasper in his human appearance for public campus classes and urban stealth: 185 cm tall, lean-muscular build, messy jet-black hair covering the sides of his head, vivid emerald-green eyes, normal human ears (wolf ears and tail concealed), subtle black runic tattoo on his shoulder."
    },
    {
        "id": "appearance_jasper_partial",
        "name": "Partial Shift (Wolf Ears & Tail — Default)",
        "description": "Jasper in his natural Partial Shift: 185 cm tall, lean-muscular athletic build, messy jet-black hair, vivid emerald-green eyes with a golden-amber ring when his instincts flare, a single pair of jet-black wolf ears on top of his head (no human ears on the sides of his head), and a bushy black wolf tail."
    },
    {
        "id": "appearance_jasper_wolf",
        "name": "Full Wolf Form (Svartúlfr Black Wolf)",
        "description": "Jasper fully shifted into his Svartúlfr beast form: a sleek, powerful midnight-black dire wolf (`Svartr`) with piercing emerald-green eyes and silent predatory agility."
    }
]
jasper_p = {
    "name": "Jasper",
    "title": "Jasper Svartr Douglas Bloodmoon",
    "comment": "MalePOV Twin Protagonist — Technomancer & Cyber-Mage at SUCC",
    "avatar": jasper_card.get('avatar'),
    "description": jasper_card.get('description'),
    "importance": "high",
    "visibility": "private",
    "pronoun_subjective": "he",
    "pronoun_objective": "him",
    "pronoun_possessive_determiner": "his",
    "pronoun_possessive_pronoun": "his",
    "pronoun_reflexive": "himself",
    "outfits": jasper_card.get('outfits', []),
    "default_outfit": jasper_card.get('default_outfit'),
    "appearances": jasper_appearances,
    "default_appearance": "appearance_jasper_partial",
}
(PERSONAS_DIR / 'Jasper_Persona.json').write_text(json.dumps(jasper_p, indent=2, ensure_ascii=False), encoding='utf-8')
print('Built FINAL/personas/Jasper_Persona.json | outfits:', len(jasper_p.get('outfits', [])), 'appearances:', len(jasper_p.get('appearances', [])))
