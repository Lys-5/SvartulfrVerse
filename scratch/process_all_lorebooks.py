import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
OPT = ROOT / 'lorebooks' / 'optimized'

PRONOUN_MAP = {
    '{{pronounSubjective}}': 'she',
    '{{pronounSubjectiveCap}}': 'She',
    '{{pronounObjective}}': 'her',
    '{{pronounObjectiveCap}}': 'Her',
    '{{pronounPosDet}}': 'her',
    '{{pronounPosDetCap}}': 'Her',
    '{{pronounPosPro}}': 'hers',
    '{{pronounPosProCap}}': 'Hers',
    '{{pronounReflexive}}': 'herself',
    '{{pronounReflexiveCap}}': 'Herself',
}

def replace_alyssa_macros(text: str) -> str:
    if not text:
        return text
    text = text.replace('{{user}}', 'Alyssa')
    for k, v in PRONOUN_MAP.items():
        text = text.replace(k, v)
    # Fix Italian "ad Alyssa" / "Ad Alyssa" if needed, both are fine in Italian
    return text

def strip_instructions(text: str) -> str:
    if not text:
        return text
    # Remove [INSTRUCTIONS: ...] blocks
    text = re.sub(r'\n*\[INSTRUCTIONS:.*?\]\s*', '\n', text, flags=re.S)
    return text.strip()

# 5 new NPC Secondary entries updated with 7-attribute Final Stats
THRAKGOR_RPG = """RPG STATS & TRAITS:
[LEVEL: 38; SPECIES: Mountain Orc (STR +3, END +2, INT -1); OCCUPATION: Warchief / Warlord (STR +2, END +1, CHA +1); CLASS: Untamed Mountain Warchief & Vanguard Cleaver]
[STATS: STR 25; PER 13; END 22; CHA 15; INT 8; AGI 11; LCK 9]
TRAITS:
- Brutal Cleave (STR +3, AGI -1): Devastating two-handed war-axe strikes capable of shearing through reinforced steel and defensive barriers.
- Warchief Roar (CHA +2, END +1): Booming guttural battle cry that rallies clan warriors and intimidates lesser foes into submission.
- Thick Hide (END +3, AGI -1): Dense, battle-scarred grayish-green skin and heavy muscle mass that shrug off blades and blunt trauma.
- Indomitable Might (STR +2, END +1): Unyielding physical dominance forged through decades of ruthless mountain tribal warfare."""

CROWE_RPG = """RPG STATS & TRAITS:
[LEVEL: 26; SPECIES: Canid Demihuman Hybrid (Feral Hound) (PER +2, END +1, AGI +2, CHA -1); OCCUPATION: Bounty Tracker & Assault Mercenary (PER +2, AGI +2); CLASS: Silent Shadow Hound & Contract Hunter]
[STATS: STR 14; PER 23; END 16; CHA 7; INT 11; AGI 24; LCK 10]
TRAITS:
- Bloodhound Scent (PER +3): Hyper-acute olfactory tracking capable of isolating a target's pheromones or blood trail across miles of urban grime.
- Predatory Leap (STR +1, AGI +3): Explosive, soundless ambush speed that closes distance before a target can draw a weapon.
- Unflinching Devotion (END +2, CHA -1): Fiercely protective survivalist loyalty toward the rare individuals who treat him as a person rather than a weapon.
- Feral Agility (PER +1, AGI +2): Razor-sharp reflexes and silent movement honed in underground fight pits and back-alley warfare."""

MORGETH_RPG = """RPG STATS & TRAITS:
[LEVEL: 42; SPECIES: Half-Orc / Half-Eadra Hybrid (STR +2, END +2, INT +2, AGI -1); OCCUPATION: Master Arcane Blacksmith (STR +2, PER +1, INT +2); CLASS: Runic Forge Master & Sovereign Metallurgist]
[STATS: STR 21; PER 16; END 21; CHA 10; INT 22; AGI 8; LCK 11]
TRAITS:
- Master Metallurgist (STR +2, PER +1, INT +2): Peerless command of quench temperatures, folded alloys, meteorite ore, and structural tensile strength.
- Arcane Runic Infusion (PER +1, INT +3): Inherited Eadra channeling that binds living elemental enchantments directly into forged steel and armor plates.
- Tusked Resilience (END +3, CHA -1): Massive anvil-shouldered Half-Orc constitution impervious to extreme forge heat, slag burns, and physical exhaustion.
- Forge Master (STR +1, END +1, LCK +1): Reverent craftsmanship producing legendary weapons and heavy vehicle plating coveted across supernatural factions."""

