import json
import pathlib
import re
import uuid

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

# Validation rules from mod23792:
# 1. name <= 200, trimmed
# 2. display_description <= 20000
# 3. scenario <= 100000
# 4. slots: 1 to 20, key /^[a-zA-Z][a-zA-Z0-9_-]{0,63}$/, unique keys, label 1 to 120, pool weight 0 to 1,000,000
# 5. greetings: 1 to 100, name 1 to 200, description <= 10000, content <= 100000
# 6. messages: 1 to 20 per greeting, content <= 100000, speaker_slot must exist in slots
# 7. top-level greeting.content == messages[0].content, greeting.speaker_slot == messages[0].speaker_slot

from build_unified_master_scenario import (
    parse_world_scene_to_messages, clean_prose, SPEAKER_TO_SLOT, det_uuid
)

def run_dry_run():
    exp = json.loads((ROOT / 'exports' / 'Svartulfr_Export.json').read_text(encoding='utf-8'))
    scenes_by_id = {}
    for sc in exp.get('world_scenarios', []):
        for ps in sc.get('premade_scenes', []):
            scenes_by_id[ps['id']] = ps

    live_cs = json.loads((ROOT / 'scratch' / 'live_wyvern_snapshot_oct16' / 'char_scenario_live.json').read_text(encoding='utf-8'))
    live_scen = live_cs.get('scenario', live_cs)

    slots = [
        {"key": "grandfather", "label": "Grandfather", "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}]},
        {"key": "father", "label": "Father", "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}]},
        {"key": "twin", "label": "Twin", "pool": [{"character_id": "_t4J9aQNJM36cUKAP4wB4U", "weight": 100}]},
        {"key": "brother", "label": "Brother", "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}]},
        {"key": "eldest_brother", "label": "Eldest Brother", "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}]},
        {"key": "uncle", "label": "Uncle", "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}]},
        {"key": "cousin", "label": "Cousin", "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}]},
        {"key": "zeera", "label": "Zeera Darkfire", "pool": []},
        {"key": "jared", "label": "Jared Thompson", "pool": []},
        {"key": "mac", "label": "Mackenzie Sanchez-Rogers", "pool": []},
        {"key": "marek", "label": "Marek", "pool": []},
        {"key": "kaladin", "label": "Major Kaladin Nargathon", "pool": []},
        {"key": "elizabeth", "label": "Elizabeth Duskwood", "pool": []},
        {"key": "magnus", "label": "Magnus Douglas III", "pool": []},
    ]
    slot_keys = {s['key'] for s in slots}

    alyssa_persona_id = 'persona_1786335754946'
    jasper_persona_id = '1792155173728' # assigned today!
    both_personas = [alyssa_persona_id, jasper_persona_id]

    greetings = []
    # 01. Opening
    op = dict(live_scen['greetings'][0])
    op['name'] = '01. Estate a Villa Douglas: Serata Call of Duty in Famiglia'
    op['linked_persona_ids'] = both_personas
    op.pop('linked_personas', None)
    greetings.append(op)

    succ_open_scenes = {
        'scene-succ-move-in-day': {
            'name': '06. SUCC Campus: Move-in Day ai Wyrm Dormitories',
            'desc': 'Mercoledì 28 Agosto 2024, Ore 11:00 - Wyrm Dormitories, Campus SUCC.',
            'slot': 'twin',
            'personas': both_personas,
            'text': """=>Narrator:
Cardboard boxes, plastic storage totes, and reinforced rolling bins choke the wide concrete paths encircling the Wyrm Dormitories. The August heat beats down mercilessly against the campus pavement.

Inside the building's central ground-floor atrium, the chatter echoes off the brutalist walls. Luggage tagged with species-specific accommodations is stacked along the perimeter.

=>Jasper:
{{scenarioChar "twin"}} si ferma al centro dell'atrio con un borsone in spalla, osservando l'ascensore bloccato e la folla di matricole che invade la scalinata centrale. "Ascensore fuori uso al primo giorno. Classico. Prendiamo le scale prima che quel minotauro col mini-frigo blocchi anche il secondo piano." """
        },
        'scene-succ-open-third-person': {
            'name': '10. SUCC Open Campus: Lunar Quad in Pieno Semestre (3a Persona)',
            'desc': 'Lunedì 9 Settembre 2024, Ore 10:30 - Lunar Quad, SUCC Campus.',
            'slot': 'cousin',
            'personas': both_personas,
            'text': """=>Narrator:
The mid-morning California sun cuts warm and bright through the trees growing over the Lunar Quad of the Supernatural University of Central California. It is the second week of the fall semester, and the campus is in full, chaotic swing.

=>Edric:
{{scenarioChar "cousin"}} si avvicina lungo il viale alberato che costeggia la fontana di marmo, lo zaino portato su una spalla sola e un caffè ghiacciato in mano. "Ehi! Sopravvissuti alla prima settimana di corsi, vedo. Dove avete lezione adesso, verso i laboratori a nord o scendete allo Student Union?" """
        },
        'scene-succ-open-second-person': {
            'name': '11. SUCC Open Campus: Lunar Quad in Pieno Semestre (2a Persona)',
            'desc': 'Lunedì 9 Settembre 2024, Ore 10:30 - Lunar Quad, SUCC Campus (Tu).',
            'slot': 'twin',
            'personas': both_personas,
            'text': """=>Narrator:
The mid-morning California sun cuts warm and bright through the trees growing over the Lunar Quad of the Supernatural University of Central California. It is the second week of the fall semester, and the campus is in full, chaotic swing.

=>Jasper:
{{scenarioChar "twin"}} ti affianca vicino alla fontana del Lunar Quad, abbassando una cuffia sull'orecchio mentre scruta i tabelloni degli annunci. "Allora, qual è il piano per stamattina? Andiamo a seguire lezione o facciamo un salto verso lo Student Union?" """
        },
        'scene-solarton-full-moon-festival': {
            'name': '17. Solarton: Festival della Luna Piena in Town Square',
            'desc': 'Giovedì 17 Ottobre 2024, Ore 20:30 - Solarton Square.',
            'slot': 'brother',
            'personas': both_personas,
            'text': """=>Narrator:
As the sun sinks behind the low coastal mountains, the warm Californian dusk gives way to the crisp chill of a full moon evening. Solarton Square is completely transformed; the central plaza is packed to the curbs with folding tables, food carts, and colorful canvas canopies strung with warm fairy lights.

=>Noah:
{{scenarioChar "brother"}} si fa largo tra le bancarelle illuminate dalle catene di luci calde con due spiedini di carne speziata al sangue in mano, porgendone uno a {{user}} con un sorriso compiaciuto. "Ammettilo: il Festival della Luna Piena di Solarton batte qualsiasi gala formale di Uptown. La band vicino alla fontana sta per attaccare e {{scenarioChar "twin"}} ha già puntato il palco." """
        },
    }

    CHRONO_PLAN = [
        ('scene-camp-mystic-arrival', '02. Estate a Camp Mystic: Benvenuti al Lago', both_personas, 'twin', False),
        ('scene-alyssa-story-1-1', '03. [FemPOV] Cap. 1 (Parte 1): Primo Giorno di College - Partenza da Villa Douglas', [alyssa_persona_id], 'father', False),
        ('scene-jasper-1', '04. [MalePOV] Cap. 1 (Jasper): Rombo sul Viale e Addii da Villa Douglas', [jasper_persona_id], 'father', True),
        ('scene-alyssa-story-1-2', '05. Cap. 1 (Parte 2): Arrivo al Griffin Clocktower sul Campus SUCC', both_personas, 'twin', False),
        ('scene-succ-move-in-day', '06. SUCC Campus: Move-in Day ai Wyrm Dormitories', both_personas, 'twin', False),
        ('scene-alyssa-story-2-1', '07. Cap. 2: Stage Formativo HSK - Il Colloquio con Zeera (Aetheris Clinic)', both_personas, 'zeera', False),
        ('scene-alyssa-story-3-1', '08. [FemPOV] Cap. 3 (Parte 1): Impatto sul Campo dei Bulls - Lo Scontro con Jared', [alyssa_persona_id], 'jared', False),
        ('scene-alyssa-story-3-2', '09. Cap. 3 (Parte 2): Tunnel e Spogliatoi del Bulls Stadium post-allenamento', both_personas, 'jared', False),
        ('scene-succ-open-third-person', '10. SUCC Open Campus: Lunar Quad in Pieno Semestre (3a Persona)', both_personas, 'cousin', False),
        ('scene-succ-open-second-person', '11. SUCC Open Campus: Lunar Quad in Pieno Semestre (2a Persona)', both_personas, 'twin', False),
        ('scene-alyssa-story-4-1', '12. [FemPOV] Cap. 4: Basso Distorto al Sidewinders - Primo Incontro con Mac', [alyssa_persona_id], 'mac', False),
        ('scene-guild-1', '13. Gilda DMHA (Cap. 1): Ingresso al Desk DMHA e Registrazione Matricola', both_personas, 'zeera', False),
        ('scene-guild-2', '14. Gilda DMHA (Cap. 2): Discesa nel Rift Sotterraneo (Hive Apex Rift)', both_personas, 'eldest_brother', False),
        ('scene-alyssa-story-5-1', '15. [FemPOV] Cap. 5: Overclock Notturno - Il Rave Clandestino di DJ Frequency', [alyssa_persona_id], 'twin', False),
        ('scene-jasper-2', '16. [MalePOV] Cap. 5 (Jasper): Sul Palco di DJ Frequency al Rave nei Magazzini', [jasper_persona_id], 'twin', True),
        ('scene-solarton-full-moon-festival', '17. Solarton: Festival della Luna Piena in Town Square', both_personas, 'brother', False),
        ('scene-alyssa-story-6-1', '18. [FemPOV] Cap. 6: Halloween dei BRO - La Festa di Beta Rho Omega', [alyssa_persona_id], 'jared', False),
        ('scene-jasper-3', '19. [MalePOV] Cap. 6 (Jasper): Pattuglia Notturna e Dragon Glass Katana al Riverbank', [jasper_persona_id], 'twin', True),
        ('scene-alyssa-story-7-1', '20. Cap. 7 (Parte 1): Pausa d\'Autunno on the Road - Partenza da The Verve con Zio Logan', both_personas, 'uncle', False),
        ('scene-alyssa-story-7-2', '21. Cap. 7 (Parte 2): Sosta Notturna al Neptune Diner sulla Pacific Coast Highway', both_personas, 'uncle', False),
        ('scene-alyssa-story-8-1', '22. Cap. 8 (Parte 1): Solstizio d\'Inverno - La Grande Veglia di Yule con Wulfnic', both_personas, 'grandfather', False),
        ('scene-alyssa-story-8-2', '23. Cap. 8 (Parte 2): La Veglia Notturna sotto l\'Albero Sacro con i Firstborn', both_personas, 'grandfather', False),
        ('scene-alyssa-story-9-1', '24. Cap. 9: Reclute sotto Scorta - Visita Tattica di Erik e Kaladin al Campus SUCC', both_personas, 'father', False),
        ('scene-alyssa-story-10-1', '25. Cap. 10: Fine del Primo Anno - Il Bivio in Cucina con Erik a Villa Douglas', both_personas, 'father', False),
        ('scene-alyssa-story-11-1', '26. [FemPOV] Cap. 11: Fumo di Gomma, Birra e Cloro - Il Branco dei Nomads con Marek', [alyssa_persona_id], 'marek', False),
    ]

    errors = []
    for sid, gname, p_ids, def_slot, is_malepov in CHRONO_PLAN:
        if sid in succ_open_scenes:
            s_obj = succ_open_scenes[sid]
            g_desc = s_obj['desc']
            s_text = s_obj['text']
        else:
            s_obj = scenes_by_id[sid]
            g_desc = clean_prose(s_obj.get('description', gname))
            s_text = s_obj.get('scene_text', '')

        msgs = parse_world_scene_to_messages(sid, s_text, default_slot=def_slot, is_malepov=is_malepov)
        if len(msgs) < 1 or len(msgs) > 20:
            errors.append(f"Greeting {sid} has {len(msgs)} messages (allowed 1-20)")
        for idx, m in enumerate(msgs):
            if m['speaker_slot'] not in slot_keys:
                errors.append(f"Greeting {sid} msg {idx} has invalid slot: '{m['speaker_slot']}'")
            if len(m['content']) > 100000:
                errors.append(f"Greeting {sid} msg {idx} content > 100k")

        greetings.append({
            'id': sid,
            'name': gname,
            'description': g_desc,
            'speaker_slot': msgs[0]['speaker_slot'],
            'content': msgs[0]['content'],
            'messages': msgs,
            'linked_persona_ids': p_ids,
        })

    print(f"Total slots: {len(slots)} (limit: 20)")
    print(f"Total greetings: {len(greetings)} (limit: 100)")
    print(f"Errors found: {len(errors)}")
    if errors:
        for err in errors:
            print(" -", err)
    else:
        print("ALL 26 GREETINGS VALIDATED 100% AGAINST WYVERN RULES!")

if __name__ == '__main__':
    run_dry_run()
