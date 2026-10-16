import json
import pathlib
import re
import datetime

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
OPT_DIR = ROOT / 'lorebooks' / 'optimized'

# 1. Save fresh Firebase token
TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwNGIwZjkxYmU2ZWIwODY3ZGFiYmFhYjU4N2RmYzJlMzNmMDBhMjQiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTHlzIiwicGljdHVyZSI6Imh0dHBzOi8vaW1hZ2VkZWxpdmVyeS5uZXQvRHY0a29Pd0hRVTNYblhMcXRsMGFWUS9iZDE4Y2UwYy02OTk0LTQ3MjktODQ1ZC0xZmIxZTc1OWY5MDAvcHVibGljIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2tvaW9zLWFjYWRlbXkiLCJhdWQiOiJrb2lvcy1hY2FkZW15IiwiYXV0aF90aW1lIjoxNzkxMDY1MDExLCJ1c2VyX2lkIjoiMnI0ZlZwdkltdGU1ZGJsamVkTGtaSnhyZTJkMiIsInN1YiI6IjJyNGZWcHZJbXRlNWRibGplZExrWkp4cmUyZDIiLCJpYXQiOjE3OTIxNTQ5MzMsImV4cCI6MTc5MjE1ODUzMywiZW1haWwiOiJtYW5kZWxsaWFsaWNlNUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwMzQzNDM3MzUzNTc4Nzg4NjAxNiJdLCJlbWFpbCI6WyJtYW5kZWxsaWFsaWNlNUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.2YzdWmhXWQTD1J0Fq-6Ur0YIBgNHuz8kXiixW4jILwJFoPBz9e_v0o3qJqv9f8RcQZE4C8iIG3kpg_te9Vo7BWfXm028lEDSMoG6sU2FQRmcEjRbxR7iK78CoNwLBcRR41KxrQnHjM2U8VBIkkcutaKW1FqVIiOYhQOHatWHHoFhSINKuupr-1A9eI4VCDjMa7Cub-gO0oD7dOU1cGn7qLD8MLSE6bKJoyYyCPtXtTX9Hf7XRSXg_977uGRqUn3_NzZ4W_NPDlmwD1LQzBccNvUme5MzQQElvrbdOm6sXxbBR_lF-tj8jnU7s0eyvMlLoe0DoYh5mRjAqFx6tdXj8g"
(ROOT / 'scratch' / 'wyvern_token.txt').write_text(TOKEN, encoding='utf-8')

computed_rpg = json.loads((ROOT / 'scratch' / 'computed_final_rpg_stats.json').read_text(encoding='utf-8'))
exp = json.loads((ROOT / 'exports' / 'Svartulfr_Export.json').read_text(encoding='utf-8'))

# Build birthdate map from world_characters in Svartulfr_Export.json
# World Epoch: 21 Dec 827 UTC, Current World Age: 10486470 (5 April 2024)
EPOCH_HOURS = 10486470
age_by_name = {}
for wc in exp.get('world_characters', []):
    bd = wc.get('birthdate')
    if bd is not None:
        years = max(18, int(round((EPOCH_HOURS - bd) / (365.2425 * 24))))
        for k in [wc.get('display_name'), wc.get('first_name'), f"{wc.get('first_name','')} {wc.get('last_name','')}".strip()]:
            if k:
                age_by_name[k.lower()] = str(years)

def infer_age(name_str: str, content: str) -> str:
    nl = name_str.lower()
    if nl in age_by_name:
        return age_by_name[nl]
    # Check if Born YYYY is in content
    m_born = re.search(r'\bBorn\s+(?:\d{1,2}\s+\w+\s+)?(\d{3,4})\b', content)
    if m_born:
        yr = int(m_born.group(1))
        return str(2024 - yr)
    # Check if an explicit age in prose exists (e.g. "di 40 anni", "22-year-old", "ventenne", etc.)
    m_yr = re.search(r'\b(\d{2,4})[- ]year[- ]old\b', content, re.IGNORECASE)
    if m_yr:
        return m_yr.group(1)
    # Check role heuristics
    cl = content.lower()
    if 'marek' in nl:
        return '38 (Born 18 March 1986)'
    if 'freshman' in cl or 'matricola' in cl or 'first-year' in cl:
        return '19'
    if 'sophomore' in cl or 'second-year' in cl:
        return '20'
    if 'junior' in cl or 'third-year' in cl:
        return '21'
    if 'senior' in cl or 'fourth-year' in cl or 'captain' in cl or 'fraternity president' in cl:
        return '22'
    if 'student' in cl or 'studente' in cl or 'succ' in cl and ('dorm' in cl or 'major' in cl or 'varsity' in cl or 'cheerleader' in cl):
        return '20'
    if 'professor' in cl or 'dean' in cl or 'director' in cl or 'veteran' in cl or 'patriarch' in cl or 'matriarch' in cl:
        return '45'
    if 'ancient' in cl or 'primordial' in cl or 'millennia' in cl or 'elder' in cl:
        return '450'
    return '28'

# 2. Extract canonical Blue Oni Marek from Svartulfr_NPC_Secondary.json
sec_path = FINAL_DIR / 'Svartulfr_NPC_Secondary.json'
prim_path = FINAL_DIR / 'Svartulfr_NPC_Primary.json'
sec_data = json.loads(sec_path.read_text(encoding='utf-8'))
prim_data = json.loads(prim_path.read_text(encoding='utf-8'))

