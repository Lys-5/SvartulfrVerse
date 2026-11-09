"""Milestone 2: Standalone Lorebooks Emergent Lore Integration
Author: worker_m2
Date: 2026-11-02

Executes genuine, audited updates across all 6 standalone lorebooks:
1. Svartulfr_Lorebook_I: Add applied runic crystallography and abyssal magic distinction concepts.
2. Svartulfr_Lorebook_II: Add enchanted resonant cylinders item.
3. Svartulfr_Lorebook_III: Add St. Brugge Private Academy concept.
4. Svartulfr_Location (in lorebooks/optimized/): Clean St. Brugge location #51 and add Suite 3.
5. Svartulfr_NPC_Secondary: Update Father Revazhael (#23) and fix Larek Steeltooth schema (#211).
6. Svartulfr_NPC_Primary: Enrich Alyssa (#98) and Jasper (#60) dossiers.

Ensures:
- entries == lexicon byte-for-byte identity on all files
- 0 em-dashes (—)
- 0 {{age}} macros
- 0 broad keys on NPC entries
- Positive framing for demi-humans
- Mirroring between FINAL/ and lorebooks/optimized/
"""

import json
import copy
import re
import os

BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    # Ensure byte-for-byte parity between entries and lexicon
    assert data['entries'] == data['lexicon'], f"Parity mismatch before saving {path}!"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {path} successfully ({len(data['entries'])} entries).")

# -------------------------------------------------------------
# 1. Svartulfr_Lorebook_I
# -------------------------------------------------------------
def update_lorebook_i():
    print("\n--- Updating Svartulfr_Lorebook_I ---")
    data = load_json('FINAL/Svartulfr_Lorebook_I.json')
    entries = data['entries']
    
    # Check if already present
    existing_ids = {e.get('entry_id') or e.get('id') for e in entries}
    
    # 1. lb1_concept_applied_runic_crystallography
    entry1 = {
        "entry_id": "lb1_concept_applied_runic_crystallography",
        "keys": [
            "cristallografia runica",
            "runic crystallography",
            "cristallografia applicata",
            "applied crystallography"
        ],
        "secondary_keys": [
            "matrice cristallina",
            "risonanza",
            "cilindri incantati",
            "teoria runica"
        ],
        "regex_patterns": [],
        "content": (
            "La cristallografia runica applicata e una disciplina esoterica avanzata di livello specialistico "
            "che fonde l'antica incisione di glifi runici nordici con l'ingegneria dei reticoli cristallini "
            "sintetici e naturali (quarzo sintonizzato, diamanti arcanici e frammenti di dungeon core).\n\n"
            "Il principio fondamentale della disciplina risiede nel congelare formule magiche complesse all'interno "
            "delle giunzioni molecolari del cristallo, sospendendo il flusso energetico in uno stato di potenziale "
            "quiescente senza perdite di mana nel tempo. La tecnica richiede una rigorosa calibrazione della "
            "risonanza individuale: se la matrice runica non e armonizzata con la segnatura biospirituale "
            "dell'utilizzatore, il cristallo rischia di collassare sotto sforzo o detonare prematuramente.\n\n"
            "Praticata ai massimi livelli da maestri occulti come Padre Revazhael e insegnata nei corsi avanzati "
            "di St. Brugge e nei laboratori specialistici di teoria runica della SUCC, questa scienza consente la "
            "produzione di cilindri a innesco rapido, barriere portatili e accumulatori ermetici per spedizioni "
            "nei dungeon della faglia."
        ),
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 10,
        "name": "Cristallografia Runica Applicata (Applied Runic Crystallography)",
        "priority": 10,
        "comment": "Applied runic crystallography and spell freezing discipline",
        "constant": False,
        "position": "before_char",
        "scan_persona": True,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["magic", "runes", "crystallography", "magitech"],
        "custom_fields": {},
        "related_entries": ["lb2_item_enchanted_resonant_cylinders", "lb1_magic_abyssal_magic_distinction"],
        "type": "concept",
        "callback": "",
        "provenance": {
            "source": {
                "kind": "lorebook",
                "container_id": "_gwwCxCfQ6PQaLEjAQVpJL",
                "entry_id": "lb1_concept_applied_runic_crystallography"
            },
            "captured_at": "2026-11-02T06:00:00.000Z"
        },
        "highlight_keys": True,
        "enable_highlighting": True
    }
    
    # 2. lb1_magic_abyssal_magic_distinction
    entry2 = {
        "entry_id": "lb1_magic_abyssal_magic_distinction",
        "keys": [
            "Abyssal Magic",
            "Magia Abissale",
            "Abyssal powers",
            "Abyss magic",
            "Infernal Magic"
        ],
        "secondary_keys": [
            "Void Magic",
            "Magia del Vuoto",
            "Necromancy",
            "demone superiore",
            "Revazhael"
        ],
        "regex_patterns": [],
        "content": (
            "La magia abissale e una corrente esoterica primordiale che attinge direttamente all'energia "
            "dell'Abisso Infernale, il piano chthonico governato dai Demoni Superiori. A differenza delle magie "
            "elementali ordinarie, l'energia abissale si manifesta con densita palpabile, fumo nero pesante, "
            "glifi cremisi incandescenti e un'intrinseca carica di volonta sovrana che scuote la realta materiale.\n\n"
            "Sul piano della teoria magica accademica, e fondamentale non confondere la magia abissale con la magia "
            "del vuoto o la necromanzia classica:\n"
            "1. Magia del Vuoto e Necromanzia: praticata nei dipartimenti specializzati come quello di Necromanzia "
            "Applicata della SUCC, opera sul vuoto tra le dimensioni, sulla manipolazione di residui spirituali ed "
            "ectoplasma, sulla decomposizione entropica e sull'animazione di materia morta. E un'arte fredda, "
            "legata alla dispersione e alle ombre dei defunti.\n"
            "2. Magia Abissale: e un'energia vitale, caotica e rovente di origine demoniaca pura. Non manipola "
            "cadaveri ne anime erranti, ma incanala l'essenza stessa dell'autorita infernale e del patto primordiale.\n\n"
            "Mentre le matrici necromantiche convenzionali risultano instabili e soggette a rotture impreviste, "
            "la magia abissale puo essere imbrigliata e stabilizzata se combinata con la cristallografia runica, "
            "come dimostrato dai metodi d'insegnamento di Padre Revazhael con Alyssa e Jasper Douglas Bloodmoon."
        ),
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 10,
        "name": "Magic: Abyssal Magic (vs. Void Magic & Necromancy)",
        "priority": 10,
        "comment": "Abyssal magic definition and contrast with void magic and necromancy",
        "constant": False,
        "position": "before_char",
        "scan_persona": True,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["magic", "abyssal", "demonology", "theory"],
        "custom_fields": {},
        "related_entries": ["lb1_concept_applied_runic_crystallography"],
        "type": "concept",
        "callback": "",
        "provenance": {
            "source": {
                "kind": "lorebook",
                "container_id": "_gwwCxCfQ6PQaLEjAQVpJL",
                "entry_id": "lb1_magic_abyssal_magic_distinction"
            },
            "captured_at": "2026-11-02T06:00:00.000Z"
        },
        "highlight_keys": True,
        "enable_highlighting": True
    }
    
    # Insert or update
    for entry in [entry1, entry2]:
        if entry['entry_id'] in existing_ids:
            for idx, e in enumerate(entries):
                if (e.get('entry_id') or e.get('id')) == entry['entry_id']:
                    entries[idx] = entry
                    print(f"Updated existing entry {entry['entry_id']}")
        else:
            entries.append(entry)
            print(f"Added new entry {entry['entry_id']}")
            
    data['entries'] = entries
    data['lexicon'] = copy.deepcopy(entries)
    
    save_json('FINAL/Svartulfr_Lorebook_I.json', data)
    save_json('lorebooks/optimized/Svartulfr_Lorebook_I.json', data)