THORVALD_RPG = """RPG STATS & TRAITS:
[LEVEL: 32; SPECIES: Werewolf (Founding Bloodline / Ut Berg Descendant) (STR +2, PER +1, END +2, INT -1); OCCUPATION: Ancestral Forest Ranger (STR +1, PER +2, END +1); CLASS: Frostbound Guardian & Firstborn Hirdman]
[STATS: STR 22; PER 19; END 23; CHA 12; INT 11; AGI 14; LCK 10]
TRAITS:
- Founding Bloodline (Ut Descendant) (STR +1, END +2, CHA +2): Direct primordial lineage of the Stone Titan Ut Berg, granting extraordinary physical density and ancestral authority.
- Stone Titan Resilience (STR +2, END +3, AGI -1): Rock-hard muscle density and unbreakable bone structure inherited from the Second Fang of Fenris.
- Wilderness Tracker (PER +3, AGI +1): Master of alpine survival, scent tracking across snow and granite, and silent woodland patrol.
- Primal Howl (STR +1, CHA +1): Resonant northern war cry that echoes through the old-growth pines and calls the hinterland pack to arms.
- Frost Resistance (END +2): Complete physiological adaptation to sub-zero mountain blizzards and freezing wilderness conditions."""

HARALD_RPG = """RPG STATS & TRAITS:
[LEVEL: 36; SPECIES: Werewolf (Founding Bloodline / Fallen Firstborn Scion) (STR +2, PER +1, END +2, INT -1); OCCUPATION: Jarl of the Hinterlands (STR +2, CHA +2, INT +1); CLASS: Ancestral Warlord & Hinterland Jarl]
[STATS: STR 23; PER 16; END 21; CHA 20; INT 13; AGI 13; LCK 10]
TRAITS:
- Founding Bloodline (Fallen Firstborn Scion) (STR +1, END +2, CHA +2): Direct scion of one of the Nine Primordial Firstborn created by Fenris who fell in the wars of antiquity.
- Jarl Command (CHA +3, INT +1): Gravely, unyielding sovereign authority that commands instant obedience across the northern hinterland clans.
- Battle-Hardened (STR +2, END +2): Decades of frontline dominance bouts and martial discipline etched into a massive warrior frame.
- Iron Will (END +2, CHA +1): Unshakeable traditionalist resolve that honors blood-sealed oaths above any modern corporate contract.
- Primordial War Cry (STR +2, CHA +1): Savage, bone-chilling ancestral roar carrying the echo of the Fallen Firstborn onto the battlefield."""

RUSS_DOSSIER_CONTENT = """[NAME: Russell 'Russ' Sinclair; ALIAS: Russ; SPECIES: Demihuman Tiger (Single pair of tiger ears atop head, no human ears, striped tiger tail); AGE: 21 (Born March 14, 2003); HEIGHT: 183 cm (6'0"); OCCUPATION: Undergraduate Student at SUCC, Tattoo Apprentice at Sacred Needle Tattoo; AFFILIATION: The Five Cocketeers; RESIDENCE: Wyrm Hall Dorm Suite, Room 304, SUCC Campus (Roommate of Jasper Douglas-Bloodmoon)]

PUBLIC DOSSIER: A lean, heavily tattooed 21-year-old Tiger Demihuman with silver-white undercut hair, sharp pale gray eyes, facial piercings (septum ring, ear gauges, eyebrow dermal, labret), a single pair of striped tiger ears atop his head, and a long expressive tiger tail. Russ is an undergraduate student at SUCC and a talented tattoo apprentice at Sacred Needle Tattoo near campus. Assigned as Jasper Douglas-Bloodmoon's roommate in Room 304 of Wyrm Hall, Russ treats the intimidating Douglas pack reputation with deadpan indifference, enforcing household rules on cable management and sharing the dorm with a stray black cat named Ash. Outside the dorm, he is the blunt, acid-tongued anchor of The Five Cocketeers alongside Raymond, Dean, Javier, and Eric.

EXTERNAL HOOKS: Known around SUCC and Solarton for his sharp draftsmanship at Sacred Needle Tattoo, his bone-dry deadpan humor, and his unvarnished, non-judgmental brotherhood with Jasper Douglas-Bloodmoon."""

