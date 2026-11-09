"""
Auto-provisions all authentic custom species, occupations, and traits
found in Primary and Secondary NPCs to achieve 100% catalog coverage on Wyvern World.
"""

import os
import sys
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.auto_provision_rpg import check_and_provision_entity

CUSTOM_OCCUPATIONS = [
    {
        "name": "Sorority Social Coordinator & Aesthetic Influencer",
        "description": "Greek life coordinator curating high-profile social galas, influencer aesthetics, and sisterhood networking.",
        "stat_modifiers": {"charisma": 3, "perception": 1, "luck": 1}
    },
    {
        "name": "Applied Necromancy Scholar",
        "description": "Academic researcher specializing in forensic soul-weaving, spirit taxonomy, and biological preservation.",
        "stat_modifiers": {"perception": 2, "intelligence": 3}
    },
    {
        "name": "Artisan / Tattoo Apprentice",
        "description": "Master artisan specializing in runic sub-dermal inking, magical wards, and steady needle craftsmanship.",
        "stat_modifiers": {"perception": 2, "agility": 2, "charisma": 1}
    },
    {
        "name": "Chemistry Student & Secret NSFW Illustrator",
        "description": "Pre-med biochemistry major managing complex clandestine freelance commissions and illicit digital ink.",
        "stat_modifiers": {"perception": 2, "intelligence": 2, "agility": 1}
    },
    {
        "name": "Logistics Director & Master Cook",
        "description": "Subterranean clan culinary master and supply chain overseer provisioning heavy banquets and raw resources.",
        "stat_modifiers": {"endurance": 2, "strength": 1}
    },
    {
        "name": "Chief of Security",
        "description": "Elite tactical coordinator commanding perimeter checkpoints, guard contingents, and physical containment.",
        "stat_modifiers": {"endurance": 2, "strength": 1}
    },
    {
        "name": "Clan Patriarch",
        "description": "Venerable high-bloodline clan sovereign exercising uncontested dynastic command.",
        "stat_modifiers": {"endurance": 2, "charisma": 1}
    }
]

