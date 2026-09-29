import json
import os
import re

def parse_json_field(val, default=None):
    if val is None:
        return default if default is not None else []
    if isinstance(val, (list, dict)):
        return val
    if isinstance(val, str):
        val = val.strip()
        if not val:
            return default if default is not None else []
        try:
            return json.loads(val)
        except Exception:
            if default is not None and isinstance(default, list):
                return [x.strip() for x in val.split(',') if x.strip()]
            return val
    return default if default is not None else []

def clean_format_text(text):
    if not text or not isinstance(text, str):
        return text if text is not None else ""
    # Enforce Rule 2: Remove em-dash (—) and en-dash (–)
    text = text.replace("—", ", ").replace("–", ", ")
    return text.strip()

def extract_npc_keys(char):
    name = (char.get('display_name') or f"{char.get('first_name', '')} {char.get('last_name', '')}").strip()
    keys = []
    if name:
        keys.append(name)

    # First name
    first = char.get('first_name')
    if first and first.strip() and first.strip() not in keys:
        keys.append(first.strip())

    # Nicknames
    nicknames = parse_json_field(char.get('nicknames'), [])
    if isinstance(nicknames, list):
        for nk in nicknames:
            if isinstance(nk, str) and nk.strip() and nk.strip() not in keys:
                keys.append(nk.strip())

    # Extract quotes or nicknames in name e.g. Roger "Rocky" Mackenzie
    quote_matches = re.findall(r'["\']([^"\']+)["\']', name)
    for qm in quote_matches:
        qm_clean = qm.strip()
        if qm_clean and len(qm_clean) > 2 and qm_clean not in keys:
            keys.append(qm_clean)

    # Titles
    titles = parse_json_field(char.get('titles'), [])
    if isinstance(titles, list):
        for t in titles:
            if isinstance(t, str) and t.strip() and t.strip() not in keys:
                keys.append(t.strip())

    # Explicit title prefixes (e.g., Professor, Coach, Ranger, Dr.)
    title_prefixes = ["Professor", "Coach", "Ranger", "Dr.", "Doctor", "Nurse"]
    for tp in title_prefixes:
        if tp in name and tp not in keys:
            # Add short form e.g. "Ranger Locke"
            parts = name.split()
            if len(parts) >= 2 and parts[0].startswith(tp):
                short_title = f"{parts[0]} {parts[-1]}"
                if short_title not in keys:
                    keys.append(short_title)

    # Clean keys: remove single letter keys or noise
    filtered_keys = []
    for k in keys:
        k_clean = k.strip()
        if len(k_clean) >= 2 and k_clean not in filtered_keys:
            filtered_keys.append(k_clean)

    return filtered_keys if filtered_keys else [name]

def reindex_entries(entries_list):
    reindexed = []
    for i, entry in enumerate(entries_list):
        e = dict(entry)
        e['uid'] = i
        reindexed.append(e)
    return reindexed