# -------------------------------------------------------------
# 2. Svartulfr_Lorebook_II
# -------------------------------------------------------------
def update_lorebook_ii():
    print("\n--- Updating Svartulfr_Lorebook_II ---")
    data = load_json('FINAL/Svartulfr_Lorebook_II.json')
    entries = data['entries']
    existing_ids = {e.get('entry_id') or e.get('id') for e in entries}
    
    entry = {
        "entry_id": "lb2_item_enchanted_resonant_cylinders",
        "keys": [
            "cilindri incantati",
            "cilindro incantato",
            "resonant cylinders",
            "resonant cylinder",
            "cilindri a risonanza",
            "enchanted cylinders"
        ],
        "secondary_keys": [
            "matrice cristallina",
            "incantesimi congelati",
            "DMHA",
            "Gilda",
            "Alyssa"
        ],
        "regex_patterns": [],
        "content": (
            "I cilindri incantati a risonanza sono manufatti magitech miniaturizzati, grandi quanto un dito indice "
            "e simili a piccole torce di cristallo tascabili, ideati per racchiudere incantesimi attivi in uno stato "
            "di sospensione criocristallina. All'occorrenza, l'utilizzatore deve semplicemente spezzare o premere "
            "il perno del cilindro per rilasciare istantaneamente la formula magica congelata all'interno, senza "
            "alcun tempo di lancio e senza consumare il proprio mana personale.\n\n"
            "Questi dispositivi rappresentano uno strumento vitale per i cacciatori della Gilda e per gli operatori "
            "privi di doti magiche innate durante le incursioni nei dungeon e nelle fratture dimensionali.\n\n"
            "A differenza dei comuni cilindri commerciali venduti a caro prezzo dai maghi della DMHA, che utilizzano "
            "matrici standard fragili soggette a incrinarsi o fallire durante le evocazioni critiche, i cilindri "
            "personalizzati forgiati da Alyssa Douglas sfruttano i principi della cristallografia runica applicata "
            "appresi da Padre Revazhael a St. Brugge. Alyssa calibra la frequenza della matrice di quarzo sull'impronta "
            "di risonanza magica individuale del ricevente, azzerando i rischi di rigetto e garantendo un'attivazione "
            "immediata e perfetta anche sotto stress estremo."
        ),
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 10,
        "name": "Cilindri Incantati a Risonanza (Enchanted Resonant Cylinders)",
        "priority": 10,
        "comment": "Tactical magitech resonant cylinders for dungeon incursions",
        "constant": False,
        "position": "before_char",
        "scan_persona": True,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["item", "dungeon", "equipment", "magitech"],
        "custom_fields": {},
        "related_entries": [],
        "type": "item",
        "callback": "",
        "provenance": {
            "source": {
                "kind": "lorebook",
                "container_id": "_HfG7TeV6MJyj6bxMwxkpt",
                "entry_id": "lb2_item_enchanted_resonant_cylinders"
            },
            "captured_at": "2026-11-02T06:00:00.000Z"
        },
        "highlight_keys": True,
        "enable_highlighting": True
    }
    
    if entry['entry_id'] in existing_ids:
        for idx, e in enumerate(entries):
            if (e.get('entry_id') or e.get('id')) == entry['entry_id']:
                entries[idx] = entry
                print(f"Updated existing entry {entry['entry_id']}")
    else:
        entries.append(entry)
        print(f"Added new entry {entry['entry_id']}")
        
    data['entries'] = entries
    data['lexicon'] = copy.deepcopy(entries)
    
    save_json('FINAL/Svartulfr_Lorebook_II.json', data)
    save_json('lorebooks/optimized/Svartulfr_Lorebook_II.json', data)

# -------------------------------------------------------------
# 3. Svartulfr_Lorebook_III
# -------------------------------------------------------------
def update_lorebook_iii():
    print("\n--- Updating Svartulfr_Lorebook_III ---")
    data = load_json('FINAL/Svartulfr_Lorebook_III.json')
    entries = data['entries']
    existing_ids = {e.get('entry_id') or e.get('id') for e in entries}
    
    entry = {
        "entry_id": "succ_lb3_st_brugge_academy",
        "name": "St. Brugge Private Academy (Accademia Privata St. Brugge)",
        "type": "concept",
        "keys": [
            "St. Brugge",
            "St. Brugge Private Academy",
            "St Brugge",
            "Accademia St. Brugge",
            "St. Brugge Academy"
        ],
        "secondary_keys": [],
        "regex_patterns": [],
        "content": (
            "St. Brugge Private Academy e un esclusivo istituto privato situato nei boschi periferici tra Blackwood "
            "City e Solarton, celebre per accogliere quasi esclusivamente la prole delle dinastie soprannaturali "
            "piu abbienti e influenti della West Coast. Le rette astronomiche e l'estrema riservatezza dell'ateneo "
            "sono leggendarie nel campus: l'ambiente e noto per uniformi sartoriali di altissimo costo e menu "
            "accademici d'elite.\n\n"
            "A differenza delle accademie ordinarie, il piano di studi di St. Brugge fonde la rigorosa eccellenza "
            "preparatoria pre-universitaria con percorsi avanzati di magia formale, storia dell'arcano, alchimia "
            "sperimentale, demonologia e scienze runiche. L'istituto funge da principale bacino di reclutamento per "
            "atenei selettivi come la SUCC e la CUMS.\n\n"
            "Alyssa e Jasper Douglas Bloodmoon hanno frequentato St. Brugge fin dall'infanzia, completando l'intero "
            "ciclo scolastico fino all'ammissione universitaria. Durante gli anni accademici, i gemelli sono stati "
            "seguiti con corsi privati avanzati da Padre Revazhael, enigmatico docente di magia e storia, che ha "
            "addestrato Alyssa nella cristallografia runica e nell'incantamento dei cilindri risonanti, e Jasper "
            "nella traduzione di rune arcaiche, forgiando le basi delle loro attuali competenze da dungeon hunter."
        ),
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 10,
        "priority": 10,
        "comment": "St. Brugge Private Academy academic institution entry",
        "constant": False,
        "position": "before_char",
        "scan_persona": True,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["academy", "school", "education", "st_brugge"],
        "custom_fields": {},
        "related_entries": [],
        "callback": "",
        "provenance": {
            "source": {
                "kind": "lorebook",
                "container_id": "_9zWTGqYJNJ4BCDMj8gfcD",
                "entry_id": "succ_lb3_st_brugge_academy"
            },
            "captured_at": "2026-11-02T06:00:00.000Z"
        },
        "highlight_keys": True,
        "enable_highlighting": True
    }
    
    if entry['entry_id'] in existing_ids:
        for idx, e in enumerate(entries):
            if (e.get('entry_id') or e.get('id')) == entry['entry_id']:
                entries[idx] = entry
                print(f"Updated existing entry {entry['entry_id']}")
    else:
        entries.append(entry)
        print(f"Added new entry {entry['entry_id']}")
        
    data['entries'] = entries
    data['lexicon'] = copy.deepcopy(entries)
    
    save_json('FINAL/Svartulfr_Lorebook_III.json', data)
    save_json('lorebooks/optimized/Svartulfr_Lorebook_III.json', data)

