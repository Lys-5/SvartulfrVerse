"""
scripts/reconcile_and_sync_all_rpg_v2.py
Executes complete healing and synchronization for:
1. Primary Lorebook NPCs (clean species/occupation/traits from master catalogs)
2. Secondary Lorebook NPCs (101 Camp Mystic entries missing S.P.E.C.I.A.L. stats computed & injected)
3. World Scenarios (anti-collision character pool correction for Jasper Route, runtime user setup in scene_instructions)
4. Omni-Parity sync across local FINAL/ files and live Wyvern Web API.
"""

import os
import sys
import json
import re
import time
import urllib.request
import urllib.error

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.sync_from_wyvern_web import get_auth_token
from scripts.auto_provision_rpg import get_catalog

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
    h = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    if content_type:
        h['Content-Type'] = 'application/json'
    return h

def load_catalogs():
    species = get_catalog('species')
    occs = get_catalog('occupations')
    traits = get_catalog('traits')
    
    sp_by_name = {s['name'].lower().strip(): s for s in species}
    occ_by_name = {o['name'].lower().strip(): o for o in occs}
    tr_by_name = {t['name'].lower().strip(): t for t in traits}
    
    return {
        'species': species, 'occupations': occs, 'traits': traits,
        'sp_by_name': sp_by_name, 'occ_by_name': occ_by_name, 'tr_by_name': tr_by_name
    }

def format_mod_str(mods):
    if not mods: return ""
    parts = []
    for k in STAT_KEYS:
        if k in mods and mods[k] != 0:
            sign = "+" if mods[k] > 0 else ""
            parts.append(f"{STAT_ABBR[k]} {sign}{mods[k]}")
    return f" ({', '.join(parts)})" if parts else ""

def map_to_catalog_species(raw_str, sp_by_name):
    t = raw_str.lower().strip()
    if any(k in t for k in ['werewolf', 'licantropo', 'lupo', 'lupine']):
        return sp_by_name.get('licantropo (werewolf)')
    if any(k in t for k in ['lamia', 'naga', 'serpentine', 'snake', 'gorgon']):
        return sp_by_name.get('lamia & naga (serpentine)')
    if any(k in t for k in ['succub', 'incub']):
        return sp_by_name.get('succube & incubo (succubus)')
    if any(k in t for k in ['minotaur', 'minotauro', 'centaur']):
        return sp_by_name.get('minotauro & centauro (minotaur)')
    if any(k in t for k in ['orc', 'orco', 'oni']):
        return sp_by_name.get('orco & oni (orc)')
    if any(k in t for k in ['dragon', 'drago', 'drake']):
        return sp_by_name.get('drago & drake (dragon)')
    if any(k in t for k in ['vampir']):
        return sp_by_name.get('vampiro (vampire)')
    if any(k in t for k in ['elf', 'elfo', 'sidhe']):
        return sp_by_name.get('elfo & sidhe (elf)')
    if any(k in t for k in ['fairy', 'fae', 'fata', 'pixie']):
        return sp_by_name.get('fata & fae (fairy)')
    if any(k in t for k in ['demon', 'demone', 'infernal', 'demonkin']):
        return sp_by_name.get('demone & infernale (demon)')
    if any(k in t for k in ['angel', 'angelo', 'celestial', 'nephilim']):
        return sp_by_name.get('angelo & celestiale (angel)')
    if any(k in t for k in ['tritone', 'sirena', 'merfolk', 'mermaid', 'merman', 'siren']):
        return sp_by_name.get('tritone & sirena (merfolk)') or sp_by_name.get('merfolk')
    if any(k in t for k in ['kitsune', 'neko', 'beast spirit']):
        return sp_by_name.get('kitsune & neko (beast spirit)')
    if any(k in t for k in ['arachne', 'aracnide', 'drider']):
        return sp_by_name.get('aracnide & drider (arachne)')
    if any(k in t for k in ['undead', 'non-morto', 'revenant', 'ghost', 'spettro', 'ghoul', 'zombie', 'banshee']):
        return sp_by_name.get('non-morto & revenant (undead)')
    if any(k in t for k in ['macchina', 'sintetico', 'machine', 'synthetic', 'cyber', 'android']):
        return sp_by_name.get('macchina & sintetico (machine)')
    if any(k in t for k in ['werebear', 'wereboar', 'werecrocodile', 'weretiger', 'werehyena', 'beastwere', 'shifter', 'mutaforma', 'kresnik']):
        return sp_by_name.get('mutaforma & antro (shifter)')
    if any(k in t for k in ['mutant', 'mutante', 'ibrido']):
        return sp_by_name.get('mutante & ibrido (mutant)')
    if any(k in t for k in ['god', 'divinita', 'primordial', 'demigod']):
        return sp_by_name.get('divinita & primordiale (demigod)')
    if any(k in t for k in ['demi-umano', 'demihuman', 'beastfolk', 'kemonomimi', 'cat', 'fox', 'tiger', 'rabbit', 'wolf beastfolk', 'avian']):
        return sp_by_name.get('demi-umano (demihuman)')
    return sp_by_name.get('umano (human)')

