"""
Scripts to apply Phase 1 (SPECIAL stat_config + stat_roles combat mapping)
and Phase 3 (Relationship config custom_moodlets with 12 complete moods)
to Wyvern World _YpX47fNraQFw2dD7TdycJ.
"""

import sys
import os
import json
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
TOKEN_PATH = os.path.join(os.path.dirname(__file__), '..', 'scratch', 'wyvern_token.txt')

def get_headers():
    with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
        token = f.read().strip()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def main():
    print(f"=== Applying Phase 1 & Phase 3 to World {WORLD_ID} ===")
    
    url = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"
    req = urllib.request.Request(url, headers=get_headers())
    with urllib.request.urlopen(req) as resp:
        current_world = json.loads(resp.read().decode('utf-8'))
        
    print(f"Fetched World: {current_world.get('name')}")
    
    # Phase 1: Stat Config (S.P.E.C.I.A.L. + stat_roles)
    special_stats = [
        {
            "id": "strength",
            "label": "Strength",
            "abbreviation": "STR",
            "description": "Physical power. Drives melee damage and physical attack rolls.",
            "enabled": True
        },
        {
            "id": "perception",
            "label": "Perception",
            "abbreviation": "PER",
            "description": "Awareness and precision. Drives attack accuracy and consumable effectiveness.",
            "enabled": True
        },
        {
            "id": "endurance",
            "label": "Endurance",
            "abbreviation": "END",
            "description": "Toughness and stamina. Drives max HP and physical defense.",
            "enabled": True
        },
        {
            "id": "charisma",
            "label": "Charisma",
            "abbreviation": "CHA",
            "description": "Social influence and presence. Affects NPC reactions and persuasion.",
            "enabled": True
        },
        {
            "id": "intelligence",
            "label": "Intelligence",
            "abbreviation": "INT",
            "description": "Mental acuity and arcane aptitude. Drives max MP, special attack, and special defense.",
            "enabled": True
        },
        {
            "id": "agility",
            "label": "Agility",
            "abbreviation": "AGI",
            "description": "Speed and reflexes. Drives initiative, evasion, and flee chance.",
            "enabled": True
        },
        {
            "id": "luck",
            "label": "Luck",
            "abbreviation": "LCK",
            "description": "Fortune and fate. Affects critical hits and initiative tiebreakers.",
            "enabled": True
        }
    ]
    
    stat_roles = {
        "hp_stat": "endurance",
        "mp_stat": "intelligence",
        "physical_attack": "strength",
        "physical_defense": "endurance",
        "special_attack": "intelligence",
        "special_defense": "intelligence",
        "speed": "agility",
        "accuracy": "perception",
        "evasion": "agility",
        "flee": "agility",
        "luck": "luck"
    }
    
    stat_config = {
        "stats": special_stats,
        "base_value": 8,
        "max_value": 30,
        "point_budget": 25,
        "stat_roles": stat_roles
    }
    
    # Phase 3: Relationship Config (12 Custom Moods)
    # custom_moodlets schema: id, label, delta, duration_hours, description
    custom_moodlets = [
        {
            "id": "rut",
            "label": "Rut",
            "delta": 15,
            "duration_hours": 72,
            "description": "Dominant mating urge, territorial possessiveness, knot swelling, protective aggression toward partner."
        },
        {
            "id": "heat",
            "label": "Heat",
            "delta": 15,
            "duration_hours": 72,
            "description": "Overwhelming primal mating drive, elevated body temperature, knotting receptivity, intense nesting."
        },
        {
            "id": "scent_marked",
            "label": "Scent Marked",
            "delta": 10,
            "duration_hours": 168,
            "description": "Coated in partner or Alpha primal scent, signaling claim and deterring rival suitors."
        },
        {
            "id": "mated_devotion",
            "label": "Mated Devotion",
            "delta": 25,
            "duration_hours": 720,
            "description": "Unbreakable psychic, emotional, and territorial devotion to bonded mate."
        },
        {
            "id": "vampiric_blood_hunger",
            "label": "Vampiric Blood Hunger",
            "delta": -5,
            "duration_hours": 24,
            "description": "Burning predatory thirst for fresh blood, sharpened fangs, diminished restraint, viewing target as vital prey."
        },
        {
            "id": "blood_frenzy",
            "label": "Blood Frenzy",
            "delta": -15,
            "duration_hours": 12,
            "description": "Uncontrollable sanguinary combat frenzy triggered by spilled arterial blood or severe blood starvation."
        },
        {
            "id": "essentia_hunger",
            "label": "Essentia Hunger",
            "delta": -5,
            "duration_hours": 24,
            "description": "Starvation for sexual, emotional, or vital life essence (Succubi/Incubi), causing restless predatory focus."
        },
        {
            "id": "seductive_haze",
            "label": "Seductive Haze",
            "delta": 10,
            "duration_hours": 24,
            "description": "Aura of pheromonal intoxication and heightened lust, blurring rational defenses and inducing compliance."
        },
        {
            "id": "pack_bond_resonance",
            "label": "Pack Bond Resonance",
            "delta": 15,
            "duration_hours": 48,
            "description": "Harmonious pack telepathic resonance, heightened senses, emotional empathy, and communal safety."
        },
        {
            "id": "feral_aggression",
            "label": "Feral Aggression",
            "delta": -10,
            "duration_hours": 12,
            "description": "Primal beast instincts overriding civilized thought; bared fangs, low growls, and combat hypervigilance."
        },
        {
            "id": "blood_oath_bond",
            "label": "Blood Oath Bond",
            "delta": 20,
            "duration_hours": 168,
            "description": "Unshakeable obligation and supernatural fidelity sworn under runic blood oath or life debt."
        },
        {
            "id": "betrayed_trust",
            "label": "Betrayed Trust",
            "delta": -25,
            "duration_hours": 72,
            "description": "Deep sorrow and bitter hostility from shattered pack loyalty, broken vows, or intimate deception."
        }
    ]
    
    # moodlets schema for legacy engine: id, label, duration, intensity, effect
    legacy_moodlets = [
        {"id": "m_rut", "label": "Rut", "duration": 72, "intensity": 5, "effect": "Dominant mating urge, knot swelling, protective aggression"},
        {"id": "m_heat", "label": "Heat", "duration": 72, "intensity": 5, "effect": "Overwhelming primal mating drive, knotting receptivity"},
        {"id": "m_scent_marked", "label": "Scent Marked", "duration": 168, "intensity": 3, "effect": "Coated in primal claiming scent, deterring rivals"},
        {"id": "m_mated_devotion", "label": "Mated Devotion", "duration": 720, "intensity": 5, "effect": "Unbreakable psychic and territorial devotion"},
        {"id": "m_vampiric_blood_hunger", "label": "Vampiric Blood Hunger", "duration": 24, "intensity": 4, "effect": "Burning predatory thirst for fresh blood, heightened senses"},
        {"id": "m_blood_frenzy", "label": "Blood Frenzy", "duration": 12, "intensity": 5, "effect": "Uncontrollable sanguinary frenzy triggered by blood"},
        {"id": "m_essentia_hunger", "label": "Essentia Hunger", "duration": 24, "intensity": 4, "effect": "Starvation for vital sexual/emotional essence"},
        {"id": "m_seductive_haze", "label": "Seductive Haze", "duration": 24, "intensity": 3, "effect": "Pheromonal intoxication and blurred rational judgment"},
        {"id": "m_pack_resonance", "label": "Pack Bond Resonance", "duration": 48, "intensity": 2, "effect": "Harmonious pack empathy and heightened senses"},
        {"id": "m_feral_aggression", "label": "Feral Aggression", "duration": 12, "intensity": 4, "effect": "Primal beast instincts, bared fangs, defensive posture"},
        {"id": "m_blood_oath_bond", "label": "Blood Oath Bond", "duration": 168, "intensity": 4, "effect": "Unshakeable supernatural fidelity sworn under blood oath"},
        {"id": "m_betrayed_trust", "label": "Betrayed Trust", "duration": 72, "intensity": 5, "effect": "Hostile wariness, broken communion, deep sorrow"}
    ]
    
    current_rel = current_world.get('relationship_config') or {}
    relationship_config = {
        **current_rel,
        "enabled": True,
        "custom_moodlets": custom_moodlets,
        "moodlets": legacy_moodlets
    }
    
    payload = {
        "stat_config": stat_config,
        "relationship_config": relationship_config
    }
    
    print("\nSending PUT update to World API...")
    req_put = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers=get_headers(),
        method='PUT'
    )
    
    try:
        with urllib.request.urlopen(req_put) as resp:
            resp_bytes = resp.read()
            updated = json.loads(resp_bytes.decode('utf-8'))
            print("[SUCCESS] World updated successfully!")
            print("New stat_config stats count:", len(updated.get('stat_config', {}).get('stats', [])))
            print("New stat_roles:", updated.get('stat_config', {}).get('stat_roles'))
            print("New custom_moodlets count:", len(updated.get('relationship_config', {}).get('custom_moodlets', [])))
            print("New moodlets count:", len(updated.get('relationship_config', {}).get('moodlets', [])))
    except urllib.error.HTTPError as e:
        print(f"[ERROR] HTTP {e.code}: {e.read().decode('utf-8')}")
        sys.exit(1)

if __name__ == '__main__':
    main()