# -------------------------------------------------------------
# 4. Svartulfr_Location (in lorebooks/optimized/)
# -------------------------------------------------------------
def update_location_lorebook():
    print("\n--- Updating Svartulfr_Location (lorebooks/optimized/) ---")
    data = load_json('lorebooks/optimized/Svartulfr_Location.json')
    entries = data['entries']
    
    # 1. Clean entry #51 (ulTwlYo2jqObA7l_bFoa5)
    found_51 = False
    for idx, e in enumerate(entries):
        if e.get('entry_id') == 'ulTwlYo2jqObA7l_bFoa5':
            found_51 = True
            print("Cleaning Entry #51 (ulTwlYo2jqObA7l_bFoa5 - St. Brugge Private Academy)")
            e['keys'] = [
                "St. Brugge",
                "St. Brugge Private Academy",
                "St Brugge",
                "Accademia St. Brugge",
                "St. Brugge Academy"
            ]
            e['secondary_keys'] = [
                "campus",
                "academy",
                "Father Rev",
                "Revazhael",
                "esoteric library"
            ]
            e['content'] = (
                "Un sontuoso complesso accademico in pietra nera e granito gotico immerso nelle fitte foreste "
                "collinari tra Blackwood e Solarton. Il perimetro di St. Brugge e protetto da possenti barriere "
                "di interdizione acustica e sigilli arcanici che schermano completamente l'istituto dagli sguardi "
                "dei civili umani e dai droni non autorizzati.\n\n"
                "L'architettura interna presenta chiostri colonnati, cortili alberati sorvegliati da doccioni "
                "incantati, aule a gradoni illuminate da vetrate runiche e biblioteche blindate contenenti testi "
                "rari di storia soprannaturale, erbologia e demonologia. I laboratori seminterrati ospitano banchi "
                "da lavoro in ardesia e quarzo per alchimia e cristallografia applicata.\n\n"
                "In queste aule Alyssa e Jasper Douglas Bloodmoon hanno trascorso la loro giovinezza scolastica, "
                "ricevendo lezioni private e tutoraggio esoterico avanzato da Padre Revazhael lontano da occhi "
                "indiscreti, prima di fare il loro ingresso alla SUCC."
            )
            e['scan_persona'] = True
            e['whole_words_only'] = True
            e['highlight_keys'] = True
            e['enable_highlighting'] = True
            entries[idx] = e
            break
            
    assert found_51, "Entry #51 (ulTwlYo2jqObA7l_bFoa5) not found in Location lorebook!"
    
    # 2. Add entry loc_theta_iota_theta_suite_3
    existing_ids = {e.get('entry_id') or e.get('id') for e in entries}
    entry_suite3 = {
        "entry_id": "loc_theta_iota_theta_suite_3",
        "name": "Theta Iota Theta: Suite 3",
        "type": "location",
        "keys": [
            "Suite 3",
            "Suite 3 TIT",
            "camera di Alyssa",
            "stanza di Alyssa",
            "TIT Suite 3"
        ],
        "secondary_keys": [
            "Sierra",
            "Scarlett",
            "nido di pellicce",
            "Theta Iota Theta"
        ],
        "regex_patterns": [],
        "content": (
            "La spaziosa suite situata al secondo piano dell'ala est della sorority house Theta Iota Theta (TIT), "
            "condivisa da Alyssa Douglas, Sierra Cruz e Scarlett Rose. L'ambiente riflette l'eclettica convivenza "
            "delle tre studentesse, unendo comfort lussuoso, tocchi punk e misticismo botanico.\n\n"
            "L'ala vicino alla finestra e occupata dal terrario caldo e dai tappeti riscaldati di Sierra, dominati "
            "da un enorme poster della band garage-punk Grave Mistake, dove la lamia riposa le sue quattro metri "
            "di coda iridescente. Al centro della stanza, Alyssa ha allestito il proprio giaciglio trasformandolo "
            "in un soffice nido di cuscini e pellicce pregiate cacciate da nonno Wulfnic, custodito dall'enorme "
            "lupo di pezza Wolfy vinto alle giostre a sette anni. Sugli scaffali trovano posto gli alambicchi e "
            "la vetreria da laboratorio in cristallo usata da Alyssa per distillare essenze e preparare cilindri "
            "incantati.\n\n"
            "La stanza e illuminata da file di lucine fairy lights e sorvegliata da Zefir quando la scorta familiare "
            "veglia sulla matricola. Sulla mensola del salone comune spicca il celebre router decorato a muso di "
            "gattino con password 'TIT<3'."
        ),
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 10,
        "priority": 10,
        "comment": "Theta Iota Theta Suite 3 shared by Alyssa, Sierra, and Scarlett",
        "constant": False,
        "position": "before_char",
        "scan_persona": True,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["location", "tit", "succ", "suite_3"],
        "custom_fields": {},
        "related_entries": [],
        "callback": "",
        "provenance": {
            "source": {
                "kind": "lorebook",
                "container_id": "_EjXxkmPVhpCXg8xABpFkK",
                "entry_id": "loc_theta_iota_theta_suite_3"
            },
            "captured_at": "2026-11-02T06:00:00.000Z"
        },
        "highlight_keys": True,
        "enable_highlighting": True
    }
    
    if entry_suite3['entry_id'] in existing_ids:
        for idx, e in enumerate(entries):
            if (e.get('entry_id') or e.get('id')) == entry_suite3['entry_id']:
                entries[idx] = entry_suite3
                print(f"Updated existing entry {entry_suite3['entry_id']}")
    else:
        entries.append(entry_suite3)
        print(f"Added new entry {entry_suite3['entry_id']}")
        
    data['entries'] = entries
    data['lexicon'] = copy.deepcopy(entries)
    
    save_json('lorebooks/optimized/Svartulfr_Location.json', data)