CUSTOM_TRAITS = [
    # Scarlett Rose
    {"name": "Symbiotic Feeding", "description": "Safe energetic nourishment through consensual emotional warmth, intimacy, or touch.", "stat_modifiers": {"charisma": 2, "endurance": 1}},
    {"name": "Hypnotic Radiance", "description": "Glamour aura captivating onlookers, softening hostilities, and commanding visual attention.", "stat_modifiers": {"charisma": 3}},
    {"name": "Sorority Matriarch", "description": "Protective matriarchal authority guiding Greek Row sisters through social, romantic, and academic hazards.", "stat_modifiers": {"charisma": 2, "perception": 1}},
    {"name": "Vulnerable Heart", "description": "Deep craving for genuine affection beneath seductive bravado; vulnerable to emotional intimacy.", "stat_modifiers": {"charisma": 1, "endurance": -1}},
    
    # Sierra Cruz
    {"name": "Serpentine Constriction", "description": "Four meters of iridescent rainbow serpent coils delivering bone-crushing grappling leverage.", "stat_modifiers": {"strength": 3, "agility": -1}},
    {"name": "Ectothermic Slumber", "description": "Cold-blooded physiology requiring warm blankets, sunlit rocks, or shared body heat during cold weather.", "stat_modifiers": {"endurance": -1, "perception": 1}},
    {"name": "Morbid Insight / Applied Necromancy", "description": "Deep academic affinity for decaying matter, bones, and spectral anatomy.", "stat_modifiers": {"intelligence": 3, "perception": 1}},
    {"name": "Craving Warmth", "description": "Instinctive biological drive to coil around trusted companions for radiant thermal comfort.", "stat_modifiers": {"charisma": 1}},

    # Russell Sinclair
    {"name": "Tiger Demihuman Physiology", "description": "Feline sensory whiskers, muscular balance, predatory hearing, and retractable talons.", "stat_modifiers": {"strength": 1, "perception": 2, "agility": 2, "intelligence": -1}},
    {"name": "Master Apprentice Ink Hand", "description": "Flawless fine motor steadiness executing permanent arcane ink and precision linework.", "stat_modifiers": {"agility": 2, "perception": 1}},
    {"name": "Deadpan Pack Immunity", "description": "Unshakeable deadpan composure immune to Alpha barking, intimidation, or theatrical tantrums.", "stat_modifiers": {"charisma": 2, "endurance": 1}},
    {"name": "Five Cocketeers Anchor", "description": "Grounded emotional rock holding the rambunctious Suite 304 roommate dynamic together.", "stat_modifiers": {"endurance": 2, "charisma": 1}},

    # Stanley Davies Jr
    {"name": "Forum Cynic / Online Scar Tissue", "description": "Seasoned veteran of anonymous net forums, flame wars, and digital cynicism.", "stat_modifiers": {"intelligence": 2, "charisma": -1}},
    {"name": "Secret NSFW Illustrator", "description": "Under-the-table anatomical precision and hyper-lucrative private commissions under alias.", "stat_modifiers": {"agility": 2, "perception": 1, "luck": 2}},
    {"name": "Involuntary Full Moon Shift", "description": "Deep biological vulnerability to lunar cycles causing uncontrollable full-body shifts under full moon.", "stat_modifiers": {"endurance": -2, "strength": 2}},
    {"name": "Heavyweight Sloucher", "description": "Massive athletic frame intentionally concealed beneath slouching posture and baggy clothes.", "stat_modifiers": {"strength": 2, "agility": -1}},

    # Darkfire Clan
    {"name": "Sovereign of the Whispering Caves", "description": "Unchallenged dominion over the deep volcanic caverns and ancestral lava fissures.", "stat_modifiers": {"endurance": 3, "charisma": 2}},
    {"name": "Century-Hardened Sinew", "description": "Flesh tempered across decades of subterranean combat and molten sulfur immersion.", "stat_modifiers": {"endurance": 3, "strength": 2}},
    {"name": "Indomitable Will", "description": "Mental fortress unyielding to telepathic intrusion, panic, or supernatural compulsion.", "stat_modifiers": {"endurance": 2, "charisma": 2}},
    {"name": "Pain Tolerance", "description": "Subterranean demon endurance ignoring severe trauma, lacerations, and burn wounds in battle.", "stat_modifiers": {"endurance": 3}},
    {"name": "Apex Tracker", "description": "Predatory olfactory and thermal hunting instincts tuned to pitch-black caves and urban tunnels.", "stat_modifiers": {"perception": 3}},
    {"name": "Close-Quarters Bruiser", "description": "Brutal close-range combat leverage crushing bones and fracturing armor with bare fists.", "stat_modifiers": {"strength": 3}},
    {"name": "Mountain Bastion", "description": "Immovable defensive stance weathering artillery-grade impact without breaking footing.", "stat_modifiers": {"endurance": 3, "strength": 1}},
    {"name": "Hearthmaster", "description": "Mastery of subterranean embers, artisanal braising, and monumental communal banqueting.", "stat_modifiers": {"endurance": 2, "luck": 1}},
    {"name": "Unyielding Grip", "description": "Crushing demonic vice-grip preventing targets from disengaging or escaping holds.", "stat_modifiers": {"strength": 2, "endurance": 1}},
    {"name": "Master of Illusions", "description": "Subtle demonic mirages weaving optical and auditory deceptions into social gatherings.", "stat_modifiers": {"intelligence": 3, "charisma": 2}},
    {"name": "Empathic Diplomat", "description": "Intuitive reading of unspoken desires, corporate tensions, and hidden political leverage.", "stat_modifiers": {"charisma": 3, "perception": 2}},
    {"name": "Sinuous Grace", "description": "Fluid acrobatic agility and silent footsteps masking heavy infernal mass.", "stat_modifiers": {"agility": 3, "perception": 1}}
]

def main():
    print("=== Auto-Provisioning Custom Occupations and Traits for 100% World Parity ===")
    
    print("\n1. Provisioning Occupations...")
    for occ in CUSTOM_OCCUPATIONS:
        prov, item = check_and_provision_entity(
            "occupations",
            occ["name"],
            occ["description"],
            occ["stat_modifiers"]
        )
        print(f"  {'[NEW]' if prov else '[EXISTING]'} Occupation: {item.get('name')} (ID: {item.get('id')})")
        
    print("\n2. Provisioning Traits...")
    for tr in CUSTOM_TRAITS:
        prov, item = check_and_provision_entity(
            "traits",
            tr["name"],
            tr["description"],
            tr["stat_modifiers"]
        )
        print(f"  {'[NEW]' if prov else '[EXISTING]'} Trait: {item.get('name')} (ID: {item.get('id')})")
        
    print("\n=== Auto-Provisioning Complete! ===")

if __name__ == '__main__':
    main()
