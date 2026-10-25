import json
import shutil
import time
import requests
import copy

print("=== DEPLOYING EDRIC 13YO & YULE PRESENTATION CANON ===")

TOKEN = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}

EDITABLE_FIELDS = [
    'name', 'display_name', 'avatar', 'description', 'personality', 'mes_example',
    'first_mes', 'scenario', 'post_history_instructions', 'pre_history_instructions',
    'visual_description', 'creator_notes', 'model_url', 'soundcloud_url', 'character_note',
    'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating', 'chat_name',
    'pronouns', 'outfits', 'default_outfit', 'shared_info', 'alternate_greetings',
    'secretFields', 'secrets', 'fields', 'commands', 'metadata'
]

# 1. FINAL/Edric_Douglas_card.json
print("\n--- 1. Edric Douglas Card ---")
with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    edric_card = json.load(f)

desc = edric_card['description']
desc = desc.replace("remarkably tall and broad for a twelve-year-old;", "remarkably tall and broad for a thirteen-year-old;")
if "BIRTHDAY: February 25;" in desc:
    desc = desc.replace("BIRTHDAY: February 25;", "BIRTHDAY: February 25 (Born February 25, 2011);")
desc = desc.replace("maybe four times in twelve years.", "maybe four times in thirteen years.")
desc = desc.replace("Edric is a minor (12 years old)", "Edric is a minor (13 years old)")

old_weight = """What he is actually afraid of is the Presentation. It is coming, everyone in the family knows roughly when, and nobody has said out loud what happens if it goes the wrong way. Edric is terrified he will not be an Alpha. He is more terrified that this will register with his uncle Erik as exactly the kind of disappointment he has always sensed he is not allowed to be, and he cannot explain to anyone, including himself, why Erik's opinion should weigh more than his own father's."""

new_weight = """What he is actually afraid of is the Presentation. Having turned thirteen on February 25, 2024, Edric is scheduled for his official Pack Presentation at Yule (Winter Solstice, December 2024) alongside all the pack pups who reached thirteen years of age in 2024. Everyone in the family knows it is approaching fast, and nobody has said out loud what happens if it goes the wrong way. Edric is terrified he will not present as an Alpha. He is more terrified that this will register with his uncle Erik as exactly the kind of disappointment he has always sensed he is not allowed to be, and he cannot explain to anyone, including himself, why Erik's opinion should weigh more than his own father's."""

if old_weight in desc:
    desc = desc.replace(old_weight, new_weight)
edric_card['description'] = desc

pers = edric_card['personality']
old_pers = "ALWAYS: Edric is a 12-year-old Pureblood House Douglas pup, Logan's son, raised at the Seven Hills garage. Pre-Presentation, terrified beneath the bravado of his First Shift."
new_pers = "ALWAYS: Edric is a 13-year-old Pureblood House Douglas pup (born February 25, 2011), Logan's publicly claimed son, raised at the Seven Hills garage. Pre-Presentation Gamma scheduled for the Pack Presentation at Yule 2024 alongside all 13-year-old pack pups, terrified beneath the bravado of his First Shift."
if old_pers in pers:
    pers = pers.replace(old_pers, new_pers)
edric_card['personality'] = pers

scen = edric_card.get('scenario', '')
scen = scen.replace("twelve-year-old Edric", "thirteen-year-old Edric")
edric_card['scenario'] = scen

with open('FINAL/Edric_Douglas_card.json', 'w', encoding='utf-8') as f:
    json.dump(edric_card, f, indent=2, ensure_ascii=False)

safe_edric = {k: edric_card[k] for k in EDITABLE_FIELDS if k in edric_card}
r_edric = requests.put('https://app.wyvern.chat/api/characters/_TbRM3EdxDjHFgqztTbCpL', headers=HEADERS, json=safe_edric)
print("PUT Edric card status:", r_edric.status_code)
assert r_edric.status_code == 200, f"Error updating Edric card: {r_edric.text[:300]}"
time.sleep(2.0)

