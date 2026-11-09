"""
Unified RPG Review, Auto-Provisioning & Omni-Parity Synchronization Engine
Svartúlfr Verse — World ID: _YpX47fNraQFw2dD7TdycJ

Performs end-to-end review and synchronization of RPG stats (S.P.E.C.I.A.L.),
species, occupations, and traits across:
1. Standalone Character Cards (FINAL/*_card.json and /api/characters/{id})
2. User Personas (FINAL/personas/*.json and /api/user-personas/{id})
3. Standalone Lorebooks (FINAL/Svartulfr_NPC_Primary.json & Secondary.json, /api/lorebooks/{id})
4. World Characters (GET /api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ)
"""

import os
import sys
import json
import re
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token
from scripts.auto_provision_rpg import check_and_provision_entity, get_catalog, save_catalog

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
STAT_KEYS = ["strength", "perception", "endurance", "charisma", "intelligence", "agility", "luck"]
STAT_ABBR = {
    "strength": "STR",
    "perception": "PER",
    "endurance": "END",
    "charisma": "CHA",
    "intelligence": "INT",
    "agility": "AGI",
    "luck": "LCK"
}

def get_headers(token, content_type=True):
    h = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    if content_type:
        h['Content-Type'] = 'application/json'
    return h
def refresh_token_if_needed():
    return get_auth_token()

def load_all_catalogs():
    species = get_catalog('species')
    occs = get_catalog('occupations')
    traits = get_catalog('traits')
    
    sp_by_name = {s['name'].lower().strip(): s for s in species}
    occ_by_name = {o['name'].lower().strip(): o for o in occs}
    tr_by_name = {t['name'].lower().strip(): t for t in traits}
    
    sp_by_id = {s['id']: s for s in species}
    occ_by_id = {o['id']: o for o in occs}
    tr_by_id = {t['id']: t for t in traits}
    
    return {
        'species': species, 'occupations': occs, 'traits': traits,
        'sp_by_name': sp_by_name, 'occ_by_name': occ_by_name, 'tr_by_name': tr_by_name,
        'sp_by_id': sp_by_id, 'occ_by_id': occ_by_id, 'tr_by_id': tr_by_id
    }

def format_mod_str(mods):
    if not mods: return ""
    parts = []
    for k in STAT_KEYS:
        if k in mods and mods[k] != 0:
            sign = "+" if mods[k] > 0 else ""
            parts.append(f"{STAT_ABBR[k]} {sign}{mods[k]}")
    return f" ({', '.join(parts)})" if parts else ""

def compute_rpg_block(name, level, species_obj, occ_obj, traits_list, base_stats, class_name):
    final_stats = dict(base_stats)
    for k in STAT_KEYS:
        if k not in final_stats:
            final_stats[k] = 8
            
    # Species mods
    for k, v in (species_obj.get('stat_modifiers') or {}).items():
        if k in final_stats: final_stats[k] += v
        
    # Occ mods
    for k, v in (occ_obj.get('stat_modifiers') or {}).items():
        if k in final_stats: final_stats[k] += v
        
    # Trait mods
    for tr in traits_list:
        for k, v in (tr.get('stat_modifiers') or {}).items():
            if k in final_stats: final_stats[k] += v
            
    sp_mod_str = format_mod_str(species_obj.get('stat_modifiers') or {})
    occ_mod_str = format_mod_str(occ_obj.get('stat_modifiers') or {})
    stats_str = "; ".join(f"{STAT_ABBR[k]} {final_stats[k]}" for k in STAT_KEYS)
    
    lines = [
        "RPG STATS & TRAITS:",
        f"[LEVEL: {level}; SPECIES: {species_obj['name']}{sp_mod_str}; OCCUPATION: {occ_obj['name']}{occ_mod_str}; CLASS: {class_name}]",
        f"[STATS: {stats_str}]",
        "TRAITS:"
    ]
    for tr in traits_list:
        t_mod = format_mod_str(tr.get('stat_modifiers') or {})
        t_desc = (tr.get('description') or '').replace('—', ', ')
        lines.append(f"- {tr['name']}{t_mod}: {t_desc}")
        
    return "\n".join(lines), final_stats

