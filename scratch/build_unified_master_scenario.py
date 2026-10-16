import json
import pathlib
import re
import uuid
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'
API_BASE = 'https://app.wyvern.chat/api'

def api_req(method: str, path: str, token: str, payload=None):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload).encode('utf-8') if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode('utf-8')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTPError {e.code} on {method} {path}: {err_body}")
        return e.code, {'error': err_body}

def det_uuid(seed_str: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"svartulfr.{seed_str}"))

def clean_prose(text: str) -> str:
    text = text.replace('—', ', ').replace('–', ', ')
    text = re.sub(r"\be'", "è", text)
    text = re.sub(r"\bE'", "È", text)
    text = re.sub(r"\ba'", "à", text)
    text = re.sub(r"\bo'", "ò", text)
    text = re.sub(r"\bu'", "ù", text)
    text = re.sub(r"\bi'", "ì", text)
    text = re.sub(r"\bpiu\b", "più", text)
    text = re.sub(r"\bPiu\b", "Più", text)
    text = re.sub(r"\bpapa\b", "papà", text)
    text = re.sub(r"\bPapa\b", "Papà", text)
    text = re.sub(r"\bcaffe\b", "caffè", text)
    return text.strip()

SPEAKER_TO_SLOT = {
    'Wulfnic': 'grandfather',
    'Erik': 'father',
    'Jasper': 'twin',
    'Alyssa': 'twin',
    'Noah': 'brother',
    'Malachia': 'eldest_brother',
    'Logan': 'uncle',
    'Edric': 'cousin',
    'Zeera': 'zeera',
    'Jared': 'jared',
    'Mac': 'mac',
    'Marek': 'marek',
    'Kaladin': 'kaladin',
    'Elizabeth': 'elizabeth',
    'Magnus': 'magnus',
    'Receptionist': 'zeera',
    'Squad Leader': 'eldest_brother',
}

def parse_world_scene_to_messages(scene_id: str, scene_text: str, default_slot: str = 'twin', is_malepov: bool = False):
    """
    Converts a multi-turn `=>Speaker:` World scene into an ordered list of
    Character Scenario messages `[{"id": ..., "speaker_slot": ..., "content": ...}]`,
    merging `=>Narrator:` blocks into the adjacent character message and framing
    any transition beats without speaking for `{{user}}`.
    """
    parts = re.split(r'^=>([^:\n]+):\s*$', scene_text.strip(), flags=re.MULTILINE)
    raw_turns = []
    if parts[0].strip():
        raw_turns.append(('Narrator', parts[0].strip()))
    for i in range(1, len(parts), 2):
        sp = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ''
        if body:
            raw_turns.append((sp, body))

    messages = []
    pending_narration = []

    for sp, body in raw_turns:
        body = clean_prose(body)
        if sp == 'Narrator':
            pending_narration.append(body)
            continue
        if sp == '{{user}}':
            # Frame the beat as external atmosphere/context without acting or speaking for {{user}}
            continue
        if sp == 'Sierra':
            pending_narration.append(body)
            continue

        slot = SPEAKER_TO_SLOT.get(sp, default_slot)
        if is_malepov and sp == 'Jasper':
            # In MalePOV, {{user}} is Jasper; let twin (Alyssa) or eldest_brother/father deliver the companion beat
            slot = 'twin'
            body = body.replace('Jasper Douglas Bloodmoon, in arte DJ Frequency,', '{{user}}, in arte DJ Frequency,')
            body = body.replace('Jasper ha sguainato', '{{user}} hain mano')
            body = body.replace('Jasper', '{{scenarioChar "twin"}}')

        if pending_narration:
            combined = '\n\n'.join(pending_narration + [body])
            pending_narration = []
        else:
            combined = body

        # Merge consecutive messages from the same slot if needed
        if messages and messages[-1]['speaker_slot'] == slot:
            messages[-1]['content'] = messages[-1]['content'] + '\n\n' + combined
        else:
            msg_id = det_uuid(f"{scene_id}.msg.{len(messages)+1}")
            messages.append({
                'id': msg_id,
                'speaker_slot': slot,
                'content': combined,
            })

    if pending_narration:
        tail_text = '\n\n'.join(pending_narration)
        if messages:
            messages[-1]['content'] = messages[-1]['content'] + '\n\n' + tail_text
        else:
            messages.append({
                'id': det_uuid(f"{scene_id}.msg.1"),
                'speaker_slot': default_slot,
                'content': tail_text,
            })

    return messages