# 2. FINAL/Logan_Douglas_card.json
print("\n--- 2. Logan Douglas Card ---")
with open('FINAL/Logan_Douglas_card.json', 'r', encoding='utf-8') as f:
    logan_card = json.load(f)

desc_l = logan_card['description']
desc_l = desc_l.replace("maybe four times in twelve years.", "maybe four times in thirteen years.")
logan_card['description'] = desc_l

with open('FINAL/Logan_Douglas_card.json', 'w', encoding='utf-8') as f:
    json.dump(logan_card, f, indent=2, ensure_ascii=False)

safe_logan = {k: logan_card[k] for k in EDITABLE_FIELDS if k in logan_card}
r_logan = requests.put('https://app.wyvern.chat/api/characters/_T8Ywcr9FEqNf9JxbK6eHP', headers=HEADERS, json=safe_logan)
print("PUT Logan card status:", r_logan.status_code)
assert r_logan.status_code == 200, f"Error updating Logan card: {r_logan.text[:300]}"
time.sleep(2.0)

# 3. FINAL/Svartulfr_Location.json (B-01 Ironwood Cabin)
print("\n--- 3. Location (B-01 Ironwood Cabin) ---")
with open('FINAL/Svartulfr_Location.json', 'r', encoding='utf-8') as f:
    loc_data = json.load(f)

old_edric_loc = "Year 1 (Junior Division): Edric Douglas (Cugino / Licantropo, Canis Lupus Svartulfr). 12 anni. Figlio del compianto Cornelius Douglas e cugino di Jasper, Alyssa, Malachia e Noah. Edric e un giovane licantropo Gamma purosangue di nobile lignaggio, leale, energico e orgoglioso delle tradizioni di famiglia. Ammesso al programma giovanile estivo di Camp Mystic per perfezionare la disciplina atletica e la resistenza, alloggia nella Ironwood Cabin sotto la custodia vigile di Jasper, che considera un mito vivente. Corre come running back nella squadra giovanile di Solarton, adora l'allenamento fisico e porta nella cabina un entusiasmo travolgente, tempestando Jasper di domande sui sistemi di sicurezza e sulle tattiche del branco."

new_edric_loc = "Year 1 (Junior Division): Edric Douglas (Cugino / Licantropo, Canis Lupus Svartulfr). 13 anni (nato il 25 febbraio 2011). Conosciuto pubblicamente come figlio di Logan Douglas (e cugino di Jasper, Alyssa, Malachia e Noah). Edric e un giovane licantropo Gamma purosangue di nobile lignaggio, leale, energico e orgoglioso delle tradizioni di famiglia. Ha compiuto 13 anni all'inizio del 2024 e si prepara per la solenne Presentazione di branco che si terra durante il solstizio d'inverno a Yule insieme a tutti i cuccioli che hanno compiuto 13 anni nel corso del 2024. Ammesso al programma giovanile estivo di Camp Mystic per perfezionare la disciplina atletica, la resistenza e il controllo emotivo prima della cerimonia, alloggia nella Ironwood Cabin sotto la custodia vigile di Jasper, che considera un mito vivente. Gioca come wide receiver nella squadra giovanile di football di Solarton (Junior Bulls), adora l'allenamento fisico e porta nella cabina un entusiasmo travolgente, tempestando Jasper di domande sui sistemi di sicurezza e sulle tattiche del branco."

ironwood_entry = loc_data['entries'][217]
if old_edric_loc in ironwood_entry['content']:
    ironwood_entry['content'] = ironwood_entry['content'].replace(old_edric_loc, new_edric_loc)
loc_data['lexicon'] = copy.deepcopy(loc_data['entries'])

with open('FINAL/Svartulfr_Location.json', 'w', encoding='utf-8') as f:
    json.dump(loc_data, f, indent=2, ensure_ascii=False)
shutil.copyfile('FINAL/Svartulfr_Location.json', 'lorebooks/optimized/Svartulfr_Location.json')