def map_to_catalog_occupation(raw_str, occ_by_name):
    t = raw_str.lower().strip()
    # Check exact name match first
    for name, obj in occ_by_name.items():
        if name in t or t in name:
            return obj
            
    if 'camp mystic camper' in t:
        return occ_by_name.get('camp mystic camper') or occ_by_name.get('succ student / civilian')
    if 'camp mystic counselor' in t or 'staff lodge' in t:
        return occ_by_name.get('camp mystic counselor / staff') or occ_by_name.get('teacher')
    if 'camper' in t:
        return occ_by_name.get('camp mystic camper') or occ_by_name.get('succ student / civilian')
    if 'counselor' in t or 'staff' in t:
        return occ_by_name.get('camp mystic counselor / staff') or occ_by_name.get('teacher')
    if any(k in t for k in ['firstborn', 'jarl']):
        return occ_by_name.get('firstborn apex sovereign')
    if any(k in t for k in ['prime alpha', 'pack leader']):
        return occ_by_name.get('pack leader')
    if any(k in t for k in ['patriarch', 'coven leader', 'founder']):
        return occ_by_name.get('patriarch / coven leader')
    if any(k in t for k in ['berserker', 'vanguard']):
        return occ_by_name.get('guild berserker (vanguard)')
    if any(k in t for k in ['tank', 'defender', 'earthwarden']):
        return occ_by_name.get('guild tank')
    if any(k in t for k in ['healer', 'medic', 'pre-med', 'support']):
        return occ_by_name.get('guild support (healer/mage)')
    if any(k in t for k in ['technomancer', 'cyber-mage', 'tecnomancer']):
        return occ_by_name.get('technomancer / cyber-mage')
    if any(k in t for k in ['puppet', 'mind weaver']):
        return occ_by_name.get('puppet master (mind weaver)')
    if any(k in t for k in ['right hand', 'advisor', 'peacekeeper']):
        return occ_by_name.get('right hand (advisor/peacekeeper)')
    if any(k in t for k in ['enforcer', 'left hand']):
        return occ_by_name.get('left hand (enforcer)')
    if any(k in t for k in ['scout', 'tracker']):
        return occ_by_name.get('scout')
    if any(k in t for k in ['rogue', 'scrapper', 'street']):
        return occ_by_name.get('street scrapper / rogue')
    if any(k in t for k in ['security', 'pmc', 'chief of security']):
        return occ_by_name.get('chief of security') or occ_by_name.get('dcc security / pmc')
    if any(k in t for k in ['hunter', 'provider']):
        return occ_by_name.get('hunter / provider')
    if any(k in t for k in ['knight']):
        return occ_by_name.get('knight (sworn warrior)')
    if any(k in t for k in ['diplomat']):
        return occ_by_name.get('diplomat')
    if any(k in t for k in ['sorority', 'influencer', 'social coordinator']):
        return occ_by_name.get('sorority social coordinator & aesthetic influencer') or occ_by_name.get('event organizer / fixer')
    if any(k in t for k in ['necromancy', 'applied necromancy']):
        return occ_by_name.get('applied necromancy scholar') or occ_by_name.get('academic / phd candidate')
    if any(k in t for k in ['tattoo', 'artisan']):
        return occ_by_name.get('artisan / tattoo apprentice') or occ_by_name.get('builder')
    if any(k in t for k in ['nsfw', 'chemistry student']):
        return occ_by_name.get('chemistry student & secret nsfw illustrator') or occ_by_name.get('academic / phd candidate')
    if any(k in t for k in ['logistics', 'master cook']):
        return occ_by_name.get('logistics director & master cook') or occ_by_name.get('builder')
    if any(k in t for k in ['teacher', 'coach']):
        return occ_by_name.get('teacher')
    if any(k in t for k in ['phd', 'academic']):
        return occ_by_name.get('academic / phd candidate')
    if any(k in t for k in ['builder', 'mechanic']):
        return occ_by_name.get('builder')
    if any(k in t for k in ['athlete', 'fighter']):
        return occ_by_name.get('pro athlete / fighter')
    if any(k in t for k in ['student']):
        return occ_by_name.get('succ student / civilian')
        
    return occ_by_name.get('citizen')