def find_best_species(text, catalogs):
    t = text.lower()
    sp_map = catalogs['sp_by_name']
    
    if any(k in t for k in ['werewolf', 'licantropo', 'lupo', 'lupine']):
        return sp_map.get('licantropo (werewolf)')
    if any(k in t for k in ['lamia', 'naga', 'serpentine', 'snake']):
        return sp_map.get('lamia & naga (serpentine)')
    if any(k in t for k in ['succub', 'incub']):
        return sp_map.get('succube & incubo (succubus)')
    if any(k in t for k in ['minotaur', 'minotauro', 'centaur']):
        return sp_map.get('minotauro & centauro (minotaur)')
    if any(k in t for k in ['orc', 'orco', 'oni']):
        return sp_map.get('orco & oni (orc)')
    if any(k in t for k in ['dragon', 'drago', 'drake']):
        return sp_map.get('drago & drake (dragon)')
    if any(k in t for k in ['vampir']):
        return sp_map.get('vampiro (vampire)')
    if any(k in t for k in ['elf', 'elfo', 'sidhe']):
        return sp_map.get('elfo & sidhe (elf)')
    if any(k in t for k in ['fairy', 'fae', 'fata', 'pixie']):
        return sp_map.get('fata & fae (fairy)')
    if any(k in t for k in ['demon', 'demone', 'vax', 'infernal']):
        return sp_map.get('demone & infernale (demon)')
    if any(k in t for k in ['angel', 'angelo', 'celestial']):
        return sp_map.get('angelo & celestiale (angel)')
    if any(k in t for k in ['tritone', 'sirena', 'merfolk']):
        return sp_map.get('tritone & sirena (merfolk)') or sp_map.get('merfolk')
    if any(k in t for k in ['kitsune', 'neko']):
        return sp_map.get('kitsune & neko (beast spirit)')
    if any(k in t for k in ['arachne', 'aracnide', 'drider']):
        return sp_map.get('aracnide & drider (arachne)') or sp_map.get('arachne / drider')
    if any(k in t for k in ['undead', 'non-morto', 'revenant', 'ghost', 'spettro', 'lich']):
        return sp_map.get('non-morto & revenant (undead)')
    if any(k in t for k in ['macchina', 'sintetico', 'cyber', 'android', 'ai', 'familiar']):
        return sp_map.get('macchina & sintetico (machine)') or sp_map.get('machine / synthetic')
    if any(k in t for k in ['mutant', 'mutante', 'ibrido']):
        return sp_map.get('mutante & ibrido (mutant)')
    if any(k in t for k in ['god', 'divinita', 'primordial', 'demigod']):
        return sp_map.get('divinita & primordiale (demigod)')
    if any(k in t for k in ['shifter', 'mutaforma']):
        return sp_map.get('mutaforma & antro (shifter)')
    if any(k in t for k in ['demi-umano', 'demihuman', 'kemonomimi', 'cat', 'fox', 'tiger', 'rabbit', 'bear']):
        return sp_map.get('demi-umano (demihuman)')
        
    return sp_map.get('umano (human)')

def find_best_occupation(text, catalogs):
    t = text.lower()
    occ_map = catalogs['occ_by_name']
    
    if any(k in t for k in ['firstborn', 'jarl']):
        return occ_map.get('firstborn apex sovereign')
    if any(k in t for k in ['prime alpha', 'pack leader', 'warchief']):
        return occ_map.get('pack leader')
    if any(k in t for k in ['patriarch', 'coven leader', 'founder']):
        return occ_map.get('patriarch / coven leader') or occ_map.get('house head (lord/patriarch)')
    if any(k in t for k in ['berserker', 'vanguard']):
        return occ_map.get('guild berserker (vanguard)') or occ_map.get('guild vanguard (dps)')
    if any(k in t for k in ['tank', 'defender', 'guardian', 'shield']):
        return occ_map.get('guild tank') or occ_map.get('defender')
    if any(k in t for k in ['healer', 'medic', 'support', 'pre-med']):
        return occ_map.get('guild support (healer/mage)')
    if any(k in t for k in ['technomancer', 'hacker', 'netrunner', 'cyber-mage', 'cyber']):
        return occ_map.get('technomancer / cyber-mage')
    if any(k in t for k in ['puppet master', 'mind weaver']):
        return occ_map.get('puppet master (mind weaver)')
    if any(k in t for k in ['right hand', 'advisor', 'consigliere']):
        return occ_map.get('right hand (advisor/peacekeeper)')
    if any(k in t for k in ['enforcer', 'left hand', 'braccio destro', 'braccio armato']):
        return occ_map.get('left hand (enforcer)')
    if any(k in t for k in ['scout', 'tracker', 'assassin']):
        return occ_map.get('scout')
    if any(k in t for k in ['street scrapper', 'rogue', 'thief', 'brawler', 'nomad']):
        return occ_map.get('street scrapper / rogue')
    if any(k in t for k in ['dcc security', 'pmc', 'security', 'guard', 'bodyguard']):
        return occ_map.get('dcc security / pmc')
    if any(k in t for k in ['hunter', 'cacciatore']):
        return occ_map.get('hunter / provider')
    if any(k in t for k in ['knight', 'cavaliere']):
        return occ_map.get('knight (sworn warrior)')
    if any(k in t for k in ['diplomat', 'ambassador', 'ceo', 'president']):
        return occ_map.get('diplomat')
    if any(k in t for k in ['event organizer', 'fixer', 'dj', 'bartender']):
        return occ_map.get('event organizer / fixer')
    if any(k in t for k in ['teacher', 'professor', 'coach', 'instructor']):
        return occ_map.get('teacher')
    if any(k in t for k in ['phd', 'academic', 'researcher', 'scientist']):
        return occ_map.get('academic / phd candidate')
    if any(k in t for k in ['builder', 'mechanic', 'smith']):
        return occ_map.get('builder')
    if any(k in t for k in ['athlete', 'hockey', 'quarterback', 'fighter']):
        return occ_map.get('pro athlete / fighter')
    if any(k in t for k in ['caretaker', 'breeder', 'pack mom']):
        return occ_map.get('caretaker / breeder') or occ_map.get("leader's mate / pack mom")
    if any(k in t for k in ['student', 'matricola', 'undergrad', 'succ']):
        return occ_map.get('succ student / civilian')
        
    return occ_map.get('citizen')