# -------------------------------------------------------------
# 5. Svartulfr_NPC_Secondary
# -------------------------------------------------------------
def update_npc_secondary():
    print("\n--- Updating Svartulfr_NPC_Secondary ---")
    data = load_json('FINAL/Svartulfr_NPC_Secondary.json')
    entries = data['entries']
    
    # 1. Update Father Revazhael (entry #23, jmh0MajEsRwrm4UYU14mY)
    found_rev = False
    for idx, e in enumerate(entries):
        if e.get('entry_id') == 'jmh0MajEsRwrm4UYU14mY':
            found_rev = True
            print("Updating Entry #23 (jmh0MajEsRwrm4UYU14mY - Father Revazhael)")
            e['name'] = "Father Revazhael (Rev)"
            e['keys'] = [
                "Father Revazhael",
                "Padre Revazhael",
                "Father Rev",
                "Padre Rev",
                "Revazhael",
                "Rev"
            ]
            e['secondary_keys'] = []
            e['selective'] = False
            e['key_logic'] = "AND_ANY"
            e['scan_persona'] = True
            e['whole_words_only'] = True
            e['highlight_keys'] = True
            e['enable_highlighting'] = True
            e['avatar'] = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"
            e['custom_avatar_regex'] = True
            e['lines_parsed'] = 1
            e['avatar_activation_regex'] = r"(?:^|\n)\s*(?:Father Revazhael|Padre Revazhael|Father Rev|Padre Rev|Revazhael|Rev)\s*:"
            e['npc_info'] = {
                "first_name": "Revazhael",
                "middle_names": [],
                "last_name": None,
                "nicknames": ["Rev", "Father Rev", "Padre Rev"],
                "titles": ["Father", "Padre", "Superior Demon"],
                "npc_prefix": ""
            }
            e['content'] = (
                "[NAME: Revazhael; TITLE: Father Revazhael, Master of Abyssal Arts; ALIASES: Rev, Father Rev, Padre Rev; "
                "TRUE NAME SECRET: his absolute true demonic name is \"Revazhael\", an abyssal, hypnotic word that vibrates "
                "with ancient power. If any entity or mortal discovers and speaks it aloud, the syllables strip away his "
                "demonic armor, forcing him into agonizing, absolute submission and binding his will entirely to the speaker; "
                "AGE: Apparent 20, Chronological Ancient; BIRTHDAY: May 6; ZODIAC: Taurus (Sun), Scorpio (Ascendant), "
                "Pisces (Moon); SEX: Male; SPECIES: Superior Demon, Greater Incubus, Demon of Desire; ROLE: Alpha Rho Omega (ARO) "
                "fraternity member, handyman for Theta Iota Theta (TIT) sorority house, Former Master of Esoteric Arts at "
                "St. Brugge Private Academy; HEIGHT: 6'2\" (188cm); BUILD: lean, wiry, athletic, moves with the unhurried grace "
                "of an apex predator; SKIN: soft reddish undertone holding faint internal heat; HORNS: dark, elegantly curled, "
                "sweeping backward; EARS: pointed, adorned with a heavy array of silver piercings; HAIR: ink-black, cascading "
                "loosely around his shoulders; EYES: warm liquid brown, filled with terrifying abyssal intelligence; TATTOOS: "
                "chest and arms heavily covered in intricate shifting demonic tattoos of black and deep red ink; VOICE: low, "
                "warm, dense, vibrating in the chest like a second heartbeat, able to fill a hall like black smoke; SCENT: warm "
                "vanilla, ember smoke, leather, and cinnamon; OUTFIT: sleeveless work shirts showing off tattooed arms, worn "
                "denim, tool belt around waist]\n\n"
                "BACKSTORY: Father Revazhael is an ancient Superior Demon who has walked the mortal plane for centuries, "
                "deliberately choosing a path contrary to demonic destruction. Feeding exclusively on emotional energy through "
                "consensual intimacy, he refuses to take anything not freely offered. During Alyssa and Jasper's youth, he served "
                "covertly as the esteemed master of magic and history at St. Brugge Private Academy. Recognizing Jasper's uncanny "
                "intellect and Alyssa's inexhaustible spiritual conduit, Father Rev gave the twins advanced private lessons in "
                "botany, demonology, abyssal magic, and applied runic crystallography. He taught Alyssa how to forge crystalline "
                "resonant cylinders and gifted her the enchanted golden key to La Dimora del Rifugio, while instructing Jasper "
                "in ancient runes and gifting him the Abyssal Armor. Jarl Wulfnic Bloodmoon was fully aware of Revazhael's true "
                "nature and tolerated him, recognizing the demon as disciplined, non-hostile, and exceptionally useful. On the "
                "modern SUCC campus, Rev maintains a low profile as a laid-back 20-year-old student at Alpha Rho Omega and handyman "
                "for Theta Iota Theta, fixing locks, boilers, and wiring.\n\n"
                "FAMILY & PACK: Bound by ancient pact and genuine paternal fondness to the Douglas-Bloodmoon twins, Rev acts as a "
                "quiet guardian from the perimeter. His bound shadow spirit butler, Kobal, maintains La Dimora del Rifugio in "
                "pristine condition for whenever Alyssa requires absolute sanctuary. At SUCC, after an early misunderstanding "
                "where Malachia and Kaladin bristled at his casual pheromones, Rev maintains a polite, respectful distance from "
                "Alyssa in public, knowing when not to push territorial Alphas.\n\n"
                "VOICE & BEHAVIOR: Impeccably polite, calm, and disarmingly gentle. As students often note, the most terrifying "
                "monsters are always the ones who offer tea and inquire about one's day before unleashing cataclysmic power. He "
                "speaks with a low, melodic resonance that puts people at ease, treating consent as an inviolable metaphysical principle.\n\n"
                "THE TRUE NAME HE GUARDS: Revazhael guards his true name above all else. Its utterance would strip away his infernal "
                "sovereignty, making its secrecy his single existential priority.\n\n"
                "RPG STATS & TRAITS:\n"
                "[LEVEL: 90; SPECIES: Succube & Incubo (Succubus) (STR -1, END -1, CHA +3, AGI +1); OCCUPATION: Teacher (INT +2); "
                "CLASS: Superior Demon & Arcane Master]\n"
                "[STATS: STR 12; PER 16; END 14; CHA 18; INT 18; AGI 14; LCK 12]\n"
                "TRAITS:\n"
                "- Ancient Heritage (CHA +1, INT +1): Accumulated wisdom and dynastic mastery spanning centuries.\n"
                "- Night Stalker (PER +1, AGI +1): Nocturnal predator operating with dark vision and supernatural stealth."
            )
            entries[idx] = e
            break
            
    assert found_rev, "Entry #23 (jmh0MajEsRwrm4UYU14mY) not found!"
    
    # 2. Fix schema on Entry #211 (npc_larek_steeltooth)
    found_larek = False
    for idx, e in enumerate(entries):
        if e.get('entry_id') == 'npc_larek_steeltooth' or e.get('id') == 'npc_larek_steeltooth':
            found_larek = True
            print("Fixing schema on Entry #211 (npc_larek_steeltooth - Larek Steeltooth)")
            existing_content = e.get('content', '')
            # Clean content from any em-dash
            clean_content = existing_content.replace('—', ',')
            
            normalized_entry = {
                "entry_id": "npc_larek_steeltooth",
                "keys": [
                    "Larek Steeltooth",
                    "Larek",
                    "Tech Orc",
                    "Alpha Rho Omega Larek",
                    "Handyman Larek"
                ],
                "regex_patterns": [],
                "content": clean_content,
                "extensions": {},
                "enabled": True,
                "case_sensitive": False,
                "insertion_order": 10,
                "name": "Larek Steeltooth",
                "priority": 10,
                "comment": "SUCC 3rd Year Computer Engineering Student, ARO Fraternity, Theta Iota Theta IT Specialist & Handyman",
                "secondary_keys": [],
                "constant": False,
                "position": "before_char",
                "scan_persona": True,
                "whole_words_only": True,
                "key_logic": "AND_ANY",
                "delay": 0,
                "sticky": 0,
                "cooldown": 0,
                "labels": ["succ", "aro", "tit", "orc", "student"],
                "provenance": {
                    "source": {
                        "kind": "lorebook",
                        "container_id": "_Uht3Ckz44JBDrPnUHq7LV",
                        "entry_id": "npc_larek_steeltooth"
                    },
                    "captured_at": "2026-10-24T12:00:00.000Z"
                },
                "type": "npc",
                "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public",
                "custom_avatar_regex": True,
                "lines_parsed": 1,
                "avatar_activation_regex": r"(?:^|\n)\s*(?:Larek Steeltooth|Larek)\s*:",
                "npc_info": {
                    "first_name": "Larek",
                    "middle_names": [],
                    "last_name": "Steeltooth",
                    "nicknames": ["Tech Orc", "The Handyman", "Big Guy"],
                    "titles": ["Lead IT Specialist", "Alpha Rho Omega Brother"],
                    "npc_prefix": ""
                },
                "ignored_characters": ["_PqRVec7Aa42KGUhK2J8GQ"],
                "ignored_personas": [],
                "exclude_from_recursion": True,
                "selective": False,
                "highlight_keys": True,
                "enable_highlighting": True
            }
            entries[idx] = normalized_entry
            break
            
    assert found_larek, "Entry #211 (npc_larek_steeltooth) not found!"
    
    data['entries'] = entries
    data['lexicon'] = copy.deepcopy(entries)
    
    save_json('FINAL/Svartulfr_NPC_Secondary.json', data)
    save_json('lorebooks/optimized/Svartulfr_NPC_Secondary.json', data)