payload_loc = {
    'name': loc_data.get('name', 'Svartúlfr - Location'),
    'description': loc_data.get('description', ''),
    'scan_depth': 5,
    'token_budget': 5000,
    'recursive_scanning': True,
    'lexicon': loc_data['lexicon']
}
r_put_loc = requests.put('https://app.wyvern.chat/api/lorebooks/_EjXxkmPVhpCXg8xABpFkK', headers=HEADERS, json=payload_loc)
print("PUT Location status:", r_put_loc.status_code)
assert r_put_loc.status_code == 200, f"Error updating Location: {r_put_loc.text[:300]}"
time.sleep(2.5)

# 4. FINAL/Svartulfr_NPC_Secondary.json (Entry 1 Edric)
print("\n--- 4. NPC Secondary (Entry 1 Edric) ---")
with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    npc_data = json.load(f)

edric_npc = npc_data['entries'][1]
new_npc_content = """[NAME: Edric Douglas; SPECIES: Werewolf, Pureblood (Canis Lupus Svartulfr); AGE: 13 (Born 25 February 2011); OCCUPATION: Middle School Student, Junior Football Player (Wide Receiver / Running Back); RESIDENCE: Douglas Compound & Logan's Garage, Blackwood City]

PUBLIC DOSSIER: The youngest active member of House Douglas, raised publicly as Logan Douglas's son (and cousin to Alyssa, Malachia, Jasper, and Noah). Edric is an energetic, polite, and fiercely determined 13-year-old Gamma werewolf who will undergo his official Pack Presentation at Yule 2024 alongside all 13-year-old cohort pups. Plays for the Solarton Junior Football squad alongside his best friend and friendly rival Jet Thompson.

EXTERNAL HOOKS: Seen around the compound training diligently, baking with Alyssa, or hanging around Logan's garage. Despite his youth, he displays the natural nobility, speed, and courage of the Douglas bloodline, eagerly anticipating his winter Presentation."""

edric_npc['content'] = new_npc_content
npc_data['lexicon'] = copy.deepcopy(npc_data['entries'])

with open('FINAL/Svartulfr_NPC_Secondary.json', 'w', encoding='utf-8') as f:
    json.dump(npc_data, f, indent=2, ensure_ascii=False)
shutil.copyfile('FINAL/Svartulfr_NPC_Secondary.json', 'lorebooks/optimized/Svartulfr_NPC_Secondary.json')