def select_traits_for_character(name, text, species_obj, occ_obj, catalogs):
    t = text.lower()
    n = name.lower()
    tr_map = catalogs['tr_by_name']
    traits = []
    
    def add_tr(tr_name):
        tr = tr_map.get(tr_name.lower().strip())
        if tr and tr not in traits:
            traits.append(tr)
            
    # Species-specific biological traits
    sp_n = species_obj['name'].lower()
    if 'licantropo' in sp_n or 'werewolf' in sp_n:
        add_tr('lupine senses')
        add_tr('partial shift mastery')
        add_tr('silver allergy')
        add_tr('regenerative factor')
        if any(k in t for k in ['dominant alpha', 'prime alpha']):
            add_tr('dominant alpha')
            add_tr('alpha command')
        elif 'alpha' in t:
            add_tr('alpha command')
        elif 'beta' in t:
            add_tr('lse beta biology')
        elif 'delta' in t:
            add_tr('lse delta biology')
        elif 'gamma' in t:
            add_tr('pre-first shift (gamma)')
        elif 'white moon' in t:
            add_tr('the white moon (omega)')
            add_tr('dominant omega')
        elif 'dominant omega' in t:
            add_tr('dominant omega')
        elif 'omega' in t:
            add_tr('submissive omega')
            
    if 'demone' in sp_n or 'vax' in t:
        add_tr('night stalker')
        add_tr('ancient heritage')
    if 'orco' in sp_n:
        add_tr('gentle giant')
    if 'macchina' in sp_n or 'cyber' in t:
        add_tr('cyber-augmented')
        add_tr('tech savvy')
        
    # Pedigree & Ancestry
    if any(k in n for k in ['wulfnic', 'zefir', 'ut']):
        add_tr('divine blood (firstborn)')
        add_tr('apex predator divine core')
        add_tr('ancient heritage')
    elif any(k in t for k in ['founding bloodline', 'bloodmoon', 'douglas']):
        add_tr('founding bloodline')
        add_tr('pureblood lineage')
    elif 'pureblood' in t:
        add_tr('pureblood lineage')
    elif 'modified' in t or 'lab' in t:
        add_tr('modified / lab lineage')
    elif 'common' in t:
        add_tr('common lupine blood')
        
    # Role / Vocation traits
    if any(k in t for k in ['berserker', 'fury', 'rage']):
        add_tr('berserker internal furnace')
        add_tr('feral blood')
    if any(k in t for k in ['dungeon', 'rift', 'dmha', 'cacciatore']):
        add_tr('dungeon veteran')
    if any(k in t for k in ['healer', 'medic', 'pre-med', 'botan']):
        add_tr('pre-med / healer')
        add_tr('eternal optimist')
    if any(k in t for k in ['hacker', 'netrunner', 'technomanc']):
        add_tr('technomantic data resonance')
        add_tr('tech savvy')
        add_tr('mastermind')
    if any(k in t for k in ['puppet', 'burattinaio']):
        add_tr('puppeteer mana strings')
        add_tr('mastermind')
    if any(k in t for k in ['strategist', 'mastermind', 'cunning']):
        add_tr('mastermind')
    if any(k in t for k in ['biker', 'nomad', 'rebel', 'rocker', 'weed', 'underground']):
        add_tr('rebel heart / underground')
    if any(k in t for k in ['cynical', 'gruff', 'reluctant', 'hardened']):
        add_tr('knight in sour armor')
    if any(k in t for k in ['burden', 'weight', 'grief', 'tragic', 'duty']):
        add_tr('the weight he carries')
    if any(k in t for k in ['aristocrat', 'old money', 'noble', 'high-society']):
        add_tr('old money / aristocrat')
    if any(k in t for k in ['nerd', 'bookworm', 'scholar', 'library']):
        add_tr('nerdy / bookworm')
    if any(k in t for k in ['trickster', 'mentor', 'sarcastic', 'witty']):
        add_tr('trickster mentor')
    if any(k in t for k in ['familiar', 'symbiosis']):
        add_tr('familiar soulbound synergy')
        
    # Cap between 2 and 6 traits
    if len(traits) < 2:
        add_tr('dungeon veteran')
        add_tr('the weight he carries')
    return traits[:6]