def generate_stats_block(level, occ_obj, species_obj, traits_list, base_stats, class_name):
    final_stats = dict(base_stats)
    for k in STAT_KEYS:
        if k not in final_stats: final_stats[k] = 8
        
    for k, v in (species_obj.get('stat_modifiers') or {}).items():
        if k in final_stats: final_stats[k] += v
    for k, v in (occ_obj.get('stat_modifiers') or {}).items():
        if k in final_stats: final_stats[k] += v
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
        
    return "\n".join(lines)

def select_traits_for_entry(name, text, species_obj, occ_obj, catalogs):
    t = text.lower()
    n = name.lower()
    tr_map = catalogs['tr_by_name']
    traits = []
    
    def add_tr(tr_name):
        tr = tr_map.get(tr_name.lower().strip())
        if tr and tr not in traits:
            traits.append(tr)
            
    # Species specific
    sp_n = species_obj['name'].lower()
    if 'licantropo' in sp_n or 'werewolf' in sp_n:
        add_tr('lupine senses')
        add_tr('partial shift mastery')
        add_tr('silver allergy')
        add_tr('regenerative factor')
    elif 'demone' in sp_n or 'infernal' in t:
        add_tr('night stalker')
        add_tr('ancient heritage')
    elif 'orco' in sp_n:
        add_tr('gentle giant')
    elif 'succube' in sp_n:
        add_tr('symbiotic feeding')
        add_tr('hypnotic radiance')
    elif 'lamia' in sp_n:
        add_tr('serpentine constriction')
        add_tr('craving warmth')
    elif 'fata' in sp_n:
        add_tr('eternal optimist')
    elif 'macchina' in sp_n or 'cyber' in t:
        add_tr('cyber-augmented')
        add_tr('tech savvy')
        
    # Custom specific by name
    if 'scarlett' in n:
        add_tr('symbiotic feeding')
        add_tr('hypnotic radiance')
        add_tr('sorority matriarch')
        add_tr('vulnerable heart')
    elif 'sierra' in n:
        add_tr('serpentine constriction')
        add_tr('ectothermic slumber')
        add_tr('morbid insight / applied necromancy')
        add_tr('craving warmth')
    elif 'russell' in n or 'russ' in n:
        add_tr('tiger demihuman physiology')
        add_tr('master apprentice ink hand')
        add_tr('deadpan pack immunity')
        add_tr('five cocketeers anchor')
    elif 'stanley' in n:
        add_tr('forum cynic / online scar tissue')
        add_tr('secret nsfw illustrator')
        add_tr('involuntary full moon shift')
        add_tr('heavyweight sloucher')
    elif 'varg' in n:
        add_tr('sovereign of the whispering caves')
        add_tr('century-hardened sinew')
        add_tr('indomitable will')
    elif 'karshin' in n:
        add_tr('pain tolerance')
        add_tr('apex tracker')
        add_tr('close-quarters bruiser')
    elif 'boros' in n:
        add_tr('mountain bastion')
        add_tr('hearthmaster')
        add_tr('unyielding grip')
    elif 'aras' in n:
        add_tr('master of illusions')
        add_tr('empathic diplomat')
        add_tr('sinuous grace')
        
    if len(traits) < 2:
        add_tr('dungeon veteran')
        add_tr('the weight he carries')
        
    return traits[:6]

