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
            if default is not None and isinstance(default, list):
                return [x.strip() for x in val.split(',') if x.strip()]
            return val
    return default if default is not None else []

def convert_svartulfr():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = os.path.join(base_dir, 'exports', 'Svartulfr_Export.json')
    if not os.path.exists(src_path):
        src_path = os.path.join(base_dir, 'Svartulfr_Export.json')

    with open(src_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    world = raw_data.get('world', {})
    raw_characters = raw_data.get('world_characters', [])
    raw_lexicon = raw_data.get('world_lexicon_entries', [])
    raw_locations = raw_data.get('world_locations', [])
    raw_environments = raw_data.get('world_environments', [])
    raw_scenarios = raw_data.get('world_scenarios', [])
    raw_maps = raw_data.get('world_maps', [])
    raw_eras = raw_data.get('world_eras', [])

    lorebook_name = world.get('name') or "SvartülfrVerse"
    description = world.get('context_description') or world.get('base_instructions') or "Svartúlfr World Lorebook"
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
    maps_converted = []
    eras_converted = []

    logic_map = {"AND_ANY": 0, "AND_ALL": 1, "NOT_ANY": 2, "NOT_ALL": 3}

    # 1. Process Lexicon Entries
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

        selective_logic = logic_map.get(key_logic, 0)

        entry_obj = {
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
                "attached_world_character_id": item.get('attached_world_character_id'),
                "party_conditions": parse_json_field(item.get('party_conditions'), []),
                "wyvern": {
                    "priority": priority,
                    "position": position,
                    "insertion_order": insertion_order,
                    "type": entry_type
                }
            }
        }
        converted_entries.append(entry_obj)
        lexicon_converted.append(entry_obj)
        uid_counter += 1

    # 2. Process Characters
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
        selective_logic = logic_map.get(key_logic, 0)

        # Prioritize long_summary (rich JED+)
        content = char.get('long_summary') or char.get('summary') or ""
        final_inst = char.get('final_instructions')
        if final_inst and final_inst.strip() and final_inst.strip() not in content:
            content = f"{content}\n\n[INSTRUCTIONS: {final_inst.strip()}]"

        entry_id = char.get('id') or f"char_{uid_counter}"

        outfits = parse_json_field(char.get('outfits'), [])
        speech_examples = parse_json_field(char.get('speech_examples'), [])
        attitudes = parse_json_field(char.get('attitudes'), [])
        rpg_stats = parse_json_field(char.get('rpg_stats'), {})

        entry_obj = {
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
                    "birthdate": char.get('birthdate'),
                    "start_timeline_position": char.get('start_timeline_position'),
                    "summary": char.get('summary'),
                    "display_description": char.get('display_description'),
                    "outfits": outfits,
                    "speech_examples": speech_examples,
                    "attitudes": attitudes,
                    "rpg_stats": rpg_stats,
                    "tags": parse_json_field(char.get('tags'), [])
                },
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "npc"
                }
            }
        }
        converted_entries.append(entry_obj)
        characters_converted.append(entry_obj)
        uid_counter += 1

    # 3. Process Locations
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

        entry_obj = {
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
                "included_lexicon_entries": parse_json_field(loc.get('included_lexicon_entries'), []),
                "excluded_lexicon_entries": parse_json_field(loc.get('excluded_lexicon_entries'), []),
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "location"
                }
            }
        }
        converted_entries.append(entry_obj)
        locations_converted.append(entry_obj)
        uid_counter += 1

    # 4. Process Environments
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

        entry_obj = {
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
                "included_lexicon_entries": parse_json_field(env.get('included_lexicon_entries'), []),
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "location"
                }
            }
        }
        converted_entries.append(entry_obj)
        environments_converted.append(entry_obj)
        uid_counter += 1

    # 5. Process Scenarios
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

        entry_obj = {
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
                "premade_scenes": parse_json_field(scen.get('premade_scenes'), []),
                "tags": tags,
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "event"
                }
            }
        }
        converted_entries.append(entry_obj)
        scenarios_converted.append(entry_obj)
        uid_counter += 1

    # 6. Process Maps
    for m in raw_maps:
        name = m.get('name') or m.get('id')
        keys = [name, f"Map of {name}", f"Mappa di {name}"]
        tags = parse_json_field(m.get('tags'), [])
        for t in tags:
            if isinstance(t, str) and t.strip() and t.strip() not in keys:
                keys.append(t.strip())

        content = m.get('description') or f"Cartographic map of {name}."
        if m.get('image_url'):
            content += f"\nMap Asset: {m.get('image_url')}"

        entry_id = m.get('id') or f"map_{uid_counter}"

        entry_obj = {
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": f"Map: {name}",
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
            "source_category": "maps",
            "extensions": {
                "map_type": m.get('map_type'),
                "image_url": m.get('image_url'),
                "pins": parse_json_field(m.get('pins'), []),
                "connections": parse_json_field(m.get('connections'), []),
                "tags": tags,
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "location"
                }
            }
        }
        converted_entries.append(entry_obj)
        maps_converted.append(entry_obj)
        uid_counter += 1

    # 7. Process Eras
    for era in raw_eras:
        name = era.get('name') or era.get('id')
        keys = [name, f"{name} Era", "Timeline Era"]
        tags = parse_json_field(era.get('tags'), [])
        for t in tags:
            if isinstance(t, str) and t.strip() and t.strip() not in keys:
                keys.append(t.strip())

        content = f"[{name.upper()}]\n"
        if era.get('start_position') is not None:
            content += f"Timeline Hours Range: {era.get('start_position')} to {era.get('end_position') if era.get('end_position') is not None else 'Current World Age'}\n"
        if era.get('description'):
            content += f"\nDescription: {era.get('description')}\n"
        if era.get('context_description'):
            content += f"\nContext: {era.get('context_description')}\n"
        if era.get('final_instructions'):
            content += f"\n[ERA INSTRUCTIONS: {era.get('final_instructions')}]\n"

        entry_id = era.get('id') or f"era_{uid_counter}"

        entry_obj = {
            "entry_id": entry_id,
            "id": entry_id,
            "uid": uid_counter,
            "name": name,
            "comment": f"Timeline Era: {name}",
            "keys": keys,
            "key": keys,
            "secondary_keys": [],
            "keysecondary": [],
            "key_logic": "AND_ANY",
            "selectiveLogic": 0,
            "selective": False,
            "content": content.strip(),
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
            "type": "concept",
            "source_category": "eras",
            "extensions": {
                "start_position": era.get('start_position'),
                "end_position": era.get('end_position'),
                "color": era.get('color'),
                "display_order": era.get('display_order'),
                "tags": tags,
                "wyvern": {
                    "priority": 10,
                    "position": "before_char",
                    "insertion_order": 100,
                    "type": "concept"
                }
            }
        }
        converted_entries.append(entry_obj)
        eras_converted.append(entry_obj)
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
            "scenarios": len(raw_scenarios),
            "maps": len(raw_maps),
            "eras": len(raw_eras)
        },
        "entries": reindex_entries(converted_entries),
        "extensions": {
            "creator": "Wyvern Web API Sync",
            "source_world_id": world.get('id', '')
        }
    }

    lorebooks_dir = os.path.join(base_dir, 'exports', 'lorebooks')
    os.makedirs(lorebooks_dir, exist_ok=True)

    out_json_path_complete = os.path.join(lorebooks_dir, 'Svartulfr_Lorebook_Complete.json')
    with open(out_json_path_complete, 'w', encoding='utf-8') as f:
        json.dump(wyvern_lorebook_complete, f, indent=2, ensure_ascii=False)
    print(f"Saved Unified Complete JSON Lorebook to: {out_json_path_complete} ({len(converted_entries)} entries)")

    # Also save Svartulfr_Lorebook.json as Complete master copy
    out_json_path_master = os.path.join(lorebooks_dir, 'Svartulfr_Lorebook.json')
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
                    "creator": "Wyvern Web API Sync",
                    "source_world_id": world.get('id', ''),
                    "part": part_num,
                    "total_parts": num_parts
                }
            }
            part_path = os.path.join(lorebooks_dir, f'Svartulfr_Lorebook_Part{part_num}.json')
            with open(part_path, 'w', encoding='utf-8') as f:
                json.dump(part_lorebook, f, indent=2, ensure_ascii=False)
            print(f"Saved Unified Lorebook Part {part_num}: {part_path} ({len(sub_entries)} entries)")

    # Save Raw Database Dumps in exports/raw_db_dumps/
    exports_dir = os.path.join(base_dir, 'exports')
    raw_dumps_dir = os.path.join(exports_dir, 'raw_db_dumps')
    entities_dir = os.path.join(exports_dir, 'entities')
    os.makedirs(raw_dumps_dir, exist_ok=True)
    os.makedirs(entities_dir, exist_ok=True)

    with open(os.path.join(raw_dumps_dir, 'raw_world.json'), 'w', encoding='utf-8') as f:
        json.dump(world, f, indent=2, ensure_ascii=False)

    clean_chars = []
    for c in raw_characters:
        item = dict(c)
        for field in ['keys', 'secondary_keys', 'nicknames', 'titles', 'outfits', 'speech_examples', 'attitudes', 'rpg_stats', 'tags', 'community_tags', 'default_inventory', 'default_creatures', 'gallery_images', 'character_traits']:
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
        for field in ['keys', 'secondary_keys', 'extensions', 'party_conditions']:
            if field in item:
                item[field] = parse_json_field(item[field], {} if field == 'extensions' else [])
        clean_lex.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_lexicon.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_lex, f, indent=2, ensure_ascii=False)

    clean_maps = []
    for m in raw_maps:
        item = dict(m)
        for field in ['tags', 'pins', 'connections']:
            if field in item:
                item[field] = parse_json_field(item[field], [])
        clean_maps.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_maps.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_maps, f, indent=2, ensure_ascii=False)

    clean_eras = []
    for er in raw_eras:
        item = dict(er)
        for field in ['tags', 'type_effectiveness']:
            if field in item:
                item[field] = parse_json_field(item[field], [])
        clean_eras.append(item)
    with open(os.path.join(raw_dumps_dir, 'raw_eras.json'), 'w', encoding='utf-8') as f:
        json.dump(clean_eras, f, indent=2, ensure_ascii=False)

    # Modular Lorebook Helper
    def export_lorebook_file(filename, name, desc, tag, entries_list, extra_ext=None):
        ext = {
            "creator": "Wyvern Web API Sync",
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
        filepath = os.path.join(entities_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(lb, f, indent=2, ensure_ascii=False)
        print(f"Exported valid Lorebook: {filepath} ({len(entries_list)} entries)")

    # 1. Characters (365 entries -> Split into 2 parts: 183 and 182, plus complete archive)
    char_mid = (len(characters_converted) + 1) // 2
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
        f"Personaggi e NPC del mondo Svartúlfr - Raccolta completa non splittata ({len(characters_converted)} personaggi)",
        "Characters",
        characters_converted
    )

    # 2. Lexicon (254 entries -> Unified file + 2 parts of 127 entries each)
    export_lorebook_file(
        "Svartulfr_Lexicon.json",
        "Svartúlfr - Lexicon",
        f"Voci di lore, magia, fazioni e storia di Svartúlfr (Completo, {len(lexicon_converted)} voci)",
        "Lexicon",
        lexicon_converted
    )

    lex_mid = (len(lexicon_converted) + 1) // 2
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

    # 3. Locations (135 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Locations.json",
        "Svartúlfr - Locations",
        "Luoghi e distretti dettagliati di Svartúlfr",
        "Locations",
        locations_converted
    )

    # 4. Environments (2 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Environments.json",
        "Svartúlfr - Environments",
        "Macro-ambienti di Svartúlfr",
        "Environments",
        environments_converted
    )

    # 5. Scenarios (9 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Scenarios.json",
        "Svartúlfr - Scenarios",
        "Scenari iniziali e aperture narrative di Svartúlfr",
        "Scenarios",
        scenarios_converted
    )

    # 6. Maps (2 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Maps.json",
        "Svartúlfr - Maps",
        "Mappe cartografiche e collegamenti geografici di Svartúlfr",
        "Maps",
        maps_converted
    )

    # 7. Eras (7 entries <= 250)
    export_lorebook_file(
        "Svartulfr_Eras.json",
        "Svartúlfr - Eras",
        "Ere storiche e suddivisione cronologica del World Clock di Svartúlfr",
        "Eras",
        eras_converted
    )

    print("\n=== CONVERSION SUMMARY ===")
    print(f"Total processed: {uid_counter} items")
    print(f"  - Characters:   {len(characters_converted)} (Part1: {len(chars_p1)}, Part2: {len(chars_p2)}, Complete: {len(characters_converted)})")
    print(f"  - Lexicon:      {len(lexicon_converted)} (Part1: {len(lex_p1)}, Part2: {len(lex_p2)}, Complete: {len(lexicon_converted)})")
    print(f"  - Locations:    {len(locations_converted)}")
    print(f"  - Environments: {len(environments_converted)}")
    print(f"  - Scenarios:    {len(scenarios_converted)}")
    print(f"  - Maps:         {len(maps_converted)}")
    print(f"  - Eras:         {len(eras_converted)}")

if __name__ == '__main__':
    convert_svartulfr()