MAC_DOSSIER_CONTENT = """[NAME: Mackenzie 'Mac' Sanchez-Rogers; ALIAS: Mac; SPECIES: Werewolf (Pureblood Rogers & Common Sanchez, Unaware / Latent); AGE: 19 (Born 2004); OCCUPATION: Freshman Undergrad at SUCC, Keyboardist of Grave Mistake, Campus Weed Dealer; RESIDENCE: Solarton / SUCC Campus]

PUBLIC DOSSIER: A tall, lanky, sun-bronzed 19-year-old freshman at SUCC with bleached messy blond hair, ocean-blue eyes, full tattoo sleeves, and a perpetual cloud of sweet weed smoke. Born in Oakland to Pureblood exile Luisa Rogers and mechanic Alejandro Sanchez, Mac is biologically a werewolf but remains completely unaware of his lupine heritage after his parents suppressed his wolf at birth with a bruja ritual. On campus, he is the talented keyboardist of the student rock band Grave Mistake (alongside Jasper, Fade, Via, and Roland) and a laid-back local weed dealer who hides his academic insecurities and childhood scars behind loud West Coast bravado and easy charm. Mutual crush of Alyssa Douglas-Bloodmoon.

EXTERNAL HOOKS: Well-known across SUCC for his synth and keyboard riffs at Sidewinders and frat parties, his reliable campus weed hookups, and his protective, flustered devotion whenever Alyssa Douglas-Bloodmoon is around."""