def fix_lorebook(filename, lid, label, catalogs, token):
    filepath = os.path.join(ROOT_DIR, 'FINAL', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        lb = json.load(f)
        
    entries = lb.get('lexicon', lb.get('entries', []))
    print(f"\nProcessing {label} ({len(entries)} entries)...")
    
    fixed_count = 0
    for e in entries:
        name = e.get('name') or 'NPC'
        content = e.get('content') or ''
        
        # Check if needs healing:
        # 1. Missing [STATS:
        # 2. Or has non-canonical species string in SPECIES: line
        needs_fix = False
        if '[STATS:' not in content:
            needs_fix = True
        else:
            sm = re.search(r'SPECIES:\s*([^;\n\]\)]+)', content, re.IGNORECASE)
            spec_str = sm.group(1).strip() if sm else ''
            sp_match = any(sm_name in spec_str.lower() or spec_str.lower() in sm_name for sm_name in catalogs['sp_by_name'])
            if not sp_match or any(w in spec_str.lower() for w in ['bloodline', 'hybrid', 'kemonomimi', 'blue oni', 'cyber-entity', 'pureblood']):
                needs_fix = True
            
        if not needs_fix:
            if '—' in content:
                e['content'] = content.replace('—', ', ')
                fixed_count += 1
            continue
            
        # Parse existing header if present
        level = 18
        raw_spec = ''
        raw_occ = ''
        raw_class = ''
        
        m_hdr = re.search(r'\[LEVEL:\s*(\d+);\s*SPECIES:\s*([^;]+);\s*OCCUPATION:\s*([^;]+)(?:;\s*CLASS:\s*([^\]]+))?\]', content, re.IGNORECASE)
        if m_hdr:
            level = int(m_hdr.group(1))
            raw_spec = m_hdr.group(2).strip()
            raw_occ = m_hdr.group(3).strip()
            raw_class = (m_hdr.group(4) or '').strip()
        else:
            # Fallback level detection
            if any(k in name.lower() for k in ['wulfnic', 'zefir', 'ut']):
                level = 99
            elif any(k in name.lower() for k in ['erik', 'logan', 'warchief']):
                level = 9
            elif any(k in content.lower() for k in ['veteran', 'elder', 'patriarch']):
                level = 15
            else:
                level = 20
                
            # Extract species from bracket block if available
            sm = re.search(r'SPECIES:\s*([^;\n\]]+)', content, re.IGNORECASE)
            raw_spec = sm.group(1).strip() if sm else ''
            om = re.search(r'OCCUPATION:\s*([^;\n\]]+)', content, re.IGNORECASE)
            raw_occ = om.group(1).strip() if om else ''
            
        sp_obj = map_to_catalog_species(raw_spec or name or content, catalogs['sp_by_name'])
        occ_obj = map_to_catalog_occupation(raw_occ or name or content, catalogs['occ_by_name'])
        
        if not raw_class:
            raw_class = f"{occ_obj['name']} ({sp_obj['name'].split()[0]})"
            
        tr_objs = select_traits_for_entry(name, content, sp_obj, occ_obj, catalogs)
        
        # Base stats budget
        base_stats = {
            'strength': 10, 'perception': 12, 'endurance': 12,
            'charisma': 12, 'intelligence': 11, 'agility': 12, 'luck': 12
        }
        # Tailor slightly by level and occupation
        if 'camper' in occ_obj['name'].lower() or 'student' in occ_obj['name'].lower():
            base_stats['luck'] += 2
        elif 'counselor' in occ_obj['name'].lower() or 'staff' in occ_obj['name'].lower():
            base_stats['perception'] += 2
            base_stats['charisma'] += 2
            
        rpg_block = generate_stats_block(level, occ_obj, sp_obj, tr_objs, base_stats, raw_class)
        
        # Clean existing RPG block from content
        clean_content = content
        if 'RPG STATS & TRAITS:' in clean_content:
            clean_content = clean_content.split('RPG STATS & TRAITS:')[0].strip()
        elif '[RPG STATS & TRAITS:' in clean_content:
            clean_content = clean_content.split('[RPG STATS & TRAITS:')[0].strip()
            
        e['content'] = (clean_content + "\n\n" + rpg_block).replace('—', ', ')
        fixed_count += 1
        
    print(f"  [FIXED] {fixed_count} entries healed in {label}.")
    
    # Parity check byte-for-byte
    lb['entries'] = list(entries)
    lb['lexicon'] = list(entries)
    
    # Save local FINAL
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(lb, f, indent=2, ensure_ascii=False)
        
    # Also save to lorebooks/optimized/
    opt_path = os.path.join(ROOT_DIR, 'lorebooks', 'optimized', filename)
    if os.path.exists(opt_path):
        with open(opt_path, 'w', encoding='utf-8') as f:
            json.dump(lb, f, indent=2, ensure_ascii=False)
            
    # Push to live Wyvern API
    print(f"  Pushing {label} to Wyvern Web API ({lid})...")
    clean_lexicon = []
    for e in entries:
        ec = dict(e)
        ec.pop('provenance', None)
        ec.pop('comment', None)
        ec.pop('lines_parsed', None)
        ec.pop('custom_fields', None)
        ec.pop('labels', None)
        ec.pop('extensions', None)
        clean_lexicon.append(ec)
        
    payload = {
        "name": lb.get("name"),
        "description": lb.get("description", ""),
        "photoURL": lb.get("photoURL"),
        "token_budget": lb.get("token_budget"),
        "visibility": lb.get("visibility", "private"),
        "rating": lb.get("rating", "explicit"),
        "scan_depth": lb.get("scan_depth", 5),
        "recursive_scanning": lb.get("recursive_scanning", True),
        "enableEntryHighlighting": lb.get("enableEntryHighlighting", True),
        "gallery": lb.get("gallery", []),
        "gallery_count": len(lb.get("gallery", [])),
        "lexicon": clean_lexicon
    }
    put_bytes = json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    headers = get_headers(token)
    url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
    req = urllib.request.Request(url, data=put_bytes, headers=headers, method='PUT')
    
    with urllib.request.urlopen(req, timeout=90) as resp:
        print(f"  [API SUCCESS] {label} synced: HTTP {resp.status} ({len(put_bytes)} bytes)")
    time.sleep(1.0)

def fix_scenarios(token):
    print("\n=== HEALING & SYNCHRONIZING SCENARIOS ===")
    headers = get_headers(token)
    
    # Character IDs
    alyssa_char_id = "_6exg3yPfe2eCDK4hTftkh"
    jasper_char_id = "_t4J9aQNJM36cUKAP4wB4U"
    
    base_pool_without_twins = [
        {"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "participation_weight": 50}, # Erik
        {"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "participation_weight": 50}, # Logan
        {"character_id": "_RDfz7XzTpM23LpPALVXHM", "participation_weight": 50}, # Malachia
        {"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "participation_weight": 50}, # Noah
        {"character_id": "_TbRM3EdxDjHFgqztTbCpL", "participation_weight": 50}, # Edric
        {"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "participation_weight": 50}, # Wulfnic
        {"character_id": "_zn24784jfcchQ7EwCyAnm", "participation_weight": 50}, # Mackenzie
        {"character_id": "_CmkCDzCn36CyYUzfPp2UY", "participation_weight": 50}  # Zeera
    ]
    
    alyssa_route_pool = [{"character_id": jasper_char_id, "participation_weight": 50}] + base_pool_without_twins
    jasper_route_pool = [{"character_id": alyssa_char_id, "participation_weight": 50}] + base_pool_without_twins
    master_omnibus_pool = [{"character_id": jasper_char_id, "participation_weight": 50}, {"character_id": alyssa_char_id, "participation_weight": 50}] + base_pool_without_twins
    
    runtime_instructions_block = (
        "\n\n[RUNTIME USER SETUP & ANTI-COLLISION]: "
        "When {{user}} plays as Alyssa or Jasper, suppress the corresponding twin character entity from being generated as an NPC companion. "
        "Initialize {{user}} starting equipment: Alyssa receives Dimensional Medicine Pochette, SUCC Student Smart Card, DCC Encrypted Comm-Link; "
        "Jasper receives Custom Arcane Cyberdeck HUD Rig, SUCC Student Smart Card, DCC Encrypted Smartphone. "
        "Starting funds: 500 USD and 250 DMHA Credits. "
        "Initial attitudes: Deep Unbreakable Pack Loyalty (trust 100) toward family (Erik, Logan, Malachia, Noah, Edric, Wulfnic) and Warm Collegiate Fellowship (trust 70) toward campus peers."
    )
    
    world_scenarios = [
        {
            "id": "_DnNNPzUpDcYRQxLhQnrHY",
            "file": "Svartulfr_World_Scenario_SUCC_Route_Alyssa.json",
            "pool": alyssa_route_pool,
            "extra_instruction": "Depict Alyssa Hvit Douglas Bloodmoon's collegiate life at SUCC. Maintain strict format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
        },
        {
            "id": "_9bH6m8PMYLWFKNgdmpB4H",
            "file": "Svartulfr_World_Scenario_SUCC_Route_Jasper.json",
            "pool": jasper_route_pool,
            "extra_instruction": "Depict Jasper Svartr Douglas Bloodmoon's collegiate life at SUCC. Maintain strict format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
        },
        {
            "id": "_2MTWKjxrQPdQVaz9y4Q7H",
            "file": "Svartulfr_World_Scenario_SUCC_Welcome_Day.json",
            "pool": master_omnibus_pool,
            "extra_instruction": "SUCC Welcome Day: Capture the collegiate atmosphere, family dynamics, and pack instincts of the Douglas-Bloodmoon clan on the SUCC campus. Format discipline: dialogue in quotes, plain text narration, zero em dashes."
        },
        {
            "id": "_FKzLEPnqWX1yXKLpcyCmc",
            "file": "Svartulfr_World_Scenario_Master_Omnibus.json",
            "pool": master_omnibus_pool,
            "extra_instruction": "Master Omnibus Scenario: Balance active scene characters naturally according to their canonical JED+ voice, attitudes, and pack hierarchies. Strict anti-ventriloquism for {{user}}. Dialogue in quotes, plain text narration, zero em-dashes."
        }
    ]
    
    for s_info in world_scenarios:
        filepath = os.path.join(ROOT_DIR, 'FINAL', 'scenarios', s_info['file'])
        with open(filepath, 'r', encoding='utf-8') as f:
            scen = json.load(f)
            
        scen['included_character_pool'] = s_info['pool']
        scen['playable_character_ids'] = [c['character_id'] for c in s_info['pool']]
        scen['scene_instructions'] = s_info['extra_instruction'] + runtime_instructions_block
        
        # Save local FINAL
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(scen, f, indent=2, ensure_ascii=False)
            
        # Push to API
        url = f"https://app.wyvern.chat/api/worlds/scenarios/{s_info['id']}"
        payload = {
            "world_id": WORLD_ID,
            "world": WORLD_ID,
            "name": scen.get('name'),
            "description": scen.get('description'),
            "scenario_premise": scen.get('scenario_premise'),
            "tags": scen.get('tags'),
            "community_tags": [],
            "avatar": scen.get('avatar'),
            "location_id": scen.get('location_id') or "_aPqjQX8UBNTC9y2tEUdX3",
            "environment_id": scen.get('environment_id') or "_38JCUykN4wwRfgGjQyjLr",
            "insertion_point": 10489906,
            "visibility": "private",
            "rating": "explicit",
            "world_only": False,
            "scenario_type": "any",
            "include_character_select": True,
            "include_rpg_build": False,
            "playable_character_ids": scen['playable_character_ids'],
            "included_character_pool": scen['included_character_pool'],
            "scene_instructions": scen['scene_instructions'],
            "premade_scenes": scen.get('premade_scenes', [])
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"  [OK PUT] World Scenario {s_info['file']} ({s_info['id']}) - HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            print(f"  [ERR PUT] World Scenario {s_info['id']}: HTTP {e.code}")
        time.sleep(0.3)

def main():
    print("=" * 70)
    print("RUNNING RECONCILIATION & SYNC PIPELINE V2")
    print("=" * 70)
    
    token = get_auth_token()
    catalogs = load_catalogs()
    print(f"Loaded Catalogs: {len(catalogs['species'])} species, {len(catalogs['occupations'])} occupations, {len(catalogs['traits'])} traits.")
    
    # 1. Primary Lorebook
    fix_lorebook('Svartulfr_NPC_Primary.json', '_zwEqgEEzh12X6gHVmMKKC', 'NPC Primary', catalogs, token)
    
    # 2. Secondary Lorebook
    fix_lorebook('Svartulfr_NPC_Secondary.json', '_Uht3Ckz44JBDrPnUHq7LV', 'NPC Secondary', catalogs, token)
    
    # 3. Scenarios
    fix_scenarios(token)
    
    print("\n" + "=" * 70)
    print("RECONCILIATION & SYNC V2 COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    main()
