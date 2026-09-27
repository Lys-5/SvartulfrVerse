import json
import os

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
            # Fallback if comma-separated
            if default is not None and isinstance(default, list):
                return [x.strip() for x in val.split(',') if x.strip()]
            return val
    return default if default is not None else []

def convert_svartulfr():
    src_path = r'd:\SvartulfrVerse\Svartulfr_Export.json'
    if not os.path.exists(src_path):
        src_path = r'c:\Users\mande\AppData\Local\com.wyvern.wyldfire\Svartulfr_Export.json'

    with open(src_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    world = raw_data.get('world', {})
    raw_characters = raw_data.get('world_characters', [])
    raw_lexicon = raw_data.get('world_lexicon_entries', [])
    raw_locations = raw_data.get('world_locations', [])
    raw_environments = raw_data.get('world_environments', [])
    raw_scenarios = raw_data.get('world_scenarios', [])

    lorebook_name = world.get('name') or "SvartülfrVerse"
    description = world.get('context_description') or world.get('base_instructions') or ""
    scan_depth = world.get('scan_depth') or 5
    rating = world.get('rating') or "explicit"
    visibility = "private"

    converted_entries = []
    uid_counter = 0

    lexicon_converted = []
    characters_converted = []
    locations_converted = []
    environments_converted = []
    scenarios_converted = []

    # 1. Process Lexicon Entries (250)
    for item in raw_lexicon:
        keys = parse_json_field(item.get('keys'), [])
        sec_keys = parse_json_field(item.get('secondary_keys'), [])
        extensions = parse_json_field(item.get('extensions'), {})
        if not isinstance(extensions, dict):
            extensions = {}

        name = item.get('name') or f"Lexicon_{uid_counter}"
        content = item.get('content') or ""
        enabled = bool(item.get('enabled', 1))
        constant = bool(item.get('constant', 0))
        case_sensitive = bool(item.get('case_sensitive', 0))
        whole_words_only = bool(item.get('whole_words_only', 1))
        scan_persona = bool(item.get('scan_persona', 0))
        priority = item.get('priority') if item.get('priority') is not None else 10
        insertion_order = item.get('insertion_order') if item.get('insertion_order') is not None else 100
        position = item.get('position') or "before_char"
        key_logic = item.get('key_logic') or "AND_ANY"
        entry_id = item.get('id') or f"lex_{uid_counter}"
        comment = item.get('comment') or name
        delay = item.get('delay')
        sticky = item.get('sticky')
        cooldown = item.get('cooldown')
        entry_type = item.get('type') or "concept"

        logic_map = {"AND_ANY": 0, "AND_ALL": 1, "NOT_ANY": 2, "NOT_ALL": 3}
        selective_logic = logic_map.get(key_logic, 0)

        converted_entries.append({
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": comment,
            "keys": keys,
            "key": keys,
            "secondary_keys": sec_keys,
            "keysecondary": sec_keys,
            "key_logic": key_logic,
            "selectiveLogic": selective_logic,
            "selective": len(sec_keys) > 0,
            "content": content,
            "enabled": enabled,
            "disable": not enabled,
            "constant": constant,
            "position": position,
            "priority": priority,
            "insertion_order": insertion_order,
            "order": insertion_order,
            "case_sensitive": case_sensitive,
            "caseSensitive": case_sensitive,
            "whole_words_only": whole_words_only,
            "matchWholeWords": whole_words_only,
            "scan_persona": scan_persona,
            "matchPersonaDescription": scan_persona,
            "delay": delay if delay is not None else 0,
            "sticky": sticky if sticky is not None else 0,
            "cooldown": cooldown if cooldown is not None else 0,
            "type": entry_type,
            "source_category": "lexicon",
            "extensions": {
                **extensions,
                "wyvern": {
                    "priority": priority,
                    "position": position,
                    "insertion_order": insertion_order,
                    "type": entry_type
                }
            }
        })

        lexicon_converted.append(converted_entries[-1])
        uid_counter += 1

    # 2. Process Characters (360)
    for char in raw_characters:
        name = char.get('display_name') or f"{char.get('first_name', '')} {char.get('last_name', '')}".strip() or char.get('id')
        keys = parse_json_field(char.get('keys'), [])
        if not keys:
            keys = [name]
            nicknames = parse_json_field(char.get('nicknames'), [])
            if nicknames and isinstance(nicknames, list):
                keys.extend(nicknames)

        sec_keys = parse_json_field(char.get('secondary_keys'), [])
        key_logic = char.get('key_logic') or "AND_ANY"
        logic_map = {"AND_ANY": 0, "AND_ALL": 1, "NOT_ANY": 2, "NOT_ALL": 3}
        selective_logic = logic_map.get(key_logic, 0)

        content = char.get('long_summary') or char.get('summary') or ""
        final_inst = char.get('final_instructions')
        if final_inst and final_inst.strip() and final_inst.strip() not in content:
            content = f"{content}\n\n[INSTRUCTIONS: {final_inst.strip()}]"

        entry_id = char.get('id') or f"char_{uid_counter}"

        converted_entries.append({
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": f"Character: {name}",
            "keys": keys,
            "key": keys,
            "secondary_keys": sec_keys,
            "keysecondary": sec_keys,
            "key_logic": key_logic,
            "selectiveLogic": selective_logic,
            "selective": len(sec_keys) > 0,
            "content": content,
            "enabled": True,
            "disable": False,
            "constant": False,
            "position": "before_char",
            "priority": 10,
            "insertion_order": 100,
            "order": 100,
            "case_sensitive": bool(char.get('case_sensitive', 0)),
            "caseSensitive": bool(char.get('case_sensitive', 0)),
            "whole_words_only": bool(char.get('whole_words_only', 1)),
            "matchWholeWords": bool(char.get('whole_words_only', 1)),
            "scan_persona": False,
            "matchPersonaDescription": False,
            "delay": 0,
            "sticky": 0,
            "cooldown": 0,
            "type": "npc",
            "source_category": "characters",
            "extensions": {
                "character_meta": {
                    "first_name": char.get('first_name'),
                    "last_name": char.get('last_name'),
                    "nicknames": parse_json_field(char.get('nicknames'), []),
                    "titles": parse_json_field(char.get('titles'), []),
                    "pronouns": char.get('pronouns'),
                    "species_id": char.get('species_id'),
                    "occupation_id": char.get('occupation_id'),
                    "is_global": bool(char.get('is_global', 1)),
                    "outfits": parse_json_field(char.get('outfits'), []),
                    "speech_examples": parse_json_field(char.get('speech_examples'), []),
                    "rpg_stats": parse_json_field(char.get('rpg_stats'), {}),
                    "tags": parse_json_field(char.get('tags'), [])
                },
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "npc"
                }
            }
        })

        characters_converted.append(converted_entries[-1])
        uid_counter += 1

    # 3. Process Locations (119)
    for loc in raw_locations:
        name = loc.get('name') or loc.get('id')
        keys = [name]
        tags = parse_json_field(loc.get('tags'), [])
        for t in tags:
            if isinstance(t, str) and t.strip() and t.strip() not in keys:
                keys.append(t.strip())

        content = loc.get('context_description') or loc.get('description') or ""
        final_inst = loc.get('final_instructions')
        if final_inst and final_inst.strip() and final_inst.strip() not in content:
            content = f"{content}\n\n[LOCATION INSTRUCTIONS: {final_inst.strip()}]"

        entry_id = loc.get('id') or f"loc_{uid_counter}"

        converted_entries.append({
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": f"Location: {name}",
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
            "priority": 10,
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
            "type": "location",
            "source_category": "locations",
            "extensions": {
                "parent_location_id": loc.get('parent_location_id'),
                "environment_id": loc.get('environment_id'),
                "tags": tags,
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "location"
                }
            }
        })

        locations_converted.append(converted_entries[-1])
        uid_counter += 1

    # 4. Process Environments (13)
    for env in raw_environments:
        name = env.get('name') or env.get('id')
        keys = [name]
        tags = parse_json_field(env.get('tags'), [])
        for t in tags:
            if isinstance(t, str) and t.strip() and t.strip() not in keys:
                keys.append(t.strip())

        content = env.get('context_description') or env.get('description') or ""
        final_inst = env.get('final_instructions')
        if final_inst and final_inst.strip() and final_inst.strip() not in content:
            content = f"{content}\n\n[ENVIRONMENT INSTRUCTIONS: {final_inst.strip()}]"

        entry_id = env.get('id') or f"env_{uid_counter}"

        converted_entries.append({
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": f"Environment: {name}",
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
            "priority": 10,
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
            "type": "location",
            "source_category": "environments",
            "extensions": {
                "tags": tags,
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "location"
                }
            }
        })

        environments_converted.append(converted_entries[-1])
        uid_counter += 1

    # 5. Process Scenarios (3)
    for scen in raw_scenarios:
        name = scen.get('name') or scen.get('id')
        keys = [name]
        tags = parse_json_field(scen.get('tags'), [])
        for t in tags:
            if isinstance(t, str) and t.strip() and t.strip() not in keys:
                keys.append(t.strip())

        content = scen.get('description') or ""
        scene_inst = scen.get('scene_instructions')
        if scene_inst and scene_inst.strip() and scene_inst.strip() not in content:
            content = f"{content}\n\n[SCENARIO INSTRUCTIONS: {scene_inst.strip()}]"

        entry_id = scen.get('id') or f"scen_{uid_counter}"

        converted_entries.append({
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": f"Scenario: {name}",
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
            "priority": 10,
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
            "type": "event",
            "source_category": "scenarios",
            "extensions": {
                "environment_id": scen.get('environment_id'),
                "location_id": scen.get('location_id'),
                "tags": tags,
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "event"
                }
            }
        })

        scenarios_converted.append(converted_entries[-1])
        uid_counter += 1

    # Helper to reindex entries per file
    def reindex_entries(entries_list):
        reindexed = []
        for i, entry in enumerate(entries_list):
            e = dict(entry)
            e['uid'] = i
            reindexed.append(e)
        return reindexed

    # Save Unified Lorebook Complete JSON (Full Archive)
    wyvern_lorebook_complete = {
        "name": f"{lorebook_name} (Complete)",
        "description": description,
        "scan_depth": scan_depth,
        "token_budget": 2048,
        "recursive_scanning": True,
        "visibility": visibility,
        "rating": rating,
        "status": "approved",
        "tags": ["SvartulfrVerse", "World", "Urban Fantasy", "Werewolves"],
        "counts": {
            "total": len(converted_entries),
            "characters": len(raw_characters),
            "lexicon": len(raw_lexicon),
            "locations": len(raw_locations),
            "environments": len(raw_environments),
            "scenarios": len(raw_scenarios)
        },
        "entries": reindex_entries(converted_entries),
        "extensions": {
            "creator": "Wyldfire",
            "source_world_id": world.get('id', '')
        }
    }

    out_json_path_complete = r'd:\SvartulfrVerse\Svartulfr_Lorebook_Complete.json'
    with open(out_json_path_complete, 'w', encoding='utf-8') as f:
        json.dump(wyvern_lorebook_complete, f, indent=2, ensure_ascii=False)
    print(f"Saved Unified Complete JSON Lorebook to: {out_json_path_complete} ({len(converted_entries)} entries)")

    # Also save Svartulfr_Lorebook.json as Complete master copy
    out_json_path_master = r'd:\SvartulfrVerse\Svartulfr_Lorebook.json'
    with open(out_json_path_master, 'w', encoding='utf-8') as f:
        json.dump(wyvern_lorebook_complete, f, indent=2, ensure_ascii=False)

    # Save Unified Lorebook Parts (<= 250 entries each) for Wyvern import
    MAX_LOREBOOK_ENTRIES = 250
    if len(converted_entries) > MAX_LOREBOOK_ENTRIES:
        num_parts = (len(converted_entries) + MAX_LOREBOOK_ENTRIES - 1) // MAX_LOREBOOK_ENTRIES
        chunk_size = (len(converted_entries) + num_parts - 1) // num_parts
        for part_idx in range(num_parts):
            start = part_idx * chunk_size
            end = min((part_idx + 1) * chunk_size, len(converted_entries))
            sub_entries = converted_entries[start:end]
            part_num = part_idx + 1
            part_lorebook = {
                "name": f"{lorebook_name} (Part {part_num})",
                "description": f"{description} - Parte {part_num} di {num_parts}",
                "scan_depth": scan_depth,
                "token_budget": 2048,
                "recursive_scanning": True,
                "visibility": visibility,
                "rating": rating,
                "status": "approved",
                "tags": ["SvartulfrVerse", "World", f"Part {part_num}"],
                "counts": {"total": len(sub_entries)},
                "entries": reindex_entries(sub_entries),
                "extensions": {
                    "creator": "Wyldfire",
                    "source_world_id": world.get('id', ''),
                    "part": part_num,
                    "total_parts": num_parts
                }
            }
            part_path = rf'd:\SvartulfrVerse\Svartulfr_Lorebook_Part{part_num}.json'
            with open(part_path, 'w', encoding='utf-8') as f:
                json.dump(part_lorebook, f, indent=2, ensure_ascii=False)
            print(f"Saved Unified Lorebook Part {part_num}: {part_path} ({len(sub_entries)} entries)")

    # Generate Clean Modular Exports (Fully Valid Individual Lorebooks)
    exports_dir = r'd:\SvartulfrVerse\exports'
    os.makedirs(exports_dir, exist_ok=True)
    raw_dumps_dir = os.path.join(exports_dir, 'raw_db_dumps')
    os.makedirs(raw_dumps_dir, exist_ok=True)

    # Save raw database dumps in raw_db_dumps/
    clean_chars = []
    for c in raw_characters:
        item = dict(c)
        for field in ['keys', 'secondary_keys', 'nicknames', 'titles', 'outfits', 'speech_examples', 'rpg_stats', 'tags', 'default_inventory', 'default_creatures', 'battle_rewards']:
            if field in item:
                item[field] = parse_json_field(item[field], {} if 'stats' in field else [])
        clean_chars.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_characters.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_chars, f, indent=2, ensure_ascii=False)

    clean_locs = []
    for l in raw_locations:
        item = dict(l)
        for field in ['tags', 'included_lexicon_entries', 'excluded_lexicon_entries', 'linked_character_pool', 'included_character_pool', 'environment_config']:
            if field in item:
                item[field] = parse_json_field(item[field], [])
        clean_locs.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_locations.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_locs, f, indent=2, ensure_ascii=False)

    clean_envs = []
    for e in raw_environments:
        item = dict(e)
        for field in ['tags', 'included_lexicon_entries', 'excluded_lexicon_entries', 'linked_character_pool', 'included_character_pool', 'environment_config']:
            if field in item:
                item[field] = parse_json_field(item[field], [])
        clean_envs.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_environments.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_envs, f, indent=2, ensure_ascii=False)

    clean_scens = []
    for s in raw_scenarios:
        item = dict(s)
        for field in ['tags', 'linked_character_pool', 'included_character_pool', 'premade_scenes', 'fields', 'starting_inventory', 'starting_creatures', 'starting_currency', 'playable_character_ids']:
            if field in item:
                item[field] = parse_json_field(item[field], [])
        clean_scens.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_scenarios.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_scens, f, indent=2, ensure_ascii=False)

    clean_lex = []
    for lx in raw_lexicon:
        item = dict(lx)
        for field in ['keys', 'secondary_keys', 'extensions']:
            if field in item:
                item[field] = parse_json_field(item[field], {} if field == 'extensions' else [])
        clean_lex.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_lexicon.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_lex, f, indent=2, ensure_ascii=False)

    # Modular Lorebook Helper
    def export_lorebook_file(filename, name, desc, tag, entries_list, extra_ext=None):
        ext = {
            "creator": "Wyldfire",
            "source_world_id": world.get('id', '')
        }
        if extra_ext:
            ext.update(extra_ext)
        lb = {
            "name": name,
            "description": desc,
            "scan_depth": scan_depth,
            "token_budget": 2048,
            "recursive_scanning": True,
            "visibility": visibility,
            "rating": rating,
            "status": "approved",
            "tags": ["SvartulfrVerse", tag],
            "counts": {
                "total": len(entries_list)
            },
            "entries": reindex_entries(entries_list),
            "extensions": ext
        }
        filepath = os.path.join(exports_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(lb, f, indent=2, ensure_ascii=False)
        print(f"Exported valid Lorebook: {filepath} ({len(entries_list)} entries)")

    # 1. Characters (360 entries -> Split into 2 parts of 180 entries each, plus complete backup)
    char_mid = len(characters_converted) // 2
    chars_p1 = characters_converted[:char_mid]
    chars_p2 = characters_converted[char_mid:]

    export_lorebook_file(
        "Svartulfr_Characters_Part1.json",
        "Svartúlfr - Characters (Part 1)",
        f"Personaggi e NPC del mondo Svartúlfr - Parte 1 di 2 ({chars_p1[0]['name']} - {chars_p1[-1]['name']})",
        "Characters",
        chars_p1,
        {"part": 1, "total_parts": 2}
    )

    export_lorebook_file(
        "Svartulfr_Characters_Part2.json",
        "Svartúlfr - Characters (Part 2)",
        f"Personaggi e NPC del mondo Svartúlfr - Parte 2 di 2 ({chars_p2[0]['name']} - {chars_p2[-1]['name']})",
        "Characters",
        chars_p2,
        {"part": 2, "total_parts": 2}
    )

    export_lorebook_file(
        "Svartulfr_Characters_Complete.json",
        "Svartúlfr - Characters (Complete Archive)",
        "Personaggi e NPC del mondo Svartúlfr - Raccolta completa non splittata (360 personaggi)",
        "Characters",
        characters_converted
    )

    # 2. Lexicon (250 entries -> Unified file + 2 parts of 125 entries each)
    export_lorebook_file(
        "Svartulfr_Lexicon.json",
        "Svartúlfr - Lexicon",
        "Voci di lore, magia, fazioni e storia di Svartúlfr (Completo, 250 voci)",
        "Lexicon",
        lexicon_converted
    )

    lex_mid = len(lexicon_converted) // 2
    lex_p1 = lexicon_converted[:lex_mid]
    lex_p2 = lexicon_converted[lex_mid:]

    export_lorebook_file(
        "Svartulfr_Lexicon_Part1.json",
        "Svartúlfr - Lexicon (Part 1)",
        f"Voci di lore, magia, fazioni e storia - Parte 1 di 2 ({lex_p1[0]['name']} - {lex_p1[-1]['name']})",
        "Lexicon",
        lex_p1,
        {"part": 1, "total_parts": 2}
    )

    export_lorebook_file(
        "Svartulfr_Lexicon_Part2.json",
        "Svartúlfr - Lexicon (Part 2)",
        f"Voci di lore, magia, fazioni e storia - Parte 2 di 2 ({lex_p2[0]['name']} - {lex_p2[-1]['name']})",
        "Lexicon",
        lex_p2,
        {"part": 2, "total_parts": 2}
    )

    # 3. Locations (119 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Locations.json",
        "Svartúlfr - Locations",
        "Luoghi e distretti dettagliati di Svartúlfr",
        "Locations",
        locations_converted
    )

    # 4. Environments (13 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Environments.json",
        "Svartúlfr - Environments",
        "Macro-ambienti di Svartúlfr",
        "Environments",
        environments_converted
    )

    # 5. Scenarios (3 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Scenarios.json",
        "Svartúlfr - Scenarios",
        "Scenari iniziali e aperture narrative di Svartúlfr",
        "Scenarios",
        scenarios_converted
    )

    print("\n=== CONVERSION SUMMARY ===")
    print(f"Total processed: {uid_counter} items")
    print(f"  - Characters:   {len(characters_converted)} (Exported as Part1: {len(chars_p1)}, Part2: {len(chars_p2)}, Complete: {len(characters_converted)})")
    print(f"  - Lexicon:      {len(lexicon_converted)} (Exported as Full: {len(lexicon_converted)}, Part1: {len(lex_p1)}, Part2: {len(lex_p2)})")
    print(f"  - Locations:    {len(locations_converted)}")
    print(f"  - Environments: {len(environments_converted)}")
    print(f"  - Scenarios:    {len(scenarios_converted)}")

if __name__ == '__main__':
    convert_svartulfr()