def process_lorebooks():
    for lb_file in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
        path = FINAL / lb_file
        lb = json.loads(path.read_text(encoding='utf-8'))
        new_entries = []
        for idx, e in enumerate(lb.get('entries', [])):
            # Remove #97 {{user}} Hvit Douglas Bloodmoon from NPC Primary
            if lb_file == 'Svartulfr_NPC_Primary.json' and '{{user}} Hvit Douglas Bloodmoon' in e.get('name', ''):
                print(f"Removing duplicate entry #{idx} ({e.get('name')}) from {lb_file}")
                continue

            # Update #24 Russ Sinclair in NPC Primary to World Dossier
            if lb_file == 'Svartulfr_NPC_Primary.json' and e.get('name') == 'Russ Sinclair':
                e['name'] = "Russell 'Russ' Sinclair"
                e['type'] = 'lore/concept'
                e['keys'] = ['Russ', 'Russ Sinclair', "Russell 'Russ'", 'Russell Sinclair']
                e['secondary_keys'] = ['Sacred Needle', 'Five Cocketeers', 'Room 304', 'Ash']
                e['selective'] = False
                e['content'] = RUSS_DOSSIER_CONTENT
                for f in ['avatar', 'custom_avatar_regex', 'avatar_activation_regex', 'lines_parsed', 'npc_info']:
                    e.pop(f, None)
                print(f"Converted Russ Sinclair (#24) to World Dossier (lore/concept)")

            # Update #55 Mackenzie Sanchez-Rogers in NPC Primary
            if lb_file == 'Svartulfr_NPC_Primary.json' and e.get('name') == 'Mackenzie Sanchez-Rogers':
                e['type'] = 'lore/concept'
                e['keys'] = ['Mackenzie Sanchez-Rogers', 'Mackenzie Rogers', 'Mac Rogers']
                e['secondary_keys'] = ['Grave Mistake', 'Open Casket', 'keyboard', 'dealer', 'Oakland', 'Luisa']
                e['selective'] = False
                e['content'] = MAC_DOSSIER_CONTENT
                print(f"Fixed Mackenzie Sanchez-Rogers (#55) World Dossier")

            # Update 5 new NPC Secondary entries RPG blocks
            if lb_file == 'Svartulfr_NPC_Secondary.json':
                ename = e.get('name', '')
                if ename == 'Thrakgor Deathspine':
                    e['content'] = re.sub(r'\[RPG STATS & TRAITS:.*?\]', THRAKGOR_RPG, e['content'], flags=re.S)
                elif ename == 'Crowe':
                    e['content'] = re.sub(r'\[RPG STATS & TRAITS:.*?\]', CROWE_RPG, e['content'], flags=re.S)
                elif ename == 'Morgeth Steeltooth':
                    e['content'] = re.sub(r'\[RPG STATS & TRAITS:.*?\]', MORGETH_RPG, e['content'], flags=re.S)
                elif ename == 'Thorvald':
                    e['content'] = re.sub(r'\[RPG STATS & TRAITS:.*?\]', THORVALD_RPG, e['content'], flags=re.S)
                elif ename == 'Harald Sigurdsson':
                    e['content'] = re.sub(r'\[RPG STATS & TRAITS:.*?\]', HARALD_RPG, e['content'], flags=re.S)

            # Replace {{user}} -> Alyssa and pronoun macros in name, keys, secondary_keys, content
            e['name'] = replace_alyssa_macros(e.get('name', ''))
            if 'keys' in e and isinstance(e['keys'], list):
                e['keys'] = [replace_alyssa_macros(k) for k in e['keys']]
            if 'secondary_keys' in e and isinstance(e['secondary_keys'], list):
                e['secondary_keys'] = [replace_alyssa_macros(k) for k in e['secondary_keys']]
            e['content'] = replace_alyssa_macros(e.get('content', ''))

            # Strip [INSTRUCTIONS: ...]
            e['content'] = strip_instructions(e['content'])

            # Clean generic keys in NPC Primary & Secondary
            if lb_file in ('Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json'):
                bad_Exact = {
                    'the compound', 'solarton pd', 'barista', 'bartender', 'professor', 'hex valley',
                    'coach', 'private detective', 'fixer', 'mortician', 'hunter', 'trapper',
                    'assistant coach', 'football coach', 'hockey captain', 'tech guy', 'tactician',
                    'Pureblood', 'pureblood', 'Uptown North', 'Uptown South', 'Bluemoon North',
                    'Bluemoon South', 'Paradise East', 'Paradise West', 'Oldtown', 'Dockside',
                    'Ironworks district', 'Arcadia', 'the docks', 'smuggling', 'philosophy',
                    'Humanities', 'hivemind', 'tendrils', 'eel', 'marksman', 'ASL', 'arctic wolf',
                    'left wing', 'solitary wolves', 'espresso', 'genderfluid', 'luxury supplier',
                    'silk suits', 'photography', 'darkroom', 'wings', 'intel broker',
                    'intelligence network', 'mascot', 'anime club', 'nurse', 'drider', 'succubus',
                    'health centre', 'TIT Sorority', 'brownies'
                }
                bad_lower = {x.lower() for x in bad_Exact}
                orig_keys = e.get('keys', [])
                filtered_keys = [k for k in orig_keys if k.strip().lower() not in bad_lower]
                # Ensure we never leave an entry with 0 keys (e.g. Bruce, Campus Staff Rat, Adrian)
                if not filtered_keys:
                    filtered_keys = [e['name']]
                elif e['name'] == 'Bruce':
                    filtered_keys = ['Bruce', 'Bruce KSA']
                elif e['name'] == 'Campus Staff Rat':
                    filtered_keys = ['Campus Staff Rat']
                elif e['name'] == 'Adrian':
                    filtered_keys = ['Adrian', 'Adrian Baker']
                e['keys'] = filtered_keys

            # Align LEVEL in NPC Primary & Secondary RPG blocks to AGE (capped at 99)
            if lb_file in ('Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json'):
                c = e.get('content', '')
                if '[LEVEL:' in c:
                    age_m = re.search(r'AGE:\s*(\d+)', c)
                    if e['name'] == 'Zefir Hvitskog':
                        target_lvl = 99 # Born 1005 AD, over 1000 years old
                    elif e['name'] == 'Nixara Hvit Bloodmoon':
                        target_lvl = 29 # Died at age 29 (or 45) -> let's check: AGE: 45 in header
                        target_lvl = 45
                    elif e['name'] == 'Echo':
                        target_lvl = 19
                    elif age_m:
                        target_lvl = min(99, int(age_m.group(1)))
                    else:
                        target_lvl = None
                    if target_lvl is not None:
                        e['content'] = re.sub(r'\[LEVEL:\s*\d+;', f'[LEVEL: {target_lvl};', c)

            # Enforce zero em-dashes and zero asterisks in lorebook entry content
            e['content'] = e['content'].replace('—', ', ').replace('*', '')

            new_entries.append(e)

        lb['entries'] = new_entries
        if 'lexicon' in lb:
            lb['lexicon'] = new_entries
        path.write_text(json.dumps(lb, indent=2, ensure_ascii=False), encoding='utf-8')
        (OPT / lb_file).write_text(json.dumps(lb, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"Saved {lb_file}: {len(new_entries)} entries (mirrored to lorebooks/optimized/)")

if __name__ == '__main__':
    process_lorebooks()