canonical_marek_entry = None
new_sec_entries = []
for e in sec_data['entries']:
    if 'Marek' in e.get('keys', []) and 'Blue Oni' in (e.get('content') or ''):
        canonical_marek_entry = e
    else:
        new_sec_entries.append(e)

sec_data['entries'] = new_sec_entries

if canonical_marek_entry:
    marek_content = canonical_marek_entry['content'].replace('AGE: {{age}};', 'AGE: 38 (Born 18 March 1986);')
    marek_rpg = computed_rpg['marek']['rpg_block']
    if 'RPG STATS & TRAITS:' in marek_content:
        marek_content = re.sub(r'RPG STATS & TRAITS:.*', marek_rpg, marek_content, flags=re.DOTALL)
    else:
        marek_content = marek_content.rstrip() + '\n\n' + marek_rpg
    marek_content = marek_content.replace('—', ', ')

    # Update Marek in Svartulfr_NPC_Primary.json
    replaced_prim = False
    for e in prim_data['entries']:
        if 'Marek' in e.get('keys', []):
            e['keys'] = ['Marek', 'Blue Oni', 'The Iron Hammer', 'Blue Devil']
            e['content'] = marek_content
            e['comment'] = 'Marek (The Iron Hammer — Blue Oni, Ironhorn Nomads Primary Enforcer)'
            replaced_prim = True
            print('Replaced Minotaur Marek in Svartulfr_NPC_Primary.json with canonical Blue Oni Marek!')
            break

    # Also rebuild FINAL/Marek_card.json with canonical Blue Oni Marek!
    FORMAT_RULE = "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
    marek_card = {
        'name': 'Marek',
        'chat_name': 'Marek',
        'tagline': 'The Iron Hammer — Blue Oni Primary Enforcer of the Ironhorn Nomads MC & Underworld Fixer',
        'avatar': '',
        'description': marek_content,
        'personality': '[NAME: Marek; ALIASES: The Iron Hammer, Blue Devil; SPECIES: Blue Oni; AGE: 38 (Born 18 March 1986); HEIGHT: 206cm (6\'9"); OCCUPATION: Ironhorn Nomads Primary Enforcer, Black-Market Fixer ("Ghosting"), Master Motorcycle Mechanic; TRAITS: Dominant, Charismatic Devil, Possessive, Street-Principled, Superstitious (never drinks the last sip)]',
        'visual_description': 'Colossal 206cm (6\'9") Blue Oni with dark royal-blue skin marked by combat scars, two large forward-curving dark horns on his forehead, long flowing snow-white hair and trimmed white goatee, piercing cold blue-grey eyes, wearing an open leather Ironhorn Nomads biker cut.',
        'first_mes': 'Marek fa il suo ingresso a torso nudo, imponente nei suoi due metri e sei di muscoli color blu reale, i lunghi capelli bianchi raccolti in una coda sciolta e le due corna scure che fendono la luce dei riflettori. "Rilassati, fiorellino. Qui nessuno fiata finche\' sei con me."',
        'mes_example': '',
        'scenario': 'Club House Ironhorn Nomads & Blackwood/Chicagoland Interstate Corridors, 2024.',
        'pre_history_instructions': 'Play Marek ("The Iron Hammer"), a colossal 206cm Blue Oni and Primary Enforcer of the Ironhorn Nomads Motorcycle Club. Smooth, dangerous, possessive, gravelly baritone.',
        'post_history_instructions': FORMAT_RULE,
        'character_note': 'Marek ("The Iron Hammer", Blue Oni, 206cm, royal-blue skin, snow-white hair, two dark horns, grey-blue eyes). Primary Enforcer of the Ironhorn Nomads MC & "Ghosting" black-market fixer. ' + FORMAT_RULE,
        'creator_notes': 'Canonical Blue Oni Marek from Svartulfr_NPC_Secondary & Chapter 11 Scenario.',
        'visibility': 'private',
        'rating': 'explicit',
        'pronouns': 'he/him',
        'tags': ['Svartulfr', 'Oni', 'Biker', 'Ironhorn Nomads'],
        'outfits': [],
    }
    (FINAL_DIR / 'Marek_card.json').write_text(json.dumps(marek_card, indent=2, ensure_ascii=False), encoding='utf-8')
    print('Rebuilt FINAL/Marek_card.json with canonical Blue Oni Marek!')

# 3. Replace all {{age}} macros in Svartulfr_NPC_Primary.json and Svartulfr_NPC_Secondary.json
for label, data, fpath, opt_path in [
    ('NPC_Primary', prim_data, prim_path, OPT_DIR / 'Svartulfr_NPC_Primary.json'),
    ('NPC_Secondary', sec_data, sec_path, OPT_DIR / 'Svartulfr_NPC_Secondary.json'),
]:
    fixed_ages = 0
    for e in data['entries']:
        c = e.get('content') or ''
        if '{{age}}' in c:
            m_name = re.search(r'\[NAME:\s*([^;\]]+)', c)
            cname = m_name.group(1).strip() if m_name else (e.get('keys', [''])[0] if e.get('keys') else '')
            inferred = infer_age(cname, c)
            e['content'] = c.replace('{{age}}', inferred)
            fixed_ages += 1
    fpath.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    opt_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'{label}: replaced {{{{age}}}} in {fixed_ages} entries (total entries={len(data["entries"])})')