def generate_base_stats_for_char(level, occ_obj, species_obj):
    extra_points = 25 + max(0, (level - 3) * 2)
    stats = {k: 8 for k in STAT_KEYS}
    
    occ_name = occ_obj['name'].lower()
    weights = {'strength': 1, 'perception': 1, 'endurance': 1, 'charisma': 1, 'intelligence': 1, 'agility': 1, 'luck': 1}
    
    if any(k in occ_name for k in ['berserker', 'vanguard', 'fighter', 'tank']):
        weights['strength'] += 4
        weights['endurance'] += 4
        weights['agility'] += 2
    elif any(k in occ_name for k in ['scout', 'rogue', 'scrapper']):
        weights['agility'] += 4
        weights['perception'] += 3
        weights['luck'] += 2
    elif any(k in occ_name for k in ['healer', 'support', 'technomancer', 'academic', 'puppet']):
        weights['intelligence'] += 4
        weights['perception'] += 3
        weights['charisma'] += 2
    elif any(k in occ_name for k in ['leader', 'diplomat', 'sovereign', 'patriarch', 'head']):
        weights['charisma'] += 4
        weights['intelligence'] += 3
        weights['endurance'] += 2
    else:
        weights['charisma'] += 2
        weights['perception'] += 2
        
    total_w = sum(weights.values())
    allocated = 0
    for k in STAT_KEYS:
        pts = int(round(extra_points * (weights[k] / total_w)))
        stats[k] += pts
        allocated += pts
        
    diff = extra_points - allocated
    stats['luck'] += diff
    
    for k in STAT_KEYS:
        stats[k] = max(5, min(30, stats[k]))
        
    return stats

