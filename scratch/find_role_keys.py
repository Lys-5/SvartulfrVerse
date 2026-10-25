import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

ROLE_WORDS = {
    'the compound', 'solarton pd', 'barista', 'bartender', 'professor', 'hex valley',
    'nurse', 'drider', 'succubus', 'health centre', 'philosophy', 'humanities',
    'hivemind', 'tendrils', 'eel', 'marksman', 'asl', 'Pureblood', 'pureblood',
    'smuggling', 'the docks', 'Arcadia', 'arcadia', 'tech guy', 'arctic wolf',
    'left wing', 'solitary wolves', 'espresso', 'genderfluid', 'luxury supplier',
    'silk suits', 'tactician', 'photography', 'darkroom', 'wings', 'football coach',
    'Assistant coach', 'intel broker', 'intelligence network', 'mascot', 'anime club',
    'tattoo artist', 'Wyrm Dormitories', 'Claw&Steel', 'Jasper roommate',
    'hockey captain', 'Private Detective', 'Fixer', 'Mortician', 'Hunter', 'Trapper',
    'Coach', 'baker', 'croissant', 'rat', 'staff', 'president', 'ksa', 'brownies',
    'TIT Sorority', 'Uptown North', 'Uptown South', 'Bluemoon North', 'Bluemoon South',
    'Paradise East', 'Paradise West', 'Oldtown', 'Dockside', 'Ironworks district'
}

for lb_file in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    lb = json.loads((FINAL / lb_file).read_text(encoding='utf-8'))
    for idx, e in enumerate(lb.get('entries', [])):
        ks = e.get('keys', [])
        bad = [k for k in ks if k in ROLE_WORDS or k.lower() in {w.lower() for w in ROLE_WORDS}]
        if bad:
            out.append(f"{lb_file} #{idx} ({e.get('name')}): {bad} in {ks}")

(ROOT / 'scratch' / 'role_keys_found.txt').write_text('\n'.join(out), encoding='utf-8')
print(f"Found {len(out)} entries with role/place keys")