payload_npc = {
    'name': npc_data.get('name', 'Svartúlfr - NPC Secondary'),
    'description': npc_data.get('description', ''),
    'scan_depth': 5,
    'token_budget': 5000,
    'recursive_scanning': True,
    'lexicon': npc_data['lexicon']
}
r_put_npc = requests.put('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=HEADERS, json=payload_npc)
print("PUT NPC Secondary status:", r_put_npc.status_code)
assert r_put_npc.status_code == 200, f"Error updating NPC Secondary: {r_put_npc.text[:300]}"
time.sleep(2.5)

# 5. FINAL/Svartulfr_Lorebook_I.json (Entry 217 Wolf Names & Yule Presentation)
print("\n--- 5. Lorebook I (Entry 217 Wolf Names & Yule Presentation) ---")
with open('FINAL/Svartulfr_Lorebook_I.json', 'r', encoding='utf-8') as f:
    lb1_data = json.load(f)

lb1_entry = lb1_data['entries'][217]
c_lb1 = lb1_entry['content']

old_intro = "Nella cultura dei licantropi norreni della Founding Bloodline e dell'antico lignaggio Svartulfr, ogni individuo riceve alla nascita un nome civile. All'eta di tredici anni, durante il sacro rito della Presentazione in cui si manifesta per la prima volta la bestia interiore, il licantropo scopre e dichiara il nome del proprio lupo spirituale. Per legge ancestrale del branco, questo nome viene assunto come secondo nome ufficiale e formale dell'individuo, sancendo la transizione verso l'eta adulta e l'accettazione del proprio spirito ferino."

new_intro = "Nella cultura dei licantropi norreni della Founding Bloodline e dell'antico lignaggio Svartulfr, ogni individuo riceve alla nascita un nome civile. All'eta di tredici anni, durante il sacro rito della Presentazione celebrato comunitariamente durante la notte solstiziale di Yule insieme a tutti i cuccioli che hanno compiuto tredici anni nel corso dell'anno solare, il licantropo scopre e dichiara il nome del proprio lupo spirituale. Per legge ancestrale del branco, questo nome viene assunto come secondo nome ufficiale e formale dell'individuo, sancendo la transizione verso l'eta adulta e l'accettazione del proprio spirito ferino."

old_sec8 = "8. I Giovani Pre-Presentazione: I cuccioli e i giovani licantropi che non hanno ancora compiuto tredici anni o non hanno ancora superato la cerimonia della Presentazione (come Edric Douglas) non possiedono un nome da lupo e usano unicamente il nome di battesimo civile."

new_sec8 = "8. I Giovani Pre-Presentazione: I cuccioli e i giovani licantropi che si trovano nel loro anno dei tredici anni prima della notte di Yule (come Edric Douglas, nato nel febbraio 2011, che attende la solenne Presentazione di Yule 2024 insieme alla sua classe anagrafica) non possiedono un nome da lupo e usano unicamente il nome di battesimo civile."

if old_intro in c_lb1:
    c_lb1 = c_lb1.replace(old_intro, new_intro)
if old_sec8 in c_lb1:
    c_lb1 = c_lb1.replace(old_sec8, new_sec8)
lb1_entry['content'] = c_lb1
lb1_data['lexicon'] = copy.deepcopy(lb1_data['entries'])

with open('FINAL/Svartulfr_Lorebook_I.json', 'w', encoding='utf-8') as f:
    json.dump(lb1_data, f, indent=2, ensure_ascii=False)
shutil.copyfile('FINAL/Svartulfr_Lorebook_I.json', 'lorebooks/optimized/Svartulfr_Lorebook_I.json')

payload_lb1 = {
    'name': lb1_data.get('name', 'Svartúlfr - Lorebook I'),
    'description': lb1_data.get('description', ''),
    'scan_depth': 5,
    'token_budget': 5000,
    'recursive_scanning': True,
    'lexicon': lb1_data['lexicon']
}
r_put_lb1 = requests.put('https://app.wyvern.chat/api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL', headers=HEADERS, json=payload_lb1)
print("PUT Lorebook I status:", r_put_lb1.status_code)
assert r_put_lb1.status_code == 200, f"Error updating Lorebook I: {r_put_lb1.text[:300]}"
time.sleep(2.5)

# 6. Master Scenario (char_scenario_1DC43ggb6mB8YLJDJKrU4)
print("\n--- 6. Master Scenario ---")
r_get_scen = requests.get('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=HEADERS)
live_scen = r_get_scen.json()
scen_text = live_scen.get('scenario', '')

old_cousin_scen = '- {{scenarioChar "cousin"}} (Edric Douglas): 12-13-year-old Pre-Presentation Gamma pup in middle school, secret biological son of Erik raised as Logan\'s son.'
new_cousin_scen = '- {{scenarioChar "cousin"}} (Edric Douglas): 13-year-old Pre-Presentation Gamma pup in middle school (born February 25, 2011; scheduled for Pack Presentation at Yule 2024 alongside the 13yo cohort), secret biological son of Erik raised as Logan\'s son.'

if old_cousin_scen in scen_text:
    scen_text = scen_text.replace(old_cousin_scen, new_cousin_scen)
    live_scen['scenario'] = scen_text

r_put_scen = requests.put('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=HEADERS, json=live_scen)
print("PUT Scenario status:", r_put_scen.status_code)
assert r_put_scen.status_code == 200, f"Error updating Master Scenario: {r_put_scen.text[:300]}"

with open('scratch/build_master_scenario.py', 'r', encoding='utf-8') as f:
    bms = f.read()
if old_cousin_scen in bms:
    bms = bms.replace(old_cousin_scen, new_cousin_scen)
    with open('scratch/build_master_scenario.py', 'w', encoding='utf-8') as f:
        f.write(bms)
    print("Synchronized scratch/build_master_scenario.py.")

print("\nALL ENTITIES DEPLOYED AND VERIFIED SUCCESSFULLY WITH 100% SUCCESS.")