# -------------------------------------------------------------
# 1. SYNC STANDALONE CHARACTER CARDS (9 cards)
# -------------------------------------------------------------
STANDALONE_CARDS = [
    {
        "file": "Jasper_Douglas_Bloodmoon_card.json",
        "id": "_t4J9aQNJM36cUKAP4wB4U",
        "name": "Jasper Svartr Douglas Bloodmoon",
        "level": 3,
        "species": "Licantropo (Werewolf)",
        "occupation": "Technomancer / Cyber-Mage",
        "class": "Guild Infiltrator & Black-Market Info-Broker",
        "traits": [
            "LSE Beta Biology", "Founding Bloodline", "Pureblood Lineage",
            "Technomantic Data Resonance", "Tech Savvy", "Mastermind",
            "Familiar Soulbound Synergy", "Lupine Senses", "Partial Shift Mastery",
            "Regenerative Factor", "Silver Allergy", "Dungeon Veteran",
            "The Weight He Carries", "Old Money / Aristocrat"
        ],
        "base_stats": {"strength": 8, "perception": 14, "endurance": 10, "charisma": 8, "intelligence": 18, "agility": 13, "luck": 10}
    },
    {
        "file": "Erik_Douglas_card.json",
        "id": "_QPea6g4Q1QfeYCVHCLMPR",
        "name": "Erik Ulfr Douglas",
        "level": 9,
        "species": "Licantropo (Werewolf)",
        "occupation": "Pack Leader",
        "class": "Prime Alpha & CEO of DCC",
        "traits": [
            "Pack Leader", "Dominant Alpha", "Alpha Command", "Apex Core Resonance",
            "Mastermind", "Pureblood Lineage", "Ancient Heritage", "The Weight He Carries",
            "Knight in Sour Armor", "Lupine Senses", "Partial Shift Mastery",
            "Regenerative Factor", "Silver Allergy", "Old Money / Aristocrat", "Dungeon Veteran"
        ],
        "base_stats": {"strength": 15, "perception": 12, "endurance": 15, "charisma": 15, "intelligence": 8, "agility": 8, "luck": 8}
    },
    {
        "file": "Logan_Douglas_card.json",
        "id": "_T8Ywcr9FEqNf9JxbK6eHP",
        "name": "Logan Dominic Járn Douglas",
        "level": 9,
        "species": "Licantropo (Werewolf)",
        "occupation": "Right Hand (Advisor/Peacekeeper)",
        "class": "Erik's Right Hand & DCC Black Market Commander",
        "traits": [
            "LSE Beta Biology", "Pureblood Lineage", "Ancient Heritage", "Feral Blood",
            "The Weight He Carries", "Knight in Sour Armor", "Rebel Heart / Underground",
            "Lupine Senses", "Partial Shift Mastery", "Regenerative Factor",
            "Silver Allergy", "Old Money / Aristocrat", "Dungeon Veteran"
        ],
        "base_stats": {"strength": 16, "perception": 13, "endurance": 16, "charisma": 8, "intelligence": 9, "agility": 11, "luck": 8}
    },
    {
        "file": "Malachia_Douglas_Bloodmoon_card.json",
        "id": "_RDfz7XzTpM23LpPALVXHM",
        "name": "Malachia Björn Douglas Bloodmoon",
        "level": 4,
        "species": "Licantropo (Werewolf)",
        "occupation": "Guild Berserker (Vanguard)",
        "class": "Guild Frontline TANK / Vanguard",
        "traits": [
            "Dominant Alpha", "Alpha Command", "Ascended Enigma", "Apex Core Resonance",
            "Pack Leader", "Founding Bloodline", "Pureblood Lineage",
            "Berserker Internal Furnace", "Feral Blood", "The Weight He Carries",
            "Knight in Sour Armor", "Lupine Senses", "Partial Shift Mastery",
            "Regenerative Factor", "Silver Allergy", "Dungeon Veteran", "Old Money / Aristocrat"
        ],
        "base_stats": {"strength": 18, "perception": 10, "endurance": 17, "charisma": 8, "intelligence": 8, "agility": 12, "luck": 8}
    },
    {
        "file": "Noah_Douglas_Bloodmoon_card.json",
        "id": "_zFLUjV8aVxQRAfQxGcAcY",
        "name": "Noah Loki Douglas Bloodmoon",
        "level": 4,
        "species": "Licantropo (Werewolf)",
        "occupation": "Right Hand (Advisor/Peacekeeper)",
        "class": "Pack PR Shield & Strategic Grey Eminence",
        "traits": [
            "LSE Delta Biology", "Founding Bloodline", "Pureblood Lineage",
            "Mastermind", "Trickster Mentor", "Eternal Optimist", "The Weight He Carries",
            "Ancient Heritage", "Lupine Senses", "Partial Shift Mastery",
            "Regenerative Factor", "Silver Allergy", "Old Money / Aristocrat", "Dungeon Veteran"
        ],
        "base_stats": {"strength": 9, "perception": 12, "endurance": 10, "charisma": 18, "intelligence": 14, "agility": 10, "luck": 8}
    },
    {
        "file": "Edric_Douglas_card.json",
        "id": "_TbRM3EdxDjHFgqztTbCpL",
        "name": "Edric Douglas",
        "level": 1,
        "species": "Licantropo (Werewolf)",
        "occupation": "SUCC Student / Civilian",
        "class": "Junior Pack Pup & Aspiring Vanguard",
        "traits": [
            "Pre-First Shift (Gamma)", "Pureblood Lineage", "Lupine Senses",
            "Partial Shift Mastery", "Regenerative Factor", "Silver Allergy", "Old Money / Aristocrat"
        ],
        "base_stats": {"strength": 14, "perception": 13, "endurance": 15, "charisma": 10, "intelligence": 11, "agility": 10, "luck": 8}
    },
    {
        "file": "Wulfnic_Bloodmoon_card.json",
        "id": "_HEQQbbRFwKdG8QE2Fh1z1",
        "name": "Wulfnic Báleygr Bloodmoon",
        "level": 99,
        "species": "Divinita & Primordiale (Demigod)",
        "occupation": "Firstborn Apex Sovereign",
        "class": "Primordial Firstborn Sovereign & Jarl of the Sacred Forest",
        "traits": [
            "Primordial Enigma", "Dominant Alpha", "Alpha Command", "Divine Blood (Firstborn)",
            "Apex Predator Divine Core", "Founding Bloodline", "Ancient Heritage",
            "Berserker Internal Furnace", "Feral Blood", "Lupine Senses",
            "Partial Shift Mastery", "Regenerative Factor", "Silver Allergy"
        ],
        "base_stats": {"strength": 20, "perception": 20, "endurance": 20, "charisma": 20, "intelligence": 14, "agility": 14, "luck": 12}
    },
    {
        "file": "Mackenzie_Sanchez_Rogers_card.json",
        "id": "_zn24784jfcchQ7EwCyAnm",
        "name": "Mackenzie Sanchez-Rogers",
        "level": 4,
        "species": "Licantropo (Werewolf)",
        "occupation": "Street Scrapper / Rogue",
        "class": "Underground Street Fighter & Protective Brawler",
        "traits": [
            "Dominant Alpha", "Alpha Command", "Pureblood Lineage", "Common Lupine Blood",
            "Rebel Heart / Underground", "Feral Blood", "Dungeon Veteran", "Lupine Senses",
            "Partial Shift Mastery", "Regenerative Factor", "Silver Allergy", "The Weight He Carries"
        ],
        "base_stats": {"strength": 16, "perception": 13, "endurance": 15, "charisma": 11, "intelligence": 8, "agility": 13, "luck": 8}
    },
    {
        "file": "Zeera_Darkfire_card.json",
        "id": "_CmkCDzCn36CyYUzfPp2UY",
        "name": "Zeera Darkfire",
        "level": 6,
        "species": "Demone & Infernale (Demon)",
        "occupation": "Diplomat",
        "class": "Horned Skull Clan Leader & CEO of HSK Consulting",
        "traits": [
            "Ancient Heritage", "Old Money / Aristocrat", "Mastermind", "Night Stalker",
            "Dungeon Veteran", "Puppeteer Mana Strings", "The Weight He Carries"
        ],
        "base_stats": {"strength": 12, "perception": 15, "endurance": 14, "charisma": 21, "intelligence": 21, "agility": 11, "luck": 8}
    }
]

