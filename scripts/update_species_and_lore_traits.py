import sys
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
import urllib.request
import json

def run():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    world_id = '_CgYT8fHXpDC4crjmegQF7'

    print("=== 1. UPDATING WEREWOLF & DEMIHUMAN SPECIES ===")
    species_updates = {
        '_rc4QKj1LcdMMbVzKbzcjg': { # Werewolf
            'name': 'Werewolf',
            'description': 'Supernatural lupine demi-human gifted with dual-heart physiology, rapid moonlight cellular regeneration, hyper-acute senses, single-pair animal ears (no human ears), and partial/hybrid shifting abilities.',
            'stat_modifiers': {
                'strength': 2,
                'endurance': 2,
                'perception': 2,
                'agility': 1,
                'intelligence': 0,
                'charisma': 0,
                'luck': 0
            }
        },
        '_dDjTNdHbC2yDRreDbd8Uh': { # Demihuman
            'name': 'Demihuman',
            'description': 'Humanoid possessing animal traits (ears, tail, claws). Possesses strictly ONE pair of ears: animal ears only, no human ears.',
            'stat_modifiers': {
                'perception': 1,
                'agility': 1,
                'endurance': 1,
                'strength': 0,
                'intelligence': 0,
                'charisma': 0,
                'luck': 0
            }
        }
    }

    for s_id, data in species_updates.items():
        url = f'https://app.wyvern.chat/api/worlds/rpg/species/{s_id}'
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PUT')
        with urllib.request.urlopen(req) as resp:
            print(f"Updated Species {data['name']} ({s_id}) -> 200 OK")

    print("\n=== 2. UPDATING CORE SECONDARY SEX TRAITS (ALPHA, BETA, OMEGA, DELTA) ===")
    trait_updates = {
        '_RpyHF1p2nqzfqTWtxzk6g': { # Alpha
            'name': 'Alpha',
            'description': 'Dominant secondary sex of the pack. Natural leaders and protectors possessing imposing pheromones, territorial instincts, knot and baculum physiology, and the vocal-pheromone Command mechanism.',
            'stat_modifiers': {
                'strength': 2,
                'charisma': 2,
                'endurance': 1,
                'intelligence': 0,
                'agility': 0,
                'perception': 0,
                'luck': 0
            }
        },
        '_gAdBAttdHrEUcGRxpUNRY': { # Beta
            'name': 'Beta',
            'description': 'The grounded backbone and tactical core of the pack. Steadfast, loyal second-in-commands, enforcers, and mediators with steady emotional equilibrium, high resilience, and reliable focus.',
            'stat_modifiers': {
                'endurance': 2,
                'agility': 1,
                'intelligence': 1,
                'strength': 0,
                'charisma': 0,
                'perception': 0,
                'luck': 0
            }
        },
        '_KqFLKp62y3kHPKEAd9Dn7': { # Omega
            'name': 'Omega',
            'description': 'Empathetic secondary sex and emotional heart of the pack. Endowed with hyper-sensitive scent glands, profound maternal/paternal instincts, heat cycles, high pain tolerance, and strong pack bonding.',
            'stat_modifiers': {
                'charisma': 2,
                'perception': 2,
                'endurance': 1,
                'strength': 0,
                'agility': 0,
                'intelligence': 0,
                'luck': 0
            }
        },
        '_WgcKgpxcY6GEhPHXRGpeA': { # Delta
            'name': 'Delta',
            'description': 'Independent and perceptive secondary sex. Natural scouts, mediators, and tactical observers who bridge social gaps between Alphas and Omegas with sharp intuition and agile adaptability.',
            'stat_modifiers': {
                'agility': 2,
                'perception': 1,
                'charisma': 1,
                'strength': 0,
                'endurance': 0,
                'intelligence': 0,
                'luck': 0
            }
        }
    }

    for t_id, data in trait_updates.items():
        url = f'https://app.wyvern.chat/api/worlds/rpg/traits/{t_id}'
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PUT')
        with urllib.request.urlopen(req) as resp:
            print(f"Updated Trait {data['name']} ({t_id}) -> 200 OK")

    print("\n=== 3. CREATING NEW SVARTULFR LORE TRAITS ===")
    new_traits = [
        {
            'name': 'Enigma',
            'description': 'Sacred and apex secondary sex (~1 per generation, including the Nine Firstborn). Dual-natured psychology combining supreme Alpha authority with deep sensory awareness. Possesses irresistible Command, supreme unoverridable scent, and cannot be submitted by any secondary sex.',
            'stat_modifiers': {
                'strength': 3,
                'charisma': 3,
                'endurance': 2,
                'perception': 2
            },
            'player_selectable': True
        },
        {
            'name': 'The White Moon',
            'description': 'Rarest Dominant Omega manifestation in lupine history (sacred title of Alyssa). Immune to Alpha and Enigma Command alike. Radiates a pacifying scent-aura that staves off feral violence, stills aggression, and inspires unshakeable devotion.',
            'stat_modifiers': {
                'charisma': 3,
                'perception': 2,
                'endurance': 2,
                'luck': 2
            },
            'player_selectable': True
        },
        {
            'name': 'Founding Bloodline',
            'description': 'Direct descendants of the Bloodmoon-Douglas founding line (Malachia, Noah, Jasper, Alyssa). Biological maturity halts permanently at 21; features dual-heart physiology in shift, massive physical durability, and accelerated moonlight cellular regeneration.',
            'stat_modifiers': {
                'strength': 2,
                'endurance': 2,
                'charisma': 1
            },
            'player_selectable': True
        },
        {
            'name': 'Divine Blood (Firstborn)',
            'description': 'Consecrated directly by Fenris in 827 AD (Wulfnic, Ut, Zefir). Biologically immortal Primordial Enigmas locked at the age of their divine crowning. Radiates an ancient aura of physical and spiritual inevitability.',
            'stat_modifiers': {
                'strength': 3,
                'endurance': 3,
                'charisma': 3
            },
            'player_selectable': True
        },
        {
            'name': 'Pureblood Heritage',
            'description': 'Descendant of an ancient noble werewolf house (Marino, O\'Connor, Duskwood). Extended lifespan of 200-400 years with graceful aging, superior bloodline stability, and aristocratic pack presence.',
            'stat_modifiers': {
                'charisma': 1,
                'endurance': 1,
                'perception': 1
            },
            'player_selectable': True
        },
        {
            'name': 'Alpha Command',
            'description': 'Mastery of the vocal-pheromone subharmonic register capable of forcing instinctive submission and compliance on standard werewolves.',
            'stat_modifiers': {
                'charisma': 2,
                'strength': 1
            },
            'player_selectable': True
        },
        {
            'name': 'Scent Tracker',
            'description': 'Hyper-acute olfactory nerves capable of dissecting scent plumes miles away, reading pheromonal spikes of fear, arousal, illness, and deceit with forensic precision.',
            'stat_modifiers': {
                'perception': 3
            },
            'player_selectable': True
        },
        {
            'name': 'Partial Shift Mastery',
            'description': 'Seamlessly manifesting predatory wolf ears, razor claws, and glowing amber eyes without undergoing a full bodily transformation, maintaining bipedal human posture and speech.',
            'stat_modifiers': {
                'agility': 2,
                'perception': 1
            },
            'player_selectable': True
        },
        {
            'name': 'Silver Sensitivity',
            'description': 'Severe biological vulnerability to silver contact. Suppresses regeneration, induces agonizing dermal burns, and temporarily paralyzes shift mechanisms.',
            'stat_modifiers': {
                'endurance': -2
            },
            'player_selectable': True
        }
    ]

    # Check which new traits already exist to avoid duplicates
    req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/rpg/traits/{world_id}', headers=headers)
    with urllib.request.urlopen(req) as resp:
        existing_traits = json.loads(resp.read().decode('utf-8'))
    existing_names = {t['name'].lower(): t['id'] for t in existing_traits}

    for nt in new_traits:
        nt_name_lower = nt['name'].lower()
        if nt_name_lower in existing_names:
            t_id = existing_names[nt_name_lower]
            url = f'https://app.wyvern.chat/api/worlds/rpg/traits/{t_id}'
            req = urllib.request.Request(url, data=json.dumps(nt).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                print(f"Updated existing trait: {nt['name']} ({t_id}) -> 200 OK")
        else:
            payload = dict(nt)
            payload['world_id'] = world_id
            url = 'https://app.wyvern.chat/api/worlds/rpg/traits'
            req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
            with urllib.request.urlopen(req) as resp:
                res_data = json.loads(resp.read().decode('utf-8'))
                new_id = res_data.get('id') or res_data.get('_id')
                print(f"Created new trait: {nt['name']} -> ID: {new_id} -> 200 OK")

    print("\n=== ALL UPDATES AND CREATIONS COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    run()