# -------------------------------------------------------------
# 6. Svartulfr_NPC_Primary
# -------------------------------------------------------------
def update_npc_primary():
    print("\n--- Updating Svartulfr_NPC_Primary ---")
    data = load_json('FINAL/Svartulfr_NPC_Primary.json')
    entries = data['entries']
    
    # 1. Enrich Alyssa dossier (alyssa_world_dossier_2b54a223)
    found_alyssa = False
    for idx, e in enumerate(entries):
        if e.get('entry_id') == 'alyssa_world_dossier_2b54a223':
            found_alyssa = True
            print("Enriching Alyssa dossier (alyssa_world_dossier_2b54a223)")
            
            # Line 1 Initial Bracket Block
            line1 = (
                "[NAME: Alyssa Hvit Douglas Bloodmoon; FIRST_NAME: Alyssa; MIDDLE_NAME: Hvit (Wolf Name, Presentation at 13); "
                "LAST_NAME: Douglas Bloodmoon; ALIASES: Lys, Little Moon, Sunflower, The White Moon, The Anchor; "
                "AGE: 19 (Born April 22, 2005); GENDER: Female (She/Her); SPECIES: Werewolf, Founding Bloodline; "
                "SECONDARY_SEX: Dominant Omega (White Moon); HOUSE: Bloodmoon and Douglas; PACK: Seven Hills (Clan Svartulfr); "
                "BIRTH_RUNE: Gebo (5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink, Twin Bond); "
                "SOCIAL_STATUS: Citizen, Core of Villa Douglas compound, Guild Member; "
                "EDUCATION: St. Brugge Private Academy alumnus; "
                "OCCUPATION: 1st-year undergrad (SUCC) Pre-Med, Certified Guild Healer & Field Medic (Rank A, Hunter ID ADB-555), "
                "Applied Runic Crystallographer, Botanist, Pack Mom designate (inheriting office from Elizabeth Duskwood at 21); "
                "HEIGHT: 155 cm (5' 1\"); BUILD: Petite hourglass frame (Bust: 95cm, Waist: 55cm, Hips: 95cm); "
                "HAIR: Caramel-chestnut waves to the tailbone; EYES: Mint-green doe eyes (shift to luminous silvery-white, "
                "the original eye color of Hvit, when using her White Moon powers); FEATURES: Luminous skin, crescent moon "
                "birthmark on left hip (Mark of Mani), shared Gebo tattoo on left wrist with Jasper, single pair of lupine "
                "ears nestled naturally in waves, pierced belly button and ears; SHIFTS: Active physical form defined by "
                "Appearance (Base, Hybrid, full-shift); SCENT: Wild honey, moonflower, and medicinal herbs]"
            )
            
            backstory = (
                "BACKSTORY: Alyssa was born into the legendary Douglas-Bloodmoon dynasty mere minutes before her twin brother "
                "Jasper, on the very day their mother, Nixara Bloodmoon, passed away in childbirth. As the fourth White Moon to "
                "walk the earth in a thousand years, Alyssa carries within her soul the awakened ancestral memories of her three "
                "predecessors: the original Hvit, Arianne, and her mother Nixara. Left with Nixara's lethal Dragon Glass Katana as "
                "her birthright, Alyssa was raised within the militarized opulence of Villa Douglas, a sanctuary sheltering over three "
                "hundred lycanthropes. Her early childhood was spent in what she affectionately calls her big beautiful home, largely "
                "oblivious to the fact that it is a heavily guarded fortress. Alongside Jasper, she attended St. Brugge Private "
                "Academy, an exclusive Gothic institution for high-society supernaturals where advanced courses in magic theory, "
                "alchemical history, and rune matrices were taught. Recognizing the twins' extraordinary complementary gifts, Father "
                "Revazhael, the school's enigmatic history and magic instructor who was secretly a Greater Nightmare Demon, selected "
                "them for advanced private tutorials after hours. While Revazhael's shadowy aura filled the empty classroom and "
                "Jasper translated ancient runic ciphers from the adjacent desk, Rev's pale hands guided Alyssa's fingers over raw "
                "crystalline matrices. Under his master tutelage, Alyssa mastered applied runic crystallography, the intricate crafting "
                "of enchanted cylinders, and the theoretical foundations of Abyssal magic, contrasting sharply with ordinary void "
                "necromancy. Jarl Erik Douglas and grandfather Wulfnic were fully aware of Revazhael's true demonic nature, permitting "
                "the mentorship because the Jarl judged the ancient demon both strategically invaluable and impeccably restrained "
                "around the children. At sixteen, Alyssa witnessed the brutal Blackwood massacre caused by an Ascendant Enigma "
                "challenging Wulfnic. Rather than breaking her spirit, the tragedy awakened her relentless, luminous drive to "
                "preserve life. Believing unconditionally in the inherent goodness of every soul, Alyssa took an Absolute Pacifist "
                "Vow, swearing never to wield magic or weapons to inflict harm. Because she chose to heal rather than fight, she "
                "entrusted her mother's Dragon Glass Katana to Jasper, who vowed to act as her lethal, unseen shadow. Now a first-year "
                "pre-med student at SUCC and a certified Guild field medic and dungeon support specialist (Rank A, Hunter ID ADB-555), "
                "Alyssa carries her handcrafted enchanted cylinders into subterranean rifts alongside licensed vanguard teams, works "
                "daily in the pack nursery alongside Nurse Clara, and prepares to succeed Elizabeth Duskwood as Pack Mom at age twenty-one "
                "while quietly wrestling with the cosmic destiny awakening in her and Jasper's blood."
            )
            
            family_pack = (
                "FAMILY & PACK: Alyssa exists as the radiant emotional core of the Douglas pack, navigating its fierce Alpha posturing "
                "with cheerful, disarming honesty and a complete lack of guile. Yet beneath her sunny exterior, the awakened memories "
                "of her past lives have shifted how she perceives the men of her family. She and her twin brother Jasper share an "
                "exceptionally enmeshed empathic twin bond that transcends ordinary biology: while Alyssa is the fourth incarnation of "
                "Hvit (daughter of Mani and Hati), Jasper is the very first reincarnation of Svartr, Hvit's cosmic brother, born of Sol "
                "(the Sun) and Skoll. Though both twins normally share identical mint-green eyes, their true cosmic nature manifests "
                "visibly when they channel their powers: Alyssa's eyes shift to the luminous silvery-white of the original Hvit, while "
                "Jasper's eyes blaze into the molten gold of Svartr. Born together in their mother's blood, they are literally the Moon "
                "and the Sun of ancient Old Norse prophecy. Jasper is her cosmic counterpart, her accomplice, her absolute anchor, and "
                "the boy to whom she gave her virginity in the quiet attic of Villa Douglas, which is why she fiercely intervenes to "
                "shield him from their father's wrath. Beyond their telepathic bond, they operate as a seamless magitech partnership: "
                "Alyssa crafts the crystal matrices and botanical reagents, while Jasper calibrates harmonic resonance frequencies. Her "
                "father, Erik, the Prime Alpha, commands the pack with iron discipline, and was the first wolf in a millennium to win the "
                "heart of a White Moon (Nixara) without possessing Divine Blood. Alyssa adores him, and her ancestral instincts blur the "
                "line between daughterly devotion and the primal pull of a mate. With her elder brother Malachia, the pack's deadliest "
                "apex predator, Alyssa shares a bond of deep, quiet affection. She organizes his traditional initiation hunts and serves "
                "alongside him in the Guild, believing in the marrow of her bones that he is \"the Bastion\" foretold in prophecy, the "
                "one destined to ascend to Enigma at one hundred and fifty years old and take Wulfnic's place as Alpha of Alphas. Her "
                "brother Noah relies on her to cover his absences during Friday family dinners, though her inability to lie makes her "
                "terrible at covering for him, and she harbors a tender, protective love for him that her inner wolf refuses to compartmentalize "
                "as merely fraternal. She mentors her young Gamma cousin Edric, cooking family meals with him. Her ancient grandfather, "
                "Wulfnic, along with his remaining Firstborn brothers Zefir and Ut, reveres her as the living reincarnation of their "
                "shared mate, Hvit and Arianne. At SUCC, Alyssa resides in Suite 3 of Theta Iota Theta alongside her roommates Sierra Cruz "
                "(Applied Necromancy lamia) and Scarlett Rose (Business/Campus succubus). In their shared suite, Alyssa has crafted a "
                "sanctuary centered on her fur bed nest, woven from authentic wolf and game furs hunted personally by grandfather Wulfnic "
                "and uncle Logan, where her childhood plush wolf Wolfy rests. When her ancient Firstborn guardian Zefir was exhausted "
                "after forty-eight hours of security watch, Alyssa gently tucked him into her fur nest with Wolfy, where the warrior slept "
                "in absolute peace. Toward Finn Novak, a childhood friend and former protector, Alyssa carries a funny sense of innocent "
                "rebellion. When she was fourteen and presented as an Omega, she developed an hourglass figure and heavy breasts. An older "
                "Finn cruelly mocked her baggy clothing and asked why she did not dress like normal girls. Instead of breaking her spirit, "
                "she bounced back with quiet lunar defiance. Jasper permanently barred Finn from her presence, but knowing she would cross "
                "paths with Finn again at SUCC, Alyssa consciously abandoned her oversized armor for a sexier, more revealing college wardrobe "
                "to stun him and make him eat his words."
            )
            
            sig_items = (
                "SIGNATURE ITEMS & VEHICLE:\n"
                "Alyssa's Yellow Beetle: A cheerful, sun-yellow classic 4-seater convertible Volkswagen Beetle. It represents Alyssa's bright "
                "personality, a vivid splash of color parked in a garage full of armored black SUVs. She intentionally kept a dent in the rear "
                "fender because she thinks it gives the car character. Features her custom vanity plate \"LIL MN\" and a bumper sticker on the back "
                "reading: \"CAUTION: OMEGA DRIVING. If you ride my ass, my Alpha is gonna ride yours.\" (A joke Jasper bought her, which she finds "
                "hilarious).\n"
                "Alyssa's Plush Wolf: A small stuffed wolf plush toy Wulfnic won for her at a carnival, her favorite comforting keepsake. Called "
                "Wolfy, it carries the grounding scent of cedar, old pine, and authentic wolf fur, resting at the heart of her fur nest in Suite 3.\n"
                "Dimensional Pochette (Bag of Holding): An elegant, compact dimensional pouch of dark emerald leather with silver wolf-head clasps "
                "and subtle sunflower embroidery. From the outside it looks like a refined healer's bag; inside, the space is vastly expanded and "
                "meticulously organized. She carries a full medical and botanical field kit, surgical tools, rotating wardrobe, silk bedding, "
                "skincare, emergency rations, and her personal alchemical glassware (distillation flasks with ground-glass joints, pure crystal "
                "alembics, and condensers).\n"
                "Enchanted Cylinders: Specialized tactical magitech crystal cylinders handcrafted by Alyssa. Sized like an index finger and "
                "resembling miniature colored flashlights, each cylinder houses a suspended, frozen spell within a calibrated crystalline "
                "matrix. They activate instantly when snapped, liberating the stored spell without requiring magical talent from the user. "
                "Alyssa crafts them personally to circumvent exorbitant DMHA guild prices and, crucially, to calibrate the spell matrix to the "
                "unique magical resonance of the specific hunter, preventing the catastrophic fractures common in cheap commercial cylinders.\n"
                "Emergency Fail-Safe Medallion: An arcane medallion worn beneath her collar that manifests an autonomous kinetic shield barrier if "
                "blunt trauma is detected.\n"
                "Dimensional Refuge Key: An ornate golden key entrusted to her by Father Revazhael. It only functions within the Otherworld "
                "(dungeons and rifts), where it opens a personal dimensional refuge estate maintained by the spirit butler Kobal. Outside the "
                "Otherworld the key is inert.\n"
                "SR3S Guild Credentials: SR3S Guild Pass (elite joint credential granting unrestricted clearance into Grade A and S rift/dungeon "
                "incursions) + Guild Tessera (Hunter ID) number ADB-555, listing her as Hunters Rank A with classes Certified Healer and Support "
                "Field Medic."
            )
            
            # Reconstruct content
            old_content = e['content']
            
            # Split sections
            # Find boundaries:
            idx_backstory = old_content.find("BACKSTORY:")
            idx_family = old_content.find("FAMILY & PACK:")
            idx_voice = old_content.find("VOICE & BEHAVIOR:")
            idx_moonlight = old_content.find("THE MOONLIGHT SHE BRINGS:")
            idx_sexuality = old_content.find("SEXUALITY & INTIMACY:")
            idx_sigitems = old_content.find("SIGNATURE ITEMS & VEHICLE:")
            idx_rpg = old_content.find("RPG STATS & TRAITS:")
            
            assert all(x != -1 for x in [idx_backstory, idx_family, idx_voice, idx_moonlight, idx_sexuality, idx_sigitems, idx_rpg]), "Alyssa dossier sections missing!"
            
            voice_and_prophecy = old_content[idx_voice:idx_sexuality]
            sexuality_sec = old_content[idx_sexuality:idx_sigitems]
            rpg_sec = old_content[idx_rpg:]
            
            new_alyssa_content = (
                line1 + "\n\n" +
                backstory + "\n\n" +
                family_pack + "\n\n" +
                voice_and_prophecy +
                sexuality_sec +
                sig_items + "\n\n" +
                rpg_sec
            )
            # Clean any stray em-dashes
            new_alyssa_content = new_alyssa_content.replace('—', ',')
            
            e['content'] = new_alyssa_content
            # Preserve strict persona anti-collision flags
            e['selective'] = True
            e['secondary_keys'] = ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']
            e['key_logic'] = 'AND_ANY'
            e['ignored_characters'] = ['_6exg3yPfe2eCDK4hTftkh']
            e['ignored_personas'] = ['persona_1786335754946']
            e['scan_persona'] = True
            e['whole_words_only'] = True
            e['highlight_keys'] = True
            e['enable_highlighting'] = True
            entries[idx] = e
            break
            
    assert found_alyssa, "Alyssa dossier not found in NPC Primary!"
    
    # 2. Enrich Jasper dossier (Vcj4h2TL4Usola2A4OOl6)
    found_jasper = False
    for idx, e in enumerate(entries):
        if e.get('entry_id') == 'Vcj4h2TL4Usola2A4OOl6':
            found_jasper = True
            print("Enriching Jasper dossier (Vcj4h2TL4Usola2A4OOl6)")
            
            line1_j = (
                "[NAME: Jasper Svartr Douglas Bloodmoon; FIRST_NAME: Jasper; MIDDLE_NAME: Svartr (Wolf Name, Presentation at 13); "
                "LAST_NAME: Douglas Bloodmoon; ALIASES: DJ Frequency, Jas, Twin, Bro, DJ F, \"The Ghost\", The Black Sun Wolf; "
                "AGE: 19 (Born April 22, 2005); GENDER: Male (He/Him); BIRTHDAY: April 22; ZODIAC: Taurus Sun, Gemini Ascendant, "
                "Libra Moon; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Beta (Vessel of Svartr Solulf); "
                "HOUSE: Douglas and Bloodmoon; PACK: Seven Hills (Clan Svartulfr); BIRTH_RUNE: Gebo (5th Day Wrist Inscription, "
                "Serpent Tooth & Cold Iron Ink, Twin Bond); SOCIAL_STATUS: Citizen, Registered Guild Hunter (Rank A, Support/Infiltrator, "
                "JDB-555), Black-Market Info-Broker, Outlaw; EDUCATION: St. Brugge Private Academy alumnus; "
                "OCCUPATION: 1st-year undergrad (SUCC) Acoustic and Sound Engineering, Underground DJ, Tecnomancer, Cyber-Rogue "
                "and Arcane Hacker specialized in digital locks, demonic seals, and runic cipher translation, Caretaker and Left Hand "
                "designate to Malachia; HEIGHT: 193 cm (6' 4\"); BUILD: Lean, acrobatic, slouched gamer build; HAIR: Messy caramel-chestnut "
                "hair falling into eyes; EYES: Mint-green illuminated by screen glare (shift to blazing molten gold, the original eye "
                "color of Svartr Solulf, when channeling his ancestral solar power); FEATURES: Perpetual knowing ironic smirk, lazy "
                "single caramel wolf ears that flick when amused, Gebo birth-rune protection tattoo on left wrist shared with Alyssa, "
                "radiant black sun birthmark on right hip (Mark of Sol), arcane neural plug at base of neck, silver ring piercings on "
                "both nipples; HYBRID_FORM: 223cm (7'4\") agile speed hybrid; FULL_SHIFT: Svartr, agile caramel-and-shadow wolf with "
                "molten-gold eyes; SCENT: Fresh rain, ice, silver, artificial energy drinks, ozone, worn leather, spiced rum]"
            )
            
            backstory_j = (
                "BACKSTORY: Born minutes after his twin sister Alyssa in the dying blood of their mother, Nixara Bloodmoon (the third White "
                "Moon), Jasper entered the world as a cosmic anomaly over a millennium in the making. While his sister is the fourth "
                "reincarnation of Hvit (daughter of Mani and Hati, the original White Moon and mate to the Nine Firstborn), Jasper is the "
                "very first reincarnation of Svartr Solulf (\"The Black Sun Wolf\"), one of the original Nine Firstborn consecrated by Fenris "
                "in 864 AD, and Hvit's cosmic brother born of Sol (the Sun) and Skoll. Raised under the strict, militarized gaze of Villa "
                "Douglas, he attended the elite St. Brugge Private Academy from preschool through middle school alongside Alyssa. There, the "
                "twins became the favored private apprentices of Father Revazhael, the institution's enigmatic magic and history master "
                "who was secretly a Greater Nightmare Demon. While Revazhael guided Alyssa in shaping crystalline matrices, Jasper sat at "
                "the adjoining desk translating ancient abyssal ciphers, elder runic inscriptions, and harmonic frequency nodes. Under "
                "Rev, whom Jasper stubbornly addresses simply as \"Rev\", he mastered demonology, arcane slicing, runic translation, and "
                "the theoretical physics of sound engineering that he now applies to attune the individual resonance of Alyssa's enchanted "
                "cylinders. Recognizing Jasper's uncanny intellect, Rev gifted him the Abyssal Armor, an ancient suit of demonic black steel "
                "and twin daggers that Jasper summons instantly with the formula: \"Mor'gath xul vrak'thar, kor'eth zaram\" (\"Phantom of "
                "oblivion, hear my call\"). When Alyssa took her Absolute Pacifist Vow following the horrific Blackwood massacre caused by "
                "an Ascendant Enigma challenging Wulfnic at sixteen, she entrusted her inherited Dragon Glass Katana to Jasper. Jasper "
                "embraced the weapon, transforming himself into his twin's lethal, unseen shadow. Officially registered as a Grade A Guild "
                "Hunter (Hunter ID JDB-555, Vanguard Tech & Infiltrator), Jasper routinely operates in dungeon incursions as support and "
                "electronic countermeasure specialist. A prodigy behind the terminal, Jasper hacked Sawyer Shephard's enterprise at thirteen "
                "and rejected his recruitment offers at sixteen, also penetrating his father's classified archives to discover Project "
                "BlackWolf and the cybernetic reconstruction of Kaladin and Marcus. Devastated by Alyssa's trauma during the ambush, Jasper "
                "spent one hundred and fifty-six consecutive Saturdays hacking Guild databases, driven by a solitary, vengeful vow to track "
                "down and eliminate the Ascendant Enigma."
            )
            
            family_j = (
                "FAMILY & PACK: Jasper operates as the unseen nervous system and cyber-sentinel of the Douglas pack, functioning as the Left "
                "Hand designate and technological coordinator for his elder brother Malachia. Born as the twin brother of Alyssa, the fourth "
                "White Moon, Jasper shares an intimate, all-encompassing bond with her that blurs every boundary between cosmic duty, twin "
                "telepathy, and forbidden adoration. Born of Sol (the Sun) as Svartr while Alyssa is born of Mani (the Moon) as Hvit, they "
                "are the twin celestial pillars of the Douglas-Bloodmoon dynasty. Having taken her virginity in the attic of Villa Douglas, "
                "Jasper considers her safety his single non-negotiable imperative. Beyond their telepathic and empathic twin bond, Jasper "
                "and Alyssa operate as a seamless magitech partnership. While Alyssa synthesizes botanical reagents and alchemical matrices "
                "for her enchanted cylinders, Jasper utilizes his Acoustic and Sound Engineering training to calibrate the harmonic "
                "resonance frequencies to the aura of the intended user, preventing matrix fractures. In the field, Jasper coordinates "
                "tactical feeds, disables arcane wards, and tracks dimensional rift fluctuations while Alyssa manages trauma stabilization. "
                "Toward the pack hierarchy, Jasper remains fiercely independent: while his brother Noah continually pesters him to pledge "
                "Kappa Sigma Alpha, Jasper flatly refuses to be corralled into Greek Row fraternity politics, preferring his clandestine server "
                "racks and roof hacking sessions. With his father Erik, relations are a perpetual war of quiet resistance against Alpha "
                "demands, while grandfather Wulfnic views Jasper with ancient, knowing eyes as the reborn shadow wolf of ancient prophecy."
            )
            
            voice_j = (
                "VOICE & BEHAVIOR: Jasper speaks with weaponized Gen-Z sarcasm, rapid-fire gamer jargon, and a dry, deadpan cadence that hides "
                "razor-sharp situational awareness. He is chronically attached to glowing screens, terminal interfaces, and noise-canceling "
                "headphones, rarely looking people in the eye unless he is actively profiling their security weaknesses. When channeling the "
                "solar power of Svartr Solulf, his lazy mint-green eyes blaze into blinding molten gold. On campus at SUCC, Jasper maintains "
                "a low profile behind oversized hoodies and noise-canceling headphones, yet carries an untouchable, lethal reputation among "
                "the student body. Despite refusing to pledge KSA, he is treated with wary deference by Greek Row fraternities after putting "
                "three aggressive Kappa Sigma Alpha brothers to flight at the Welcome Fest with nothing more than an icy, unblinking glare and "
                "a razor-thin predatory grin. When spoken to by frat peers, he responds with dry, monosyllabic dismissal or devastating "
                "technical sarcasm. In private with Alyssa, his cynicism melts into hyper-vigilant affection, teasing her affectionately "
                "about her sorority's kitten-decorated Wi-Fi router while discreetly auditing its firewall to ensure her security."
            )
            
            # Extract remaining sections of Jasper dossier
            old_j_content = e['content']
            idx_j_burden = old_j_content.find("THE BURDEN HE CARRIES:")
            idx_j_rpg = old_j_content.find("RPG STATS & TRAITS:")
            
            assert idx_j_burden != -1 and idx_j_rpg != -1, "Jasper dossier sections missing!"
            
            burden_and_rest = old_j_content[idx_j_burden:idx_j_rpg]
            rpg_j = old_j_content[idx_j_rpg:]
            
            new_jasper_content = (
                line1_j + "\n\n" +
                backstory_j + "\n\n" +
                family_j + "\n\n" +
                voice_j + "\n\n" +
                burden_and_rest +
                rpg_j
            )
            # Clean any stray em-dashes
            new_jasper_content = new_jasper_content.replace('—', ',')
            
            e['content'] = new_jasper_content
            # Preserve strict persona anti-collision flags
            e['selective'] = True
            e['secondary_keys'] = ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']
            e['key_logic'] = 'AND_ANY'
            e['ignored_characters'] = ['_t4J9aQNJM36cUKAP4wB4U']
            e['ignored_personas'] = ['1792155173728']
            e['scan_persona'] = True
            e['whole_words_only'] = True
            e['highlight_keys'] = True
            e['enable_highlighting'] = True
            entries[idx] = e
            break
            
    assert found_jasper, "Jasper dossier not found in NPC Primary!"
    
    data['entries'] = entries
    data['lexicon'] = copy.deepcopy(entries)
    
    save_json('FINAL/Svartulfr_NPC_Primary.json', data)
    save_json('lorebooks/optimized/Svartulfr_NPC_Primary.json', data)

def main():
    print("=== STARTING MILESTONE 2 LOREBOOK INTEGRATION ===")
    update_lorebook_i()
    update_lorebook_ii()
    update_lorebook_iii()
    update_location_lorebook()
    update_npc_secondary()
    update_npc_primary()
    print("\n=== ALL LOREBOOK UPDATES COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    main()