def convert_g3_characters():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = os.path.join(base_dir, 'exports', 'Svartulfr_Export.json')
    if not os.path.exists(src_path):
        src_path = os.path.join(base_dir, 'Svartulfr_Export.json')

    with open(src_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    world = raw_data.get('world', {})
    chars = raw_data.get('world_characters', [])

    g1_names = [
        'erik douglas', 'malachia douglas bloodmoon', 'noah douglas bloodmoon',
        'jasper douglas bloodmoon', 'alyssa douglas bloodmoon', 'logan douglas',
        'edric douglas', 'lord cornelius douglas', 'magnus douglas iii',
        'elizabeth duskwood', 'wulfnic bloodmoon', 'ut berg', 'zefir hvitskog',
        'fenris', 'nixara bloodmoon', 'kaladin nargathon', 'marcus thornfield'
    ]

    g2_names = [
        # Council (21)
        'cass harrow', 'naomi black', 'darius vale', 'bianca rossi', 'dominic chen',
        'aurora night', 'eclipse noir', 'isobel blackwater', 'helena weiss',
        "marcus o'connor", 'vito marino', 'angelo moreno', 'federico "riki" savini',
        'federico savini', 'harlan "huck" beaumont', 'harlan beaumont', 'zeera',
        'brak ironfist', 'barrow', 'harrison black', 'abel vilas', 'cassian aralas', 'marlowe voss',
        # Team Ukiyo & Nomads (5)
        'radek', 'goran', 'kian', 'marek',
        # Grave Mistake (4)
        'fade greymoor', 'mackenzie sanchez-rogers', 'roland vickers', 'viola carter', 'via carter',
        # Athletes (6)
        'vincent campbell', 'finnegan novak', 'jared thompson', 'santiago herrera',
        'bailey rogers', 'tomas matthews',
        # Frat / Sorority (6)
        'scarlett rose', 'sierra', 'janice thompson', 'andrew campbell', 'andy campbell',
        'brittany willow', 'rev',
        # Five Cocketeers & Roommates (5)
        'russ sinclair', 'dean', 'eric', 'raymond', 'javier reyes',
        # Staff / Faculty (10)
        'archer wolfwood', 'professor loewe', 'richard loewe', 'ariadne cirillo', 'dullahan', 'coach d',
        'barkley rover', 'adelin coso', 'coach mithers', 'hideo reid',
        'professor mollusk moreau', 'mollusk moreau', 'professor marit christiansen', 'marit christiansen',
        # Featured Students (9)
        'casey williams', 'chase anderson', 'stanley davies jr.', 'stanley davies jr',
        'roman blackwood', 'kolya varenkov', 'iordan r. vess', 'iordan vess', 'oskar', 'tate', 'nikolaj jökull', 'nikolaj jokull',
        # Featured Alumni & Familiari (4)
        'hank thompson', 'jasmin thompson', 'stanley davies sr.', 'stanley davies sr', 'eris davies',
        # Sinners (8)
        'jean-luc virtuoso', 'alicia virtuoso', 'dante', 'zero', 'dr. arthur sinclair', 'arthur sinclair',
        'gluttony - kevin', 'kevin', 'envy - siobhan', 'siobhan', 'greed - roxie', 'roxie',
        # Ballantines (4)
        'ruaraidh "rory" ballantine', 'ruaraidh ballantine', 'rory ballantine',
        'sullivan "sully" jones', 'sullivan jones', 'sully jones',
        'harper aries', 'daniel "danny" boone', 'daniel boone', 'danny boone',
        # Core Allies (6)
        "eithne dal'kereth", 'yael', 'bryson', 'dominic rogers', 'luisa sanchez rogers', 'luisa sanchez', 'allegra lumsden'
    ]

    def clean_name(n):
        return (n or '').strip().lower()

    g1_set = set(g1_names)
    g2_set = set(g2_names)

    def is_g1_or_g2(char):
        name = clean_name(char.get('display_name') or char.get('first_name', '') + ' ' + char.get('last_name', ''))
        for g1 in g1_set:
            if g1 == name: return True
        for g2 in g2_set:
            if g2 == name: return True
        for g1 in g1_set:
            if len(g1) > 4 and (g1 in name or name in g1): return True
        for g2 in g2_set:
            if len(g2) > 4 and (g2 in name or name in g2): return True
        return False

    g3_chars = [c for c in chars if not is_g1_or_g2(c)]

    g3_a_real = [c for c in g3_chars if len(c.get('long_summary') or '') > 100]
    g3_b_stubs = [c for c in g3_chars if len(c.get('long_summary') or '') <= 100]

    print(f"Total Characters: {len(chars)}")
    print(f"G3 Candidates Total: {len(g3_chars)} (G3-A Real: {len(g3_a_real)}, G3-B Stubs: {len(g3_b_stubs)})")

    def build_lexicon_entry(char, uid, is_real):
        cid = char.get('id') or f"g3_{uid}"
        name = (char.get('display_name') or f"{char.get('first_name', '')} {char.get('last_name', '')}").strip()
        keys = extract_npc_keys(char)

        # Build content in Pronoun Pruned Prose (PPP)
        if is_real:
            ls = clean_format_text(char.get('long_summary') or "")
            s = clean_format_text(char.get('summary') or "")
            content = ls if len(ls) > 100 else s
            final_inst = clean_format_text(char.get('final_instructions') or "")
            if final_inst and final_inst not in content:
                content = f"{content}\n\n[INSTRUCTIONS: {final_inst}]"
        else:
            s = clean_format_text(char.get('summary') or "")
            content = s if s else f"[NAME: {name}; STATUS: background NPC / Solarton student]\n\n{name} is an affiliated background NPC or resident at Solarton / SUCC."

        entry_obj = {
            "entry_id": cid,
            "id": cid,
            "uid": uid,
            "name": name,
            "comment": f"G3 NPC ({'Real' if is_real else 'Stub'}) converted from World Character ID: {cid}",
            "keys": keys,
            "key": keys,
            "secondary_keys": [],
            "keysecondary": [],
            "key_logic": "AND_ANY",
            "selectiveLogic": 0,
            "selective": False,
            "content": content,
            "enabled": True,
            "disable": False,
            "constant": False,
            "position": "before_char",
            "priority": 15,
            "insertion_order": 100,
            "order": 100,
            "case_sensitive": False,
            "caseSensitive": False,
            "whole_words_only": True,
            "matchWholeWords": True,
            "scan_persona": False,
            "matchPersonaDescription": False,
            "delay": 0,
            "sticky": 0,
            "cooldown": 0,
            "type": "npc",
            "lines_parsed": 1,
            "source_category": "characters_g3",
            "extensions": {
                "source_character_id": cid,
                "g3_subgroup": "G3-A_real" if is_real else "G3-B_stub",
                "character_meta": {
                    "first_name": char.get('first_name'),
                    "last_name": char.get('last_name'),
                    "nicknames": parse_json_field(char.get('nicknames'), []),
                    "titles": parse_json_field(char.get('titles'), []),
                    "pronouns": char.get('pronouns'),
                    "species_id": char.get('species_id'),
                    "species": char.get('species'),
                    "birthdate": char.get('birthdate'),
                    "start_timeline_position": char.get('start_timeline_position'),
                    "display_description": clean_format_text(char.get('display_description') or "")
                },
                "wyvern": {
                    "priority": 15,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "npc",
                    "lines_parsed": 1
                }
            }
        }
        return entry_obj

    g3_converted_all = []
    g3_converted_a = []
    g3_converted_b = []

    uid_counter = 0

    # 1. Convert G3-A Real
    for c in g3_a_real:
        entry = build_lexicon_entry(c, uid_counter, is_real=True)
        g3_converted_all.append(entry)
        g3_converted_a.append(entry)
        uid_counter += 1

    # 2. Convert G3-B Stubs
    for c in g3_b_stubs:
        entry = build_lexicon_entry(c, uid_counter, is_real=False)
        g3_converted_all.append(entry)
        g3_converted_b.append(entry)
        uid_counter += 1

    entities_dir = os.path.join(base_dir, 'exports', 'entities')
    os.makedirs(entities_dir, exist_ok=True)

    def write_lorebook_file(filename, name, desc, entries_list, extra_ext=None):
        ext = {
            "creator": "Wyvern G3 NPC Converter",
            "source_world_id": world.get('id', ''),
            "source_category": "characters_g3",
            "feature": "Lexicon type npc (Register NPCs)"
        }
        if extra_ext:
            ext.update(extra_ext)
        lb = {
            "name": name,
            "description": desc,
            "scan_depth": 5,
            "token_budget": 2048,
            "recursive_scanning": True,
            "visibility": "private",
            "rating": "explicit",
            "status": "approved",
            "tags": ["SvartulfrVerse", "Lexicon", "NPC", "G3"],
            "counts": {"total": len(entries_list)},
            "entries": reindex_entries(entries_list),
            "extensions": ext
        }
        filepath = os.path.join(entities_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(lb, f, indent=2, ensure_ascii=False)
        print(f"Exported Lorebook: {filepath} ({len(entries_list)} entries)")

    # Complete G3 NPC Lorebook
    write_lorebook_file(
        "Svartulfr_Lexicon_NPCs_G3.json",
        "Svartúlfr - Lexicon NPCs (G3 Complete)",
        f"Raccolta completa NPC di fondo G3 ({len(g3_converted_all)} voci) registrati con Lexicon type: npc",
        g3_converted_all
    )

    # G3-A Real
    write_lorebook_file(
        "Svartulfr_Lexicon_NPCs_G3_A_Real.json",
        "Svartúlfr - Lexicon NPCs (G3-A Real Characters)",
        f"Personaggi secondari G3 con schede reali ({len(g3_converted_a)} voci) registrati con Lexicon type: npc",
        g3_converted_a
    )

    # G3-B Stubs
    write_lorebook_file(
        "Svartulfr_Lexicon_NPCs_G3_B_Stubs.json",
        "Svartúlfr - Lexicon NPCs (G3-B Stubs)",
        f"Placeholder e comparse minori G3 ({len(g3_converted_b)} voci) registrati con Lexicon type: npc",
        g3_converted_b
    )

    # Split complete G3 into parts <= 250 entries for direct Wyvern Import
    MAX_LOREBOOK_ENTRIES = 250
    if len(g3_converted_all) > MAX_LOREBOOK_ENTRIES:
        num_parts = (len(g3_converted_all) + MAX_LOREBOOK_ENTRIES - 1) // MAX_LOREBOOK_ENTRIES
        chunk_size = (len(g3_converted_all) + num_parts - 1) // num_parts
        for p_idx in range(num_parts):
            p_num = p_idx + 1
            start = p_idx * chunk_size
            end = min((p_idx + 1) * chunk_size, len(g3_converted_all))
            chunk = g3_converted_all[start:end]
            write_lorebook_file(
                f"Svartulfr_Lexicon_NPCs_G3_Part{p_num}.json",
                f"Svartúlfr - Lexicon NPCs (G3 Part {p_num})",
                f"NPC di fondo G3 - Parte {p_num} di {num_parts} ({chunk[0]['name']} - {chunk[-1]['name']})",
                chunk,
                {"part": p_num, "total_parts": num_parts}
            )

    print("\n=== G3 TO LEXICON CONVERSION COMPLETE ===")
    print(f"Total G3 NPCs Converted: {len(g3_converted_all)}")
    print(f"  - G3-A Real Secondary: {len(g3_converted_a)}")
    print(f"  - G3-B Minor Stubs:    {len(g3_converted_b)}")

if __name__ == '__main__':
    convert_g3_characters()