def main():
    synced = json.loads((ROOT / 'scratch' / 'synced_wyvern_ids.json').read_text(encoding='utf-8'))
    token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

    # Fetch fresh GET of char_scenario_1DC43ggb6mB8YLJDJKrU4 to get current revision and opening greeting
    st, live_scen = api_req('GET', f'/character-scenarios/{SCENARIO_ID}', token)
    print(f"GET /character-scenarios/{SCENARIO_ID} -> status={st}, revision={live_scen.get('revision')}")

    alyssa_persona_id = 'persona_1786335754946'
    jasper_persona_id = synced['personas']['jasper']['persona_id']
    both_personas = [alyssa_persona_id, jasper_persona_id]

    created_chars = synced['characters_created']
    alyssa_card_id = created_chars['alyssa']['id']
    zeera_card_id = created_chars['zeera']['id']
    jared_card_id = created_chars['jared']['id']
    mac_card_id = created_chars['mac']['id']
    marek_card_id = created_chars['marek']['id']
    kaladin_card_id = created_chars['kaladin']['id']
    elizabeth_card_id = created_chars['elizabeth']['id']
    magnus_card_id = created_chars['magnus']['id']

    # Build 14 Slots
    slots = [
        {
            "key": "grandfather",
            "label": "Grandfather",
            "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}]
        },
        {
            "key": "father",
            "label": "Father",
            "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}]
        },
        {
            "key": "twin",
            "label": "Twin",
            "pool": [
                {"character_id": "_t4J9aQNJM36cUKAP4wB4U", "weight": 100},
                {"character_id": alyssa_card_id, "weight": 100}
            ]
        },
        {
            "key": "brother",
            "label": "Brother",
            "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}]
        },
        {
            "key": "eldest_brother",
            "label": "Eldest Brother",
            "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}]
        },
        {
            "key": "uncle",
            "label": "Uncle",
            "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}]
        },
        {
            "key": "cousin",
            "label": "Cousin",
            "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}]
        },
        {
            "key": "zeera",
            "label": "Zeera Darkfire",
            "pool": [{"character_id": zeera_card_id, "weight": 100}]
        },
        {
            "key": "jared",
            "label": "Jared Thompson",
            "pool": [{"character_id": jared_card_id, "weight": 100}]
        },
        {
            "key": "mac",
            "label": "Mackenzie Sanchez-Rogers",
            "pool": [{"character_id": mac_card_id, "weight": 100}]
        },
        {
            "key": "marek",
            "label": "Marek",
            "pool": [{"character_id": marek_card_id, "weight": 100}]
        },
        {
            "key": "kaladin",
            "label": "Major Kaladin Nargathon",
            "pool": [{"character_id": kaladin_card_id, "weight": 100}]
        },
        {
            "key": "elizabeth",
            "label": "Elizabeth Duskwood",
            "pool": [{"character_id": elizabeth_card_id, "weight": 100}]
        },
        {
            "key": "magnus",
            "label": "Magnus Douglas III",
            "pool": [{"character_id": magnus_card_id, "weight": 100}]
        },
    ]

    # Load all World Scenarios from exports/Svartulfr_Export.json
    exp = json.loads((ROOT / 'exports' / 'Svartulfr_Export.json').read_text(encoding='utf-8'))
    ws_by_id = {sc['id']: sc for sc in exp.get('world_scenarios', [])}
    scenes_by_id = {}
    for sc in exp.get('world_scenarios', []):
        for ps in sc.get('premade_scenes', []):
            scenes_by_id[ps['id']] = ps

    # Also add the 4 SUCC Open Campus scenes from create_succ_scenarios.js
    succ_open_scenes = {
        'scene-succ-move-in-day': {
            'id': 'scene-succ-move-in-day',
            'name': '06. SUCC Campus: Move-in Day ai Wyrm Dormitories',
            'description': 'Mercoledì 28 Agosto 2024, Ore 11:00 - Wyrm Dormitories, Campus SUCC. Scatoloni, mini-frigo portati a spalla da minotauri, matricole di ogni specie e alloggi adattati biologicamente nel pieno del trasloco universitario.',
            'default_slot': 'twin',
            'personas': both_personas,
            'text': """=>Narrator:
Cardboard boxes, plastic storage totes, and reinforced rolling bins choke the wide concrete paths encircling the Wyrm Dormitories. The August heat beats down mercilessly against the campus pavement, though occasional bursts of chilled air blow out through the dormitory's automated double doors whenever someone kicks them open, usually while swearing and hoisting a heavy box or three.

A pair of sweat-drenched minotaur movers hoist a mini-fridge up the outer concrete steps, while a harpy student perched atop a second-story balcony railing carefully lowers luggage down to a friend. At the check-in canopy on the front lawn, a harassed-looking resident advisor is repeating the building's fire code into a megaphone, reminding everyone for the fifth time that enchanted cast-iron skillets were permitted, but open flames and unregistered silver kitchenware were grounds for an immediate disciplinary hearing.

Inside the building's central ground-floor atrium, the chatter echoes off the brutalist walls. Luggage tagged with species-specific accommodations is stacked along the perimeter: UV-blackout trunks for nocturnal students, specialized heat-pad bundles for reptilian dormers, and plastic-wrapped mattress covers treated to resist stray claws.

=>Jasper:
{{scenarioChar "twin"}} si ferma al centro dell'atrio con un borsone in spalla, osservando l'ascensore bloccato e la folla di matricole che invade la scalinata centrale. "Ascensore fuori uso al primo giorno. Classico. Prendiamo le scale prima che quel minotauro col mini-frigo blocchi anche il secondo piano." """
        },
        'scene-succ-open-third-person': {
            'id': 'scene-succ-open-third-person',
            'name': '10. SUCC Open Campus: Lunar Quad in Pieno Semestre (3a Persona)',
            'description': 'Lunedì 9 Settembre 2024, Ore 10:30 - Lunar Quad, SUCC Campus. Seconda settimana del semestre autunnale al centro del campus universitario soprannaturale di Solarton.',
            'default_slot': 'cousin',
            'personas': both_personas,
            'text': """=>Narrator:
The mid-morning California sun cuts warm and bright through the trees growing over the Lunar Quad of the Supernatural University of Central California. It is the second week of the fall semester, and the campus is in full, chaotic swing.

Near the sun-drenched fountain, a couple of lizard demihumans are sprawled out on heated stone benches while nearby, a pretty plant-fae strums on a ukulele from beneath an oversized parasol. Over on the gravel paths, a pair of burly werewolf athletes in yellow and blue varsity jackets jog past, tails flicking in sync, laughing loud enough to scatter a flock of bird-kin students conversing on the lower branches of an oak tree.

Bulletins line the kiosk boards: flyers advertising tryouts for the Bears hockey squad, notices for the upcoming monthly Moon Market downtown, and flyers for the campus Vampire and Undead Association.

=>Edric:
{{scenarioChar "cousin"}} si avvicina lungo il viale alberato che costeggia la fontana di marmo, lo zaino portato su una spalla sola e un caffè ghiacciato in mano. "Ehi! Sopravvissuti alla prima settimana di corsi, vedo. Dove avete lezione adesso, verso i laboratori a nord o scendete allo Student Union?" """
        },
        'scene-succ-open-second-person': {
            'id': 'scene-succ-open-second-person',
            'name': '11. SUCC Open Campus: Lunar Quad in Pieno Semestre (2a Persona)',
            'description': 'Lunedì 9 Settembre 2024, Ore 10:30 - Lunar Quad, SUCC Campus. Apertura sandbox libera in seconda persona al centro del Lunar Quad.',
            'default_slot': 'twin',
            'personas': both_personas,
            'text': """=>Narrator:
The mid-morning California sun cuts warm and bright through the trees growing over the Lunar Quad of the Supernatural University of Central California. It is the second week of the fall semester, and the campus is in full, chaotic swing.

Near the sun-drenched fountain, you see that a couple of lizard demihumans are sprawled out on heated stone benches while nearby, a pretty plant-fae strums on a ukulele from beneath an oversized parasol. Over on the gravel paths, a pair of burly werewolf athletes in yellow and blue varsity jackets jog past, tails flicking in sync.

Bulletins line the kiosk boards: flyers advertising tryouts for the Bears hockey squad, notices for the upcoming monthly Moon Market downtown, and flyers for the campus Vampire and Undead Association. You are standing at the crossroads past the quad's marble lupine fountain, the path leading west toward the residence halls, north to the lecture halls, and south toward the student union and athletic fields.

=>Jasper:
{{scenarioChar "twin"}} ti affianca vicino alla fontana del Lunar Quad, abbassando una cuffia sull'orecchio mentre scruta i tabelloni degli annunci. "Allora, qual è il piano per stamattina? Andiamo a seguire lezione o facciamo un salto verso lo Student Union?" """
        },
        'scene-solarton-full-moon-festival': {
            'id': 'scene-solarton-full-moon-festival',
            'name': '17. Solarton: Festival della Luna Piena in Town Square',
            'description': 'Giovedì 17 Ottobre 2024, Ore 20:30 - Solarton Square. La piazza centrale di Solarton illuminata a festa per il plenilunio tra concerti indie-punk, bancarelle per licantropi e studenti della SUCC.',
            'default_slot': 'brother',
            'personas': both_personas,
            'text': """=>Narrator:
As the sun sinks behind the low coastal mountains, the warm Californian dusk gives way to the crisp chill of a full moon evening. Solarton Square is completely transformed; the central plaza, usually a sleepy pedestrian hub full of tourists and families, is packed to the curbs with folding tables, food carts, and colorful canvas canopies strung with warm fairy lights.

The air is dense with the combined scents of traditional and mystical festival fare: sizzling butter and roasted corn mingling with the heavy iron tang of rare, spiced flank steaks from the were-friendly butcher stalls. Further toward the historic fountain, a local indie band finishes their sound check, the bassist idly letting a tufted tail thump against their amplifier to test the rhythm.

=>Noah:
{{scenarioChar "brother"}} si fa largo tra le bancarelle illuminate dalle catene di luci calde con due spiedini di carne speziata al sangue in mano, porgendone uno a {{user}} con un sorriso compiaciuto. "Ammettilo: il Festival della Luna Piena di Solarton batte qualsiasi gala formale di Uptown. La band vicino alla fontana sta per attaccare e {{scenarioChar "twin"}} ha già puntato il palco." """
        },
    }

    # Build ordered greetings list
    greetings = []

    # Greeting 1: Existing Opening (Call of Duty at Villa Douglas)
    opening_g = dict(live_scen['greetings'][0])
    opening_g['name'] = '01. Estate a Villa Douglas: Serata Call of Duty in Famiglia'
    opening_g['linked_persona_ids'] = both_personas
    opening_g.pop('linked_personas', None)
    greetings.append(opening_g)

    # Chronological plan of the remaining 25 scenes
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

    for sid, gname, p_ids, def_slot, is_malepov in CHRONO_PLAN:
        if sid in succ_open_scenes:
            s_obj = succ_open_scenes[sid]
            g_desc = s_obj['description']
            s_text = s_obj['text']
        else:
            s_obj = scenes_by_id[sid]
            g_desc = clean_prose(s_obj.get('description', gname))
            s_text = s_obj.get('scene_text', '')

        msgs = parse_world_scene_to_messages(sid, s_text, default_slot=def_slot, is_malepov=is_malepov)
        greetings.append({
            'id': sid,
            'name': gname,
            'description': g_desc,
            'speaker_slot': msgs[0]['speaker_slot'],
            'content': msgs[0]['content'],
            'messages': msgs,
            'linked_persona_ids': p_ids,
        })

    master_scenario_text = (
        "Setting: Contemporary Supernatural California (2024–2025) — Blackwood City (Seven Hills, Villa Douglas, Uptown, Dockside, Ironworks) "
        "and Solarton (Southern Union Monster College / SUCC Campus, Greek Row, DMHA Guild Hall, Camp Mystic).\n\n"
        "Protagonists & Pack Family Cast:\n"
        "- {{user}} and {{scenarioChar \"twin\"}} are the 19-year-old Douglas-Bloodmoon twins (Alyssa Hvit, Dominant OmegaPre-Med Healer, and Jasper Svartr, Beta Technomancer & DJ Frequency), starting their freshman year at SUCC.\n"
        "- {{scenarioChar \"father\"}} (Erik Ulfr Douglas): Prime Alpha Pack Leader of House Douglas and CEO of the Douglas Commercial Coalition (DCC).\n"
        "- {{scenarioChar \"eldest_brother\"}} (Malachia Björn): 26-year-old Dominant Alpha, undefeated heavyweight fighter, and silent protective shield of the twins.\n"
        "- {{scenarioChar \"brother\"}} (Noah Loki): 25-year-old Delta diplomat, corporate strategist, and charming socialite.\n"
        "- {{scenarioChar \"uncle\"}} (Logan Járn Douglas): Erik's Beta brother, mechanic at The Verve, and grounded confidant.\n"
        "- {{scenarioChar \"cousin\"}} (Edric Douglas): Logan's 20-year-old son and loyal campus companion.\n"
        "- {{scenarioChar \"grandfather\"}} (Wulfnic Báleygr Bloodmoon): 1,197-year-old Primordial Firstborn Alpha of the Sacred Forest.\n"
        "- Key Allies, Rivals & Contacts: {{scenarioChar \"zeera\"}} (CEO of HSK Consulting), {{scenarioChar \"jared\"}} (SUCC Bulls Quarterback & BRO Frat), {{scenarioChar \"mac\"}} (Grave Mistake synth player), {{scenarioChar \"marek\"}} (Blue Oni Enforcer of the Ironhorn Nomads MC), {{scenarioChar \"kaladin\"}} (Commander of DCC Security), {{scenarioChar \"elizabeth\"}} (Lady Duskwood), and {{scenarioChar \"magnus\"}} (Elder Lord Douglas).\n\n"
        "Core Rules:\n"
        "- Demi-humans and Werewolves in Partial Shift possess ONLY ONE PAIR OF EARS (their animal ears on top of the head, no human ears).\n"
        "- Respect familial boundaries between Douglas/Bloodmoon relatives (deep pack warmth, teasing, and protective loyalty; no romantic or sexual framing between blood relatives).\n"
        "- Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
    )

    display_desc = (
        "Scenario Unificato Ufficiale dello **SvartúlfrVerse** (2024–2025): dalle serate in famiglia a **Villa Douglas** e le vacanze estive a **Camp Mystic**, "
        "fino all'intero primo anno accademico alla **SUCC (Southern Union Monster College)** di Solarton, le spedizioni nei Rift della **Gilda DMHA**, "
        "i concerti al **Sidewinders**, i rave clandestini di **DJ Frequency**, la veglia del Solstizio di **Yule** con **Wulfnic** e le notti con gli **Ironhorn Nomads**.\n\n"
        "- **Dual-Protagonist Support (`Alyssa` & `Jasper`)**: scegli la Persona proposta (**Alyssa** per i greeting condivisi o `[FemPOV]`, **Jasper** per i greeting condivisi o `[MalePOV]`) e assegna il gemello corrispondente nello slot **Twin**."
    )

    put_payload = {
        "name": "SvartúlfrVerse — Cronache dei Gemelli Douglas-Bloodmoon (Villa Douglas, SUCC & Gilda)",
        "display_description": display_desc,
        "avatar": live_scen.get("avatar", ""),
        "tags": ["Werewolf", "group", "SUCC", "College", "Urban Fantasy", "Demihuman", "AnyPOV", "FemPOV", "MalePOV"],
        "visibility": "private",
        "rating": "explicit",
        "revision": live_scen.get("revision"),
        "linked_world_id": "",
        "scenario": master_scenario_text,
        "startup_script": "",
        "slots": slots,
        "greetings": greetings,
        "lorebook_ids": live_scen.get("lorebook_ids", []),
        "gallery": live_scen.get("gallery", []),
    }

    (FINAL_DIR / 'Svartulfr_Master_Scenario.json').write_text(json.dumps(put_payload, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Saved FINAL/Svartulfr_Master_Scenario.json | slots={len(slots)} | greetings={len(greetings)}")

    st_put, res_put = api_req('PUT', f'/character-scenarios/{SCENARIO_ID}', token, put_payload)
    print(f"PUT /character-scenarios/{SCENARIO_ID} -> status={st_put} | new_revision={res_put.get('revision')} | slot_count={res_put.get('slot_count')} | greeting_count={res_put.get('greeting_count')}")

if __name__ == '__main__':
    main()