def sync_standalone_cards(catalogs, token):
    print("\n--- [STEP 1] SYNCING 9 STANDALONE CHARACTER CARDS ---")
    headers = get_headers(token)
    
    for cdef in STANDALONE_CARDS:
        filepath = os.path.join(ROOT_DIR, 'FINAL', cdef['file'])
        with open(filepath, 'r', encoding='utf-8') as f:
            card_data = json.load(f)
            
        sp_obj = catalogs['sp_by_name'][cdef['species'].lower()]
        occ_obj = catalogs['occ_by_name'][cdef['occupation'].lower()]
        tr_objs = [catalogs['tr_by_name'][t.lower()] for t in cdef['traits'] if t.lower() in catalogs['tr_by_name']]
        
        rpg_block, final_stats = compute_rpg_block(
            cdef['name'], cdef['level'], sp_obj, occ_obj, tr_objs, cdef['base_stats'], cdef['class']
        )
        
        desc = card_data.get('description', '')
        if 'RPG STATS & TRAITS:' in desc:
            desc = desc.split('RPG STATS & TRAITS:')[0].strip()
            
        # Re-inject RPG block before ATTITUDES or at the end
        if 'ATTITUDES & PACK RELATIONSHIPS:' in desc:
            parts = desc.split('ATTITUDES & PACK RELATIONSHIPS:')
            new_desc = parts[0].strip() + "\n\n" + rpg_block + "\n\nATTITUDES & PACK RELATIONSHIPS:" + parts[1]
        else:
            new_desc = desc + "\n\n" + rpg_block
            
        new_desc = new_desc.replace('—', ', ')
        card_data['description'] = new_desc
        
        # Save local JSON
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(card_data, f, indent=2, ensure_ascii=False)
            
        # Push to live Wyvern API
        url = f"https://app.wyvern.chat/api/characters/{cdef['id']}"
        payload = {
            'description': new_desc,
            'name': card_data.get('name'),
            'tags': card_data.get('tags', []),
            'rating': card_data.get('rating', 'explicit'),
            'visibility': card_data.get('visibility', 'private')
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                print(f"  [OK] Card synced: {cdef['name']} ({cdef['id']})")
        except urllib.error.HTTPError as e:
            print(f"  [ERR] Failed to sync card {cdef['name']}: {e.code} {e.read().decode('utf-8', errors='ignore')[:100]}")
            
        time.sleep(0.3)

# -------------------------------------------------------------
# 2. SYNC USER PERSONAS (3 personas)
# -------------------------------------------------------------
PERSONAS_CONFIG = [
    {
        "file": "Alyssa_Persona.json",
        "id": "persona_1786335754946",
        "name": "Alyssa Hvit Douglas Bloodmoon",
        "level": 19,
        "species": "Licantropo (Werewolf)",
        "occupation": "Guild Support (Healer/Mage)",
        "class": "Guild Support (Combat Medic / Healer)",
        "traits": [
            "Familiar Soulbound Synergy", "The White Moon (Omega)", "Dominant Omega",
            "Founding Bloodline", "Pre-Med / Healer", "Eternal Optimist",
            "Regenerative Factor", "Lupine Senses", "Partial Shift Mastery",
            "Silver Allergy", "Common Lupine Blood", "Dungeon Veteran",
            "Old Money / Aristocrat", "Nerdy / Bookworm"
        ],
        "base_stats": {"strength": 9, "perception": 14, "endurance": 10, "charisma": 13, "intelligence": 12, "agility": 9, "luck": 15}
    },
    {
        "file": "Jasper_Persona.json",
        "id": "1792155173728",
        "name": "Jasper Svartr Douglas Bloodmoon",
        "level": 19,
        "species": "Licantropo (Werewolf)",
        "occupation": "Technomancer / Cyber-Mage",
        "class": "Guild Infiltrator & Black-Market Info-Broker",
        "traits": [
            "LSE Beta Biology", "Founding Bloodline", "Pureblood Lineage",
            "Technomantic Data Resonance", "Tech Savvy", "Mastermind",
            "Familiar Soulbound Synergy", "Lupine Senses", "Partial Shift Mastery",
            "Regenerative Factor", "Silver Allergy", "Dungeon Veteran",
            "The Weight He Carries", "Old Money / Aristocrat"
        ],
        "base_stats": {"strength": 8, "perception": 14, "endurance": 10, "charisma": 8, "intelligence": 18, "agility": 13, "luck": 10}
    },
    {
        "file": "Echo_Persona.json",
        "id": "1791389790053",
        "name": "Echo",
        "level": 19,
        "species": "Macchina & Sintetico (Machine)",
        "occupation": "Technomancer / Cyber-Mage",
        "class": "Jasper's Technomantic Cyber-Familiar",
        "traits": [
            "Cyber-Augmented", "Tech Savvy", "Technomantic Data Resonance",
            "Familiar Soulbound Synergy", "Mastermind", "Night Stalker", "Nerdy / Bookworm"
        ],
        "base_stats": {"strength": 8, "perception": 25, "endurance": 11, "charisma": 4, "intelligence": 37, "agility": 15, "luck": 8}
    }
]

def sync_personas(catalogs, token):
    print("\n--- [STEP 2] SYNCING 3 USER PERSONAS ---")
    headers = get_headers(token)
    
    for pdef in PERSONAS_CONFIG:
        filepath = os.path.join(ROOT_DIR, 'FINAL', 'personas', pdef['file'])
        with open(filepath, 'r', encoding='utf-8') as f:
            pdata = json.load(f)
            
        sp_obj = catalogs['sp_by_name'][pdef['species'].lower()]
        occ_obj = catalogs['occ_by_name'][pdef['occupation'].lower()]
        tr_objs = [catalogs['tr_by_name'][t.lower()] for t in pdef['traits'] if t.lower() in catalogs['tr_by_name']]
        
        rpg_block, final_stats = compute_rpg_block(
            pdef['name'], pdef['level'], sp_obj, occ_obj, tr_objs, pdef['base_stats'], pdef['class']
        )
        
        desc = pdata.get('description', '')
        if 'RPG STATS & TRAITS:' in desc:
            desc = desc.split('RPG STATS & TRAITS:')[0].strip()
            
        if 'ATTITUDES & PACK RELATIONSHIPS:' in desc:
            parts = desc.split('ATTITUDES & PACK RELATIONSHIPS:')
            new_desc = parts[0].strip() + "\n\n" + rpg_block + "\n\nATTITUDES & PACK RELATIONSHIPS:" + parts[1]
        else:
            new_desc = desc + "\n\n" + rpg_block
            
        new_desc = new_desc.replace('—', ', ')
        pdata['description'] = new_desc
        
        # Save local JSON
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(pdata, f, indent=2, ensure_ascii=False)
            
        # Push to live Wyvern API
        url = f"https://app.wyvern.chat/api/user-personas/{pdef['id']}"
        payload = {
            'name': pdata.get('name'),
            'description': new_desc,
            'title': pdata.get('title', ''),
            'comment': pdata.get('comment', ''),
            'avatar': pdata.get('avatar', ''),
            'importance': pdata.get('importance', 1)
        }
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                print(f"  [OK] Persona synced: {pdef['name']} ({pdef['id']})")
        except urllib.error.HTTPError as e:
            print(f"  [ERR] Failed to sync persona {pdef['name']}: {e.code} {e.read().decode('utf-8', errors='ignore')[:100]}")
            
        time.sleep(0.3)

# -------------------------------------------------------------
# 3. SYNC LOREBOOK NPCS (Primary: 99, Secondary: 211)
# -------------------------------------------------------------
def sync_lorebook_npcs(catalogs, token):
    print("\n--- [STEP 3] SYNCING STANDALONE LOREBOOKS (PRIMARY & SECONDARY) ---")
    headers = get_headers(token)
    
    lbs = [
        ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary'),
        ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary')
    ]
    
    for lid, filename, label in lbs:
        filepath = os.path.join(ROOT_DIR, 'FINAL', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lb_data = json.load(f)
            
        entries = lb_data.get('lexicon', [])
        print(f"Processing {label}: {len(entries)} entries...")
        
        modified_count = 0
        for e in entries:
            name = e.get('name') or 'NPC'
            content = e.get('content') or ''
            
            if 'RPG STATS & TRAITS:' in content or '[STATS:' in content:
                # Already has block, check and verify no raw em-dash
                if '—' in content:
                    e['content'] = content.replace('—', ', ')
                    modified_count += 1
                continue
                
            # Classify and generate RPG block
            sp_obj = find_best_species(name + ' ' + content, catalogs)
            occ_obj = find_best_occupation(name + ' ' + content, catalogs)
            tr_objs = select_traits_for_character(name, content, sp_obj, occ_obj, catalogs)
            
            # Level heuristic
            level = 4
            if any(k in name.lower() for k in ['wulfnic', 'zefir', 'ut']):
                level = 99
            elif any(k in name.lower() for k in ['erik', 'logan', 'warchief']):
                level = 9
            elif any(k in content.lower() for k in ['veteran', 'commander', 'major']):
                level = 15
            elif any(k in content.lower() for k in ['student', 'pup', 'freshman']):
                level = 2
                
            base_stats = generate_base_stats_for_char(level, occ_obj, sp_obj)
            class_name = f"{occ_obj['name']} ({sp_obj['name'].split()[0]})"
            
            rpg_block, final_stats = compute_rpg_block(name, level, sp_obj, occ_obj, tr_objs, base_stats, class_name)
            
            e['content'] = (content.strip() + "\n\n" + rpg_block).replace('—', ', ')
            modified_count += 1
            
        # Crucial Rule: Parità entries == lexicon
        lb_data['entries'] = list(entries)
        lb_data['lexicon'] = list(entries)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(lb_data, f, indent=2, ensure_ascii=False)
        print(f"  [SAVED] {label} saved locally with {modified_count} newly injected RPG blocks.")
        
        # Sync via Wyvern API using compact payload (omitting provenance to keep body < 1MB)
        url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
        clean_lexicon = []
        for e in entries:
            ec = dict(e)
            ec.pop("provenance", None)
            clean_lexicon.append(ec)
            
        compact_payload = {
            "name": lb_data.get("name"),
            "description": lb_data.get("description", ""),
            "photoURL": lb_data.get("photoURL"),
            "token_budget": lb_data.get("token_budget"),
            "visibility": lb_data.get("visibility", "private"),
            "rating": lb_data.get("rating", "explicit"),
            "scan_depth": lb_data.get("scan_depth", 5),
            "recursive_scanning": lb_data.get("recursive_scanning", True),
            "enableEntryHighlighting": lb_data.get("enableEntryHighlighting", True),
            "gallery": lb_data.get("gallery", []),
            "gallery_count": len(lb_data.get("gallery", [])),
            "lexicon": clean_lexicon
        }
        put_bytes = json.dumps(compact_payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        try:
            req = urllib.request.Request(url, data=put_bytes, headers=headers, method='PUT')
            with urllib.request.urlopen(req, timeout=90) as resp:
                print(f"  [OK] Remote Lorebook synced: {label} ({lid}) - HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            print(f"  [ERR] Failed to sync remote Lorebook {label}: {e.code} {e.read().decode('utf-8', errors='ignore')[:120]}")
            
        time.sleep(1.0)

# -------------------------------------------------------------
# 4. SYNC WORLD CHARACTERS (126 characters on World)
# -------------------------------------------------------------
def sync_world_characters(catalogs, token):
    print(f"\n--- [STEP 4] SYNCING 126 WORLD CHARACTERS ON WORLD {WORLD_ID} ---")
    headers = get_headers(token)
    
    url_list = f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}"
    req = urllib.request.Request(url_list, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chars_list = json.loads(resp.read().decode('utf-8'))
        
    print(f"Found {len(chars_list)} characters on live World.")
    success_count = 0
    err_count = 0
    
    for i, c in enumerate(chars_list):
        cid = c['id']
        fn = c.get('first_name') or ''
        ln = c.get('last_name') or ''
        dn = c.get('display_name') or ''
        name = (fn + ' ' + ln).strip() or dn or c.get('name') or 'Character'
        
        # Detail
        c_url = f"https://app.wyvern.chat/api/worlds/characters/{cid}"
        try:
            req_d = urllib.request.Request(c_url, headers=headers)
            with urllib.request.urlopen(req_d) as resp_d:
                detail = json.loads(resp_d.read().decode('utf-8'))
        except Exception as e:
            print(f"  [ERR GET] {name} ({cid}): {e}")
            err_count += 1
            continue
            
        summary_text = (detail.get('long_summary') or '') + ' ' + (detail.get('summary') or '') + ' ' + (detail.get('display_description') or '')
        
        # Classify
        sp_obj = find_best_species(name + ' ' + summary_text, catalogs)
        occ_obj = find_best_occupation(name + ' ' + summary_text, catalogs)
        tr_objs = select_traits_for_character(name, summary_text, sp_obj, occ_obj, catalogs)
        
        # Level
        current_rpg = detail.get('rpg_stats') or {}
        level = current_rpg.get('level') or 4
        if any(k in name.lower() for k in ['wulfnic', 'zefir', 'ut']):
            level = 99
        elif any(k in name.lower() for k in ['erik', 'logan', 'warchief']):
            level = 9
            
        # Stats
        base_stats = current_rpg.get('base_stats') or {}
        if not any(k in base_stats for k in STAT_KEYS):
            base_stats = generate_base_stats_for_char(level, occ_obj, sp_obj)
        else:
            # Ensure all 7 keys present
            for k in STAT_KEYS:
                if k not in base_stats:
                    base_stats[k] = 8
                    
        class_name = f"{occ_obj['name']} ({sp_obj['name'].split()[0]})"
        rpg_block, final_stats = compute_rpg_block(name, level, sp_obj, occ_obj, tr_objs, base_stats, class_name)
        
        # Update summary text
        ls = detail.get('long_summary') or ''
        if 'RPG STATS & TRAITS:' in ls:
            ls = ls.split('RPG STATS & TRAITS:')[0].strip()
        ls = (ls.strip() + "\n\n" + rpg_block).replace('—', ', ')
        
        patch_payload = {
            'character_traits': [tr['id'] for tr in tr_objs],
            'rpg_stats': {
                'enabled': True,
                'level': level,
                'species_id': sp_obj['id'],
                'occupation_id': occ_obj['id'],
                'base_stats': base_stats
            },
            'long_summary': ls
        }
        
        try:
            req_put = urllib.request.Request(c_url, data=json.dumps(patch_payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req_put) as resp_put:
                success_count += 1
                if (i + 1) % 15 == 0 or (i + 1) == len(chars_list):
                    print(f"  [PROGRESS] Synced {i + 1}/{len(chars_list)} characters on World...")
        except urllib.error.HTTPError as e:
            print(f"  [ERR PUT] {name} ({cid}): HTTP {e.code}")
            err_count += 1
            
        time.sleep(0.12)
        
    print(f"World Characters sync complete: {success_count} updated, {err_count} errors.")

def main():
    print("==================================================================")
    print("   SVARTÚLFR VERSE — COMPREHENSIVE RPG OMNI-PARITY SYNC PIPELINE   ")
    print("==================================================================")
    
    token = refresh_token_if_needed()
    catalogs = load_all_catalogs()
    print(f"Catalogs loaded: {len(catalogs['species'])} species, {len(catalogs['occupations'])} occupations, {len(catalogs['traits'])} traits.")
    
    # 1. Standalone Cards
    sync_standalone_cards(catalogs, token)
    
    # 2. Personas
    sync_personas(catalogs, token)
    
    # 3. Lorebooks
    sync_lorebook_npcs(catalogs, token)
    
    # 4. World Characters
    sync_world_characters(catalogs, token)
    
    print("\n==================================================================")
    print("   ALL CHARACTER RPG REVIEWS AND SYNCS COMPLETED SUCCESSFULLY!    ")
    print("==================================================================")

if __name__ == '__main__':
    main()
